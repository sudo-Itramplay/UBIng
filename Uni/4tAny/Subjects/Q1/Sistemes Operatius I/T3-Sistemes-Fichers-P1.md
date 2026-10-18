---
id: T3-Sistemes-Fichers-P1
aliases: []
tags:
  - tipus/teoria
  - assignatura/SO
assignatura: SO
data: "2026-10-17"
---

# T3 — Sistemes de fitxers (Parte 1)

**Referència: PDF 03 — Sistemas de ficheros (Parte 1)**

---

## 1. Test ràpid del bloc anterior (MV / contenidors)

- Test del Campus Virtual (15:15-15:30) sobre el bloc de virtualització; autoavaluació abans d'entrar en sistemes de fitxers

> [!question]- P1 · Quina afirmació descriu millor una màquina virtual?
> **b) Un sistema que emula *hardware* per executar SOs convidats.** (a) és un compilador; (c) descriu més aviat el paper del hypervisor sobre crides al SO, no la MV; (d) és un contenidor, no una MV

> [!question]- P2 · Quin component de la MV assigna i gestiona els recursos físics del host?
> **b) Hypervisor o *Virtual Machine Manager* (VMM).** El SO *guest* (a) gestiona el seu entorn virtual; Docker Engine (d) és de contenidors

> [!question]- P3 · En virtualització, en què consisteix el mecanisme *trap-and-emulate*?
> **a) Interceptar les instruccions privilegiades i executar-les a l'hipervisor.** Les instruccions privilegiades del guest provoquen una *trap*; l'hipervisor les emula i retorna el resultat

> [!question]- P4 · Quina afirmació és INCORRECTA sobre els contenidors?
> **c) Simulen *hardware* complet.** És fals: els contenidors **comparteixen el kernel** del SO host (a vertader), són més lleugers que les MVs (b vertader) i fan servir *namespaces* i *cgroups* (d vertader)

> [!question]- P5 · Quin avantatge principal ofereixen els contenidors vs les MVs en desenvolupament?
> **b) Arrencada més ràpida i menor consum de recursos.** (a) i (d) són avantatges de les MVs; (c) no aplica

> [!question]- P6 · Quina diferència hi ha entre *docker image* i *docker container*?
> **d) La imatge és la plantilla; el contenidor és la seva instància en execució.** (Directament de les definicions de la T2b)

---

## 2. Objectius de la sessió

- Repassar els conceptes clau de **directoris i fitxers**
- Descriure diversos **dispositius d'emmagatzematge**
- Comprendre els principis dels **sistemes de fitxers**
- Analitzar les característiques dels **sistemes de fitxers FAT**

**Avís important:** canvi d'aula per al parcial → **B2 i B3**

---

## 3. Ficheros: abstracció del SO

- Dels fitxers i els directoris s'emmagatzemen habitualment al **disc**; l'usuari treballa amb fitxers i directoris i pensa que són **dades lineals**, quan al disc no és així

> [!question]- Ràpid: quina diferència hi ha entre un *fichero* i un *directori*? I entre un *fichero* i un *archivo*?
> - **Fitxer vs directori**: el **fitxer** és una col·lecció ordenada de dades amb relació entre si, emmagatzemada permanentment; el **directori** **no conté les dades** dels fitxers — conté les **entrades** que permeten trobar-los (noms → metadades + apuntadors). Cada directori té els seus propis metadades (permisos, dates).
> - **Fitxer vs archivo**: **sinònims**. El PPT diu literalment "*un fichero (o archivo) és una col·lecció ordenada de dades*" — canvia el terme segons la variant d'espanyol, el concepte és el mateix

### Definició de fitxer

- Un **fitxer** (o **arxiu**) és una **col·lecció ordenada de dades** amb relació entre si, emmagatzemada de forma **permanent** en un dispositiu de memòria **no volàtil**
- Aquestes dades **permaneixen al mitjà** (salvo catàstrofe) i continuen existint després que el programa que les va crear deixi d'executar-se, fins i tot després d'un **reinici**
- Aquesta és la **diferència amb les dades de la memòria RAM** (volàtil): no sobreviuen al programa ni a la desconnexió

