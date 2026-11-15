---
id: T3-Sistemes-Fichers-P2
aliases: []
tags:
  - tipus/teoria
  - assignatura/SO
assignatura: SO
data: "2026-10-24"
---

# T3 — Sistemes de fitxers (Parte 2)

**Referència: PDF 03 — Sistemas de ficheros (Parte 2)** (D1-45)

---

## 1. Anuncis i objectius de la sessió

- **Correccions de la P1** pujades al CV (falta el *grupo A*)
- Pujat el **vídeo-resum del Tema 2** al CV
- **8 dies per al parcial** · **Test de l'unitat 2 la setmana vinent**
- Referència del professor: djangogirls.org Barcelona

**Objectius** (D4):

- Analitzar els sistemes de fitxers **FFS** (i comparar-los amb els **FAT**)
- Consolidar els coneixements bàsics de sistemes de fitxers
- Resumir el tema de sistemes de fitxers
- Comentar (si hi ha temps) el **parcial del curs anterior**

---

## 2. Repàs: què falta als FAT? (D5)

- Ja vam veure que tenen **diverses limitacions**: fitxers fragmentats, sistema de *backup*, control d'accés d'usuaris, ...
- D'aquí cap on evolucionen els sistemes moderns: **FFS**

---

## 3. FATX (X = 12, 16, 32) i exFAT (D6)

- **X** = bits utilitzats per representar les **entrades de la taula FAT**

| Característica | FAT12 | FAT16 | FAT32 (28 útils) | exFAT |
|---|---|---|---|---|
| Bits per entrada FAT | 12 | 16 | 32 | 32 |
| Clústers de dades aprox. | 4.084 | 65.524 | 268 milions | Milers de milions |
| Mida màx. de fitxer | Limitada pel volum | 4 GiB − 1 byte | 4 GiB − 1 byte | 16 EiB (teòric) |
| Mida màx. de volum | Molt petita | ~2 GiB habitual | ~2 TiB habitual (sectors de 512 B) | Molt elevada |
| Ús típic | Disquets | Sistemes antics | USB, targetes SD | USB i targetes SDXC |

---

## 4. Sistemes FFS (Unix Fast File System) (D7-9)

- Desenvolupat a **mitjans dels 80** (la FAT, als **70**)
- És la **base de molts sistemes de fitxers actuals**: **ext3, ext4, NTFS**, ...
- Diferència estructural clau: la FAT emmagatzema els blocs d'un fitxer en una **llista enlazada**; el FFS fa servir **vectors**
- Els blocs d'un fitxer s'**indexen** de manera que es pugui treballar de forma eficient amb fitxers **grans i petits**
- Permet **controlar l'accés** dels usuaris a cada fitxer (**lectura, escriptura, execució**)
- El FFS inclou **heurístiques de localitat** que aconsegueixen que els fitxers estiguin "repartits" al disc de forma **contígua** → el **braç** del disc magnètic es mou **menys** en lectura/escriptura

> [!question]- Per què "Fast"? Què té a veure la localitat amb la velocitat?
> Al disc magnètic cada salt té un **cost mecànic** (seek + latència de rotació). Si els blocs d'un mateix fitxer (i els metadades associats) són **contigus**, el braç recorre menys distància i es fan **menys seek** → el sistema és més ràpid. D'aquí el nom *Fast* File System.

---

## 5. Organització d'una partició FFS (D10-11)

### Nivell disc sencer

- **MBR** (Master Boot Record) + **taula de particions** (*partition table*)
- La resta del disc es divideix en **particions** (*disk partitions*)

### Dins d'una partició amb FFS (localitzacions conegudes pel sistema)

| Zona | Què conté |
|---|---|
| **Boot block** | El codi necessari per **arrencar el SO** des d'aquesta partició |
| **Superblock** | Els **paràmetres clau** del sistema de fitxers; es carrega a memòria quan s'arrenca o quan el sistema de fitxers s'inicia |
| **Free space mgmt** | La informació dels **blocs lliures** al disc |
| **I-nodes** | Els blocs que componen cada fitxer; **un únic i-node (amb el seu ID) per fitxer** |
| **Root dir** | El (primer) bloc del **directori arrel**; la seva posició és **coneguda** pel sistema |
| **Files & directories** | Els fitxers i directoris del disc; es va **modificant** a mesura que s'escriuen/esborren dades |

---

## 6. I-nodes (D12-14)

