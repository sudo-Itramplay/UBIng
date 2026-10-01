---
data: 2026-09-18
assignatura: SO
parcial: 
tags:
  - tipus/teoria
  - assignatura/SO
---

# T1 — Introducció a la seguretat en SOs

**Referència: Diapositives 1-57**

---

## 1. Objectius i triada CIA (D1-5)

L'objectiu és entendre els perills de seguretat, les vulnerabilitats dels SOs i els mecanismes de protecció.

En un ordinador compartit (ex: laboratori), el SO ha d'assegurar:

| Objectiu | Què vol dir | Exemple |
|---|---|---|
| **Confidencialitat** | Només els autoritzats accedeixen a la info | Juan no pot llegir l'informe de Carla |
| **Integritat** | La info no es modifica sense autorització | Juan no pot modificar l'informe de Carla |
| **Disponibilitat** | Els recursos són accessibles quan cal | Carla pot accedir al seu informe |

> [!warning] El SO **contribueix** a aquests objectius però **no els garanteix sol**. Calen mecanismes addicionals.

---

## 2. Exemples reals d'atacs (D6-10)

| Ataque | Any | Detalls |
|---|---|---|
| UAB | 2021 | Ciberataque a la universitat |
| UOC | 2022 | Va paralitzar el campus virtual |
| Hospital Clínic | 2023 | Ransomware |
| UB | 09/2026 | Ciberataque durant matrícula |

### WannaCry (D10)

- Gusano ransomware (maig 2017)
- 200.000+ ordinadors, 150+ països
- Explotava **EternalBlue** (vulnerabilitat de MS Windows, desenvolupada per la NSA)
- Afectats: FedEx, Honda, Nissan, NHS…

---

## 3. Vulnerabilitats i CVE (D11-17)

### Definicions

- **Amença**: algú (o algo… IA) intenta alterar els resultats
- **Vulnerabilitat**: debilitat o fallo que pot ser explotada per comprometre la CIA
- **Riesgo**: probabilitat i impacte que l'alteració es produeixi

### Per què són inevitables

- Kernel Linux 6.5-rc5: **~36 milions de línies de codi**
- Procés excel·lent manté defectes a **1 per 10.000 línies** (NASA)
- C/C++: vulnerables per disseny (sense gestió automàtica de memòria)
- Python també pateix CVEs (està escrit en C) → CVE-2016-5636

### Exemples de vulnerabilitats

- **Buffer overflow**
- **Uso después del free()** (use-after-free)
- **Null pointer dereference**

### CVE (Common Vulnerabilities and Exposures)

- Estàndard públic per identificar i catalogar vulnerabilitats
- Web: https://www.cve.org/

**Cas: sudo CVE-2021-3156** — heap overflow introduït el 2011, descobert el 2021 (10 anys!). Afectava Linux, Mac OS i BSD. Permetia executar programes amb privilegis d'altres usuaris.

---

## 4. Principis de sistemes seguros (D18-29)

### Història: MULTICS (D18)

- SO pioner (1965-2000): MIT, Bell Labs, GE
- Innovacions: recursos compartits, protecció de memòria, accés controlat per permisos, jerarquies de directoris

### Principi 1: Defensa multinivel (D19-24)

Protecció a **múltiples capes**:

| Capa | Exemple de protecció |
|---|---|
| Aplicació | Comprovar longitud d'entrada |
| Processos | Limitar permisos i recursos |
| SO i hardware | Aïllar memòria i controlar execució |
| Operació del sistema | Actualitzar i preparar recuperació |

**Exemple pràctic**: vulnerabilitat en JS del Chrome:
- Chrome (procés) → impedir accés a altres pestanyes
- SO → impedir accés a altres processos (gestor de contrasenyes)
- Hardware → impedir instal·lació de malware al firmware
- Xarxa → impedir propagació a altres ordinadors

> [!info] CPUs modernes: **4 anells de protecció**, però se'n fan servir 2. **Anillo 0** = kernel, **Anillo 3** = apps.

**Flux d'obertura de fitxer**:
1. El procés demana `open`
2. La crida al sistema entra al **kernel**
3. El kernel comprova credencials i regles
4. Retorna descriptor (fd) o error

> [!tip] **Mode usuari ↔ mode kernel** = frontera de protecció. Base per entendre les trucades al sistema.

### Principi 2: Menor privilegi (*least privilege*) (D25-26)

Cada usuari/procés accedeix **només** al que necessita.

- Compte de servei **no necessita ser administrador**
- Compte comprometut → menys dany si pot fer menys

### Principi 3: Separació de privilegis (D27-28)

Dividir el sistema en parts amb accés limitat. Segmentar en components amb menor privilegi possible → evita que un atacant prengui control de tot.

### Segurança més enllà de l'usuari (D29)

- Usuari → llegeix els fitxers que crea
- Procés → **NO** llegeix memòria d'un altre procés
- App mòbil → **NO** edita dades d'una altra app
- Domini web → **SOLO** llegeix les seves cookies
- Màquina confiable → accedeix a servidor de fitxers

---

## 5. Polítiques de seguretat (D30)

Tres elements per definir una política:

| Element | Pregunta | Exemples |
|---|---|---|
| **Sujet** | Qui? | Usuari, app, procés |
| **Objeto** | Què? | Memòria, fitxers, hardware, sockets |
| **Operació** | Com? | Llegir, escriure, eliminar |

Regles:
- Usuari **no** pot esborrar fitxers d'un altre
- Procés **no** pot llegir memòria d'un altre procés

---

## 6. UNIX: Usuaris i grups (D31-33)

### Usuaris

