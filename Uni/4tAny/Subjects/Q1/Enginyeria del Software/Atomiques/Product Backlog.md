---
id: Product Backlog
aliases: []
tags:
  - assignatura/ES
  - tipus/teoria
---

# Product Backlog

**Referència: [[SCRUM]] Diapositives 8-11**

Llista **refinada i prioritzada** de features que neix de la **Product Vision** de la Product Owner. És el **road map** del producte.

- Existeix i **evoluciona** al llarg de tota la vida del producte.
- En qualsevol punt és la visió **única i definitiva** de "tot el que l'equip podria fer mai, per ordre de prioritat".
- **Només n'existeix un de sol**.
- El primer pas per començar Scrum és la Product Vision de la PO → es converteix en aquesta llista.

Què hi ha a dins — **els 4 tipus d'item** (es fan servir per tota la vida del producte, no només coses noves):

| Tipus | Què és, exactament | Pregunta que respon | Exemple |
|---|---|---|---|
| **Feature de client** | Capacitat **nova** que l'usuari pot fer i abans no podia | "Què pot fer l'usuari que abans no podia?" | "enable all users to place book in shopping cart" |
| **Millora d'enginyeria** (*engineering improvement*) | Algo que **ja funciona** però es reforça o reescriu perquè vagi millor (escalabilitat, rendiment, deute tècnic). L'usuari no veu cap funció nova | "Què funciona, però malament o fràgil?" | "rework the transaction processing module to make it scalable" |
| **Exploració / recerca** | Encara **no se sap com** fer-ho: investigar opcions abans de comprometre's. És **incertesa**, encara no toca el codi de producció | "Què hem de descobrir abans de decidir?" | "investigate solutions for speeding up credit card validation" |
| **Defecte conegut** (*known defect*) | Algo existent **no funciona com hauria** (s'ha detectat, potser ni està a Production) | "Què està trencat?" | "diagnose and fix the order processing script errors" |

> [!warning] On es confonen els 4:
> - **Millora vs defecte**: la millora *funciona* però es vol que vagi millor; el defecte *no funciona* com hauria.
> - **Millora vs exploració**: a la millora **ja saps com** fer-ho; a l'exploració **encara no** — l'item és descobrir-ho.
> - **Exploració vs feature**: l'exploració no dona cap capacitat nova a l'usuador, dona **informació** per decidir.
> - **Defecte vs feature**: arreglar el trencat ≠ oferir el nou.

- **Release Backlog** = subconjunt destinat a l'alliberament actual; focus principal de la PO.
- Cada item es valora amb **prioritat**, estimació de **valor** i estimació d'**esforç**.

> [!warning] **Product Backlog** (única, tota la vida) vs **Release Backlog** (subconjunt per a un alliberament). Truc d'examen.

Dins d'un sprint, els items seleccionats es descomposen al [[Sprint]] Backlog en tasques individuals. Sovint s'escriuen com a [[User Story|user stories]].

Vegeu també: [[Scrum Roles]] · [[Definition of Done]]