- Els i-nodes (que emmagatzemen els blocs d'un fitxer) són en una **posició coneguda** del sistema de fitxers
- Cada i-node té una **mida fixa** (en bytes) i un **ID** (valor numèric) → el sistema el **localitza ràpidament** (ex.: "i-node 1074", localitzable immediatament)

### A FFS (D13)

- Un **directori**, intuïtivament, és un **fitxer (taula)** amb els **noms** dels fitxers que conté i **l'i-node** que els correspon
  - Exemple de taula de directori: `Archivo B`, `Archivo A`, `Fichero Z`, `Fichero G` → cadascun amb la seva entrada *i-node*
- **El nombre d'i-nodes està prefixat!** Hi ha **un i-node per cada 16 KB** d'espai al disc — més que suficient per a les necessitats de l'usuari
- Organització del disc: `Free space mgmt` → zona d'**i-nodes** (1, 2, 3, 4, 5, ... 1074) → `Root dir`

### Què guarda un i-node (D14)

Dos blocs de camps:

1. **Atributs del fitxer**: mida, data de creació, **permisos**, propietari, ...
2. **Punterers als blocs** del fitxer (aquí l'exemple del fitxer A ocupa els blocs **4, 7, 2, 10, 12** — els mateixos de l'exemple de la T3-P1 amb la FAT, però aquí dins l'i-node)

---

## 7. Punterers: com serveix un i-node per a mides diferents? (D15-19)

### El problema

- Si hi ha **un i-node per fitxer**, com es gestionen fitxers de **mida diferent**?
- Amb blocs de **4096 bytes** i només **punterers directos**: `12 × 4096 = 48 KB`
- "Potser als 80 era suficient... **però què passa si el fitxer té més de 48 KB?**"

### La solució: 15 punterers de 4 tipus

- Cada i-node conté un **vector de punterers** als blocs del fitxer, de **diferents tipus**
- **En total 15 punterers**: els **12 primers són directes**, i després n'hi ha d'**indirectes** (simple, doble, triple)

| # | Tipus | Què apunta | Blocs accessibles | Mida màx. (bloc 4 KB, punter 4 B) |
|---|---|---|---|---|
| 1-12 | **Directe** | Directament a un bloc de dades | 12 | 12 × 4 KB = **48 KB** |
| 13 | **Indirecte** | Un bloc que conté *només* punterers directes | 1024 (`4096 / 4`) | 48 KB + 1024×4 KB = **~4 MB** |
| 14 | **Doblement indirecte** | Un bloc de punterers indirectes | 1024² | **~4 GB** |
| 15 | **Triplement indirecte** | Encara un nivell més | 1024³ | **~4 TB** |

- Un **bloc de punterers indirectes** de 4 KB amb punterers de 4 B conté **1024 punterers** → `48 KB + (1024 × 4 KB) ≈ 4 MB`
- El FFS utilitza un **arbre fix multinivell asimètric** capaç de donar suport a fitxers **petits i grans** de forma eficient; molts sistemes actuals han adoptat aquest enfocament (amb optimitzacions)

> [!question]- Per què "asimètric"?
> Perquè no tots els nivells es recorren igual: els **primers 48 KB** es resolen en **0 indireccions** (punterers directes), els següents en **1**, després **2**, després **3**. Un fitxer petit no paga el cost d'una cadena llarga de punterers, i un de gran té prou capacitat. L'arbre no és uniforme ni complet: és *fix* (15 entrades, prefixat) i *asimètric* (cadascuna amb un abast molt diferent).

### Cadena de punterers (D18)

```
i-node ─┬─ Direct block 1..12 ──────────────────► Data block
        ├─ Indirect block ────► Data block N ───► Data block
        └─ Double-indirect block ─► indirect block ─► Data block
```

---

## 8. Exemple: localitzar `/usr/ast/mbox` (D20-21)

> [!quote] "*Se desea abrir el fichero ubicado en /usr/ast/mbox del sistema de ficheros. ¿Qué pasos hay que realizar?*"

Cadena d'**directoris → i-nodes → blocs** (xifres de la figura D20):

| Pas | Què passa |
|---|---|
| 1 | El sistema coneix la posició del **directori arrel**. Es busca l'entrada `usr` |
| 2 | `usr` → **i-node 6**; l'i-node 6 diu que `/usr` és al **bloc 132** |
| 3 | Al **bloc 132** (`/usr`) es busca `ast` |
| 4 | `ast` → **i-node 26**; l'i-node 26 diu que `/usr/ast` és al **bloc 406** |
| 5 | Al **bloc 406** (`/usr/ast`) es busca `mbox` |
| 6 | `mbox` → **i-node 60**. Es llegeix l'i-node 60 i ja es pot obrir el fitxer. Un cop obert, el SO guarda internament l'i-node associat |

Contingut de les taules de la figura:

```
Root directory:  1 .   1 ..   4 bin   7 dev   14 lib   9 etc   6 usr   8 tmp
Bloc 132 (/usr): 6 .   1 ..  19 dick 30 erik  51 jim   26 ast  45 bal
Bloc 406 (/usr/ast): 26 . 6 .. 64 grants 92 books 60 mbox 81 minix 17 src
```

> [!warning] Errates als passos escrits del PPT (D21)
> El text dels passos diu "**bloque 123**" (pas 3) i "**i-node 25**" (pas 4). La figura (D20) diu **bloc 132** i **i-node 26** — el text és una errata; segueix les xifres de la figura.

---

## 9. Exemple: lectura amb `read(fd, vector, 4096*4)` (D22-23)

- Suposem blocs de **4096 bytes**; la crida demana **4 × 4096 = 16384 bytes** (4 blocs)
- Un usuari del SO "**veu**" els blocs d'un fitxer com a **contigus**
- Els **i-nodes fan el mapeig** entre els **bytes lògics** i la **posició física** al disc

Mapeig de la figura D22:

| Posició lògica (bytes) | Bloc físic |
|---|---|
| 0 – 4095 | Bloc **3** |
| 4096 – 8191 | Bloc **1** |
| 8192 – 12287 | Bloc **8** |
| 12288 – 16383 | Bloc **4** |

(Alguns dels blocs que es veuen al disc estan buits i d'altres ocupats per altres fitxers — **el fitxer no és contigu físicament però ho sembla lògicament**.)

Què fa el sistema de fitxers davant de `read(fd, vector, 4096*4)`:

1. **Dividir** la petició en els **blocs** que la componen
2. Fer la **petició de lectura** a cadascun dels blocs (3, 1, 8, 4)
3. "**Unir**" els blocs llegits en un sol **vector**, en ordre lògic

---

## 10. Balanç FFS fins aquí (D24)

- Cada fitxer té associat un **i-node**, que es pot interpretar com l'**arrel d'un arbre** que emmagatza els blocs del fitxer
- Aquest arbre és **asimètric** i permet tractar de forma eficaç fitxers **grans i petits** (directes, indirectes, doblement i triplement indirectes)
- Ara falta: com es gestiona l'**espai lliure** i la **heurística de localitat**

---

## 11. Espai lliure al FFS: *bitmap* (D25)

- Per buscar espai lliure, el FFS utilitza un **bitmap emmagatzemat al disc** (*Free space mgmt*), on **cada bloc es representa amb un bit (0/1)**
  - `0` = bloc **lliure** · `1` = bloc **ocupat**
- El bitmap és en una **posició coneguda** pel sistema de fitxers
- Avui en dia s'utilitzen, per exemple, **estructures d'arbre** per localitzar blocs lliures amb la **mida sol·licitada**

> [!question]- I la FAT com buscava espai lliure? Quina diferència hi ha?
> La FAT **recorria la taula** buscant un element no ocupat (algoritme "el següent bloc lliure") → fragmentació. El FFS té un **bitmap dedicat**: en una sola lectura de bitmap es veu l'estat de tots els blocs, i es pot triar un bloc **contigu** al que ja ocupa el fitxer (millor localitat).

---

## 12. Heurística de localitat al FFS (D26)

- Al **disc magnètic** es divideix en **grups** (*block groups*); cada grup permet emmagatzemar els **metadades** (i-nodes, directoris, *bitmap* d'espai lliure, ...)
- Un **directori concret** està associat a un **grup concret**; el FFS intenta emmagatzemar els **fitxers d'aquell directori al seu grup**
- La figura mostra anells concèntrics `Block Group 0`, `1`, `2`, ...; cadascun conté tres zones:
  - **inodes**
  - **Data Blocks for files in directories /...** (blocs de dades dels fitxers del directori associat)
  - **Free Space Bitmap**

**Per què importa**: els metadades i les dades d'un directori queden **físicament a prop** → en llistar/obrir un directori i els seus fitxers, el braç pràcticament **no es mou**.

---

## 13. Principis bàsics: FAT vs FFS (D27)

| | **FAT** (File Allocation Table) | **FFS** (Unix Fast File System) |
|---|---|---|
| Època | Desenvolupat als **70** | Desenvolupat a **mitjans dels 80** |
| Ús avui | Memòries **USB**, targetes de càmeres digitals | Base d'**ext3, ext4, NTFS**, ... |
| Estructura | **Llista enlazada** | **Vectors** |

> Els FFS són la base dels sistemes de fitxers més moderns. **Què ha canviat els darrers anys?**

---

## 14. Millores als sistemes FFS (D28)

Les millores s'han centrat en el **rendiment** i la **consistència de les dades**:

- **Directoris**: en comptes d'una **taula no ordenada**, es fan servir **arbres balancejats** per emmagatzemar els elements
- **Journaling** (*journaling file system*, "registre per diari"): assegura la **consistència dels metadades** en cas de **tall elèctric, avaria**, etc.
- **Copy-on-Write (COW)**: permet emmagatzemar de forma **implícita i eficient** còpies de seguretat del mateix sistema de fitxers al disc; si una còpia falla, es pot recuperar una còpia antiga. **Exemple: BTRFS**

> [!question]- Journaling vs COW: quina és la diferència d'objectiu?
> El **journaling** escriu primer un **registre d'intenció** dels metadades per poder **refer-los** si hi ha un tall → evita la corrupció. El **COW** mai **sobreescriu** el bloc existent: escriu una còpia nova i després actualitza el punter → conserva **versions anteriors** com a còpies de seguretat. (El primer protegeix contra *pèrdua de consistència*, el segon afegeix *versions recuperables*.)

---

## 15. Discos d'estat sòlid (SSD) (D29-30)

- Fins ara hem parlat de FAT i FFS aplicats a **discos magnètics** (amb parts mòvils). I els **SSD**?
- **No tenen parts mòvils** → rendiment **molt superior**, sobretot en **accés aleatori**
- Pregunta oberta del PPT: **"¿Qué pasa si no se alimentan durante un temps?"**
- Els FAT i FFS tal com es fan servir als discs magnètics **no són adequats** per a aquests dispositius:
  - Accedeixen a les **mateixes posicions físiques** per emmagatzemar les dades → **degrada ràpidament** l'electrònica d'un SSD

### Solucions (D30)

- **Wear leveling**: permet que els SSD **utilitzin els sistemes de fitxers habituals** (FAT, FFS, NTFS, ...) repartint les escriptures per tota la memòria per no cremar les mateixes cel·les
- **Log-structured filesystems**: sistemes de fitxers **específics** per a aquests dispositius (el PPT hi escriu "*long-structured*", errata per *log-structured*)

---

## 16. Les dades: conclusió del tema (D31-40)

### Evolució (D31, D40)

- La capacitat d'emmagatzematge ha crescut **pràcticament de forma exponencial** → ha calgut **redissenyar** cada vegada els sistemes per incloure les funcionalitats necessàries
- **El 2026, cada persona genera ~61,22 GB de dades al dia** (font: datademia.es)
- **Tota** sistema de fitxers té **limitacions i avantatges** → fer servir el que **millor s'adapti** a les necessitats
- Els sistemes de fitxers **continuen evolucionant**... i avui en dia s'utilitzen molt els **sistemes distribuïts**

### Dades "sleeping" (D32-35)

- *Data never sleeps: AI Edition (2025)* (domo.com)
- Un **dijous qualsevol**: 07:15 desbloqueig del mòbil (biometria) · 07:20 temps (ubicació) · 07:40 pagant un café (banc) · 08:15 Google Maps (GPS) · 09:00 WhatsApp (metadades) · 09:30 Gmail · 11:00 smartwatch (freqüència cardíaca) · 14:30 targeta restaurant · 15:00 fotos del dinar · 18:00 Netflix · 21:30 Alexa posa música · 22:00 rellotge intel·ligent (monitorització del son)

### La manca de dades també informa (D36-39)

- **Aforaments de bala**: els punts vermells a les fotos d'avions de la II Guerra Mundial marquen on rebien bales els avions que tornaven a base → "*la raó darrere de per què ens falten certs dades pot ser més significativa que les dades que tenim!*"
- **Ronald Coase** (Premi Nobel d'Economia, 1991): "*Si tortures les dades prou temps, confessaran el que sigui*"
- **George Dyson** (escriptor i historiador de la tecnologia): "*Facebook defineix qui som, Amazon defineix què volem i Google defineix què pensem*"
- D39: portada del llibre **"Los irresponsables"** de **Sarah Wynn-Williams**

---

## 17. Examen parcial 2025-2026 (D41-44)

> Exemples de l'examen real del curs anterior. Enunciats en el **text original** (castellà).

### Problema 1 (3,5 punts; 0,5 per pregunta)

> [!quote] Enunciat
> *Mañana a la noche durante la castañada, un sistema de monitorización registrará la temperatura de varios hornos de castañas en Barcelona (we love datal). Cada medición se guardará como un número en coma flotante (float) dentro del fichero `sensor_castanya.log`. Este archivo contiene inicialmente 1000 registros del año pasado y está representado por el i-node 532. Supongamos que el tamaño de bloque del sistema de ficheros es de 4096 bytes y que el bloque físico inicial asignado al archivo es el 200. Analiza el siguiente programa en C que se encargará de añadir las nuevas lecturas al final del archivo y responde a las siguientes preguntas. Razona las respuestas.*

```c
 1  int main() {
 2    int fd = open("sensor_castanya.log", O_WRONLY | O_APPEND);
 3    if (fd < 0) return 1;
 5    float t[3] = {66.6, 67.2, 65.9};
 6    ssize_t n = write(fd, t, sizeof(t));
 8    if (n < 0) perror("write");
 9    else printf("Añadidas %ld bytes\n", n);
11    close(fd);
12    return 0;
13  }
```

**Preguntes:**

- **a)** Explica pas a pas què fa el programa. Quin és l'efecte del flag `O_APPEND` a `open()`?
- **b)** Calcula la mida total (en bytes) i el nombre de blocs ocupats pel fitxer **abans i després** d'executar-lo.
- **c)** En quin format s'emmagatzema la informació del sensor? Per què, en obrir-lo amb un editor de text, surten caràcters **ilegibles**?
- **d)** Quins blocs **lògics i físics** es modifiquen o s'afegeixen al FFS en escriure les dades noves? **Quants accés a disc** serien necessaris si no hi hagués **caché**?
- **e)** Si el mateix fitxer fos a un **FAT**, quantes **entrades de la FAT** caldria actualitzar per registrar l'escriptura? Explica el procés.
- **f)** Les dades de temperatura són a un **SSD**, però el sistema de còpia de seguretat usa un **HDD**. Explica les diferències principals en **organització física, latència i estratègia d'accés**.
- **g)** Què és el **Master Boot Record (MBR)** i quina informació conté?

