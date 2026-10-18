---
id: UserStories
aliases:
  - User Stories
tags:
  - assignatura/ES
  - tipus/teoria
---

# User Stories

**Referència: Diapositives 1-19** (`PDFs/UserStories.pdf` — Eloi Puertas, basat en les diapos d'Oriol Pujol)

## Product Backlog (context)

- Llista **prioritzada** de totes les features i funcionalitats necessàries per completar el projecte.
- Conté **tot** el que el projecte requerirà i **evoluciona** amb el temps: no només features noves, sinó també **bug fixes** i **recerca** — qualsevol cosa que consumeixi temps de l'equip.
- Respon les preguntes **"què estem construint i per què?"**; aquesta informació es captura en **work items**.
- Al **inici** de qualsevol projecte és poc probable tenir una llista neta i ben definida d'items llestos per estimar i prioritzar; normalment tens una pila de **story note cards** i potser alguna especificació funcional.

**Referència: Diapositives 2-3** · relacionat: [[Product Backlog]]

## Stories, no tasks

- El consell número u per escriure una bona user story: **write stories, not tasks**.
- La finalitat de la story és **iniciar la conversa** sobre què necessita el negoci i com es pot satisfer amb **programari**.
- La user story **no és una especificació final** lliurada per implementar.

### Three C's

Els detalls d'una story viuen en tres llocs:

| C | Què és |
|---|---|
| **Card** | Les stories s'escriuen tradicionalment en **note cards** (post-its), que poden portar anotacions d'estimacions i notes. Propòsit: **iniciar la conversa** entre tècnics i negoci des d'un **punt comú d'enteniment** |
| **Conversation** | Els **detalls** de la story surten durant les **converses amb el Product Owner** |
| **Confirmation** | Els **acceptance tests confirmen** que la story s'ha codificat correctament — la validació de les **expectatives del Product Owner** |

**Referència: Diapositives 4-6** → [[User Story]] · [[Three C's]]

## INVEST

Les user stories han de ser:

- **Independent**
  - Tan independents com sigui possible; sovint és més fàcil pensar-ho com **"order independent"**: les stories es poden fer en **qualsevol ordre**.
  - Això permet una **priorització real** de cada story. Quan hi ha **dependències**, pot ser impossible implementar una story valuosa sense implementar-ne d'altres **molt menys valuoses**.
- **Negotiable**
  - Una story **no és un contracte**; **és una invitació a la conversa**. Captura l'**essència** del que es desitja.
  - El resultat ha de ser el producte d'una **negociació col·laborativa** entre **client, desenvolupador i tester** (com a mínim).
  - L'objectiu és **satisfacer les necessitats del client**, no desenvolupar a la lletra de la story si això és **insuficient**.
  - Pregunta màgica per fer avançar la conversa: ***"How will I know I've done that?"***
- **Valuable**
  - Si una story no té valor **discernible**, **no s'ha de fer**.
  - Com que les stories es prioritzen al backlog pel **valor de negoci**, això hauria de ser evident.
  - La story té valor per a l'**"user"** de la user story.
  - La clàusula **"so that <value>"** hi és per una raó: és **exactament el valor** que intentem lliurar.
- **Estimable**
  - Ha de poder **estimar-se o dimensionar-se** per poder prioritzar-se correctament. Una story d'alt valor però amb temps de desenvolupament **molt llarg** pot no ser la prioritat més alta.
  - Si **no es pot estimar**: **divideix** la story (sovint guanyes claredat). Si dividir no ajuda, potser cal fer **recerca sobre la story primer**.
- **Small**
  - Sí, són trossos petits... **però quin de petit?** Depèn de l'equip i la metodologia.
  - Sugerència: **iteracions de 2 setmanes** → stories de **3-4 dies de treball de mitjana — TOTAL!** (inclou tot el treball per arribar a l'estat "done").
  - Fes **la cosa més senzilla que funciona — i para!**
- **Testable**
  - Tota story ha de poder **testar-se** per estar "done". De fet, és útil pensar que **testable = es poden escriure els acceptance criteria immediatament**.
  - Això fomenta **col·laboració primerenca**, **construeix qualitat** movent el QA cap amunt del procés, i permet transformar fàcilment a un procés d'**acceptance test-driven development**.

**Referència: Diapositives 7-13** → nota atòmica: [[INVEST]]

## Piràmide de requisits

![[Piramide Requisits.png]]

| Nivell | Què és |
|---|---|
| **Vision** | Descriu els **objectius de negoci** |
| **Theme** | Les **capacitats** que el producte lliurat ha de proveir per **valer la pena ser alliberat** |
| **Epic** | **Permet a un usuari** aconseguir un **objectiu de negoci clarament identificat** |
| **User Story** | Un **requisit d'usuari** que s'ha d'**implementar** al sistema lliurat |
| **Acceptance Criteria** | **Criteris** necessaris per **validar** una user story |

Com es construeix (exercici final del PDF — "Starting Product Backlog"):

1. Tria un projecte (**Theme**).
2. Comença pels **Epics**.
3. **Descompon** els Epics en **User Stories**.
4. GOTO 1.

**Referència: Diapositiva 19** · piràmide: imatge de classe → [[Piràmide de requisits]]

## No tot és una story

Certes necessitats de negoci **no es poden expressar** com a story:

- Un **change request** (petició de canvi).
- Una **constraint**: rendiment requerit, stack tecnològic, base de dades a fer servir.
- Un **requisit tècnic**: protocol de comunicació, compliment d'estàndards de seguretat.

No intentis **encabir-los** al format de user story — escriu-los en **text pla**. Les user stories per a sistemes **backend** són habitualment un tema **difícil** en qualsevol projecte.

## Bad user stories

Errors típics del PDF:

- **"Auto-save every few minutes"** — és una tasca, no una story. Correcció del PDF: *"As a player, I want auto-save the current game after key events, so that one does not have to repeat the whole stage."*
- **"Add tips and reminders of user interface functionality"** — mateix cas. Correcció: *"As a novice player, I want UI tips so that I can get familiar with controls and icons"*
- **"Fix bug #127"** — no diu ni per a qui ni quin valor aporta.
- **"Decrease loading time"** — objectiu vagu, sense rol ni benefici.

## TIPS per escriure bones stories

- Per **identificar** stories, comença pels **objectius de cada rol d'usuari** en fer servir el sistema.
- En **dividir** una story, intenta stories que **cappen totes les capes** de l'aplicació.
- Stories **petites** per a la funcionalitat que s'implementarà **aviat**; stories **àmplies** per a la funcionalitat més **llunyana**.
- Mantén la **interfície d'usuari fora** de les stories el màxim de temps possible.
- Escriu stories per a un **sol usuari**.
- Mantén les stories **curtes**.
- Que sigui el **client**, no el desenvolupador, qui **escrigui** la story.

## Conclusions

- **Write stories, not tasks**
- Segueix els principis **INVEST**
- Comença la **conversa** el més aviat possible

## FITXA de repàs

| Element | Què és | Regla clau |
|---|---|---|
| **Format story** | As a \<rol\> · I want \<objectiu\> · So that \<benefici\> · Acceptance criteria | El "so that" és el **valor** |
| **Three C's** | Card · Conversation · Confirmation | La card només **inicia** la conversa; els detalls surten parlant |
| **INVEST** | 6 qualitats d'una bona story | Independent, Negotiable, Valuable, Estimable, Small, Testable |
| **Piràmide** | Vision → Theme → Epic → User Story → Acceptance Criteria | D'objectius de negoci a criteris de validació |
| **No tot és story** | Change requests, constraints, requisits tècnics | **Text pla**, no format story |
| **Qui escriu** | El **client** | La story **no és** una especificació |

## Dubtes / a revisar

- La diapositiva "Types of user stories" és **només un separador** sense contingut — sembla que l'únic tipus treballat és el format "As a...".
- "Bad user stories": confirmar a classe si les dues primeres es reescriuen en format "As a..." (sembla que sí pel format de la diapositiva).
- La piràmide (Vision → Theme → Epic → User Story → Acceptance Criteria) **no surt definida al PDF** — ve de la imatge de classe; comprovar si es pot avaluar.

---
[[_Index_ES]] · [[SCRUM]] · [[Product Backlog]]
