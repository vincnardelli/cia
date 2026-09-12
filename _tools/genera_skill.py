# -*- coding: utf-8 -*-
"""Genera dai contenuti del repo i file derivati della skill:
   skill/programma.md          tabella settimane → concetti → URL
   skill/lab.md                indice dei lab con URL
   skill/istruzioni_gpt.txt    testo da incollare nelle istruzioni di un GPT / Gem / Project (senza frontmatter)
   assets/skill/compatta.json  versione compatta per il pannello "Risolvi con AI"
   assets/skill/cbd-skill.zip  cartella della skill per Claude (SKILL.md + allegati)
Eseguire: python3 _tools/genera_skill.py"""
import os, glob, yaml, json, zipfile, re

ROOT = os.path.join(os.path.dirname(__file__), '..')
SITE = 'https://www.vincnardelli.com/cbd'

def fm(path):
    s = open(path, encoding='utf-8').read()
    parts = s.split('---')
    return yaml.safe_load(parts[1]), '---'.join(parts[2:]).strip()

# ── programma.md ──
weeks = []
for f in sorted(glob.glob(os.path.join(ROOT, '_settimane', '*.md'))):
    d, body = fm(f)
    d['slug'] = os.path.basename(f)[:-3]
    weeks.append(d)
pil = {1: 'Il codice (R)', 2: 'Come imparano le macchine (R → Python)', 3: 'LLM e agenti (Python)'}
out = ['# Programma del corso', '', 'Tre pilastri, dodici settimane, cinque ore a settimana. Il programma è una guida, non una gabbia: la settimana in cui si è arrivati in aula può differire.', '']
for p in (1, 2, 3):
    out.append(f'## Pilastro {p} — {pil[p]}'); out.append('')
    out.append('| sett. | titolo | idea | concetti introdotti | pagina |'); out.append('|---|---|---|---|---|')
    for w in weeks:
        if w['pillar'] == p:
            out.append(f"| {w['number']} | {w['title']} | {w['idea']} | {', '.join(w['concepts_new'])} | {SITE}/settimana/{w['slug']}/ |")
    out.append('')
out += ['## Ordine dei costrutti', '',
        'Se lo studente non dice a che punto è, deducilo dal codice che scrive. Ordine di apparizione: variabili e operatori → if/else → operatori logici e %in% → vettori e indicizzazione → ciclo for → funzioni → data frame e dplyr → ggplot2 → alberi (R) → Python e pandas → random forest → testi ed embeddings → API LLM → agenti.', '']
open(os.path.join(ROOT, 'skill', 'programma.md'), 'w', encoding='utf-8').write('\n'.join(out))

# ── lab.md ──
labs = []
for f in glob.glob(os.path.join(ROOT, '_lab', '*.md')):
    d, body = fm(f); d['slug'] = os.path.basename(f)[:-3]; d['rules'] = body; labs.append(d)
