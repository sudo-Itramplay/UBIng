---
id: Docker i Microservices
aliases: []
tags: []
---

### 1. Introducció i l'Evolució dels Sistemes Distribuïts

- **El Repte dels Sistemes Moderns:** En el disseny de programari distribuït, ens trobem en una cruïlla quan una aplicació deixa de ser un únic servei acoblat i passa a estar configurada per desenes o centenars de serveis que han de funcionar de manera autònoma.

- **Idea Clau de l'Evolució:** L'objectiu de l'arquitectura de programari actual és realitzar una transició controlada: passar d'una aplicació distribuïda única (centrada en un bloc rígid) cap a un ecosistema complet de serveis distribuïts totalment independents.

- **L'Arquitectura Multicapa Tradicional:** Com a recordatori acadèmic, les aplicacions web tradicionals s'han estructurat històricament sota una arquitectura clàssica de tres capes:
  - **Presentació (Frontend):** La interfície d'usuari i la interacció directa.
  - **Lògica de Negoci (Backend):** On resideixen les regles operatives de l'aplicació.
  - **Persistència (Base de Dades):** L'emmagatzematge de la informació.

- **El Problema d'Aquest Enfocament:** Malgrat estar lògicament dividida en capes, a la pràctica, **tot el sistema acostuma a desplegar-se conjuntament** com una única entitat. Això lliga el cicle de vida de cada capa a les altres, limitant l'agilitat i l'evolució independent del programari.

---

### 2. L'Arquitectura Monolítica: Avantatges i Limitacions

- **Definició d'Aplicació Monolítica:** És un patró arquitectònic on tot el sistema de backend (que inclou funcionalitats com autenticació, gestió d'usuaris, comandes, pagaments i notificacions) s'executa com **un únic procés**, sota **una única aplicació** i requereix **un únic desplegament** global cap a la base de dades.

![[screenshot-2026-05-23_09-37-58 1.png]]

> [!done] Avantatges del Monòlit:
> No hem de demonitzar el monòlit, ja que presenta clars avantatges de disseny:
>
> - Simplicitat arquitectònica inherent.
> - Depuració (_debugging_) senzilla i directa.
> - Un únic lliurament (_deploy_) a producció.
> - Facilitat òbvia per començar projectes des de zero.
> - Menor sobrecàrrega de comunicació distribuïda per xarxa.

Ideal per a:
Prototips inicials, sistemes de mida petita i equips de desenvolupament reduïts.

> [!Fail] Problemes Crítics del Monòlit:
> A mesura que el sistema creix, el monòlit esdevé inviable a causa de tres factors de disseny:
>
> - **Escalabilitat Limitada:** Si un sol mòdul pateix un consum excessiu de CPU (per exemple, el mòdul de _Pagaments_ es troba saturat), no es pot escalar només aquesta part; **s'ha d'escalar obligatòriament tot el sistema sencer**, malbaratant recursos del clúster.
> - **Acoblament Elevat (_High Coupling_):** Tots els mòduls interns comparteixen el mateix espai de memòria, procés, cicle de vida i dependències de llibreries. Això provoca una baixa independència entre components; qualsevol canvi petit (com modificar el mòdul de _Pagaments_) exigeix recompilar tot el codi font i fer un _redeploy_ complet de l'aplicació.
> - **Tolerància a Fallades Limitada:** En compartir el mateix procés d'execució, una excepció greu no controlada o un desbordament de memòria provocat per un bug en un component secundari (com un error en el mòdul de _Notificacions_) provocarà la caiguda (_crash_) completa de l'aplicació, deixant el sistema sencer fora de servei.

---

### 3. Fonaments i Principis dels Microserveis

- **La Solució dels Microserveis:** Consisteix a dividir el sistema en un conjunt de serveis autònoms i independents.

- **Definició Acadèmica:** Un microservei és un servei petit, desplegable de manera totalment independent, que té una responsabilitat perfectament acotada i definida dins del domini del sistema.

- **Característiques Fonamentals:**
  - S'executa com un **procés independent** a nivell de sistema operatiu.
  - Té una **responsabilitat concreta** (_Single Responsibility_).
  - Exposa de forma clara una **interfície de programació (API)** per interactuar.
  - Permet el **desplegament independent** sense sincronització d'equips.
  - És **escalable de manera individual** segons la seva demanda de recursos.
  - Està completament **desacoblat** de la resta de components de l'ecosistema.

