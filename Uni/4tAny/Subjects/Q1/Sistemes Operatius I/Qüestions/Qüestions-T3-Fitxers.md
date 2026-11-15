---
id: Qüestions-T3-Fitxers
aliases:
  - Qüestions T3
tags:
  - tipus/parcial
  - assignatura/SO
assignatura: SO
data: "2026-10-30"
---

# Qüestions — T3 Sistemes de fitxers

Banc de preguntes del **Tema 3** (sistemes de fitxers), en el mateix format que [[Qüestions-T1-Seguretat|Qüestions T1]] i [[Qüestions-T2-MV-Contenidors|Qüestions T2]]: **concepte** (dels apunts de classe) → **pregunta** (en castellà) → **resposta** → **per què sí i per què les altres no**.

Font: [[T3-Sistemes-Fichers-P1]] (Parte 1) i [[T3-Sistemes-Fichers-P2]] (Parte 2), PDFs 03.

> [!tip] Per a què serveix
> El **Problema 3** del parcial 2026-2027 té els apartats **a), b) i e) ocults** i són **preguntes del Tema 3** (la mateixa lògica que al Problema 2). Aquí tens tot el temari del bloc en format test i amb les respostes.

---

## P1 — Fitxer vs directori

### Concepte

Un **fitxer** és una **col·lecció ordenada de dades** amb relació entre si, emmagatzamada permanentment en un dispositiu **no volàtil**. Un **directori** **no conté les dades** dels fitxers: conté les **entrades** (noms → i-node + metadades) que permeten trobar-los.

### Pregunta

¿Contiene un directorio los datos de los archivos que contiene?

- [x] **No: contiene las entradas (nombre → metadatos y puntero al i-node) que permiten localizarlos**
- [ ] Sí, el directorio es una tabla con el contenido de cada archivo
- [ ] Solo si el archivo ocupa más de un bloque
- [ ] Depende del sistema de ficheros

### Per què la A sí

Definició de classe: el directori és una **taula**; les dades viuen als **blocs** apuntats per l'i-node de cada fitxer.

### Per què les altres no

- **Sí, es una tabla con el contenido**: el directori és una taula, però de **entrades**, no del contingut.
- **Si ocupa més d'un bloc**: el fitxer pot ocupar molts blocs i el directori sempre només en guarda la referència.
- **Depende del FS**: la distinció fitxer/directori és del model de SO, no de la implementació.

> [!tip] "fichero" i "archivo" són **sinònims**
> El PPT diu literalment *"un fichero (o archivo) es una colección ordenada de datos"* → el canvi de terme és la variant d'espanyol, el concepte és el mateix.

---

## P2 — Sector vs bloc

### Concepte

- **Sector de disc**: unitat mínima que el **disc** pot llegir o escriure (típicament **512 bytes**).
- **Bloc del sistema de fitxers**: unitat mínima que el **SO** llegeix o escriu. Té **el mateix tamany o un múltiple** del sector; són comuns 1024, 2048, 4096 o 8192 (Intel: **4096**).

### Pregunta

¿Cuál es la diferencia entre un sector de disco y un bloque del sistema de ficheros?

- [x] **El sector es la unidad mínima que lee el disco; el bloque es la unidad mínima que lee el SO (es un múltiplo del sector)**
- [ ] Son exactamente lo mismo
- [ ] El bloque siempre es más pequeño que el sector
- [ ] El sector depende del sistema de ficheros

### Per què la A sí

És la definició de classe, i és la clau per entendre la resta del tema.

### Per què les altres no

- **Són el mateix**: no, són unitats de **capes diferents** (hardware vs SO).
- **El bloc és més petit**: al contrari, és **igual o més gran** (múltiple).
- **El sector depèn del FS**: no, el sector és propietat del **disc**.

---

## P3 — I-node: què guarda i com es localitza

### Concepte

