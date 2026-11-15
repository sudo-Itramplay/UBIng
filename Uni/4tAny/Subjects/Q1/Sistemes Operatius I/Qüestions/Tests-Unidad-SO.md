---
id: Tests-Unidad-SO
aliases: []
tags:
  - tipus/parcial
  - assignatura/SO
assignatura: SO
data: "2026-10-24"
---

# Tests d'unitat — Sistemes Operatius I

Els **tests d'unitat** de l'assignatura: 15:15-15:30, al **Campus Virtual**, un per bloc. Les preguntes es mantenen en **l'original** (castellà); les respostes són **deduïdes dels PDFs i les notes** — no venen marcades a les diapositives, així que si el professor en corrigeix alguna, actualitza-ho aquí.

---

## Calendari

| # | Test | Setmana | Què cobreix | Diapositives del correcció | Estat |
|---|---|---|---|---|---|
| 1 | Test seguridad SO | 3 (28 Sep - 4 Oct) | T1 — Introducció seguretat | PDF 02 P1, D5-10 | **Fet** |
| 2 | Test MV y virtualización | 5 (12-18 Oct) | T2 — MV + T2b — Contenedors | PDF 03 P1, D6-11 | **Fet** |
| 3 | **Test Sistema de ficheros** | 6 (19-25 Oct) | T3-P1 + T3-P2 | — | **PRÒXIM** |
| 4 | Test concurrencia 1 | 11 (23-29 Nov) | Concurrència amb espera activa + semàforos | — | — |
| 5 | Test concurrencia 2 | 14 (14-20 Des) | Monitores + repàs | — | — |

> [!tip] Patró del professor
> Cada sessió de teoria **comença** repassant el test del bloc anterior. Per tant el **test 3** sortirà dels conceptes de **T3-P1 i T3-P2**, i el correcció es veurà a la sessió de la **setmana 7** (junt amb el repàs del parcial).

---

## Test 1 — Seguretat en SOs (setmana 3) ✅

**Referència: PDF 02 Parte 1, D5-10.** Respostes amb més detall a [[Qüestions-T1-Seguretat|Qüestions T1 — Seguretat]].

> [!question]- P1 · En un sistema con Access Control Lists (ACL), ¿qué ventaja se obtiene respecto al modelo clásico de permisos (rwx)?
> **b) Control más granular sobre usuarios específicos.** (a) és fals: les ACL fan *més* comprovacions, no més ràpides. (c) és fals: els grups **continuen existint**, l'ACL hi s'afegeix. (c→d) és fals: cap mecanisme de permisos de fitxer dona accés a *kernel mode*
> *(Respon-te a tu mateix: per què l'opció no pot ser "eliminació de los permisos de grupo"?)*

> [!question]- P2 · ¿Cuál de los siguientes escenarios es un ejemplo típico de vulnerabilidad de tipo buffer overflow?
> **a) Escritura fuera de los límites de un array.** (b) és *stack exhaustion*, no overflow de buffer. (c) és un problema de **concurrença**, no de memòria. (d) és xarxa

> [!question]- P3 · ¿Qué técnica intenta proteger la pila de ejecución insertando valores de control entre el búfer y la dirección de retorno?
> **c) Canarios (pío-pío).** ASLR (a) i DEP (b) no insereixen res entre el buffer i l'adreça de retorn; PIE (d) afecta la càrrega de l'executable

> [!question]- P4 · ¿Qué opción de compilación hace que un ejecutable se cargue en direcciones aleatorias cada vez que se ejecuta?
> **c) -pie.** -no-pie (a) fa el contrari; -z execstack (b) fa la pila **executable** (elimina DEP); -O2 (d) és optimització

> [!question]- P5 · Identifica la afirmación INCORRECTA sobre mecanismos de protección ante buffer overflow.
> **d) PIE desactiva las comprobaciones de límites de los buffers.** És fals: PIE només canvia la **ubicació** de càrrega. ASLR (a), DEP (b) i canaris (c) són **vertaders**

> [!question]- P6 · ¿Cuál de las siguientes acciones reduce el riesgo de vulnerabilidades por buffer overflow?
> **c) Usar funciones como fgets() o strncpy().** (a) i (b) són les **causes** del problema; (d) desactiva una protecció

---

## Test 2 — MV i virtualització (setmana 5) ✅

