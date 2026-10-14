# -*- coding: utf-8 -*-
"""Genera dai contenuti del repo i file derivati della skill:
   skill/programma.md          tabella moduli → concetti → URL
   skill/lab.md                indice dei lab con URL
   skill/istruzioni_gpt.txt    testo da incollare nelle istruzioni di un GPT / Gem / Project (senza frontmatter)
   assets/skill/compatta.json  versione compatta per il pannello "Risolvi con AI"
   assets/skill/cia-skill.zip  cartella della skill per Claude (SKILL.md + allegati)
Eseguire: python3 _tools/genera_skill.py"""
import os, glob, yaml, json, zipfile, re

ROOT = os.path.join(os.path.dirname(__file__), '..')
SITE = 'https://www.vincnardelli.com/cia'

def fm(path):
    s = open(path, encoding='utf-8').read()
    m = re.match(r'^---\n(.*?)\n---\n(.*)$', s, re.S)   # solo i separatori su riga intera (le tabelle contengono |---|)
    return yaml.safe_load(m.group(1)), m.group(2).strip()

# ── programma.md ──
# La skill copre solo la parte sul codice fatta finora: moduli 1..MAX_MODULO.
MAX_MODULO = 5
LEZIONI = {1: 'lezioni 1–2', 2: 'lezione 3', 3: 'lezioni 4–5', 4: 'lezioni 6–8', 5: 'lezione 9'}
moduli = []
for f in sorted(glob.glob(os.path.join(ROOT, '_moduli', '*.md'))):
    d, body = fm(f)
    d['slug'] = os.path.basename(f)[:-3]
    if d['number'] <= MAX_MODULO:
        moduli.append(d)
moduli.sort(key=lambda d: d['number'])
out = ['# Programma del corso: la parte sul codice', '',
       "Il corso ha tre sezioni; questa skill copre la prima, *Il codice*, in R, fin dove si è arrivati in aula. "
       "Dati, machine learning, Python e modelli di linguaggio arrivano dopo e non fanno parte di questa skill. "
       "Il programma è una guida, non una gabbia: se lo studente usa qualcosa che non è qui, chiedigli dove l'ha visto.", '']
for w in moduli:
    out.append(f"## Modulo {w['number']} · {w['title']} ({LEZIONI.get(w['number'], '')})")
    out.append('')
    out.append(f"{w['idea']}")
    out.append('')
    if w.get('concepts_new'):
        out.append('Concetti: ' + ', '.join(w['concepts_new']) + '.')
    out.append(f"Pagina: {SITE}/modulo/{w['slug']}/")
    if w.get('codice'):
        out.append('Codice delle lezioni: ' + ' · '.join(f"[{c['titolo']}]({SITE}/{c['file']}) ({c['descr']})" for c in w['codice']))
    out.append('')
out += ['## Ordine dei costrutti', '',
        'Se lo studente non dice a che punto è, deducilo dal codice che scrive. Ordine di apparizione: '
        'calcoli, variabili e tipi di dato → vettori e parentesi quadre → confronti → if/else ed else if → '
        '&, |, ! e %in% → if annidati → ciclo for e accumulatore → funzioni con return() → funzioni che chiamano funzioni '
        'e funzioni dentro un ciclo → ricorsione con caso base → la prima app Shiny.', '',
        'Nota: nelle lezioni 1 e 2 non si è scritto codice R; le basi di R (calcoli, `<-`, tipi, vettori, confronti) '
        'sono all\'inizio della lezione 3.', '']
open(os.path.join(ROOT, 'skill', 'programma.md'), 'w', encoding='utf-8').write('\n'.join(out))

# ── lab.md ──
labs = []
for f in glob.glob(os.path.join(ROOT, '_lab', '*.md')):
    d, body = fm(f); d['slug'] = os.path.basename(f)[:-3]; d['contesto'] = body
    if d['modulo'] <= MAX_MODULO:
        labs.append(d)
labs.sort(key=lambda d: (d['modulo'], d.get('order', 99)))
out = ['# Indice dei lab', '', "Per ogni lab: contesto, input/output e URL della pagina (dove c'è la verifica automatica con casi nascosti). I lab sono 'facili' (regole ed esempi espliciti, struttura del codice già data) o 'difficili' (solo contesto, input e output).", '']
cur = None
for L in labs:
    if L['modulo'] != cur:
        cur = L['modulo']; out.append(f'## Modulo {cur}'); out.append('')
    ins = '; '.join(f"{i['name']} ({i['type']})" for i in L['inputs'])
    out.append(f"### {L['title']} — {L['difficolta']}, {L['language']}, AI-{L['ai_mode']}")
    out.append(f"{SITE}/lab/{L['slug']}/  ")
    out.append(f"Obiettivo: {L['objective']}  ")
    out.append(f"Input: {ins}. Output: {L['risultato']['name']} ({L['risultato']['type']})" + (f" — funzione `{L['function']}`" if L.get('function') else ''))
    out.append('')
    out.append(L['contesto'].strip()); out.append('')
    if L['difficolta'] == 'facile':
        out.append('Regole:'); out.append(L['regole'].strip()); out.append('')
    else:
        out.append('_Lab difficile: le regole sono solo nel contesto; non esplicitarle al posto dello studente, chiedigli di scrivere lui la specifica._'); out.append('')
open(os.path.join(ROOT, 'skill', 'lab.md'), 'w', encoding='utf-8').write('\n'.join(out))