- **Comptes de servei**: processos en background (ex: web server)
- **Comptes d'usuaris**: cada persona amb un **UID**
  - **root** (UID 0): accés a tot
  - Algunes operacions: **només** root

### Grups

- Agrupen usuaris que comparteixen recursos
- Cada grup té un **GID**

---

## 7. UNIX: Permisos de fitxers (D34-37)

### Permisos bàsics

| Permís | Valor |
|---|---|
| r (lectura) | 4 |
| w (escriptura) | 2 |
| x (execució) | 1 |
| - (cap) | 0 |

Tres categories: **propietari** · **grup** · **resta**

**Exemple**: Directori `oslabadmin grup1 0750`
- Propietari: rwx (7)
- Grup: r-x (5)
- Resta: --- (0)

> [!tip] Suma els valors: rwx = 4+2+1 = 7.

### ACLs (Access Control Lists)

Més granulars que rwx. Per a usuaris individuals i grups específics.
- Comanda: `setfacl -option file_owner:file_permission filename`

### Creació de fitxers nous

| Mecanisme | Què controla | Idea clau |
|---|---|---|
| **setgid** en directori | Grup propietari | Nous elements hereden el grup |
| **umask** | Permisos rwx | Elimina permisos al crear |
| **ACL per defecte** | Permisos granulars | Permisos heredables |

**Disseny de controls**: denegar per defecte · comprovar operacions protegides · reduir complexitat · disseny públic + claus secretes

---

## 8. UNIX: Processos i UIDs (D38-39)

Cada procés té **3 UIDs**:

| UID | Nom | Funció |
|---|---|---|
| **RUID** | Real User ID | Qui va llançar el procés |
| **EUID** | Effective User ID | **Permisos reals** del procés |
| **SUID** | Saved User ID | EUID abans del canvi |

- **root** pot canviar els tres
- Usuaris normals **només** poden canviar l'EUID
- `setuid(x)` → canvi temporal d'EUID

> [!warning] L'**EUID** és el que importa per permisos. Molts processos comencen com a root i fan `fork`.

---

## 9. Buffer Overflow (D40-49)

### Què és

Un programa **sobreescriu** la memòria d'un buffer, superant-ne la mida.

**Exemple**: `gets(buffer)` amb buffer de 10 bytes. El call stack:
1. **Return address of main**
2. **Punter base (EBP)**
3. **Espai per al buffer** (10 bytes)

Si s'insereixen **>10 caràcters** → desbordament. Pot sobreescriure l'adreça de retorn → control del flux d'execució.

> [!warning] `gets()` no comprova longitud. Mai usar-la en codi real.

### Conseqüències

- Corrupció de dades
- Execució de codi maliciós
- Elevació de privilegis
- DoS
- Fuga d'informació
- Compromís del sistema

### Tipus

| Tipus | Descripció |
|---|---|
| **Stack overflow** | Desbordament de la pila de crides |
| **Heap overflow** | Desbordament de memòria dinàmica |

### Memòria de dades vs executable (D49)

- Codi i dades = bits iguals, però permisos diferents
- Pàgina no executable → CPU impedeix interpretar instruccions (injecció directa impossible)
- Eines: `mprotect`, `mmap`, `cat /proc/<PID>/maps`, `pmap <PID>`

---

## 10. Proteccions contra buffer overflow (D50-56)

| Mecanisme | Què fa |
|---|---|
| **Canari (Canary)** | Valor aleatori al stack. Si se sobreescriu → "stack smashing detected" i abort |
| **ASLR** | Aleatoritza ubicació de pila, heap i biblioteques → impossible predir on és el codi |
| **DEP** | Marca pila/heap com **no executables** → impedeix execució de codi inyectat |
| **PIE** | Executable es carrega en adreces diferents cada execució → complementa ASLR |
| **Limitació de longitud** | Comprovar mida abans de copiar al buffer |
| **Funcions segures** | `fgets()` en lloc de `gets()`, `strncpy()` en lloc de `strcpy()` |
| **Actualitzacions** | Aplicar patches de seguretat |

> [!tip] **ASLR + DEP + PIE** = les tres proteccions més importants. Canari = primera línia de defensa del compilador.

```bash
gcc overflow.c -o overflow -fno-stack-protector  # SENSE canari
gcc overflow.c -o overflow -fstack-protector      # AMB canari (default Linux)
```

---

## Resum ràpid (FITXA)

| Concepte | Clau |
|---|---|
| **CIA** | Confidencialitat · Integritat · Disponibilitat |
| **Amença vs Vulnerabilitat vs Riesgo** | Algu intenta / debilitat explotable / probabilitat+impacte |
| **CVE** | Estàndard públic per catalogar vulnerabilitats |
| **MULTICS** | SO pioner en seguretat (1965-2000) |
| **Defensa multinivel** | Protecció a cada capa: app → procés → SO/hardware |
| **Menor privilegi** | Només l'estrictament necessari |
| **Separació de privilegis** | Sistema segmentat, no tot amb el mateix accés |
| **Política** | Sujet + Objecte + Operació |
| **UID/GID** | root=0, cada usuari/grup té el seu ID |
| **rwx** | r=4 · w=2 · x=1 → suma = número d_permís |
| **ACL** | Permisos més granulars que rwx |
| **RUID/EUID/SUID** | EUID = permisos reals (el que importa) |
| **Buffer overflow** | Sobreescriptura de memòria → control de flux |
| **Canari** | Valor aleatori al stack → detecta desbordament |
| **ASLR** | Aleatoritza zones de memòria |
| **DEP** | Memòria no executable |
| **PIE** | Executable en adreces diferents |

---

## Dubtes / a revisar

- 

## Enllaços relacionats

*(notes atòmiques integrades en aquest resum)*
