# -*- coding: utf-8 -*-
"""Genera i file _lab/*.md a partire da definizioni Python.
I valori attesi dei test sono calcolati da un'implementazione di riferimento in Python,
così specifica, soluzione e test restano coerenti. Eseguire: python3 _tools/genera_lab.py"""
import yaml, os, math, textwrap

OUT = os.path.join(os.path.dirname(__file__), '..', '_lab')
os.makedirs(OUT, exist_ok=True)
LABS = []

def lab(slug, **kw):
    kw['slug'] = slug
    LABS.append(kw)

def r2(x): return round(x + 1e-12, 2)

# ─────────────────────────── SETTIMANA 1 ───────────────────────────
def scontrino(prezzo_netto, quantita):
    return r2(prezzo_netto * quantita * 1.22)
lab('scontrino', title='Scontrino', modulo=1, order=1, level='base', language='R', ai_mode='off',
    objective="Calcolare il totale di uno scontrino a partire dal prezzo netto e dalla quantità, con IVA al 22%.",
    inputs=[dict(name='prezzo_netto', type='numero', desc='prezzo unitario senza IVA, in euro'),
            dict(name='quantita', type='numero', desc='pezzi acquistati')],
    risultato=dict(name='totale', type='numero', desc='totale da pagare, arrotondato a 2 decimali'),
    rules="""- Il totale netto è `prezzo_netto * quantita`.
- L'IVA è il 22% del totale netto: il totale da pagare è il netto più l'IVA.
- Arrotonda il risultato a due decimali con `round(x, 2)`.""",
    fn=scontrino,
    cases=[dict(prezzo_netto=10, quantita=3, visible=True), dict(prezzo_netto=19.9, quantita=1, visible=True),
           dict(prezzo_netto=10, quantita=0, boundary=True, hint="Con zero pezzi il totale deve essere 0: il tuo codice lo gestisce senza bisogno di un caso speciale?"),
           dict(prezzo_netto=0.99, quantita=7, boundary=True, hint="Con i centesimi l'arrotondamento conta: hai usato round(x, 2) sul totale finale, non sul prezzo unitario?"),
           dict(prezzo_netto=1234.5, quantita=2)],
    skeleton="prezzo_netto <- 10\nquantita <- 3\n\n# calcola il totale con IVA al 22%: alla fine deve esistere la variabile totale\n",
    solution="prezzo_netto <- 10\nquantita <- 3\n\nnetto <- prezzo_netto * quantita\niva <- netto * 0.22\ntotale <- round(netto + iva, 2)\ntotale\n")

def cambio(importo_euro, tasso):
    commissione = max(2, 0.01 * importo_euro)
    netto = importo_euro - commissione
    return r2(netto * tasso) if netto > 0 else 0
lab('cambio-valuta', title='Cambio valuta', modulo=1, order=2, level='extra', language='R', ai_mode='off',
    objective="Convertire un importo in euro in dollari applicando la commissione dello sportello.",
    inputs=[dict(name='importo_euro', type='numero', desc='euro da cambiare'), dict(name='tasso', type='numero', desc='dollari per un euro, es. 1.08')],
    risultato=dict(name='dollari', type='numero', desc='dollari ricevuti, arrotondati a 2 decimali'),
    rules="""- La commissione è il **maggiore** tra 2 € e l'1% dell'importo.
- Si cambia solo l'importo al netto della commissione: `dollari = (importo - commissione) * tasso`.
- Se l'importo non copre nemmeno la commissione, si ricevono 0 dollari (mai un valore negativo).
- Arrotonda a due decimali.""",
    fn=cambio,
    cases=[dict(importo_euro=100, tasso=1.08, visible=True), dict(importo_euro=500, tasso=1.1, visible=True),
           dict(importo_euro=200, tasso=1.0, boundary=True, hint="A 200 € l'1% vale esattamente 2 €: le due commissioni coincidono, il risultato deve essere lo stesso qualunque delle due scegli."),
           dict(importo_euro=2, tasso=1.08, boundary=True, hint="Con 2 € la commissione mangia tutto l'importo: cosa resta da cambiare?"),
           dict(importo_euro=1, tasso=1.08, boundary=True, hint="Con 1 € il netto è negativo: il risultato deve essere 0, non un numero negativo."),
           dict(importo_euro=1000, tasso=0.95)],
    skeleton="importo_euro <- 100\ntasso <- 1.08\n\n# alla fine deve esistere la variabile dollari\n",
    solution="importo_euro <- 100\ntasso <- 1.08\n\ncommissione <- max(2, importo_euro * 0.01)\nnetto <- importo_euro - commissione\nif(netto > 0){\n  dollari <- round(netto * tasso, 2)\n}else{\n  dollari <- 0\n}\ndollari\n")

def interesse(capitale, tasso, anni):
    return r2(capitale * (1 + tasso / 100) ** anni)
lab('interesse-composto', title='Interesse composto', modulo=1, order=3, level='extra', language='R', ai_mode='on',
    objective="Calcolare il montante di un capitale investito a interesse composto per un certo numero di anni.",
    inputs=[dict(name='capitale', type='numero', desc='euro investiti'), dict(name='tasso', type='numero', desc='tasso annuo in percentuale, es. 3 per il 3%'), dict(name='anni', type='numero', desc='anni di investimento (intero)')],
    risultato=dict(name='montante', type='numero', desc='capitale finale, arrotondato a 2 decimali'),
    rules="""- Ogni anno il capitale cresce del tasso: `montante = capitale * (1 + tasso/100)^anni`.
- Attenzione: il tasso è dato in percentuale (3 significa 3%), non in frazione.
- Arrotonda a due decimali.""",
    fn=interesse,
    cases=[dict(capitale=1000, tasso=3, anni=2, visible=True), dict(capitale=5000, tasso=5, anni=10, visible=True),
           dict(capitale=1000, tasso=3, anni=0, boundary=True, hint="Con zero anni il montante è il capitale iniziale: qualunque numero elevato a 0 fa 1."),
           dict(capitale=1000, tasso=0, anni=5, boundary=True, hint="Con tasso zero il capitale non cambia. Hai diviso il tasso per 100 prima di sommarlo a 1?"),
           dict(capitale=250.5, tasso=1.5, anni=7)],
    skeleton="capitale <- 1000\ntasso <- 3\nanni <- 2\n\n# alla fine deve esistere la variabile montante\n",
    solution="capitale <- 1000\ntasso <- 3\nanni <- 2\n\nmontante <- round(capitale * (1 + tasso/100)^anni, 2)\nmontante\n")

def piano_risparmio(capitale, versamento, tasso, anni):
    m = capitale
    for _ in range(int(anni)):
        m = m * (1 + tasso / 100) + versamento
    return r2(m)
lab('piano-risparmio', title='Piano di risparmio', modulo=1, order=4, level='sfida', language='R', ai_mode='on',
    objective="Calcolare quanto si accumula versando ogni anno una somma fissa su un conto a interesse composto.",
    inputs=[dict(name='capitale', type='numero', desc='somma iniziale'), dict(name='versamento', type='numero', desc='versato alla fine di ogni anno'), dict(name='tasso', type='numero', desc='tasso annuo in percentuale'), dict(name='anni', type='numero', desc='anni (intero)')],
    risultato=dict(name='montante', type='numero', desc='somma finale, 2 decimali'),
    rules="""- Ogni anno, nell'ordine: il saldo cresce del tasso, poi si aggiunge il versamento.
- Con zero anni non succede nulla: il montante è il capitale iniziale.
- Non esiste una formula "già vista" nel corso: serve ripetere il passo per ogni anno (o trovare la formula da soli).""",
    fn=piano_risparmio,
    cases=[dict(capitale=1000, versamento=100, tasso=2, anni=3, visible=True),
           dict(capitale=0, versamento=1200, tasso=4, anni=10),
           dict(capitale=1000, versamento=100, tasso=2, anni=0, boundary=True),
           dict(capitale=500, versamento=0, tasso=3, anni=5, boundary=True),
           dict(capitale=1000, versamento=100, tasso=0, anni=4, boundary=True)],
    skeleton="capitale <- 1000\nversamento <- 100\ntasso <- 2\nanni <- 3\n\n# alla fine deve esistere la variabile montante\n",
    solution="capitale <- 1000\nversamento <- 100\ntasso <- 2\nanni <- 3\n\nmontante <- capitale\nif(anni > 0){\n  for(i in 1:anni){\n    montante <- montante * (1 + tasso/100) + versamento\n  }\n}\nmontante <- round(montante, 2)\nmontante\n")

# ─────────────────────────── SETTIMANA 2 ───────────────────────────
def boomer(anno): return "Boomer" if 1946 <= anno <= 1964 else "Non Boomer"
lab('boomer', title='Boomer finder', modulo=2, order=1, level='base', language='R', ai_mode='off',
    objective="Stabilire se una persona è un baby boomer a partire dall'anno di nascita.",
    inputs=[dict(name='anno', type='numero', desc='anno di nascita')],
    risultato=dict(name='status', type='testo', desc='"Boomer" oppure "Non Boomer"'),
    rules="""- È boomer chi è nato **dal 1946 al 1964 compresi**.
- Tutti gli altri sono "Non Boomer".
- Scrivilo in almeno due modi diversi (con due `if`, con `&`, con `%in%`) e controlla che diano lo stesso risultato sui casi al confine.""",
    fn=boomer,
    cases=[dict(anno=1955, visible=True), dict(anno=2006, visible=True),
           dict(anno=1946, boundary=True, hint="Il 1946 è compreso: chi è nato quell'anno è boomer. Il tuo confronto usa < oppure <=?"),
           dict(anno=1964, boundary=True, hint="Anche il 1964 è compreso. Controlla il confronto sull'estremo superiore."),
           dict(anno=1945, boundary=True), dict(anno=1965, boundary=True)],
    skeleton='anno <- 1955\n\n# alla fine deve esistere la variabile status ("Boomer" o "Non Boomer")\n',
    solution='anno <- 1955\n\nif(anno >= 1946 & anno <= 1964){\n  status <- "Boomer"\n}else{\n  status <- "Non Boomer"\n}\nstatus\n')

def autovelox(velocita, limite):
    d = velocita - limite
    if d <= 0: return 0
    if d <= 10: return 36
    if d <= 40: return 148
    if d <= 60: return 370
    return 500
lab('autovelox', title='Autovelox', modulo=2, order=2, level='base', language='R', ai_mode='off',
    objective="Calcolare la sanzione per eccesso di velocità secondo l'art. 142 del Codice della Strada.",
    inputs=[dict(name='velocita', type='numero', desc='velocità rilevata, km/h'), dict(name='limite', type='numero', desc='limite di velocità, km/h')],
    risultato=dict(name='multa', type='numero', desc='sanzione in euro'),
    rules="""Art. 142 CdS (importi minimi):

- entro il limite: nessuna sanzione;
- oltre il limite di **non oltre 10 km/h**: 36 €;
- di **oltre 10 e non oltre 40 km/h**: 148 €;
- di **oltre 40 e non oltre 60 km/h**: 370 €;
- di **oltre 60 km/h**: 500 €.""",
    fn=autovelox,
    cases=[dict(velocita=45, limite=50, visible=True), dict(velocita=75, limite=50, visible=True),
           dict(velocita=60, limite=50, boundary=True, hint="Esattamente 10 km/h oltre il limite è \"non oltre 10\": quindi 36 €. Il tuo confronto lo include?"),
           dict(velocita=90, limite=50, boundary=True, hint="40 km/h oltre il limite: \"non oltre 40\" → 148 €."),
           dict(velocita=110, limite=50, boundary=True, hint="60 km/h oltre: \"non oltre 60\" → 370 €."),
           dict(velocita=111, limite=50, boundary=True), dict(velocita=50, limite=50, boundary=True, hint="Velocità uguale al limite: nessuna sanzione."),
           dict(velocita=200, limite=130)],
    skeleton="velocita <- 70\nlimite <- 50\n\n# alla fine deve esistere la variabile multa\n",
    solution="velocita <- 70\nlimite <- 50\n\ndifferenza <- velocita - limite\n\nif(differenza <= 0){\n  multa <- 0\n}else if(differenza <= 10){\n  multa <- 36\n}else if(differenza <= 40){\n  multa <- 148\n}else if(differenza <= 60){\n  multa <- 370\n}else{\n  multa <- 500\n}\nmulta\n")

def voli(seat_type, days_before, load_factor):
    prezzo = {'Economy': 100, 'Premium': 180, 'Business': 350}[seat_type]
    if days_before > 60: m1 = 0.80
    elif days_before >= 31: m1 = 0.90
    elif days_before >= 15: m1 = 1.00
    elif days_before >= 7: m1 = 1.20
    elif days_before >= 3: m1 = 1.40
    else: m1 = 1.70
    if load_factor < 0.50: m2 = 0.90
    elif load_factor <= 0.70: m2 = 1.00
    elif load_factor <= 0.85: m2 = 1.15
    else: m2 = 1.35
    extra = 1.10 if (days_before <= 2 and load_factor > 0.85) else 1
    return r2(prezzo * m1 * m2 * extra + 25)
lab('pricing-voli', title='Pricing dei voli', modulo=2, order=3, level='base', language='R', ai_mode='off',
    objective="Calcolare il prezzo di un biglietto aereo in base a classe, giorni di anticipo e riempimento dell'aereo.",
    inputs=[dict(name='seat_type', type='testo', desc='"Economy", "Premium" o "Business"'), dict(name='days_before', type='numero', desc='giorni di anticipo (intero)'), dict(name='load_factor', type='numero', desc='riempimento tra 0 e 1')],
    risultato=dict(name='prezzo_finale', type='numero', desc='prezzo in euro, 2 decimali'),
    rules="""- **Tariffa base**: Economy 100 €, Premium 180 €, Business 350 €.
- **Anticipo** (`days_before`): oltre 60 giorni −20%; da 31 a 60 −10%; da 15 a 30 0%; da 7 a 14 +20%; da 3 a 6 +40%; da 0 a 2 +70%.
- **Riempimento** (`load_factor`): sotto 0.50 −10%; da 0.50 a 0.70 0%; oltre 0.70 fino a 0.85 +15%; oltre 0.85 +35%.
- **Fee fissa**: 25 € aggiunti alla fine.
- **Stress di mercato**: se `days_before` è 2 o meno **e** `load_factor` supera 0.85, ulteriore +10% (prima della fee).
- I moltiplicatori si applicano in cascata: `base × anticipo × riempimento × stress + 25`.""",
    fn=voli,
    cases=[dict(seat_type='Economy', days_before=5, load_factor=0.82, visible=True), dict(seat_type='Business', days_before=90, load_factor=0.3, visible=True),
           dict(seat_type='Economy', days_before=60, load_factor=0.6, boundary=True, hint="60 giorni è \"da 31 a 60\": sconto del 10%, non del 20%."),
           dict(seat_type='Economy', days_before=61, load_factor=0.6, boundary=True),
           dict(seat_type='Economy', days_before=15, load_factor=0.6, boundary=True, hint="15 giorni è ancora nella fascia 0%."),
           dict(seat_type='Economy', days_before=7, load_factor=0.6, boundary=True), dict(seat_type='Economy', days_before=3, load_factor=0.6, boundary=True),
           dict(seat_type='Premium', days_before=20, load_factor=0.5, boundary=True, hint="0.50 esatto è nella fascia \"da 0.50 a 0.70\": 0%."),
           dict(seat_type='Premium', days_before=20, load_factor=0.7, boundary=True), dict(seat_type='Premium', days_before=20, load_factor=0.85, boundary=True, hint="0.85 esatto è ancora +15%; il +35% scatta solo *oltre* 0.85."),
           dict(seat_type='Economy', days_before=2, load_factor=0.86, boundary=True, hint="Due giorni e aereo quasi pieno: scatta anche lo stress di mercato (+10%)."),
           dict(seat_type='Economy', days_before=2, load_factor=0.85, boundary=True, hint="A 0.85 esatto lo stress NON scatta: la regola dice \"supera 0.85\".")],
    skeleton='seat_type   <- "Economy"\ndays_before <- 5\nload_factor <- 0.82\n\n# alla fine deve esistere la variabile prezzo_finale\n',
    solution=open(os.path.join(os.path.dirname(__file__), '..', 'materiale_lezioni', '5', 'prezzo_voli.R')).read().replace('prezzo_finale <- (prezzo_dinamico * extra_stress) + fee_fissa', 'prezzo_finale <- round((prezzo_dinamico * extra_stress) + fee_fissa, 2)'))

def autovelox_punti(velocita, limite, punti_iniziali):
    d = velocita - limite
    dec = 0 if d <= 10 else 3 if d <= 40 else 6 if d <= 60 else 10
    return max(0, punti_iniziali - dec)
