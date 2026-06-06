---
data: 2026-05-27
assignatura: SD
parcial: Final (2n Parcial)
tags:
  - tipus/parcial
  - assignatura/SD
---

# Resum Final — Software Distribuit (2n Parcial)

> Notes atòmiques al [[_MOC|MOC de SD]] · [[Big Data i Teorema CAP]] · [[Hadoop]] · [[Spark]] · [[P2P]] · [[Java RMI]] · [[Web Services]] · [[Microserveis]] · [[Docker i Kubernetes]]

> Contingut complet posterior al Parcial 1: [[P2P]], [[Microserveis]] · [[Docker i Kubernetes]], [[Hadoop]], [[Spark]], [[Web Services]].

---

# 1. P2P

### 1. Fonaments de l'Arquitectura Peer-to-Peer (P2P)

L'arquitectura P2P representa un canvi de paradigma en els sistemes distribuïts on s'elimina, totalment o parcialment, la jerarquia clàssica de servidor centralitzat.

- **Definició conceptual**: És un paradigma on cada node (peer) contribueix amb dades i recursos (processament, emmagatzematge, amplada de banda) per assolir un servei uniforme.
    
- **Simetria funcional**: Tots els nodes del sistema tenen, en teoria, les mateixes funcions i responsabilitats.
    
- **Comunicació directa**: Un peer s'ha de poder comunicar amb qualsevol altre sense la intermediació obligatòria d'un servidor, tot i que a la pràctica moltes aplicacions utilitzen elements híbrids (com el DNS).
    
- **Localització de peers**: Perquè el sistema funcioni, els nodes s'han de trobar. Això es fa mitjançant:
    
    - **Directoris centralitzats**: Un índex mestre (estil Napster).
        
    - **Taules de Hash Distribuïdes (DHT)**: On cada node manté part de la informació de rutes.
        
- **Classificació segons topologia**:
    
    - **Centralitzat**: Índex mestre únic.
        
    - **Distribuït pur**: Nodes aleatoris sense jerarquia.
        
    - **Híbrid**: Existència de "supernodes" que gestionen índexs de nodes aleatoris.
        
    - **Estructurat**: Basat estrictament en DHT.
        

### 2. Taules de Hash Distribuïdes (DHT) i Xarxes Superposades

Les DHT són la solució d'enginyeria per garantir que un sistema P2P sigui escalable i tolerant a fallades sense dependre de ningú.

- **Característiques clau**:
    
    - **Autonomia**: Sense coordinació central.
        
    - **Escalabilitat**: El cost de coordinació per node és típicament de $log(n)$, permetent milions de nodes. (Nomes afecta a un nombre reduït de nodes)
        
    - **Tolerància a fallades**: El sistema es reconfigura automàticament quan els nodes entren o surten (churn).
        
- **Estructura i Funcionament**:
    
    - **Espai de claus**: S'atorga a cada node un rang contigu de claus.
        
    - **Hash Consistent**: Propietat que minimitza la redistribució de claus quan canvia el nombre de nodes (només afecten els veïns directes).
        
    - **Funció de distància**: Mètrica lògica (no geogràfica) per determinar la proximitat entre claus (ex: distància en una circumferència).

>[!warning] Repassa 
>![[Pasted image 20260502092930.png]]


- **Overlay Network (Xarxa Superposada)**:
    
    - És la xarxa lògica formada pels enllaços que cada node manté cap als seus veïns.
        
    - **Topologia**: Defineix l'estructura del veïnatge.
        
    - **Algorismes d'enrutament**: Com el _Nearest Neighbour_, per trobar el propietari d'una clau.
        
    - **Broadcast/Multicast**: Algorismes per difondre consultes o estadístiques a través de l'overlay.
        

### 3. Cas d'Estudi: BitTorrent

BitTorrent és l'exemple canònic de sistema P2P optimitzat per a la distribució massiva de fitxers grans, centrat en l'eficiència de descàrrega més que en la cerca.

- **Estratègia Quid Pro Quo**: "Comparteixo si tu comparteixes". Per evitar els "free riders" (nodes egoistes), el sistema premia els que més pugen dades, tot i que permet descàrregues esporàdiques a nodes nous per iniciar el procés.
    
- **Protocol de funcionament**:
    
    1. Localització del fitxer `.torrent` (metadata: hash, nom, URL del tracker).
        
    2. Petició al **Tracker** (servidor que coordina el torrent).
        
    3. El tracker retorna una llista de peers: **Seeds** (tenen tot el fitxer) i **Leechers** (els falten peces).
        
- **Gestió de peces (Segments de 256KB)**:
    
    - **Descàrrega en paral·lel**: Es demanen múltiples peces a diferents peers simultàniament.
        
    - **Rarest First**: Es prioritza descarregar les peces menys freqüents a la xarxa per assegurar la disponibilitat global del fitxer.
        
    - **Selecció d'enviament (Choking)**: Periòdicament se seleccionen els 4 peers amb millor taxa de descàrrega.
        
    - **Optimistic Upload**: Cada 30 segons s'envia dades a un peer aleatori per descobrir nous nodes més ràpids.
        

### 4. Seguretat i Blockchain

**Referència: Diapositives 8, 15-17**

En sistemes descentralitzats, la confiança és el repte tecnològic principal.

- **Seguretat P2P clàssica**: Ús de claus públiques per autenticar la identitat del peer i criptografia per assegurar la confidencialitat de les transaccions.
	- Al conecctar-se el servidor li dona al peer una clau pública
	- A cada iteració el peer l'ha de mostrar
    
- **Blockchain (Llibre de comptabilitat distribuït)**:
    
    - Cada transacció està signada digitalment. S'encripta i signa per provar l'autenticitat
        
    - **Blocs encadenats**: Cada bloc conté el hash del bloc anterior, fent-lo gairebé immodificable.
	    - Com que conté el has anterior, ens és dificil alterar-lo però també ens ajuda per tal de poder desxifrar la seva traçabilitat
        
    - **Proof of Work (PoW)**: Mecanisme que requereix un esforç computacional (temps/mineria) per crear blocs, evitant la generació massiva malintencionada.
        
    - **Consens**: Una transacció s'accepta si el 51% dels participants la validen.

![[Pasted image 20260502093635.png]]
![[Pasted image 20260502093719.png]]

### 5. Paradigma d'Objectes Distribuïts i Java RMI

Aquest model busca abstraure la xarxa perquè el programador senti que treballa amb objectes locals, tot i que s'executen en màquines remotes.

