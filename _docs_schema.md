# Schema dei contenuti (branch 2026-27)

## _settimane/NN-slug.md

```yaml
---
layout: settimana
number: 2                 # 1..12
title: Decidere
pillar: 1                 # 1 = Il codice (R) · 2 = Come imparano le macchine · 3 = LLM e agenti
language: R               # R | Python | R → Python
idea: "Il computer sceglie un ramo in base a una condizione."   # una frase
hours: 5
dates: []                 # es. [2026-09-21, 2026-09-25] — da compilare
concepts_new: [if/else, else if, operatori logici, "%in%"]      # concetti introdotti (stringhe brevi, riusate identiche altrove)
concepts_required: [variabili, confronti]                       # concetti che devono già essere noti (stessa stringa usata in concepts_new di un'altra settimana)
explorations: []          # slug di _esplorazioni
slides_pdf:               # opzionale
---
```
Il corpo è la **lezione in markdown**: spiegazione estesa (più di quanto detto in aula), con:
- blocchi di codice R con ```r
- box "In aula abbiamo visto solo…" scritto come `> **In aula** …` (blockquote)
- box attenzione per i casi limite: `> **Attenzione** …`
- un paragrafo finale "Per approfondire" con link alla settimana precedente/successiva quando serve.
I lab NON si elencano nel corpo: li aggiunge il layout leggendo `_lab` (campo `week`).

## _lab/slug.md

```yaml
---
layout: lab
title: Autovelox
week: 2
level: base               # base | extra | sfida
language: R               # R | Python
ai_mode: off              # off (fatto a mano in aula) | on (con l'assistente)
objective: "Calcolare la sanzione per eccesso di velocità secondo l'art. 142 CdS."
inputs:
  - {name: velocita, type: numero, desc: "velocità rilevata in km/h"}
  - {name: limite,   type: numero, desc: "limite di velocità in km/h"}
output: {name: multa, type: numero, desc: "importo della sanzione in euro"}
skeleton: |
  velocita <- 70
  limite <- 50

  # scrivi qui il tuo codice: alla fine deve esistere la variabile multa
tests:                    # i primi con visible: true compaiono nella specifica come esempi
  - {inputs: {velocita: 45, limite: 50}, expected: 0, visible: true}
  - {inputs: {velocita: 60, limite: 50}, expected: 36, boundary: true, hint: "Hai controllato cosa succede a esattamente 10 km/h oltre il limite?"}
tolerance: 0.01           # tolleranza numerica (default 0.01)
solution: |
  velocita <- 70
  ...
solution_after: 2026-09-25   # per i lab base: data dopo cui la soluzione è visibile (vuoto = subito dopo il superamento)
---
```
Il corpo del lab è la sezione **Regole** in markdown (elenco o tabella, come nelle slide), più eventuale contesto (una o due righe).