### Problema 2 (3,5 punts; 0,5 per pregunta) — Docker

> [!quote] Enunciat
> *Durante esta semana, algunos alumnos de la facultad han desarrollado un pequeño servicio web llamado `pumpkin-metrics`, encargado de recopilar y exponer métricas sobre el peso y temperatura de calabazas asadas a diferentes hornos con sensores inteligentes (¡los datos nunca duermen!). El equipo ha empaquetado la aplicación en un contenedor Docker basado en Debian...*

```dockerfile
FROM debian:12-slim

ARG APP_VERSION=1.0
ENV APP_ENV=prod PYTHONUNBUFFERED=1

RUN apt-get update && \
    apt-get install -y --no-install-recommends python3 curl && \
    apt-get purge -y nano || true && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

RUN addgroup --system pumpkin && \
    adduser --system --ingroup pumpkin --home /srv/pumpkin pumpkin

WORKDIR /srv/pumpkin
COPY --chown=pumpkin:pumpkin app/ .

VOLUME ["/data", "/logs"]
EXPOSE 8080
USER pumpkin
HEALTHCHECK CMD curl -fss http://localhost:8080/health || exit 1
ENTRYPOINT ["python3", "server.py"]
CMD ["--port=8080", "--version=${APP_VERSION}"]
```