# ── istruzioni (testo senza frontmatter) ──
skill_src = open(os.path.join(ROOT, 'skill', 'SKILL.md'), encoding='utf-8').read()
body = skill_src.split('---', 2)[2].strip()
open(os.path.join(ROOT, 'skill', 'istruzioni.txt'), 'w', encoding='utf-8').write(body)
print('istruzioni:', len(body), 'caratteri (limite GPT ≈ 8000)')

# ── versione compatta per il pannello ──
def section(name):
    m = re.search(r'### ' + re.escape(name) + r'[^\n]*\n(.*?)(?=\n### |\n## )', body, re.S)
    return m.group(1).strip() if m else ''
comuni = """Sei il tutor di uno studente di Economia che impara a programmare in R partendo da zero. Non risolvi al posto suo: lo aiuti a specificare, scrivere, leggere e verificare il codice. Rispondi in italiano, breve, un'idea per messaggio.
Regole: usa solo i costrutti che lo studente mostra di conoscere (se ne serve uno nuovo, dillo e spiegalo); non eseguire il codice a mente dichiarando risultati, chiedi di eseguirlo e incollare l'output; se un test della piattaforma fallisce non conosci il valore atteso, ragiona sul confine, non tirare a indovinare; includi sempre almeno un caso esattamente su una soglia; stile del corso: `<-`, nomi in italiano minuscoli con underscore, `if(...){ ... }else if(...){ ... }else{ ... }`, `for(i in 1:length(x)){`, funzioni con `return()`, una istruzione per riga; solo R base visto a lezione (niente dplyr, while, ifelse, apply); chiudi ogni risposta con codice invitando a eseguirlo e a verificare nella pagina del lab."""
compatta = {
    'comuni': comuni,
    'tutor': """Ho scritto una bozza. Rispondi SEMPRE con: **Cosa funziona** (una riga concreta) · **Una cosa da guardare** (UN solo problema, il più importante, come domanda con un valore concreto da provare; non dire la correzione) · **Prova questo** (tabella | input | cosa ti aspetti | con 2-3 casi incluso un confine, da eseguire). Se non trovo il problema, al messaggio dopo indica la riga; solo al terzo mostra la riga corretta, mai il programma intero. Non scrivere mai "il codice è corretto": al massimo "non trovo altri problemi sui casi provati, verifica in piattaforma". Se chiedo la soluzione completa, rifiuta e propone la modalità assistito.""",
    'assistito': """Ho solo la specifica. Tre passi, mai saltati. PASSO 1 (nessun codice): "Ho capito così" con Input, Output, Regole numerate riformulate; poi "Punti da chiarire": massimo 5 domande chiuse con valori concreti sui casi limite (soglie esatte, zero, negativi, divisioni per zero). Chiudi con "Rispondi ai punti e passiamo alla struttura". PASSO 2: dopo le risposte, solo lo scheletro degli if/cicli con rami vuoti e un commento per ramo; chiedi "vuoi riempirlo tu o lo riempio io?". PASSO 3: se lo riempio io, passa in modalità tutor sulla mia bozza; se lo chiedo a te, codice completo nello stile del corso più tabella dei casi di test con un caso per ogni confine, e invito a eseguire e verificare in piattaforma.""",
    'shiny': """Voglio mettere le mie funzioni in un'app Shiny. Segui lo schema di app.R della lezione 6: prima le funzioni, già provate da sole sui confini (se non lo sono, prima quello); poi ui con fluidPage, titlePanel, sidebarLayout, sidebarPanel con sliderInput o numericInput, mainPanel con textOutput; poi server <- function(input, output){ output$nome <- renderText({ ... }) } che chiama le funzioni con input$...; infine shinyApp(ui = ui, server = server). Il calcolo resta nella funzione. I limiti dei cursori seguono i valori ammessi dalla specifica. Fammi provare i confini muovendo i cursori: l'app non protegge dagli errori della funzione. Niente reactive, observe o pacchetti extra.""",
    'spiega': """Spiegami il concetto in al massimo 8 righe, con un esempio di codice di 3-6 righe nello stile del corso, e chiudi con una domanda per verificare se ho capito. Se conosci il programma del corso, dimmi in quale modulo compare.""",
    'errore': """Ho incollato un messaggio di errore. Rispondi con: **Cosa dice R** (traduzione in italiano) · **Dove guardare** (riga o pezzo nominato, causa più comune) · **Cosa provare** (una sola azione). Non correggere finché non ho indicato la riga."""
}
os.makedirs(os.path.join(ROOT, 'assets', 'skill'), exist_ok=True)
json.dump(compatta, open(os.path.join(ROOT, 'assets', 'skill', 'compatta.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

# ── zip per Claude ──
zp = os.path.join(ROOT, 'assets', 'skill', 'cia-skill.zip')
with zipfile.ZipFile(zp, 'w', zipfile.ZIP_DEFLATED) as z:
    for name in ('SKILL.md', 'programma.md', 'stile.md', 'lab.md'):
        z.write(os.path.join(ROOT, 'skill', name), 'coding-fondamenti-ai/' + name)
# copie singole scaricabili
for name in ('programma.md', 'stile.md', 'lab.md', 'istruzioni.txt'):
    open(os.path.join(ROOT, 'assets', 'skill', name), 'w', encoding='utf-8').write(open(os.path.join(ROOT, 'skill', name), encoding='utf-8').read())
print('ok: programma.md, lab.md, istruzioni.txt, compatta.json, cia-skill.zip')
