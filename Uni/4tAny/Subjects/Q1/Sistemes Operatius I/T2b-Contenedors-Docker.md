---
id: T2b-Contenedors-Docker
aliases: []
tags:
  - tipus/teoria
  - assignatura/SO
assignatura: SO
data: "2026-10-17"
---

# T2b — Contenedors i Docker (virtualització a nivell de SO)

**Referència: PDF 02 — Máquinas virtuales y virtualización del SO (Parte 2)**

---

## 1. Repàs ràpid de la setmana passada

- Les **MVs** són una **abstracció de la capa de hardware**: hypervisors (VMM) permeten executar 1 o més MVs en una màquina física, i cada MV és una **còpia completa** del SO, aplicacions, binaris i llibreries
- La **virtualització de processos** permet executar un procés en un entorn independent; la MV és qui lidiar amb el SO
- La virtualització té per objecte **segregar aplicacions**, **administrar** el seu rendiment i ús de recursos, i tenir una **forma fàcil** d'iniciar-les, aturar-les, moure-les i administrar-les

> [!question]- Repàs: de veritat ens interessa virtualitzar sempre TOTS els recursos d'una màquina física?
> No. Per a determinades aplicacions no cal una virtualització total dels recursos i del SO; llavors és més adequada la **virtualització a nivell de SO** (*OS-level virtualization*), que veurem tot seguit.

---

## 2. Cas Héctor / María (P1)

- **Héctor** té **Python 2.7** instal·lat i programa amb algo **només disponible en aquesta versió**
- **María** té **Python 3.6** (un altre projecte), però Héctor vol que María executi el codi de la seva aplicació a la seva màquina

> [!question]- P1 · Quins possibles escenaris es poden donar en aquesta situació?
> - **María instal·la Python 2.7** també: funciona, però pot **conflictivar** amb el seu Python 3.6 (dues versions al mateix sistema)
> - **Héctor crea un contenidor** amb Python 2.7 i **totes les llibreries i recursos necessaris**, i li passa a María: ella l'executa **sense tocar** el seu entorn
> - (Alternativa del capítol anterior) Héctor crea una **MV** amb Python 2.7 + aplicació — possible però **massa pesat** per a un sol requisit de versió; per això, en casos com aquest, és més adequada la virtualització a nivell de SO

---

## 3. Què és la virtualització a nivell de SO?

- Definició (Wikipedia): un **paradigma de SO** en què el **kernel** permet l'existència de **múltiples instàncies d'espai d'usuari aïllades**, anomenades **contenedores** (LXC, Solaris containers, Docker, Podman), **zones** (Solaris), **virtual private servers** (OpenVZ), **partitions**, **virtual environments** (VEs), **virtual kernels** (DragonFly BSD) o **jails** (FreeBSD jail o chroot jail)
- Aquestes instàncies **poden semblar ordinadors reals** des del punt de vista dels programes que s'hi executen
- Els contenedores són una **abstracció de la capa d'aplicacions** (no de la capa de hardware com les MVs)
- Els processos dins d'un contenedor **només veuen els espais d'usuari aïllats** que se'ls assignen
- Múltiples contenedores poden executar-se en una màquina (o en vàries)
- Execució **ràpida** i amb els **recursos assignats**

### Chroot / jail (1979)

- Comanda d'Unix que permet **modificar l'entorn d'execució**: el procés (i els seus fills) només poden "veure" els fitxers que hi ha sota un **directori arrel especificat** (ex: `/jail`)
- L'antecedent històric dels contenidors

### Característica clau dels contenidors

- Els processos fan les **crides al sistema directament al SO** → **no cal un hypervisor** com a les MVs
- Poden executar apps en contenedores diferents (**seguretat**) facilitant-ne la instal·lació i el manteniment
- En sistemes d'allotjament, cada usuari té un contenedor amb recursos assignats; permet la **distribució fàcil del contenedor sencer** als clients

---

## 4. Contenedores vs MVs

> [!question]- P2 · (a) Enumera les avantatges que aporta programar amb contenedores
> - **Ràpids i lleugers**: pesen **MBs** (les MVs, GBs) i arrenquen en segons
> - **Portabilitat**: un contenedor conté totes les llibreries necessàries per executar l'aplicació → funciona igual a qualsevol màquina
> - **Eficiència**: no cal duplicar el SO ni un hypervisor; les crides al sistema van **directes al SO host**
> - **Aïllament**: cada contenedor té els seus espais d'usuari aïllats i recursos restringits
> - **Fàcil distribució**: es distribueix el contenedor sencer al client

