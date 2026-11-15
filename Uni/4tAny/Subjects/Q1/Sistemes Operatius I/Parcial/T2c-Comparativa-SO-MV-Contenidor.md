---
id: T2c-Comparativa-SO-MV-Contenidor
aliases: []
tags:
  - tipus/teoria
  - assignatura/SO
assignatura: SO
data: "2026-10-24"
---

# T2c — SO, MV i contenidor: on va el kernel i per on passen les crides

**Nota de síntesi sobre el tema 2** (complementa [[T2-Maquines-Virtualitzacio-SO|T2 — MV]] i [[T2b-Contenedors-Docker|T2b — Contenedors i Docker]]). No ve del PDF: és una elaboració pròpia per entendre *per què* es comporten com es comporten.

---

## 1. La pregunta que ho ordena tot

No memoritzis taules. Respon aquestes **tres preguntes** per a cadascun i la resta se segueix solet:

1. **Què es virtualitza?**
2. **Quants kernels hi ha?**
3. **On es processa una crida al sistema?**

| | Què es virtualitza | Quants kernels | On es processa la crida |
|---|---|---|---|
| **Procés** | res | 1 (el del sistema) | Al kernel real |
| **MV** | el **hardware** sencer | 1 **per MV** (el guest) | Kernel **guest** → després **trap** al VMM |
| **Contenedor** | **espai d'usuari** | **1 sol**, compartit | Al **mateix** kernel host |

La fila del **procés** és la base: és l'estat normal sense virtualitzar. Tant la MV com el contenidor són formes de ficar-hi una capa pel mig — però **cap a on**.

---

## 2. Un SO complet = kernel + espai d'usuari

Això és la peça que falta per entendre-ho tot.

Un **sistema operatiu complet** té dues parts ben diferents:

| Part | Què és | Exemples |
|---|---|---|
| **Kernel** | Gestiona el **hardware**: crides al sistema, memòria, CPU, *drivers* | `vmlinuz`, `ntoskrnl.exe` |
| **Espai d'usuari** | Tot el que s'executa **a sobre** i parla amb el kernel | `libc`, `bash`, `systemd`, `ls`, `/usr`, `apt` |

> [!important] La idea central del tema 2
> - Una **MV** se'n porta **els dos**: kernel **+** espai d'usuari
> - Un **contenedor** se'n porta **només un**: l'**espai d'usuari**, i **comparteix el kernel** del host

Un contenedor no és "un Linux petit". És **un directori amb binaries**. No duu kernel perquè **no en pot dur**: per això és lleuger.

---

## 3. Com flueix una crida al sistema

### Sense virtualitzar (procés normal)

```
aplicació            (mode usuari)
   └─ libc
        └─ syscall  ──►  KERNEL  ──►  hardware
                       (mode kernel)
```

Una sola travessia. És el cost base, zero *overhead*.

### Amb MV

```
app del guest        (mode usuari, dins la MV)
   └─ libc del guest
        └─ syscall ──► KERNEL GUEST
                          └─ vol tocar hardware ──► TRAP ──► VMM / hipervisor
                                                               └─► KERNEL HOST
                                                                      └─► hardware
```

- La trucada de l'aplicació **sí que arriba a un kernel**: el del **guest**
- El problema és que aquell kernel **creu que controla la màquina** i intenta fer operacions **privilegiades** (escriure a disc, canviar registres...)
- El processador el **captura** (*trap*) i l'hipervisor ho **emula** → **trap-and-emulate** (amb **VT-x** a x86)
- **Dues capes de kernel** pel mig → és d'on surt l'*overhead* de les MVs

### Amb contenedor

```
app del contenedor   (mode usuari)
   └─ libc de la imatge del contenedor
        └─ syscall  ──►  KERNEL HOST   (l'únic)
                            └─► hardware
```

