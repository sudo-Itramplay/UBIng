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

L’objectiu principal de RMI és que els programadors desenvolupin
aplicacions distribuı̈des amb Java usant la mateixa sintaxi i
semàntica que les aplicacions Java tradicionals.

Per implementar una aplicació RMI funcional, cal seguir una estructura de classes molt precisa.

- **Components de l'Arquitectura**:
	- **Objecte Remot**: Aquells objectes que algun dels seus mètodes espoden invocar des d’un altre procés corrent en una màquina remota.
	
	- **Objecte Local**: Aquells objectes que només poden ser invocats per un procés local en el qual l’objecte existeixi.
	
	- **Invocació de mètode remot**: Acció d’invocar un mètode d’una interfı́cieremota en un objecte remot.
    
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
>La classe del servidor d’objecte remot és una classe que té el codi
que crea i exporta un objecte remot.

   
- **Exportació manual**: Si no podem heretar (perquè ja heretem d'una altra classe), hem d'utilitzar el mètode estàtic `UnicastRemoteObject.exportObject(obj, port)`.

>[!tip] Recorda
>l’exportació d’objecte distribuı̈t fa que el procés del servidor comenci a escoltar i esperi que els clients es connectin i sol·licitin el servei de l’objecte.
   
- **Concurrència al Servidor**: Heu de tenir present que un servidor RMI és **concurrent per naturalesa**. Cada petició d'un client s'executa en un fil (thread) separat. Com a enginyers, és la vostra responsabilitat aplicar mecanismes de sincronització (`synchronized`, panys) si els mètodes accedeixen a recursos compartits per evitar condicions de carrera.
    
- **Publicitat de l'objecte**: El `main` del servidor ha de crear la instància de la implementació i lligar-la al registre amb un nom únic per fer-la accessible al món exterior.
    

### L'Aplicació Client i la Mecànica de Crida

El client ha de ser capaç de "traduir" una referència abstracta en una crida de mètode real.

- **Localització i Casting**: El client obté un objecte genèric del registre. És un **error comú** intentar convertir-lo a la classe d'implementació; el client **només ha de conèixer la interfície**. El casting s'ha de fer sempre cap a la interfície remota (ex: `(DateServer) Naming.lookup(...)`).

>[!fail] Error comú
>És un error comú convertir la referència obtinguda des el registre a la classe d’implementació de la interfı́cie en comptes de la classe d’interfı́cie.
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