lab('autovelox-punti', title='Autovelox con punti patente', modulo=2, order=4, level='extra', language='R', ai_mode='off',
    objective="Estendere l'autovelox: oltre alla sanzione, calcolare i punti patente rimasti dopo la decurtazione.",
    inputs=[dict(name='velocita', type='numero'), dict(name='limite', type='numero'), dict(name='punti_iniziali', type='numero', desc='punti sulla patente prima della multa')],
    risultato=dict(name='punti_finali', type='numero', desc='punti rimasti (mai sotto zero)'),
    rules="""- Fasce come nell'Autovelox: entro il limite o non oltre 10 km/h → nessuna decurtazione; oltre 10 e non oltre 40 → 3 punti; oltre 40 e non oltre 60 → 6 punti; oltre 60 → 10 punti.
- I punti non possono scendere sotto zero.""",
    fn=autovelox_punti,
    cases=[dict(velocita=75, limite=50, punti_iniziali=20, visible=True), dict(velocita=55, limite=50, punti_iniziali=20, visible=True),
           dict(velocita=60, limite=50, punti_iniziali=20, boundary=True), dict(velocita=90, limite=50, punti_iniziali=20, boundary=True),
           dict(velocita=120, limite=50, punti_iniziali=4, boundary=True, hint="Con 4 punti e una decurtazione di 10 il risultato deve essere 0, non −6."),
           dict(velocita=111, limite=50, punti_iniziali=10, boundary=True)],
    skeleton="velocita <- 75\nlimite <- 50\npunti_iniziali <- 20\n\n# alla fine deve esistere la variabile punti_finali\n",
    solution="velocita <- 75\nlimite <- 50\npunti_iniziali <- 20\n\ndifferenza <- velocita - limite\nif(differenza <= 10){\n  decurtazione <- 0\n}else if(differenza <= 40){\n  decurtazione <- 3\n}else if(differenza <= 60){\n  decurtazione <- 6\n}else{\n  decurtazione <- 10\n}\npunti_finali <- punti_iniziali - decurtazione\nif(punti_finali < 0){\n  punti_finali <- 0\n}\npunti_finali\n")

def bollo(kw, classe_euro):
    tariffe = {6: (2.58, 3.87), 5: (2.58, 3.87), 4: (2.58, 3.87), 3: (2.70, 4.05), 2: (2.80, 4.20), 1: (3.00, 4.50), 0: (3.00, 4.50)}
    a, b = tariffe[int(classe_euro)]
    return r2(a * min(kw, 100) + b * max(0, kw - 100))
lab('bollo-auto', title='Bollo auto', modulo=2, order=5, level='extra', language='R', ai_mode='on',
    objective="Calcolare il bollo auto (regole semplificate) in base alla potenza e alla classe ambientale.",
    inputs=[dict(name='kw', type='numero', desc='potenza in kW'), dict(name='classe_euro', type='numero', desc='classe Euro da 0 a 6')],
    risultato=dict(name='bollo', type='numero', desc='importo in euro, 2 decimali'),
    rules="""Tariffa per kW (regole semplificate a fini didattici):

| classe Euro | fino a 100 kW | ogni kW oltre i 100 |
|---|---|---|
| 4, 5, 6 | 2,58 € | 3,87 € |
| 3 | 2,70 € | 4,05 € |
| 2 | 2,80 € | 4,20 € |
| 0, 1 | 3,00 € | 4,50 € |

- I primi 100 kW si pagano alla tariffa bassa; **solo** i kW oltre i 100 alla tariffa alta.
- Arrotonda a due decimali.""",
    fn=bollo,
    cases=[dict(kw=85, classe_euro=6, visible=True), dict(kw=140, classe_euro=4, visible=True),
           dict(kw=100, classe_euro=5, boundary=True, hint="100 kW esatti: tutti alla tariffa bassa, nessun kW oltre."),
           dict(kw=101, classe_euro=5, boundary=True, hint="101 kW: 100 alla tariffa bassa e 1 solo alla tariffa alta, non 101 alla tariffa alta."),
           dict(kw=100, classe_euro=3, boundary=True), dict(kw=120, classe_euro=0), dict(kw=120, classe_euro=1, boundary=True), dict(kw=120, classe_euro=2)],
    skeleton="kw <- 85\nclasse_euro <- 6\n\n# alla fine deve esistere la variabile bollo\n",
    solution="kw <- 85\nclasse_euro <- 6\n\nif(classe_euro >= 4){\n  bassa <- 2.58\n  alta <- 3.87\n}else if(classe_euro == 3){\n  bassa <- 2.70\n  alta <- 4.05\n}else if(classe_euro == 2){\n  bassa <- 2.80\n  alta <- 4.20\n}else{\n  bassa <- 3.00\n  alta <- 4.50\n}\n\nif(kw <= 100){\n  bollo <- kw * bassa\n}else{\n  bollo <- 100 * bassa + (kw - 100) * alta\n}\nbollo <- round(bollo, 2)\nbollo\n")

def irpef(reddito):
    def scaglioni(r, sc):
        imp, prev = 0, 0
        for lim, al in sc:
            if r > prev: imp += (min(r, lim) - prev) * al
            prev = lim
        return imp
    i25 = scaglioni(reddito, [(28000, .23), (50000, .35), (float('inf'), .43)])
    i26 = scaglioni(reddito, [(15000, .20), (28000, .23), (50000, .36), (75000, .40), (120000, .43), (float('inf'), .46)])
    return r2(i26 - i25)
lab('irpef', title='IRPEF 2025 vs 2026', modulo=2, order=6, level='extra', language='R', ai_mode='on',
    objective="Calcolare l'IRPEF lorda con gli scaglioni 2025 e con la proposta 2026, e la differenza tra le due.",
    inputs=[dict(name='reddito', type='numero', desc='reddito complessivo annuo, euro')],
    risultato=dict(name='differenza', type='numero', desc='IRPEF 2026 − IRPEF 2025, in euro, 2 decimali'),
    rules="""Aliquote per scaglione (ogni fascia tassa **solo la parte di reddito che ci cade dentro**):

| scaglione | 2025 | 2026 (proposta) |
|---|---|---|
| fino a 15.000 € | 23% | 20% |
| da 15.001 a 28.000 € | 23% | 23% |
| da 28.001 a 50.000 € | 35% | 36% |
| da 50.001 a 75.000 € | 43% | 40% |
| da 75.001 a 120.000 € | 43% | 43% |
| oltre 120.000 € | 43% | 46% |

- Calcola `imposta_2025` e `imposta_2026`, poi `differenza <- imposta_2026 - imposta_2025` (negativa se il 2026 conviene).
- Arrotonda la differenza a due decimali.""",
    fn=irpef,
    cases=[dict(reddito=45000, visible=True), dict(reddito=10000, visible=True),
           dict(reddito=15000, boundary=True, hint="15.000 esatti stanno tutti nel primo scaglione: nel 2026 al 20%."),
           dict(reddito=28000, boundary=True, hint="A 28.000 non c'è ancora nessun euro tassato al 35%/36%."),
           dict(reddito=50000, boundary=True), dict(reddito=75000, boundary=True), dict(reddito=120000, boundary=True),
           dict(reddito=0, boundary=True, hint="Reddito zero: imposta zero in entrambi gli anni, differenza zero."),
           dict(reddito=200000)],
    skeleton="reddito <- 45000\n\n# calcola imposta_2025 e imposta_2026: alla fine deve esistere la variabile differenza\n",
    # il file di lezione ha un refuso nell'ultimo scaglione 2025 (0.46 invece di 0.43): corretto qui
    solution=open(os.path.join(os.path.dirname(__file__), '..', 'materiale_lezioni', '8', 'irpef.R')).read().split('aliquota_totale_2026')[0].replace('(reddito - 120000) * 0.46', '(reddito - 120000) * 0.43', 1) + "\ndifferenza <- round(imposta_2026 - imposta_2025, 2)\ndifferenza\n")

def penali(importo, giorni_ritardo):
    if giorni_ritardo <= 10: p = 0
    elif giorni_ritardo <= 30: p = 0.05
    elif giorni_ritardo <= 60: p = 0.10
    elif giorni_ritardo <= 90: p = 0.20
    else: p = 0.20 + 0.02 * (giorni_ritardo - 90)
    return r2(importo * (1 + p))
lab('penali-fatture', title='Penali sulle fatture', modulo=2, order=7, level='extra', language='R', ai_mode='on',
    objective="Calcolare il totale di una fattura pagata in ritardo, applicando le penali previste.",
    inputs=[dict(name='importo', type='numero', desc='importo della fattura'), dict(name='giorni_ritardo', type='numero', desc='giorni di ritardo (intero, 0 se puntuale)')],
    risultato=dict(name='totale', type='numero', desc='importo più penale, 2 decimali'),
    rules="""- entro 10 giorni di ritardo: nessuna penale;
- da 11 a 30 giorni: 5% dell'importo;
- da 31 a 60 giorni: 10%;
- da 61 a 90 giorni: 20%;
- oltre 90 giorni: 20% **più il 2% per ogni giorno oltre il 90°**.""",
    fn=penali,
    cases=[dict(importo=1000, giorni_ritardo=20, visible=True), dict(importo=1000, giorni_ritardo=0, visible=True),
           dict(importo=1000, giorni_ritardo=10, boundary=True, hint="10 giorni è ancora \"entro 10\": nessuna penale."),
           dict(importo=1000, giorni_ritardo=11, boundary=True), dict(importo=1000, giorni_ritardo=30, boundary=True), dict(importo=1000, giorni_ritardo=31, boundary=True),
           dict(importo=1000, giorni_ritardo=60, boundary=True), dict(importo=1000, giorni_ritardo=90, boundary=True, hint="A 90 giorni la penale è il 20% secco: il 2% al giorno parte dal 91°."),
           dict(importo=1000, giorni_ritardo=91, boundary=True, hint="91 giorni: 20% + 2% × 1 giorno = 22%."),
           dict(importo=250, giorni_ritardo=100)],
    skeleton="importo <- 1000\ngiorni_ritardo <- 20\n\n# alla fine deve esistere la variabile totale\n",
    solution="importo <- 1000\ngiorni_ritardo <- 20\n\nif(giorni_ritardo <= 10){\n  penale <- 0\n}else if(giorni_ritardo <= 30){\n  penale <- 0.05\n}else if(giorni_ritardo <= 60){\n  penale <- 0.10\n}else if(giorni_ritardo <= 90){\n  penale <- 0.20\n}else{\n  penale <- 0.20 + 0.02 * (giorni_ritardo - 90)\n}\ntotale <- round(importo * (1 + penale), 2)\ntotale\n")

def isee(reddito, patrimonio, componenti):
    scala = {1: 1.0, 2: 1.57, 3: 2.04, 4: 2.46, 5: 2.85}
    s = scala[min(int(componenti), 5)] + max(0, componenti - 5) * 0.35
    return r2((reddito + 0.2 * patrimonio) / s)
lab('isee', title='ISEE semplificato', modulo=2, order=8, level='sfida', language='R', ai_mode='on',
    objective="Calcolare un ISEE semplificato di una famiglia a partire da reddito, patrimonio e numero di componenti.",
    inputs=[dict(name='reddito', type='numero', desc='reddito familiare annuo'), dict(name='patrimonio', type='numero', desc='patrimonio mobiliare e immobiliare'), dict(name='componenti', type='numero', desc='persone nel nucleo (intero ≥ 1)')],
    risultato=dict(name='isee', type='numero', desc='ISEE, 2 decimali'),
    rules="""- L'indicatore della situazione economica è `ISE = reddito + 20% del patrimonio`.
- La scala di equivalenza dipende dai componenti: 1 → 1,00; 2 → 1,57; 3 → 2,04; 4 → 2,46; 5 → 2,85; **oltre 5, +0,35 per ogni componente in più**.
- `ISEE = ISE / scala`, arrotondato a due decimali.""",
    fn=isee,
    cases=[dict(reddito=30000, patrimonio=50000, componenti=3, visible=True),
           dict(reddito=30000, patrimonio=0, componenti=1, boundary=True), dict(reddito=30000, patrimonio=0, componenti=5, boundary=True),
           dict(reddito=30000, patrimonio=0, componenti=6, boundary=True), dict(reddito=30000, patrimonio=0, componenti=8), dict(reddito=0, patrimonio=100000, componenti=2)],
    skeleton="reddito <- 30000\npatrimonio <- 50000\ncomponenti <- 3\n\n# alla fine deve esistere la variabile isee\n",
    solution="reddito <- 30000\npatrimonio <- 50000\ncomponenti <- 3\n\nise <- reddito + 0.2 * patrimonio\nif(componenti == 1){\n  scala <- 1\n}else if(componenti == 2){\n  scala <- 1.57\n}else if(componenti == 3){\n  scala <- 2.04\n}else if(componenti == 4){\n  scala <- 2.46\n}else{\n  scala <- 2.85 + (componenti - 5) * 0.35\n}\nisee <- round(ise / scala, 2)\nisee\n")

# ─────────────────────────── SETTIMANA 3 ───────────────────────────
def bmi(altezza, peso):
    b = peso / altezza ** 2
    if b < 18.5: return "Sottopeso"
    if b < 25: return "Normopeso"
    if b < 30: return "Sovrappeso"
    if b < 35: return "Obesità grado I"
    if b < 40: return "Obesità grado II"
    return "Obesità grado III"
lab('bmi', title='Classificazione BMI', modulo=3, order=1, level='base', language='R', ai_mode='off',
    objective="Calcolare l'indice di massa corporea di un paziente e classificarlo secondo le fasce del Ministero della Salute.",
    inputs=[dict(name='altezza', type='numero', desc='in metri'), dict(name='peso', type='numero', desc='in kg')],
    risultato=dict(name='classificazione', type='testo', desc='una delle sei categorie, scritta esattamente come nella tabella'),
    rules="""- `BMI = peso / altezza^2`.
- Sottopeso: BMI < 18,5 · Normopeso: 18,5 ≤ BMI < 25 · Sovrappeso: 25 ≤ BMI < 30 · Obesità grado I: 30 ≤ BMI < 35 · Obesità grado II: 35 ≤ BMI < 40 · Obesità grado III: BMI ≥ 40.
- Le categorie vanno scritte così: `"Sottopeso"`, `"Normopeso"`, `"Sovrappeso"`, `"Obesità grado I"`, `"Obesità grado II"`, `"Obesità grado III"`.
- Poi, in RStudio, applica lo stesso codice a più pazienti con un ciclo `for` (la verifica qui controlla un paziente alla volta).""",
    fn=bmi,
    cases=[dict(altezza=1.73, peso=86, visible=True), dict(altezza=1.81, peso=60, visible=True),
           dict(altezza=2, peso=100, boundary=True, hint="BMI esattamente 25: la tabella dice 25 ≤ BMI < 30 → Sovrappeso. Se il tuo codice dice Normopeso, guarda il confronto sulla soglia."),
           dict(altezza=2, peso=74, boundary=True, hint="BMI 18,5 esatto: è Normopeso, perché la soglia 18,5 è compresa nel normopeso."),
           dict(altezza=2, peso=120, boundary=True), dict(altezza=2, peso=140, boundary=True), dict(altezza=2, peso=160, boundary=True), dict(altezza=1.6, peso=45)],
    skeleton="altezza <- 1.73\npeso <- 86\n\n# alla fine deve esistere la variabile classificazione (testo)\n",
    solution='altezza <- 1.73\npeso <- 86\n\nbmi <- peso / altezza^2\n\nif(bmi < 18.5){\n  classificazione <- "Sottopeso"\n}else if(bmi < 25){\n  classificazione <- "Normopeso"\n}else if(bmi < 30){\n  classificazione <- "Sovrappeso"\n}else if(bmi < 35){\n  classificazione <- "Obesità grado I"\n}else if(bmi < 40){\n  classificazione <- "Obesità grado II"\n}else{\n  classificazione <- "Obesità grado III"\n}\nclassificazione\n')

def taxi(distanza):
    costo = 0
    for km in distanza:
        v = km * 60
        costo += 28 / 60 if v < 20 else 1.14 * km
    return r2(costo)
lab('taxi', title='Taxi a Roma', modulo=3, order=2, level='base', language='R', ai_mode='off',
    objective="Calcolare il costo di una corsa in taxi a Roma a partire dai km percorsi in ogni minuto.",
    inputs=[dict(name='distanza', type='vettore di numeri', desc='km percorsi in ciascun minuto della corsa')],
    risultato=dict(name='costo', type='numero', desc='costo totale in euro, 2 decimali'),
    rules="""- In ogni minuto il tassametro sceglie la tariffa in base alla velocità di quel minuto: `velocita = km * 60` (km/h).
- Velocità **sotto i 20 km/h** → tariffa oraria: 28 €/h, cioè 28/60 € per quel minuto.
- Velocità di 20 km/h o più → tariffa chilometrica: 1,14 € per km percorso in quel minuto.
- Il costo è la somma dei minuti. Arrotonda a due decimali.""",
    fn=taxi,
    cases=[dict(distanza=[1, 0.3, 0.5, 0.8, 0.2], visible=True), dict(distanza=[0.5, 0.5, 0.5], visible=True),
           dict(distanza=[0.1], boundary=True, hint="Un solo minuto a 6 km/h: costa un sessantesimo della tariffa oraria."),
           dict(distanza=[0.35, 0.3], boundary=True, hint="21 km/h e 18 km/h: il primo minuto è a km, il secondo a tempo."),
           dict(distanza=[0, 0, 0, 0], boundary=True, hint="Taxi fermo per quattro minuti: la velocità è zero, ma il tassametro corre a tempo."),
           dict(distanza=[2, 1.5, 1.2])],
    skeleton="distanza <- c(1, 0.3, 0.5, 0.8, 0.2)\n\n# alla fine deve esistere la variabile costo\n",
    solution="distanza <- c(1, 0.3, 0.5, 0.8, 0.2)\n\ntariffa_min <- 28/60\ntariffa_km <- 1.14\ncosto <- 0\n\nfor(i in 1:length(distanza)){\n  velocita <- distanza[i] * 60\n  if(velocita < 20){\n    costo <- costo + tariffa_min\n  }else{\n    costo <- costo + tariffa_km * distanza[i]\n  }\n}\ncosto <- round(costo, 2)\ncosto\n")