**Referència: PDF 03 Parte 1, D6-11.** També a [[T3-Sistemes-Fichers-P1#1. Test ràpid del bloc anterior (MV / contenidors)|T3-P1 §1]].

> [!question]- P1 · ¿Cuál de las siguientes afirmaciones describe mejor una máquina virtual?
> **b) Un sistema que emula hardware para ejecutar SOs invitados.** (a) és un compilador; (c) descriu més el paper de l'hipervisor sobre **crides al SO**, no la MV; (d) és un **contenedor**, no una MV

> [!question]- P2 · ¿Qué componente de una máquina virtual se encarga de asignar y gestionar los recursos físicos del host?
> **b) Hypervisor o Virtual Machine Manager (VMM).** El SO *guest* (a) gestiona el seu entorn virtual; Docker Engine (d) és de contenidors

> [!question]- P3 · En el contexto de virtualización, el mecanismo "trap-and-emulate" consiste en:
> **a) Interceptar instrucciones privilegiadas y ejecutarlas en el hipervisor.** Les instruccions privilegiades del guest provoquen una *trap*; l'hipervisor les emula i retorna el resultat. (b) és traducció de codi, (c) és memòria compartida, (d) són senyals del SO

> [!question]- P4 · Identifica la afirmación incorrecta sobre los contenedores:
> **c) Simulan hardware completo.** És fals: els contenidors **comparteixen el kernel** del SO host. (a), (b) i (d) són **vertaders**

> [!question]- P5 · ¿Qué ventaja principal ofrecen los contenedores frente a las máquinas virtuales en desarrollo de software?
> **b) Arranque más rápido y menor consumo de recursos.** (a) i (d) són avantatges de les **MVs** (el contenidor **no** pot executar kernels diferents); (c) no aplica

> [!question]- P6 · ¿Qué diferencia existe entre docker image y docker container?
> **d) La imagen es la plantilla; el contenedor es su instancia en ejecució.** (Directament de les definicions de la T2b)

