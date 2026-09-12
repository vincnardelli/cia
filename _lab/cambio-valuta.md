---
layout: lab
title: Cambio valuta
week: 1
order: 2
level: extra
language: R
ai_mode: 'off'
objective: Convertire un importo in euro in dollari applicando la commissione dello sportello.
inputs:
- name: importo_euro
  type: numero
  desc: euro da cambiare
- name: tasso
  type: numero
  desc: dollari per un euro, es. 1.08
output:
  name: dollari
  type: numero
  desc: dollari ricevuti, arrotondati a 2 decimali
skeleton: |
  importo_euro <- 100
  tasso <- 1.08

  # alla fine deve esistere la variabile dollari
tests:
- inputs:
    importo_euro: 100
    tasso: 1.08
  expected: 105.84
  visible: true
- inputs:
    importo_euro: 500
    tasso: 1.1
  expected: 544.5
  visible: true
- inputs:
    importo_euro: 200
    tasso: 1.0
  expected: 198.0
  visible: false
  boundary: true
  hint: 'A 200 € l''1% vale esattamente 2 €: le due commissioni coincidono, il risultato deve essere lo stesso qualunque delle due scegli.'
- inputs:
    importo_euro: 2
    tasso: 1.08
  expected: 0
  visible: false
  boundary: true
  hint: 'Con 2 € la commissione mangia tutto l''importo: cosa resta da cambiare?'
- inputs:
    importo_euro: 1
    tasso: 1.08
  expected: 0
  visible: false
  boundary: true
  hint: 'Con 1 € il netto è negativo: il risultato deve essere 0, non un numero negativo.'
- inputs:
    importo_euro: 1000
    tasso: 0.95
  expected: 940.5
  visible: false
solution: |
  importo_euro <- 100
  tasso <- 1.08

  commissione <- max(2, importo_euro * 0.01)
  netto <- importo_euro - commissione
  if(netto > 0){
    dollari <- round(netto * tasso, 2)
  }else{
    dollari <- 0
  }
  dollari
solution_after: ''
---

- La commissione è il **maggiore** tra 2 € e l'1% dell'importo.
- Si cambia solo l'importo al netto della commissione: `dollari = (importo - commissione) * tasso`.
- Se l'importo non copre nemmeno la commissione, si ricevono 0 dollari (mai un valore negativo).
- Arrotonda a due decimali.