lab('autovelox-funzione', title='Autovelox come funzione', modulo=3, order=3, level='base', language='R', ai_mode='off',
    objective="Riscrivere l'autovelox come funzione `multa(velocita, limite)` riutilizzabile, e verificarla con gli stessi casi del modulo 2.",
    inputs=[dict(name='velocita', type='numero'), dict(name='limite', type='numero')],
    risultato=dict(name='multa', type='numero', desc='valore restituito dalla funzione'), function='multa',
    rules="""- Stesse regole dell'[Autovelox](../autovelox/): 0 / 36 / 148 / 370 / 500 € per le fasce "entro il limite", "non oltre 10", "non oltre 40", "non oltre 60", "oltre 60".
- Il codice deve **definire** la funzione `multa <- function(velocita, limite){ ... }` che **restituisce** l'importo (ultima espressione o `return()`).
- La verifica chiama la tua funzione con i valori di ogni caso: non servono assegnazioni di prova.
- In RStudio, usala su un vettore di veicoli con un ciclo `for` e conta quante multe superano i 100 €.""",
    fn=autovelox,
    cases=[dict(velocita=45, limite=50, visible=True), dict(velocita=75, limite=50, visible=True),
           dict(velocita=60, limite=50, boundary=True), dict(velocita=90, limite=50, boundary=True), dict(velocita=110, limite=50, boundary=True), dict(velocita=111, limite=50, boundary=True), dict(velocita=50, limite=50, boundary=True)],
    skeleton="multa <- function(velocita, limite){\n  # calcola e restituisci l'importo\n\n}\n\n# prova: multa(75, 50)\n",
    solution="multa <- function(velocita, limite){\n  differenza <- velocita - limite\n  if(differenza <= 0){\n    importo <- 0\n  }else if(differenza <= 10){\n    importo <- 36\n  }else if(differenza <= 40){\n    importo <- 148\n  }else if(differenza <= 60){\n    importo <- 370\n  }else{\n    importo <- 500\n  }\n  return(importo)\n}\n\nmulta(75, 50)\n")

def taxi2(distanza, giorno, ora, costo_uber):
    if 6 <= ora < 22: fisso = 5 if giorno == 'D' else 3
    else: fisso = 7
    c = fisso
    for km in distanza:
        v = km * 60
        c += 28 / 60 if v < 20 else 1.14 * km
    return "Uber" if costo_uber < c else "Taxi"
lab('taxi-uber', title='Taxi o Uber?', modulo=3, order=4, level='extra', language='R', ai_mode='off',
    objective="Aggiungere al taxi la quota fissa (giorno e ora) e decidere se conviene il taxi o Uber.",
    inputs=[dict(name='distanza', type='vettore di numeri', desc='km per minuto'), dict(name='giorno', type='testo', desc='iniziale del giorno: "L","M","M","G","V","S","D"'), dict(name='ora', type='numero', desc='ora di partenza, da 0 a 23'), dict(name='costo_uber', type='numero', desc='prezzo proposto da Uber')],
    risultato=dict(name='decisione', type='testo', desc='"Taxi" oppure "Uber"'),
    rules="""- **Quota fissa**: giorni feriali dalle 6 alle 21 (ora < 22) 3 €; domenica ("D") nella stessa fascia 5 €; **notturna** (dalle 22 in poi o prima delle 6, qualsiasi giorno) 7 €.
- **Quota variabile**: come nel lab Taxi (28 €/h sotto i 20 km/h, 1,14 €/km altrimenti).
- Si sceglie "Uber" solo se costa **strettamente meno** del taxi; a parità, "Taxi".""",
    fn=taxi2,
    cases=[dict(distanza=[1, 0.3, 0.5, 0.8, 0.2], giorno='D', ora=12, costo_uber=9, visible=True), dict(distanza=[1, 0.3, 0.5, 0.8, 0.2], giorno='L', ora=12, costo_uber=9, visible=True),
           dict(distanza=[1, 0.3, 0.5, 0.8, 0.2], giorno='L', ora=22, costo_uber=9, boundary=True, hint="Alle 22 è già tariffa notturna (7 €): il taxi costa più di 9 €?"),
           dict(distanza=[1, 0.3, 0.5, 0.8, 0.2], giorno='L', ora=21, costo_uber=9, boundary=True),
           dict(distanza=[1, 0.3, 0.5, 0.8, 0.2], giorno='L', ora=6, costo_uber=9, boundary=True, hint="Alle 6 in punto è già tariffa diurna."),
           dict(distanza=[1, 0.3, 0.5, 0.8, 0.2], giorno='L', ora=5, costo_uber=9, boundary=True),
           dict(distanza=[0.5, 0.5], giorno='M', ora=10, costo_uber=4.14, boundary=True, hint="A parità di prezzo la regola dice Taxi: il confronto è < oppure <=?"),
           dict(distanza=[0.5, 0.5], giorno='D', ora=10, costo_uber=6)],
    skeleton='distanza <- c(1, 0.3, 0.5, 0.8, 0.2)\ngiorno <- "D"\nora <- 12\ncosto_uber <- 9\n\n# alla fine deve esistere la variabile decisione ("Taxi" o "Uber")\n',
    solution='distanza <- c(1, 0.3, 0.5, 0.8, 0.2)\ngiorno <- "D"\nora <- 12\ncosto_uber <- 9\n\nif(ora >= 6 & ora < 22){\n  if(giorno == "D"){\n    costo <- 5\n  }else{\n    costo <- 3\n  }\n}else{\n  costo <- 7\n}\n\nfor(i in 1:length(distanza)){\n  velocita <- distanza[i] * 60\n  if(velocita < 20){\n    costo <- costo + 28/60\n  }else{\n    costo <- costo + 1.14 * distanza[i]\n  }\n}\n\nif(costo_uber < costo){\n  decisione <- "Uber"\n}else{\n  decisione <- "Taxi"\n}\ndecisione\n')

def portafoglio(rendimenti):
    m = 100
    for r in rendimenti: m *= (1 + r)
    return r2(m)
lab('portafoglio', title='Portafoglio', modulo=3, order=5, level='extra', language='R', ai_mode='on',
    objective="Calcolare il valore finale di 100 € investiti, dato il vettore dei rendimenti giornalieri.",
    inputs=[dict(name='rendimenti', type='vettore di numeri', desc='rendimento di ogni giorno in frazione, es. 0.01 = +1%')],
    risultato=dict(name='valore_finale', type='numero', desc='valore dei 100 € iniziali alla fine, 2 decimali'),
    rules="""- Si parte da 100 €. Ogni giorno il valore viene moltiplicato per `(1 + rendimento)` di quel giorno.
- Un rendimento di −1 (−100%) azzera il capitale: da lì in poi resta zero.
- Arrotonda a due decimali. Fallo con un ciclo `for`; se conosci `prod()` usalo per controllare.""",
    fn=portafoglio,
    cases=[dict(rendimenti=[0.01, -0.02, 0.03], visible=True), dict(rendimenti=[0.1, 0.1], visible=True),
           dict(rendimenti=[0.05], boundary=True, hint="Un solo giorno: il ciclo deve funzionare anche con un vettore di lunghezza 1."),
           dict(rendimenti=[0.2, -1, 0.5], boundary=True, hint="Dopo un −100% il valore è zero e resta zero: 0 × 1,5 = 0."),
           dict(rendimenti=[0, 0, 0], boundary=True), dict(rendimenti=[-0.5, 1])],
    skeleton="rendimenti <- c(0.01, -0.02, 0.03)\n\n# alla fine deve esistere la variabile valore_finale\n",
    solution="rendimenti <- c(0.01, -0.02, 0.03)\n\nvalore_finale <- 100\nfor(i in 1:length(rendimenti)){\n  valore_finale <- valore_finale * (1 + rendimenti[i])\n}\nvalore_finale <- round(valore_finale, 2)\nvalore_finale\n")

def rata(capitale, tasso, anni):
    n = anni * 12
    if tasso == 0: return r2(capitale / n)
    i = tasso / 100 / 12
    return r2(capitale * i / (1 - (1 + i) ** (-n)))
lab('rata-mutuo', title='Rata del mutuo', modulo=3, order=6, level='extra', language='R', ai_mode='on',
    objective="Scrivere la funzione `rata(capitale, tasso, anni)` che calcola la rata mensile di un mutuo a rata costante.",
    inputs=[dict(name='capitale', type='numero', desc='importo del mutuo'), dict(name='tasso', type='numero', desc='tasso annuo in percentuale, es. 4 per il 4%'), dict(name='anni', type='numero', desc='durata in anni')],
    risultato=dict(name='rata', type='numero', desc='rata mensile, 2 decimali'), function='rata',
    rules="""- Tasso mensile `i = tasso/100/12`, numero di rate `n = anni * 12`.
- Formula della rata costante (ammortamento "alla francese"): `rata = capitale * i / (1 - (1 + i)^(-n))`.
- **Se il tasso è zero** la formula divide per zero: in quel caso la rata è semplicemente `capitale / n`.
- Restituisci la rata arrotondata a due decimali.""",
    fn=rata,
    cases=[dict(capitale=150000, tasso=4, anni=25, visible=True), dict(capitale=10000, tasso=6, anni=1, visible=True),
           dict(capitale=12000, tasso=0, anni=1, boundary=True, hint="Tasso zero: la formula dà NaN (0/0). Serve un caso a parte: capitale diviso numero di rate."),
           dict(capitale=100000, tasso=0.5, anni=30), dict(capitale=5000, tasso=12, anni=2)],
    skeleton="rata <- function(capitale, tasso, anni){\n  # calcola e restituisci la rata mensile\n\n}\n\n# prova: rata(150000, 4, 25)\n",
    solution="rata <- function(capitale, tasso, anni){\n  n <- anni * 12\n  if(tasso == 0){\n    importo <- capitale / n\n  }else{\n    i <- tasso / 100 / 12\n    importo <- capitale * i / (1 - (1 + i)^(-n))\n  }\n  return(round(importo, 2))\n}\n\nrata(150000, 4, 25)\n")

def sconto(totale_carrello, tessera):
    s = 0
    if totale_carrello >= 250: s = 10
    elif totale_carrello >= 100: s = 5
    if tessera == 'silver': s += 2
    elif tessera == 'gold': s += 7
    s = min(s, 15)
    return r2(totale_carrello * (1 - s / 100))
lab('sconto-fedelta', title='Sconto fedeltà', modulo=3, order=7, level='sfida', language='R', ai_mode='on',
    objective="Scrivere la specifica e il codice di un programma fedeltà: sconto a soglie più bonus tessera, con un tetto massimo.",
    inputs=[dict(name='totale_carrello', type='numero'), dict(name='tessera', type='testo', desc='"nessuna", "silver" o "gold"')],
    risultato=dict(name='totale_scontato', type='numero', desc='importo da pagare, 2 decimali'),
    rules="""- Sconto base: 0% sotto i 100 €; 5% da 100 € in su; 10% da 250 € in su.
- Bonus tessera in punti percentuali: silver +2, gold +7, nessuna +0.
- Lo sconto complessivo non può superare il 15%.
- Prima di scrivere codice, scrivi tu la specifica completa (input, output, casi limite) e passala all'assistente in modalità *sviluppo assistito*.""",
    fn=sconto,
    cases=[dict(totale_carrello=80, tessera='nessuna', visible=True), dict(totale_carrello=300, tessera='gold', visible=True),
           dict(totale_carrello=100, tessera='nessuna', boundary=True), dict(totale_carrello=250, tessera='silver', boundary=True),
           dict(totale_carrello=250, tessera='gold', boundary=True), dict(totale_carrello=99.99, tessera='gold', boundary=True), dict(totale_carrello=120, tessera='silver')],
    skeleton='totale_carrello <- 80\ntessera <- "nessuna"\n\n# alla fine deve esistere la variabile totale_scontato\n',
    solution='totale_carrello <- 80\ntessera <- "nessuna"\n\nif(totale_carrello >= 250){\n  sconto <- 10\n}else if(totale_carrello >= 100){\n  sconto <- 5\n}else{\n  sconto <- 0\n}\n\nif(tessera == "silver"){\n  sconto <- sconto + 2\n}else if(tessera == "gold"){\n  sconto <- sconto + 7\n}\n\nif(sconto > 15){\n  sconto <- 15\n}\ntotale_scontato <- round(totale_carrello * (1 - sconto/100), 2)\ntotale_scontato\n')

# ─────────────────────────── SETTIMANA 4 (dati) ───────────────────────────
import pandas as pd
HERE = os.path.dirname(__file__)
tit = pd.read_csv(os.path.join(HERE, '..', 'dati', 'titanic.csv'))
eco = pd.read_csv(os.path.join(HERE, '..', 'dati', 'ecommerce.csv'))
fin = pd.read_csv(os.path.join(HERE, '..', 'dati', 'finanza.csv'))

lab('ecommerce-giovani', title='Clienti giovani', modulo=4, order=1, level='base', language='R', ai_mode='off',
    objective="Contare gli ordini fatti da clienti con meno di 35 anni nel dataset ecommerce.",
    inputs=[dict(name='data', type='data frame', desc='già caricato: il file ecommerce.csv (colonne CustomerID, OrderID, OrderDate, Age, Gender, Membership, ProductCategory, ProductName, UnitPrice, Quantity, TotalAmount, PaymentMethod, City, ReturnStatus)')],
    risultato=dict(name='n_giovani', type='numero', desc='numero di righe con Age < 35'),
    data_url='dati/ecommerce.csv', data_var='data', packages=['dplyr'],
    rules="""- Il data frame `data` è già caricato quando premi Verifica (in RStudio: `data <- read.csv("ecommerce.csv")`).
- Conta le righe con `Age < 35`. La colonna `Age` ha valori mancanti: decidi cosa farne e scrivilo nel codice, non lasciarlo al caso.
- Il risultato deve essere un **numero** (non una tabella): da una pipeline dplyr, estrailo con `$n` oppure usa `nrow()` / `sum()`.""",
    fixed=[dict(expected=int((eco.Age < 35).sum()), visible=True, hint="Ricorda: gli NA in Age non sono né < 35 né >= 35. Con filter() spariscono in silenzio; con sum(data$Age < 35) restituiscono NA se non usi na.rm = TRUE.")],
    skeleton="library(dplyr)\n# data è già caricato\n\n# alla fine deve esistere la variabile n_giovani (un numero)\n",
    solution='library(dplyr)\n\nn_giovani <- data %>%\n  filter(!is.na(Age), Age < 35) %>%\n  summarise(n = n())\nn_giovani <- n_giovani$n\nn_giovani\n')

lab('titanic-over50', title='Titanic: gli over 50', modulo=4, order=2, level='base', language='R', ai_mode='off',
    objective="Quante persone con più di 50 anni erano a bordo del Titanic?",
    inputs=[dict(name='titanic', type='data frame', desc='già caricato: titanic.csv (PassengerId, Survived, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked)')],
    risultato=dict(name='n_over50', type='numero', desc='passeggeri con Age > 50'),
    data_url='dati/titanic.csv', data_var='titanic', packages=['dplyr'],
    rules="""- Conta i passeggeri con `Age > 50` (età nota).
- Estrai il numero dalla tabella di `summarise()`.
- Poi, in RStudio, continua con le altre domande del modulo: la percentuale di uomini e donne tra gli over 50 (percentuale *rispetto a chi?*).""",
    fixed=[dict(expected=int((tit.Age > 50).sum()), visible=True, hint="177 passeggeri non hanno l'età: filter(Age > 50) li scarta da solo, ma devi saperlo e dirlo.")],
    skeleton="library(dplyr)\n# titanic è già caricato\n\n# alla fine deve esistere la variabile n_over50 (un numero)\n",
    solution='library(dplyr)\n\nrisultato <- titanic %>%\n  filter(!is.na(Age), Age > 50) %>%\n  summarise(n = n())\nn_over50 <- risultato$n\nn_over50\n')