> [!tip] Preguntes obertes del mateix bloc (no test, però les va deixar)
> **P1** Cas Héctor/María: tres escenarios possibles (María instal·la Python 2.7 / María instal·la MV + Python 2.7 / Héctor crea un contenedor). Veure [[T2b-Contenedors-Docker#2. Cas Héctor / María (P1)|T2b §2]]
> **P6** Enumera 3 gestors de contenedors (Docker, rkt, CRI-O, LXC/LXD)
> **P9** Què és Kubernetes i què aporta a Docker → [[T2b-Contenedors-Docker#13. Kubernetes|T2b §13]]

---

## Test 3 — Sistemes de ficheros (setmana 6) ✅

**Hi ha un banc de preguntes complet del Tema 3 a [[Qüestions-T3-Fitxers|Qüestions T3 — Fitxers]] (P1-P18), amb les respostes i el per què de les opcions equivocades.** El que segueix és el resum de conceptes i les preguntes que el professor va deixar als PDFs.

Referència: PDF 03 P1 + P2. Veure [[T3-Sistemes-Fichers-P1]] i [[T3-Sistemes-Fichers-P2]].

### Conceptes que cauen segur

| Concepte | On | La pregunta que se'n deriva |
|---|---|---|
| Fitxer vs directori vs *archivo* | [[T3-Sistemes-Fichers-P1#3. Ficheros: abstracció del SO\|T3-P1 §3]] | El directori **conté les dades** dels fitxers? |
| Sector vs bloc | [[T3-Sistemes-Fichers-P1#Sector vs bloc\|T3-P1 §5]] | Quin és la unitat del disc i quin la del SO? |
| HDD vs SSD | [[T3-Sistemes-Fichers-P1#5. Dispositius d'emmagatzematge\|T3-P1 §5]] | Per què el contigu és 10x més ràpid? Què fa el wear leveling? |
| Truncar vs esborrar | [[T3-Sistemes-Fichers-P1#8. Operacions sobre fitxers i directoris\|T3-P1 §8]] | Esborrar **llibera** l'espai, truncar **no**? |
| FAT = llista enlazada | [[T3-Sistemes-Fichers-P1#12. El sistema FAT en detall\|T3-P1 §12]] | Per què l'accés aleatori és **pobre**? |
| FFS = vectors | [[T3-Sistemes-Fichers-P2#4. Sistemes FFS (Unix Fast File System) (D7-9)\|T3-P2 §4]] | Què ha canviat respecte a la FAT? |
| I-node | [[T3-Sistemes-Fichers-P2#6. I-nodes (D12-14)\|T3-P2 §6]] | Quant i-nodes per quina quantitat de disc? Què guarda? |
| 15 punterers | [[T3-Sistemes-Fichers-P2#7. Punterers: com serveix un i-node per a mides diferents? (D15-19)\|T3-P2 §7]] | Com pot servir un fitxer de 4 GB? |
| Bitmap vs FAT (espai lliure) | [[T3-Sistemes-Fichers-P2#11. Espai lliure al FFS: bitmap (D25)\|T3-P2 §11]] | Com busca espai lliure cadascun? |
| Heurística de localitat | [[T3-Sistemes-Fichers-P2#12. Heurística de localitat al FFS (D26)\|T3-P2 §12]] | Per què agrupar el directori i els seus fitxers? |
| Journaling / COW | [[T3-Sistemes-Fichers-P2#14. Millores als sistemes FFS (D28)\|T3-P2 §14]] | Quin és l'objectiu de cadascun? |
| MBR | [[T3-Sistemes-Fichers-P1#14. Arrencada: MBR\|T3-P1 §14]] | Què conté? |

### Preguntes ràpides que el professor va deixar als PDFs

> [!question]- Per què "Fast" File System? Què hi té a veure la localitat?
> Cada salt del braç té **cost mecànic**. Blocs **contigus** → menys *seek* → més ràpid. Veure [[T3-Sistemes-Fichers-P2#4. Sistemes FFS (Unix Fast File System) (D7-9)|T3-P2 §4]]

> [!question]- Per què l'arbre de punterers de l'i-node és **asimètric**?
> Perquè els primers 48 KB es resolen amb **0 indireccions**, els següents amb 1, després 2 i 3. Un fitxer petit **no paga** la cadena llarga. Veure [[T3-Sistemes-Fichers-P2#7. Punterers: com serveix un i-node per a mides diferents? (D15-19)|T3-P2 §7]]

> [!question]- I la FAT com buscava espai lliure? Quina diferència amb el bitmap del FFS?
> La FAT **recorria la taula** buscant un element no ocupat → molta fragmentació. El FFS té un **bitmap dedicat**: en una lectura es veu l'estat de tots els blocs. Veure [[T3-Sistemes-Fichers-P2#11. Espai lliure al FFS: bitmap (D25)|T3-P2 §11]]

> [!question]- Journaling vs COW: quin objectiu cadascun?
> **Journaling** = consistència dels metadades davant d'**avaria/tall**. **COW** = conserva **versions anteriors** (còpies de seguretat) perquè mai no sobreescriu. Veure [[T3-Sistemes-Fichers-P2#14. Millores als sistemes FFS (D28)|T3-P2 §14]]

> [!question]- Oberta del PPT: què passa amb un SSD si no rep alimentació durant un temps?
> **El professor no hi va donar resposta escrita** — confirmar a classe (retenció de càrrega de les cel·les NAND)

### Exercici que va anunciar

> "Luego haremos un ejercicio en la máquina virtual…" (PDF 03 P1, D3). Si es fa, recollir-lo aquí i a [[T3-Sistemes-Fichers-P1#7. Exercici: quant ocupa realment un fitxer?|T3-P1 §7]].

### Bona pràctica: el Problema 1 del parcial

Tot el **Problema 1** del parcial 2025-2026 és pur **sistemes de fitxers** (mida en blocs, FFS, FAT, SSD, MBR). El tens a [[T3-Sistemes-Fichers-P2#17. Examen parcial 2025-2026 (D41-44)|T3-P2 §17]] — és el millor simulacre del test 3.

---

## Test 4 — Concurrencia 1 (setmana 11)

**Encara no hi ha material** (tema 4, es veu a partir de la setmana 7). Quan hi sigui, afegir aquí.

Cobertura prevista segons el pla: **introducció a la concurrència, paradigmes de programació concurrent, espera activa**.

---

## Test 5 — Concurrencia 2 (setmana 14)

**Encara no hi ha material.** Cobertura prevista: **semàforos, monitores** + repàs general.

---

## Enllaços relacionats

- [[_Index_SO|Índex Sistemes Operatius I]]
- [[T1-Introduccio-Seguretat-SO|T1 — Introducció Seguretat SO]]
- [[T2-Maquines-Virtualitzacio-SO|T2 — MV i virtualització]]
- [[T2b-Contenedors-Docker|T2b — Contenedors i Docker]]
- [[T2c-Comparativa-SO-MV-Contenidor|T2c — SO, MV i contenidor]]
- [[T3-Sistemes-Fichers-P1|T3 — Sistemes de fitxers (Parte 1)]]
- [[T3-Sistemes-Fichers-P2|T3 — Sistemes de fitxers (Parte 2)]]
