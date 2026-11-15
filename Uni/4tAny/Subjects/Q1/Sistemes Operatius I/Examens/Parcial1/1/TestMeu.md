---
id: TestMeu
aliases: []
tags:
  - assignatura/SOI
  - tipus/parcial
---

| Column1   | Column2    |
|--------------- | --------------- |
| Preg1   | 3   |
| Preg2   | 4   |
| Preg3     | 2   |
| Preg4    | 3   |
| Preg5   | 3   |
| Preg6   | 1   |
| Preg7   | 1   |
| Preg8   | 2   |



He fallat:
  1, 3, 4, 5, 8

Les preguntes m'han semblat molt molt mal formulades, molt rares, de preguntarme que és algo i que dsps les respostes siguin per funcions 

A part d'això, el que menys he tingut per ma és les preguntes 5 6 7 i 8

---

## Correcció (solucions oficials, PDF marcat en groc)

| Preg | Meva | Correcta |  |
|---|---|---|---|
| 1 | 3 | **2** | ✗ |
| 2 | 4 | 4 | ✓ |
| 3 | 2 | **4** | ✗ |
| 4 | 3 | **4** | ✗ |
| 5 | 3 | **2** | ✗ |
| 6 | 1 | 1 | ✓ |
| 7 | 1 | 1 | ✓ |
| 8 | 2 | **3** | ✗ |

**3/8** (el test pesa un 35% de la nota)

## Què he fallat i per què

- **P1 (VMM)**: he triat la definició d'**emulació** ("maquinari diferent del real" = emulador, ex QEMU). El VMM **virtualitza** (mateixa arquitectura); la funció essencial és fer de **"SO que executa i gestiona altres SOs"** — literalment l'opció 2 i literalment la nota T2 §8. La 4 només val per un type 2 (massa estreta). → [[T2-Maquines-Virtualitzacio-SO#6. Virtualització vs emulació]]
- **P3 (Docker, marcar la FALSA)**: la falsa és la **4** (Docker no serveix per desenvolupar distribucions). He marcat la 2 pensant que era falsa; al curs l'aïllament es dona per cert. *Queixa legítima*: la 2 ("cap dada fora del context") i la 3 (fork-bomb) són discutibles de debò (volums/bind-mounts, límits cgroups) — però a l'examen cal jugar al marc del PPT. → [[T2b-Contenedors-Docker]]
- **P4 (JVM)**: era "totes certes". La 1 (arquitectura neutral = **bytecodes**) i la 2 (processos individuals) són exactament T2 §2: la JVM és una **MV de procés** — no virtualitza hardware, virtualitza una ISA abstracta; cada procés Java = la seva JVM. → [[T2-Maquines-Virtualitzacio-SO#2. La JVM (exemple de MV de procés)]] · [[T2c-Comparativa-SO-MV-Contenidor]] (fila JVM)
- **P5 (FAT)**: la FAT té **mida fixa** (fixada en formatar; depèn del disc, no del nº de fitxers) i guarda **quins blocs formen cada fitxer** (les cadenes). Nom/data van a les **entrades de directori**, no a la FAT — trampes 1 i 4. He caigut a la 3 ("mida variable"). → [[T3-Sistemes-Fichers-P1#12. El sistema FAT en detall]]
- **P8 (SSD)**: el problema és la **durabilitat** (escriure sempre als mateixos blocs → desgast; d'aquí *wear leveling* + log-structured), no el rendiment (4) ni "NTFS més modern i adequat" (2, trampa). → [[T3-Sistemes-Fichers-P2#15. Discos d'estat sòlid (SSD) (D29-30)]]

## On centrar-me

1. **Sistemes de fitxers** (les que dic que costa més: 5 i 8): FAT (mida fixa, què guarda, on van les metadades) + SSD (durabilitat vs rendiment).
2. **Virtualització vs emulació**: abans de marcar, preguntar-me *mateixa CPU o CPU diferent?*
3. **MV de sistema vs MV de procés (JVM)**: tancar el `(?)` de classe1.
4. Tècnica: en preguntes negatives ("marqui la FALSA") valorar **per escrit** cada opció cert/fals; amb "totes són certes", verificar cada subproposició una a una.

> L'estil del professor: definicions **per funció**. Cal agafar la funció essencial (P1: gestionar múltiples MVs) i descartar les que descriuen un altre concepte (emulador) o un cas particular (type 2).