lab('titanic-prima-classe', title='Titanic: sopravvivenza in prima classe', modulo=4, order=3, level='extra', language='R', ai_mode='on',
    objective="Qual è la percentuale di sopravvissuti tra i passeggeri di prima classe?",
    inputs=[dict(name='titanic', type='data frame', desc='già caricato: titanic.csv')],
    risultato=dict(name='perc_prima', type='numero', desc='quota di sopravvissuti in prima classe, tra 0 e 1 (3 decimali)'),
    data_url='dati/titanic.csv', data_var='titanic', packages=['dplyr'], tolerance=0.002,
    rules="""- `Survived` vale 1 se sopravvissuto, 0 altrimenti: la **media** di Survived è già la percentuale.
- Raggruppa per `Pclass`, calcola la media per classe, poi estrai il valore della classe 1.
- Confronta con la terza classe: la differenza è il punto della domanda.""",
    fixed=[dict(expected=round(float(tit[tit.Pclass == 1].Survived.mean()), 3), visible=True, hint="La percentuale è calcolata *dentro* la classe (denominatore: i passeggeri di prima classe), non sul totale dei sopravvissuti.")],
    skeleton="library(dplyr)\n# titanic è già caricato\n\n# alla fine deve esistere la variabile perc_prima (un numero tra 0 e 1)\n",
    solution='library(dplyr)\n\ntabella <- titanic %>%\n  group_by(Pclass) %>%\n  summarise(perc = mean(Survived))\nperc_prima <- round(tabella$perc[tabella$Pclass == 1], 3)\nperc_prima\n')

lab('titanic-biglietti', title='Titanic: biglietti condivisi', modulo=4, order=4, level='sfida', language='R', ai_mode='on',
    objective="Quanti biglietti erano associati a più di un passeggero?",
    inputs=[dict(name='titanic', type='data frame', desc='già caricato: titanic.csv')],
    risultato=dict(name='n_condivisi', type='numero', desc='numero di codici Ticket con almeno 2 passeggeri'),
    data_url='dati/titanic.csv', data_var='titanic', packages=['dplyr'],
    rules="""- Raggruppa per `Ticket`, conta i passeggeri per biglietto, tieni solo i biglietti con più di uno.
- Il risultato è il numero di **biglietti**, non di passeggeri.
- Servono due passaggi di conteggio: uno dentro i gruppi, uno sul risultato.""",
    fixed=[dict(expected=int((tit.Ticket.value_counts() > 1).sum()), visible=False, hint="Stai contando biglietti o passeggeri? Dopo il primo summarise ogni riga è un biglietto: contale con nrow() o n().")],
    skeleton="library(dplyr)\n# titanic è già caricato\n\n# alla fine deve esistere la variabile n_condivisi (un numero)\n",
    solution='library(dplyr)\n\nbiglietti <- titanic %>%\n  group_by(Ticket) %>%\n  summarise(n = n()) %>%\n  filter(n > 1)\nn_condivisi <- nrow(biglietti)\nn_condivisi\n')

# ─────────────────────────── SETTIMANA 5 ───────────────────────────
lab('finanza-volatilita', title='Finanza: la volatilità', modulo=5, order=1, level='base', language='R', ai_mode='off',
    objective="Calcolare la volatilità (deviazione standard dei rendimenti giornalieri) del titolo Unicredit.",
    inputs=[dict(name='returns', type='data frame', desc='già caricato: finanza.csv (Ferrari, Enel, Intesa, Unicredit, day) con i rendimenti giornalieri del 2023')],
    risultato=dict(name='volatilita', type='numero', desc='deviazione standard dei rendimenti di Unicredit (4 decimali)'),
    data_url='dati/finanza.csv', data_var='returns', tolerance=0.0002,
    rules="""- In finanza il rischio di un titolo si misura con la **variabilità** dei suoi rendimenti: `sd()`.
- Calcola `sd(returns$Unicredit)` e arrotonda a 4 decimali.
- In RStudio confronta le quattro azioni: quale ha il rendimento medio più alto? quale il rischio più alto? coincidono?""",
    fixed=[dict(expected=round(float(fin.Unicredit.std(ddof=1)), 4), visible=True, hint="sd() usa n−1 al denominatore: è quella che vogliamo. Non c'è nessun NA, quindi non serve na.rm.")],
    skeleton="# returns è già caricato\n\n# alla fine deve esistere la variabile volatilita\n",
    solution="volatilita <- round(sd(returns$Unicredit), 4)\nvolatilita\n")

lab('finanza-correlazione', title='Finanza: due banche', modulo=5, order=2, level='extra', language='R', ai_mode='on',
    objective="Misurare quanto i rendimenti di Intesa e Unicredit si muovono insieme.",
    inputs=[dict(name='returns', type='data frame', desc='già caricato: finanza.csv')],
    risultato=dict(name='correlazione', type='numero', desc='coefficiente di correlazione tra Intesa e Unicredit (3 decimali)'),
    data_url='dati/finanza.csv', data_var='returns', tolerance=0.002,
    rules="""- `cor(x, y)` misura quanto due serie salgono e scendono insieme: da −1 a +1.
- Calcola la correlazione tra `Intesa` e `Unicredit` e arrotonda a 3 decimali.
- Poi in RStudio fai il grafico a dispersione con ggplot2 e confronta con la coppia Ferrari–Enel.""",
    fixed=[dict(expected=round(float(fin.Intesa.corr(fin.Unicredit)), 3), visible=True, hint="La correlazione è simmetrica: cor(Intesa, Unicredit) = cor(Unicredit, Intesa). Se ottieni un numero diverso, forse hai preso una colonna sbagliata.")],
    skeleton="# returns è già caricato\n\n# alla fine deve esistere la variabile correlazione\n",
    solution="correlazione <- round(cor(returns$Intesa, returns$Unicredit), 3)\ncorrelazione\n")


# ─────────────────────────── NUOVI LAB 2026 (servizi, retail, personale) ───────────────────────────
# ── modulo 1: aritmetica e confronti ──
def spedizione(totale): return totale >= 49.90
lab('spedizione-gratis', title='Spedizione gratis?', modulo=1, order=2, level='base', language='R', ai_mode='off',
    objective="Dire se un carrello ha diritto alla spedizione gratuita, che scatta da 49,90 € in su.",
    inputs=[dict(name='totale', type='numero', desc='valore del carrello in euro')],
    risultato=dict(name='gratis', type='logico', desc='TRUE se la spedizione è gratuita, FALSE altrimenti'),
    rules="""- La spedizione è gratuita se il totale è **almeno** 49,90 €.
- Il risultato è un valore logico (`TRUE`/`FALSE`), ottenuto da un confronto: non serve nessun `if`.""",
    fn=spedizione,
    cases=[dict(totale=60, visible=True), dict(totale=20, visible=True),
           dict(totale=49.90, boundary=True, hint="49,90 esatti: il testo dice 'da 49,90 in su', quindi è compreso. Il confronto giusto è >=, non >."),
           dict(totale=49.89, boundary=True), dict(totale=0)],
    solution="totale <- 60\n\ngratis <- totale >= 49.90\ngratis\n")

def costo_dip(lordo_mensile): return r2(lordo_mensile * 13 * 1.30)
lab('costo-dipendente', title='Quanto costa un dipendente', modulo=1, order=3, level='base', language='R', ai_mode='off',
    objective="Calcolare il costo annuo di un dipendente per l'azienda a partire dal lordo mensile.",
    inputs=[dict(name='lordo_mensile', type='numero', desc='stipendio lordo mensile in euro')],
    risultato=dict(name='costo_annuo', type='numero', desc='costo annuo per l\'azienda, 2 decimali'),
    rules="""- Le mensilità sono **13** (c'è la tredicesima).
- Sul lordo annuo l'azienda paga contributi pari al **30%**: il costo è il lordo annuo più i contributi.
- Arrotonda a due decimali.""",
    fn=costo_dip,
    cases=[dict(lordo_mensile=1800, visible=True), dict(lordo_mensile=2500, visible=True),
           dict(lordo_mensile=0, boundary=True, hint="Con lordo zero il costo è zero: se ottieni altro, hai sommato una cifra fissa da qualche parte."),
           dict(lordo_mensile=1234.56, boundary=True, hint="Con i centesimi conta dove arrotondi: alla fine, sul costo annuo, non sul lordo."),
           dict(lordo_mensile=3100)],
    solution="lordo_mensile <- 1800\n\nlordo_annuo <- lordo_mensile * 13\ncontributi <- lordo_annuo * 0.30\ncosto_annuo <- round(lordo_annuo + contributi, 2)\ncosto_annuo\n")

def pareggio(costi_fissi, prezzo, costo_unitario): return math.ceil(costi_fissi / (prezzo - costo_unitario) - 1e-9)
lab('punto-pareggio', title='Punto di pareggio', modulo=1, order=4, level='sfida', language='R', ai_mode='on',
    objective="Quanti pezzi bisogna vendere in un mese per coprire i costi fissi.",
    inputs=[dict(name='costi_fissi', type='numero', desc='costi fissi mensili in euro'), dict(name='prezzo', type='numero', desc='prezzo di vendita di un pezzo'),
            dict(name='costo_unitario', type='numero', desc='costo variabile di un pezzo')],
    risultato=dict(name='pezzi', type='numero', desc='pezzi da vendere, intero'),
    rules="""- Ogni pezzo venduto contribuisce ai costi fissi per `prezzo - costo_unitario` (il **margine di contribuzione**).
- I pezzi da vendere sono `costi_fissi / margine`, arrotondati **per eccesso** con `ceiling()`: non si vende mezzo pezzo, e con uno in meno non si è ancora in pareggio.""",
    fn=pareggio,
    cases=[dict(costi_fissi=3000, prezzo=8, costo_unitario=3, visible=True), dict(costi_fissi=3000, prezzo=8.5, costo_unitario=3, visible=True),
           dict(costi_fissi=1000, prezzo=12, costo_unitario=2, boundary=True, hint="1000 / 10 fa esattamente 100: ceiling() non deve aggiungere nulla quando la divisione è esatta."),
           dict(costi_fissi=999, prezzo=10, costo_unitario=0, boundary=True, hint="99,9 pezzi: con 99 non si è in pareggio, ne servono 100. round() darebbe 100 per caso, ma con 99,4 sbaglierebbe: usa ceiling()."),
           dict(costi_fissi=5000, prezzo=25, costo_unitario=19.5)],
    solution="costi_fissi <- 3000\nprezzo <- 8\ncosto_unitario <- 3\n\nmargine <- prezzo - costo_unitario\npezzi <- ceiling(costi_fissi / margine)\npezzi\n")

def occupazione(occupate, totali): return round(occupate / totali * 100 + 1e-9, 1)
lab('occupazione-hotel', title='Occupazione dell\'hotel', modulo=1, order=5, level='base', language='R', ai_mode='off',
    objective="Calcolare il tasso di occupazione di un hotel in una notte, in percentuale.",
    inputs=[dict(name='occupate', type='numero', desc='camere occupate'), dict(name='totali', type='numero', desc='camere dell\'hotel')],
    risultato=dict(name='tasso', type='numero', desc='percentuale con un decimale'),
    rules="""- Il tasso di occupazione è `occupate / totali * 100`.
- Arrotonda a **un** decimale.""",
    fn=occupazione,
    cases=[dict(occupate=80, totali=100, visible=True), dict(occupate=37, totali=45, visible=True),
           dict(occupate=0, totali=45, boundary=True), dict(occupate=45, totali=45, boundary=True, hint="Hotel pieno: 100, non 100.0 con decimali strani né 1."),
           dict(occupate=13, totali=120)],
    solution="occupate <- 80\ntotali <- 100\n\ntasso <- round(occupate / totali * 100, 1)\ntasso\n")

# ── modulo 2: decidere ──
def rimborso(prezzo, ritardo):
    if ritardo < 60: return 0
    if ritardo < 120: return r2(prezzo * 0.25)
    return r2(prezzo * 0.50)
lab('rimborso-treno', title='Rimborso per il ritardo del treno', modulo=2, order=3, level='base', language='R', ai_mode='off',
    objective="Calcolare il rimborso dovuto al passeggero in base ai minuti di ritardo all'arrivo.",
    inputs=[dict(name='prezzo', type='numero', desc='prezzo del biglietto in euro'), dict(name='ritardo', type='numero', desc='minuti di ritardo all\'arrivo')],
    risultato=dict(name='rimborso', type='numero', desc='euro da rimborsare, 2 decimali'),
    rules="""- Ritardo **sotto i 60 minuti**: nessun rimborso.
- Da 60 a 119 minuti: rimborso del **25%** del prezzo.
- Da **120 minuti in su**: rimborso del **50%**.
- Arrotonda a due decimali.""",
    fn=rimborso,
    cases=[dict(prezzo=50, ritardo=30, visible=True), dict(prezzo=50, ritardo=75, visible=True),
           dict(prezzo=50, ritardo=60, boundary=True, hint="60 minuti esatti: il rimborso scatta 'da 60 in su'. Il tuo confronto usa < o <=?"),
           dict(prezzo=50, ritardo=59, boundary=True), dict(prezzo=50, ritardo=120, boundary=True, hint="120 esatti è già la fascia del 50%."),
           dict(prezzo=50, ritardo=119, boundary=True), dict(prezzo=89.9, ritardo=200)],
    solution='prezzo <- 50\nritardo <- 30\n\nif(ritardo < 60){\n  rimborso <- 0\n}else if(ritardo < 120){\n  rimborso <- round(prezzo * 0.25, 2)\n}else{\n  rimborso <- round(prezzo * 0.50, 2)\n}\nrimborso\n')

def museo(eta, studente, prima_domenica):
    if prima_domenica: return 0
    if eta < 6 or eta >= 70: return 0
    if eta <= 18 or studente: return 8
    return 15
lab('biglietto-museo', title='Biglietto del museo', modulo=2, order=4, level='base', language='R', ai_mode='off',
    objective="Calcolare il prezzo del biglietto di un museo civico in base a età, tessera studente e giorno.",
    inputs=[dict(name='eta', type='numero', desc='anni del visitatore'), dict(name='studente', type='logico', desc='TRUE se ha la tessera studente'),
            dict(name='prima_domenica', type='logico', desc='TRUE se è la prima domenica del mese')],
    risultato=dict(name='prezzo', type='numero', desc='0, 8 oppure 15'),
    rules="""- La **prima domenica del mese** l'ingresso è gratuito per tutti.
- Negli altri giorni: gratis **sotto i 6 anni** e **dai 70 in su**; ridotto a 8 € **fino ai 18 anni compresi** oppure con tessera studente; intero 15 € per tutti gli altri.
- Le condizioni vanno controllate nell'ordine giusto: prima i casi gratuiti, poi i ridotti.""",
    fn=museo,
    cases=[dict(eta=30, studente=False, prima_domenica=False, visible=True), dict(eta=16, studente=False, prima_domenica=False, visible=True), dict(eta=25, studente=True, prima_domenica=False, visible=True),
           dict(eta=5, studente=False, prima_domenica=False, boundary=True), dict(eta=6, studente=False, prima_domenica=False, boundary=True, hint="6 anni: non è più 'sotto i 6', quindi paga il ridotto."),
           dict(eta=18, studente=False, prima_domenica=False, boundary=True, hint="18 anni compresi: ridotto."), dict(eta=19, studente=False, prima_domenica=False, boundary=True),
           dict(eta=70, studente=False, prima_domenica=False, boundary=True, hint="Dai 70 in su è gratis: 70 compreso."), dict(eta=69, studente=False, prima_domenica=False, boundary=True),
           dict(eta=40, studente=False, prima_domenica=True), dict(eta=75, studente=True, prima_domenica=False, hint="Over 70 con tessera studente: vince il gratis, perché lo controlli prima.")],
    solution='eta <- 30\nstudente <- FALSE\nprima_domenica <- FALSE\n\nif(prima_domenica){\n  prezzo <- 0\n}else if(eta < 6 | eta >= 70){\n  prezzo <- 0\n}else if(eta <= 18 | studente){\n  prezzo <- 8\n}else{\n  prezzo <- 15\n}\nprezzo\n')

def parcheggio(minuti):
    if minuti <= 30: return 0
    return min(12, math.ceil(minuti / 60 - 1e-9) * 1.5)
lab('parcheggio', title='Tariffa del parcheggio', modulo=2, order=5, level='base', language='R', ai_mode='off',
    objective="Calcolare quanto si paga all'uscita di un parcheggio a partire dai minuti di sosta.",
    inputs=[dict(name='minuti', type='numero', desc='minuti di sosta, dall\'ingresso all\'uscita')],
    risultato=dict(name='costo', type='numero', desc='euro da pagare'),
    rules="""- Fino a **30 minuti** la sosta è gratuita.
- Oltre i 30 minuti si paga **1,50 € per ogni ora o frazione di ora**, contando dall'ingresso: 31 minuti sono una frazione della prima ora, 61 minuti sono già due ore.
- Il **massimo giornaliero** è 12 €.""",
    fn=parcheggio,
    cases=[dict(minuti=20, visible=True), dict(minuti=45, visible=True), dict(minuti=150, visible=True),
           dict(minuti=30, boundary=True, hint="30 minuti esatti sono ancora gratis ('fino a 30')."), dict(minuti=31, boundary=True),
           dict(minuti=60, boundary=True, hint="60 minuti sono un'ora esatta, non due: ceiling(60/60) = 1."), dict(minuti=61, boundary=True),
           dict(minuti=480, boundary=True, hint="8 ore fanno esattamente 12 €: il tetto non taglia nulla."), dict(minuti=600, hint="10 ore farebbero 15 €, ma il massimo giornaliero è 12.")],
    solution='minuti <- 45\n\nif(minuti <= 30){\n  costo <- 0\n}else{\n  ore <- ceiling(minuti / 60)\n  costo <- ore * 1.5\n  if(costo > 12){\n    costo <- 12\n  }\n}\ncosto\n')

