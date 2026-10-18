---
id: SCRUM
aliases: []
tags:
  - assignatura/ES
  - tipus/teoria
---

# SCRUM

**Referència: Diapositives 1-25** (`PDFs/SCRUM.pdf` — Eloi Puertas, basat en les diapos d'Oriol Pujol)

## Què és

**Scrum** és una metodologia àgil on els productes es construeixen en una sèrie d'**iteracions de durada fixa**. Quatre pilars donen estructura al framework:

1. **Sprint planning**
2. **Stand ups** (daily meetings)
3. **Sprints**
4. **Retrospectives**

Característiques:

- Pràctica àgil que lliura programari als usuaris més ràpid i millor.
- Suporta una **aproximació creativa** al desenvolupament.
- Val per a qualsevol complexitat i innovació.
- **Escala linealment** a grans nombres de desenvolupadors.

> [!note] Tema central: **inspect and adapt**
> Desenvolupar implica aprendre, innovar i tenir sorpreses. Per això Scrum mana fer un **pas curt** de desenvolupament, **inspeccionar** tant el producte resultant com l'eficàcia de les pràctiques actuals, **adaptar** els objectius de producte i les pràctiques de procés, i **repetir per sempre**.

**Referència: Diapositives 1-3**

## Agile vs Scrum

> [!question] Quina diferència hi ha? És una especialització?
> - **Agile** és una **filosofia**: un conjunt de valors i principis (iterar, lliurar incrementalment, rebre feedback, respondre al canvi per sobre de seguir un pla). Diu **per què** i **cap on**, mai **com**.
> - **Scrum** és un **framework àgil concret**: un receptari tancat de **rols, esdeveniments i artefactes** que et diu **com** treballar dia a dia (sprints time-boxed, 3 rols, daily, review, retro...).
> - **Relació**: Scrum és **a dins** d'Agile — n'és una **implementació**, com ho són XP o Kanban. **No es tria entre una o l'altra**: fer Scrum **és** ser àgil d'una manera concreta. Més que una especialització, és una **concreció** de la filosofia.
>
> **Per què fer servir un o l'altra?**
> - No pots "fer servir Agile sol": et queda una **bona intenció sense pràctiques** — ningú et diu què fer dilluns al matí.
> - Per això es treballen en **dues capes**: (1) adoptes la **mentalitat àgil**, (2) et dones d'alta en un **framework** per executar-la.
> - **Scrum** quan vols **estructura i ritme**: rols definits, iteracions fixes, cerimònies regulars.
> - **Un altre àgil** (ex. [[Kanban]] properament) quan vols **flux continu** sense sprints.
>
> **Resum examen**: *Agile = filosofia (el perquè) · Scrum = un dels frameworks que la fan realitat (el com).* Un sense l'altre no funciona: Scrum sense mentalitat àgil = fer els ritus buits; mentalitat àgil sense Scrum = intenció sense mètode.

**Referència: Diapositiva 2** — el PDF només diu *"Scrum is an agile methodology"*; la comparació ampliada és **marc general**, no surt al PDF.

## Sprints

- **Curts**: màxim 1 mes, un rere l'altra **sense pauses**.
- **Time-boxed**: acaben en una data concreta, **sense extensions**.
- Cada sprint es centra en els requisits del client d'una **llista prioritzada**.
- L'equip es **compromet** a completar els elements abans del final del sprint.
- Durant el sprint, els elements triats **no canvien**.
- Cada dia l'equip es reuneix breument per inspeccionar el progrés i ajustar els següents passos.
- Al final del sprint, **Sprint Review** amb els stakeholders: es demostra el que s'ha construït.
- El feedback obtingut s'incorpora al **següent** sprint.

> [!warning] La durada del sprint **mai s'allarga**, passi el que passi.

**Referència: Diapositiva 4** → nota atòmica: [[Sprint]]

## Rols de Scrum

| Rol | Objectiu | Com ho fa | Observacions clau |
|---|---|---|---|
| **Product Owner** (stakeholder) | Maximitzar el **ROI** identificant features del producte | Converteix els objectius en una **llista prioritzada**; decideix què va a dalt per al proper sprint i re-prioritza i refina contínuament la llista | **Un i només una persona** serveix de PO, i és responsable del **valor** del treball |
| **Team** | Lliurar el producte potencialment lliurable cada sprint | L'equip decideix **què es compromet** i com ho aconsegueix millor | **Cross-functional** (anàlisi, disseny, codi, test, documentació) i **self-organizing** amb molta autonomia i responsabilitat. Mida: **7 ± 2 persones** |
| **ScrumMaster** | Ajudar l'equip i la PO a tenir èxit | **Facilita el procés**, donant suport a l'equip mentre s'organitza i es gestiona; pot pressionar la PO | **No és el manager de l'equip ni un project manager**: no diu què fer, com fer-ho ni assigna tasques. **ScrumMaster i PO no poden ser la mateixa persona** |

> [!warning] Truc d'examen: el ScrumMaster **no mana, facilita**. No hi ha cap d'equip a Scrum.

**Referència: Diapositives 5-7** → nota atòmica: [[Scrum Roles]]

## Pas 1: Product Backlog

Primer pas: la **Product Vision** de la Product Owner, que evoluciona cap a una llista refinada i prioritzada de features: el **Product Backlog**.

Característiques:

- Existeix i **evoluciona** al llarg de tota la vida del producte; és la **road map** del producte.
- En qualsevol punt és la visió **única i definitiva** de "tot el que l'equip podria arribar a fer mai, per ordre de prioritat".
- **Només existeix un** Product Backlog.

Què inclou — **4 tipus d'item que no s'han de confondre**:

| Tipus | Què és | Exemple del PDF |
|---|---|---|
| **Feature de client** | Capacitat **nova** per a l'usuari | "enable all users to place book in shopping cart" |
| **Millora d'enginyeria** | Algo **existent** que es reforça o reescriu perquè vagi millor (escalabilitat...); cap funció nova | "rework the transaction processing module to make it scalable" |
| **Feina exploradora / recerca** | Encara **no se sap com** fer-ho: investigar abans de decidir — **incertesa**, no codi | "investigate solutions for speeding up credit card validation" |
| **Defecte conegut** | Algo existent que **no funciona com hauria** | "diagnose and fix the order processing script errors" |

> [!warning] Diferències clau: millora = *funciona però millorable* · defecte = *trencat* · exploració = *no se sap com* (dóna informació, no funció) · feature = *nou per a l'usuari*. Detall a [[Product Backlog]].

- **Release Backlog** = subconjunt del Product Backlog destinat a l'alliberament actual; en general és el focus principal de la PO.

A la pràctica, cada item de la taula porta: detalls (wiki), **prioritat**, estimació de **valor** i estimació d'**esforç** (ex. valor 7 / esforç 5 per a "As a buyer I want to place orders").

**Referència: Diapositives 8-11** → nota atòmica: [[Product Backlog]]

## Pas 2: Sprint Planning

### Part 1

**Actors**: Product Owner, Team i Scrum Master.

1. Revisar els elements d'**alta prioritat** que la PO vol implementar.
2. Discutir els objectius i revisar la **Definition of Done** (normalment: codi als estàndards, revisat, implementat amb desenvolupament dirigit per **tests unitaris**, testejat amb **100% d'automatització** de tests, i documentat).

### Part 2

**Actors**: només el Team.

1. L'equip **selecciona** els items del Product Backlog que es compromet a acabar, començant **per dalt** de la llista.
2. Planificació detallada de tasques per implementar els items que l'equip decideix prendre.
3. L'equip decideix **quant treball es compromet** a completar, en lloc que se li assigni.

Pasos de la Part 2:

1. **Determinar capacitat**: durada del sprint (ex. 2 setmanes = 8 dies laborables) × hores disponibles de cada membre (ex. Isabel 8 dies × 4 h = 32 h · Hind 6 × 6 = 36 h · Alex 10 × 3 = 30 h · Mustafa 4 × 8 = 32 h). Les hores **no inclouen** reunions, temps de cafè, vacances, etc.
2. **Descobrir quants items caben**: discussion de disseny a la pissarra negra i, un cop entès el disseny, l'equip **descomposa** els items en tasques individuals registrades al **Sprint Backlog** (item → tasques → voluntari → hores estimades).
3. Seguiment amb post-its: **"Not Yet Started"**, **"In progress"**, **"Completed"**.

**Referència: Diapositives 12-16**

## Durant el Sprint

### Daily Scrum

- **5-15 minuts**, cada dia a l'hora convinguda.
- **Tothom assisteix**, sense excepcions.
- Reunió **dempeus** (standing meeting).
- Cada membre informa de **tres coses** (només tres):
  1. Què s'ha fet des de l'última reunió.
  2. Què planeja fer fins a la propera reunió.
  3. Quin impediment o bloqueig hi ha al mig.

> [!note] No és un reporting: com no hi ha cap d'equip, és un pas de **sincronització**. A la daily **no es discuteix** ni es passa cap altra informació. El que s'hagi de resoldre, queda per a una reunió a part després (aquesta segona reunió **no és obligatòria** per a la resta de l'equip, i pot ser necessària per adaptar-se a les novetats de la daily).

**Referència: Diapositives 17-18** → nota atòmica: [[Daily Scrum]]

### Actualització del Sprint Backlog i burndown

- Cada dia s'actualitza el Sprint Backlog amb les **hores restants** estimades per tasca (ex. columnes Day 1, Day 2, Day 3...).
- Si l'esforç de cada dia es plotja en un graf, tenim el **Sprint Burndown Chart**.

> [!tip] El burndown ideal és un graf que **baixa** cap a "zero esforç restant". **No mostra quant temps ha gastat l'equip, sinó quant queda per gastar.** Es fa amb paper i bolígraf.

**Referència: Diapositives 19-20** → nota atòmica: [[Burndown Chart]]

## Finalització del Sprint

**REGLA: la durada mai s'allarga.**

Això vol dir que els **primers sprints** l'equip falla els compromisos. Després **sobre-compensa** seleccionant molts menys items (i llavors sí que pot demanar més items al Product Owner).

### Sprint Review

- **Jugadors**: Product Owner, ScrumMaster i team.
- **Objectiu**: semblant a una "demo", però la idea és **inspect and adapt**. Conversa entre la PO i l'equip; el ScrumMaster s'assegura que tothom coneix la **Definition of Done**.
- Els elements **no fets correctament tornen al Product Backlog**.

### Sprint Retrospective

- **Jugadors**: ScrumMaster i team.
- **Objectiu**: inspeccionar i adaptar el **procés**.
- Documenta què funciona bé i què podria funcionar millor. Es posen d'acord en les **causes** i es proposen **canvis**.

> [!tip] **Review = producte** (el que s'ha construït) · **Retrospective = procés** (com s'ha treballat). És el parell que més es confon a l'examen.

**Referència: Diapositives 21-23**

## La nova Sprint

- L'agregació de tot l'esforç del **Release Backlog** permet crear el **Release Burndown Chart**.
- "Everything is completely **finished** every Sprint": codi, tests, documentació... tot.

**Referència: Diapositives 24-25**

## FITXA de repàs

| Element | Què és | Regla clau |
|---|---|---|
| **Sprint** | Iteració ≤ 1 mes, time-boxed | La durada **mai s'allarga** |
| **Product Backlog** | Llista única prioritzada de tot el que es pot fer | En existeix **un de sol**; la PO el reprioritza |
| **Sprint Backlog** | Descomposició en tasques dels items del sprint | L'equip decideix quant agafa, **no se li assigna** |
| **Daily Scrum** | Reunió diària 5-15 min, dempeus | **3 preguntes**; sincronització, no debat |
| **Definition of Done** | Criteris per donar un element per acabat | Es revisa a Planning 1, es vigila a la Review |
| **Sprint Review** | Demo + inspect&adapt amb la PO | Els mal fets **tornen al backlog** |
| **Sprint Retrospective** | Inspect&adapt del **procés** | Sense la PO: només ScrumMaster + team |
| **Burndown** | Graf de l'esforç **restant** per dia | Mostra quant **queda**, no quant s'ha gastat |
| **ScrumMaster** | Facilita el procés | **No és manager**; no pot ser també la PO |

## Dubtes / a revisar

- Taula de capacitat: **Alex té 10 dies disponibles** en un sprint de **8 dies laborables** — incoherent; preguntar a classe.
- El PDF diu **"four pillars"** (sprint planning, stand ups, sprints, retrospectives) però més endavant treballa també la **Sprint Review** — comprovar si l'examen segueix la llista de 4 o en compta 5.
- Connectar amb l'**avaluació** de la [[Intro]] (0,25 × Sessions de Planning): què s'espera de nosaltres en una session de planning real.

---
[[_Index_ES]] · [[Intro]]
