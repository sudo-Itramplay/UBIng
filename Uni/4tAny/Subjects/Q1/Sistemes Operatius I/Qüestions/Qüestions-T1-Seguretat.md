---
tags:
  - tipus/parcial
  - assignatura/SO
---

# Qüestions — T1 Seguretat

Test de pràctica sobre la [[T1-Introduccio-Seguretat-SO|T1 — Introducció Seguretat SO]]. Cadascuna: **concepte** (dels apunts de classe) → **pregunta** → **resposta** → **per què sí i per què les altres no**. Les preguntes es mantenen en l'original (castellà).

---

## P1 — Compilació i ASLR

### Concepte

**ASLR** (Address Space Layout Randomization) aleatoritza la ubicació de la pila, el heap i les biblioteques a cada execució — impossible predir on és el codi.

**PIE** (Position Independent Executable) és un executable que **es carrega en adreces diferents cada execució** → complementa ASLR. ASLR + DEP + PIE = les tres proteccions més importants contra buffer overflow.

Un executable **no-PIE** es carrega sempre a la mateixa adreça fixa → facilita l'atac.

### Pregunta

¿Qué opción de compilación hace que un ejecutable se cargue en direcciones aleatorias cada vez que se ejecuta?

- [ ] -O2
- [ ] -z execstack
- [ ] -no-pie
- [x] **-pie**

### Per què la D sí

`-pie` genera un executable PIE → es carrega a adreça aleatòria cada execució (gràcies a ASLR).

### Per què les altres no

- **-O2**: optimització del compilador, no té res a veure amb l'adreçament.
- **-z execstack**: fa el contrari — marca la pila com **executable**, eliminant DEP i facilitant l'execució de codi injectat.
- **-no-pie**: **desactiva** PIE → adreça fixa sempre.

---

## P2 — ACLs

### Concepte

El model clàssic UNIX (**rwx**) només distingeix tres categories: **propietari**, **grup**, **resta**. No pots donar permís a un usuari concret que no sigui ni propietari ni del grup.

Les **ACLs** (Access Control Lists) són **més granulars que rwx**: permisos per a **usuaris individuals i grups específics**, un a un. Comanda: `setfacl -option file_owner:file_permission filename`.

### Pregunta

En un sistema con Access Control Lists (ACL), ¿qué ventaja se obtiene respecto al modelo clásico de permisos (rwx)?

- [ ] Mayor velocidad de acceso
- [ ] Eliminación de los permisos de grupo
- [ ] Posibilidad de ejecutar código en kernel mode
- [x] **Control más granular sobre usuarios específicos**

### Per què la D sí

Definició literal d'ACL: permisos més granulars, per a usuaris/grups específics, anant més enllà de les tres categories rwx.

### Per què les altres no

- **Mayor velocidad**: ACLs afegeixen comprovacions, no acceleren l'accés.
- **Eliminación de los permisos de grupo**: els grups continuen existint; les ACLs **hi afegeixen** precisió, no substitueixen el model.
- **Ejecutar código en kernel mode**: cap mecanisme de permisos de fitxers dona accés a kernel mode (anell 0). Això és qüestió d'anells de protecció, no d'ACLs.

---

## P3 — Què és un buffer overflow

### Concepte

Un **buffer overflow** és quan un programa **sobreescriu** la memòria d'un buffer superant-ne la mida. Exemple clàssic: `gets(buffer)` amb buffer de 10 bytes — `gets()` no comprova longitud. Amb més de 10 caràcters es desborda i pot sobreescriure l'adreça de retorn → control del flux d'execució.

Tipus: **stack overflow** (pila de crides) i **heap overflow** (memòria dinàmica).

### Pregunta

¿Cuál de los siguientes escenarios es un ejemplo típico de vulnerabilidad de tipo buffer overflow?

- [ ] Acceso concurrente a un fichero bloqueado
- [ ] Saturación de la red por tráfico SSH
- [x] **Escritura fuera de los límites de un array**
- [ ] Llamada recursiva sin condición de parada

### Per què la C sí

Definició mateixa: escriure **més enllà dels límits** d'un array/buffer.

### Per què les altres no

- **Acceso concurrente a un fichero bloqueado**: problema de **concurrencia/sincronització**, no de límits de memòria.
- **Saturación de la red**: problema de **xarxa / DoS**, no de memòria.
- **Recursió sense condició de parada**: és un **stack overflow per recursió** — s'acaben les entrades de pila, no es desborda un buffer. Relacionat però diferent: aquí no s'escriu fora de límits d'un array, sinó que la pila s'omple de trucades.

---

## P4 — Proteccions (identifica la INCORRECTA)

### Concepte

Contra buffer overflow hi ha diversos mecanismes (T1, secció 10):