- **No hi ha traducció**. El procés fa la crida **directament al kernel real**
- El que ha canviat és **què ve** el procés (noms de fitxers, PIDs, xarxa, usuaris), **no com** es fan les trucades
- Per això el rendiment és gairebé **nadiu** i l'arrencada és de **segons**

> [!tip] Resum en una frase
> **La MV intercepta les crides. El contenedor les deixa passar i els canvia la vista.**

---

## 4. Aïllament: imposició vs cooperació

La diferència de *per què* no es poden barrejar els dos models:

**MV → aïllament per imposició.** El guest té una **màquina sencera virtual**. Simplement **no existeix cap instrucció** per sortir-ne ni per tocar el hardware real. No depèn de la bona voluntat de ningú.

**Contenedor → aïllament per filtratge.** El kernel és **el mateix** que el del host, així que l'aïllament és **cooperatiu**: el procés fa consultes normals al kernel, i el kernel **les respon amb camps filtrats**.

### Què filtra el kernel: namespaces i cgroups

| | Què fa | Què controla | Exemples |
|---|---|---|---|
| **Namespaces** | **Aïlla** | Què **veu** el procés | PID, muntatge, xarxa, usuaris, UTS (hostname), IPC |
| **Cgroups** | **Limita** | Quant **pot consumir** | memòria, CPU, E/S de disc, nombre de processos |

Detall que cal retenir: **no simulen hardware**. Són **camps filtrats** que el kernel posa a les respostes de les consultes dels processos.

- Cada procés dins un contenedor té el **seu propi PID**, començant per 1 — però per al kernel **continua sent un procés qualsevol** amb un PID real de tota la vida
- El *hostname*, la llista de fitxers de `/`, la targeta de xarxa... tot és **la mateixa visió filtrada**

### Conseqüència de seguretat

> [!warning] El preu del model
> A la MV, un *exploit* del kernel guest s'ha d'esforçar per sortir de la màquina virtual. Al contenidor, **el kernel és compartit**: qualsevol *bug* del kernel host (**lato sensu**) és un risc per a **tots** els contenidors alhora. Per això el mode *root* dins un contenidor és perillós (*privilege escalation*).

---

## 5. Conseqüències pràctiques (tot se'n segueix)

