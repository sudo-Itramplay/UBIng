---
id: Respostes-Parcial1-SO2-26-27
aliases:
  - Respostes Parcial 1 SO2
tags:
  - tipus/parcial
  - assignatura/SO
assignatura: SO
data: "2026-10-30"
---

# Respostes — Parcial 1 SO2 (2026-10-30)

**Enunciat:** [[Parcial/Examen/parcial1_SO2_26-27_Released.pdf|parcial1_SO2_26-27_Released.pdf]] (3 problemes, 10 punts)

> [!warning] Enunciat **parcialment ocult**
> A la versió publicada hi ha els apartats **XXXXX**: els **a) i b) de tots els problemes** i l'**e) del Problema 3**. Sónt els **5 punts** que el professor publica el mateix dia de l'examen (9:00).
> Per tant: **c), d), e) de P1 · c), d), e), f) de P2 · c), d) de P3** tenen l'enunciat publicat i es responen un a un. La resta s'ha **deduït del codi i de les preguntes del curs** → estan marcats amb ⚠️ i la resposta és la que es creu que sortirà.

**Tot el contingut d'aquesta nota ve del material de classe**: [[T1-Introduccio-Seguretat-SO]], [[T2-Maquines-Virtualitzacio-SO]], [[T2b-Contenedors-Docker]], [[T2c-Comparativa-SO-MV-Contenidor]], [[T3-Sistemes-Fichers-P1]], [[T3-Sistemes-Fichers-P2]] i els PDFs 01, 02 i 03.

---

## 0. Fitxa de dades (per no oblidar-les)

| Dada | Valor |
|---|---|
| Buffer de P1 | `char usuario[16]` → 16 bytes a la **pila**; `sizeof usuario` = **16** |
| P1 | check `strlen(nombre) >= 16` → s'accepta longitud **≤ 15** → `strcpy` escriu **≤ 16 bytes** (15 + `'\0'`) |
| P2 | `n = candidatos × 100000` elements; `n × 8` bytes → argument **50** ⇒ 5.000.000 doubles = **40.000.000 B (≈38,1 MiB)**; màxim (100) = 80.000.000 B |
| P2 | `sizeof(costes)` = `sizeof(double*)` = **8** = `sizeof(double)` → **funciona per casualitat** (64 bits) |
| P2 | Sortida: `Coste medio: 49.95` (patró 0,0 … 99,9 repetit; mitjana 49,95) |
| P2 d) | 4 × 512 MiB = 2048 MiB = **2 GiB** = exactament la RAM → **afirmació FALSA** |
| P3 | `inicio = 11×4096 + 3072` = **48.128 B**; lectura = 3072 × 2 = **6144 B**; final 54.272 B < 100.000 B |
| P3 | blocs lògics tocats: **11, 12 i 13** (bloc 11 a offset 3072 dins del bloc) |
| P3 c) | lectures de bloc = 1 (indirecte) + 3 (dades) = **4** |
| P3 d) | FAT: **11 salts** de cadena (bloc lògic 0 → 11) |

---

# Problema 1 — Seguretat en SOs (3,0 punts)

> *Vulnerabilitats al intèrpret PHP → execució de codi amb els permisos del procés servidor. Codi: `preparar_peticion()` amb `char usuario[16]`. El servidor és Linux i el compte de servei **no** és root.*

## a) Anàlisi del codi ⚠️ (enunciat ocult)

**Teoria del Tema 1 que has de tenir a mà (T1 §9-10):**

| Concepte | Clau |
|---|---|
| **Buffer overflow** | Un programa **sobreescriu** la memòria d'un buffer superant-ne la mida |
| **Pila** | De dalt a baix: **adreça de retorn** → **EBP** → **espai del buffer**. Un overflow pot sobreescriure l'**adreça de retorn** → control del flux d'execució |
| **Conseqüències** | Corrupció de dades · execució de codi maliciós · elevació de privilegis · DoS · fuga d'informació · compromís del sistema |
| **Tipus** | **Stack overflow** (pila de crides) · **Heap overflow** (memòria dinàmica) |
| **Defenses** | **Canari** (valor aleatori al stack → "stack smashing detected" i abort) · **ASLR** (aleatoritza pila, heap i biblioteques) · **DEP** (pila/heap **no executables**) · **PIE** (executable carregat en adreces diferents) · **limitació de longitud** · **funcions segures** (`fgets`, `strncpy`) · **actualitzacions** |
| **Funcions segures** | `fgets()` en lloc de `gets()`, `strncpy()` en lloc de `strcpy()` |
| **Compilació** | `-fstack-protector` (canari, default a Linux) · `-pie` / `-fPIE` · ASLR + DEP + PIE = les tres proteccions més importants |
| **Principis** | **Defensa multinivel** · **Menor privilegi** · **Separació de privilegis** · **Denegar per defecte** |
| **CVE** | Estàndard públic per identificar i catalogar vulnerabilitats |

**El codi NO té buffer overflow.** És la conclusió que cal demostrar amb números, no de probabilitat:

1. `char usuario[16]` → 16 bytes, i `sizeof usuario` = **16** (és un *array*, no un punter → `sizeof` dona la mida de l'array).
2. La condició `strlen(nombre) >= sizeof usuario` rebutja **qualsevol longitud ≥ 16**. Per tant el que arriba a `strcpy` té longitud **≤ 15**.
3. `strcpy` copia els 15 caràcters **+ el `'\0'`** → com a màxim **16 bytes** → **omple el buffer exactament, no el desborda**.
   - El `>=` (i no `>`) és el que evita el *off-by-one*: amb `>` passaria una cadena de 16 caràcters → 17 bytes → 1 byte de desbordament.
   - I la hipòtesi del enunciat ("el contingut no canvia durant l'execució") és la que fa **vàlida** la comprovació: no hi ha *TOCTOU*, la longitud mesurada és la que es copia.

**Ara bé, el patró és fràgil i el risc real continua hi sent:**

| Observació | Per què importa |
|---|---|
| `strcpy` és una **funció insegura** | La seguretat depèn **d'una comprovació manual**; en qualsevol altra versió/funció, si la comprovació falta, el desbordament torna. Solució: `strncpy`/`snprintf` (T1 §10, *Funcions segures*) |
| És una **defensa d'una sola capa** (aplicació) | Principi de **defensa multinivel**: la vulnerabilitat real estava al **intèrpret PHP en C**, i es disparava **abans** de que s'executés el codi de l'aplicació → aquesta funció **no hauria protegit res** |
| El buffer és a la **pila** | Un desbordament aquí sobreescriu EBP i **adreça de retorn** → control del flux d'execució → execució de codi amb els permisos del procés servidor (exactament el que diu el enunciat) |

**Què hauria passat sense la comprovació** (o amb `>`): desbordament de buffer → corrupció de dades, execució de codi maliciós, elevació de privilegis, DoS, fuga d'informació, compromís del sistema (T1 §9).

**Defenses de classe que ho haurien frenat** (T1 §10): **canari** (*stack smashing detected*), **ASLR**, **DEP** (pila no executable), **PIE**, comprovació de longitud i funcions segures.

## b) Correcions i defenses ⚠️ (enunciat ocult)

**1. Corregir el codi (no dependre d'una comprovació manual):**

```c
int preparar_peticion(const char *nombre)
{
    char usuario[16];
    if (nombre == NULL) return -1;
    int n = snprintf(usuario, sizeof usuario, "%s", nombre);
    if (n < 0 || (size_t)n >= sizeof usuario) return -1;   /* no hi ha truncament */
    printf("Peticion preparada para %s\n", usuario);
    return 0;
}
```

Alternativa clàssica de classe: `strncpy(usuario, nombre, sizeof usuario - 1); usuario[sizeof usuario - 1] = '\0';` (recordant que `strncpy` **no** posa el `'\0'` si la font és llarga).

**2. Compilar el servidor amb les proteccions (T1 §10 i Qüestions T1):**
`-fstack-protector` (canari, default a Linux) · `-pie` (PIE) · `-fPIE` · `-D_FORTIFY_SOURCE=2` · ASLR i DEP actius al sistema.

**3. Defensa multinivel (T1 §19-24) — capes:**
- **Aplicació**: validació de longitud i funcions segures (el codi corregit).
- **Procés**: el compte de servei sense privilegis i amb els seus **propis** fitxers.
- **SO i hardware**: pila no executable (DEP), ASLR+PIE, canari, actualitzacions del paquet (parche de PHP).
- **Operació**: WAF, segmentació de la xarxa, còpies de seguretat, resposta davant l'incident.

**4. El que de veritat hagués corregit l'incident:** actualitzar l'intèrpret PHP (parche del CVE) i compilar-lo amb les proteccions; el codi de l'aplicació era secundari perquè la vulnerabilitat s'executava **abans**.

## c) «Com que no s'executa com a root, un atacant no podrà causar danys importants»

**L'afirmació és FALSA** (o, com a molt, una mitigació parcial, no una garantia):

- **No ser root és una bona pràctica** (menor privilegi), pero **no és suficient**: el compte de servei ja tenia permís de **llegir els materials docents** i de **modificar els fitxers de les qualificacions**. Amb només això ja es trenquen els tres objectius de la **CIA**:
  - **Confidencialitat**: filtració de materials docents i de notes.
  - **Integritat**: manipulació de les qualificacions.
  - **Disponibilitat**: el servei es pot deixar penjat (DoS) o esborrar material.
- **Es va validar amb root?** Cap: amb `root` l'atacant hauria tingut el control **total** del sistema. Però "menys mal" ≠ "sense mal".

**Separació d'usuaris i permisos proposada** (principis de la **menor privilegi** i la **separació de privilegis**, T1 §25-28):

| Compte | Propietari de | Permisos | Idea |
|---|---|---|---|
| `campus-web` | codi de l'aplicació, `sessions/`, `tmp/` | `r-x` al codi, `rwx` a `sessions/` i `tmp/` | El servei web **no ha de poder** llegir els materials docents ni escriure les notes → se li **treuen** aquests permisos |
| `campus-materials` | materials docents | `r--` per al servei web (o millor: **cap** permisos) | Els materials només els ha de poder llegir qui els publica |
| `campus-grades` | fitxers de qualificacions | `rw-` **només** per al propietari del procés de notes; el servei web només `r--` | Que el servei **llegeixi** les notes però **no les pugui modificar** |

Concretament, amb ACL (T1 §7 i l'apartat d):

```bash
# 1) compte separat per al servei, sense cap grup extra
# 2) notes: propietari = campus-grades, al servei web només lectura
chown campus-grades:notas  notas.csv
chmod 640 notas.csv
setfacl -m m::r--  notas.csv          # obre el sostre (sostre de la màscara)
setfacl -m u:campus-web:r-- notas.csv # el servei web llegeix, no escriu
```

**Principis aplicats:**
- **Menor privilegi** (T1 §25-26): el servei accedeix **només** al que necessita.
- **Separació de privilegis** (T1 §27-28): el sistema es divideix en components amb accés limitat → un comprometiment no es propaga.
- **Defensa multinivel** (T1 §19-24) i **disseny de controls: denegar per defecte** (T1 §7) → el que no cal, no es concedeix.

## d) ACL: què són i què expressen que l'rwx no pot

**Definició:** una **llista de control d'accés** és, per a cada fitxer, una **llista d'entrades**; cada entrada és un **subjecte** (un usuari concret o un grup) + uns **permisos** (`rwx`), i el sistema concedeix el que la llista diu.

**Clau de classe:** **rwx i ACL són el mateix sistema.** `chmod 640` crea una ACL de **3 entrades** (`user::`, `group::`, `other::`); el **rwx és el nom que donem a les tres primeres**, i l'ACL és la **llista completa**, que en pot tenir moltes més. L'ACL **no substitueix** els permisos de grup: **s'hi afegeix per sobre**. Amb ACL estesa hi ha una **màscara** (sostre) que limita `user:x:`, `group::` i `group:x:` — però **no** `user::` ni `other::`.

**Què expressa que l'rwx no pot:**

| Model UNIX | ACL |
|---|---|
| Només **3 categories**: propietari, grup, resta | Una entrada **per usuari concret** i **per grup concret**, tantes com calgui |
| Per donar accés a l'Alice caldria posar-la **al grup** del propietari (i rebrà **tots** els permisos del grup) o obrir la lectura a **"resta"** (és a dir, a tot el món) | `user:alice:rwx` → l'Alice té permisos **exactament** indicats, sense tocar el grup ni la resta |
| Una sola categoria "grup" | **Grups diferents amb permisos diferents** (`group:professors:rw`, `group:estudiants:r`) |

**Exemple aplicat al Campus Virtual:**

```bash
# El fitxer de notes el té el procés de notes; el servei web només el llegeix
setfacl -m u:campus-web:r-- notas.csv
setfacl -m m::r--     notas.csv     # el sostre: l'efectiu de l'ACL = entrada AND màscara
getfacl notas.csv
```

```
user::rw-        # propietari (campus-grades): no passa per la màscara
group::r--       # grup: passa per la màscara
other::---       # resta: sense accés
user:campus-web:r--  # el servei web: efectiu = r-- AND màscara = r--
mask::r--        # el sostre (ls -l el mostra amb un "+")
```

Amb l'rwx tradicional **no es pot expressar**: posar `campus-web` al grup del propietari li donaria els permisos **del grup** (incloent-hi l'escriptura, si el grup en té), i obrir la lectura a "resta" la donaria a **tot el món**. L'ACL és el que permet "**aquest** servei en concret: només lectura" — que és exactament el que fa falta per separar **confidencialitat i integritat** de les notes.

*(NFSv4 ACL és més potent: entrades `allow`/`deny` explícites i herència des del directori. La POSIX ACL de Linux només té entrades allow + màscara.)*

### Exemple concret (sortida real, executada)

**Pas 1 — `chmod 640 notas.csv` → ACL MÍNIMA (3 entrades), cap màscara:**

```
user::  rw        # propietari
group:: r         # grup
other::           # resta
```
```
$ ls -l notas.csv
-rw-r-----  1 itram itram  15 ... notas.csv     ← sense "+"
```

**Pas 2 — `setfacl -m u:itram:rwx notas.csv` → l'ACL s'allarga i apareix la MÀSCARA:**

```
user::rw
user:itram:rwx        # ← l'entrada nova: un USUARI concret
group::r
group:docker:r        # ← un GRUP concret
mask::r               # ← el sostre (NO hi era abans)
other::
```
```
$ ls -l notas.csv
-rw-r-----+  1 itram itram  15 ... notas.csv
     ^^^^^^^  el camp "grup" mostra la MÀSCARA, no el grup::  i el "+" avisa que hi ha ACL estesa
```
⚠️ En aquest punt `getfacl` marca **`#effective:r--`** a l'usuari: la seva entrada diu `rwx`, però la màscara `r--` la retalla → **efectiu = entrada AND màscara = `r--`**. L'Alice encara **no** pot escriure.

**Pas 3 — `setfacl -m m::rw- notas.csv` → s'obre el sostre i l'Alice ja escriu:**

```
mask::rw
```
```
$ ls -l notas.csv
-rw-rw----+  1 itram itram  15 ... notas.csv     ← la màscara ha canviat de r-- a rw-
```

**Pas 4 — `chmod g-w` NO toca `group::`: escriu la MÀSCARA.**

Després de `chmod g-w` el `group::` **segueix sent `r--`** i el que canvia és `mask::rw` → `mask::r--` (torna a `-rw-r-----+`). Per això l'Alice torna a quedar limiteda, i el `chmod` de tota la vida continua "funcionant" sobre una ACL estesa.

**Regla deuat per a l'examen:**
> `chmod g` escriu la **màscara**; `ls -l` mostra la **màscara**; la màscara **no** toca `user::` ni `other::`.

### Què NO es pot expressar amb l'rwx (el nucli de la pregunta d)

| Situació real | Amb rwx | Amb ACL |
|---|---|---|
| El servei web ha de **llegir** les notes, el propietari ha de poder **escriure**-les | O poses el servei al grup del propietari (i rep **tots** els permisos del grup, incloent-hi `w`) → **integritat en risc**, o obris la lectura a "resta" → **confidencialitat en risc** | `user:campus-web:r--` → el servei llegeix i **no** pot modificar; el propietari conserva `rw-` |
| Dos grups amb permisos **diferents** sobre el mateix fitxer | Impossible: només hi ha **una** categoria "grup" | `group:professors:rw` i `group:estudiants:r` |
| Un usuari concret **ni propietari ni del grup** | Impossible | `user:albert:rwx` |

*(Justificació de fons: `chmod` té només tres tecles — `u`, `g`, `o` — i no pot expressar "ara canvio només l'Alice". La màscara és exactament l'entrada que el sistema va inventar perquè `chmod` i `ls -l` no es trenquessin en tenir una llista més llarga que 3.)*

## e) PIE i ASLR

**PIE (Position-Independent Executable)**: un executable compilat/linkat per poder **carregar-se en adreces diferents en cada execució** (en lloc d'una adreça fixa). Compilar amb `-pie` (o `-fPIE`).

**Relació amb ASLR:** ASLR aleatoritza la ubicació de **pila, heap i biblioteques** a cada execució. **ASLR sense PIE és incompleto**: el binari principal continuaria carregant-se sempre a la mateixa adreça coneguda, de manera que els *gadgets* de codi del propi executable són predicibles. **PIE habilita que ASLR també aleatoritzi la base del programa** → PIE i ASLR **s'han d'utilitzar junts**. (Amb ASLR + DEP + PIE → *ASLR + DEP + PIE* són les tres proteccions més importants; el **canari** és la primera línia de defensa del compilador.)

**¿Hauria corregit per si sol les vulnerabilitats de PHP? NO.**

- PIE **no elimina cap vulnerabilitat**: el buffer overflow de l'intèrpret PHP seguia existint, i el codi maliciós es podria injectar igual.
- PIE només fa **més difícil** l'explotació: l'atacant ja no pot predir on és el codi per reutilitzar *gadgets* ni on és la pila → l'explotació deixa de ser determinista i s'ha de fer probabilística (per cada execució, una nova execució).
- La correcció de veritat és **arreglar el codi vulnerable** (corregir el CVE / actualitzar l'intèrpret) i aplicar **defensa multinivel**: canari + ASLR + PIE + DEP + menys privilegi + actualitzacions. PIE és **una capa més**, no la solució.

---

# Problema 2 — Contenidors i Docker (3,5 punts)

> *Servei que genera recorreguts d'entrenament; cada petició executa un programa C. Es va passar de màquina virtual a contenidor. Codi: `main` amb `candidatos = atoi(argv[1])`, `n = candidatos * 100000` i un vector de `double`.*

## a) Teoria del Tema 2 — MV vs contenidor ⚠️ (enunciat ocult)

> [!tip] a) i b) són **preguntes de teoria del Tema 2**
> Segons el professor, els apartats ocults **a) i b) del Problema 2 són del Tema 2** (MV / virtualització / contenidors), no d'anàlisi de codi. Per tant la resposta **primària** és la teoria, i l'anàlisi del codi queda com a **plan B** (per si el profe demana, al final, "què fa el programa / quanta memòria reserva").
> **Banc de preguntes del Tema 2 amb totes les respostes:** [[Qüestions-T2-MV-Contenidors|Qüestions T2 — MV i Contenidors]] (18 preguntes amb les opcions i per què les altres no).

**Les claus que has de tenir parades (T2, T2b, T2c):**

**Què és la virtualització a nivell de SO (el contenidor):** un **paradigma de SO** en què el **kernel** permet l'existència de **múltiples instàncies d'espai d'usuari aïllades** (contenedors, zones, jails, VEs…). El contenidor és una **abstracció de la capa d'aplicacions**, no de la capa de hardware (a diferència de la MV). Els processos hi fan les **crides al sistema directament al SO** → **no cal hypervisor**.

**MV vs contenidor, en una taula:**

| | **MV** | **Contenidor** |
|---|---|---|
| Què virtualitza | el **hardware** de la màquina | el **SO** (nivell de SO) |
| Què porta | kernel **+** espai d'usuari | **només l'espai d'usuari** |
| Kernels | **1 per MV** (el guest) | **1 sol**, compartit amb el host |
| SO guest | Cada MV pot executar un **SO diferent** | Un **únic SO host** |
| On es processa la crida | kernel **guest** → operació privilegiada → **trap** → VMM → kernel host | **directament** al kernel host |
| Aïllament | per **imposició** (no hi ha instrucció per sortir-ne) | per **filtratge** cooperatiu del mateix kernel |
| Tamany / arrencada | **GBs** / minuts | **MBs** / **segons** |
| SO diferent? | **Sí** (Windows sobre Linux) | **No** → necessita el kernel del host |

**Per què aquí un contenidor i no una MV (el cas del problema):** per reduir el consum de recursos i el **temps de posada en marxa**, i perquè cada càlcul és **aïllat** del servei de reserves que comparteix servidor. El cost: el contenidor **comparteix kernel** → un *bug* del kernel host és un risc per a **tots** els contenidors alhora, i el mode *root* dins d'un contenidor és perillós (privilege escalation).

**Si l'enunciat demana "avantatges dels contenidors":** ràpids i lleugers · portabilitat (porten totes les llibreries) · eficiència (crides directes al SO) · aïllament dels espais d'usuari · fàcil distribució.

**Si l'enunciat demana "avantatges de la virtualització":** duplicar el hardware subjacent a preu competitiu, aïllament, poder **parar / clonar / moure** una MV, recursos restringits per usuari, i el risc de la **fallada comuna** si peta l'host.

## b) Teoria del Tema 2 — Docker, imatges i recursos ⚠️ (enunciat ocult)

**Conceptes que has de poder definir:**

- **Docker**: tecnologia **open source de contenidors** (2013), que internament utilitza **cgroups** (limitar) i **namespaces** (aïllar), i hi afegeix **portabilitat** (el contenidor porta totes les llibreries) i **gestió de versions** estàtica a Git.
- **Imatge**: *captura de l'estat* d'un contenidor → **plantilla** per crear contenidors; d'una imatge en poden sortir **varis contenidors**. La imatge **parent** és la del `FROM`; `FROM scratch` → imatge base.
- **Contenidor**: **instància en execució** d'una imatge.
- **Dockerfile**: fitxer de **text pla** (estil *makefile*) per crear imatges.
- **Docker Compose**: eina per **definir i executar varis contenidors simultàniament** (`docker-compose.yml`).
- **Volums**: espais d'emmagatzematge **fora del contenidor**; **no s'esborren** amb el contenidor; per compartir dades.
- **Ports**: per defecte **no s'exposen**; cal publicar-los amb **`-p`** (crea un firewall que mapeja port del contenidor → port del host). Xarxes: **bridge** (mateix host) i **overlay** (host exterior).
- **Kubernetes**: orquestrador que aporta **gestió, desplegament i escalat** d'un gran nombre de contenidors.

**Si l'enunciat demana "què permet el contenidor controlar" (P3 de la T2b):** memòria RAM, espai de directori/fitxer accessible, nombre màxim de **CPUs** i nombre màxim de **processos** → i això ho fan els **cgroups**; els **namespaces** només aïllen la vista.

### Plan B — si finalment l'enunciat demana anàlisi del codi

**Pas a pas del programa:**

1. `argc != 2` → surt (cal exactament un argument).
2. `candidatos = atoi(argv[1])` → nombre de candidats (1..100); si és fora de rang → surt.
3. `n = (size_t)candidatos * 100000` → nombre d'elements del vector.
4. `costes = malloc(n * sizeof(costes))` → reserva el vector de `double`.
5. Primer bucle: `costes[i] = (double)(i % 1000) / 10.0` → omple el vector amb el patró **0,0 · 0,1 · … · 99,9** repetit cada 1000 elements.
6. Segon bucle: `suma += costes[i]` → suma total.
7. `printf("Coste medio: %.2f\n", suma / n)` → imprimeix la **mitjana** i acaba.

**Memòria (amb `sizeof(double) = 8` i 64 bits):**

| Argument | `n` (elements) | Bytes reservats | Equivalent |
|---|---|---|---|
| 50 | 5.000.000 | **40.000.000 B** | ≈ 38,1 MiB |
| 100 (màxim) | 10.000.000 | **80.000.000 B** | ≈ 76,3 MiB |
| 1 (mínim) | 100.000 | 800.000 B | ≈ 0,76 MiB |

**Sortida per a l'argument 50:** `Coste medio: 49.95` (la mitjana de 0,0…99,9 és 49,95; el patró es repeteix exactament 5000 cops, 5.000.000/1000).

**Sense desbordament d'enters:** el càstig a `size_t` es fa **abans** de multiplicar, i el màxim és 10.000.000 elements × 8 B = 80.000.000 B → **cap overflow** ni en `int` ni en `size_t` (64 bits).

**El que està bé:** es comprova `argc`, es valida el rang del paràmetre, es **comprova el retorn de `malloc`** (`NULL` → "Memoria insuficiente") i s'allibera la memòria amb `free`.

**El que es pot millorar:**

1. **`sizeof(costes)` en lloc de `sizeof(*costes)`** → `costes` és un **punter**, així que `sizeof(costes)` = `sizeof(double*)` = **8**. Funciona **per casualitat** perquè en 64 bits el punter i el `double` ocupen els mateixos 8 bytes. Amb un altre tipus de dada el càlcul seria **erroni**; la forma correcta és `sizeof(*costes)`.
2. **`atoi` no valida l'entrada** → si el paràmetre no és un número, `atoi` retorna 0 (i el programa surt pel rang, però sense missatge); a més `atoi` és **indefinit en overflow**. La forma correcta és `strtol` amb comprovació d'error. *(L'enunciat diu que l'argument és un enter decimal vàlid → no hi ha problema en aquest cas.)*
3. **Memòria i temps desproporcionats per al que es calcula**: la mitjana d'un patró **periodic** es pot calcular en **O(1)** i **sense reservar 40 MB**. I es podrien fusionar els dos bucles (un sol pas).
4. **Codi de sortida únic** → no distingeix "falta l'argument" de "memòria insuficient"; en un servei seria convenient distingir errors.
5. Relació amb la seguretat: el procés ha de ser **sense privilegis** dins del contenidor i els recursos (CPU/memòria) s'han de **limitar** amb *cgroups* (apartat c).

## c) Mecanisme per limitar CPU i memòria; per què els namespaces no serveixen

**Mecanisme: els *control groups* (cgroups).** Són el que **limita els recursos** d'un contenidor: memòria RAM, quota de CPU, E/S de disc i nombre de processos (T2b §6, T2c §4).

**Per què només amb *namespaces* no es resol:**

- Els **namespaces aïllen**: només controlen **què veu** el procés (PID, muntatge, xarxa, usuaris, UTS, IPC). No posen cap límit de consum.
- Els **cgroups limiten**: controlen **quant pot consumir** el procés.
- Per tant, un contenidor **només amb namespaces** és una millora del `chroot`: el procés veu la seva pròpia vista, però pot demanar **tota la CPU i tota la memòria** del host → un sol càlcul podria ofegar la **mateixa aplicació de reserves del rocòdrom** que viu al mateix servidor (i, per la compartició del kernel, és un risc per a tots els contenidors alhora).
- Conclusió de classe: **la MV intercepta les crides; el contenidor les deixa passar i en canvia la vista** → l'aïllament del contenidor és per **filtratge** (cooperatiu), i el control de recursos el fan els *cgroups*.

## d) 4 contenidors × 512 MiB en un servidor de 2 GiB sense swap

**L'afirmació «els llímits sumen exactament la memòria física, doncs el funcionament està garantit» és FALSA.** Un límit de memòria és un **tope per contenidor**, no una **reserva**; i la memòria física no és tota per als contenidors.

**Dos aspectes a considerar abans d'acceptar la configuració:**

1. **La memòria que no és dels contenidors.** Els 2 GiB del servidor els comparteixen el **kernel**, el **dimoni de Docker**, la **caché de pàgines** i, sobretot, **l'altra aplicació del servidor (les reserves del rocòdrom)** i el sistema en general. Per tant els 2 GiB **no** són tots per als 4 contenidors → cal deixar marge (per exemple, no assignar el 100% de la RAM als contenidors).
2. **Un límit és un màxim, no una garantia, i no hi ha swap.** Els 4 contenidors poden arribar **alhora** als seus 512 MiB → sense swap no hi ha marge: el sistema hauria d'arribar al **OOM killer** (matant processos, pot ser el servei de reserves!) o patir *thrashing* si hi hagués swap. Cal **dimensionar amb marge i monitoritzar**, no suposar que "suma exacta" vol dir "cap problema".

**Matís important:** en aquest cas concret el risc **no és del programa**: amb argument 50 el procés només necessita **40 MB** (i 80 MB com a màxim), molt per sota del límit de 512 MiB. El risc real és que la **suma de pics** dels 4 contenidors + la resta del servidor no càpiga.

*(I un altre matís tècnic: en cgroups v2, `memory.max` compta també la memòria de la caché de pàgines → un procés pot morir per OOM abans d'arribar al límit aparent.)*

## e) Registre d'imatges (Docker Hub); repositori vs etiqueta

**Funció del registre d'imatges (Docker Hub):** és un **repositori centralitzat i públic** on es **publiquen i es descarreguen les imatges** de Docker (`docker pull`, `docker push`). Així les imatges es **comparteixen entre màquines** en lloc de reconstruir-les i s'hi apliquen versions/tags.

**Distingir repository i tag** (T2b §9 i P2 §7 de l'edició 2025-2026):

| | **Repositori** | **Etiqueta (tag)** |
|---|---|---|
| Què és | Un **contenidor lògic** d'imatges, identificat per un nom (p. ex. `ubuntu`, o `organitzacio/projecte`) | Un **punter a una versió concreta** d'una imatge dins del repositori (p. ex. `22.04`, `latest`) |
| Referència completa | `repositori` | `repositori:etiqueta` → `ubuntu:22.04` |
| Conté | Totes les versions/etiquetes | Una imatge concreta |
| Característica | El repositori és el "lloc"; el tag és la "direcció" | El tag és **mutable** (es pot reapuntar); la **immutabilitat** la dona el **digest** |

Relació amb la resta: la **imatge** és la *plantilla* (captura de l'estat d'un contenidor) i el **contenidor** n'és la *instància en execució*; el **Dockerfile** és la recepta per construir la imatge. Per això `:latest` és **perillós** (canvi silenciós) i és millor fixar versions explícites (`:1.0`) o el digest.

## f) Orquestració de contenidors

**Què és:** l'**automatització de la gestió d'un conjunt de contenidors** (a un o molts hosts) mitjançant una descripció declarativa de l'estat **desitjat** (quin servei, quina imatge, quants exemplars, xarxes, volums, secrets) i un component que s'encareceix que l'estat **real** hi convergeixi.

**Què aporta respecte a executar-los individualment** (`docker run` a mà): **descobreix, planifica, manté i escala** el Conjunt; l'operador no ha de fer res manualment.

**Dues tasques que pot fer (de classe):**
1. **Escalat** (horitzontal) de serveis: crear/eliminar exemplars segons la càrrega (T2b §13, Kubernetes: *gestió, desplegament i escalat* d'un gran nombre de contenidors).
2. **Recuperació automàtica / reinici** de contenidors que fallen (*self-healing*) i **desplegament de versions** amb *rolling update* i possibilitat de *rollback*.

*(Al nivell bàsic de classe: **Docker Compose** permet definir i executar **varis contenidors simultàniament** amb un `docker-compose.yml`; per a grans flotes, **Kubernetes** és l'orquestrador. T2b §9 i §13.)*

---

# Problema 3 — Sistemes de fitxers (3,5 punts)

> *`ocarina.raw`: 100.000 B, mostres de 2 B, sense capçalera. Blocs de 4096 B. `int16_t muestras[3072]`, `inicio = 11*4096 + 3072`, un `lseek` i un `read` de `sizeof muestras`.*

## a) Teoria del Tema 3 — i-node i estructura del FFS ⚠️ (enunciat ocult)

> [!tip] a), b) i e) són **preguntes de teoria del Tema 3**
> Igual que al Problema 2, els apartats ocults del P3 són del **Tema 3** (sistemes de fitxers). Per tant la resposta **primària** és la teoria, i l'anàlisi del codi queda com a **plan B**.
> **Banc de preguntes del Tema 3 amb totes les respostes:** [[Qüestions-T3-Fitxers|Qüestions T3 — Fitxers]] (18 preguntes P1-P18).

**Les claus que has de tenir parades:**

**Què és un i-node i què emmagatzema:** un **únic i-node per fitxer**, de **mida fixa** i amb un **ID numèric** → el sistema el localitza immediatament. Guarda **dos blocs de camps**:
1. **Atributs**: mida, dates, **permisos**, propietari…
2. **Punterers als blocs** del fitxer (el que fa que el fitxer sigui "un vector" i no una llista enlaçada).

Els i-nodes viuen en una **zona coneguda** del sistema de fitxers i el **nombre d'i-nodes està prefixat**: **un i-node per cada 16 KB** d'espai al disc. Un **directori** és un fitxer (taula) que associa **noms → i-node**.

**Els 15 punterers (arbre fix i asimètric):**

| # | Tipus | Blocs | Mida màxima (bloc 4 KB, punter 4 B) |
|---|---|---|---|
| 1-12 | **Directe** | 12 | 48 KB |
| 13 | **Indirecte simple** | 1024 | ~4 MB |
| 14 | **Doblement indirecte** | 1024² | ~4 GB |
| 15 | **Triplement indirecte** | 1024³ | ~4 TB |

**Per què "asimètric":** els primers 48 KB es resolen amb **0 indireccions**, els següents amb **1**, després **2**, després **3** → un fitxer petit no paga la cadena llarga i un de gran té prou capacitat. Un bloc de punteres de 4096 B amb punters de 4 B hi capen **1024**.

**FAT vs FFS (el contrast que sempre demanen):** la FAT emmagatzema els blocs d'un fitxer en una **llista enlaçada** (i per això l'**accés aleatori és pobre** i els fitxers queden **fragmentats**); el FFS usa **vectors** (punterers a l'i-node) → accés **directe** i escalable.

**Si l'enunciat demana "com es localitza un fitxer" (exemple de classe `/usr/ast/mbox`):** es coneix la posició del **directori arrel** → es busca `usr` → el seu **i-node 6** diu que `/usr` és al **bloc 132** → al bloc 132 es busca `ast` → l'**i-node 26** diu que és al **bloc 406** → al bloc 406 es busca `mbox` → l'**i-node 60** → es llegeix l'i-node i el fitxer queda obert. (Xifres de la **figura** D20: el text del PPT té errates.)

### Plan B — si finalment l'enunciat demana què fa el codi

1. `open("ocarina.raw", O_RDONLY)` → descriptor; si torna `-1` → surt amb error.
2. `off_t inicio = 11 * 4096 + 3072` = **48.128 bytes** → és el **desplaçament absolut** del fragment dins del fitxer.
3. `lseek(fd, inicio, SEEK_SET)` → posiciona el punter de lectura a l'offset 48.128 (dins del **bloc lògic 11**, al byte 3072 del bloc). Si torna `-1` → error.
4. `read(fd, muestras, sizeof muestras)` → `sizeof muestras` = 3072 × `sizeof(int16_t)` = 3072 × **2** = **6144 bytes**; es llegeixen al vector de la **pila**.
5. Com que 48.128 + 6.144 = **54.272 ≤ 100.000**, el fitxer és prou gran → el `read` **torna tots els 6144 bytes** → imprimeix `Bytes leidos: 6144`.
6. `close(fd)` i sortida.

**Observacions:**
- **No llegeix tota la gravació**: gràcies al `lseek` salta directament al fragment → només llegeix **6144 bytes** (el 6,1 % del fitxer) en lloc dels 100.000. És el **accés aleatori** que ho permet.
- **Alineament de mostres**: 48.128 és **parell** → el fragment comença exactament en un límit de mostra (mostra 24.064) → les 3072 mostres llegides són mostres completes (24.064 … 27.135).
- El `read` omple el buffer **de dades**, no cal (i no es) un `malloc`: és un array de 6144 bytes a la pila.

## b) Teoria del Tema 3 — mida, blocs i espai assignat ⚠️ (enunciat ocult)

**Mida lògica vs espai assignat (la distinció de classe, T3-P1 §7 i §9):**

- **Mida lògica**: el que veu el procés en llegir → el camp *size* de l'**i-node**. Per a `ocarina.raw`: **100.000 bytes**.
- **Espai assignat**: els **blocs de debò** al disc. Amb blocs de 4096 B → `ceil(100.000 / 4096)` = **25 blocs** (0…24); l'últim és **parcial** (1696 B).
- Els **bytes sobrants** d'un bloc **no els pot fer servir cap altre fitxer** → el fitxer ocupa 25 × 4096 = **102.400 B** al disc tot i tenir 100.000 B de mida lògica.
- **No es pot llegir un byte** sense llegir **tot el bloc** → una lectura de 6144 bytes consumeix **3 blocs** de disc.

**Els altres conceptes curts del tema que poden aparèixer:**

- **Sector vs bloc:** el **sector** és la unitat mínima que el **disc** pot llegir o escriure (típicament 512 B); el **bloc** és la unitat mínima que el **SO** llegeix o escriu (1024–8192 B; aquí 4096 B) i és **igual o múltiple** del sector.
- **Espai lliure:** el **FFS** ho fa amb un **bitmap** (1 bit per bloc: 0 = lliure, 1 = ocupat) en una posició coneguda; la **FAT** ha de **recórrer la taula** buscant el "següent bloc lliure" → fragmentació.
- **Localitat:** el FFS agrupa en **block groups** (i-nodes + dades + bitmap per grup) i associa cada directori a un grup → menys *seek*.
- **Truncar vs esborrar:** truncar = reduir la mida **sense esborrar**; esborrar = treure l'entrada del directori i **lliurar els blocs**.
- **MBR:** sector d'arrencada **fora** del sistema de fitxers amb la **taula de particions** (tipus, mida, active) i el codi d'arrencada; el localitza la **BIOS**.

### Plan B — si finalment l'enunciat demana les xifres del codi

- **Mostres llegides:** 3072 mostres (de 2 bytes) = **6144 bytes**.
- **Rang de mostres del fitxer:** de la 24.064 a la 27.135 (amb mostres numerades des de 0).
- **Blocs lògics implicats:** el fragment va del byte 48.128 al 54.271 → travessa **3 blocs**:
  - bloc **11** (bytes 45.056–49.151): només la part final, des del byte 48.128 → **1024 bytes** del fragment;
  - bloc **12** (49.152–53.247): **sencer** → 4096 bytes;
  - bloc **13** (53.248–57.343): només el inici, fins al 54.271 → **1024 bytes**.
- **Mida del fitxer en blocs:** **25 blocs** (l'últim parcial, 1696 B).
- Per la mateixa raó, una lectura de 6144 bytes **consumeix 3 blocs** de disc encara que només calguin 6144 bytes.

## c) FFS: quins punters i quantes lectures de bloc

**Pas 0 — el model (per no perdre el fil):** un **fitxer** és un **corrent de bytes** pla i continu (0 … mida−1) repartit en **molts blocs**, i **cap bloc no conté dades de dos fitxers**. L'**i-node** fa el mapeig `byte → bloc lògic → bloc física`.

**Pas 1 — quins blocs lògics toca el fragment?**

`inicio = 11×4096 + 3072 = 48.128` i la lectura és de `3072 × 2 = 6144` bytes → del byte 48.128 al 54.271.

| Càlcul | Resultat |
|---|---|
| `48128 / 4096` = 11 (resto **3072**) | el fragment **comença al bloc lògic 11**, a l'offset 3072 |
| `54271 / 4096` = 13 (resto **1023**) | el fragment **acaba al bloc lògic 13**, a l'offset 1023 |

```
bloc 11 (45056─49151) │ bloc 12 (49152─53247) │ bloc 13 (53248─57343)
  [3072 no][ 1024 ✔ ]  [    4096 ✔    ]        [ 1024 ✔ ][2048 no]
                    48128                  54272
```
→ Blocs implicats: **11, 12 i 13**.

**Pas 2 — quin punter apunta a cada bloc?**

```
i-node (ja en memòria)
 ├── punters 1..11  ──► blocs lògics 0..10
 ├── punter 12 (DIRECTE) ──► bloc lògic 11          ← el fragment en comença aquí
 ├── punter 13 (INDIRECTE SIMPLE) ──► BLOC DE PUNTERS
 │        ├── entrada 0 ──► bloc lògic 12
 │        └── entrada 1 ──► bloc lògic 13           ← el MATEIX bloc de punteres
 ├── punter 14 (doble indirecte)  → no cal
 └── punter 15 (triple indirecte) → no cal
```

- Els **12 directes** cobreixen els blocs **0…11** → el **bloc 11** el resol el **12è punter directe**.
- L'**indirecte simple** cobreix els blocs **12 … 1035** (1024 entrades) → els blocs **12 i 13 hi cauen tots dos**, i com que són **consecutius**, **un sol bloc de punteres** en dona els dos. No cal el doble ni el triple indirecte.

**Pas 3 — quantes lectures de bloc?**

| # | Què es llegeix | Per què |
|---|---|---|
| 1 | **bloc de punteres indirecte simple** | per saber on són els blocs 12 i 13 (no en sabíem res) |
| 2 | **bloc de dades 11** | 1024 bytes del fragment |
| 3 | **bloc de dades 12** | 4096 bytes del fragment |
| 4 | **bloc de dades 13** | 1024 bytes del fragment |
| | **TOTAL** | **4 lectures de bloc** |

No es compten: l'i-node (ja és en memòria), les cerques de directori ni les lectures anticipades.

**Pas 4 — per què no 2 ni 3?**

> **lectures = (blocs de dades tocats) + (1 per cada nivell de punter caldre llegir)**

| Fragment | Lectures | Motiu |
|---|---|---|
| només bloc 11 | **1** | resolt amb un directe, sense cap bloc de punteres |
| només bloc 12 | **2** | 1 del bloc de punteres + 1 de dades ← el "dues lectures" |
| blocs **11, 12 i 13** (el nostre) | **4** | 1 directe + 1 bloc de punteres + 2 dades |
| només blocs 12 i 13 | **3** | 1 bloc de punteres + 2 dades |
| bloc 2000 (fora de l'indirecte simple) | **+1 nivell** | cal el **doble indirecte**: 2 blocs de punteres + 1 de dades |

**El truc de la pregunta:** el fragment **travessa la frontera** entre el que resolen els directes (fins al 11) i el que resol l'indirecte (a partir del 12). Per això la resposta és **4** i no 3, i per això l'enunciat parla de «el **bloque de punteros indirectos**» en singular: n'hi ha **un** per als dos blocs.

**Cost real:** per obtenir 6144 bytes es llegeixen **3 blocs sencers = 12.288 bytes** del disc (el doble), perquè el sistema de fitxers **no pot llegir un byte sense llegir el bloc sencer**.

→ Cal **1 punter directe** i **1 punter indirecte simple** (el mateix bloc de punteres serveix per als blocs 12 i 13).

## d) Si el fitxer estigués en FAT: quants salts i valoració de l'afirmació

**Quants salts de la cadena FAT:** el primer **clúster** del fitxer és el **bloc lògic 0** (l'entrada del directori en desa el seu número). El primer bloc **sol·licitat** és el lògic **11** (offset 48.128 → `floor(48128/4096) = 11`).

Per arribar-hi cal seguir la **llista enlaçada**: clúster 0 → 1 → 2 → … → 11, és a dir **11 salts** entre entrades de la cadena FAT, és a dir **11 entrades de la FAT llegides** (les dels blocs lògics 0…10; l'última és la que dona el clúster físico del bloc 11).

Per a **tot el fragment** (blocs 11, 12 i 13) i **sense memòria cau**: 13 entrades de la FAT (per als lògics 0…12) + 3 lectures de dades = **16 accessos**, contra els **4** del FFS.

**Afirmació: «Si coneixem el primer bloc físico, podem calcular els altres sumant el número de bloc lògic» → FALSA.**

- A la **FAT** els blocs d'un fitxer formen una **llista enlaçada** i poden estar **fragmentats**: el número del següent bloc **no es dedueix** sinó que **està emmagatzemat** a l'entrada corresponent de la taula FAT. L'únic bloc el coneixem de antemà és el **primer** (per l'entrada del directori); la resta cal **recorrer la cadena**.
- Només seria cert si el fitxer estigués emmagatzemat **contigu** (i encara la FAT és l'autoritat) → i això no es pot garantir.
- Aquesta és la **limitació estructural de la FAT** que resoldrà el FFS: **accés aleatori pobre** (per arribar a un bloc cal recórrer la llista enlazada) i **fitxers fragmentats**. Amb el **FFS** (vectors + i-node) l'accés és **directe**: el bloc lògic 12 s'aconsegueix amb un sol accés al bloc indirecte, sense recórrer res.
- (I la **heurística de localitat** del FFS encara millora el rendiment en HDD: blocs d'un mateix directori al mateix grup → menys *seek*.)

## e) Altres preguntes curtes del tema ⚠️ (enunciat ocult)

*El text exacte no es coneix; aquestes són les respostes curtes del **Tema 3** per si hi ha sortit alguna (tot el temari del bloc, en format test, és a [[Qüestions-T3-Fitxers|Qüestions T3 — Fitxers]]):*

- **Mida del fitxer en blocs:** 100.000 B amb blocs de 4096 B → **25 blocs** (l'últim parcial: 1696 B). Els blocs s'ocupen **sencers** i els bytes sobrants **no** els pot fer servir cap altre fitxer.
- **Sector vs bloc:** el **sector** és la unitat mínima que el **disc** pot llegir/escriure (normalment 512 B); el **bloc** és la unitat mínima que el **SO** llegeix o escriu (1024–8192 B; aquí 4096 B). El bloc és un múltiple del sector.
- **Espai lliure:** el **FFS** ho fa amb un **bitmap** (1 bit per bloc; 0 = lliure, 1 = ocupat) en una posició coneguda; la **FAT** ha de **recórrer la taula** buscant el "següent bloc lliure" → molta fragmentació.
- **Localitat:** el FFS agrupa en **block groups** (i-nodes + dades + bitmap per grup) i associa cada directori a un grup → els fitxers d'un directori queden **físicament a prop** → el braç del disc es mou menys (cada salt té un cost mecànic).
- **FAT vs FFS:** la FAT usa una **llista enlaçada** (anys 70), el FFS **vectors** (mitjans dels 80; base d'ext3/ext4/NTFS).
- **Millores del FFS:** directoris amb **arbres balancejats**, **journaling** (consistència dels metadades davant d'un tall/avarcia) i **copy-on-write** (no sobreescriu → conserva versions anteriors; ex. BTRFS).
- **I-node:** **atributs + punterers als blocs**; mida fixa i ID; **un i-node per cada 16 KB** de disc.
- **Truncar vs esborrar:** truncar = reduir la mida **sense esborrar**; esborrar = treure l'entrada del directori i **lliurar els blocs**.
- **SSD:** sense parts mòvils → accés aleatori molt ràpid; cal **esborrar** el bloc abans d'escriure-hi; **wear leveling** per no degradar les cel·les.
- **MBR:** sector d'arrencada **fora** del sistema de fitxers, amb la **taula de particions** (tipus, mida, active) i el codi d'arrencada; el localitza la **BIOS**.


---

## Dubtes / a revisar

- **Els enunciats a), b) (i e) de P3) estan ocults** → les respostes són la **deducció raonada** a partir del codi i del material de classe. Cal contrastar-les amb el que publiqui el professor el dia de l'examen (9:00 del 30-10-2026).
- **P3 a/b/e**: el mateix criteri que al P2 → la resposta **primària** és la **teoria del Tema 3** (i-node i els 15 punterers · mida lògica vs espai assignat · sector vs bloc · bitmap · localitat · journaling vs COW · MBR) i l'anàlisi del codi queda com a **plan B**. Banc de preguntes: [[Qüestions-T3-Fitxers|Qüestions T3 — Fitxers]].
- **P1 a/b**: el codi publicat **no té buffer overflow** (la comparació `>= sizeof usuario` és correcta: 15 caràcters + `'\0'` = 16 bytes exactes). Si el professor havia publicat una versió **deliberadament segura** per veure qui calcula els números en lloc de dir "sí, hi ha overflow", la resposta és aquesta. Si l'enunciat ocult demanava "identifica la vulnerabilitat", la resposta és: *patró insegur* (`strcpy` + dependència d'una comprovació manual, una sola capa) i les vulnerabilitats reals estaven al **intèrpret PHP en C**.
- **P2 a/b**: el guany (49,95 i 40.000.000 B) està **verificat executant** el codi; el `sizeof(costes)` funcionant «per casualitat» és el punt picant del fragment.
- **P1 d) (ACL)**: l'exemple de la màscara està **verificat executant-lo** (sortida real de `ls -l` sobre el fitxer, amb l'ACL escrita com a xattr POSIX). `setfacl`/`getfacl` **no són instal·lats** a Void → `xbps-install acl` si vols poder-hi jugar a mà; si el profe fa la pregunta en viu, ells també ho faran amb `setfacl`.
- **P2 a/b**: el professor ha confirmat que són **preguntes de teoria del Tema 2** → la resposta primària és la de la secció (MV vs contenidor · Docker/imatges/volums/ports/Kubernetes) i l'anàlisi del codi queda com a **plan B**. Tot el temari del bloc, en format test, és a [[Qüestions-T2-MV-Contenidors|Qüestions T2 — MV i Contenidors]].
- **P3 d)**: el compte de **11 salts** fa referència a la **cadena**; si el profe preguntés pel **nombre d'accés a la FAT** amb memòria cau/no cau, són 11 (per arribar al bloc 11) i 13 (per tot el fragment), sempre + 3 lectures de dades.
- **P3 c)**: les lectures anticipades (*readahead*) i la cerca de directoris queden **expressament excloses** per l'enunciat → 4 lectures.

---

## Enllaços relacionats

- [[T1-Introduccio-Seguretat-SO|T1 — Introducció a la seguretat en SOs]] (P1)
- [[Qüestions-T1-Seguretat|Qüestions T1 — Seguretat]] (PIE, ASLR, ACL, canaris)
- [[T2b-Contenedors-Docker|T2b — Contenedors i Docker]] (P2)
- [[Qüestions-T2-MV-Contenidors|Qüestions T2 — MV i Contenidors]] (banc de preguntes del Tema 2)
- [[T2c-Comparativa-SO-MV-Contenidor|T2c — SO, MV i contenidor]] (cgroups vs namespaces)
- [[T2-Maquines-Virtualitzacio-SO|T2 — Màquines virtuals i virtualització]] (P2)
- [[T3-Sistemes-Fichers-P1|T3 — Sistemes de fitxers (Parte 1)]] (FAT, sector vs bloc, MBR)
- [[T3-Sistemes-Fichers-P2|T3 — Sistemes de fitxers (Parte 2)]] (FFS, i-node, 15 punterers)
- [[Qüestions-T3-Fitxers|Qüestions T3 — Fitxers]] (banc de preguntes del Tema 3)
- [[T3-Sistemes-Fichers-P1|T3 — Sistemes de fitxers (Parte 1)]] (FAT, sector vs bloc, MBR)
- [[T3-Sistemes-Fichers-P2|T3 — Sistemes de fitxers (Parte 2)]] (FFS, i-node, 15 punterers)
- [[NotesMVs|Notes MVs]] · [[Tests-Unidad-SO|Tests d'unitat]]
- [[_Index_SO|Índex Sistemes Operatius I]]
