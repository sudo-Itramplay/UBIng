---
id: KANBAN
aliases: []
tags:
  - assignatura/ES
  - tipus/teoria
---

# KANBAN

**Referència: Diapositives 1-37** (`PDFs/KANBAN.pdf` — Eloi Puertas, basat en les diapos d'Oriol Pujol)

## Què és Kanban

- Tècnica **industrial** per **"pulling"** el treball a través de tot el seu **cicle de vida**, fent que flueixi de manera més **suau** i a un **ritme més alt**.
- Kanban també **il·lumina les activitats normalment ocultes**. Aquesta visibilitat és a **dos nivells**: activitats individuals i el cicle de vida **com a tot**.
- La paraula **"Kanban"** és **japonesa** i vol dir **"Visual Card"**.

## El rol de Kanban

Kanban tracta de **millorar l'agilitat de negoci**. Preguntes que et fa:

- **Quant sovint** es produeixen discussions amb els clients?
- **Quant triga** a fer alguna cosa un cop **ens hem compromès**?
- **Quant sovint** podem **desplegar** una feature nova?

Kanban dóna eines: **replenishment cadence**, **lead time**, **delivery cadence**.

## Objectius de Kanban

- Minimitzar **retards** (waste).
- **Millorar la qualitat**.
- **Lliurar aviat i sovint**.
- **Equilibrar** demanda i throughput.
- Millorar la **predicibilitat**.
- **Prioritzar per resultat** (outcome).

## Principis de Kanban

1. **Visualize Work** — visualitza la feina.
2. **Limit Work-In-Progress (WIP)** — limita el treball en progrés.
3. **Make Policies Explicit** — fes les polítiques explícites.
4. **Measure and Manage workflow** — mesura i gestiona el flux.

## Tauler: lanes i cards

El primer pas per **visualitzar el flux** és entendre el **procés actual**:

- **On és ara?** ("estic treballant-hi" → "està en desenvolupament"; "està acabat però no testejat" → "esperant test").
- **On anirà?** ("quan acabi serà llest per test"; "després serà testejat i llest per integració").
- **On era abans?** ("l'analista de negocis hi havia treballat abans" → "anàlisi fet / llest per desenvolupar").

Lanes del tauler creixen d'aquestes preguntes:

```
Ready for development → In development → In test → Ready for integration
```

Layout bàsic (qualsevol projecte):

```
TO DO  →  Work in Progress  →  Done
```

Layout ampliat:

```
TO DO → Analyze → DEV → TEST → DONE
```

- **Lanes** descriuen **accions**.
- **Cards** descriuen **coses amb valor que l'equip lliura** (user stories, tasques).

> [!tip] Exercici "Do your kanban wall!": per a cada tasca, respon — **quin tipus de feina és? on és ara? on era abans de jo agafar-la? on anirà un cop acabi la meva feina?**

## Límits de Work In Progress

- Les tècniques àgils es basen en **lliurament continu i freqüent**; **limitar el WIP** és una manera d'aconseguir-ho.
- *"Amb dues mans només pots ser competent amb fins a dues eines — per què planificar com si en tinguéssim més?"*

Kanban és **mantenir el flux i eliminar el waste**:

- Posa **límits a les columnes** on es fa la feina.
- **Trobar els límits correctes és dur**: comença amb una **millor estimació** i **afina** (fine-tune).
- Objectiu final: **throughput constant alt** i rendiment personal/equip.

> [!warning] **Nota de capacitat**: 100% de capacitat a totes les lanes significa **throughput mínim**. És com un **embús de tràfic**: si totes les lanes són al màxim, el flux segueix els elements al capdavant i **s'atura fàcilment**. És un símptoma de **congestió** que pot portar a **blocking**.

## No emparris, pulla

- Fàcil generar **fricció** entre equips, especialment quan un és més performant i **empenta** més feina de la que l'altre pot manejar.
- Sistema **pull**: un equip **pulla** feina quan **està llest** per a ella.
- Cada cop que algú pulla un item, **identifica l'ownership** de les tasques.

## Cues al tauler

- Amb diversos **equips interdependents**, l'equip **més lent** pot **bloquejar tot el procés**.
- Com que fem servir **pull**, una lane bloquejada vol dir que l'equip responsable **no pot pullar feina nova** fins que l'equip bloquejant pulli un item.
- Per això és **raonable afegir cues** (queues) al tauler. Aquestes també tenen una **capacitat màxima**.

Exemple de tauler amb cues:

```
TO DO | DEV [WIP máx. 2] [cua "fet" 3] | TEST [WIP máx. 2] | DONE
```

## Assignació de tasques

Un tester ha acabat la seva tasca. Què fa?

1. **Assistir** l'altre tester si cal.
2. **Pullar** feina nova.

> [!warning] **REGLA: centra't des de l'ítem més a la dreta** (rightmost). Després de completar, pulla feina nova.

**Starvation**: un equip sense feina mentre la resta van plens → **swarm with the dev team!** (vés a ajudar l'equip de desenvolupament).

## Bugs al final del procés

Es troba un **bug a la lane DONE**: l'item **no es pot marcar com a done**. Què fem?

1. **Primer: adapta el procés per reflectir el escenari real.** Si es troba un bug, **no estava "done"**: s'ha detectat **durant el procés d'acceptació** de l'item → afegeix una lane **ACCEPT** on l'item es "rebutja" amb el bug.
2. **Moure l'item enrere a DEV?** **DISALLOWING MOVING BACK INCENTIVES FINISHING THE TASKS** — no permetre que torni enrere **incentiva acabar** les tasques.
3. Solucions:
   - **(A)** **Redefinir QA** com a testing **i** bug fixing → **SWARM ON THE BUG** (tots sobre el bug).
   - **(B)** L'item **NO es mou**!!! S'introdueix un **item nou** a TODO: **"BUG"**.

## Polítiques explícites

- **Definir polítiques explícites** = definir el **procés d'assegurament de qualitat** (QA Process). Mostrant-les explícitament, podem **verificar-les** a cada stage del procés.
- A Kanban es fa afegint una **descripció de la política de qualitat** a seguir cada vegada que una tasca **transiciona** a un stage.

Exemple:

| Quan... | Política |
|---|---|
| Una tasca **s'introdueix** | Escriu-hi la **data** |
| Un item es **pulla a WIP** | Escriu la **data del pull** |
| Un item es **pulla a DONE** | Escriu la **data del pull** |

Pregunta oberta del PDF: **quines polítiques són útils per al teu flux?**

## Mesurar i gestionar el flux

- **Eina**: **Cumulative Flow Chart**. Cada dia **marca quantes tasques hi ha a cada columna**.
- **Llegida vertical**: un punt del graf ens parla del **treball en progres** (new arrivals / currently working on / departures).
- **Llegida horizontal**: ens parla de la **durada** de les tasques:

| Concepte | Definició |
|---|---|
| **Lead time** | Temps entre **inici i lliurament** d'un item — **el que el client veu** |
| **Cycle time** | Temps entre **inici i completió** d'un item — **mesura de la capacitat real del procés** |
| **Throughput** | **Items / temps** |

**Referència: Diapositives 34-36** → [[Cumulative Flow Chart]] · [[Lead Time i Cycle Time]]

## Conclusió: Scrumban

**Què triar, SCRUM o KANBAN? SCRUMBAN!**

| De | Agafa |
|---|---|
| **SCRUM** | Les **iteracions i artefactes**: Backlogs, Sprint, Daily meetings, Revision, Retrospective |
| **KANBAN board** | Per **visualitzar i fer seguiment** del progrés **durant els sprints** i **limitar el WIP** |

**Referència: Diapositiva 37** · relacionat: [[SCRUM]] · [[Agile vs Scrum]]

## FITXA de repàs

| Element | Què és | Regla clau |
|---|---|---|
| **Kanban** | Tècnica de **pull** del treball; "Visual Card" (japonès) | Flux suau + activitats **visibles** |
| **4 principis** | Visualize · Limit WIP · Explicit policies · Measure & Manage | Estructura del tema |
| **Lanes vs cards** | Lanes = **accions** · Cards = **coses amb valor** (US, tasques) | El tauler neix de les 3 preguntes |
| **WIP** | Límit per columna | 100% capacitat = **embús** |
| **Pull** | L'equip pulla quan **està llest** | Mai push; identifica **ownership** |
| **Cues** | Entre equips interdependents | També tenen **capacitat màxima** |
| **Task assignment** | Opcions: assistir / pullar | **Rightmost first**; starvation → **swarm** |
| **Bug a DONE** | Adapta el procés (lane ACCEPT) | **Mai cap enrere**; (A) swarm on the bug / (B) nou item BUG a TODO |
| **Lead vs Cycle** | Lead = el que veu el **client** · Cycle = **capacitat real** | Throughput = items temps |
| **Scrumban** | Scrum (iteracions+artefactes) + tauler Kanban | El tauler viu **dins** dels sprints |

## Dubtes / a revisar

- La frase **"DISALLOWING MOVING BACK INCENTIVES FINISHING THE TASKS"** té phrasing estrany — confirmar a classe el sentit exacte.
- Les diapos d'exemples de tauler (pàg. 20-30) són **esquemes visuals** sense text; he reconstruït els taulers des del text extret — comprovar si el layout exacte importa per a l'examen.
- **Replenishment cadence** i **delivery cadence** apareixen esmentats com a eines però **no es defineixen** al PDF.

---
[[_Index_ES]] · [[SCRUM]] · [[Agile vs Scrum]]