> [!important] El Principi de Responsabilitat Única (_Single Responsibility_):
> Cada servei ha de fer una sola cosa ben definida dins del domini de l'e-commerce (ex: _user-service_, _order-service_, _payment-service_, _notification-service_). S'ha d'evitar taxativament mantenir un únic servei de backend central que contingui tota la lògica de negoci del programari.

![Com es cada microservei? Estructura](../../Images/microServiceIs.png)

- **Arquitectura Distribuïda Real:** En una implementació real, cada microservei disposa del seu propi procés, la seva API i, de vital importància, la seva **persistència pròpia (Base de dades per servei)**. **Mai es comparteix memòria directament** ni bases de dades comunes; tota comunicació es fa exclusivament per xarxa mitjançant les seves respectives APIs.

---

### 4. Patrons de Comunicació Inter-Servei

#### **Tipologies de Comunicació:**

Perquè l'ecosistema funcioni, els serveis han d'intercanviar informació mitjançant diferents paradigmes:

1.  **Comunicació Síncrona (Request / Response):** El client envia una petició i queda bloquejat esperant la resposta del servidor (Exemple típic: **REST sobre HTTP** o arquitectures CRUD simples).

2.  **Comunicació Asíncrona (Pas de missatges / Esdeveniments):** Els serveis intercanvien informació sense bloquejos temporals utilitzant un missatger intermediari (_Message Broker_) com **Kafka** o **RabbitMQ**.

3.  **Comunicació Mesh de Serveis (Mesh Architecture):** Comunicació directa de tipus _peer-to-peer_ (P2P) assistida per components de descobriment de serveis (Exemple: **gRPC**, o malles de serveis com **Istio** i **Linkerd**).

#### **Exemple de Flux Síncron REST:**

Si l'_Order Service_ requereix dades d'un producte, realitza una crida HTTP síncrona `GET /products/42` cap al _Product Service_, el qual processa la petició i retorna una càrrega útil en format JSON (`{ "id": 42, "name": "Laptop", "price": 899 }`).

![](../../Images/Comunicació%20síncrona%20entre%20serveis.png)

- **Avantatges de REST:**
  - És altament atractiu per la seva simplicitat,
  - és àmpliament conegut pel sector,
  - reutilitza la infraestructura nativa d'HTTP,
  - ofereix interoperabilitat total
  - És fàcil de depurar.

És ideal per a consultes immediates.

- **El Perill del Coupling Temporal:**

El gran desavantatge del model síncron és l'acoblament temporal:
Si per processar una comanda l'_Order Service_ ha de cridar el _Payment Service_, i aquest al seu torn ha de cridar l'_Inventory Service_, es genera una dependència lineal. **Si un sol servei de la cadena cau o triga massa, tota la cadena de peticions es bloqueja** provocant errors en cascada i fallades distribuïdes per _timeout_.

![](../../Images/Coupuling%20temporal.png)

![](../../Images/Exemple%20de%20fallada%20distribuida.png)

---

### 5. Mecanismes de Tolerància a Fallades

- **La Realitat dels Sistemes Distribuïts:** En entorns reals apareixen errors de xarxa, latències variables, fallades parcials i problemes de consistència de dades. Hem d'assumir que el sistema no és una única màquina fiable, sinó un conjunt de processos independents comunicats per un medi insegur (la xarxa).

- **Filosofia de Disseny:** La tolerància a fallades no busca evitar l'error de manera utòpica, sinó **dissenyar el sistema perquè continuï funcionant de forma degradada malgrat les fallades parcials**.

#### **Estratègies:**