### El fitxer és una abstracció del SO

- El concepte de fitxer és una **abstracció del SO** que, de forma **transparent al programador**, utilitza els recursos del *hardware* creant-hi per sobre una **estructura lògica**
- El SO crea tot el **sistema de fitxers** de l'ordinador: directoris per organitzar-los, taules per localitzar-los al disc, etc.
- El SO proporciona **serveis** per al maneig de fitxers: obrir, tancar, llegir, escriure, eliminar

---

## 4. Sistema de fitxers (file systems)

- Un **sistema de fitxers** és l'element del SO que **controla/gestiona** de forma transparent la **informació** associada a **fitxers i directoris**
- Sense aquest sistema, les dades al serien un **gran cos de dades** sense saber on acaba una dada i comença la següent
- La majoria de SOs utilitzen el seu **propi** sistema de fitxers

> [!question]- Ràpid: com s'emmagatzema la informació dels fitxers? I la dels directoris? I com es gestiona l'espai lliure?
> Respostes que dona el PPT més endavant (veure seccions [[#10. Fonaments de disseny]] i [[#12. El sistema FAT en detall]]):
> - **Fitxers**: **contigus o no contigus** als disc. FAT = **llista enlazada** (blocs no contigus); FFS = **vectors** (apunta a blocs contigus, millor rendiment). Idealment contigus
> - **Directoris**: cada directori s'emmagatzema com un **fitxer amb una estructura de taula** (llistat d'entrades: noms, mida, permisos, apuntadors als blocs; i entrades per subdirectoris)
> - **Espai lliure**: el sistema ha de saber quins blocs són lliures (a FAT: recórrer la **taula FAT** buscant elements no ocupats, marcats amb un **codi especial**); si són contigus, millor

### A tenir en compte

- El problema d'emmagatzemar, recuperar o manipular informació **no és trivial** → hi ha **múltiples solucions**
- **No hi ha una forma "correcta"** d'implementar un sistema de fitxers (**trade-off**) → depèn del dispositiu d'emmagatzematge o de les aplicacions

---

## 5. Dispositius d'emmagatzematge

### Una mica d'història

- **1956**: disc dur de **5 MB** a **3.000$/mes** (avui ~30.000$) — [vídeo (3 min)](https://www.youtube.com/watch?v=yS0oRIX8sJM)

### Sector vs bloc

> [!important] **Clau per entendre tota la resta**
> - **Sector de disc**: **unitat mínima** que el disc pot **llegir o escriure** (típicament **512 bytes**)
> - **Bloc del sistema de fitxers**: **unitat mínima** que el SO **llegeix o escriu**. **Totes** les operacions del sistema de fitxers es fan sobre blocs
> - Un bloc del sistema de fitxers té el **mateix tamany o un múltiple** del sector. Són comuns blocs de **1024, 2048, 4096 o 8192 bytes**; Intel utilitza un bloc de **4096 bytes**

### Disc dur magnètic (HDD)

- Format per diversos **discos** (*platters*) col·locats un sobre l'altre; s'escriuen per **ambdues cares**
- Existeix un **únic braç mecànic** amb un capçal de lectura a cada cara del disc → només **una operació** de lectura/escriptura **en un instant**; no es poden llegir/varis discs a la vegada
- Llegir/escriure **sectors contigus** és una operació **més ràpida (10x)** que sobre sectors **no contigus** — perquè el braç s'ha de **moure** (seeks) entre pistes
- Molts fabricants (Seagate, WD, Toshiba), cadascú amb la seva **geometria** (nombre de discs, sectors...)
- **Controlador de disc** integrat al *hardware*: el **gestor de disc** (*driver*) es comunica amb ell per gestionar les operacions indicades pel SO
- **Emmagatzematge lògic**: el *driver* ve el disc com un **dispositiu d'emmagatzematge lineal**; en accedir a una adreça lògica, el controlador **tradueix** l'adreça a la **posició física** del disc

### Disc d'estat sòlid (SSD)

- **Sense parts mòviles**; les dades s'emmagatzemen en circuits elèctrics (**memòria flash NAND**) que es **degraden** amb el temps → calen tècniques específiques per assegurar la **durabilitat**
- **Mateix model lògic** que els HDD (blocs, sectors, particions) → accés més **ràpid** i major **resistència a cops**
- **Escriptura més lenta**: abans d'escriure en un bloc de disc **cal esborrar-lo** (no passa amb els HDD)

> [!question]- SSD: com assegurem la durabilitat si els blocs es degraden i cal esborrar-los abans d'escriure?
> - **Wear leveling**: **distribueix** les escriptures evitant escriure sempre als mateixos sectors
> - **TRIM**: el SO informa el SSD de quins blocs **ja no es fan servir**, mantenint el rendiment
> - **Garbage collection**: gestiona **caché, errors i borrats** automàtics

---

## 6. Requisits d'un sistema de fitxers: metadades i directoris

- Per emmagatzemar fitxers i directoris, a més del **contingut**, cal guardar informació que permeti **localitzar, gestionar i protegir** els fitxers: els seus **metadades**
  - **Mida i ubicació** de les dades
  - **Propietari** i **permisos** d'accés
  - **Dates** de modificació, accés i, quan s'admet, de **creació**
- Els fitxers s'organitzen en **directoris**, que relacionen els **noms** amb els fitxers i subdirectoris que contenen; cada directori té els seus propis metadades (permisos, dates)
- Un directori **no conté necessàriament les dades** dels fitxers → conté les **entrades** que permeten trobar-los

### Comandes per consultar metadades (Linux)

| Comanda | Què mostra |
|---|---|
| `ls -l` | Permisos, nombre d'enllaços, propietari, grup, mida i data de modificació |
| `stat fitxer` | Metadades detallats: identificador, mida, **blocs assignats**, permisos i dates |
| `lsattr fitxer` | Indicadors especials a Linux, com *immutable* o *solo añadir* |
| `getfacl fitxer` | **Llista de control d'accés (ACL)**: permisos per a usuaris i grups |
| `getfattr -d fitxer` | **Atributs estesos** a Linux; per defecte, els de l'espai *user* |
| `file fitxer` | Identifica el **tipus de fitxer** mitjançant proves, incloent l'anàlisi del contingut |
| `du -sh directori` | Estima l'**espai ocupat** pel directori i el seu contingut |
| `df -h` | Espai total, utilitzat i disponible dels **sistemes de fitxers muntats** |

---

## 7. Exercici: quant ocupa realment un fitxer?

```bash
mkdir -p ~/practica-tamaños
cd ~/practica-tamaños
printf 'Hola, sistemas operativos\n' > mensaje.jpg
truncate -s 100M reserva.bin
ls -lh mensaje.jpg reserva.bin
stat mensaje.jpg reserva.bin
du -h mensaje.jpg reserva.bin
du -h --apparent-size mensaje.jpg reserva.bin
df -h .
file mensaje.jpg reserva.bin
```

> [!quote] "*Un archivo puede medir 100 MiB de **tamaño lógico**, tener asignados 0 **bytes para sus datos** y estar en un sistema de ficheros con 20 GiB de **espacio disponibles**. Su extensión **NO** garantiza su contenido.*"

> [!question]- Exercici: 1. `mensaje.jpg` conté una imatge? 2. `reserva.bin` ocupa realment 100 MiB? 3. Quin comandament diria quant espai queda disponible?
> 1. **No.** Conté el text *"Hola, sistemas operativos"* — **l'extensió no garanteix el contingut**. Ho confirma `file mensaje.jpg` (el tipus es detecta pel contingut, no per l'extensió)
> 2. **No.** `truncate` reserva espai **lògic** (*sparse file*): ocupa 100 MiB de **mida lògica** però pot tenir **0 bytes assignats** per a les seves dades reals. Es veu amb `du -h` (espai real, ~0) vs `du -h --apparent-size` (100 MiB) i amb els **blocs assignats** de `stat`
> 3. **`df -h`** — mostra l'espai total, utilitzat i disponible del sistema de fitxers

> [!question]- Exercici: mida lògica? Espai assignat? Espai disponible? Quin tipus de contingut reconeix el sistema?
> - **Mida lògica**: `mensaje.jpg` ~24 bytes; `reserva.bin` **100 MiB**
> - **Espai assignat**: `mensaje.jpg` ocupa un bloc real (petit); `reserva.bin` **0 bytes** de dades reals
> - **Espai disponible**: el que mostri `df -h .` (a l'exemple del PPT, 20 GiB)
> - **Tipus** (`file`): `mensaje.jpg` → **text**; `reserva.bin` → **buit / dades buides** — res a veure amb les extensions

---

## 8. Operacions sobre fitxers i directoris

### Operacions sobre fitxers

- **Crear**: el sistema ha de trobar **ràpidament** espai lliure al disc per al fitxer
- **Escriure**: donat el nom, el sistema ha de trobar la **ubicació** del fitxer al disc i permetre-hi escriure
- **Llegir**: un cop trobada la ubicació, s'han de poder **llegir** les dades
- **Posicionament**: permetre posicionar el punter de lectura/escriptura a **qualsevol punt** del fitxer
- **Esborrar**: elimina l'entrada dels **metadades del directori** i **llibera tot l'espai** que ocupava al disc
- **Truncar**: redueix l'espai que ocupa un fitxer (a una longitud específica) **sense esborrar-lo**; continua existint amb els seus metadades

### Operacions sobre directoris

- **Buscar un fitxer**: trobar-lo per accedir als seus metadades
- **Crear un fitxer**: afegir nous fitxers a un directori
- **Esborrar un fitxer**: eliminar l'entrada del directori (i els seus metadades)
- **Renombrar un fitxer**: canviar el nom de l'entrada al directori
- **Llistar el contingut**: llistar els fitxers (i subdirectoris) que conté

---

## 9. Nivell físic

- Als **blocs de disc** s'emmagatzemen els fitxers i els seus metadades
- Ocupen un **nombre sencer de blocs**; els bytes d'un bloc no utilitzats pel fitxer **no poden ser utilitzats** per altres fitxers
- **No es pot llegir un byte** d'un fitxer: cal llegir **tot el bloc**, portar-lo a memòria i accedir al byte demanat
- En manipular fitxers, els bytes es "veuen" de forma **contínua/lineal**, però els fitxers (**i els seus metadades**) **no tenen per què estar contigus** físicament al disc
- **Idealment**, els blocs d'un fitxer serien **contigus** al disc → millor **rendiment** del disc magnètic

---

## 10. Fonaments dels dissenys implementats

- Al llarg de l'evolució dels sistemes de fitxers hi ha hagut **diverses formes** d'implementar-ho; aquí, només els **principis**
- Reptes: com implementar que un fitxer **no estigui emmagatzemat en blocs contigus**, i com **accedir de forma eficient** a un bloc de fitxer fent-ho **escalable** a fitxers grans i petits

### Directoris com a taules

- Fem servir **estructures jeràrquiques** de directoris
- **Cada directori s'emmagatzema al disc com un fitxer** amb una estructura similar a una **taula** que:
  - Conté el **llistat** de fitxers, amb la **mida**, els **permisos**, ... i un **apuntador** cap als **blocs** del fitxer
  - Cada directori pot contenir **subdirectoris**: per a cada subdirectori hi ha un **apuntador** cap al fitxer que conté els fitxers del subdirectori
- "¿Com gestionem aquestes taules de forma eficient? No és una tasca senzilla..."

### Espai lliure i localitat

- El sistema ha de saber **quin blocs són lliures** — i si són **contigus**, millor
- S'ha d'intentar **evitar la fragmentació** d'un fitxer
- La **heurística de localitat**: als discs magnètics, els **directoris** (les taules) i els **fitxers** que conté haurien d'estar **físicament propers**

### Disseny ideal (resum)

- **Accés eficient** a un bloc: blocs **contigus** (evitar moure el braç)
- Un **lloc al disc** per als **metadades** (mida en bytes, data de creació) i els apuntadors als blocs
- **Escalable** per a fitxers petits i grans

---

## 11. Principis bàsics: FAT i FFS

| | **FAT** (File Allocation Table) | **FFS** (Unix Fast File System) |
|---|---|---|
| Època | Finals dels **70** | Mitjans dels **90** |
| Ús avui | Memòries USB, targetes SD (simplicitat) | Base d'**ext3, ext4, NTFS** |
| Estructura | **Llista enlazada** dels blocs d'un fitxer | **Vectors** dels blocs d'un fitxer |

---

## 12. El sistema FAT en detall

- Desenvolupat per **Microsoft a finals dels 1970**; per a **MS-DOS** i les primeres versions de **Windows**
- Millorat anys enrere per donar suport a la gran capacitat d'emmagatzematge actual
- Avui: discs i memòries **USB**, **targetes de memòria** de càmeres fotogràfiques, etc.

### Estructura (en localitzacions conegudes pel sistema)

- La **taula FAT**: taula que es fa servir com **llista enlazada**; emmagatzema la informació dels **blocs** que formen cada fitxer
- El **directori arrel**: el (primer) bloc del directori arrel; la seva **posició és coneguda** pel sistema
- **Fitxers i directoris**: on s'emmagatzemen; es va **omplint** a mesura que s'afegeixen dades

### La taula FAT

- Taula d'**enters** que emmagatzema, en forma de **llista enlazada**, els blocs dels fitxers
- La **mida de la taula és fixa**: depèn de la **capacitat del disc**
- Exemple: el fitxer A ocupa els blocs **4, 7, 2, 10 i 12**; el fitxer B, els blocs **3, 11 i 14**
- Els **blocs buits** i el "**final**" d'un fitxer es **marquen amb un codi especial**

### Directoris de la FAT

- Cada directori és un **fitxer** que emmagatzema una **taula (no ordenada)** dels fitxers que el componen:
  - **Metadades**: mida en bytes, data de creació, ...
  - El **primer índex** de la llista enlazada (per al fitxer A, el **4**; per al B, el **6**)
- Per als **subdirectoris**, una entrada cadascun que apunta al fitxer que emmagatzema el contingut del subdirectori

### Espai lliure i fragmentació

- Per trobar **espai lliure** per a un fitxer nou, el sistema **recorre la taula FAT** buscant un element **no ocupat** (marcat amb un codi especial)
- Algoritmes **molt senzills**: es busca a la taula "el **següent** bloc lliure" → els fitxers poden quedar **molt fragmentats**
- Els sistemes FAT inclouen un **defragmentador**: programa que **mou les dades** al disc per aconseguir que els fitxers estiguin **contigus**

---

## 13. Limitacions del sistema FAT

- **Fitxers fragmentats**: l'estratègia fa que els fitxers acostumin a estar molt fragmentats
- **Accés aleatori pobre**: per accedir a un bloc cal **recórrer la llista enlazada** de la taula FAT
- **Taula de fitxers d'un directori**: el llistat **no està ordenat**; amb milers de fitxers seria poc eficient
- **Control d'accés pobre**: no permet controlar l'accés a diferents usuaris
- **Seguretat**: no incorpora sistemes de seguretat dels sistemes moderns (ex: protecció contra **corrupció** de disc si el sistema es penja)

---

## 14. Arrencada: MBR

> [!question]- Pregunta d'un alumne (curs anterior): com arrenca el SO sense el sistema de fitxers?
> A la **partició *boot*** s'indiquen els ***paths*** per arrencar. A més, les dades crítiques d'arrencada viuen **fora** del sistema de fitxers: al **Master Boot Record (MBR)**

### Master Boot Record (MBR)

- **Dades crítiques** emmagatzemades al **sector d'arrencada** del disc (sector especial, de vegades **ocult**) que conté una **taula de particions**:
  - **Tipus** de partició
  - **Mida** (inici i fi)
  - **Configuració** (active / no active)
- En **arrencar**, la **BIOS** localitza el **MBR** per carregar el SO o el **menú d'arrencada**
- Existeixen altres taules de particions, com les **GUID (GPT)**

Veure [procés BIOS/MBR (neosmart)](https://neosmart.net/wiki/mbr-boot-process/)

---

## 15. En resum (del professor)

- Els **sistemes de fitxers** gestionen l'organització de **fitxers i directoris**
- En general, els SOs disposen d'un **sistema de fitxers** propi
- Els sistemes de fitxers **varien** segons el **dispositiu d'emmagatzematge** o l'aplicació
- Els sistemes **FAT** són **senzills** d'implementar però tenen **limitacions**
- Moltes de les limitacions vistes es redueixen amb els sistemes de fitxers **FFS**

---

## Preguntes del PPT (índex ràpid)

| # | Pregunta | On |
|---|---|---|
| Test P1-P6 | Test del bloc de virtualització (MV/contenedors) | [[#1. Test ràpid del bloc anterior (MV / contenidors)]] |
| Ràpid | Fitxer vs directori · fitxer vs archivo | [[#3. Ficheros: abstracció del SO]] |
| Ràpid | Com s'emmagatzemen fitxers, directoris i espai lliure? | [[#4. Sistema de fitxers (file systems)]] |
| SSD | Com assegurar la durabilitat dels blocs? | [[#5. Dispositius d'emmagatzematge]] |
| Exercici | Quant ocupa realment un fitxer? (3 preguntes + anàlisi) | [[#7. Exercici: quant ocupa realment un fitxer?]] |
| Alumne | Com arrenca el SO sense el sistema de fitxers? | [[#14. Arrencada: MBR]] |

---

## Resum ràpid (FITXA)

| Concepte | Clau |
|---|---|
| **Fitxer** | Col·lecció ordenada de dades, permanent (no volàtil); **abstracció del SO** |
| **Sistema de fitxers** | Element del SO que controla/gestiona fitxers i directoris; sense ell, un gran cos de dades sense estructura |
| **Directori** | **No conté les dades** — conté **entrades** que permeten trobar-les (fitxers com a taules) |
| **Sector** | Unitat mínima de **disc** (típic **512 bytes**) |
| **Bloc** | Unitat mínima del **SO** (múltiple del sector: 1024-8192; Intel **4096**) |
| **HDD** | Platters + **únic braç mecànic** → una operació alhora; contigu **10x més ràpid** |
| **Emmagatzematge lògic** | El *driver* ve el disc **lineal**; el controlador tradueix adreça lògica → física |
| **SSD** | Flash NAND, **sense parts mòviles**, mateix model lògic; **esborrar abans d'escriure**; wear leveling / TRIM / garbage collection |
| **Metadades** | Mida i ubicació, propietari i permisos, dates |
| **Truncar vs esborrar** | Truncar = reduir mida **sense esborrar**; esborrar = treure metadades + **llibera blocs** |
| **Nivell físic** | Blocs **sencers**; no es llegeix un byte sinó tot el bloc; contigus = millor rendiment |
| **Heurística de localitat** | Directoris i fitxers **físicament a prop** |
| **FAT** | Finals 70s, **llista enlazada**; USB/SD; senzilla però fragmentació, accés aleatori pobre, sense control d'accés ni seguretat |
| **FFS** | Mitjans 90s, **vectors**; base d'ext3/ext4/NTFS |
| **MBR** | Sector d'arrencada amb **taula de particions** (tipus, mida, active); la BIOS el localitza per arrencar; alternativa **GPT** |

---

## Dubtes / a revisar

- **Test P1-P6**: respostes deduïdes del contingut de T2/T2b (no venen marcades al PDF); el professor les va donar al test — confirmar si alguna és altra
- **"Ràpid" de fitxers/directoris/espai lliure**: les respostes s'anticipen des del contingut de FAT/FFS del mateix PPT; si el professor en volia més (ex. *bitmap* d'espai lliure), afegir-ho
- Exercici de mida: provar-lo a la VM quan toqui el taller ("Luego haremos un ejercicio en la máquina virtual…")

---

## Enllaços relacionats

- [[T2b-Contenedors-Docker|T2b — Contenedors i Docker (Parte 2)]]
- [[T2-Maquines-Virtualitzacio-SO|T2 — MV i virtualització]]
- [[T1-Introduccio-Seguretat-SO|T1 — Introducció Seguretat SO]]
