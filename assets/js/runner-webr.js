/* runner-webr.js — esegue R nel browser con webR (https://docs.r-wasm.org/webr/).
   Espone window.CBDRunner = { ready, run(code), evalTests(code, tests, opts) }.
   Canale PostMessage: non richiede header COOP/COEP, quindi funziona su GitHub Pages.   */
import { WebR, ChannelType } from 'https://webr.r-wasm.org/latest/webr.mjs';

const root = document.querySelector('.lab[data-lab]');
const statusEl = document.querySelector('[data-runtime-status]');
const setStatus = (t, cls) => { if (statusEl) { statusEl.textContent = t; statusEl.className = 'bench__runtime ' + (cls || ''); } };

const webR = new WebR({ channelType: ChannelType.PostMessage });
let shelter = null;

const ready = (async () => {
  setStatus('carico R nel browser…', 'is-loading');
  await webR.init();
  shelter = await new webR.Shelter();
  // pacchetti richiesti dal lab (es. dplyr): installati dal repository webR
  const pk = (root && root.dataset.packages) ? root.dataset.packages.split(',').filter(Boolean) : [];
  if (pk.length) { setStatus('installo ' + pk.join(', ') + '…', 'is-loading'); await webR.installPackages(pk, { quiet: true }); }
  // dataset del lab: scaricato e scritto nel filesystem virtuale, poi letto con read.csv
  if (root && root.dataset.dataUrl) {
    setStatus('scarico i dati…', 'is-loading');
    const buf = await (await fetch(root.dataset.dataUrl)).arrayBuffer();
    await webR.FS.writeFile('/home/web_user/dati.csv', new Uint8Array(buf));
  }
  setStatus('R pronto ✓', 'is-ready');
})().catch(e => { setStatus('R non disponibile: ' + e, ''); throw e; });

/* prologo comune: carica i dati nella variabile attesa dal lab */
function prologue() {
  if (root && root.dataset.dataUrl) return `${root.dataset.dataVar || 'data'} <- read.csv("/home/web_user/dati.csv")\n`;
  return '';
}

/* esecuzione libera: restituisce output della console (stdout+stderr) o errore */
async function run(code) {
  await ready;
  try {
    const res = await shelter.captureR(prologue() + code, { withAutoprint: true, captureStreams: true, captureConditions: false });
    const out = res.output.map(o => o.data).join('\n');
    return { output: out };
  } catch (e) {
    return { error: cleanError(e) };
  } finally { shelter.purge(); }
}

/* valuta i test: per ogni caso, assegna gli input, esegue il codice in un ambiente nuovo, legge l'output */
async function evalTests(code, tests, opts) {
  await ready;
  const results = [];
  for (const t of tests) {
    const assign = Object.entries(t.inputs || {}).map(([k, v]) => `${k} <- ${toR(v)}`).join('\n');
    let expr;
    if (opts.fn) {
      // lab "funzione": il codice definisce fn; il test la chiama con gli input nell'ordine dichiarato
      const args = (opts.inputs || []).map(n => toR(t.inputs[n])).join(', ');
      expr = `${prologue()}${code}\n.__out <- ${opts.fn}(${args})`;
    } else {
      expr = `${prologue()}${assign}\n${code}\n.__out <- ${opts.outputVar}`;
    }
    try {
      await webR.objs.globalEnv.bind('.codice', expr);
      const val = await webR.evalRString(
        `.env <- new.env(); eval(parse(text = .codice), envir = .env); ` +
        `.v <- get('.__out', envir = .env); if (is.null(.v)) '' else paste(as.character(.v), collapse = ', ')`
      );
      results.push({ obtained: val });
    } catch (e) {
      results.push({ error: cleanError(e), obtained: null });
    }
  }
  return results;
}

function toR(v) {
  if (Array.isArray(v)) return 'c(' + v.map(toR).join(', ') + ')';
  if (typeof v === 'number') return String(v);
  if (typeof v === 'boolean') return v ? 'TRUE' : 'FALSE';
  if (v === null || v === undefined) return 'NA';
  return JSON.stringify(String(v));
}
function cleanError(e) {
  let m = (e && e.message) ? e.message : String(e);
  m = m.replace(/^Error in eval\(parse\(text = \.codice\), envir = \.env\):\s*/i, '').replace(/^Error:\s*/i, '');
  return m;
}

window.CBDRunner = { ready, run, evalTests };