- **Timeouts (Temps d'espera límits):** Cap comunicació distribuïda pot esperar indefinidament una resposta. S'estableix un límit estricte (Ex: `requests.get(url, timeout=3)`) per alliberar fils d'execució.

- **Retries (Reintents):** Si una operació falla per una caiguda transitòria de la xarxa, es pot reintentar la petició de manera automàtica. No obstant això, repetir operacions a cegues pot comportar greus efectes secundaris.

- **Idempotència:** Per poder fer reintents de manera segura, les operacions han de ser idempotents. Una operació és idempotent si el seu resultat final és exactament el mateix tant si s'executa una sola vegada com si es repeteix centenars de vegades. Els mètodes `GET`, `PUT` o `DELETE` solen ser idempotents, mentre que un `POST /payments` conceptualment no ho és, ja que podria cobrar dues vegades al client si es reintenta sense un identificador únic.

- **Circuit Breakers (Tallacircuits):** Si un microservei falla repetidament, el sistema "obre el circuit" per evitar saturar-lo amb més peticions inútils durant un temps prudencial (Ex: si el servei de pagaments falla reiteradament, es bloquegen les crides durant 1 minut i es retorna un error immediat controlat).

- **Fallbacks (Respostes de contingència):** Proporcionar una ruta o resposta alternativa quan el servei principal està inaccessible per oferir una degradació acceptable de la interfície (Ex: si falla el servei de notificacions, es mostra el text "Notificacions no disponibles" en comptes de fer fallar tota la pantalla de l'usuari).

---

### 6. El Patró API Gateway

En una arquitectura microservei el frontend no parla amb totss els serveis, s'utilitza un **Api Gateway**

> [!info] **Definició:**
> L'API Gateway actua com un **punt d'entrada únic i centralitzat** per a totes i cadascuna de les peticions que fan els clients (web, mòbil, etc.) cap al nostre sistema intern.

- **Responsabilitats de Gestió:** L'API Gateway s'encarrega d'encapsular tasques transversals de l'enginyeria de sistemes distribuïts, descarregant d'aquesta feina els microserveis de negoci:

- **Enrutament (_Routing_):** Derivar cada petició HTTP al microservei correcte (User, Order, Payment) segons la ruta sol·licitada.

- **Autenticació i Seguretat:** Validar la identitat de l'usuari a la porta d'entrada abans de permetre l'accés a la xarxa interna.

- **Limitació de Taxa (_Rate Limiting_):** Controlar el volum de peticions per evitar atacs de denegació de servei o abusos de l'API.

- **Registre d'Auditoria (_Logs_):** Mantenir una traça centralitzada dels accessos al sistema.

- **Agregació de Respostes:** Combinar dades de múltiples microserveis interns en una única resposta optimitzada per al Frontend.

---

### 7. Arquitectures Basades en Esdeveniments (EDA) i Patró Productor-Consumidor

- **Paradigma Asíncron:** Com a alternativa a les crides síncrones causants d'acoblament, podem utilitzar sistemes de missatgeria distribuïda per intercanviar informació de manera totalment asíncrona.

> [!done] **Avantatges d'EDA:**
>
> - Proporciona un desacoblament temporal absolut (els serveis no han de coincidir en el temps de resposta)
> - millora substancialment la tolerància a fallades global
> - permet el processament de tasques pesades en segon pla (_background_)
> - ofereix un escalat elàstic excel·lent.

- **Què és un Esdeveniment?** És la representació d'un fet altament rellevant que ha passat dins del sistema informàtic. És crucial entendre que un esdeveniment descriu una acció que **JA ha succeït** i, per tant, és immutable. Els verbs es redacten sempre en passat (Exemples: `UserRegistered`, `OrderCreated`, `PaymentCompleted`, `StockReserved`).

![](../../Images/Exemple%20de%20processament%20asíncron.png)

- **El Model Productor-Consumidor:** Els microserveis integrats en aquest model no es coneixen directament entre si, evitant acoblaments de codi.
  - Es basen en esdeveniments i missatges

- **Productor (_Producer_):** El servei que genera i publica l'esdeveniment en un canal o tema (_topic_) específic (Ex: l'_Order Service_ publica la notificació que s'ha creat una ordre al clúster de Kafka).

![](../../Images/Què%20és%20un%20esdeveniment.png)

- **Consumidor (_Consumer_):** El servei o serveis que estan subscrits a aquest _topic_ i reben l'esdeveniment per processar-lo de manera independent quan tinguin recursos disponibles (Ex: el _Notification Service_ llegeix el canal i envia un correu electrònic a l'usuari; el _Payment Service_ llegeix el mateix canal i efectua el cobrament de forma asíncrona).

- **Tecnologies de Referència:** Per implementar aquesta arquitectura, utilitzem plataformes de _streaming_ de dades o cues de missatges com **Apache Kafka**, **RabbitMQ** o serveis cloud administrats com **AWS SNS/SQS**.

> [!important] **Arquitectura Híbrida:**
> El disseny de sistemes real de la indústria rarament és pur. El més habitual és trobar una combinació híbrida: s'utilitza **comunicació síncrona (REST)** per a operacions de resposta immediata que l'usuari requereix veure instantàniament a la pantalla, i **comunicació asíncrona (Esdeveniments/Kafka)** per desencadenar tots els processos de _background_, analítiques o notificacions posteriors.

![](../../Images/Mesh%20de%20Serveis.png)

---

### 8. Desplegament de Microserveis: El paper de Docker i Kubernetes

- **La Problemàtica del Desplegament:** En disposar de dotzenes de serveis distribuïts, sorgeixen problemes logístics complexos de gestionar manualment: instal·lació en entorns diferents, conflictes de versions de llibreries, dependències creuades, col·lisions de ports, escalabilitat elàstica, monitorització heterogènia i la gestió eficient de logs i secrets de configuració.

- **La Solució Industrial:** S'utilitza la combinació estratègica de **Contenidors (Docker)** i **Orquestradors (Kubernetes)** per automatitzar completament el cicle de vida del programari en producció.

- **Docker (Contenidització a nivell d'OS):** Permet empaquetar de forma aïllada un microservei juntament amb el seu _runtime_, llibreries, fitxers de configuració i dependències exactes en una única unitat lleugera i executable anomenada **Contenidor**. Això garanteix que el programari es comportarà de manera **idèntica a qualsevol entorn** de computació.

#### Taula Comparativa Avançada: Màquines Virtuals (VM) vs Contenidors (Docker)

Aquesta comparativa és un clàssic de la disciplina i té una alta rellevància per a qualsevol avaluació acadèmica:

| Característica / Mètrica  | Màquina Virtual (VM)                                                                                                  | Contenidor (Docker)                                                                                             |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| **Nivell d'Abstracció**   | Abstrau el **Hardware** físic mitjançant un hipervisor. Inclou un OS convidat complet amb el seu propi BIOS i Kernel. | Abstrau a nivell d'**Operating System**. Comparteix el mateix Kernel de l'OS amfitrió (Host).                   |
| **Mida del Paquet**       | Molt pesada (ordre de **diversos Gigabytes**).                                                                        | Lleugera (ordre de **desenes de Megabytes**).                                                                   |
| **Temps de d'Arrencada**  | Lent (de **30 a 45 segons** o minuts, ja que requereix un procés de boot complet).                                    | Gairebé instantani (**< 50 mil·lisegons**, ja que és només un procés de l'OS).                                  |
| **Temps de Parada**       | Triga entre **5 i 10 segons**.                                                                                        | Ultra ràpid (**< 50 mil·lisegons**).                                                                            |
| **Consum de Recursos**    | Elevat (reserva de RAM i CPU fixa i exclusiva per a cada VM).                                                         | Molt menor (eficiència dinàmica, permet allotjar molts més contenidors en un mateix servidor).                  |
| **Aïllament i Seguretat** | **Molt alt**. L'aïllament per hardware fa que si una VM falla, és molt improbable que afecti les altres.              | **Menor**. En compartir recursos de Kernel comuns, requereix precaucions de seguretat tradicionals addicionals. |

- **Exemple de Disseny d'un Dockerfile:** El `Dockerfile` és el fitxer de text d'automatització on definim els passos secuencials per construir la imatge del nostre microservei
  - Ex: indicar la imatge base de Python, definir el directori de treball `/app`, copiar el llistat de `requirements.txt`, executar el gestor de paquets `pip install` i finalment declarar el comando d'arrencada executiu `CMD ["python", "main.py"]`).

![](../../Images/Exemple%20Dockerfile.png)

- **Kubernetes (Orquestració a Gran Escala):** Quan la topologia del sistema creix i hem de gestionar i coordinar centenars de contenidors Docker distribuïts en múltiples servidors, Docker per si sol es queda curt. Kubernetes (K8s) és una plataforma distribuïda dissenyada expressament per actuar com a orquestrador.

![](../../Images/KubernetesQuees.png)

- **Funcions de Kubernetes:** K8s no s'encarrega d'executar una sola aplicació aïllada; s'encarrega de governar **ecosistemes complets de programari** en producció assumint tasques automatitzades com:
  - **Scheduling:** Decidir en quin node físic del clúster s'ha d'executar cada contenidor segons els recursos lliures.
  - **Restart Automàtic (_Self-Healing_):** Detectar si un contenidor ha caigut o està corrupte, destruir-lo i reiniciar-lo de forma immediata sense intervenció humana.
  - **Escalat Elàstic:** Augmentar o reduir el nombre de rèplica d'un microservei de forma automàtica basant-se en la demanda real de CPU o xarxa.
  - **Networking i Balanceig de Càrrega (_Load Balancing_):** Gestionar l'enrutament de xarxa intern i distribuir el tràfic de forma homogènia entre totes les rèpliques actives d'un mateix microservei per evitar saturacions.
  - **Observabilitat:** Proveir mecanismes bàsics per auditar l'estat de salut de la infraestructura.

---

### 9. Assumpcions Erònies, Trade-offs i Presa de Decisions arquitectòniques

- **Les Fal·làcies de la Computació Distribuïda:** Molts enginyers novells prenen decisions de disseny errònies assumint la fal·làcia que _"un sistema de microserveis és exactament igual que un monòlit però amb els fitxers separats"_. Com a arquitectes, heu de recordar sempre a l'examen que la realitat física imposa restriccions severes.

> [!fail] **És un error greu assumir que:**
>
> - La xarxa és 100% fiable.
> - La latència de comunicació és zero.
> - L'ample de banda és infinit.
> - El cost econòmic i computacional de transmetre missatges és zero.
> - Existeix una seguretat implícita a la xarxa.

- **La Realitat és Complexa:** En destrossar el monòlit, entrem en un món de fallades parcials, latències de xarxa variables, pèrdues de consistència de dades entre bases de dades distribuïdes i errors de comunicació constants.

#### **Criteris de Decisió: Quan NO utilitzar microserveis:**

- Sistemes petits, aplicacions corporatives simples o desenvolupament de prototips ràpids (_MVP_).

- Equips d'enginyeria reduïts (la sobrecàrrega de gestió els enfonsaria).

- Baixa necessitat real d'escalabilitat elàstica.

- Baixa complexitat de domini de negoci.

#### **Criteris de Decisió: Quan SÍ fer el salt a microserveis:**

- Sistemes de programari grans, altament complexos i amb perspectives de creixement sostingut.

- Necessitat imperiosa d'escalar funcionalitats de manera individual per estalvi de costos o rendiment.

- Equips de desenvolupament grans, multidisciplinars i especialitzats que necessiten treballar en paral·lel sense trepitjar-se.

- Necessitat de tenir cicles de lliurament i desplegaments independents sense dependre de decisions globals de l'empresa.

- Dominis de negoci rics, amb fronteres de responsabilitats perfectament acotades (_Bounded Contexts_).

- Requisits estrictes de tolerància a fallades millorada en alta disponibilitat.

#### Problemes: **Els Costos Ocults de l'Arquitectura de Microserveis:**

Recordeu que cap decisió en enginyeria és gratuïta (_No silver bullet_). Implementar microserveis afegeix una enorme sobrecàrrega operativa i de gestió:

- La comunicació distribuïda afegeix una gran complexitat de codi i infraestructura.

- Dificultat extrema per fer depuració (_debugging_) de fluxos tradicionals.

- Complexitat en la gestió i consistència de les dades distribuïdes.

- Dificultat afegida per dissenyar tests unitaris i d'integració.

- Sobrecàrrega en les tasques de monitorització, manteniment i traçabilitat del flux de l'execució d'una petició a través dels serveis.

- **L'Ecosistema d'Eines d'Observabilitat:** Per mitigar aquests inconvenients i fer governable el sistema, es requereix un esforç d'enginyeria molt superior al d'un monòlit, recolzant-nos en eines de la indústria com:
  - **Prometheus:** Recollida de mètriques en temps real.
  - **Grafana:** Visualització de panells de control analítics.
  - **Jaeger i Zipkin:** Eines de traçabilitat distribuïda per seguir el camí exacte d'una petició a través de la teranyina de microserveis interns.