# ── modulo 3: vettori, cicli, funzioni ──
def sotto_scorta(giacenza, soglia): return sum(1 for g, s in zip(giacenza, soglia) if g < s)
lab('sotto-scorta', title='Prodotti sotto scorta', modulo=3, order=4, level='base', language='R', ai_mode='off',
    objective="Contare quanti prodotti del magazzino sono scesi sotto la loro scorta minima e vanno riordinati.",
    inputs=[dict(name='giacenza', type='vettore di numeri', desc='pezzi in magazzino, un valore per prodotto'), dict(name='soglia', type='vettore di numeri', desc='scorta minima di ciascun prodotto, stesso ordine')],
    risultato=dict(name='da_riordinare', type='numero', desc='numero di prodotti con giacenza sotto la soglia'),
    rules="""- I due vettori hanno la stessa lunghezza: il prodotto `i` ha giacenza `giacenza[i]` e soglia `soglia[i]`.
- Un prodotto va riordinato se la giacenza è **strettamente minore** della soglia: alla soglia esatta è ancora a posto.
- Scorri i prodotti con un ciclo `for` e conta; poi, in RStudio, prova a farlo senza ciclo con `sum(giacenza < soglia)`.""",
    fn=sotto_scorta,
    cases=[dict(giacenza=[12, 3, 40, 0], soglia=[10, 5, 20, 2], visible=True), dict(giacenza=[5, 5, 5], soglia=[5, 5, 5], visible=True),
           dict(giacenza=[4, 5, 6], soglia=[5, 5, 5], boundary=True, hint="Solo il primo è sotto: 5 non è 'sotto 5'."),
           dict(giacenza=[0], soglia=[1], boundary=True), dict(giacenza=[0, 0, 0], soglia=[0, 0, 0], boundary=True, hint="Giacenza zero con soglia zero: non è sotto soglia."),
           dict(giacenza=[100, 2, 7, 30, 1], soglia=[50, 3, 7, 40, 5])],
    solution="giacenza <- c(12, 3, 40, 0)\nsoglia <- c(10, 5, 20, 2)\n\nda_riordinare <- 0\nfor(i in 1:length(giacenza)){\n  if(giacenza[i] < soglia[i]){\n    da_riordinare <- da_riordinare + 1\n  }\n}\nda_riordinare\n")

def straordinari(ore, paga_oraria):
    tot = 0
    for h in ore:
        tot += min(h, 8) * paga_oraria + max(h - 8, 0) * paga_oraria * 1.3
    return r2(tot)
lab('straordinari', title='Straordinari della settimana', modulo=3, order=5, level='base', language='R', ai_mode='on',
    objective="Calcolare la paga settimanale di un addetto a partire dalle ore lavorate ogni giorno, con la maggiorazione per gli straordinari.",
    inputs=[dict(name='ore', type='vettore di numeri', desc='ore lavorate in ciascun giorno della settimana'), dict(name='paga_oraria', type='numero', desc='euro per ora ordinaria')],
    risultato=dict(name='paga', type='numero', desc='paga della settimana in euro, 2 decimali'),
    rules="""- In ogni giorno le prime **8 ore** sono ordinarie e si pagano a `paga_oraria`.
- Le ore **oltre l'ottava**, giorno per giorno, sono straordinario e si pagano al **130%** (`paga_oraria * 1.3`).
- La paga è la somma dei giorni. Arrotonda a due decimali.
- Il conteggio è per giorno: 9 ore il lunedì e 7 il martedì fanno un'ora di straordinario, non zero.""",
    fn=straordinari,
    cases=[dict(ore=[8, 8, 8, 8, 8], paga_oraria=12, visible=True), dict(ore=[9, 8, 10, 8, 7], paga_oraria=12, visible=True),
           dict(ore=[9, 7], paga_oraria=10, boundary=True, hint="Le ore si compensano tra giorni? No: 9 e 7 danno un'ora di straordinario e sette ordinarie il secondo giorno."),
           dict(ore=[8.5, 8, 8, 8, 8], paga_oraria=10, boundary=True), dict(ore=[0, 0, 0, 0, 0], paga_oraria=15, boundary=True),
           dict(ore=[12, 12, 12, 12, 12], paga_oraria=10), dict(ore=[6, 6, 6], paga_oraria=11.5)],
    solution="ore <- c(8, 8, 8, 8, 8)\npaga_oraria <- 12\n\npaga <- 0\nfor(i in 1:length(ore)){\n  if(ore[i] > 8){\n    ordinarie <- 8\n    extra <- ore[i] - 8\n  }else{\n    ordinarie <- ore[i]\n    extra <- 0\n  }\n  paga <- paga + ordinarie * paga_oraria + extra * paga_oraria * 1.3\n}\npaga <- round(paga, 2)\npaga\n")

def nps(voti):
    prom = sum(1 for v in voti if v >= 9); det = sum(1 for v in voti if v <= 6)
    return round((prom - det) / len(voti) * 100 + 1e-9, 1)
lab('nps', title='Net Promoter Score', modulo=3, order=6, level='base', language='R', ai_mode='on',
    objective="Calcolare l'NPS di un servizio a partire dai voti da 0 a 10 dati dai clienti alla domanda «lo consiglieresti?».",
    inputs=[dict(name='voti', type='vettore di numeri', desc='un voto da 0 a 10 per ogni cliente intervistato')],
    risultato=dict(name='nps', type='numero', desc='da −100 a 100, un decimale'),
    rules="""- I clienti con voto **9 o 10** sono *promotori*; quelli con voto **da 0 a 6** sono *detrattori*; 7 e 8 sono *passivi* e non contano.
- `NPS = (promotori − detrattori) / totale intervistati × 100`.
- Arrotonda a un decimale. Contali con un ciclo e due contatori; in RStudio confronta con `sum(voti >= 9)`.""",
    fn=nps,
    cases=[dict(voti=[10, 9, 8, 7, 6, 10], visible=True), dict(voti=[9, 9, 9], visible=True),
           dict(voti=[8, 9], boundary=True, hint="8 è passivo, 9 è promotore: (1 − 0) / 2 = 50."), dict(voti=[6, 7], boundary=True, hint="6 è detrattore, 7 è passivo: (0 − 1) / 2 = −50."),
           dict(voti=[7, 8, 8, 7], boundary=True, hint="Solo passivi: il denominatore li conta comunque, NPS 0."), dict(voti=[6, 6]),
           dict(voti=[10, 0, 5, 9, 7, 3, 8, 9, 10, 2])],
    solution="voti <- c(10, 9, 8, 7, 6, 10)\n\npromotori <- 0\ndetrattori <- 0\nfor(i in 1:length(voti)){\n  if(voti[i] >= 9){\n    promotori <- promotori + 1\n  }else if(voti[i] <= 6){\n    detrattori <- detrattori + 1\n  }\n}\nnps <- round((promotori - detrattori) / length(voti) * 100, 1)\nnps\n")

def provvigioni(vendite):
    tot = 0
    for v in vendite:
        tot += min(v, 10000) * 0.03
        if v > 10000: tot += (min(v, 20000) - 10000) * 0.05
        if v > 20000: tot += (v - 20000) * 0.08
    return r2(tot)
lab('provvigioni', title='Provvigioni dell\'agente', modulo=3, order=8, level='sfida', language='R', ai_mode='on',
    objective="Calcolare le provvigioni annue di un agente di commercio a partire dal venduto di ciascun mese, con scaglioni progressivi.",
    inputs=[dict(name='vendite', type='vettore di numeri', desc='venduto in euro in ciascuno dei 12 mesi')],
    risultato=dict(name='provvigioni', type='numero', desc='totale annuo in euro, 2 decimali'),
    rules="""- In ogni mese: **3%** sul venduto fino a 10.000 €; **5%** sulla parte tra 10.000 e 20.000 €; **8%** sulla parte oltre 20.000 €.
- Gli scaglioni sono progressivi (come l'IRPEF): ogni aliquota si applica solo alla fetta che cade nella sua fascia.
- Le provvigioni annue sono la somma dei dodici mesi, arrotondata a due decimali.""",
    fn=provvigioni,
    cases=[dict(vendite=[8000] * 12, visible=True), dict(vendite=[15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000], visible=False),
           dict(vendite=[10000] * 12, boundary=True, hint="10.000 esatti stanno tutti nel primo scaglione: 300 al mese."),
           dict(vendite=[20000] * 12, boundary=True, hint="20.000: 300 sul primo scaglione più 500 sul secondo, niente terzo."),
           dict(vendite=[25000] * 12, boundary=True), dict(vendite=[0] * 12, boundary=True),
           dict(vendite=[3000, 12000, 27000, 9999.5, 10000.5, 0, 18000, 22000, 5000, 30000, 11000, 7000])],
    solution="vendite <- c(8000, 8000, 8000, 8000, 8000, 8000, 8000, 8000, 8000, 8000, 8000, 8000)\n\nprovvigioni <- 0\nfor(i in 1:length(vendite)){\n  v <- vendite[i]\n  if(v <= 10000){\n    mese <- v * 0.03\n  }else if(v <= 20000){\n    mese <- 10000 * 0.03 + (v - 10000) * 0.05\n  }else{\n    mese <- 10000 * 0.03 + 10000 * 0.05 + (v - 20000) * 0.08\n  }\n  provvigioni <- provvigioni + mese\n}\nprovvigioni <- round(provvigioni, 2)\nprovvigioni\n")

# ── modulo 4: data frame e dplyr (dataset ecommerce; i valori attesi li calcola R) ──
ECOM = dict(name='data', type='data frame', desc='già caricato: ecommerce.csv (CustomerID, OrderID, OrderDate, Age, Gender, Membership, ProductCategory, ProductName, UnitPrice, Quantity, TotalAmount, PaymentMethod, City, ReturnStatus, Courier, DeliveryDays, Discount)')
lab('fatturato-categoria', title='La categoria che vende di più', modulo=4, order=3, level='base', language='R', ai_mode='off',
    objective="Trovare la categoria di prodotto con il fatturato più alto.",
    inputs=[ECOM], risultato=dict(name='categoria_top', type='testo', desc='il nome della categoria, come scritto nel file'),
    data_url='dati/ecommerce.csv', data_var='data', packages=['dplyr'], r_expected=True,
    rules="""- Il fatturato di una categoria è la somma di `TotalAmount` delle sue righe: `group_by(ProductCategory)` e `summarise(fatturato = sum(TotalAmount))`.
- Ordina con `arrange(desc(fatturato))` e prendi la prima riga.
- Il risultato è il **testo** della categoria (una stringa), non la tabella: estrailo con `$ProductCategory[1]`.""",
    fixed=[dict(visible=False, hint="Vuoi il nome della categoria, non il suo fatturato: dopo arrange, la prima riga della colonna ProductCategory.")],
    solution='library(dplyr)\n\ntabella <- data %>%\n  group_by(ProductCategory) %>%\n  summarise(fatturato = sum(TotalAmount)) %>%\n  arrange(desc(fatturato))\ncategoria_top <- tabella$ProductCategory[1]\ncategoria_top\n')

lab('tasso-reso', title='Quanti ordini tornano indietro', modulo=4, order=4, level='base', language='R', ai_mode='on',
    objective="Calcolare la quota di ordini resi tra quelli pagati con PayPal.",
    inputs=[ECOM], risultato=dict(name='tasso_paypal', type='numero', desc='quota tra 0 e 1, 3 decimali'),
    data_url='dati/ecommerce.csv', data_var='data', packages=['dplyr'], tolerance=0.002, r_expected=True,
    rules="""- `ReturnStatus` vale 1 se l'ordine è stato reso, 0 altrimenti: la sua **media** è già la quota di resi.
- Tieni solo le righe con `PaymentMethod == "PayPal"` e calcola la media; arrotonda a 3 decimali.
- In RStudio confronta i quattro metodi con `group_by(PaymentMethod)`: il reso dipende da come si paga?""",
    fixed=[dict(visible=True, hint="Il denominatore sono gli ordini PayPal, non tutti gli ordini: filtra prima di fare la media.")],
    solution='library(dplyr)\n\npaypal <- data %>%\n  filter(PaymentMethod == "PayPal")\ntasso_paypal <- round(mean(paypal$ReturnStatus), 3)\ntasso_paypal\n')

lab('terza-citta', title='Le città con più ordini', modulo=4, order=5, level='base', language='R', ai_mode='on',
    objective="Trovare la terza città per numero di ordini.",
    inputs=[ECOM], risultato=dict(name='terza', type='testo', desc='il nome della terza città in classifica'),
    data_url='dati/ecommerce.csv', data_var='data', packages=['dplyr'], r_expected=True,
    rules="""- Conta gli ordini per città: `group_by(City)` e `summarise(n = n())`.
- Ordina dalla più grande alla più piccola e prendi la **terza** riga.
- Il risultato è il nome della città (testo).""",
    fixed=[dict(visible=False, hint="Terza riga dopo l'ordinamento decrescente: tabella$City[3]. Se ordini in senso crescente prendi la terzultima.")],
    solution='library(dplyr)\n\nclassifica <- data %>%\n  group_by(City) %>%\n  summarise(n = n()) %>%\n  arrange(desc(n))\nterza <- classifica$City[3]\nterza\n')

lab('categoria-resi', title='La categoria che torna indietro di più', modulo=4, order=6, level='sfida', language='R', ai_mode='on',
    objective="Trovare la categoria di prodotto con il tasso di reso più alto.",
    inputs=[ECOM], risultato=dict(name='categoria_resi', type='testo', desc='il nome della categoria'),
    data_url='dati/ecommerce.csv', data_var='data', packages=['dplyr'], r_expected=True,
    rules="""- Per ogni categoria il tasso di reso è la media di `ReturnStatus` (non la somma: le categorie hanno numeri di ordini diversi).
- Ordina per tasso decrescente e prendi il nome della prima categoria.""",
    fixed=[dict(visible=False, hint="Media, non somma: con la somma vince semplicemente la categoria con più ordini.")],
    solution='library(dplyr)\n\ntabella <- data %>%\n  group_by(ProductCategory) %>%\n  summarise(tasso = mean(ReturnStatus)) %>%\n  arrange(desc(tasso))\ncategoria_resi <- tabella$ProductCategory[1]\ncategoria_resi\n')

# ── modulo 5: leggere i dati ──
lab('rfm-gold', title='Segmenti RFM: quanti clienti Gold', modulo=5, order=1, level='base', language='R', ai_mode='off',
    objective="Costruire le tre metriche RFM dagli scontrini, assegnare i segmenti con case_when e contare i clienti Gold.",
    inputs=[dict(name='scontrini', type='data frame', desc='già caricato: retail_rfm.csv (CustomerID, InvoiceDate, Quantity, UnitPrice, Total), una riga per riga di scontrino')],
    risultato=dict(name='n_gold', type='numero', desc='numero di clienti nel segmento Gold'),
    data_url='dati/retail_rfm.csv', data_var='scontrini', packages=['dplyr'], r_expected=True,
    rules="""- Converti la data con `as.Date(scontrini$InvoiceDate)`; la data di riferimento è l'ultima del file (`max`).
- Per cliente: `recency` = giorni tra la data di riferimento e il suo ultimo acquisto, `frequency` = numero di righe, `monetary` = somma di `Total`.
- Punteggi con `ntile(desc(recency), 4)`, `ntile(frequency, 4)`, `ntile(monetary, 4)`; segmento con il `case_when` della lezione, in quell'ordine, con `TRUE ~ "Altri"` alla fine.
- `n_gold` è il numero di clienti con segmento `"Gold"`: dalla tabella, non a occhio.""",
    fixed=[dict(visible=False, hint="Gold è 4-4-4 su tutti e tre i punteggi, e va controllato per primo nel case_when. Se ottieni un numero diverso, guarda se hai usato desc() sulla recency.")],
    solution='library(dplyr)\n\nscontrini$InvoiceDate <- as.Date(scontrini$InvoiceDate)\ndata_riferimento <- max(scontrini$InvoiceDate)\n\nrfm <- scontrini %>%\n  group_by(CustomerID) %>%\n  summarise(recency = as.numeric(data_riferimento - max(InvoiceDate)),\n            frequency = n(),\n            monetary = sum(Total)) %>%\n  mutate(r_score = ntile(desc(recency), 4),\n         f_score = ntile(frequency, 4),\n         m_score = ntile(monetary, 4)) %>%\n  mutate(segmento = case_when(\n    r_score == 4 & f_score == 4 & m_score == 4 ~ "Gold",\n    r_score == 1 & f_score == 1 & m_score == 1 ~ "Persi",\n    f_score == 4 ~ "Fedeli",\n    r_score == 4 ~ "Attivi",\n    m_score == 4 ~ "Alta spesa",\n    TRUE ~ "Altri"\n  ))\n\ngold <- rfm %>%\n  filter(segmento == "Gold")\nn_gold <- nrow(gold)\nn_gold\n')