> [!question]- P2 · (b) Quines diferències hi ha entre les MVs i els contenedores?
> | | **MVs** | **Contenedores** |
> |---|---|---|
> | Què virtualitza | El **hardware** de la màquina | El **SO** (nivell de SO) |
> | SO guest | Cada MV pot executar un **SO diferent** | Cada contenedor s'executa sobre un **únic SO host** |
> | Velocitat | Lents d'inicialitzar | **Ràpids** |
> | Tamany | Considerable (**GBs**) | **MBs** |
> | Portabilitat | Menys portàtils | Més **portables i eficients** |

---

## 5. Què pot controlar un contenedor?

> [!question]- P3 · Quin tipus de recursos pot controlar un contenedor?
> Els contenedores controlen l'**espai d'usuari** on s'executen els programes:
> - **Memòria RAM**
> - **Espai de directori/fitxer** al qual poden accedir
> - **Nombre màxim de CPUs** que poden utilitzar
> - **Nombre màxim de processos** que s'executen dins del contenedor

---

## 6. Tecnologies Linux rere els contenidors

> [!question]- P4 · En Linux, quines tecnologies es fan servir actualment per gestionar l'accés a aquests recursos?
> Els contenedores estan gestionats internament pel SO:
> - **Control groups (cgroups)**: permeten **limitar** els recursos (tecnologia que limita...)
> - **Namespaces**: permeten **aislar** els contenedores entre sí. Cada procés dins del seu contenedor té el seu **propi PID**

---

## 7. Docker a Windows: com és possible?

- **Docker Desktop** és la tecnologia que permet executar Docker a Windows i Mac
- Docker, però, es va desenvolupar gràcies als serveis del **kernel Linux**, en particular **cgroups** i **namespaces**

> [!question]- P5 · Com és possible oferir serveis Docker a Windows?
> - **Windows Hyper-V virtualitzation**
> - Habilitat per funcionar **nativament (sense emulació)** a Linux mitjançant **WSL 2** (*Windows Subsystem for Linux*)

### WSL 2

> [!quote] "*WSL 2 introduces a significant architectural change as it is a **full Linux kernel built by Microsoft**, allowing Linux **containers to run natively without emulation**.*"
> Amb Docker Desktop sobre WSL 2 es poden fer servir **entorns Linux** sense haver de mantenir scripts de build tant de Linux com de Windows. Millora també el compartit de sistema de fitxers, el temps d'arrencada, etc.

---

## 8. Què és Docker?

- Tecnologia **open source** de contenidors, apareguda el **2013**
- Internament utilitza **cgroups** i **namespaces**
- Docker hi afegeix múltiples característiques per manipular i executar contenidors:
  - **Portabilitat** dels contenidors entre màquines: un contenedor conté totes les llibreries necessàries per executar una aplicació
  - Permet crear contenidors de forma **senzilla**; inclou funcionalitats de gestió de versions similar a **Git**

### Imatge parent

> [!info] La **imatge parent** d'una imatge és la designada a la directriu `FROM` del Dockerfile. Totes les comandes posteriors es basen en aquesta imatge parent. Un Dockerfile amb `FROM scratch` no usa cap imatge parent i crea una **imatge base**.

> [!question]- P6 · (a) Enumera 3 gestors de contenidors · (b) Revisa la web oficial d'un d'ells
> (a) Dels enllaços del PPT en surten 4 (en calen 3): **Docker** (docker.com), **CRI-O** (cri-o.io), **rkt** (coreos.com/rkt), **LXC/LXD** (linuxcontainers.org)
> (b) Tasca pendent: entrar a la web oficial d'un d'ells i revisar-ne la documentació

---

## 9. Definicions de Docker