- **Conceptes fonamentals**:
    
    - **Objecte Remot**: Mètodes invocables des d'altres processos/màquines.
        
    - **Objecte Local**: Només accessible pel procés que el conté.
        
    - **Abstracció**: S'orienta a funcionalitats (mètodes) en lloc d'intercanvi manual de missatges (sockets).
    
>[!tip] Procès real vs lògic
>![[Pasted image 20260502093932.png]]
>![[Pasted image 20260502093907.png]]

- **Diferències Crítiques en la Invocació**:
    
    - **Arguments no-remots**: Es passen **per còpia** (necessiten ser `Serializable`).
        
    - **Objectes remots**: Es passen sempre **per referència** (via la seva interfície remota).
        
    - **Excepcions**: Tota crida remota ha de gestionar `RemoteException` a causa de possibles fallades de xarxa o protocol.
        

### 6. Arquitectura i Implementació de Java RMI

L'objectiu principal de RMI és que els programadors desenvolupin
aplicacions distribuı̈des amb Java usant la mateixa sintaxi i
semàntica que les aplicacions Java tradicionals.

Per implementar una aplicació RMI funcional, cal seguir una estructura de classes molt precisa.

- **Components de l'Arquitectura**:
	- **Objecte Remot**: Aquells objectes que algun dels seus mètodes espoden invocar des d'un altre procés corrent en una màquina remota.
	
	- **Objecte Local**: Aquells objectes que només poden ser invocats per un procés local en el qual l'objecte existeixi.
	
	- **Invocació de mètode remot**: Acció d'invocar un mètode d'una interfı́cie remota en un objecte remot.
    
    - **Interfície Remota**: Defineix els mètodes disponibles. Ha d'heretar de `java.rmi.Remote`.
        
    - **Servidor d'Objectes**: Màquina virtual que instancia els objectes i els exporta.
        
    - **RMIregistry**: El servei de noms (port 1099 per defecte) on els servidors registren els seus objectes (`bind`/`rebind`) i els clients els busquen (`lookup`).

>[!info] Inici
>Quan una MV S'inicia no té cap referència remota:
>- Per trobar-la utilitzarà un servei de directori per localitzar un objecte remot a partir del seu nom
>
>Un cop localitzat el primer objecte, aquest ens enviarà algunes referències remotes com a valors de retorn de la crida d'algun dels seus mètodes remots (callback)



### El Servei de Directori: RMIRegistry i Localització

El procés de "bootstrap" en RMI és un dels conceptes més crítics per entendre com s'estableix la comunicació inicial en un entorn on, d'entrada, no tenim referències remotes.

>[!info] RMI
>Ens permet fer servir diferents serveis de directori per registrar un objecte distribuit

- **El problema de la llengüeta**: Tal com indica la metàfora de la diapositiva, una màquina virtual (JVM) no neix amb referències a objectes externs. Necessita un mecanisme per "estirar" la primera referència.
    
- **RMIRegistry**: És un servidor de noms simple i fonamental que s'executa per defecte al port TCP 1099. Actua com una "guia de telèfons" on els noms (Strings) s'associen a referències d'objectes remots.
	- ![[Pasted image 20260502095018.png]]
    
    
- **Operacions de `java.rmi.Naming`**:
    
    - `bind(name, obj)` i `rebind(name, obj)`: Utilitzades pel servidor per publicar l'objecte. `rebind` és preferible perquè sobreescriu si el nom ja existeix.
        
    - `lookup(url)`: Utilitzada pel client per obtenir la referència (Stub) mitjançant una URL de tipus `rmi://host:port/name`.
        
    - `unbind(name)` i `list()`: Per a manteniment i consulta de les associacions actuals.

>[!tip] Més mètodes
>![[Pasted image 20260502095055.png]]
        
- **Seguretat inicial**: Un cop localitzat el primer objecte, aquest pot retornar noves referències (callbacks), evitant haver de passar sempre pel registre.
    

![[Pasted image 20260502095159.png]]

### Implementació del Servidor d'Objectes

Dissenyar el costat del servidor implica separar clarament la definició del servei de la seva execució real.

- **La Interfície Remota**: És el contracte. Ha d'estendre `java.rmi.Remote` i cada mètode ha de declarar que llança `java.rmi.RemoteException`.  Aquesta excepció és obligatòria perquè les fallades de xarxa són imprevisibles i alienes a la lògica de l'aplicació.

>[!warning] Apunt
>Aquesta interficie no et demana implementar cap mètodem excepte de l'exepció

- **La Implementació (`Impl`)**: És la classe que realment conté el codi. Habitualment hereta d'`UnicastRemoteObject`, la qual cosa li confereix la capacitat de "ser exportat" (començar a escoltar peticions en un port TCP) de forma automàtica en ser instanciat.

