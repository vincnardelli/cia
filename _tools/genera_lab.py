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
lab('scontrino', title='Scontrino', week=1, order=1, level='base', language='R', ai_mode='off',
    objective="Calcolare il totale di uno scontrino a partire dal prezzo netto e dalla quantità, con IVA al 22%.",
    inputs=[dict(name='prezzo_netto', type='numero', desc='prezzo unitario senza IVA, in euro'),
            dict(name='quantita', type='numero', desc='pezzi acquistati')],
    output=dict(name='totale', type='numero', desc='totale da pagare, arrotondato a 2 decimali'),
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
lab('cambio-valuta', title='Cambio valuta', week=1, order=2, level='extra', language='R', ai_mode='off',
    objective="Convertire un importo in euro in dollari applicando la commissione dello sportello.",
    inputs=[dict(name='importo_euro', type='numero', desc='euro da cambiare'), dict(name='tasso', type='numero', desc='dollari per un euro, es. 1.08')],
    output=dict(name='dollari', type='numero', desc='dollari ricevuti, arrotondati a 2 decimali'),
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
lab('interesse-composto', title='Interesse composto', week=1, order=3, level='extra', language='R', ai_mode='on',
    objective="Calcolare il montante di un capitale investito a interesse composto per un certo numero di anni.",
    inputs=[dict(name='capitale', type='numero', desc='euro investiti'), dict(name='tasso', type='numero', desc='tasso annuo in percentuale, es. 3 per il 3%'), dict(name='anni', type='numero', desc='anni di investimento (intero)')],
    output=dict(name='montante', type='numero', desc='capitale finale, arrotondato a 2 decimali'),
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
lab('piano-risparmio', title='Piano di risparmio', week=1, order=4, level='sfida', language='R', ai_mode='on',
    objective="Calcolare quanto si accumula versando ogni anno una somma fissa su un conto a interesse composto.",
    inputs=[dict(name='capitale', type='numero', desc='somma iniziale'), dict(name='versamento', type='numero', desc='versato alla fine di ogni anno'), dict(name='tasso', type='numero', desc='tasso annuo in percentuale'), dict(name='anni', type='numero', desc='anni (intero)')],
    output=dict(name='montante', type='numero', desc='somma finale, 2 decimali'),
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
lab('boomer', title='Boomer finder', week=2, order=1, level='base', language='R', ai_mode='off',
    objective="Stabilire se una persona è un baby boomer a partire dall'anno di nascita.",
    inputs=[dict(name='anno', type='numero', desc='anno di nascita')],
    output=dict(name='status', type='testo', desc='"Boomer" oppure "Non Boomer"'),
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
lab('autovelox', title='Autovelox', week=2, order=2, level='base', language='R', ai_mode='off',
    objective="Calcolare la sanzione per eccesso di velocità secondo l'art. 142 del Codice della Strada.",
    inputs=[dict(name='velocita', type='numero', desc='velocità rilevata, km/h'), dict(name='limite', type='numero', desc='limite di velocità, km/h')],
    output=dict(name='multa', type='numero', desc='sanzione in euro'),
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
lab('pricing-voli', title='Pricing dei voli', week=2, order=3, level='base', language='R', ai_mode='off',
    objective="Calcolare il prezzo di un biglietto aereo in base a classe, giorni di anticipo e riempimento dell'aereo.",
    inputs=[dict(name='seat_type', type='testo', desc='"Economy", "Premium" o "Business"'), dict(name='days_before', type='numero', desc='giorni di anticipo (intero)'), dict(name='load_factor', type='numero', desc='riempimento tra 0 e 1')],
    output=dict(name='prezzo_finale', type='numero', desc='prezzo in euro, 2 decimali'),
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
lab('autovelox-punti', title='Autovelox con punti patente', week=2, order=4, level='extra', language='R', ai_mode='off',
    objective="Estendere l'autovelox: oltre alla sanzione, calcolare i punti patente rimasti dopo la decurtazione.",
    inputs=[dict(name='velocita', type='numero'), dict(name='limite', type='numero'), dict(name='punti_iniziali', type='numero', desc='punti sulla patente prima della multa')],
    output=dict(name='punti_finali', type='numero', desc='punti rimasti (mai sotto zero)'),
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
lab('bollo-auto', title='Bollo auto', week=2, order=5, level='extra', language='R', ai_mode='on',
    objective="Calcolare il bollo auto (regole semplificate) in base alla potenza e alla classe ambientale.",
    inputs=[dict(name='kw', type='numero', desc='potenza in kW'), dict(name='classe_euro', type='numero', desc='classe Euro da 0 a 6')],
    output=dict(name='bollo', type='numero', desc='importo in euro, 2 decimali'),
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
lab('irpef', title='IRPEF 2025 vs 2026', week=2, order=6, level='extra', language='R', ai_mode='on',
    objective="Calcolare l'IRPEF lorda con gli scaglioni 2025 e con la proposta 2026, e la differenza tra le due.",
    inputs=[dict(name='reddito', type='numero', desc='reddito complessivo annuo, euro')],
    output=dict(name='differenza', type='numero', desc='IRPEF 2026 − IRPEF 2025, in euro, 2 decimali'),
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
    solution=open(os.path.join(os.path.dirname(__file__), '..', 'materiale_lezioni', '8', 'irpef.R')).read().split('aliquota_totale_2026')[0] + "\ndifferenza <- round(imposta_2026 - imposta_2025, 2)\ndifferenza\n")

def penali(importo, giorni_ritardo):
    if giorni_ritardo <= 10: p = 0
    elif giorni_ritardo <= 30: p = 0.05
    elif giorni_ritardo <= 60: p = 0.10
    elif giorni_ritardo <= 90: p = 0.20
    else: p = 0.20 + 0.02 * (giorni_ritardo - 90)
    return r2(importo * (1 + p))
lab('penali-fatture', title='Penali sulle fatture', week=2, order=7, level='extra', language='R', ai_mode='on',
    objective="Calcolare il totale di una fattura pagata in ritardo, applicando le penali previste.",
    inputs=[dict(name='importo', type='numero', desc='importo della fattura'), dict(name='giorni_ritardo', type='numero', desc='giorni di ritardo (intero, 0 se puntuale)')],
    output=dict(name='totale', type='numero', desc='importo più penale, 2 decimali'),
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
lab('isee', title='ISEE semplificato', week=2, order=8, level='sfida', language='R', ai_mode='on',
    objective="Calcolare un ISEE semplificato di una famiglia a partire da reddito, patrimonio e numero di componenti.",
    inputs=[dict(name='reddito', type='numero', desc='reddito familiare annuo'), dict(name='patrimonio', type='numero', desc='patrimonio mobiliare e immobiliare'), dict(name='componenti', type='numero', desc='persone nel nucleo (intero ≥ 1)')],
    output=dict(name='isee', type='numero', desc='ISEE, 2 decimali'),
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
lab('bmi', title='Classificazione BMI', week=3, order=1, level='base', language='R', ai_mode='off',
    objective="Calcolare l'indice di massa corporea di un paziente e classificarlo secondo le fasce del Ministero della Salute.",
    inputs=[dict(name='altezza', type='numero', desc='in metri'), dict(name='peso', type='numero', desc='in kg')],
    output=dict(name='classificazione', type='testo', desc='una delle sei categorie, scritta esattamente come nella tabella'),
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
lab('taxi', title='Taxi a Roma', week=3, order=2, level='base', language='R', ai_mode='off',
    objective="Calcolare il costo di una corsa in taxi a Roma a partire dai km percorsi in ogni minuto.",
    inputs=[dict(name='distanza', type='vettore di numeri', desc='km percorsi in ciascun minuto della corsa')],
    output=dict(name='costo', type='numero', desc='costo totale in euro, 2 decimali'),
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

lab('autovelox-funzione', title='Autovelox come funzione', week=3, order=3, level='base', language='R', ai_mode='off',
    objective="Riscrivere l'autovelox come funzione `multa(velocita, limite)` riutilizzabile, e verificarla con gli stessi casi della settimana 2.",
    inputs=[dict(name='velocita', type='numero'), dict(name='limite', type='numero')],
    output=dict(name='multa', type='numero', desc='valore restituito dalla funzione'), function='multa',
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
lab('taxi-uber', title='Taxi o Uber?', week=3, order=4, level='extra', language='R', ai_mode='off',
    objective="Aggiungere al taxi la quota fissa (giorno e ora) e decidere se conviene il taxi o Uber.",
    inputs=[dict(name='distanza', type='vettore di numeri', desc='km per minuto'), dict(name='giorno', type='testo', desc='iniziale del giorno: "L","M","M","G","V","S","D"'), dict(name='ora', type='numero', desc='ora di partenza, da 0 a 23'), dict(name='costo_uber', type='numero', desc='prezzo proposto da Uber')],
    output=dict(name='decisione', type='testo', desc='"Taxi" oppure "Uber"'),
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
lab('portafoglio', title='Portafoglio', week=3, order=5, level='extra', language='R', ai_mode='on',
    objective="Calcolare il valore finale di 100 € investiti, dato il vettore dei rendimenti giornalieri.",
    inputs=[dict(name='rendimenti', type='vettore di numeri', desc='rendimento di ogni giorno in frazione, es. 0.01 = +1%')],
    output=dict(name='valore_finale', type='numero', desc='valore dei 100 € iniziali alla fine, 2 decimali'),
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
lab('rata-mutuo', title='Rata del mutuo', week=3, order=6, level='extra', language='R', ai_mode='on',
    objective="Scrivere la funzione `rata(capitale, tasso, anni)` che calcola la rata mensile di un mutuo a rata costante.",
    inputs=[dict(name='capitale', type='numero', desc='importo del mutuo'), dict(name='tasso', type='numero', desc='tasso annuo in percentuale, es. 4 per il 4%'), dict(name='anni', type='numero', desc='durata in anni')],
    output=dict(name='rata', type='numero', desc='rata mensile, 2 decimali'), function='rata',
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
lab('sconto-fedelta', title='Sconto fedeltà', week=3, order=7, level='sfida', language='R', ai_mode='on',
    objective="Scrivere la specifica e il codice di un programma fedeltà: sconto a soglie più bonus tessera, con un tetto massimo.",
    inputs=[dict(name='totale_carrello', type='numero'), dict(name='tessera', type='testo', desc='"nessuna", "silver" o "gold"')],
    output=dict(name='totale_scontato', type='numero', desc='importo da pagare, 2 decimali'),
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

lab('ecommerce-giovani', title='Clienti giovani', week=4, order=1, level='base', language='R', ai_mode='off',
    objective="Contare gli ordini fatti da clienti con meno di 35 anni nel dataset ecommerce.",
    inputs=[dict(name='data', type='data frame', desc='già caricato: il file ecommerce.csv (colonne CustomerID, OrderID, OrderDate, Age, Gender, Membership, ProductCategory, ProductName, UnitPrice, Quantity, TotalAmount, PaymentMethod, City, ReturnStatus)')],
    output=dict(name='n_giovani', type='numero', desc='numero di righe con Age < 35'),
    data_url='dati/ecommerce.csv', data_var='data', packages=['dplyr'],
    rules="""- Il data frame `data` è già caricato quando premi Verifica (in RStudio: `data <- read.csv("ecommerce.csv")`).
- Conta le righe con `Age < 35`. La colonna `Age` ha valori mancanti: decidi cosa farne e scrivilo nel codice, non lasciarlo al caso.
- Il risultato deve essere un **numero** (non una tabella): da una pipeline dplyr, estrailo con `$n` oppure usa `nrow()` / `sum()`.""",
    fixed=[dict(expected=int((eco.Age < 35).sum()), visible=True, hint="Ricorda: gli NA in Age non sono né < 35 né >= 35. Con filter() spariscono in silenzio; con sum(data$Age < 35) restituiscono NA se non usi na.rm = TRUE.")],
    skeleton="library(dplyr)\n# data è già caricato\n\n# alla fine deve esistere la variabile n_giovani (un numero)\n",
    solution='library(dplyr)\n\nn_giovani <- data %>%\n  filter(!is.na(Age), Age < 35) %>%\n  summarise(n = n())\nn_giovani <- n_giovani$n\nn_giovani\n')

lab('titanic-over50', title='Titanic: gli over 50', week=4, order=2, level='base', language='R', ai_mode='off',
    objective="Quante persone con più di 50 anni erano a bordo del Titanic?",
    inputs=[dict(name='titanic', type='data frame', desc='già caricato: titanic.csv (PassengerId, Survived, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked)')],
    output=dict(name='n_over50', type='numero', desc='passeggeri con Age > 50'),
    data_url='dati/titanic.csv', data_var='titanic', packages=['dplyr'],
    rules="""- Conta i passeggeri con `Age > 50` (età nota).
- Estrai il numero dalla tabella di `summarise()`.
- Poi, in RStudio, continua con le altre domande della settimana: la percentuale di uomini e donne tra gli over 50 (percentuale *rispetto a chi?*).""",
    fixed=[dict(expected=int((tit.Age > 50).sum()), visible=True, hint="177 passeggeri non hanno l'età: filter(Age > 50) li scarta da solo, ma devi saperlo e dirlo.")],
    skeleton="library(dplyr)\n# titanic è già caricato\n\n# alla fine deve esistere la variabile n_over50 (un numero)\n",
    solution='library(dplyr)\n\nrisultato <- titanic %>%\n  filter(!is.na(Age), Age > 50) %>%\n  summarise(n = n())\nn_over50 <- risultato$n\nn_over50\n')

lab('titanic-prima-classe', title='Titanic: sopravvivenza in prima classe', week=4, order=3, level='extra', language='R', ai_mode='on',
    objective="Qual è la percentuale di sopravvissuti tra i passeggeri di prima classe?",
    inputs=[dict(name='titanic', type='data frame', desc='già caricato: titanic.csv')],
    output=dict(name='perc_prima', type='numero', desc='quota di sopravvissuti in prima classe, tra 0 e 1 (3 decimali)'),
    data_url='dati/titanic.csv', data_var='titanic', packages=['dplyr'], tolerance=0.002,
    rules="""- `Survived` vale 1 se sopravvissuto, 0 altrimenti: la **media** di Survived è già la percentuale.
- Raggruppa per `Pclass`, calcola la media per classe, poi estrai il valore della classe 1.
- Confronta con la terza classe: la differenza è il punto della domanda.""",
    fixed=[dict(expected=round(float(tit[tit.Pclass == 1].Survived.mean()), 3), visible=True, hint="La percentuale è calcolata *dentro* la classe (denominatore: i passeggeri di prima classe), non sul totale dei sopravvissuti.")],
    skeleton="library(dplyr)\n# titanic è già caricato\n\n# alla fine deve esistere la variabile perc_prima (un numero tra 0 e 1)\n",
    solution='library(dplyr)\n\ntabella <- titanic %>%\n  group_by(Pclass) %>%\n  summarise(perc = mean(Survived))\nperc_prima <- round(tabella$perc[tabella$Pclass == 1], 3)\nperc_prima\n')

lab('titanic-biglietti', title='Titanic: biglietti condivisi', week=4, order=4, level='sfida', language='R', ai_mode='on',
    objective="Quanti biglietti erano associati a più di un passeggero?",
    inputs=[dict(name='titanic', type='data frame', desc='già caricato: titanic.csv')],
    output=dict(name='n_condivisi', type='numero', desc='numero di codici Ticket con almeno 2 passeggeri'),
    data_url='dati/titanic.csv', data_var='titanic', packages=['dplyr'],
    rules="""- Raggruppa per `Ticket`, conta i passeggeri per biglietto, tieni solo i biglietti con più di uno.
- Il risultato è il numero di **biglietti**, non di passeggeri.
- Servono due passaggi di conteggio: uno dentro i gruppi, uno sul risultato.""",
    fixed=[dict(expected=int((tit.Ticket.value_counts() > 1).sum()), visible=False, hint="Stai contando biglietti o passeggeri? Dopo il primo summarise ogni riga è un biglietto: contale con nrow() o n().")],
    skeleton="library(dplyr)\n# titanic è già caricato\n\n# alla fine deve esistere la variabile n_condivisi (un numero)\n",
    solution='library(dplyr)\n\nbiglietti <- titanic %>%\n  group_by(Ticket) %>%\n  summarise(n = n()) %>%\n  filter(n > 1)\nn_condivisi <- nrow(biglietti)\nn_condivisi\n')

# ─────────────────────────── SETTIMANA 5 ───────────────────────────
lab('finanza-volatilita', title='Finanza: la volatilità', week=5, order=1, level='base', language='R', ai_mode='off',
    objective="Calcolare la volatilità (deviazione standard dei rendimenti giornalieri) del titolo Unicredit.",
    inputs=[dict(name='returns', type='data frame', desc='già caricato: finanza.csv (Ferrari, Enel, Intesa, Unicredit, day) con i rendimenti giornalieri del 2023')],
    output=dict(name='volatilita', type='numero', desc='deviazione standard dei rendimenti di Unicredit (4 decimali)'),
    data_url='dati/finanza.csv', data_var='returns', tolerance=0.0002,
    rules="""- In finanza il rischio di un titolo si misura con la **variabilità** dei suoi rendimenti: `sd()`.
- Calcola `sd(returns$Unicredit)` e arrotonda a 4 decimali.
- In RStudio confronta le quattro azioni: quale ha il rendimento medio più alto? quale il rischio più alto? coincidono?""",
    fixed=[dict(expected=round(float(fin.Unicredit.std(ddof=1)), 4), visible=True, hint="sd() usa n−1 al denominatore: è quella che vogliamo. Non c'è nessun NA, quindi non serve na.rm.")],
    skeleton="# returns è già caricato\n\n# alla fine deve esistere la variabile volatilita\n",
    solution="volatilita <- round(sd(returns$Unicredit), 4)\nvolatilita\n")

lab('finanza-correlazione', title='Finanza: due banche', week=5, order=2, level='extra', language='R', ai_mode='on',
    objective="Misurare quanto i rendimenti di Intesa e Unicredit si muovono insieme.",
    inputs=[dict(name='returns', type='data frame', desc='già caricato: finanza.csv')],
    output=dict(name='correlazione', type='numero', desc='coefficiente di correlazione tra Intesa e Unicredit (3 decimali)'),
    data_url='dati/finanza.csv', data_var='returns', tolerance=0.002,
    rules="""- `cor(x, y)` misura quanto due serie salgono e scendono insieme: da −1 a +1.
- Calcola la correlazione tra `Intesa` e `Unicredit` e arrotonda a 3 decimali.
- Poi in RStudio fai il grafico a dispersione con ggplot2 e confronta con la coppia Ferrari–Enel.""",
    fixed=[dict(expected=round(float(fin.Intesa.corr(fin.Unicredit)), 3), visible=True, hint="La correlazione è simmetrica: cor(Intesa, Unicredit) = cor(Unicredit, Intesa). Se ottieni un numero diverso, forse hai preso una colonna sbagliata.")],
    skeleton="# returns è già caricato\n\n# alla fine deve esistere la variabile correlazione\n",
    solution="correlazione <- round(cor(returns$Intesa, returns$Unicredit), 3)\ncorrelazione\n")

# ─────────────────────────── scrittura file ───────────────────────────
def build_tests(L):
    tests = []
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

class Lit(str): pass
def lit_repr(dumper, data): return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
yaml.add_representer(Lit, lit_repr)

for L in LABS:
    fm = dict(layout='lab', title=L['title'], week=L['week'], order=L['order'], level=L['level'], language=L['language'], ai_mode=L['ai_mode'],
              objective=L['objective'], inputs=L['inputs'], output=L['output'])
    if L.get('function'): fm['function'] = L['function']
    for k in ('data_url', 'data_var', 'packages', 'tolerance'):
        if k in L: fm[k] = L[k]
    fm['skeleton'] = Lit(L['skeleton'])
    fm['tests'] = build_tests(L)
    fm['solution'] = Lit(L['solution'])
    fm['solution_after'] = ''
    y = yaml.dump(fm, allow_unicode=True, sort_keys=False, width=1000)
    with open(os.path.join(OUT, L['slug'] + '.md'), 'w') as f:
        f.write('---\n' + y + '---\n\n' + L['rules'].strip() + '\n')
print('lab generati:', len(LABS))
for L in LABS: print(' ', L['week'], L['level'].ljust(5), L['slug'])