lab('corriere-affidabile', title='Il corriere più regolare', modulo=5, order=2, level='base', language='R', ai_mode='off',
    objective="Trovare il corriere con i tempi di consegna più regolari, cioè con la deviazione standard più bassa.",
    inputs=[ECOM], risultato=dict(name='corriere_regolare', type='testo', desc='il nome del corriere'),
    data_url='dati/ecommerce.csv', data_var='data', r_expected=True, packages=['dplyr'],
    rules="""- Regolare non vuol dire veloce: un corriere che consegna sempre in 4 giorni è più prevedibile di uno che va da 1 a 8. La regolarità si misura con `sd(DeliveryDays)`.
- Per corriere: `group_by(Courier)` e `summarise(media = mean(DeliveryDays), variabilita = sd(DeliveryDays))`.
- Ordina per variabilità crescente e prendi il primo nome. In RStudio guarda anche la media: il più regolare è anche il più veloce?""",
    fixed=[dict(visible=False, hint="Ordina per sd crescente (arrange senza desc): il più regolare è quello con la deviazione standard più piccola, non più grande.")],
    solution='library(dplyr)\n\ntabella <- data %>%\n  group_by(Courier) %>%\n  summarise(media = mean(DeliveryDays), variabilita = sd(DeliveryDays)) %>%\n  arrange(variabilita)\ncorriere_regolare <- tabella$Courier[1]\ncorriere_regolare\n')

lab('sconto-quantita', title='Sconto e quantità', modulo=5, order=3, level='base', language='R', ai_mode='on',
    objective="Misurare quanto lo sconto applicato e i pezzi acquistati crescono insieme.",
    inputs=[ECOM], risultato=dict(name='correlazione', type='numero', desc='coefficiente di correlazione, 3 decimali'),
    data_url='dati/ecommerce.csv', data_var='data', tolerance=0.002, r_expected=True,
    rules="""- `cor(x, y)` va da −1 a +1: vicino a +1 le due colonne salgono insieme, vicino a 0 non c'è legame.
- Calcola la correlazione tra `Discount` e `Quantity` e arrotonda a 3 decimali.
- In RStudio fai il grafico a dispersione con ggplot2 e poi confronta con la correlazione tra `Discount` e `TotalAmount`: perché è più bassa?""",
    fixed=[dict(visible=True, hint="La correlazione è simmetrica, cor(a, b) = cor(b, a): se il numero non torna, hai preso una colonna sbagliata (TotalAmount al posto di Quantity?).")],
    solution='correlazione <- round(cor(data$Discount, data$Quantity), 3)\ncorrelazione\n')

lab('ticket-medio', title='Dove si spende di più per ordine', modulo=5, order=4, level='base', language='R', ai_mode='on',
    objective="Trovare la città con lo scontrino medio più alto.",
    inputs=[ECOM], risultato=dict(name='citta_top', type='testo', desc='il nome della città'),
    data_url='dati/ecommerce.csv', data_var='data', packages=['dplyr'], r_expected=True,
    rules="""- Lo **scontrino medio** (ticket medio) di una città è `mean(TotalAmount)` sui suoi ordini: non il fatturato totale, che premia le città grandi.
- Raggruppa per `City`, calcola media e numero di ordini, ordina per media decrescente, prendi il primo nome.
- In RStudio guarda quanto sono vicine le prime tre: la differenza è abbastanza grande da decidere qualcosa?""",
    fixed=[dict(visible=False, hint="Media per città, non somma: con la somma vince la città con più ordini.")],
    solution='library(dplyr)\n\ntabella <- data %>%\n  group_by(City) %>%\n  summarise(ticket = mean(TotalAmount), ordini = n()) %>%\n  arrange(desc(ticket))\ncitta_top <- tabella$City[1]\ncitta_top\n')

lab('assenze-reparto', title='Assenze per reparto', modulo=5, order=5, level='sfida', language='R', ai_mode='on',
    objective="Trovare il reparto con più giorni di assenza per addetto.",
    inputs=[dict(name='personale', type='data frame', desc='già caricato: personale.csv (id, reparto, ruolo, sede, anno_assunzione, stipendio_lordo, giorni_assenza, part_time), una riga per dipendente')],
    risultato=dict(name='reparto_assenze', type='testo', desc='il nome del reparto'),
    data_url='dati/personale.csv', data_var='personale', packages=['dplyr'], r_expected=True,
    rules="""- Il confronto giusto è **per addetto**: giorni di assenza totali del reparto diviso il numero di dipendenti del reparto (cioè la media di `giorni_assenza`).
- Raggruppa per `reparto`, calcola la media, ordina in senso decrescente, prendi il primo nome.""",
    fixed=[dict(visible=False, hint="Per addetto, non totale: Vendite ha più assenze in tutto perché ha più persone. La media di giorni_assenza per reparto è il numero giusto.")],
    solution='library(dplyr)\n\ntabella <- personale %>%\n  group_by(reparto) %>%\n  summarise(addetti = n(), per_addetto = mean(giorni_assenza)) %>%\n  arrange(desc(per_addetto))\nreparto_assenze <- tabella$reparto[1]\nreparto_assenze\n')

# ── lab tolti (finanza e doppioni): restano definiti sopra ma non vengono generati ──
DROP = {'cambio-valuta', 'interesse-composto', 'piano-risparmio', 'autovelox-punti', 'bollo-auto', 'taxi-uber',
        'portafoglio', 'rata-mutuo', 'titanic-prima-classe', 'titanic-biglietti', 'finanza-volatilita', 'finanza-correlazione'}
LABS[:] = [L for L in LABS if L['slug'] not in DROP]
for L in LABS:
    if L['slug'] == 'pricing-voli': L['level'] = 'sfida'; L['order'] = 9; L['ai_mode'] = 'on'