| Mecanisme | Què fa |
|---|---|
| **Canari** | Valor aleatori al stack; si se sobreescriu → "stack smashing detected" i abort |
| **ASLR** | Aleatoritza ubicació de pila, heap i biblioteques → impossible predir on és el codi |
| **DEP** | Marca pila/heap com **no executables** → impedeix execució de codi inyectat |
| **PIE** | Executable es carrega en adreces diferents cada execució → complementa ASLR |

Cap d'ells "desactiva comprovacions de límits" — això és feina de les **funcions segures** (`fgets`, `strncpy`) i la **limitació de longitud**.

### Pregunta

Identifica la afirmación INCORRECTA sobre mecanismos de protección ante buffer overflow.

- [ ] Los canarios detectan corrupción de la pila
- [ ] ASLR dificulta predecir direcciones de memoria
- [x] **PIE desactiva las comprobaciones de límites de los buffers**
- [ ] DEP evita ejecutar código en zonas de datos

### Per què la C és la resposta

**PIE no desactiva cap comprovació de límits** — és fals. PIE només permet que l'executable es carregui a adreça aleatòria (complementa ASLR). Les comprovacions de límits les fa el programador/les funcions segures; PIE no les toca.

### Per què les altres són correctes (per tant, no són resposta)

- **Canarios detectan corrupción de la pila**: ✅ cert — el canari és un valor de control entre buffer i adreça de retorn; si es corromp, s'aborta.
- **ASLR dificulta predecir direcciones**: ✅ cert — és exactament la seva funció.
- **DEP evita ejecutar código en zonas de datos**: ✅ cert — marca pila/heap com no executables.

---

## P5 — Reduir el risc de buffer overflow

### Concepte

La primera línia de prevenció és **no desbordar el buffer en origen**:

- ❌ `gets()`, `strcpy()` — no validen mida → causes clàssiques de buffer overflow
- ✅ `fgets()`, `strncpy()` — limiten l'escritura al buffer

A més: comprovar la longitud abans de copiar (limitació de longitud) i mantenir el sistema actualitzat.

### Pregunta

¿Cuál de las siguientes acciones reduce el riesgo de vulnerabilidades por buffer overflow?

- [x] **Usar funciones como fgets() o strncpy()**
- [ ] Desactivar ASLR para depurar programas
- [ ] Usar funciones como gets() o strcpy()
- [ ] No validar el tamaño de entrada del usuario

### Per què la A sí

`fgets()` i `strncpy()` són les **funcions segures**: validen/limiten la mida d'escritura al buffer → no es pot desbordar.

### Per què les altres no

- **Desactivar ASLR**: treu una protecció, **augmenta** el risc. Només té sentit puntualment per depurar.
- **gets() / strcpy()**: són justament les funcions **insegures** que causen buffer overflow — el contrari del que pregunten.
- **No validar la mida**: és la definició de com es provoca un buffer overflow → augmenta el risc.

---

## P6 — Canaries

### Concepte

El **canari** (canari de pila) és la primera línia de defensa del compilador: insereix un **valor de control/aleatori** entre el buffer i l'adreça de retorn. En un flux normal: buffer → EBP → adreça de retorn; el canari queda intercalat. Si un overflow intenta arribar a l'adreça de retorn, **primer ha de trencar el canari** → el compilador el comprova abans del `ret` → "stack smashing detected" i abort.

Compilació: `-fstack-protector` (per defecte a Linux) / `-fno-stack-protector` (sense).

### Pregunta

¿Qué técnica intenta proteger la pila de ejecución insertando valores de control entre el buffer y la dirección de retorno?

- [ ] DEP
- [x] **Canarios**
- [ ] ASLR
- [ ] PIE

### Per què la B sí

La descripció de la pregunta és literalment el canari: **valors de control entre el buffer i l'adreça de retorn**. Si es corrompen, es detecta el desbordament.

### Per què les altres no

- **DEP**: no insereix cap valor — marca pila/heap com **no executables** (impedeix executar codi injectat, no detecta la corrupció).
- **ASLR**: no insereix valors — **aleatoritza adreces** de memòria.
- **PIE**: no insereix valors — permet que l'executable es carregui a **adreça diferent** cada execució.

---

## Resum ràpid

| Mecanisme | Què fa | No fa |
|---|---|---|
| **Canaries** | Valors de control entre buffer i adreça de retorn; detecten corrupció | No aleatoritza res |
| **ASLR** | Randomitza adreces de memòria cada execució | No insereix valors ni marca pàgines |
| **PIE** | Executable carregable a adreça aleatòria | No desactiva comprovacions de límits |
| **DEP / NX** | Impedeix executar codi en zones de dades (pila, heap) | No detecta corrupcions |
| **ACLs** | Permisos més granulars que el model rwx clàssic | No dóna accés a kernel mode |
| **Funcions segures** | `fgets`/`strncpy` limiten l'escritura | — |

---
[[T1-Introduccio-Seguretat-SO|T1 — Introducció Seguretat SO]] · [[_Index_SO|Index SO]]
