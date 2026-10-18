---
id: T2-Maquines-Virtualitzacio-SO
aliases: []
tags:
  - tipus/teoria
  - assignatura/SO
assignatura: SO
data: "2026-10-01"
---

# T2 — Màquines Virtuals i virtualització del SO

**Referència: PDF 02 — Máquinas virtuales y virtualización del SO (Parte 1)**

---

## 1. Repàs: el SO com a màquina estesa

- Un SO es pot veure com una **màquina estesa**:
  - Amaga al usuari tots els **mecanismes complexos** que es fan internament (ex: accés a dispositius)
  - Ofereix al usuari una **MV** i una **interfície** (crides al sistema), facilitant-ne l'ús
- El SO permet executar **processos** (instàncies de programes):
  - Cada procés té la **il·lusió** de fer servir tota la màquina (100% recursos)
  - Executa instruccions en **mode usuari** i accedeix als dispositius d'E/S a través del SO
  - Un *bug* o un *malware* **no hauria d'afectar** la resta de processos (**aïllament**)
  - Cap procés **no hauria de consumir** tots els recursos en detriment de la resta
- El SO ho aconsegueix **gestionant els recursos** disponibles i amb tècniques de **time-sharing** del hardware

> [!question]- timesharing: en què es compartia?
> En el **hardware** (CPU, memòria, dispositius...). Es parteix en intervals de temps i es turna entre processos: a cada procés li toca un trosset i creu que té la màquina sencera.

---

## 2. La JVM (exemple de MV de procés)

- A Java, el **JVM** executa el codi **on sigui** i **oculta a l'usuari** la màquina virtual on s'executa
- Filosofia: **abstrau el hardware** subiacent i ofereix un entorn d'execució virtualitzat per a aplicacions Java → **"write once, run anywhere"** (independent del hardware)
- **Facilita les trucades al sistema**: la JVM es comunica amb el SO de sota
- El SO permet **instanciar** múltiples JVMs (cadascuna, la seva MV de procés)

---

## 3. Què és una MV? Els SO són MV?

### Definició (VMware)

- **MV** (*Virtual Machine*): un recurs de càlcul que usa **software en lloc d'un ordinador físic** per executar programes i desplegar apps
- Un o més **"guest" virtuals** s'executen sobre un **"host" físic**
- Cada MV té el **seu propi SO** i funciona **separada** de la resta, fins i tot totes al mateix host → ex: una MV de macOS sobre un PC Windows

### Estrictament, un SO **no és** una MV

- Un SO té **accés directe al hardware** i és l'**únic software que el controla**
- Ofereix un nivell d'abstracció als processos: memòria infinita, 100% de CPU... (**il·lusió**), garantint-ne la seguretat
- Les **llibreries d'usuari** (`libc`, `printf`, `fwrite`...) faciliten fer servir les eines que ofereix el SO

> [!warning] Restriccions del SO: està dissenyat per a **una arquitectura determinada**, executa un **conjunt d'instruccions** concret i és l'únic que controla el hardware → **limitem la flexibilitat** del sistema. D'aquí neix la virtualització.

---

## 4. Activitat: virtualitzar o no?

- **Virtualitzar** → més barat: poques màquines físiques aguanten moltes MVs
- Però: **menys rendiment** que hardware dedicat
- **Risc**: si peta el servidor on són, **peten totes** les MVs que hi ha a sobre