- Un **únic i-node per fitxer**, de **mida fixa** i amb un **ID numèric** → el sistema el localitza ràpidament (i-node 1074).
- Guarda **dos blocs de camps**: (1) **atributs** (mida, dates, permisos, propietari…) i (2) **punterers als blocs** del fitxer.
- Els i-nodes viuen en una **zona coneguda** del sistema de fitxers; el **nombre d'i-nodes està prefixat**: **un i-node per cada 16 KB** d'espai al disc.
- Un **directori** és un fitxer (taula) que associa **noms → i-node**.

### Pregunta

¿Qué información almacena un i-node?

- [x] **Los atributos del archivo y los punteros a sus bloques de datos**
- [ ] Solo el nombre del archivo
- [ ] El contenido del archivo y el nombre
- [ ] Únicamente la lista de nombres del directorio padre

### Per què la A sí

Definició de classe (D14): **atributos + punteros a los bloques**.

### Per què les altres no

- **Solo el nombre**: el nom és a l'**entrada del directori**, no a l'i-node.
- **El contenido**: el contingut és als **blocs de dades**; l'i-node hi apunta.
- **La lista de noms del pare**: això és el **directori** (un altre i-node, el del directori).

---

## P4 — Els 15 punterers de l'i-node

### Concepte

Amb blocs de 4096 B i punterers de 4 B (1024 punterers per bloc indirecte):

| # | Tipus | Blocs accessibles | Mida màxima |
|---|---|---|---|
| 1-12 | **Directe** | 12 | 48 KB |
| 13 | **Indirecte simple** | 1024 | ~4 MB |
| 14 | **Doble indirecte** | 1024² | ~4 GB |
| 15 | **Triple indirecte** | 1024³ | ~4 TB |

### Pregunta

En un i-node de FFS con bloques de 4096 bytes, ¿cuántos bloques lógicos puede direccionar un puntero indirecto simple?

- [x] **1024 bloques**
- [ ] 4096 bloques
- [ ] 12 bloques
- [ ] 256 bloques

### Per què la A sí

Un bloc de punteres de 4096 B amb punterers de 4 B → **4096 / 4 = 1024** punteres → 1024 blocs de dades.

### Per què les altres no

- **4096**: confuses els bytes del bloc amb el nombre de punteres.
- **12**: són els **punteres directes**.
- **256**: cap relació amb 4096/4.

> [!tip] Amb 12 directes el màxim és **48 KB**; sense els indirectes, un fitxer de 48 KB ja no cabria.

---

## P5 — Per què l'arbre de punteres és asimètric

### Concepte

L'arbre és **fix** (15 entrades, prefixat) i **asimètric**: els primers 48 KB es resolen amb **0 indireccions**, els següents amb **1**, després **2** i després **3**. Un fitxer petit no paga el cost d'una cadena llarga de punteres i un de gran té prou capacitat.

### Pregunta

¿Por qué el árbol de punteros del i-node se dice que es asimétrico?

- [x] **Porque cada nivel cubrece un rango muy distinto: 0 indirecciones para los primeros 48 KB, 1 después, 2 y 3 sucesivamente**
- [ ] Porque los punteros tienen tamaños distintos
- [ ] Porque algunos punteros apuntan a bloques y otros a i-nodes
- [ ] Porque el número de punteros directos varía según el archivo

### Per què la A sí

És la definició de classe: l'abast de cada tipus de punter és **molt diferent**, i el cost d'indireccions creix amb la mida del fitxer.

### Per què les altres no

- **Tamanys diferents**: tots els punteres són del mateix tamany (4 B).
- **Uns apunten a blocs, altres a i-nodes**: tots apunten a **blocs** (de dades o de punteres).
- **El nombre de directes varia**: no, és **fix** (12 sempre).

---

## P6 — FAT vs FFS: estructura

### Concepte

| | **FAT** (anys 70) | **FFS** (mitjans dels 80) |
|---|---|---|
| Estructura | **llista enlaçada** | **vectors** |
| Mida màx. fitxer | FAT32: 4 GiB − 1 B | Triple indirecte: ~4 TB |
| Ús avui | USB, targetes SD | Base d'ext3/ext4/NTFS |

### Pregunta