# ─────────────────────────── contesti ───────────────────────────
# Il testo che lo studente legge per primo: la situazione, chi chiede cosa, perché conta.
# Per i lab "difficili" (ex sfida) le regole stanno solo qui, in prosa: non c'è la lista puntata.
CONTESTI = {
'scontrino': """Lavori nel piccolo negozio di elettronica di famiglia e il registratore di cassa si è rotto proprio il giorno dei saldi. Tuo zio ti passa un foglio con i prezzi **netti** dei prodotti, cioè senza IVA, e ti chiede di calcolare a mano quanto far pagare a ogni cliente.

Il primo cliente compra tre cavi HDMI da 10 € l'uno. Tu sai che in Italia l'IVA ordinaria è del 22% e che si applica sul totale della merce, non sul singolo pezzo. Il totale va scritto sullo scontrino con due decimali, come su qualsiasi ricevuta.

Scrivi il programma che, dati prezzo netto e quantità, calcola il totale da pagare. Tuo zio lo userà tutto il giorno, quindi deve funzionare anche nei casi strani: un cliente che ci ripensa e compra zero pezzi, o un prezzo con i centesimi.""",

'cambio-valuta': """Stai partendo per New York e passi da uno sportello di cambio in aeroporto. Sul cartello c'è scritto il tasso del giorno (per esempio 1,08 dollari per un euro) e, in piccolo, la commissione: **2 euro oppure l'1% dell'importo, quello che è maggiore**. La commissione viene trattenuta in euro, prima del cambio: si convertono solo i soldi che restano.

Vuoi sapere in anticipo quanti dollari ricevi per un certo importo, così da decidere se conviene cambiare tanto in una volta o poco alla volta. Ti serve anche capire cosa succede con importi piccoli: se dai allo sportello 2 euro, la commissione se li mangia tutti e non ricevi nulla; con 1 euro, il conto verrebbe addirittura negativo, e lo sportello ovviamente non ti paga per cambiare.

Scrivi il programma che, dati importo in euro e tasso, calcola i dollari ricevuti con due decimali.""",

'interesse-composto': """Tua nonna ha messo da parte 1.000 euro e li vuole lasciare su un conto deposito che rende il 3% all'anno. Ti chiede quanto troverà tra due anni, e poi tra cinque, e poi tra dieci. La banca applica l'**interesse composto**: ogni anno gli interessi si aggiungono al capitale, e l'anno dopo fruttano anche loro.

Il dettaglio che frega tutti è il tasso: la banca lo scrive come percentuale (3), ma nella formula serve come frazione (0,03). Il risultato, come su un estratto conto, va arrotondato a due decimali.

Scrivi il programma che, dati capitale, tasso in percentuale e numero di anni, calcola il montante finale.""",

'piano-risparmio': """Un tuo amico ha appena iniziato a lavorare e vuole mettere via qualcosa ogni anno. Apre un conto con un capitale iniziale, e poi **ogni anno, il giorno dell'anniversario**, la banca prima accredita gli interessi sul saldo di quel momento (con il tasso annuo del conto, espresso in percentuale) e subito dopo lui versa una somma fissa. Vuole sapere quanto avrà sul conto dopo un certo numero di anni.

Ti dà tre esempi per capirsi: con 1.000 euro iniziali, 100 di versamento annuo e il 2%, dopo un anno ha 1.120 euro (1.000 più il 2%, più i 100 versati). Dopo zero anni, ovviamente, ha ancora solo il capitale iniziale. E se il tasso fosse zero, il conto crescerebbe solo dei versamenti.

Non esiste una formula già vista nel corso: devi ripetere il passo anno per anno. Il risultato va arrotondato a due decimali.""",

'boomer': """Un'agenzia di marketing sta preparando una campagna pensata per i *baby boomer*, la generazione nata nel dopoguerra. Per segmentare l'elenco clienti servono regole precise, e la definizione che l'agenzia adotta è quella demografica standard: è boomer chi è nato **dal 1946 al 1964, estremi compresi**.

Ti passano una colonna con l'anno di nascita di ogni cliente e ti chiedono un programma che, dato l'anno, risponda "Boomer" oppure "Non Boomer" (scritti esattamente così, perché poi il testo finisce in un filtro automatico).

Il punto delicato è ai bordi: chi è nato nel 1946 o nel 1964 è dentro. Il capo dell'agenzia è pignolo e vuole che tu lo scriva in almeno due modi diversi, per controllare che diano lo stesso risultato proprio su quegli anni.""",

'autovelox': """Il Comune sta sostituendo il software di un autovelox e ti chiede di riscrivere la parte che calcola la multa. La legge è l'articolo 142 del Codice della Strada, che prevede importi crescenti in base a **di quanto** si supera il limite, e per questo lab si usano gli importi minimi.

Il testo di legge parla di eccessi "non oltre 10 km/h", "oltre 10 e non oltre 40", "oltre 40 e non oltre 60" e "oltre 60". Chi rispetta il limite non paga nulla. Le parole "non oltre" e "oltre" decidono da che parte cade chi va esattamente 10 km/h sopra il limite, e la differenza tra 36 e 148 euro per un automobilista la fa il tuo confronto.

Scrivi il programma che, data la velocità rilevata e il limite del tratto, calcola l'importo della sanzione.""",

'pricing-voli': """Una compagnia aerea low cost ti ha assunto come stagista nel team che decide i prezzi dei biglietti. Il prezzo non è mai fisso: parte da una **tariffa base** che dipende dalla classe (Economy 100 €, Premium 180 €, Business 350 €) e viene poi corretta da due fattori.

Il primo è l'**anticipo** con cui si prenota: chi compra con più di 60 giorni di anticipo ha uno sconto del 20%, tra 31 e 60 giorni il 10%, tra 15 e 30 giorni paga il prezzo pieno, tra 7 e 14 giorni paga il 20% in più, tra 3 e 6 giorni il 40% in più, e chi compra negli ultimi due giorni il 70% in più. Il secondo è il **riempimento** dell'aereo (`load_factor`, da 0 a 1): sotto il 50% dei posti venduti sconto del 10%, tra 50% e 70% nessuna correzione, oltre il 70% fino all'85% +15%, oltre l'85% +35%.

A tutto questo si aggiunge una **fee fissa** di 25 € alla fine, e c'è una regola di "stress di mercato": se mancano 2 giorni o meno **e** l'aereo è pieno oltre l'85%, si applica un ulteriore +10% prima della fee. I moltiplicatori si applicano in cascata: base × anticipo × riempimento × stress, poi + 25. Scrivi il programma che calcola il prezzo finale.""",

'autovelox-punti': """Dopo il calcolo della multa, il Comune ti chiede di completare il software dell'autovelox con la **decurtazione dei punti** dalla patente. Anche qui le fasce seguono l'articolo 142: chi resta entro il limite o lo supera di non oltre 10 km/h non perde punti; oltre 10 e non oltre 40 km/h perde 3 punti; oltre 40 e non oltre 60 ne perde 6; oltre 60 ne perde 10.

Il programma riceve, oltre a velocità e limite, i punti che l'automobilista ha attualmente sulla patente, e deve restituire quanti gliene restano. Un dettaglio che il vecchio software sbagliava: i punti **non possono andare sotto zero**. Un neopatentato con 2 punti che ne perde 6 resta a zero, non a meno quattro.""",

'bollo-auto': """Un concessionario vuole mostrare sul sito, accanto a ogni auto usata, quanto costa il bollo annuale, così i clienti non hanno sorprese. Ti chiede un calcolatore basato su una versione **semplificata** delle regole regionali: la tariffa dipende dalla potenza in kW e dalla classe ambientale Euro.

La logica è a scaglioni: i **primi 100 kW** si pagano a una tariffa bassa, e **solo i kW oltre i 100** a una tariffa più alta. Le due tariffe dipendono dalla classe: Euro 4, 5 e 6 pagano 2,58 € per kW fino a 100 e 3,87 € per ogni kW oltre; Euro 3 paga 2,70 e 4,05; Euro 2 paga 2,80 e 4,20; Euro 0 e 1 pagano 3,00 e 4,50.

Scrivi il programma che, dati kW e classe Euro (un numero da 0 a 6), calcola il bollo con due decimali. Fai attenzione a un'auto da esattamente 100 kW: non ha nessun kW "oltre".""",

'irpef': """Un commercialista vuole mostrare ai clienti, con un numero, cosa cambierebbe per loro con la **riforma delle aliquote IRPEF** in discussione. Ti chiede un programma che, dato il reddito imponibile annuo, calcoli l'imposta lorda con gli scaglioni del 2025 e con quelli proposti per il 2026, e restituisca la differenza (negativa se con il 2026 si paga meno).

L'IRPEF è **progressiva a scaglioni**: ogni aliquota si applica solo alla parte di reddito che cade in quella fascia, non all'intero reddito. Nel 2025 le fasce sono: fino a 15.000 € al 23%, da 15.001 a 28.000 al 23%, da 28.001 a 50.000 al 35%, oltre 50.000 al 43%. Nella proposta 2026: fino a 15.000 al 20%, da 15.001 a 28.000 al 23%, da 28.001 a 50.000 al 36%, da 50.001 a 75.000 al 40%, da 75.001 a 120.000 al 43%, oltre 120.000 al 46%.

Il commercialista userà il numero per decidere a chi mandare la newsletter, quindi la differenza deve essere esatta al centesimo, e deve tornare anche per chi guadagna esattamente 15.000, 28.000 o 50.000 euro.""",

'penali-fatture': """Nell'ufficio amministrativo di una piccola azienda ti chiedono di automatizzare il calcolo delle **penali per ritardato pagamento** che vanno aggiunte alle fatture dei clienti in ritardo. Le condizioni sono scritte nel contratto standard: entro 10 giorni di ritardo non si applica nulla; da 11 a 30 giorni si aggiunge il 5% dell'importo; da 31 a 60 giorni il 10%; da 61 a 90 giorni il 20%; oltre i 90 giorni si applica il 20% **più un 2% dell'importo per ogni giorno oltre il novantesimo**.

Il programma riceve l'importo della fattura e i giorni di ritardo e restituisce il totale da pagare (importo più penale), con due decimali. I clienti litigano sempre sui giorni di confine, il decimo, il trentesimo, il novantesimo: il tuo codice deve applicare esattamente ciò che dice il contratto.""",

'isee': """Il CAF del quartiere è sommerso di richieste per le agevolazioni scolastiche, e ti chiede uno strumento che dia alle famiglie una **stima dell'ISEE** prima dell'appuntamento. È una versione semplificata, ma segue la logica vera dell'indicatore.

Si parte dall'ISE, l'indicatore della situazione economica: il reddito annuo della famiglia più il **20% del patrimonio** (conti, case, risparmi). Poi l'ISE si divide per una **scala di equivalenza** che tiene conto di quante persone vivono dei quegli stessi soldi: un componente vale 1,00; due componenti 1,57; tre 2,04; quattro 2,46; cinque 2,85; e per ogni componente oltre il quinto si aggiungono 0,35 alla scala. Il risultato, l'ISEE, va arrotondato a due decimali.

Scrivi il programma che, dati reddito, patrimonio e numero di componenti, calcola l'ISEE. Le famiglie numerose sono quelle che più spesso hanno diritto alle agevolazioni: assicurati che la regola "oltre cinque" torni per sei, sette, otto persone.""",

'bmi': """Uno studio medico vuole aggiungere alla cartella digitale dei pazienti la **classificazione automatica del peso** secondo le fasce del Ministero della Salute. L'indice di massa corporea (BMI) si calcola come peso in kg diviso il quadrato dell'altezza in metri, e in base al valore il paziente rientra in una di sei categorie.

Le fasce sono: Sottopeso sotto 18,5; Normopeso da 18,5 a 25 escluso; Sovrappeso da 25 a 30 escluso; Obesità grado I da 30 a 35 escluso; Obesità grado II da 35 a 40 escluso; Obesità grado III da 40 in su. Il medico userà il testo nella cartella, quindi le sei etichette vanno scritte esattamente così: "Sottopeso", "Normopeso", "Sovrappeso", "Obesità grado I", "Obesità grado II", "Obesità grado III".

Scrivi il programma che, dati altezza e peso, restituisce la categoria. Un paziente con BMI esattamente 25 è sovrappeso, non normopeso: le soglie appartengono alla fascia superiore.""",

'taxi': """A Roma il tassametro non fa pagare solo i chilometri: quando il taxi è fermo nel traffico, scatta la **tariffa a tempo**. Un'associazione di consumatori ti chiede di ricostruire il costo di una corsa a partire da un tracciato GPS, per verificare gli scontrini dei tassisti.

Il tracciato è un vettore con i **km percorsi in ciascun minuto** della corsa. In ogni minuto il tassametro guarda la velocità di quel minuto (i km del minuto moltiplicati per 60 danno i km/h): se è **sotto i 20 km/h** applica la tariffa oraria, 28 € all'ora, cioè 28/60 € per quel minuto; se è di 20 km/h o più applica la tariffa chilometrica, 1,14 € per ogni km percorso in quel minuto. Il costo della corsa è la somma dei minuti, arrotondata a due decimali.

Scrivi il programma che, dato il vettore delle distanze, calcola il costo. Un taxi fermo per quattro minuti a un semaforo ha velocità zero, ma il tassametro corre lo stesso.""",

'autovelox-funzione': """Il software dell'autovelox scritto nel modulo 2 funziona, ma il Comune ne ha comprati altri dodici, su strade con limiti diversi, e vuole usare **lo stesso codice** per tutti senza copiarlo e incollarlo ogni volta. È il momento di trasformarlo in una **funzione**.

Le regole restano quelle dell'articolo 142: nessuna sanzione entro il limite; 36 € per un eccesso non oltre 10 km/h; 148 € oltre 10 e non oltre 40; 370 € oltre 40 e non oltre 60; 500 € oltre 60. Il tuo codice deve **definire** la funzione `multa(velocita, limite)` che restituisce l'importo. La verifica non assegna variabili: chiama direttamente la tua funzione con i valori di ogni caso.

In RStudio, poi, usala su un vettore di veicoli con un ciclo e conta quante multe superano i 100 euro: è esattamente ciò che vuole il Comune.""",

'taxi-uber': """Dopo la corsa calcolata nel lab del taxi, l'associazione dei consumatori vuole rispondere alla domanda che tutti si fanno alle due di notte fuori da un locale: **conviene il taxi o Uber?** Uber comunica il prezzo in anticipo; il taxi va ricostruito.

Al costo variabile del tassametro (28 €/h sotto i 20 km/h, 1,14 €/km altrimenti, minuto per minuto) va aggiunta la **quota fissa** di partenza, che a Roma dipende da giorno e ora: nei giorni feriali dalle 6 alle 21 sono 3 €; la domenica nella stessa fascia 5 €; di **notte**, cioè dalle 22 in poi o prima delle 6, qualunque giorno sia, 7 €. Il giorno è indicato con una lettera ("D" per domenica), l'ora con un numero intero da 0 a 23.

Il programma riceve il tracciato, il giorno, l'ora e il prezzo di Uber, e risponde "Taxi" oppure "Uber". Si sceglie Uber solo se costa **strettamente meno** del taxi: a parità si prende il taxi, che almeno è già lì.""",

'portafoglio': """Un'app di trading mostra ai clienti il grafico del loro portafoglio, ma un cliente sostiene che il valore finale sia sbagliato. Ti chiedono di ricalcolarlo in modo indipendente a partire dai **rendimenti giornalieri**: un vettore in cui 0,01 significa +1% quel giorno e −0,02 significa −2%.

Si parte da 100 euro. Ogni giorno il valore viene moltiplicato per uno più il rendimento del giorno. C'è un caso estremo da gestire: un rendimento di −1, cioè −100%, azzera il capitale, e da lì in poi resta zero anche se i giorni successivi vanno bene, perché non c'è più nulla da far crescere.

Scrivi il programma che, dato il vettore dei rendimenti, calcola il valore finale con due decimali. Fallo con un ciclo, giorno per giorno; se conosci `prod()`, usalo solo per controllare.""",

'rata-mutuo': """Una banca online vuole un simulatore di mutuo sul sito: il cliente inserisce capitale, tasso annuo e durata, e vede la **rata mensile**. Il mutuo è a rata costante, l'ammortamento "alla francese" usato da quasi tutte le banche italiane.

La formula è nota: si calcola il tasso mensile `i = tasso/100/12` e il numero di rate `n = anni * 12`, e la rata è `capitale * i / (1 - (1 + i)^(-n))`. Il simulatore però deve gestire anche le promozioni a **tasso zero**: in quel caso la formula divide per zero, e la rata è semplicemente il capitale diviso il numero di rate.

Il codice va scritto come funzione `rata(capitale, tasso, anni)` che restituisce la rata mensile arrotondata a due decimali, perché la banca la chiamerà da mille punti diversi del sito.""",

'sconto-fedelta': """Una catena di negozi di abbigliamento lancia il nuovo programma fedeltà e ti chiede di scrivere il calcolo dello **sconto alla cassa**. La direzione marketing ti ha spiegato le regole a voce, in riunione, e questa è la tua trascrizione.

Lo sconto base dipende da quanto si spende: niente sconto sotto i 100 euro, il 5% da 100 euro in su, il 10% da 250 euro in su. Chi ha la tessera fedeltà ha un **bonus** che si somma in punti percentuali: la tessera silver aggiunge 2 punti, la gold 7, chi non ha tessera non aggiunge nulla. Lo sconto complessivo, base più bonus, **non può in nessun caso superare il 15%**: un cliente gold da 300 euro avrebbe 10 + 7 = 17, ma paga con il 15%.

Il programma riceve la spesa e la tessera ("silver", "gold" o "nessuna") e restituisce il prezzo finale con due decimali. Prima di scrivere codice, scrivi tu la specifica completa, con i casi limite (100 euro esatti, 250 esatti, il tetto del 15%), e passala all'assistente in modalità *aiutami a partire*.""",

'ecommerce-giovani': """Il responsabile marketing di un negozio online vuole capire quanto pesano i **clienti giovani** sugli ordini, per decidere se investire in una campagna sui social. Ti passa l'estratto degli ordini dell'anno (`ecommerce.csv`, una riga per ordine, con le colonne CustomerID, OrderID, OrderDate, Age, Gender, Membership, ProductCategory, ProductName, UnitPrice, Quantity, TotalAmount, PaymentMethod, City, ReturnStatus) e ti chiede una prima cifra: quanti ordini sono stati fatti da clienti con meno di 35 anni.

Il data frame `data` è già caricato quando premi Verifica (in RStudio lo carichi tu con `read.csv`). C'è una trappola: la colonna `Age` ha dei **valori mancanti**, perché non tutti i clienti hanno indicato l'età. Devi decidere cosa farne e scriverlo nel codice, non lasciarlo al caso. Il risultato deve essere un numero, non una tabella.""",

'titanic-over50': """Il dataset dei passeggeri del Titanic è il classico su cui tutti imparano a leggere una tabella, e per questo lo usiamo. Il data frame `titanic` è già caricato: una riga per passeggero, con le colonne PassengerId, Survived, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked.

La prima domanda è semplice: **quante persone con più di 50 anni** erano a bordo? Il conteggio riguarda chi ha l'età nota; 177 passeggeri non ce l'hanno, e vanno lasciati fuori consapevolmente. Il risultato deve essere un numero estratto dalla tabella che ottieni con dplyr.

Poi, in RStudio, continua con le altre domande del modulo: la percentuale di uomini e donne tra gli over 50, chiedendoti sempre "percentuale rispetto a chi?".""",

'titanic-prima-classe': """La frase "sul Titanic si salvavano i ricchi" è ripetuta ovunque: vediamo se i dati la confermano. Il data frame `titanic` è già caricato e la colonna `Survived` vale 1 per chi è sopravvissuto e 0 per chi no. Questo significa che la **media** di `Survived` è già la percentuale di sopravvissuti.

Raggruppa i passeggeri per classe (`Pclass`), calcola la media di `Survived` per ogni classe, ed estrai il valore della prima classe, arrotondato a tre decimali, come numero tra 0 e 1. Poi confronta con la terza classe: la differenza tra i due numeri è la risposta alla domanda. Attenzione al denominatore: la percentuale è calcolata dentro la classe, non sul totale dei sopravvissuti.""",

'titanic-biglietti': """Un ricercatore che studia le famiglie a bordo del Titanic ha notato che un biglietto poteva coprire più persone: coniugi, figli, domestici. Ti chiede una cifra per iniziare: **quanti biglietti erano associati a più di un passeggero**.

Il data frame `titanic` è già caricato; il codice del biglietto è nella colonna `Ticket`, uguale per tutti i passeggeri che viaggiavano con quel biglietto. Il risultato che il ricercatore vuole è il numero di **biglietti** condivisi, non il numero di passeggeri che viaggiavano su biglietti condivisi: sono due numeri diversi, e servono due passaggi di conteggio, uno per raggruppare i passeggeri per biglietto e uno per contare i gruppi che superano una persona.""",

'finanza-volatilita': """Una società di gestione del risparmio ti chiede di calcolare il **rischio** di quattro titoli italiani nel 2023 a partire dai rendimenti giornalieri. Il data frame `returns` è già caricato, con una colonna per titolo (Ferrari, Enel, Intesa, Unicredit) e la colonna `day`: ogni valore è il rendimento percentuale di quel giorno.

In finanza il rischio di un titolo si misura con la **variabilità** dei suoi rendimenti, cioè la deviazione standard: un titolo che oscilla molto è rischioso anche se in media guadagna. Calcola la volatilità di Unicredit con `sd()` e arrotondala a quattro decimali. Non ci sono valori mancanti.

In RStudio confronta poi le quattro azioni: quale ha il rendimento medio più alto? quale il rischio più alto? coincidono?""",

'finanza-correlazione': """La stessa società di gestione vuole costruire un portafoglio **diversificato**, e la diversificazione funziona solo se i titoli non si muovono tutti insieme. Ti chiede di misurare quanto i rendimenti di due banche, Intesa e Unicredit, salgono e scendono negli stessi giorni.

Il data frame `returns` è già caricato. Lo strumento è il coefficiente di correlazione, `cor(x, y)`, che va da −1 (si muovono in direzioni opposte) a +1 (si muovono identici); intorno a 0 sono indipendenti. Calcola la correlazione tra le due banche e arrotondala a tre decimali.

Poi in RStudio fai il grafico a dispersione con ggplot2 e confronta con la coppia Ferrari–Enel: due banche si assomigliano più di un'auto sportiva e un'utility?""",
}


