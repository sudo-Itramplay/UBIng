---
id: Qüestions-T2-MV-Contenidors
aliases:
  - Qüestions T2
tags:
  - tipus/parcial
  - assignatura/SO
assignatura: SO
data: "2026-10-30"
---

# Qüestions — T2 MVs i Contenidors

Banc de preguntes del **Tema 2** (MVs, virtualització i contenidors), en el mateix format que [[Qüestions-T1-Seguretat|Qüestions T1 — Seguretat]]: **concepte** ( dels apunts de classe) → **pregunta** (en castellà, com els tests) → **resposta** → **per què sí i per què les altres no**.

Font: [[T2-Maquines-Virtualitzacio-SO]], [[T2b-Contenedors-Docker]], [[T2c-Comparativa-SO-MV-Contenidor]] i el test ràpid de [[T3-Sistemes-Fichers-P1#1. Test ràpid del bloc anterior (MV / contenidors)|T3-P1 §1]].

> [!tip] Per a què serveix
> El **Problema 2** del parcial 2026-2027 té els apartats **a) i b) ocults** i, segons el professor, són **preguntes de teoria del Tema 2**. Aquí tens les respostes preparades per a tot el temari del bloc.

---

## P1 — Què és una MV

### Concepte

Una **MV** (*Virtual Machine*) és un recurs de càlcul que usa **software en lloc d'un ordinador físic** per executar programes i desplegar apps. Un o més **guests virtuals** s'executen sobre un **host** físic; cada MV té el **seu propi SO** i funciona separada de la resta (fins i tot totes al mateix host).

### Pregunta

¿Cuál de las siguientes afirmaciones describe mejor una máquina virtual?

- [ ] Un compilador que genera código para otra arquitectura
- [x] **Un sistema que emula hardware para ejecutar SOs invitados**
- [ ] Un hypervisor que se encarga de las llamadas al sistema
- [ ] Un contenedor que comparte el kernel del host

### Per què la B sí

Definició literal de la classe: la MV **emula el hardware** per poder executar SOs *invitados*. El terme "emula" aquí és el del PPT (la MV presenta un hardware diferent del real).

### Per què les altres no

- **Compilador**: no té res a veure; un compilador tradueix codi, no crea màquines.
- **Hypervisor**: descriu el paper del VMM (component que assigna i gestiona els recursos del host), no de la MV.
- **Contenedor**: el contenidor **comparteix el kernel** del host i no emula hardware → és el model de virtualització a nivell de SO, no una MV.

---

## P2 — Qui assigna els recursos del host

### Concepte

El **VMM** (*Virtual Machine Manager*), aka **hypervisor**, és el component que fa la virtualització/emulació: té la funcionalitat d'un ordinador físic i **assigna i gestiona els recursos**， pot oferir-ne un de diferent al real, i pot executar diverses MVs.

### Pregunta

¿Qué componente de una máquina virtual se encarga de asignar y gestionar los recursos físicos del host?

- [ ] El sistema operativo guest
- [x] **El hypervisor o Virtual Machine Manager (VMM)**
- [ ] Docker Engine
- [ ] El kernel del SO host

### Per què la B sí

És la definició de VMM/hypervisor: gestiona i assigna els recursos (**planificació, memòria, E/S**) de la màquina física a cada MV.

### Per què les altres no

- **SO guest**: gestiona el seu *entorn virtual*, no els recursos del host.
- **Docker Engine**: és el gestor de **contenidors**, no d'hipervisors.
- **Kernel del host**: és el del sistema on corre l'hipervisor, no el component que fa la virtualització.

---

## P3 — trap-and-emulate

### Concepte

A una MV, el VMM fa creure a cada SO guest que té el control total del sistema, encara que s'executa en mode usuari. Quan el guest fa una operació **no permesa** (escriure a disc, canviar registres…):

1. el processador la **captura** (*trap*),
2. el **VMM executa** realment allò que el guest demanava (gràcies al mapeig de la MV).

A x86 hi ha les instruccions **VT-x (VTX)** que ho faciliten.

### Pregunta

En el contexto de virtualización, en qué consiste el mecanismo "trap-and-emulate"?

- [x] **Interceptar instrucciones privilegiadas y ejecutarlas en el hipervisor**
- [ ] Traducir el código de la MV a código nativo del host
- [ ] Compartir el espacio de memoria entre host y guests
- [ ] Enviar señales al SO guest

### Per què la A sí

És literalment el mecanisme: el processador captura (*trap*) la instrucció privilegiada i el hipervisor la **emula**.