¿Qué diferencia estructural existe entre FAT y FFS?

- [x] **FAT almacena los bloques del archivo en una lista enlazada; FFS usa vectores (punteros en el i-node)**
- [ ] FAT usa vectores y FFS usa listas enlazadas
- [ ] Ambos usan listas enlazadas, pero FFS añade un índice
- [ ] No hay diferencia: FFS es simplemente una versión más reciente de FAT

### Per què la A sí

És la comparació central del tema (D27).

### Per què les altres no

- **Invertit**: és exactament al revés.
- **FFS amb índex**: FFS no té cap taula central; el "índex" és l'i-node.
- **No hi ha diferència**: FFS **neix** per resoldre les limitacions de la FAT.

---

## P7 — Per què la FAT té "accés aleatori pobre"

### Concepte

Limitacions de la **FAT** (T3-P1 §13):

- **Fitxers fragmentats** (l'algoritme del "següent bloc lliure" els escampa).
- **Accés aleatori pobre**: per arribar a un bloc cal **recórrer la llista enlaçada** de la taula FAT.
- **Directoris no ordenats**.
- **Control d'accés d'usuaris pobre** → sense seguretat.

### Pregunta

En un sistema de ficheros FAT, ¿por qué es dice que el acceso aleatorio es pobre?

- [x] **Porque para llegar a un bloque hay que recorrer la lista enlazada de la tabla FAT desde el primer bloque**
- [ ] Porque la tabla FAT ocupa demasiado espacio en disco
- [ ] Porque los bloques están comprimidos
- [ ] Porque no permite abrir ficheros de más de 4 GiB

### Per què la A sí

Definició de classe: cal **recórrer la cadena** → el cost creix amb la distància al bloc.

### Per què les altres no

- **Mida de la taula**: la mida és fixa i depèn de la capacitat del disc, no és el problema d'accés.
- **Compresió**: la FAT no comprimeix res.
- **4 GiB**: és un límit de mida de fitxer (FAT32), una altra limitació diferent.

---

## P8 — Escriptura i lectura: el mapeig lògic → física

### Concepte

L'usuari "veu" el fitxer **contigu**; els **i-nodes fan el mapeig** entre els **bytes lògics** i la **posició física**. El FS divideix la petició en blocs, llegeix cada bloc i els **uneix** en un sol vector, en ordre lògic.

Exemple de classe (`read(fd, vector, 4096*4)`): offsets 0–4095 → bloc 3 · 4096–8191 → bloc 1 · 8192–12287 → bloc 8 · 12288–16383 → bloc 4.

### Pregunta

Cuando el SO ejecuta read(fd, buf, 4*4096) sobre un fichero FFS, ¿qué hace?

- [x] **Divide la petición en bloques, lee cada bloque físico y los une en el vector en orden lógico**
- [ ] Copia el fichero entero en memoria y devuelve los últimos 16 KB
- [ ] Lee los 16 KB contiguos en el disco
- [ ] Devuelve un error, porque el tamaño de lectura no coincide con el bloque

### Per què la A sí

És el procediment descrit a classe (D22-23) i el que fa el FS.

### Per què les altres no

- **Copia tot el fitxer**: no, l'objectiu del sistema de fitxers és exactament evitar-ho.
- **Llegeix 16 KB contigus**: el fitxer **no és contiguctràgicament**; cal anar als blocs que diu l'i-node.
- **Error de mida**: la lectura pot ser de qualsevol mida; es llegeixen els blocs que calen.

---

## P9 — Localitzar un fitxer: /usr/ast/mbox

### Concepte

Passos (xifres de la figura D20):

1. Es coneix la posició del **directori arrel** → es busca l'entrada `usr`.
2. `usr` → **i-node 6**; l'i-node 6 diu que `/usr` és al **bloc 132**.
3. Al **bloc 132** es busca `ast`.
4. `ast` → **i-node 26**; diu que `/usr/ast` és al **bloc 406**.
5. Al **bloc 406** es busca `mbox`.
6. `mbox` → **i-node 60** → es llegeix l'i-node 60 i el fitxer queda obert.

### Pregunta

Al abrir el fichero /usr/ast/mbox, ¿cuántos i-nodes hay que leer antes de poder abrir el fichero?

- [x] **Tres: el de /usr, el de /usr/ast y el de mbox**
- [ ] Uno: el del fichero mbox
- [ ] Ninguno: el kernel mantiene todo en caché
- [ ] Cuatro: hay que leer también el i-node de la raíz

### Per què la A sí

Cal resoldre **tots els components del camí** (`usr` → `ast` → `mbox`): cada directori del camí és un fitxer amb la seva taula i el seu i-node.

### Per què les altres no

- **Un sol**: no es pot saber l'i-node de `mbox` sense trobar abans on és `ast` i `usr`.
- **Cap, per la caché**: la memòria cau és una optimització, no la garantia.
- **Quatre**: l'i-node de l'arrel es llegeix per trobar `usr`, però no és un i-node **del fitxer**; la resposta de classe són els tres del camí.

> [!warning] Errates dels apunts
> El text dels passos del PPT diu "**bloque 123**" i "**i-node 25**"; la **figura** diu **bloc 132** i **i-node 26** → segueix la figura.

---

## P10 — Espai lliure: bitmap vs taula FAT

### Concepte

- **FFS**: un **bitmap** a disc (*Free space mgmt*), on **cada bloc és 1 bit** (0 = lliure, 1 = ocupat), en **posició coneguda**. En una sola lectura es veu l'estat de tots els blocs i es pot triar un bloc **contigu**.
- **FAT**: es **recorre la taula** buscant un element no ocupat ("el següent bloc lliure") → **molta fragmentació**.

### Pregunta

¿Cómo busca espacio libre el FFS y en qué se diferencia de la FAT?

- [x] **Con un bitmap (1 bit por bloque) en una posición conocida; la FAT recorre la tabla buscando el siguiente bloque libre**
- [ ] La FAT usa un bitmap y el FFS recorre la tabla
- [ ] Ambos recorren la tabla, pero el FFS busca bloques contiguos
- [ ] El FFS no gestiona el espacio libre: lo hace el hardware

### Per què la A sí

És la comparació dels dos mètodes (D25 vs T3-P1 §12).

### Per què les altres no

- **Invertit**: és al revés.
- **Els dos recorren la taula**: el FFS **no** té taula FAT; té bitmap.
- **El hardware**: no, és cosa del sistema de fitxers.

---

## P11 — Heurística de localitat

### Concepte

Al disc magnètic es divideix en **grups** (*block groups*); cada grup conté les **metadades** (i-nodes, directoris, bitmap). Un **directori concret** s'associa a un **grup concret** i el FFS hi posa els fitxers → metadades i dades **físicament a prop** → el braç del disc es mou menys (cada salt té un cost mecànic: *seek* + latència de rotació).

### Pregunta

¿Por qué el FFS agrupa los archivos de un directorio en el mismo block group?

- [x] **Para que sus metadatos y sus datos estén físicamente cerca y el brazo del disco se mueva menos (menos seeks)**
- [ ] Para que los archivos del mismo directorio sean idénticos
- [ ] Para reservar espacio de forma más rápida
- [ ] Para poder comprimir mejor los datos

### Per què la A sí

És l'**heurística de localitat** (D26): el guany no és la capacitat, és el **salt** del braç.

### Per què les altres no

- **Idèntics**: no tenen res a veure.
- **Reserva més ràpida**: és la feina del **bitmap**.
- **Compressió**: cap relació.

---

## P12 — Journaling vs Copy-on-Write

### Concepte

- **Journaling**: escriu primer un **registre d'intenció** dels metadades per poder **refer-los** si hi ha un tall o una avaria → evita la **pèrdua de consistència**.
- **Copy-on-Write**: **mai sobreescriu** el bloc existent: en escriu una còpia nova i després actualitza el punter → conserva **versions anteriors** com a còpies de seguretat (ex. **BTRFS**).

### Pregunta

¿Cuál es la diferencia de objetivo entre journaling y copy-on-write?

- [x] **Journaling asegura la consistencia de los metadatos tras un corte; COW conserva versiones anteriores al no sobrescribir nunca**
- [ ] Journaling es más rápido y COW más seguro
- [ ] Son dos nombres para lo mismo
- [ ] COW solo funciona en discos SSD

### Per què la A sí

És la pregunta literal del PPT (D28) i la resposta dels apunts.

### Per què les altres no

- **Velocitat vs seguretat**: no és una comparació de velocitat; són **objectius diferents**.
- **Són el mateix**: tenen mecanismes diferents i objectius diferents.
- **Només SSD**: el COW és un disseny de sistema de fitxers (BTRFS és el cas de referència).

---

## P13 — Esborrar vs truncar

### Concepte

- **Esborrar**: elimina l'entrada dels **metadades del directori** i **llibera tot l'espai** que ocupava al disc.
- **Truncar**: redueix l'espai que ocupa un fitxer **sense esborrar-lo**; continua existint amb els seus metadats.

### Pregunta

¿Qué diferencia hay entre borrar y truncar un fichero?

- [x] **Borrar elimina la entrada del directorio y libera el espacio; truncar reduce el espacio sin borrar el fichero**
- [ ] Son exactamente la misma operación
- [ ] Truncar borra el fichero y borrar solo libera espacio
- [ ] Truncar solo funciona con ficheros de menos de 4 KB

### Per què la A sí

Definició de classe (T3-P1 §8).

### Per què les altres no

- **El mateix**: no, una elimina el fitxer i l'altra no.
- **Invertit**: és al revés.
- **4 KB**: truncar funciona amb qualsevol mida.

> [!tip] Fitxer *sparse* (de l'exercici de classe)
> `truncate -s 100M reserva.bin` deixa el fitxer amb **100 MiB de mida lògica** i **0 blocs assignats** → `stat` mostra *Size* 100M i *Blocks* 0; `du` mostra 0. Els bytes sobrants d'un bloc **no** els pot aprofitar cap altre fitxer.

---

## P14 — SSD: wear leveling i per què FAT/FFS no hi serveixen

### Concepte

- L'**SSD** no té parts mòvils → **accés aleatori molt ràpid** i **mateix model lògic** (blocs, sectors, particions).
- En un SSD, abans d'escriure en un bloc **cal esborrar-lo** (a diferència de l'HDD).
- Els FAT i FFS "tal com" s'usen en discs magnètics **no són adequats**: accedeixen sempre a les **mateixes posicions físiques** → **degrada ràpidament** l'electrònica.
- Solucions: **wear leveling** (repartir les escriptures per tota la memòria) i **log-structured filesystems**.
- Altres tècniques de classe: **TRIM** (el SO informa de quins blocs ja no s'usen) i **garbage collection**.

### Pregunta

¿Qué problema presentan los sistemas de ficheros FAT y FFS al usarse en un SSD?

- [x] **Que acceden siempre a las mismas posiciones físicas, degradando rápidamente la electrónica de la memoria flash**
- [ ] Que no pueden direccionar archivos de más de 4 GiB
- [ ] Que el SSD no soporta el acceso aleatorio
- [ ] Que necesitan sectoras de 512 bytes y el SSD usa de 4096

### Per què la A sí

És la resposta literal del PPT (D29) i dels apunts.

### Per què les altres no

- **4 GiB**: és el límit de mida de fitxer de la FAT32, no un problema del SSD.
- **El SSD no suporta accés aleatori**: és al revés, és el que el fa **molt ràpid**.
- **Sectores**: és un problema de *tamaño de sector*, no d'activació del medi.

> [!warning] *Wear leveling* = **durabilitat**, no rendiment. En l'actualitat el fa la FTL del SSD; a l'examen, explica'l amb el PPT (repartir les escriptures).

---

## P15 — MBR

### Concepte

El **Master Boot Record** és el **sector d'arrencada** del disc (de vegades ocult) amb **dades crítiques d'arrencada que viuen fora del sistema de fitxers**, incloent-hi la **taula de particions**:

- **Tipus** de partició
- **Mida** (inici i fi)
- **Configuració** (active / no active)

En arrencar, la **BIOS** localitza el MBR per carregar el SO o el menú d'arrencada. Alternatives: **GPT**.

### Pregunta

¿QUÉ contiene el Master Boot Record (MBR)?

- [x] **El código de arranque y la tabla de particiones (tipo, tamaño, active)**
- [ ] El contenido del primer directorio del sistema de ficheros
- [ ] La tabla FAT completa
- [ ] Una copia de seguridad de los i-nodes

### Per què la A sí

Definició de classe (T3-P1 §14).

### Per què les altres no

- **El directori arrel**: el MBR viu **fora** del sistema de fitxers.
- **La taula FAT**: la FAT és **dins** la partició, no al MBR.
- **Còpia dels i-nodes**: no hi ha cap còpia de seguretat al MBR.

---

## P16 — Metadades: què en desa el sistema de fitxers

### Concepte

A més del contingut, cal guardar **metadades** que permetin localitzar, gestionar i protegir els fitxers:

- **Mida i ubicació** de les dades
- **Propietari i permisos** d'accés
- **Dates** de modificació, accés i creació

Cada directori té els **seus propis** metadades. Comandes útils: `ls -l` · `stat` (mostra els **blocs assignats**) · `getfacl` · `du` · `df -h` · `file`.

### Pregunta

¿Qué información se almacena como metadatos de un fichero?

- [x] **Tamaño y ubicación de los datos, propietario, permisos y fechas**
- [ ] Solo el nombre y la extensión
- [ ] El contenido completo del fichero
- [ ] Un hash del contenido para detectar cambios

### Per què la A sí

És la llista de classe (T3-P1 §6).

### Per què les altres no

- **Nom i extensió**: l'extensió és una **convenció**; el sistema reconeix el contingut pels *magic bytes* (`file`).
- **El contingut**: això són les dades, no els metadades.
- **Hash**: no en mana cap el sistema de fitxers del curs.

---

## P17 — Defragmentació: què fa i què NO fa

### Concepte

La **defragmentació** reorganitza els blocs d'un fitxer perquè quedin **contigus** (5 salts → 1).

- **Es conserva el contingut i l'ordre** → no es toca el fitxer, només on és.
- **No augmenta l'espai lliure** → no s'elimina cap bloc, només es reordenen.
- A l'**HDD** redueix els desplaçaments del capçal; en un **SSD** **no serveix de res** (no hi ha braç ni latència de rotació).

### Pregunta

Tras defragmentar un fichero en un disco duro, ¿qué cambia?

- [x] **Solo la ubicación física de sus bloques: pasa a estar fragmentado a contiguo (menos seeks)**
- [ ] El contenido del fichero, que se comprime
- [ ] El tamaño del fichero, que se reduce
- [ ] Se libera espacio en disco

### Per què la A sí

Les tres idees del PPT (D51): contingut i ordre intactes, espai igual, menys desplaçaments del capçal.

### Per què les altres no

- **Comprimeix**: el contingut no canvia.
- **Es redueix la mida**: no, ni el contingut ni la mida canvien.
- **Allibera espai**: no, **no s'elimina cap bloc** → l'espai lliure és el mateix.

---

## P18 — Oberta: per què "Fast" File System

### Concepte

Al disc magnètic cada **salt** té un **cost mecànic** (*seek* + latència de rotació). Si els blocs d'un mateix fitxer (i les seves metadades) són **contigus**, el braç recorre menys distància i hi ha **menys seeks** → el sistema és més ràpid. D'aquí el nom *Fast File System*.

### Pregunta

¿Por qué se llama "Fast" al FFS? ¿Qué tiene que ver la localidad con la velocidad?

### Resposta esperada

- El guany **no** és la capacitat ni la velocitat de còpia: és el **cost dels salts**.
- La **localitat** (directori i fitxers del mateix grup, blocs contigus) fa que el braç es mogui menys.
- El FFS combina **aïllament** (vectors) amb **localitat** (block groups) → de les dues limitacions de la FAT resol la **fragmentació** i millora el **accés aleatori**.

---

## Fitxa ràpida — Tema 3

| Concepte | Clau |
|---|---|
| **Fitxer** | Col·lecció ordenada de dades, permanent (no volàtil); abstracció del SO |
| **Directori** | Fitxer-taula; **no conté les dades**, sinó les entrades |
| **Sector** | Unitat mínima del **disc** (512 B típic) |
| **Bloc** | Unitat mínima del **SO** (1024–8192; Intel 4096) |
| **HDD** | Un sol braç → una operació a la vegada; contigu **10x més ràpid** |
| **SSD** | Flash NAND, sense parts mòvils, esborra abans d'escriure; wear leveling / TRIM / GC |
| **Metadades** | Mida i ubicació, propietari i permisos, dates |
| **Truncar vs esborrar** | Truncar = reduir sense esborrar · esborrar = treure metadades + llibera blocs |
| **FAT** | Anys 70; **llista enlazada**; fragmentació, accés aleatori pobre, sense control d'accés |
| **FFS** | Mitjans dels 80; **vectors**; base d'ext3/ext4/NTFS |
| **Estructura FFS** | `Boot block` · `Superblock` · `Free space mgmt` · `I-nodes` · `Root dir` · dades |
| **I-node** | Mida fixa + ID; atributs + punterers; **1 per cada 16 KB** de disc |
| **15 punterers** | 12 directes (48 KB) · 1 indirecte (~4 MB) · 1 doble (~4 GB) · 1 triple (~4 TB) |
| **Arbre** | **Fix** i **asimètric** (0/1/2/3 indireccions segons la mida) |
| **Mapeig lògic-físic** | L'usuari veu el fitxer contigu; l'i-node tradueix rang de bytes → bloc |
| **Espai lliure** | FFS: **bitmap** (1 bit/bloc) · FAT: recorre la taula → fragmentació |
| **Localitat** | **Block groups**; directori ↔ grup → menys *seek* |
| **Millores FFS** | Arbres balancejats als directoris · **journaling** (consistència) · **COW** (versions) |
| **MBR** | Sector d'arrencada amb la **taula de particions**; la BIOS el localitza |

---

## Dubtes / a revisar

- **Època del FFS**: el PDF Parte 1 diu "mitjans dels **90**" i el Parte 2 diu "mitjans dels **80**" → el **80** és el correcte (4.3BSD, 1986) i el que diu el professor a la Parte 2.
- **P9**: les xifres de la **figura** (bloc 132, i-node 26) prevalen sobre les errates del text del PPT.
- **P14**: *wear leveling* = durabilitat; la resposta ha de seguir el PPT (repartició de les escriptures).
- **P18**: és una pregunta oberta del PPT → la resposta ha de lligar els **salts** amb la **localitat**.
- **Problema 1e** del parcial 2025-2026 (depèn de la mida de clúster) i **2f-g** (contenidors vs MVs · virtualització vs emulació) són a [[T3-Sistemes-Fichers-P2#17. Examen parcial 2025-2026 (D41-44)|T3-P2 §17]] i a [[Qüestions-T2-MV-Contenidors|Qüestions T2]].

---

## Enllaços relacionats

- [[T3-Sistemes-Fichers-P1|T3 — Sistemes de fitxers (Parte 1)]]
- [[T3-Sistemes-Fichers-P2|T3 — Sistemes de fitxers (Parte 2)]]
- [[Tests-Unidad-SO|Tests d'unitat]] (Test 3 = conceptes d'aquest tema)
- [[Qüestions-T1-Seguretat|Qüestions T1 — Seguretat]]
- [[Qüestions-T2-MV-Contenidors|Qüestions T2 — MV i Contenidors]]
- [[Respostes-Parcial1-SO2-26-27|Respostes Parcial 1 SO2 (2026-2027)]]
- [[_Index_SO|Índex Sistemes Operatius I]]