labs.sort(key=lambda d: (d['week'], d.get('order', 99)))
out = ['# Indice dei lab', '', 'Per ogni lab: specifica sintetica e URL della pagina (dove ci sono regole complete, esempi e verifica automatica con casi nascosti).', '']
cur = None
for L in labs:
    if L['week'] != cur:
        cur = L['week']; out.append(f'## Settimana {cur}'); out.append('')
    ins = '; '.join(f"{i['name']} ({i['type']})" for i in L['inputs'])
    out.append(f"### {L['title']} — {L['level']}, {L['language']}, AI-{L['ai_mode']}")
    out.append(f"{SITE}/lab/{L['slug']}/  ")
    out.append(f"Obiettivo: {L['objective']}  ")
    out.append(f"Input: {ins}. Output: {L['output']['name']} ({L['output']['type']})" + (f" — funzione `{L['function']}`" if L.get('function') else ''))
    out.append('')
    out.append(L['rules']); out.append('')
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
comuni = """Sei il tutor di uno studente di Economia che impara a programmare (R di default, Python se lo chiede). Non risolvi al posto suo: lo aiuti a specificare, scrivere, leggere e verificare il codice. Rispondi in italiano, breve, un'idea per messaggio.
Regole: usa solo i costrutti che lo studente mostra di conoscere (se ne serve uno nuovo, dillo e spiegalo); non eseguire il codice a mente dichiarando risultati, chiedi di eseguirlo e incollare l'output; se un test della piattaforma fallisce non conosci il valore atteso, ragiona sul confine, non tirare a indovinare; includi sempre almeno un caso esattamente su una soglia; stile del corso: `<-`, nomi in italiano minuscoli con underscore, `if(...){ ... }else if(...){ ... }else{ ... }`, una istruzione per riga, R base prima di dplyr; chiudi ogni risposta con codice invitando a eseguirlo e a verificare nella pagina del lab."""
compatta = {
    'comuni': comuni,
    'tutor': """Ho scritto una bozza. Rispondi SEMPRE con: **Cosa funziona** (una riga concreta) · **Una cosa da guardare** (UN solo problema, il più importante, come domanda con un valore concreto da provare; non dire la correzione) · **Prova questo** (tabella | input | cosa ti aspetti | con 2-3 casi incluso un confine, da eseguire). Se non trovo il problema, al messaggio dopo indica la riga; solo al terzo mostra la riga corretta, mai il programma intero. Non scrivere mai "il codice è corretto": al massimo "non trovo altri problemi sui casi provati, verifica in piattaforma". Se chiedo la soluzione completa, rifiuta e propone la modalità assistito.""",
    'assistito': """Ho solo la specifica. Tre passi, mai saltati. PASSO 1 (nessun codice): "Ho capito così" con Input, Output, Regole numerate riformulate; poi "Punti da chiarire": massimo 5 domande chiuse con valori concreti sui casi limite (soglie esatte, zero, negativi, divisioni per zero). Chiudi con "Rispondi ai punti e passiamo alla struttura". PASSO 2: dopo le risposte, solo lo scheletro degli if/cicli con rami vuoti e un commento per ramo; chiedi "vuoi riempirlo tu o lo riempio io?". PASSO 3: se lo riempio io, passa in modalità tutor sulla mia bozza; se lo chiedo a te, codice completo nello stile del corso più tabella dei casi di test con un caso per ogni confine, e invito a eseguire e verificare in piattaforma.""",
    'traduci': """Traduci il mio codice R in Python (o viceversa) mostrando i due blocchi affiancati con lo stesso ordine di righe, poi una tabella | R | Python | nota | con solo le differenze che contano (graffe/indentazione, <- / =, c() / liste, 1:n / range, %>% / metodi pandas, TRUE/True, NA/NaN). Chiudi ricordando di ripassare gli stessi casi di test nell'altro linguaggio: i confini (< contro <=) sono dove le traduzioni sbagliano.""",
    'spiega': """Spiegami il concetto in al massimo 8 righe, con un esempio di codice di 3-6 righe nello stile del corso, e chiudi con una domanda per verificare se ho capito. Se conosci il programma del corso, dimmi in quale settimana compare.""",
    'errore': """Ho incollato un messaggio di errore. Rispondi con: **Cosa dice R** (traduzione in italiano) · **Dove guardare** (riga o pezzo nominato, causa più comune) · **Cosa provare** (una sola azione). Non correggere finché non ho indicato la riga."""
}
os.makedirs(os.path.join(ROOT, 'assets', 'skill'), exist_ok=True)
json.dump(compatta, open(os.path.join(ROOT, 'assets', 'skill', 'compatta.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

# ── zip per Claude ──
zp = os.path.join(ROOT, 'assets', 'skill', 'cbd-skill.zip')
with zipfile.ZipFile(zp, 'w', zipfile.ZIP_DEFLATED) as z:
    for name in ('SKILL.md', 'programma.md', 'stile.md', 'lab.md'):
        z.write(os.path.join(ROOT, 'skill', name), 'coding-fondamenti-ai/' + name)
# copie singole scaricabili
for name in ('programma.md', 'stile.md', 'lab.md', 'istruzioni.txt'):
    open(os.path.join(ROOT, 'assets', 'skill', name), 'w', encoding='utf-8').write(open(os.path.join(ROOT, 'skill', name), encoding='utf-8').read())
print('ok: programma.md, lab.md, istruzioni.txt, compatta.json, cbd-skill.zip')