Comanda de construcció: `docker build -t pumpkin-metrics:1.0 .`

**Preguntes:**

- **a)** Funció de `--no-install-recommends` i de netejar `/var/lib/apt/lists/*`. Quin impacte té en la **mida** i la **seguretat** de la imatge?
- **b)** Quin efecte té `apt-get purge -y nano || true` si el paquet **no està instal·lat**? Per què `|| true`?
- **c)** Per a què serveixen `addgroup` i `adduser`? Quin avantatge té executar el contenidor amb `USER pumpkin` en lloc de `root`?
- **d)** Què garanteix `COPY --chown=pumpkin:pumpkin app/ .`? Quins problemes si s'ometés `--chown`?
- **e)** Defineix **repositori, imatge i tag** a Docker Hub. Per què fer servir sempre `:latest` pot ser problemàtic enfront de `:1.0`?
- **f)** Compara **contenidors** i **màquines virtuals** quant a aïllament, *kernel*, *overhead* i temps d'arrencada. Posa un exemple representatiu de cada tecnologia.
- **g)** Distingeix entre **virtualització** i **emulació**, i dóna un exemple real de cada cas.

> [!tip] On repassar
> **a-e** → [[T2b-Contenedors-Docker|T2b — Contenedors i Docker]] · **f-g** → [[T2-Maquines-Virtualitzacio-SO|T2 — MV i virtualització]]