### Per què les altres no

- **Traducir código**: és el que fa Valgrind (MV de procés amb IR), no el mecanisme del hypervisor.
- **Memòria compartida**: no forma part del trap-and-emulate (encara que el mapeig de la MV impliqui traducción d'adreces).
- ** senyals**: no tenen res a veure amb la captura d'instruccions privilegiades.

> [!warning] Els **contenidors mai utilitzen trap-and-emulate**
> Un contenidor fa les crides al sistema **directes al kernel host**: no fa operacions privilegiades, no hi ha *trap*. (T2c §3)

---

## P4 — Contenidors: identifica la INCORRECTA

### Concepte

Els contenidors **no simulen hardware complet**: comparteixen el **kernel** del SO host (només porten l'espai d'usuari), són més lleugers que les MVs i es basen en **namespaces** i **cgroups**.

### Pregunta

Identifica la afirmación INCORRECTA sobre los contenedores:

- [ ] Comparten el kernel del sistema operativo host
- [ ] Son más ligeros que las máquinas virtuales
- [x] **Simulan hardware completo**
- [ ] Se-basis en namespaces y cgroups

### Per què la C és la resposta

És fals: el contenidor **comparteix el kernel** del host; no emula hardware. (a), (b) i (d) són vertaderes.

### Per què les altres són correctes

- **Comparten el kernel**: el contenidor només aporta l'**espai d'usuari**.
- **Més lleugers**: pesen **MB** (les MVs, GBs) i arrenquen en **segons**.
- **namespaces + cgroups**: són les tecnologies Linux que hi ha al darrere.

---

## P5 — Avantatge principal dels contenidors

### Concepte

Contenidors: **ràpids i lleugers** (MBs vs GBs, arrencada en segons), **portables** (porten totes les llibreries), **eficients** (crides al sistema directes al SO host, sense hypervisor), **aïllats** (espais d'usuari separats) i **fàcils de distribuir**.

### Pregunta

¿Qué ventaja principal ofrecen los contenedores frente a las máquinas virtuales en el desarrollo de software?

- [x] **Arranque más rápido y menor consumo de recursos**
- [ ] Poder ejecutar un sistema operativo diferente en cada contenedor
- [ ] Mayor aislamiento de seguridad frente a una VM
- [ ] Eliminar la necesidad de un sistema operativo host

### Per què la A sí

Arrencada en **segons** i consum **MBs**: és el avantatge que es destaca a classe.

### Per què les altres no

- **SO diferent per contenidor**: **impossible** — el contenidor no porta kernel (porta només espai d'usuari i necessita el kernel del host). Qui pot fer-ho és la **MV**.
- **Major aïllament de seguretat**: és al revés — la MV aïlla per **imposició**; el contenidor comparteix kernel → un *bug* del kernel afecta tots els contenidors.
- **Eliminar el SO host**: fals, el contenidor **s'executa sobre** el SO host.

---

## P6 — docker image vs docker container

### Concepte

- **Imatge**: *captura de l'estat* d'un contenidor → **plantilla** per crear contenidors.
- **Contenidor**: **instància en execució** d'una imatge.
- D'una imatge en poden sortir **varis contenidores**.

### Pregunta

¿Qué diferencia existe entre docker image y docker container?

- [ ] La imagen se ejecuta y el contenedor es crea
- [ ] Son exactamente lo mismo
- [x] **La imagen es la plantilla; el contenedor es su instancia en ejecución**
- [ ] El contenedor es una máquina virtual

### Per què la C sí

Definició de classe: imatge = plantilla; contenidor = instància en execució.

### Per què les altres no

- **La imatge s'executa**: no, la imatge no s'executa; el que s'executa és el contenidor.
- **Són el mateix**: no, una és la plantilla i l'altre la instància.
- **El contenidor és una MV**: no, és virtualització a nivell de SO.

---

## P7 — Virtualització vs emulació

### Concepte

La clau és **mirar la CPU**: no és una cosa de kernels, és d'**arquitectura (ISA)**.

| | **Virtualització** | **Emulació** |
|---|---|---|
| Arquitectura | Hardware contending i virtual = **la mateixa** | El hardware virtual **simula una arquitectura diferent** |
| Exemple | VirtualBox executant Ubuntu en un PC Intel/AMD | **QEMU emulant una CPU ARM** sobre un PC x86; consoles antigues emulades |
| Rendiment | Més ràpid | Més lent |

> **mateixa CPU → virtualització · CPU diferent → emulació**

### Pregunta

¿Cuál es la diferencia entre virtualización y emulación?

- [x] **La emulación simula una arquitectura (ISA) diferente a la del hardware físico**
- [ ] La virtualización usa un hypervisor y la emulación no
- [ ] La emulación es siempre más rápida que la virtualización
- [ ] Solo se puede emular en máquinas con hypervisor type 1

### Per què la A sí

És la definició de classe: emulació = hardware virtual que simula una **arquitectura diferent** de la física.

### Per què les altres no

- **El hypervisor**: hi ha emuladors que no són hypervisors; la distinció no hi va.
- **Sempre més ràpida**: és al revés, l'emulació és **més lenta** (compatibilitat a canvi de rendiment).
- **Només type 1**: fals.

---

## P8 — Tipus d'hipervisor

### Concepte

| Tipus | On va l'hipervisor | Exemple |
|---|---|---|
| **Type 0** | Dins el **firmware** (el més bàsic) | — |
| **Type 1** (*bare metal*) | Directament sobre el **hardware**, **sense SO host**; grans servidors | **VMware ESXi** |
| **Type 2** (*hosted*) | Sobre el **SO host**, com un **procés** més | **VMware Workstation**, VirtualBox |

### Pregunta

¿Sobre qué se instala un hipervisor de tipo 1 (bare metal)?

- [ ] Sobre el sistema operativo del host, como un proceso más
- [x] **Directamente sobre el hardware, sin sistema operativo host**
- [ ] Dentro del firmware de la máquina
- [ ] Dentro de un contenedor

### Per què la B sí

Type 1 = *bare metal*: la VMM s'executa **directament sobre el hardware** i fa les funcions d'un SO (planificació, memòria) → grans servidors.

### Per què les altres no

- **Sobre el SO host**: això és el **type 2**.
- **Dins el firmware**: això és el **type 0**.
- **Dins un contenedor**: un contenidor **no porta kernel** → no hi pot haver cap hipervisor.

---

## P9 — Namespaces vs cgroups

### Concepte

| | Què fa | Què controla | Exemples |
|---|---|---|---|
| **Namespaces** | **Aïllen** | **Què VEU** el procés | PID, muntatge, xarxa, usuaris, UTS (hostname), IPC |
| **Cgroups** | **Limiten** | **Quant pot consumir** | memòria, CPU, E/S de disc, nombre de processos |

Cap dels dos **simula hardware**: són **camps filtrats** que el kernel posa a les respostes de les consultes dels processos.

### Pregunta

¿Qué controla el mecanismo de namespaces en Linux?

- [ ] El consumo máximo de CPU y memoria del proceso
- [x] **Lo que el proceso ve: PIDs, sistema de ficheros, red, usuarios**
- [ ] El hardware que ve la máquina virtual
- [ ] Las llamadas al sistema que se ejecutan en modo kernel

### Per què la B sí

Els namespaces **aïllen la vista**: cada procés dins d'un contenidor veu el **seu propi PID** (començant per 1), el seu sistema de fitxers, la seva xarxa, el seu hostname.

### Per què les altres no

- **CPU i memòria**: això ho fan els **cgroups** (limitar), no els namespaces.
- **El hardware de la MV**: els contenidors no emulen hardware.
- **Les crides al sistema en mode kernel**: els contenidors fan crides **directes** al kernel host; no hi ha cap canvi de mode (a diferència de la MV, on el guest creu al kernel i fa *trap*).

---

## P10 — Registre d'imatges, repositori i etiqueta

### Concepte

- **Docker Registry / Docker Hub**: **repositori** on es pengen les imatges (fitxers que permeten generar el contenidor).
- **Imatge**: captura de l'estat d'un contenidor → plantilla.
- **Tag**: punter a una versió concreta d'una imatge dins del repositori (`ubuntu:22.04`).
- **Digest**: identificador **immutable** (el tag és mutable).

### Pregunta

¿Qué es un repositorio en Docker Hub?

- [x] **Un conjunto de imágenes (contenedoras), que pueden tener distintas etiquetas (tags)**
- [ ] Un espacio de trabajo donde se edita el Dockerfile
- [ ] Una máquina virtual con Docker instalado
- [ ] El directorio local donde se guardan las imágenes descargadas

### Per què la A sí

El repositori és el contenidor lògic d'**imatges**; cada versió concreta s'hi identifica amb un **tag**.

### Per què les altres no

- **Espai de treball del Dockerfile**: el Dockerfile és un fitxer de text pla (estil *makefile*) per **crear** imatges.
- **MV amb Docker**: no té res a veure.
- **Directori local**: allà hi ha les imatges **descàrregades** (`docker images`), que provenen del registre.

> [!warning] `:latest` és perillós
> `latest` és una etiqueta com qualsevol altra (**mutable**: es pot reapuntar). Per a desplegar convé fixar versió (`:1.0`) o **digest**.

---

## P11 — Volums de Docker

### Concepte

Els **volums** són **espais d'emmagatzematge creats fora del contenidor**. Serveixen per **compartir dades** entre contenidors i **no s'esborren** quan s'esborra el contenidor.

### Pregunta (V/F)

"Los volúmenes de Docker son espacios de almacenamiento de datos. Al eliminar un contenedor que tiene montado un volumen, los datos del volumen también se eliminan."

- [ ] Verdadero
- [x] **Falso**

### Per què és fals

Els volums viuen **fora del contenidor** → en eliminar el contenidor, **les dades es conserven**. I existeixen precisament per poder **compartir dades entre contenidors**: si s'esborressin, no complirien la seva funció.

---

## P12 — Imatge parent i Dockerfile

### Concepte

- **Dockerfile**: fitxer de **text pla de configuració** (similar al *makefile*) per crear imatges.
- **Imatge parent**: la designada a la directriu **`FROM`**; totes les comandes posteriors es basen en ella.
- **`FROM scratch`**: no fa servir cap imatge parent → crea una **imatge base**.

### Pregunta

En un Dockerfile, ¿qué determina la instrucción FROM?

- [x] **La imagen parent sobre la que se construyen las capas siguientes**
- [ ] El usuario con el que se ejecutará el contenedor
- [ ] Los puertos que se publican
- [ ] El volumen que se monta

### Per què la A sí

`FROM` és la imatge **parent**: la base de la qual衍生 totes les comandes posteriors.

### Per què les altres no

- **Usuari**: és la instrucció `USER`.
- **Ports**: és `EXPOSE` (i el flag `-p` en publicar).
- **Volum**: és `VOLUME`.

---

## P13 — Per què un contenidor no pot executar Windows sobre Linux

### Concepte

Un **SO complet** = **kernel + espai d'usuari**.

| | Què porta | Kernels |
|---|---|---|
| **MV** | kernel **+** espai d'usuari | 1 **per MV** (el guest) |
| **Contenidor** | només l'**espai d'usuari** | **1 sol**, compartit amb el host |

Un contenidor **no duu kernel perquè no en pot dur**: per això és lleuger. El kernel que l'executa és el del host (Linux) → un espai d'usuari de Windows **necessita el kernel de Windows**.

### Pregunta

¿Por qué un contenedor con una imagen de Windows no puede ejecutarse sobre un host Linux?

- [x] **Porque el contenedor no incluye kernel; usa el del host, que es Linux**
- [ ] Porque Windows no tiene soporte de containers
- [ ] Porque el hypervisor lo impide
- [ ] Porque las imágenes de Windows ocupan más espacio

### Per què la A sí

El contenidor porta **només espai d'usuari** i comparteix el kernel del host.

### Per què les altres no

- **Windows no té suport de contenidors**: fals (Docker Desktop ho ofereix).
- **El hypervisor ho impedeix**: el contenidor **no hi passa** pel hypervisor; les seves crides van directes al kernel host.
- **Mida**: no és el motiu.

---

## P14 — Com és possible Docker a Windows

### Concepte

Docker es va desenvolupar amb serveis del **kernel Linux** (en particular **cgroups** i **namespaces**). Per oferir-lo a Windows/Mac cal un **kernel Linux real**:

- **Windows Hyper-V virtualization**
- **WSL 2** (*Windows Subsystem for Linux*): un **kernel Linux complet construït per Microsoft**, que permet executar contenidors Linux **nativament sense emulació**.

### Pregunta

¿Qué componente permite que los contenedores Linux se ejecuten nativamente en Windows?

- [x] **WSL 2, que incluye un kernel Linux completo construido por Microsoft**
- [ ] El hypervisor de tipo 0
- [ ] La emulación de la ISA con QEMU
- [ ] Un contenedor dentro de otro contenedor

### Per què la A sí

WSL 2 introdueix un **kernel Linux complet** → contenidors Linux **nativament, sense emulació**.

### Per què les altres no

- **Hypervisor type 0**: no dona cap kernel Linux.
- **QEMU emulació**: seria **emulació**, no execució nativa; i a x86↔ARM és precisament el cas d'emulació.
- **Contenidor dins de contenidor**: no resol el problema del kernel.

---

## P15 — Orquestració

### Concepte

**Orquestració** = automatitzar la gestió d'un **conjunt de contenidors** (a un o molts hosts): quins serveis han de córrer, amb quina imatge, quants exemplars, xarxes, volums… i **mantenir l'estat real igual a l'estat desitjat**.

Al nivell bàsic de classe: **Docker Compose** (fitxer `docker-compose.yml` per definir i executar **varis contenidors simultàniament**). Per a grans flotes: **Kubernetes** — *orquestrador* que aporta **gestió, desplegament i escalat** d'un gran nombre de contenidors.

### Pregunta

¿Qué aporta la orquestación de contenedores frente a ejecutar contenedores individualmente?

- [ ] Eliminar la necesidad de un kernel Linux en el host
- [x] **Gestionar automáticamente el conjunto: despliegue, escalado, reinicio de contenedores que fallan**
- [ ] Sustituir a los namespaces por cgroups
- [ ] Convertir los contenedores en máquinas virtuales

### Per què la B sí

L'orquestrador automatitza el **cicle de vida** del conjunt: escalat, reinici/recuperació, *rolling update*, planificació i descobriment de serveis.

### Per què les altres no

- **Eliminar el kernel**: fals; el contenidor ** sempre el necessita.
- **Substituir namespaces per cgroups**: són **complementaris**, no substitutable.
- **Convertir en MVs**: al revés.

---

## P16 — El tipus de MV segons la funcionalitat

### Concepte

- **MV de sistema**: executa un **SO complet** (inclou type 1 i 2) i li ofereix el seu hardware virtual.
- **MV de procés**: executa un **procés** en un entorn independent; la VMM **no virtualitza hardware real**, sinó un **sistema virtual abstracte**. Exemples: **JVM** (bytecodes) i **Valgrind** (tradueix a *IR* i recompila).

### Pregunta

¿Cuál es un ejemplo de máquina virtual de proceso?

- [ ] VMware ESXi
- [x] **La JVM, que ejecuta bytecodes en una máquina abstracta**
- [ ] Docker
- [ ] VirtualBox

### Per què la B sí

La JVM és una **MV de procés**: abstrau el hardware i ofereix un entorn d'execució virtualitzat per a les aplicacions Java (*write once, run anywhere*).

### Per què les altres no

- **ESXi**: hipervisor **type 1** → MVs de **sistema**.
- **Docker**: contenidor, no MV.
- **VirtualBox**: hipervisor **type 2** → MVs de sistema.

---

## P17 — Temps relatiu dins una MV

### Concepte

Dins una MV, quan **no se li assignen recursos de temps**, queda **"congelada"**. El temps que passa "dins" la MV **no és temps real**: és relatiu a la MV.

### Pregunta

¿Qué ocurre con una máquina virtual que no tiene asignados recursos de tiempo?

- [x] **Queda "congelada": su reloj interno deja de avanzar respecto al tiempo real**
- [ ] Se apaga automáticamente
- [ ] Pierde todos sus datos en disco
- [ ] Se convierte en un contenedor

### Per què la A sí

És la idea de classe: el temps de la MV és **relatiu** a la MV, no al temps real de la màquina.

### Per què les altres no

- **S'apaga**: no, queda congelada (suspesa).
- **Perd les dades**: no, el seu estat és persistent.
- **Es converteix en contenidor**: no.

---

## P18 — Oberta: MV o contenidor? (activitat de classe)

### Concepte

**Virtualitzar** és més barat: poques màquines físiques aguanten moltes MVs. Però hi ha **menys rendiment** que hardware dedicat, i un **risc**: si peta el servidor on són, **peten totes** les MVs que hi ha a sobre. D'altra banda, per a determinades aplicacions no cal una virtualització total i és més adequada la **virtualització a nivell de SO**.

### Pregunta

Una empresa necessita desplegar 50 servidores lógicos para una app web, con presupuesto limitado y necesidad de seguridad, flexibilidad y alta disponibilidad. ¿Qué elegirías? ¿Y si falla un físico con 10 MVs?

### Resposta esperada

- **Amb pressupost i necessitat d'alta disponibilitat → MVs** (o contenidors orquestrats si l'aplicació és aïllable): permeten aïllar, clonar, moure i reiniciar serveis de manera independent, i el cost per servidor baixa.
- **Si un física amb 10 MVs falla** → cal replanificació: les MVs s'han de **recuperar** d'una còpia (o del *snapshot*) en un altre host → d'aquí la necessitat de **alta disponibilitat** i de còpies de seguretat; el risc inherent és que la fallada d'un host es queda totes les MVs que hi havia.
- **Si l'aplicació és una sola i no cal un SO diferent** → **contenidor**: més lleuger, arrencada immediata, i es pot orquestrar (replicació i balanceig) per obtenir la disponibilitat demanada.

---

## Fitxa ràpida — Tema 2

| Concepte | Clau |
|---|---|
| **MV** | Software en lloc d'ordinador físic; guests sobre un host; cada MV amb el seu SO |
| **SO = MV?** | No: el SO té accés directe al hardware i és l'únic que el controla |
| **Time-sharing** | Compartir el hardware per temps → il·lusió de 100% a cada procés |
| **VMM / hypervisor** | Assigna i gestiona els recursos del host; pot executar diverses MVs |
| **Virtualització vs emulació** | Mateixa ISA → virtualització · ISA diferent → emulació (QEMU ARM sobre x86) |
| **Trap-and-emulate** | Guest fa op. privilegiada → *trap* → el VMM l'emula (VT-x) |
| **Type 0 / 1 / 2** | Firmware · bare metal (ESXi) · sobre el SO host (Workstation) |
| **MV de sistema vs procés** | SO complet vs procés (JVM → bytecodes; Valgrind → IR) |
| **Contenidor** | Virtualització a **nivell de SO**: portem **només l'espai d'usuari** |
| **Contenidor vs MV** | Kernel compartit vs 1 kernel per MV · MBs i segons vs GBs i minuts |
| **Crides al sistema** | Contenidor → **directes** al kernel host · MV → kernel guest → *trap* → VMM |
| **Namespaces** | **Aïllen**: què **veu** el procés (PID, muntatge, xarxa, usuaris, UTS, IPC) |
| **Cgroups** | **Limiten**: quant **pot consumir** (memòria, CPU, E/S, processos) |
| **Aïllament** | MV per **imposició** · contenidor per **filtratge** cooperatiu |
| **Risc compartit** | El kernel és únic → un *bug* del kernel host afecta **tots** els contenidors |
| **Docker** | Open source (2013); cgroups + namespaces; imatges, Dockerfile, Compose, volumes, ports, xarxes |
| **DockerHub / Registry** | Repositori d'**imatges** |
| **Imatge / contenidor** | Plantilla / instància en execució |
| **Repositori / tag** | Contenidor lògic d'imatges / punter a una versió (mutable) |
| **Volums** | Emmagatzematge **fora** del contenidor; **no s'esborren** amb ell |
| **Compose** | Executa **varis contenidors** alhora (`docker-compose.yml`) |
| **Kubernetes** | Orquestrador: gestió, desplegament i **escalat** |
| **Docker a Windows** | Cal un kernel Linux real: **Hyper-V** o **WSL 2** |

---

## Dubtes / a revisar

- **P18** és l'activitat de classe del PPT (escenari dels 50 servidors): la resposta "correcta" la fixa el professor; la línia defensable és *MV per a aïllament i disponibilitat, contenidor per a casos lleugers i orquestrables*.
- **P9**: si el profe pregunta pels *namespaces* en plural, la resposta és la llista de tipus (PID, mount, network, user, UTS, IPC) + "no simulen hardware, filtren camps".
- Confirmar amb el professor què espera de **Kubernetes** (el PPT no ho desenvolupa: hi ha anotat "a verificar" a [[T2b-Contenedors-Docker#13. Kubernetes|T2b §13]]).

---

## Enllaços relacionats

- [[T2-Maquines-Virtualitzacio-SO|T2 — Màquines Virtuals i virtualització del SO]]
- [[T2b-Contenedors-Docker|T2b — Contenedors i Docker]]
- [[T2c-Comparativa-SO-MV-Contenidor|T2c — SO, MV i contenidor]]
- [[T3-Sistemes-Fichers-P1#1. Test ràpid del bloc anterior (MV / contenidors)|T3-P1 §1 — Test ràpid del bloc]]
- [[Qüestions-T1-Seguretat|Qüestions T1 — Seguretat]]
- [[Respostes-Parcial1-SO2-26-27|Respostes Parcial 1 SO2 (2026-2027)]]
- [[_Index_SO|Índex Sistemes Operatius I]]
