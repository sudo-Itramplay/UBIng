---
id: Piràmide de requisits
aliases: []
tags:
  - assignatura/ES
  - tipus/teoria
---

# Piràmide de requisits

**Referència: [[UserStories]]** · *(imatge de classe; el PDF no la defineix)*

![[Piramide Requisits.png]]

De dalt a baix, d'objectius de negoci a criteris de validació:

| Nivell | Què és |
|---|---|
| **Vision** | Descriu els **objectius de negoci** |
| **Theme** | Les **capacitats** que el producte lliurat ha de proveir per **valer la pena ser alliberat** |
| **Epic** | **Permet a un usuari** aconseguir un **objectiu de negoci clarament identificat** |
| **User Story** | Un **requisit d'usuari** que s'ha d'**implementar** al sistema lliurat |
| **Acceptance Criteria** | **Criteris** necessaris per **validar** una [[User Story|user story]] |

Com es construeix de baix a dalt (exercici "Starting Product Backlog" del PDF):

1. Tria un projecte (**Theme**).
2. Comença pels **Epics**.
3. **Descompon** els Epics en **User Stories**.
4. GOTO 1.

> [!warning] On es confonen **Epic vs User Story**: l'Epic és un **objectiu de negoci** gran que un usuari aconsegueix; la story és un **requisit concret** a implementar. L'Epic es **descomposa** en stories. I l'**Acceptance Criteria** no és un nivell de requisit sinó **com saps si una story s'ha fet bé**.

Vegeu també: [[Product Backlog]] · [[INVEST]]