| | MV | Contenedor |
|---|---|---|
| Pesa | **GB** (duu SO complet) | **MB** (només espai d'usuari) |
| Arrenca | minuts | **segons** |
| Executa un kernel diferent? | **Sí** (Windows sobre Linux) | **No** |
| Aïllament | Fort (imposició) | Més feble (cooperatiu) |
| Rendiment | *Overhead* per trap | Gairebé **nadiu** |
| Què cal instal·lar | SO sencer cada cop | Només l'aplicació i les llibreries |

> [!question]- Per què un contenedor **no pot** executar Windows sobre Linux?
> Perquè **no porta kernel**. Porta només l'espai d'usuari, i el kernel que l'executa és el del host (Linux). Un espai d'usuari de Windows **necessita el kernel de Windows** per funcionar.

> [!question]- I llavors com funciona Docker a Windows?
> Perquè **es posa un kernel de debò**: Docker Desktop fa servir **Hyper-V** o **WSL 2**, que és un **kernel Linux real construït per Microsoft**. El contenidor no aporta el kernel — el **necessita ja present**. Sense WSL2/Hyper-V no hi ha kernel Linux, i sense kernel Linux no hi ha contenidor.

Aquestes dues preguntes són la prova de si ho has entès de debò.

---

## 6. On encaixa tot el que ja saps

| Concepte | On va |
|---|---|
| **Type 1 / Type 2** (T2) | És **on va l'hipervisor**: sobre hardware, o sobre el SO host. No canvia quantes capes de kernel hi ha entre l'aplicació i la màquina |
| **Trap-and-emulate / VT-x** (T2) | Mecanisme **exclusiu de les MVs**. Els contenidors **no hi entren mai**: no fan operacions privilegiades, fan crides normals |
| **JVM** (T2) | **MV de procés** — no virtualitza hardware, virtualitza una **ISA abstracta** (bytecodes). És un cas diferent de tots dos |
| **Valgrind** (T2) | També MV de procés: recompila via IR |
| **chroot / jail** (T2b) | L'avantpassat del contenedor: **només** filtrava la vista de fitxers (un sol namespace) |
| **cgroups + namespaces** (T2b) | El que fa que el contenedor sigui més que un `chroot` |

### Jerarquia completa en un host real

```
Hardware
  └─ KERNEL HOST (l'únic)
       ├─ procés: contenedor A        ← fa syscall directe
       ├─ procés: contenedor B        ← fa syscall directe
       └─ procés: hipervisor type 2
            └─ MV ── kernel guest ── trap ──► (torna al kernel host)
```

Fixa't que **tot acaba al mateix kernel**. La diferència és quantes capes s'hi arriba abans.

---

## 7. Errors freqüents

- **"El contenedor és una MV petita"** — no. No té hardware virtual, no té kernel propi, no fa trap-and-emulate
- **"Els contenidors són més segurs que les MVs"** — depèn del que mesuris. Aïllament **estructural**: guanya la MV. Velocitat de desplegament i eficiència: guanya el contenidor
- **"Amb `--privileged` un contenedor és segur"** — és el contrari: desactiva gairebé tots els mecanismes d'aïllament
- **"Docker al Mac executa contenidors Linux nadiu"** — no; passa per una MV de Linux (Hyper-V / WSL 2). A Linux, Docker **sí** que és nadiu
- **Confondre virtualització amb emulació** — és cosa d'**arquitectura** (ISA), no de capes de kernel (veure T2 §6)

---

## Resum ràpid (FITXA)

| Concepte | Clau |
|---|---|
| **SO complet** | **Kernel + espai d'usuari**. És la clau de tot |
| **MV** | Es porta **els dos** (kernel + espai). Virtualitza el **hardware** |
| **Contenedor** | Es porta **només l'espai d'usuari** i **comparteix el kernel** del host |
| **Crida al sistema (MV)** | Arriba al **kernel guest** → operació privilegiada → **trap** → VMM → kernel host |
| **Crida al sistema (contenedor)** | Va **directa** al **kernel host**. Zero traducció |
| **Aïllament MV** | Per **imposició**: el guest no té com sortir-ne |
| **Aïllament contenedor** | Per **filtratge cooperatiu** del mateix kernel |
| **Namespaces** | Què **veu** el procés: PID, muntatge, xarxa, usuaris, UTS, IPC |
| **Cgroups** | Quant **pot consumir**: memòria, CPU, E/S, processos |
| **Per què pesa MB** | No duu kernel ni SO sencer |
| **Per què no pot executar Windows** | No té kernel propi → necessita el del host |
| **Docker a Windows** | Cal un **kernel Linux real**: Hyper-V / WSL 2 |
| **Risc compartit** | El kernel és únic: un *bug* afecta **tots** els contenidors |

---

## Dubtes / a revisar

- Confirmar amb el professor si a l'examen es demana **dibuixar** el diagrama de fluxe de crides (T2 §7) o només descriure'l
- El **CVE de Linux que passava de guest a host** que va comentar a classe (apuntat a T2) — encaixa aquí: un *bug* del kernel host és el risc compartit del model de contenidors
- Si vols practicar-ho a la VM: `ls -l /proc/1/ns/` dins un contenidor vs al host mostra que els namespaces són **diferents** però el kernel, **el mateix**

---

## Enllaços relacionats

- [[T2-Maquines-Virtualitzacio-SO|T2 — Màquines Virtuals i virtualització del SO]]
- [[T2b-Contenedors-Docker|T2b — Contenedors i Docker]]
- [[T1-Introduccio-Seguretat-SO|T1 — Introducció Seguretat SO]]
- [[T3-Sistemes-Fichers-P2|T3 — Sistemes de fitxers (Parte 2)]]