### Problema 3 (3,0 punts) — programació segura

> [!quote] Enunciat
> *Estamos probando un programa que procesa nombres de participantes y registra etiquetas de calabazas. Os pedimos detectar errores de programación y proponer correcciones y medidas defensivas para el siguiente código. Responde a las siguientes preguntas de forma breve, justificando siempre las respuestas.*

```c
 1  int main(void) {
 2      char *h1 = malloc(16);
 3      char *h2 = malloc(16);
 4
 5      if (!h1 || !h2) return 1;
 6
 7      printf("Introdueix el teu nom (entrada arbitrària): ");
 8      fflush(stdout);
 9      ssize_t n = read(STDIN_FILENO, h1, 32);
10      if (n > 0) {/* eliminar possible salt de línia */
11          if (h1[n-1] == '\n') h1[n-1] = '\0';
12          else h1[n < 16 ? n : 15] = '\0';
13      }
14
15      printf("Hola %s\n", h1);
16
17      free(h1);
18
19      printf("Reutilitzant punter alliberat: %s\n", h1);
20
21      char *h3 = malloc(32);
22      strcpy(h3, "carbassa-espantosa");
23      printf("h3: %s\n", h3);
24
25      free(h2);
26      free(h3);
27      return 0;
28  }
```

**Preguntes:**