*(Escenari de l'activitat: una empresa necessita desplegar 50 servidors lògics per a una app web, amb pressupost limitat i necessitat de seguretat, flexibilitat i alta disponibilitat. Què triaríeu? I si un físic amb 10 MVs falla, què en fem?)*

---

## 5. La virtualització

- **Definició**: procés d'**abstraure els recursos físics** d'un sistema (CPU, memòria, emmagatzematge, xarxa) per crear **entorns virtuals independents** que s'executen de forma **simultània i aïllada** sobre un **mateix sistema físic**
- Objectiu: donar **més flexibilitat** a les restriccions del SO
- En virtualitzar, la **interfície i els recursos del sistema virtual es mapegen** als del sistema real:
  - Ex: una targeta gràfica o de xarxa **virtual** pot ser diferent de la física

### Components habituals d'una MV

| Component | Què és |
|---|---|
| **Host** | Sistema físic real |
| **VMM** (*Virtual Machine Manager*) | aka **hypervisor**. Responsable de la virtualització/emulació. Té la funcionalitat d'un ordinador físic (pot oferir-ne un de diferent al real) i pot executar diverses MVs |
| **MV / Guest** | Còpia virtual del host. Típicament, el procés guest **és un SO** |

---

## 6. Virtualització vs emulació

**Clau: mira la CPU.** No és una cosa de kernels, és d'**arquitectura** (ISA) sencera.

| | **Virtualització** | **Emulació** |
|---|---|---|
| Arquitectura | Hardware físic i virtual = **la mateixa** | El hardware virtual **simula una arquitectura diferent** de la física |
| Exemple | VirtualBox executant **Ubuntu** en un PC **Intel/AMD** | **QEMU** emulant una CPU **ARM** sobre un PC **x86** |
| Més exemples | — | Consoles antigues (**PlayStation**) emulades en un PC modern |
| Rendiment | Més ràpid | Més lent (compatibilitat a canvi de rendiment) |

> [!tip] Resum en una frase: **mateixa CPU → virtualització · CPU diferent → emulació**.

---

## 7. Els SOs guest, el mode usuari i VT-x / trap-and-emule

- Cada SO es dissenya per tenir el **control total del hardware**
- A una MV, el VMM:
  - Fa **creure** a cada **SO guest** que té el control total del sistema (encara que **s'executa en mode usuari**)
- Els processadors més modernos inclouen **instruccions de màquina** que faciliten això; a les arquitectures **x86** se'n diuen **instruccions VT-x** (VTX)
- Amb elles es fa el **trap-and-emule**:
  1. Un SO guest fa una operació **no permesa** (ex: escriure dades a disc)
  2. El processador la **captura** (*trap*)
  3. El **VMM executa** el que volia fer el guest; gràcies al **mapeig** de la MV, s'executa realment allò que el guest demanava

> [!note] **Temps relatiu a la MV**: dins una MV, quan **no se li assignen recursos de temps**, queda **"congelada"**. El temps que passa "dins" la MV **no és el temps real**, és relatiu a la MV.

---

## 8. Tipus de MVs (segons l'hipervisor)

![[Tipus-Hypervisors-Type-1-Type-2.png]]

### Type 0

- **On va**: dins el hardware / **firmware** (el més bàsic)
- Poc comú
- Solucions basades en **hardware** amb suport per crear MVs i gestionar-les via ***firmware***
- Software **mínim** necessari per virtualitzar completament els guests i controlar el flux d'informació entre ells

### Type 1 (*native* / *bare metal*)

- **On va**: directament sobre el **hardware** (**no hi ha SO host**)
- La VMM s'instal·la al servidor i **s'executa directament sobre el hardware**
- Actua com un **SO que permet executar i gestionar altres SOs** i proveeix serveis tradicionals de SO (planificació, gestió de memòria)
- Es fan servir en **grans servidors**
- Una única màquina executa **múltiples SOs simultanis**, cadascú amb la seva MV i **creient que té el control total**
- Exemple: **VMware ESXi** ("bare metal" on normalment s'instal·la el SO)

### Type 2 (*hosted*)

- **On va**: sobre el **SO del host** (com un procés més)
- El SO del host és **convencional**; l'hipervisor s'executa **com un procés** dins el host
- Té la seva capa de virtualització que abstrau el hardware
- Cada MV té la seva **CPU virtual, memòria, discs, xarxa**...
- El disc d'una MV **és un fitxer al host**: copiar-lo/clonar-lo = una MV idèntica
- Exemple: **VMware Workstation**

### Comparació ràpida

| Tipus | On va l'hipervisor | Exemple |
|---|---|---|
| **Type 0** | Firmware (dins el hardware) | — |
| **Type 1** | Directament sobre el **hardware** (sense SO host) | VMware ESXi |
| **Type 2** | Sobre el **SO host** (com a procés) | VMware Workstation |

> [!tip] **Jerarquia, de baix a dalt**: type 0 = **firmware** (el més bàsic, dins el hardware) · type 1 = VMM directament sobre el **hardware** (sense SO host) · type 2 = hipervisor sobre el **SO host** (els "guests" són els SOs de les MVs, un nivell més amunt).

> [!info] **Whonix**: no és un hipervisor tipus 1. Són **dues MVs** (Workstation + Gateway) que es cremen sobre un **hipervisor type 2** (VirtualBox/QEMU). El patró type 1 és l'ESXi: instal·lat directament on normalment va el SO, "saltant-se" el SO host.

---

## 9. Tipus de MV segons la funcionalitat

### MVs de sistema

- Executen un **SO** complet
- Inclouen els **type 1 i 2**
- Proveeixen un **sustitut d'una MV** i permeten oferir a cada SO el seu **hardware virtual**

### MVs de procés

- Executen un **procés** en un entorn **independent de la plataforma**
- La VMM **no virtualitza hardware real** sinó un **sistema virtual abstracte**
- Ex: JVM → **bytecodes** (codi de màquina d'una màquina abstracta)

---

## 10. Valgrind

- Eina de programació per a **depuració de memòria**, **detecció de fuges de memòria** i **creació de perfils**
- Definició resumida (en anglès):

> [!quote] "*Valgrind is in essence a **virtual machine** using just-in-time (JIT) compilation... **Nothing from the original program ever gets run directly on the host processor**.*"
> En resum: és una **MV de procés** que **no executa mai el codi original directament** al host: el tradueix a un **IR** (*Intermediate Representation*) i el **recompila**.

- **Benefici**: detecta fuites i errors de memòria en binaris ja compilats, sense tornar-los a compilar amb debug
- **Desavantatge**: rendiment (tot passa per IR + recompilació → overhead)

---

## 11.Beneficis de les MVs

### Beneficis i característiques

- **Virtualització d'escriptoris**: escriptoris virtuals per a una organització (ex: la Facultat durant la pandèmia)
- **Virtualització de servidors**: una màquina física gestiona múltiples servidors; **si un falla, els altres no es veuen afectats**
- **Recursos**: pots subcontratar (empresa especialitzada en infraestructures de MVs) si necessites grans recursos
- **Aïllament + recursos restringits**: un usuari pot tenir una MV amb menys CPU/RAM de la que realment té la màquina
- La virtualització permet **parar** una MV, **copiar-la** (clonar), **moure-la**, **guardar-la**...
- Facilita el **desenvolupament i test** de nous SO i d'aplicacions en diferents SOs alhora

> [!info] Qui en fa servir: AWS, Microsoft Azure, Google Cloud Platform, IBM Cloud... (empreses de tots els tamanys externalitzen serveis amb MVs per escalabilitat)

---

## 12. En resum (del professor)

- La virtualització proveeix una **duplicació del hardware** subjacent
- A les **MVs de sistema**, cada VM pot executar un **SO diferent** i oferir un **hardware diferent** a cada SO
- Els dissenyadors de CPUs hi afegeixen cada cop més característiques per facilitar el **suport a la virtualització**
- Aquesta arquitectura té una **complexitat alta**: per a determinades aplicacions és més útil la **virtualització a nivell de SO** (propera sessió)

---

## Resum ràpid (FITXA)

| Concepte | Clau |
|---|---|
| **MV** | Recurs de càlcul amb software en lloc d'ordinador físic; guests sobre host, cada un amb el seu SO |
| **SO = MV?** | Estrictament **no**: accés directe al hardware, únic que el controla |
| **Time-sharing** | Compartir el **hardware** per temps → il·lusió de 100% a cada procés |
| **Virtualització** | Abstraure recursos físics → entorns independents, simultanis i aïllats sobre un físic |
| **Components MV** | **Host** (físic) · **VMM/hypervisor** · **Guest** (còpia virtual, típic un SO) |
| **Virtualització vs emulació** | **Mateixa arquitectura** vs **arquitectura diferent** simulada |
| **Trap-and-emule** | Guest fa op no permesa → **trap** del processador → **VMM l'emula** |
| **VT-x (VTX)** | Instruccions x86 que faciliten la virtualització |
| **Temps de la MV** | Relatiu a la MV: sense recursos, queda "congelada" |
| **Type 0** | Firmware/hardware, el més bàsic |
| **Type 1** | VMM sobre **bare metal** (sense SO host); grans servidors; VMware ESXi |
| **Type 2** | Hipervisor com a **procés** sobre el SO host; VMware Workstation |
| **MV de sistema vs procés** | SO complet vs procés (JVM → bytecodes, Valgrind) |
| **Valgrind** | MV de procés: no executa el codi directament, ho tradueix a IR i recompila |
| **MV: balanç** | Barates, clonables, parables, aïllades, bones per test; **risc**: si peta el server on són, peten totes |

---

## Dubtes / a revisar

- El CVE de Linux que **traspàs de guest a host** era amb el **trap-and-emule / VT-x**? (ho deia a classe)
- **Whonix**: confirmar que es considera type 2 (dues MVs sobre VirtualBox/QEMU), no type 1
- Història/beneficis de Valgrind: el professor en posa alguna pregunta petita de test — repassar-les per separat

---

## Enllaços relacionats

- [[T2b-Contenedors-Docker|T2b — Contenedors i Docker (Parte 2)]]
- [[T1-Introduccio-Seguretat-SO|T1 — Introducció Seguretat SO]]
- [[classe1|Classe 1 — notes brutes (MV i coses)]]