CONTESTI.update({
'spedizione-gratis': """Il sito di un negozio di articoli sportivi mostra, accanto al carrello, la scritta «spedizione gratuita da 49,90 €». Il reparto marketing vuole aggiungere un messaggio che dica al cliente, mentre riempie il carrello, se ha già diritto alla spedizione gratis o no: è una delle leve più efficaci per far aggiungere un ultimo articolo.

Ti chiedono la regola nella forma più semplice possibile: dato il totale del carrello, un valore vero/falso che il sito userà per mostrare o nascondere il messaggio. Il confine conta: a 49,90 esatti la spedizione è gratuita, a 49,89 no. Non serve nessuna decisione «se…allora»: basta un confronto, e il risultato è direttamente `TRUE` o `FALSE`.""",

'costo-dipendente': """La titolare di un piccolo studio di consulenza vuole assumere una persona e sta facendo i conti. L'annuncio dice 1.800 euro lordi al mese, ma lei sa che il costo per l'azienda è molto più alto: in Italia le mensilità sono tredici (c'è la tredicesima) e sul lordo annuo l'azienda versa contributi che, per semplificare, contiamo al 30%.

Ti chiede un programma che, dato il lordo mensile, calcoli il costo annuo che sosterrà l'azienda, con due decimali, così da poterlo confrontare con il budget. Lo userà per più candidati, anche con cifre con i centesimi: l'arrotondamento va fatto una volta sola, alla fine.""",

'punto-pareggio': """Due amici vogliono aprire una pizzeria da asporto e devono rispondere alla domanda che ogni banca farà loro: quante pizze dovete vendere al mese per non perderci? I costi fissi mensili (affitto, bollette, stipendi) sono noti. Ogni pizza si vende a un prezzo e costa, in ingredienti e scatola, una cifra fissa: la differenza tra i due è quello che ogni pizza venduta lascia per coprire i costi fissi.

Il numero cercato è quante pizze servono perché la somma di quei contributi copra i costi fissi. Non esistono le mezze pizze, e con una pizza in meno non si è ancora in pareggio: quindi la divisione va sempre arrotondata **per eccesso**, anche quando manca pochissimo. Quando invece la divisione è esatta, non si aggiunge nulla.

Scrivi il programma che, dati costi fissi, prezzo e costo unitario, calcola il numero di pizze del pareggio. In R esiste la funzione `ceiling()`.""",

'occupazione-hotel': """La direttrice di un hotel di 45 camere guarda ogni mattina un numero solo: il tasso di occupazione della notte appena passata, cioè la percentuale di camere occupate sul totale. È il numero con cui ragiona la catena, con cui si decidono i prezzi del giorno e con cui si confrontano gli hotel tra loro.

Il gestionale glielo mostra, ma vuole ricalcolarlo lei quando arrivano i dati dagli altri hotel del gruppo, che hanno numeri di camere diversi. Scrivi il programma che, date le camere occupate e le camere totali, calcola il tasso in percentuale con un decimale. Una notte con l'hotel pieno deve dare 100, una notte vuota 0.""",

'rimborso-treno': """Lavori all'assistenza clienti di una compagnia ferroviaria e ogni giorno arrivano richieste di rimborso per ritardo. Le condizioni di trasporto sono chiare: se il treno arriva con un ritardo **sotto i 60 minuti** non è dovuto nulla; **da 60 a 119 minuti** il passeggero ha diritto al 25% del prezzo del biglietto; **da 120 minuti in su** al 50%.

Ti chiedono di automatizzare il calcolo: dati il prezzo del biglietto e i minuti di ritardo, l'importo da rimborsare con due decimali. I passeggeri più agguerriti sono quelli con 59 o 60 minuti di ritardo, e con 119 o 120: sono esattamente i casi su cui il tuo programma deve fare la cosa scritta nelle condizioni.""",

'biglietto-museo': """Il museo civico della città ha una tariffa che gli addetti alla biglietteria sanno a memoria ma che il nuovo sito deve calcolare da solo. La **prima domenica del mese** l'ingresso è gratuito per tutti, chiunque sia il visitatore. Negli altri giorni, i bambini **sotto i 6 anni** e le persone **dai 70 anni in su** entrano gratis; **fino ai 18 anni compresi**, oppure con la tessera studente a qualunque età, il biglietto è ridotto a 8 euro; tutti gli altri pagano l'intero, 15 euro.

Scrivi il programma che, dati età, tessera studente (vero/falso) e prima domenica (vero/falso), restituisce il prezzo. L'ordine dei controlli conta: un settantacinquenne con tessera studente entra gratis, non a 8 euro, perché il gratuito viene prima del ridotto.""",

'parcheggio': """Il parcheggio del centro commerciale ha una cassa automatica e la società che lo gestisce ti chiede di riscrivere la regola che calcola l'importo all'uscita, perché quella vecchia sbagliava proprio sui casi che generano reclami.

La sosta è gratuita **fino a 30 minuti**. Oltre i 30 minuti si paga 1,50 euro **per ogni ora o frazione di ora**, contando dal momento dell'ingresso: chi resta 31 minuti paga una frazione della prima ora, cioè 1,50 euro; chi resta 61 minuti è già nella seconda ora e paga 3 euro; chi resta esattamente 60 minuti paga un'ora sola. C'è un **massimo giornaliero** di 12 euro, oltre il quale il contatore si ferma.

Scrivi il programma che, dati i minuti di sosta, calcola l'importo. In R l'arrotondamento per eccesso è `ceiling()`.""",

'sotto-scorta': """Il responsabile del magazzino di un negozio di ferramenta ha due elenchi, uno accanto all'altro: per ogni prodotto la **giacenza** (i pezzi sullo scaffale) e la **scorta minima** sotto la quale bisogna riordinare. Ogni lunedì li confronta a mano e conta quanti prodotti vanno riordinati, per sapere quante righe avrà l'ordine al fornitore.

I due elenchi sono due vettori della stessa lunghezza, nello stesso ordine: il prodotto in posizione 3 ha giacenza `giacenza[3]` e soglia `soglia[3]`. Un prodotto va riordinato se la giacenza è **strettamente sotto** la soglia: chi è esattamente alla soglia è ancora a posto.

Scrivi il programma che conta i prodotti da riordinare scorrendo i vettori con un ciclo. In RStudio, dopo, prova a ottenere lo stesso numero senza ciclo, con `sum(giacenza < soglia)`: è una riga sola, ma solo dopo aver capito il ciclo.""",

'straordinari': """Nell'ufficio del personale di un supermercato, ogni fine settimana bisogna calcolare la paga degli addetti a partire dal cartellino: un vettore con le ore lavorate in ciascun giorno. Il contratto dice che in ogni giornata le prime **8 ore** sono ordinarie e si pagano alla paga oraria; le ore **oltre l'ottava** sono straordinario e valgono il 130% della paga oraria.

Il punto che il vecchio foglio Excel sbagliava: il conteggio è **giorno per giorno**. Chi fa 9 ore il lunedì e 7 il martedì ha un'ora di straordinario, non zero, perché le ore non si compensano tra giornate.

Scrivi il programma che, dati il vettore delle ore e la paga oraria, calcola la paga della settimana con due decimali.""",

'nps': """Un'azienda di telefonia manda ai clienti la domanda standard della soddisfazione: «quanto consiglieresti il nostro servizio a un amico, da 0 a 10?». Il numero che il management vuole vedere ogni mese è il **Net Promoter Score**: si contano i *promotori* (chi ha risposto 9 o 10) e i *detrattori* (da 0 a 6), si fa la differenza e la si divide per il numero totale di intervistati, in percentuale. Chi ha risposto 7 o 8 è *passivo*: non conta né in un verso né nell'altro, ma resta nel denominatore.

Ti passano il vettore dei voti e ti chiedono l'NPS con un decimale. Va da −100 (tutti detrattori) a 100 (tutti promotori). Un mese con soli 7 e 8 dà zero: non è un errore, è la definizione.

Contali con un ciclo e due contatori; poi, in RStudio, confronta con `sum(voti >= 9)`.""",

'provvigioni': """Un'azienda che vende macchine per il caffè ai bar paga i propri agenti a provvigione, con un contratto a **scaglioni progressivi calcolati mese per mese**: sul venduto di ogni mese, il 3% sulla parte fino a 10.000 euro, il 5% sulla parte tra 10.000 e 20.000, l'8% sulla parte oltre i 20.000. È lo stesso meccanismo dell'IRPEF: ogni aliquota si applica solo alla fetta che cade nella sua fascia, non a tutto il venduto.

Un agente con 25.000 euro di venduto in un mese prende quindi 300 sul primo scaglione, 500 sul secondo e 400 sul terzo; uno con 10.000 esatti prende 300 e basta. L'ufficio amministrazione ti passa il vettore del venduto dei dodici mesi di un agente e vuole le provvigioni dell'anno, con due decimali.

Prima di scrivere codice, scrivi tu la specifica con i casi al confine (10.000 esatti, 20.000 esatti, un mese a zero), poi ragiona su come applicare la regola a un mese, e infine ripetila con un ciclo.""",

'fatturato-categoria': """Il direttore commerciale di un negozio online vuole sapere, prima della riunione di budget, quale categoria di prodotto ha generato più fatturato nell'anno. Il data frame `data` è già caricato: una riga per ordine, con la categoria in `ProductCategory` e l'importo in `TotalAmount`.

La domanda vuole un nome, non una tabella: dopo aver sommato il fatturato per categoria e ordinato dal più grande al più piccolo, il risultato è il testo della prima riga. In RStudio guarda anche il secondo e il terzo posto: quanto distacco c'è?""",

'tasso-reso': """Il responsabile logistica di un negozio online sospetta che gli ordini pagati con PayPal vengano resi più spesso, perché il reso è più semplice da avviare. Prima di cambiare le condizioni vuole un numero.

Il data frame `data` è già caricato; la colonna `ReturnStatus` vale 1 se l'ordine è stato reso e 0 altrimenti, quindi la sua media è già la quota di resi. Calcola la quota di resi tra gli ordini pagati con PayPal (`PaymentMethod == "PayPal"`), arrotondata a tre decimali. Poi, in RStudio, confronta i quattro metodi di pagamento: il sospetto regge?""",

'terza-citta': """Il negozio online vuole aprire un punto di ritiro in una terza città, dopo le due dove già c'è. La scelta più semplice è la terza città per numero di ordini. Il data frame `data` è già caricato, con la città di consegna in `City`.

Conta gli ordini per città, ordina dalla più grande alla più piccola e prendi il nome della terza. Attenzione al verso dell'ordinamento: se ordini in senso crescente, la terza riga è una città piccola.""",

'categoria-resi': """Il responsabile qualità del negozio online vuole capire su quale categoria di prodotto concentrare i controlli: quella che viene resa più spesso. Non la categoria con più resi in assoluto, che sarebbe semplicemente quella con più ordini, ma quella con la quota di resi più alta rispetto ai suoi ordini.

Il data frame `data` è già caricato; `ReturnStatus` vale 1 per gli ordini resi. Il risultato è il nome della categoria.""",

'rfm-gold': """Il responsabile marketing di una catena di negozi vuole scrivere ai clienti migliori, quelli che il reparto chiama **Gold**: hanno comprato di recente, comprano spesso e spendono molto. Il metodo è l'RFM della lezione: per ogni cliente si calcolano *recency* (giorni dall'ultimo acquisto rispetto all'ultima data del file), *frequency* (numero di righe di scontrino) e *monetary* (totale speso); ogni metrica si trasforma in un punteggio da 1 a 4 con `ntile`, ricordando che per la recency il migliore è chi ha **pochi** giorni; e i segmenti si assegnano con il `case_when` della lezione, nell'ordine: Gold se 4-4-4, Persi se 1-1-1, Fedeli se frequency 4, Attivi se recency 4, Alta spesa se monetary 4, Altri per tutti gli altri.

Il data frame `scontrini` è già caricato (in RStudio: `read.csv("retail_rfm.csv")`); la data va convertita con `as.Date`. La domanda è una sola: quanti clienti sono Gold. Il numero deve uscire dalla tabella, con un `filter` o un `group_by`, non contato a occhio.""",

'corriere-affidabile': """Il negozio online lavora con quattro corrieri e riceve lamentele sui tempi di consegna. Il responsabile logistica non cerca il corriere più veloce: cerca quello **più regolare**, perché un cliente accetta 4 giorni se glieli hai promessi, non accetta che a volte siano 2 e a volte 8. La regolarità si misura con la deviazione standard dei giorni di consegna, come nella lezione la variabilità di un titolo.

Il data frame `data` è già caricato, con il corriere in `Courier` e i giorni in `DeliveryDays`. Per ogni corriere calcola media e deviazione standard, ordina per deviazione crescente e prendi il primo nome. In RStudio guarda anche la media: il più regolare è anche il più veloce?""",

'sconto-quantita': """Il responsabile vendite del negozio online sostiene che gli sconti fanno comprare più pezzi. Il responsabile finanza sostiene che gli sconti fanno solo spendere di meno. Prima di litigare, un numero: quanto lo sconto applicato all'ordine e i pezzi acquistati crescono insieme.

Il data frame `data` è già caricato, con lo sconto in percentuale in `Discount` e i pezzi in `Quantity`. Lo strumento è il coefficiente di correlazione, `cor(x, y)`, da −1 a +1. Arrotonda a tre decimali. Poi, in RStudio, calcola anche la correlazione tra sconto e importo dell'ordine: è più bassa, e vale la pena chiedersi perché.""",

'ticket-medio': """Il negozio online sta scegliendo in quale città fare una campagna con un buono sconto sopra una certa spesa. Serve la città dove i clienti spendono di più **per ordine**: lo scontrino medio (ticket medio), non il fatturato totale, che premia semplicemente le città con più ordini.

Il data frame `data` è già caricato. Raggruppa per città, calcola la media di `TotalAmount` e il numero di ordini, ordina per media decrescente e prendi il nome della prima. In RStudio guarda quanto sono vicine le prime tre: la differenza è abbastanza grande per decidere?""",

'assenze-reparto': """La direttrice del personale di un'azienda di servizi vuole capire in quale reparto il tema delle assenze pesa di più, per parlarne con il responsabile. Il primo conto che le hanno portato, i giorni di assenza totali per reparto, non la convince: le Vendite risultano prime, ma sono anche il reparto con più persone. Il confronto sensato è **per addetto**: i giorni di assenza di un reparto divisi per il numero di dipendenti di quel reparto.

Il data frame `personale` è già caricato (in RStudio: `read.csv("personale.csv")`): una riga per dipendente, con `reparto` e `giorni_assenza`. Il risultato che vuole è il nome del reparto con più giorni di assenza per addetto.""",
})

# ─────────────────────────── scrittura file ───────────────────────────
import subprocess, json, tempfile
DATI = os.path.join(os.path.dirname(__file__), '..', 'dati')

def r_run(code, outvar, workdir=DATI):
    """esegue codice R (Rscript) e restituisce il valore dell'output come stringa, o solleva"""
    script = code + f'\ncat(paste(as.character({outvar}), collapse = ", "))\n'
    with tempfile.NamedTemporaryFile('w', suffix='.R', delete=False, encoding='utf-8') as f: f.write(script); path = f.name
    r = subprocess.run(['Rscript', '--vanilla', path], cwd=workdir, capture_output=True, text=True, env={**os.environ, 'LANG': 'en_US.UTF-8', 'LC_ALL': 'en_US.UTF-8'})
    os.unlink(path)
    if r.returncode != 0: raise RuntimeError(r.stderr.strip().splitlines()[-1] if r.stderr.strip() else 'errore R')
    return r.stdout.strip().splitlines()[-1] if r.stdout.strip() else ''

def parse_val(v, exp_type):
    if exp_type == 'numero': return float(v) if '.' in v or 'e' in v else int(v)
    if exp_type == 'logico': return v.upper() == 'TRUE'
    return v

def build_tests(L):
    tests = []
    if L.get('r_expected'):
        prologue = f"{L['data_var']} <- read.csv(\"{os.path.basename(L['data_url'])}\")\n"
        val = r_run(prologue + L['solution'], L['risultato']['name'])
        exp = parse_val(val, L['risultato']['type'])
        for c in L['fixed']:
            t = dict(inputs={}, expected=exp, visible=bool(c.get('visible', False)))
            if c.get('hint'): t['hint'] = c['hint']
            tests.append(t)
        return tests
    if 'fixed' in L:
        for c in L['fixed']:
            t = dict(inputs={}, expected=c['expected'], visible=bool(c.get('visible', False)))
            if c.get('hint'): t['hint'] = c['hint']
            tests.append(t)
        return tests
    names = [i['name'] for i in L['inputs']]
    for c in L['cases']:
        inp = {k: c[k] for k in names}
        exp = L['fn'](**inp)
        t = dict(inputs=inp, expected=exp, visible=bool(c.get('visible', False)))
        if c.get('boundary'): t['boundary'] = True
        if c.get('hint'): t['hint'] = c['hint']
        tests.append(t)
    return tests

def valida(L, tests):
    """la soluzione R deve dare gli stessi valori del riferimento Python, caso per caso (come fa il runner)"""
    if L.get('r_expected') or 'fixed' in L: return []
    names = [i['name'] for i in L['inputs']]
    errs = []
    code_lines = [l for l in L['solution'].split('\n')]
    for t in tests:
        assign = '\n'.join(f"{k} <- {to_r(v)}" for k, v in t['inputs'].items())
        # come nel runner: le righe che assegnano un input vengono neutralizzate
        import re as _re
        body = '\n'.join(('# ' + l) if any(_re.match(r'^\s*' + _re.escape(n) + r'\s*(<-|=)', l) for n in names) else l for l in code_lines)
        if L.get('function'):
            args = ', '.join(to_r(t['inputs'][n]) for n in names)
            code = f"{body}\n.__out <- {L['function']}({args})"
        else:
            code = f"{assign}\n{body}\n.__out <- {L['risultato']['name']}"
        try: got = r_run(code, '.__out', workdir=os.getcwd())
        except Exception as e: errs.append(f"{t['inputs']}: errore R {e}"); continue
        exp = t['expected']
        ok = (abs(float(got) - exp) <= float(L.get('tolerance', 0.01))) if isinstance(exp, (int, float)) and not isinstance(exp, bool) else (str(got).upper() == str(exp).upper())
        if not ok: errs.append(f"{t['inputs']}: R={got} atteso={exp}")
    return errs

def to_r(v):
    if isinstance(v, bool): return 'TRUE' if v else 'FALSE'
    if isinstance(v, (list, tuple)): return 'c(' + ', '.join(to_r(x) for x in v) + ')'
    if isinstance(v, (int, float)): return repr(v)
    return '"' + str(v) + '"'

def scaffold(solution, names):
    """la forma della soluzione (if/else, cicli, funzione) con i corpi sostituiti da '# ...' (solo lab facili)"""
    import re as _re
    out, prev_dots = [], False
    for line in solution.rstrip().split('\n'):
        st = line.strip()
        if not st: continue
        if any(_re.match(r'^' + _re.escape(n) + r'\s*<-', st) for n in names): continue        # input: già in testa
        if st.startswith('library('): continue
        if _re.match(r'^(if\s*\(|\}\s*else|for\s*\(|while\s*\(|\}|\w+\s*<-\s*function)', st):
            out.append(line.rstrip()); prev_dots = False
        else:
            if prev_dots: continue
            indent = line[:len(line) - len(line.lstrip())]
            out.append(indent + '# ...'); prev_dots = True
    # l'ultima riga della soluzione è di solito l'output nudo: via, ci pensa print()
    if out and out[-1].strip() == '# ...': out.pop()
    return out

def build_skeleton(L, difficolta):
    """input assegnati in testa, print dell'output in coda; i lab facili hanno in mezzo la struttura"""
    out = L['risultato']['name']
    names = [i['name'] for i in L['inputs']]
    first = next((c for c in L.get('cases', []) if c.get('visible')), None)
    lines = []
    if L.get('data_url'):
        if L.get('packages'): lines.append('library(dplyr)')
        lines.append(f"# {L['data_var']} è già caricato (in RStudio: {L['data_var']} <- read.csv(\"{os.path.basename(L['data_url'])}\"))")
    elif L.get('function'):
        args = ', '.join(names)
        call = ', '.join(to_r(first[n]) for n in names) if first else args
        if difficolta == 'facile':
            body = scaffold(L['solution'], names)
            # scaffold contiene già la riga "fn <- function(...){" e la graffa finale; togliamo la chiamata finale se presente
            body = [b for b in body if not b.strip().startswith('print(')]
            return '\n'.join(body + ['', f'print({L["function"]}({call}))']) + '\n'
        return '\n'.join([f"{L['function']} <- function({args}){{", '  ', '}', '', f'print({L["function"]}({call}))']) + '\n'
    else:
        for n in names:
            lines.append(f"{n} <- {to_r(first[n])}" if first else f"{n} <- ")
    lines.append('')
    if difficolta == 'facile':
        lines += scaffold(L['solution'], names)
        lines.append('')
    lines.append(f'print({out})')
    return '\n'.join(lines) + '\n'

class Lit(str): pass
def lit_repr(dumper, data): return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
yaml.add_representer(Lit, lit_repr)

for L in LABS:
    difficolta = 'difficile' if L['level'] == 'sfida' else 'facile'
    fm = dict(layout='lab', title=L['title'], modulo=L['modulo'], order=L['order'], difficolta=difficolta, language=L['language'], ai_mode=L['ai_mode'],
              objective=L['objective'], inputs=L['inputs'], risultato=L['risultato'])
    if L.get('function'): fm['function'] = L['function']
    for k in ('data_url', 'data_var', 'packages', 'tolerance'):
        if k in L: fm[k] = L[k]
    fm['regole'] = Lit(L['rules'].strip() + '\n')
    fm['skeleton'] = Lit(build_skeleton(L, difficolta))
    fm['tests'] = build_tests(L)
    problemi = valida(L, fm['tests'])
    for e in problemi: print('  !! ', L['slug'], e)
    fm['solution'] = Lit(L['solution'])
    fm['solution_after'] = ''
    y = yaml.dump(fm, allow_unicode=True, sort_keys=False, width=1000)
    if L['slug'] not in CONTESTI: raise SystemExit('manca il contesto di ' + L['slug'])
    with open(os.path.join(OUT, L['slug'] + '.md'), 'w') as f:
        f.write('---\n' + y + '---\n\n' + CONTESTI[L['slug']].strip() + '\n')
print('lab generati:', len(LABS))
for L in LABS: print(' ', L['modulo'], ('difficile' if L['level']=='sfida' else 'facile').ljust(9), L['slug'])