> [!question]- P7 · Descriu: Docker Registry / DockerHub, Docker Images, Dockerfile, Docker compose, Volumes, Links
> - **Docker Registry / DockerHub**: **repositori** on es pengen els fitxers que permeten generar el contenedor (les *Docker images*). Ex: una imatge que inclou un compilador Java
> - **Imatges**: **captura de l'estat d'un contenedor**; serveixen de **plantilles** per crear contenidors. N'hi ha moltes públiques (Ubuntu, CentOS) que descarreguem i adaptem a la nostra aplicació. D'una imatge en poden sortir **varis contenidores**
> - **Contenedores**: **instàncies en execució** d'una imatge
> - **Dockerfile**: fitxer de **text pla de configuració** (similar al *makefile*) que es fa servir per crear imatges (o a partir d'una descarregada de DockerHub)
> - **Docker compose**: eina per **definir i executar varis contenidors simultàniament**. Usa el Dockerfile per configurar la imatge i baixar dependències, i `docker-compose.yml` per a la configuració dels serveis (diferents contenidors)
> - **Volumes**: **espais d'emmagatzematge creats fora del contenedor**. Útils per **compartir dades** entre contenidors
> - **Links**: **enllacen els contenidors** d'una màquina entre sí

---

## 10. Pregunta d'examen: volums

> [!question]- V/F · "Els volums de Docker són espais d'emmagatzematge de dades. En eliminar un contenedor que conté un volum muntat, les dades del volum també s'eliminen." Justifica
> **Fals.** Els volums viuen **fora del contenedor** (són espais d'emmagatzematge creats fora d'ell), per tant en eliminar el contenedor **les dades del volum es conserven**. A més, justament existeixen per poder **compartir dades entre contenidors**: si en borrar un contenedor s'esborressin, no podrien complir la seva funció.

---

## 11. Comandes bàsiques de Docker

> [!question]- P8 · Llista les comandes bàsiques de Docker per tractar contenidors i imatges
> **Contenedores:**
> | Comanda | Què fa |
> |---|---|
> | `ps` | Llista de contenidors executant-se |
> | `ps -a` / `ps --all` | Tots els contenidors, inclosos els parats |
> | `top` | Processos d'un contenedor |
> | `start` | Aixeca un contenedor parat |
> | `stop` | Atura un contenedor en execució |
> | `pause` | Pausa els processos dins del contenedor |
> | `commit` | Crea una **imatge** des del contenedor |
> | `rm` | Elimina un contenedor parat |
> | `exec` | Aplica una comanda dins un contenedor ja executant-se (ex: `docker exec -it myUbuntu /bin/bash`) |
>
> **Imatges:**
> | Comanda | Què fa |
> |---|---|
> | `images` | Llista d'imatges locals |
> | `run` | Crea un contenedor a partir d'una imatge i executa una comanda |
> | `tag` | Etiqueta una imatge |
> | `pull` | Descarrega una imatge del repositori |
> | `rmi` | Elimina una imatge local |

---

## 12. Xarxes, ports i linkeig de contenidors

### Ports

- Per defecte, en crear un contenedor els **ports no s'exposen a l'exterior**
- Per fer-los disponibles per a serveis o contenidors **fora de la xarxa del contenedor**, cal **publicar-los** amb el flag **`-p`**: crea un **firewall** que mapeja el **port del contenedor** al **port del host** → permet la connexió amb l'exterior

### Xarxes

- **Bridge**: per a contenidors executant-se **dins del mateix Docker host**. Per defecte hi ha una xarxa local *default*, però convé crear la nostra pròpia per tenir més capacitat de configuració
- **Overlay**: per connectar amb un **Docker host exterior** (o configurar l'enrutament mitjançant el SO)
- Connectar un contenedor en execució a una xarxa: `docker network connect my-net my-Linux`

---

## 13. Kubernetes

> [!question]- P9 · Què és Kubernetes? Què aporta Kubernetes a Docker?
> El PPT només diu que Docker **se sovint s'utilitza amb Kubernetes** — no en desenvolupa la resposta. Resum breu (a verificar): Kubernetes és un **orquestrador de contenidors**; aporta la gestió, desplegament i escalat d'un gran nombre de contenidors. Veure `## Dubtes / a revisar`

---

## 14. Docker al món empresarial

- Com amb les MVs, **externalitzar** aquests serveis dona **flexibilitat i escalabilitat**
- Empreses que ofereixen serveis per executar contenidors: **Google Container Engine**, **Amazon EC2 Container Service**, **Azure Container Service**, **Acquia**, **Digital Ocean**
- Cas d'ús real: arquitectura end-to-end per a la recollida i explotació de dades des d'una API pública — visualització de dades COVID-19 (TFG UB, Luís Roset, 2021)

---

## 15. En resum (del professor)

- La virtualització permet virtualitzar/emular un ordenador; en aquest bloc n'hem vist **dues formes**:
  - **Màquines virtuals (MV)**
  - **Contenedores**
- Es pot executar un **SO diferent** a cada MV; les MVs permeten limitar els recursos assignats al SO
- Els **contenedores** són executats pel **SO host**; a cada contenedor se li poden limitar els recursos assignats, i les **crides al sistema es fan directament al SO**

---

## Preguntes del PPT (índex ràpid)

| # | Pregunta | On |
|---|---|---|
| Repàs | Ens interessa virtualitzar sempre tots els recursos? | [[#1. Repàs ràpid de la setmana passada]] |
| P1 | Escenaris Héctor (Python 2.7) / María (Python 3.6) | [[#2. Cas Héctor / María (P1)]] |
| P2 | (a) Avantatges dels contenidors · (b) Diferències MV vs contenidors | [[#4. Contenedores vs MVs]] |
| P3 | Quins recursos pot controlar un contenidor? | [[#5. Què pot controlar un contenedor?]] |
| P4 | Tecnologies Linux per gestionar l'accés | [[#6. Tecnologies Linux rere els contenidors]] |
| P5 | Com és possible Docker a Windows? | [[#7. Docker a Windows: com és possible?]] |
| P6 | Enumera 3 gestors de contenidors | [[#8. Què és Docker?]] |
| P7 | Registry, Images, Dockerfile, compose, Volumes, Links | [[#9. Definicions de Docker]] |
| V/F | Volums s'esborren amb el contenedor? | [[#10. Pregunta d'examen: volums]] |
| P8 | Comandes bàsiques Docker | [[#11. Comandes bàsiques de Docker]] |
| P9 | Què és Kubernetes? | [[#13. Kubernetes]] |

---

## Resum ràpid (FITXA)

| Concepte | Clau |
|---|---|
| **Virtualització nivell de SO** | Kernel amb múltiples instàncies d'usuari **aïllades** = contenidors; semblen ordinadors reals |
| **Chroot/jail (1979)** | El procés (i fills) només "veu" els fitxers sota un directori arrel |
| **Contenedor vs MV** | Contenedor = virtualitza el **SO**, MBs, ràpid, únic SO host · MV = virtualitza **hardware**, GBs, lent, SO diferent |
| **Crides al sistema** | Contenedores: **directes al SO** (sense hypervisor) |
| **cgroups** | **Limitar** recursos del contenidor |
| **Namespaces** | **Aïllar** contenidors entre sí (PID propi per contenidor) |
| **Docker (2013)** | Open source; usa cgroups + namespaces; portabilitat + gestió de versions estilo Git |
| **DockerHub / Registry** | Repositori d'**imatges** |
| **Imatge** | Captura de l'estat; plantilla per crear contenidors; `FROM` = imatge parent, `FROM scratch` = imatge base |
| **Contenedor** | Instància **en execució** d'una imatge |
| **Dockerfile** | Text pla de configuració (estil makefile) per crear imatges |
| **Compose** | Executa varis contenidors alhora (`docker-compose.yml`) |
| **Volumes** | Emmagatzematge **fora** del contenidor; **no s'esborren** amb el contenidor; per compartir dades |
| **Links** | Enllacen contenidors d'una màquina |
| **Ports `-p`** | Mapeja port del contenidor → port del host (firewall) |
| **Xarxa bridge / overlay** | Mateix host / host exterior |
| **Docker a Windows** | Hyper-V + **WSL 2** (kernel Linux complet de Microsoft, natiu sense emulació) |

---

## Dubtes / a revisar

- **P6 (b)**: revisar la web oficial d'un gestor de contenidors (Docker, CRI-O, rkt, LXC) — tasca del PPT, pendent
- **P9 Kubernetes**: el PPT no desenvolupa la resposta; confirmar amb el professor què en vol (orquestrador: gestió/desplegament/escalat de contenidors)
- **Pregunta V/F de volums**: la resposta es dedueix de la definició del PPT ("volums fora del contenidor"); confirmar si l'esperada és exactament aquesta justificació
- Gestors de contenidors del P6: dels enllaços del PPT surten **Docker**, **CRI-O**, **rkt**, **LXC** (linuxcontainers.org) — confirmar quins 3 vol

---

## Enllaços relacionats

- [[T2-Maquines-Virtualitzacio-SO|T2 — MV i virtualització (Parte 1)]]
- [[T1-Introduccio-Seguretat-SO|T1 — Introducció Seguretat SO]]
