---
id: INVEST
aliases: []
tags:
  - assignatura/ES
  - tipus/teoria
---

# INVEST

**Referència: [[UserStories]] Diapositives 7-13**

Els sis principis que ha de complir una bona **user story**. Segons el PDF, les user stories han de ser:

- **Independent**
  - Tan independents com sigui possible; sovint és més fàcil pensar-ho com **"order independent"**: es poden fer en **qualsevol ordre**.
  - Això permet una **priorització real** de cada story. Quan hi ha **dependències**, pot ser impossible implementar una story valuosa sense implementar-ne d'altres **molt menys valuoses**.
- **Negotiable**
  - Una story **no és un contracte**; **és una invitació a la conversa**. Captura l'**essència** del que es desitja.
  - El resultat ha de ser el producte d'una **negociació col·laborativa** entre **client, desenvolupador i tester** (com a mínim).
  - L'objectiu és **satisfacer les necessitats del client**, no desenvolupar a la lletra de la story si això és **insuficient**.
  - Pregunta màgica per fer avançar la conversa: ***"How will I know I've done that?"***
- **Valuable**
  - Si una story no té valor **discernible**, **no s'ha de fer**.
  - Les stories es prioritzzen al backlog pel **valor de negoci**, així que hauria de ser evident.
  - La story té valor per a l'**"user"** de la user story.
  - La clàusula **"so that <value>"** hi és per una raó: és **exactament el valor** que intentem lliurar.
- **Estimable**
  - Ha de poder **estimar-se o dimensionar-se** per prioritzar-se correctament. Una story d'alt valor però amb temps de desenvolupament **molt llarg** pot no ser la prioritat més alta.
  - Si **no es pot estimar**: **divideix** la story (sovint guanyes claredat). Si dividir no ajuda, potser cal fer **recerca sobre la story primer**.
- **Small**
  - Quin de petit? Depèn de l'equip i la metodologia.
  - Sugerència: **iteracions de 2 setmanes** → stories de **3-4 dies de treball de mitjana — TOTAL!** (inclou tot el treball per arribar a l'estat "done").
  - Fes **la cosa més senzilla que funciona — i para!**
- **Testable**
  - Tota story ha de poder **testar-se** per estar "done". De fet, és útil pensar que **testable = es poden escriure els acceptance criteria immediatament**.
  - Això fomenta **col·laboració primerenca**, **construeix qualitat** movent el QA cap amunt del procés, i permet transformar fàcilment a un procés d'**acceptance test-driven development**.

> [!tip] Mnemòtec: **I-N-V-E-S-T**. Cada lletra és un motiu pel qual una story "no està bé" — si una story no va, pregunta quina lletra falla.

Vegeu també: [[User Story]] · [[Three C's]] · [[Piràmide de requisits]]