>[!warning] Compte!
>La classe del servidor d'objecte remot és una classe que té el codi
que crea i exporta un objecte remot.

   
- **Exportació manual**: Si no podem heretar (perquè ja heretem d'una altra classe), hem d'utilitzar el mètode estàtic `UnicastRemoteObject.exportObject(obj, port)`.

>[!tip] Recorda
>l'exportació d'objecte distribuı̈t fa que el procés del servidor comenci a escoltar i esperi que els clients es connectin i sol·licitin el servei de l'objecte.
   
- **Concurrència al Servidor**: Heu de tenir present que un servidor RMI és **concurrent per naturalesa**. Cada petició d'un client s'executa en un fil (thread) separat. Com a enginyers, és la vostra responsabilitat aplicar mecanismes de sincronització (`synchronized`, panys) si els mètodes accedeixen a recursos compartits per evitar condicions de carrera.
    
- **Publicitat de l'objecte**: El `main` del servidor ha de crear la instància de la implementació i lligar-la al registre amb un nom únic per fer-la accessible al món exterior.
    

### L'Aplicació Client i la Mecànica de Crida

El client ha de ser capaç de "traduir" una referència abstracta en una crida de mètode real.

- **Localització i Casting**: El client obté un objecte genèric del registre. És un **error comú** intentar convertir-lo a la classe d'implementació; el client **només ha de conèixer la interfície**. El casting s'ha de fer sempre cap a la interfície remota (ex: `(DateServer) Naming.lookup(...)`).

>[!fail] Error comú
>És un error comú convertir la referència obtinguda des el registre a la classe d'implementació de la interfı́cie en comptes de la classe d'interfı́cie.
>![[Pasted image 20260502100345.png]]
>![[Pasted image 20260502100404.png]]

- **Sintaxi Transparent**: Un dels grans avantatges de RMI és que, un cop tenim la referència, la invocació del mètode remot és sintàcticament idèntica a la d'un mètode local. Tota la complexitat de la xarxa queda amagada sota la capa del "Stub".
    
- **Dependències de classes**: Tant el client com el servidor han de compartir exactament el mateix paquet (package) i definició de la interfície remota. Si els packages no coincideixen, el sistema de serialització fallarà.
    
- **Passos per a l'execució**:
    
    1. Iniciar el registre (rmiregistry).
        
    2. Executar el servidor (que registrarà l'objecte).
        
    3. Executar el client (que buscarà i usarà l'objecte).
        

### Semàntica d'Invocació i Pas de Paràmetres

Aquest és, probablement, el punt més important per a un examen, ja que defineix com viatja la informació per la xarxa.

- **Pas per Còpia (Objectes no-remots)**: Quan passem un objecte normal (com un `String` o un `Date`), RMI n'envia una còpia completa. Per fer-ho, la classe ha d'implementar la interfície `java.io.Serializable`. Qualsevol canvi que el servidor faci en aquest objecte **no es reflectirà** al client.
    
- **Pas per Referència (Objectes remots)**: Si passem un objecte que és, en si mateix, un objecte remot (implementa `Remote`), RMI no en copia les dades, sinó que envia una referència (Stub). Això permet al receptor tornar a invocar mètodes sobre l'objecte original.
    
- **Especialització de mètodes**: Mètodes com `equals()`, `hashCode()` o `toString()` es comporten de manera especial en objectes remots per referir-se a la identitat de l'objecte remot i no a la còpia local del Stub.
    
- **Casos d'estudi (SimpleBankSystem)**: L'exemple final mostra com interfícies com `BankManager`, `Account` i `Client` interactuen. Noteu que una crida a `getAccount` retorna una interfície `Account` (referència remota), permetent una navegació distribuïda complexa entre diferents objectes del servidor.

- **Passos de Desenvolupament**:
    
    1. Definir la interfície remota.
        
    2. Implementar la interfície (normalment estenent `UnicastRemoteObject`).
        
    3. Crear el servidor: Instanciar l'objecte i registrar-lo al `rmiregistry`.
        
    4. Crear el client: Cercar l'objecte pel seu nom, fer el _casting_ a la interfície i invocar els mètodes.
        
- **Proxies (Stub/Skeleton)**: L'RMI genera automàticament el codi de preparació de dades (marshalling) i gestió de connexions, actuant com a intermediaris transparents per a l'usuari.

---

# 2. Docker i Microserveis

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

En una arquitectura microservei el frontend no parla amb tots els serveis, s'utilitza un **Api Gateway**

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

---

# 3. Hadoop

## 1. Problemàtica dels Sistemes Distribuïts Tradicionals

### Intenció

La programació i gestió de sistemes distribuïts sota els paradigmes tradicionals presenta una complexitat inherent molt elevada a causa de factors físics i temporals de la xarxa. Quan escalem els sistemes per processar grans volums d'informació, els models clàssics fallen en la gestió dels recursos.

### Definicions i Conceptes de Referència

- **Sincronització de Dades**: L'intercanvi de dades entre nodes independents requereix protocols estrictes de sincronització que afegeixen sobrecàrrega (_overhead_) al sistema.
    
- **Restriccions d'Amplada de Banda**: La transferència de dades a través de la xarxa està limitada per la capacitat física dels canals de comunicació.
    
- **Dependències Temporals**: La coordinació de l'ordre d'execució de tasques paral·leles i concurrents esdevé altament complexa de gestionar.
    
- **Fallades Parcials**: En un entorn distribuït, la probabilitat que un o diversos nodes caiguin és alta; gestionar aquestes fallades sense aturar el sistema complet és un dels grans reptes de l'enginyeria.
    
![[Pasted image 20260518182956.png]]

### L'Emmagatzemament Clàssic i el Coll d'Ampolla

Tradicionalment, les dades en un sistema distribuït es guarden de forma centralitzada en una unitat de dades en xarxa (com un NAS o un servidor de fitxers compartit). En el moment en què es requereix realitzar una computació, les dades es copien des d'aquesta unitat central cap als diferents nodes de computació.

```
[ Unitat de dades en xarxa ] --( Còpia de dades per xarxa )--> [ Nodes de Computació ]
```

Aquest enfocament és funcional i eficient únicament quan treballem amb una quantitat relativament limitada de dades.

### El Problema del Big Data

Els sistemes moderns han de processar volums massius d'informació diàriament. Sota aquest escenari, l'acció de transferir i proporcionar les dades als processadors a través de la xarxa ha esdevingut l'autèntic **coll d'ampolla** dels sistemes distribuïts actuals. 
Per tant, es fa totalment necessària una nova aproximació arquitectònica a la distribució del sistema.

---

## 2. Requeriments i Fonaments del Nou Paradigma

### Intenció

Per solucionar el coll d'ampolla del Big Data, qualsevol nova arquitectura de programari distribuït d'alta capacitat ha de complir de manera nativa amb una sèrie de requeriments de robustesa, consistència i escalabilitat.

### Requeriments del Sistema

- **1.-Robustesa a Fallades Parcials**: 
	- El sistema ha de ser resilient. No es pot permetre en cap cas que tot el sistema caigui completament a causa de la fallada d'uns quants components o nodes.
    
- **2.-Recuperació i Tolerància a la Pèrdua de Dades**:
    
    - Si un component del sistema falla, la seva càrrega de treball s'ha d'assumir de manera automàtica i transparent per una altra unitat del sistema.
        
    - Sota cap concepte es pot permetre la pèrdua de dades com a conseqüència d'una fallada de maquinari o programari.
        
- **3.-Recuperació Calenta d'un Component**: 
	- Si un node que ha fallat es recupera, ha de ser capaç d'ajuntar-se de nou al clúster de forma dinàmica, sense que sigui necessari reiniciar el sistema sencer.
    
- **4.-Consistència d'Execució**: 
	- La fallada de qualsevol component durant l'execució d'un treball (_job_) no ha d'afectar mai el resultat o la sortida final d'aquest treball.
    
- **5.-Escalabilitat**:
    
    - **Escalabilitat en Càrrega**: Afegir més càrrega de treball al sistema no ha de provocar una fallada general, sinó un descens controlat i proporcional en el rendiment global dels treballs individuals.
        
    - **Escalabilitat en Recursos**: L'increment de recursos físics (afegir més nodes al clúster) ha de repercutir directament en un augment equivalent de la capacitat de càrrega del sistema.
        

### Teorema de CAP

En l'àmbit dels sistemes distribuïts, el Teorema de CAP és una veritat de disseny fonamental que postula que un sistema distribuït només pot garantir simultàniament dues de les següents tres propietats:

1. **Consistència (Consistency)**: Tota operació de lectura ha de rebre l'escriptura més recent o, en el seu defecte, un error.
    
2. **Disponibilitat (Availability)**: Cada petició rebuda per un node actiu (no caigut) en el sistema ha de retornar una resposta obligatòriament (sense garantia de si conté l'escriptura més recent).
    
3. **Tolerància a Particions (Partition Tolerance)**: El sistema continua funcionant i operant encara que hi hagi pèrdues de paquets o retards en les comunicacions entre els nodes.
    
![[Pasted image 20260518183310.png]]

>[!important] Fallada de xarxa
>En cas que hi hagi una fallada en la xarxa, s'ha d'escollir entre consistència o disponibilitat (o rebre una dada no actualitzada o esperar per assegurar-se que hi ha consistència)

### Error Comú de Disseny

Un error típic d'estudiant és creure que es pot dissenyar un sistema Big Data que sigui completament consistent, sempre disponible i tolerant a particions (CA+P). 

En entorns reals amb milers de nodes connectats per xarxa, les fallades de xarxa són inevitables. Per tant, la tolerància a particions (P) és un requisit obligatori. En cas d'una fallada en la xarxa, l'enginyer ha d'escollir de manera estricta entre **Consistència (CP)** o **Disponibilitat (AP)**; és a dir, o es rep una dada potencialment no actualitzada o es bloqueja la petició esperant assegurar la consistència.

---

## 3. Arquitectura d'Apache Hadoop

### Intenció

Apache Hadoop sorgeix per donar resposta pràctica als requeriments anteriors, basant-se en el treball d'enginyeria publicat per Google a principis dels anys 2000 per al seu motor de cerca. L'objectiu de Hadoop és oferir una plataforma escalable, robusta i fiable.

### La Idea Bàsica de Disseny

La idea disruptiva de Hadoop consisteix a **distribuir les dades tan bon punt aquestes es guarden en el sistema**. En lloc de moure les dades cap a la computació, Hadoop mou el codi de computació cap on resideixen les dades.

### Conceptes Clau d'Arquitectura

- **Abstracció d'Alt Nivell**: Les aplicacions es programen abstretes dels detalls de baix nivell com la gestió de la xarxa, el control de dependències o les sincronitzacions complexes.
    
- **Minimització de Comunicacions**: Els nodes es comuniquen entre ells tan poc com sigui possible durant l'execució per evitar saturar la xarxa.
    
- **Distribució a Priori**: Les dades es reparteixen de manera anticipada entre les diferents màquines de l'entorn.
    
- **Localització de la Computació**: La computació s'executa, sempre que sigui possible, en el node físic exacte on estan emmagatzemades les dades a processar.
    
- **Replicació de Dades**: Per assegurar l'alta disponibilitat i la fiabilitat de la informació, les dades es repliquen múltiples vegades al llarg del clúster.
    

### Components del Clúster

Un clúster de Hadoop està compost per un conjunt de màquines individuals de propòsit general denominades **nodes**. El clúster pot escalar des d'un únic node de desenvolupament fins a milers de nodes en producció. A nivell de programari, l'ecosistema es fonamenta en dos components bàsics indispensables:

1. **Hadoop Distributed File System (HDFS)**: El sistema de fitxers distribuït encarregat de l'emmagatzemament.
    
2. **MapReduce Software Framework**: L'entorn de programari encarregat de la computació distribuïda.
    

> _Nota_: Tot i que l'ecosistema de Hadoop inclou moltes altres eines com Pig, Hive, HBase, Flume, Oozie, Sqoop o Mahout, el nucli del temari se centra exclusivament en HDFS i MapReduce.

---

## 4. El Sistema de Fitxers Distribuït: HDFS

### Intenció

Entendre el funcionament de l'HDFS és crucial per als exàmens, especialment com gestiona la divisió de fitxers i la seva topologia de replicació per aconseguir tolerància a fallades catastròfiques de maquinari.

### Mecànica d'Emmagatzemament i Blocs

L'HDFS és un sistema de fitxers virtual escrit en Java que s'executa posicionant-se per sobre del sistema de fitxers natiu de cada sistema operatiu del node (com ext4 o NTFS).

Quan un fitxer es carrega a l'HDFS, aquest es divideix automàticament en porcions de mida fixa anomenades **blocs**, la mida típica dels quals és de **64 MB o 128 MB**.
- Les Tasques de mapping treballen en porcions petites de dades (1 bloc)

Aquests blocs es distribueixen de forma asíncrona i immediata entre les diferents màquines (DataNodes) del clúster. Diferents blocs que pertanyen a un mateix fitxer s'emmagatzemen intencionadament en diferents màquines per maximitzar el paral·lelisme.

### Ràtio de Replicació per Defecte

Per defecte, cada bloc de dades es replica en **3 màquines diferents** del clúster. Això garanteix que, davant la caiguda simultània de dos nodes que continguin el mateix bloc, la informació romangui accessible al tercer node sense corrupció.

### Disseny i Optimització de l'HDFS

L'HDFS presenta unes característiques de disseny molt particulars que solen preguntar-se en els exàmens teòrics:

- **Fitxers Grans**: Està optimitzat per treballar millor amb un nombre moderat de fitxers de gran mida (milions de fitxers de 100 MB o superiors). No està dissenyat per gestionar milers de milions de fitxers petits a causa de la saturació de la memòria de metadades.
    
- **Lectures Consecutives**: Està altament optimitzat per a fitxers llargs i operacions d'accés seqüencial a les dades (_streaming de dades_), penalitzant l'accés aleatori (_random access_).
    

### Serveis de l'Arquitectura HDFS (Master/Slave)

L'arquitectura d'emmagatzemament utilitza un patró mestre-esclau molt definit amb els següents serveis en execució:

- **NameNode (Mestre)**: És el node crític del sistema. S'encarrega de mantenir i gestionar de forma centralitzada totes les metadades de l'HDFS. El NameNode sap quins blocs formen un fitxer determinat i en quines màquines físiques estan emmagatzemats exactament.
    
- **Secondary NameNode**: Realitza tasques periòdiques de manteniment de la imatge de metadades de l'HDFS per alleugerir la càrrega del NameNode principal. **Atenció**: No funciona en cap cas com un servidor de _backup_ actiu o de recuperació immediata (_failover_).
    
- **DataNode (Esclaus)**: Són els nodes encarregats de l'emmagatzemament físic pur. S'ocupen de desar i llegir els blocs de dades reals a les unitats de disc locals segons les ordres del mestre.


![[Pasted image 20260518184654.png]]


![[Pasted image 20260518184632.png]]

### Interacció amb l'HDFS via API de Línia de Comandes

Per interactuar amb el sistema de fitxers s'empra el comando d'alt nivell `hadoop fs`. Les dues instruccions bàsiques d'ingrés i extracció d'informació són:

- **Còpia de local cap a l'HDFS**:

    ```bash
    hadoop fs -copyFromLocal local_dir/ hdfs_dir
    ```

### Característiques del Framework

- **Paral·lelització automàtica**: Distribueix la feina entre múltiples nodes sense intervenció del programador.
    
- **Abstracció completa**: Amaga de l'enginyer tota la infraestructura de baix nivell de la xarxa, permetent programar en llenguatges com Java o Python.
    
- **Eines de Monitorització**: Proporciona telemetria integrada per auditar el progrés de les tasques en temps real.
    

### Tractament Robust de Fallades en MapReduce

Hadoop inverteix un gran esforç arquitectònic en la gestió de fallades, prioritzant sempre la **Consistència** i el **Tractament de fallades** per sobre de la disponibilitat immediata de recursos:

- **Caiguda d'un Node de Computació**: El programa Màster detecta la caiguda del node i reassigna immediatament la tasca de mapping o reducció a un altre node del clúster que tingui una rèplica d'aquest mateix bloc de dades.
    
- **Aïllament de Reinici**: Tornar a engegar o reassignar una tasca fallida és una operació independent que no implica cap mena de comunicació ni alteració dels altres nodes que segueixen treballant de forma normal amb les seves porcions de dades.
    
- **Reincorporació Dinàmica**: Si el node caigut es reinicia o es recupera el seu enllaç, s'afegeix de forma completament automàtica al clúster i se li comencen a assignar noves tasques sense necessitat d'intervenció manual.
    
- **Execució Especulativa per Nodes Lents**: Si el mestre detecta que un node s'està executant amb un rendiment degradat o anormalment lent, pot aixecar una instància paral·lela i idèntica d'aquesta mateixa tasca en un altre node alternatiu. El primer node que finalitzi l'execució lliurarà els seus resultats al sistema, i l'altra instància serà descartada.
    

---

## 6. Anatomia d'un Clúster Hadoop i Execució d'un Treball

### Intenció

És fonamental conèixer quines entitats de programari interactuen quan un client llança una petició de computació (_job_) cap al clúster de producció.

### Flux de Funcionament d'un Job

Quan una aplicació client desitja realitzar una lectura de dades o executar un processament, el cicle de vida es divideix en els següents passos ordinals:

1. **Petició del Client**: El Client de Hadoop envia el codi font compilat (un fitxer `.jar` en Java) juntament amb la configuració de l'entorn (un fitxer `.xml`) cap al clúster.
    
2. **Planificació pel JobTracker (Mestre)**: El servei **JobTracker** (situat al Master Node) rep la petició del client, avalua el volum de dades, determina el pla d'execució òptim i comença a distribuir les tasques individuals. Per fer-ho de forma eficient, es comunica prèviament amb el **NameNode** per obtenir la informació exacta de localització (_file location info_) dels blocs que formen els fitxers d'entrada.
    
3. **Execució en els TaskTrackers (Esclaus)**: El JobTracker assigna les tasques de Map i Reduce individuals als serveis **TaskTracker** de cada node esclau (_Slave Node_). El TaskTracker és el responsable directe d'instanciar, executar i monitorar les tasques de Map i Reduce dins d'aquella màquina específica.
    
4. **Lectura Directa de dades en l'HDFS**: Per a l'execució de la tasca o quan una aplicació client simplement requereix fer una lectura d'un fitxer (per exemple, el fitxer `/user/eloi/bar`):
    
    - El client demana al NameNode la llista de blocs i la seva ubicació.
        
    - Un cop obtinguda la metadada, el client o el procés de mapping es comunica **directament amb els DataNodes físics** pertinents (per exemple, els nodes N2, N1 o N3) per extreure o escriure la informació. Això evita que el tràfic de dades massiu hagi de passar pel NameNode mestre, evitant la seva saturació.

![[Pasted image 20260518184841.png]]
![[Pasted image 20260518184854.png]]

---

## 7. MapReduce: L'Algorisme WordCount

### Intenció

L'algorisme de comptar paraules és l'exemple acadèmic per excel·lència (_Hello World_) dels sistemes distribuïts Big Data, utilitzat per il·lustrar la potència de la paral·lelització en MapReduce.

### El Repte del Volum

Comptar la freqüència d'aparició de cada paraula en un text de dimensions colossals és una tasca inviable de realitzar de manera seqüencial en una sola màquina. Tot i així, és un problema conceptualment senzill de paral·lelitzar si distribuïm adequadament els fragments del text al llarg del clúster.

### Desenvolupament de les Fases de WordCount

1. **Descomposició de Dades**: Hadoop s'encarrega de rebre el fitxer de text de l'usuari i descompondre'l de forma totalment automàtica en blocs de l'HDFS.
    
2. **Fase Map**: Cada node esclau agafa un bloc de text i processa l'entrada línia a línia. Per cada paraula que troba, emet una parella clau-valor simple on la clau és la paraula en si i el valor és el número 1 de forma individual (per exemple, `(paraula, 1)`), sense realitzar sumes en aquest punt.
    
3. **Fase de Shuffle & Sort**: El motor de Hadoop agrupa totes les paraules idèntiques provinents de tots els mapatges, ordenant el llistat per la clau (la paraula).
    
4. **Fase Reduce**: La funció Reduce rep com a entrada la paraula i un llistat amb tots els valors unitaris associats (ex: `(paraula, [1, 1, 1, 1])`). La funció procedeix a executar l'operació d'agregació sumant tots els valors per obtenir el recompte absolut final d'aquella clau en tot el fitxer.

---

# 4. Spark

## 1. Introducció i Motivació de Spark

### Intenció - Perquè es fa Spark?

L'evolució de l'anàlisi de dades massives (_Big Data_) ha requerit el disseny de nous models de programació distribuïda que superin les limitacions dels frameworks tradicionals (MapReduce), garantint alhora la tolerància a fallades.

### Motivació i Limitacions de MapReduce

L'objectiu fonamental de Spark és suportar una gamma més àmplia d'aplicacions que el model MapReduce, mantenint el seu sistema automàtic de tolerància a fallades. MapReduce esdevé altament ineficient per a programes de múltiples passades que no requereixen d'un intercanvi massiu de dades entre múltiples operacions paral·leles.

Aquestes ineficiències afecten directament tasques molt comunes en Big Data, tals com:

- **Algorismes Iteratius:** Inclouen la gran majoria de fluxos de treball d'Aprenentatge Automàtic (_Machine Learning_) i els algorismes de grafs.

- **Mineria de Dades Interactiva:** Escenaris on un usuari carrega un conjunt de dades en memòria mitjançant un _cluster_ i hi realitza consultes repetides.

- **Aplicacions d'Streaming:** Sistemes que requereixen mantenir i actualitzar un estat agregat de les dades al llarg del temps.

---

## 2. Característiques Fonamentals i Arquitectura Spark vs. Hadoop

### Intenció

Comprendre la diferència arquitectònica en la gestió del flux de dades i de l'emmagatzematge intermedi entre els frameworks clàssics basats en disc i els moderns basats en memòria distribuïda.

> **Referència:** Diapositives 3 i 4.

### Spark vs. Hadoop (MapReduce)

Mentre que MapReduce es basa en fer córrer una sèrie de tasques independents on cadascuna d'elles llegeix obligatòriament d'un disc físic (com HDFS) i torna a escriure-hi els resultats intermedis, Spark optimitza radicalment aquest procés. El fet de llegir i escriure les dades de forma replicada a cada pas computacional afegeix un cost de latència i d'E/S (_I/O_) molt significatiu.

Spark introdueix una abstracció central anomenada **Resilient Distributed Datasets (RDD)**, la qual es manté resident en la memòria distribuïda del _cluster_ entre les diferents peticions. Això elimina la necessitat de persistir i replicar estats intermedis a disc de forma contínua. En lloc de dependre de la replicació física per a la tolerància a fallades, Spark fa servir la **traçabilitat** (_lineage_): cada RDD recorda exactament com va ser construït a partir d'altres _datasets_ primigenis o operacions prèvies (com `map`, `join` o `groupBy`), permetent recomputar de forma aïllada i sota demanda qualsevol fragment de dades perdut.

A nivell de construcció tecnològica, Spark està implementat nativament utilitzant el llenguatge **Scala**, i ofereix de base APIs completament funcionals per a **Python** i **Java**.

---

## 3. Arquitectura del Cluster: Driver i Workers

### Intenció

Estudiar la topologia mestre-esclau de l'entorn d'execució de Spark i com es distribueixen les tasques i el cicle de vida de les aplicacions de programari distribuït.

> **Referència:** Diapositives 5 i 6.

### Components de la Topologia

L'execució de qualsevol codi Spark requereix el desplegament coordenat de dos tipus de programes diferenciats:

- **Driver Program (Programa Driver):** És el procés central que s'executa en un node passarel·la (_gateway node_). S'encarrega d'orquestrar l'aplicació i de controlar el flux d'execució general.

- **Worker Nodes (Nodes Treballadors):** Són els nodes encarregats d'executar les tasques reals de computació. Es poden executar directament en nodes dedicats del _cluster_ o instanciar-se mitjançant fils locals (_local threads_). Cada Worker allotja un procés **Executor** que gestiona una **Cache** de memòria i executa diferents unitats de treball anomenades **Tasks** (Tasques). Els objectes RDD es troben fragmentats i distribuïts de forma horitzontal al llarg de la memòria d'aquests workers.

Entre el Driver i els Workers actua el **Cluster Manager**, que s'encarrega de l'assignació física de recursos.

### L'Objecte SparkContext

Abans de realitzar qualsevol computació, un programa Spark ha d'instanciar obligatòriament un objecte **SparkContext**. Aquest objecte actua com el punt d'entrada principal de l'aplicació i compleix les següents funcions crítiques:

- Indica formalment a l'aplicació Spark com i a on s'ha d'accedir al _cluster_ de nodes.

- S'utilitza de forma explícita mitjançant la variable de referència `sc` per a la creació inicial dels RDDs.

- El seu paràmetre configuatiu anomenat `master` determina de manera unívoca el tipus i la mida de la topologia del _cluster_ utilitzat.

---

## 4. L'Abstracció RDD (Resilient Distributed Datasets)

### Intenció

Analitzar formalment el funcionament intern, les propietats de disseny de la col·lecció de dades distribuïda de Spark i el seu model de particionament.

> **Referència:** Diapositives 7, 8 i 11.

### Propietats Core de l'RDD

L'RDD és la principal abstracció de dades dins de l'ecosistema Spark. Les seves característiques fonamentals de disseny programàtic són:

- **Immutabilitat:** Un cop un RDD ha estat construït, el seu estat és absolutament immutable i no pot ser modificat.

- **Traçabilitat Integrada:** Monitoritza i enregistra tota l'activitat i transformacions que s'apliquen sobre ell, permetent recomputar eficientment qualsevol pèrdua parcial o total de dades en cas d'avaria en algun node.

- **Execució Paral·lela:** Permet l'execució d'operacions concurrents i paral·leles sobre col·leccions d'elements distribuïts.

Un RDD pot ser construït seguint tres mecanismes principals: paral·lelitzant una col·lecció de dades en memòria que ja existeixi en el programa driver, transformant un RDD preexistent, o mitjançant la lectura directa de fitxers emmagatzemats en un sistema de fitxers distribuït (com HDFS o qualsevol altre emmagatzematge compatible).

### Particionament i Paral·lelisme

El programador té la potestat d'especificar explícitament el nombre de **particions** en què es divideix lògicament un RDD. Com a regla general d'arquitectura de programari distribuït, un **major nombre de particions es tradueix en un major nivell de paral·lelisme** potencial. Això obstant, en fase de disseny cal equilibrar acuradament aquesta relació tenint en compte el nombre de nodes físics reals i els fils de processament (_threads_) disponibles al sistema.

### Mecanismes de Caching

Un RDD es pot fer persistent de forma explícita a la memòria dels workers invocant els mètodes `.persist()` o `.cache()` sobre el propi objecte. Aquesta memòria cache manté la propietat de tolerància a fallades: si qualsevol fragment o partició es perd, l'arquitectura el recalcula automàticament de manera transparent fent servir el seu historial de transformacions original.

---

## 5. Operacions sobre RDDs: Transformacions i Accions

### Intenció

Classificar els dos tipus d'operacions en Spark, entenent el paradigma d'avaluació mandrosa (_lazy evaluation_) i les funcions de transformació i agregació de dades.

> **Referència:** Diapositives 8, 9, 10 i 12.

### Transformacions i Avaluació Mandrosa

Les **Transformacions** s'encarreguen de crear nous conjunts de dades distribuïts agafant com a origen un RDD preexistent. Operen sota el paradigma de l'**avaluació mandrosa (_lazy evaluation_)**, cosa que significa que els resultats de les funcions no es computen de manera immediata quan es declaren al codi. En el seu lloc, Spark construeix i guarda internament el graf o conjunt de transformacions ordenades que caldrà aplicar al dataset. Aquesta estratègia permet:

- Optimitzar de forma global els càlculs i els plans d'execució necessaris abans d'executar-los.

- Facilitar la recuperació automàtica davant de caigudes del sistema o de la presència de workers lents (_stragglers_).

Arquitectònicament, es pot conceptualitzar una transformació com una **recepta** conceptual per a obtenir un resultat final.

| Transformation | Description |
| -------------- | ----------- |
| `map(func)` | Retorna un nou dataset distribuït format en passar cada element de la font original a través d'una funció `func`. |
| `filter(func)` | Retorna un nou dataset format seleccionant només aquells elements de la font on la funció `func` retorna l'estat _true_. |
| `distinct([numTasks])` | Retorna un nou dataset distribuït que conté els elements únics (sense duplicats) de la font original. |
| `flatMap(func)` | Similar a `map`, però cada element d'entrada es pot mapejar a 0 o més elements de sortida (la funció `func` ha de retornar una seqüència `Seq` en lloc d'un únic ítem). |

### Accions

Les **Accions** són operacions que forcen a Spark a executar de manera efectiva tot el graf de transformacions acumulat sobre el conjunt de dades. Són l'únic mecanisme disponible per tal d'enviar o extreure resultats cap a l'exterior del framework (com ara retornar les dades al programa driver o escriure-les a un sistema de fitxers).

| Action | Description |
| ------ | ----------- |
| `reduce(func)` | Agrega els elements d'un dataset mitjançant una funció `func`. Aquesta funció pren dos arguments i en retorna un de sol; ha de ser commutativa i associativa per poder ser computada correctament en paral·lel. |
| `take(n)` | Retorna una matriu (_array_) que conté els primers $n$ elements del dataset. |
| `collect()` | Retorna absolutament tots els elements del dataset en forma de matriu al programa principal. **AVÍS D'EXAMEN:** Cal assegurar-se prèviament que la mida del volum de dades hi cabrà físicament en la memòria del _driver program_ per evitar un col·lapse del sistema. |
| `takeOrdered(n, key=func)` | Retorna $n$ elements del dataset ordenats de manera ascendent o segons s'especifiqui en una funció de clau (`key=func`) opcional. |

### Cicle de Vida d'un Programa Spark

L'execució d'una aplicació en Spark descriu una seqüència de quatre fases ben definides:

1.  **Creació:** Es construeixen els RDDs originals a partir de fonts de dades externes o es paral·lelitza una col·lecció resident en la memòria del programa driver.

2.  **Transformació:** S'apliquen de manera mandrosa seqüències de transformacions sobre les dades per anar generant nous RDDs intermedis.

3.  **Persistència:** Es marquen de manera opcional aquells RDDs que es volen retenir en memòria mitjançant operacions de _caché_ per a optimitzar futures reutilitzacions.

4.  **Execució:** Es llança una acció final que executa de forma efectiva totes les computacions distribuïdes en paral·lel, produint els resultats desitjats pel flux de treball.

---

## 6. Model de Comunicació: Variables Compartides

### Intenció

Entendre la gestió de variables globals en un sistema distribuït de memòria compartida virtual, els problemes derivats dels tancaments (_closures_) de codi i les solucions de readifusió i acumulació.

> **Referència:** Diapositives 13 i 14.

### El Problema dels Closures en els Workers

Spark crea de manera completament automàtica **tancaments (_closures_)** quan s'envien funcions cap als workers (com per exemple en invocar un `map`). Aquests _closures_ encapsulen les funcions juntament amb el seu propi entorn de variables, incloent-hi qualsevol variable de caràcter global que estigui sent utilitzada pels nodes treballadors.

El model de disseny està pensat perquè **no es requereixi cap mena de comunicació de dades directa entre workers** durant l'execució d'aquestes funcions. Això comporta un problema d'estat inherent: **els canvis aplicats a les variables globals dins dels workers són completament locals i no es retornen mai ni es propaguen cap al programa driver** o cap a la resta de workers. Un exemple típic d'aquest problema és intentar incrementar un comptador global dins d'un worker amb l'objectiu de calcular el total global de dades processades de tot el clúster.

### Solucions Arquitectòniques

Per solucionar aquesta mancança de sincronització, Spark proveeix dos tipus específics de variables compartides:

- **Variables de Redifusió (Broadcast Variables):** Dissenyades per enviar de manera altament eficient grans volums de dades de **només lectura** des del node driver cap a cadascun dels workers del clúster. Es guarden de manera persistent en la memòria local dels nodes treballadors per a ser utilitzades de manera repetida en una o diverses operacions successives, evitant retransmissions ineficients.

- **Variables Acumuladores (Accumulators):** Dissenyades específicament per realitzar operacions d'agregació associativa i commutativa de valors numèrics (suporten tipus de dades com _integers_, _double_, _long_ i _float_) des dels diferents workers cap al driver. Tenen una restricció d'accés asimètrica: **només el programa driver té permís per llegir el valor final de l'acumulador**. Per als workers, l'acumulador és un element estrictament de **només escriptura**. Es poden declarar tant en accions com en transformacions, recordant però una regla de disseny crítica per a exàmens: **només l'execució d'accions garanteix de manera fefaent el processament correcte dels acumuladors**. Un comportament mandrós en una transformació pot provocar que l'acumulador no s'incrementi fins que no s'invoqui una acció sobre aquell flux d'execució.

---

# 5. Web Services

## 1. Introducció als Web Services

Els Web Services representen l'evolució dels objectes distribuïts aplicada a l'escala global d'Internet.


>[!info] Extres: **Paradigmes de Programació Distribuïda**: 
>S'emmarquen dins d'una jerarquia que inclou el pas de missatges, arquitectures client-servidor, aplicacions web (MVC sobre HTTP), RMI/RPC i sistemes P2P .
>
   
- **Definició**: Proveeixen una interfície de servei equivalent a objectes distribuïts sobre el web, garantint la interoperabilitat total a Internet .
    
- **Ús i Propòsit**: Són essencials per a la integració B2B (_business-to-business_) i actuen com a _middleware_ per al _Cloud Computing_ .
    
- **Accés**: No estan dissenyats per a ser accedits directament per usuaris via navegador, sinó per aplicacions client dedicades.

#### Creació: 
- **Components de Disseny**: Al crear-los, s'ha d'especificar:
- la representació de dades (JSON, XML, SOAP), 
- la descripció del servei (WSDL, API), 
- el directori de serveis (UDDI) 
- el protocol d'accés (HTTP, TCP) .
    
- **Arquitectures Principals**: Destaquen XML-RPC, SOAP+WSDL i, sobretot, l'estil RESTful .
    

## 2. RESTful Web Services

REST (_Representational State Transfer_) no és un protocol, sinó un estil d'arquitectura que aprofita les capacitats nadiues de l'HTTP.

![[Pasted image 20260418100232.png]]

- **Filosofia**: Es basa en una aproximació amb un estil d'operacions molt restrictiu on s'emfatitza la manipulació dels recursos .
    
- **Principis Bàsics**:
    
    - Ús explícit dels mètodes HTTP.
        
    - Independència d'estats (_Stateless_).
        
    - URIs estructurades com directoris.
        
    - Transferència de dades en XML o JSON.
        
- **Mètodes HTTP Explícits**:
    
    - **GET**: Recuperar un recurs (segur i idempotent).
        
    - **POST**: Crear un nou recurs (no és idempotent).
        
    - **PUT**: Actualitzar o canviar l'estat d'un recurs (idempotent).
        
    - **DELETE**: Eliminar un recurs.
        
- **Exemple de flux**: Un recurs creat amb POST obté una nova URL, que després pot ser consultada amb GET o modificada amb PUT.

![[Pasted image 20260418100358.png]]

#### Exemples - POST

![[Pasted image 20260418100533.png]]

#### Exemples - PUT

![[Pasted image 20260418100607.png]]

## 3. El Servidor Stateless i el Sistema de Caché

L'escalabilitat de REST prové de traslladar la responsabilitat de l'estat al client i optimitzar la xarxa mitjançant cachés.

- **Disseny Stateless**: El servidor no manté sessions; cada petició ha de ser completa i independent.
    
- **Control de Caché**: El servidor utilitza capçaleres com `Cache-Control` per indicar si un recurs es pot guardar localment.
    
- **Paràmetres Clau**:
    
    - `max-age`: Temps en segons que el recurs és vàlid a la caché.
        
    - `Expires`: Data específica de caducitat.
        
- **Requests Condicionals**: Permeten estalviar amplada de banda preguntant si el recurs ha canviat.
    
    - **Time-based**: Ús de `Last-Modified` al servidor i `If-Modified-Since` al client. Si no ha canviat, el servidor respon amb un codi **304 Not Modified** .
        
    - **Content-based**: Ús d'**ETag** (un hash del contingut). El client envia `If-None-Match` per verificar si la versió local coincideix amb la del servidor .
        
![[Pasted image 20260418100754.png]]

## 4. Estructura de URIs i Representació de Recursos

La interfície ha de ser "neta" i les dades han de ser fàcilment processables per màquines.

- **URIs Intuïtives**: Han de ser directes, predictibles i evitar els _query strings_ (paràmetres `?id=...`) sempre que sigui possible.
    
- **Exemple de bona URI**: `http://www.myservice.org/discussion/2026/04/15/topic`.
    
- **Representació**: Reflecteix l'estat del recurs en el moment de la petició, normalment mitjançant JSON (`application/json`) o XML (`application/xml`) .
    
- **Llibreries**: Existeixen eines com GSON per passar d'objectes natius (com Java) a estructures JSON automàticament .
    

## 5. Gestió de Sessions i Limitacions HTTP

HTTP és un protocol _stateless_, però les aplicacions necessiten continuïtat (sessions).

- **El rastre de l'usuari**: El navegador ha de mantenir un identificador de sessió que el servidor pugui reconèixer .
    
- **Estratègies de Sessió**:
    
    - **Camps Ocults**: `<input type="hidden">`. Insegur, ja que és visible al codi font .
	    ![[Pasted image 20260418101148.png]] 
    - **Cookies**: Peça d'informació enviada pel servidor (`Set-cookie`) que el client torna a cada petició a una URL vàlida .
	    ![[Pasted image 20260418101208.png]]
        
    - **URL Rewriting**: Passar l'identificador com a paràmetre a cada enllaç. Si el client perd el paràmetre, perd la sessió .

>[!warning] SEGURETAT!
>Tots els sistemes anteriors són poc segurs, evita enviar informació compromerssa per mantenir la sessió, i fes-los que expirin (els id de sessió)

- **Seguretat**: Les dades de sessió poden ser manipulades o capturades si s'envien en text pla. És vital fer servir identificadors que expirin i no enviar mai informació sensible directament .
    

## 6. Autentificació: De l'Accés Bàsic al JWT

Com garantim que l'usuari és qui diu ser en un entorn distribuït.

- **Accés Bàsic (Basic Auth)**: Concatena usuari i passaport amb ":" i ho codifica en Base64. És trivial de descodificar i només és segur sota **HTTPS** .
    
- **JSON Web Token (JWT)**: Estàndard modern (RFC 7519) per transmetre dades sensibles de forma autocontinguda i signada .
	- Són generats per servidor, i les dades estàn autocontingdes al token
    
- **Parts d'un JWT**:
    
    1. **Header**: Algorisme de signatura i tipus.
        
    2. **Payload**: Dades de l'usuari (issuer, subject, expire, etc.) .
        
    3. **Signature**: Hash del header i payload signat amb una clau privada.
        
- **Flux JWT**: El client fa login, el servidor genera el JWT i el retorna; a partir d'aquí, el client l'envia a la capçalera d'autorització de cada petició .
    

## 7. Asincronia i Comunicació Bidireccional

HTTP tradicional no permet que el servidor iniciï comunicació, però hi ha solucions.

- **AJAX (Asynchronous JavaScript and XML)**: Permet recepció de dades no bloquejant al client-side usant l'objecte `XMLHttpRequest`. Associa una funció a l'esdeveniment `onreadystatechange` per processar la resposta quan arribi .
    
- **WebSockets**: Canal bidireccional i _full-duplex_ sobre un únic socket TCP. Permet interacció en viu (jocs, xats). Només el _handshake_ inicial és HTTP; després es passa a un protocol TCP propi al port 80 .
    
- **Ecosistema**: Llibreries com JQuery o React, i frameworks com Vue o Angular faciliten la gestió de l'asincronia i la manipulació del DOM .