- **a)** Identifica i **nomena** les vulnerabilitats del codi. Per a cadascuna, explica **per què és perillosa** (1 punt)
- **b)** Proposa **correccions concretes** (fragments segurs) que eliminin les vulnerabilitats de l'apartat anterior (1 punt)
- **c)** Quines **opcions de compilador** recomanaries activar per millorar la seguretat del binari? Explica breument l'efecte de cadascuna (0,5 punts)
- **d)** Què és un **CVE**? Com comprovaries si una versió d'una biblioteca té un CVE conegut? (0,5 punts)

> [!tip] On repassar
> Tot → [[T1-Introduccio-Seguretat-SO|T1 — Introducció Seguretat SO]]

---

## Preguntes del PPT (índex ràpid)

| # | Pregunta | On |
|---|---|---|
| Ràpid | Per què "Fast"? Què hi té a veure la localitat? | [[#4. Sistemes FFS (Unix Fast File System) (D7-9)]] |
| Ràpid | Per què l'arbre de punterers és *asimètric*? | [[#7. Punterers: com serveix un i-node per a mides diferents? (D15-19)]] |
| Oberta | Què passa si un SSD no rep alimentació durant un temps? | [[#15. Discos d'estat sòlid (SSD) (D29-30)]] |
| Ràpid | I la FAT com buscava espai lliure? Diferència amb el bitmap? | [[#11. Espai lliure al FFS: bitmap (D25)]] |
| Ràpid | Journaling vs COW: quin objectiu cadascun? | [[#14. Millores als sistemes FFS (D28)]] |
| Examen | Problema 1 (FFS + FAT + SSD + MBR) | [[#Problema 1 (3,5 punts; 0,5 per pregunta)]] |
| Examen | Problema 2 (Docker) | [[#Problema 2 (3,5 punts; 0,5 per pregunta) — Docker]] |
| Examen | Problema 3 (programació segura) | [[#Problema 3 (3,0 punts) — programació segura]] |

---

## Resum ràpid (FITXA)

| Concepte | Clau |
|---|---|
| **FATX** | X = bits per entrada de la taula (12/16/32); FAT32 → 4 GiB−1 per fitxer; exFAT → 16 EiB teòric |
| **FFS** | Mitjans **80s**, Unix *Fast* File System; **vectors** no llista enlazada; base d'**ext3/ext4/NTFS** |
| **Estructura FFS** | Partició → `Boot block` · `Superblock` · `Free space mgmt` · `I-nodes` · `Root dir` · `Files & directories` |
| **I-node** | Mida **fixa** + **ID** numèric; guarda **atributs** (mida, dates, permisos, propietari) + **punterers als blocs**; **un per fitxer** |
| **Directori** | Un **fitxer (taula)**: nom → i-node. El **nombre d'i-nodes està prefixat**: **1 per cada 16 KB** de disc |
| **15 punterers** | **12 directes** = 48 KB · **1 indirecte** = ~4 MB · **1 doble** = ~4 GB · **1 triple** = ~4 TB (bloc 4 KB, punter 4 B) |
| **Arbre d'i-node** | **Fix** (15 entrades) i **asimètric** (0/1/2/3 nivells d'indirecció segons la mida) |
| **Mapeig lògic-físic** | L'usuari ve el fitxer **contigu**; l'i-node tradueix **rang de bytes → bloc físic** |
| **Espai lliure FFS** | **Bitmap** (1 bit/bloc: 0 lliure, 1 ocupat) en posició coneguda; avui, **arbres** per trobar blocs de la mida demanada |
| **Localitat FFS** | Disc en **grups**; cada grup = i-nodes + dades + bitmap; un **directori ↔ un grup** → els fitxers del directori van al seu grup → menys **seek** |
| **Millores FFS** | Directoris → **arbres balancejats**; **journaling** (consistència de metadades); **COW** (còpies de seguretat, ex. **BTRFS**) |
| **SSD** | Sense parts mòvils → accés aleatori **molt ràpid**; els FS de discs magnètics **degraden** les cel·les escrivint sempre als mateixos llocs → **wear leveling** + **log-structured filesystems** |
| **Dades 2026** | ~**61,22 GB/dia** per persona; la **manca** de dades també informa (avions de la II GM) |
| **MBR** | Primer sector del disc: codi d'arrencada + **taula de particions** (tipus, mida, active) |

---

## Dubtes / a revisar

- **Època del FFS**: la T3-P1 deia "mitjans dels **90**"; aquest PDF diu literalment "**mediados de los 80s**". Seguir el 80 (és el que diu el professor a la Parte 2) — repassar si toca a l'examen
- **D21**: errates als passos (`bloque 123` → **132**, `i-node 25` → **26**); les xifres correctes són les de la figura D20
- **D30**: el PPT escriu "*long-structured filesystems*"; el terme correcte és **log-structured**
- **Pregunta oberta del PPT** (D29): què passa amb un SSD sense alimentació un temps? El professor no hi va donar resposta escrita — confirmar a classe (retenció de càrrega de les cel·les NAND)
- **Problema 1e**: dependrà de la mida de clúster que es doni (o s'assumeixi) a l'examen; raonar sobre els dos casos (clúster petit vs 4 KB) i recordar que la mida del fitxer es guarda a l'**entrada de directori**, no a la taula FAT
- **Problema 2f-g**: encara no resoltos aquí; fer-los servir com a test de T2/T2b abans del parcial
- **Test de l'unitat 2 la setmana vinent** → quan arribi, afegir-lo com a secció (igual que el Test P1-P6 a la nota P1)
- **NTFS (fora del curs)**: l'**MFT** té entrades de **mida fixa** (1 KB/fitxer) però la **taula $MFT sí que pot créixer** — el contrari que la FAT (taula sencera fixa en formatar). Si un test demanés "variable" per NTFS, seria certa; per la FAT, no.
- **Test 2019 P8 (SSD)**: la resposta surt literal de D29 ("accedeixen a les mateixes posicions físiques → degrada ràpidament l'electrònica") + D30 (wear leveling = **durabilitat**). Simplificació del professor (avui el wear leveling el fa la FTL del SSD); a l'examen, anar amb el PPT.

---

## Enllaços relacionats

- [[T3-Sistemes-Fichers-P1|T3 — Sistemes de fitxers (Parte 1)]]
- [[T2b-Contenedors-Docker|T2b — Contenedors i Docker]]
- [[T2-Maquines-Virtualitzacio-SO|T2 — MV i virtualització]]
- [[T1-Introduccio-Seguretat-SO|T1 — Introducció Seguretat SO]]
