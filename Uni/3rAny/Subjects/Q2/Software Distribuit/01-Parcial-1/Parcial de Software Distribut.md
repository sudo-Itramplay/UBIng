
# Tema 1 - Introduccio

> [!abstract] Resum del 1r Parcial · notes atòmiques al [[_MOC|MOC de SD]]
> **Intro:** [[Software Distribuït]] · [[Reptes dels Sistemes Distribuïts]] · [[Middleware]] · [[Arquitectura Multicapa]] · [[Tipologia de Clients]]
> **SO:** [[Procés i Thread]] · [[IPC i Protocols]] · [[Sincronització]]
> **Client-Servidor:** [[Model Client-Servidor]] · [[Sockets]] · [[TCP Stream-mode]] · [[UDP Datagram-mode]] · [[Endianness i Marshalling]] · [[Tipus de Servidors]] · [[Multicast]]
> **Threads:** [[Threads]] · [[Threads a Java]] · [[Problemes de Concurrència]] · [[Sincronització en Java]] · [[Coordinació de Threads]]
> **Web:** [[Web]] · [[HTTP]] · [[Contingut Dinàmic Web]] · [[MVC]]

## 1. Software Distribut

- **Definició bàsica:** Sistemes on ordinadors independents col·laboren per a una tasca comuna.

## 2. Models d'Arquitectura (Rols i Responsabilitats)

Hi ha tres models principals segons com es reparteixen la feina:

Models:
	Ordinador central amb terminals
	Client/Servidor
	P2P

### A. Model d'Ordinador Central (Mainframe)

- **Arquitectura:**
    
    - **Central:** Conté totes les dades i la lògica.
        
    - **Terminals:** Només fan la presentació (pantalla).
        
- **Problemes:** Saturació del servidor i usuaris sense capacitat de transacció pròpia.
    

### B. Model Client/Servidor

- **Arquitectura:**
    
    - **Servidor:** Dades + Lògica.
        
    - **Client:** Presentació + Lògica.
        
- **Funcionament:** La connexió sempre l'inicia el client (rols asimètrics).
    
- **Nota:** Un servidor pot actuar com a client d'un altre servidor.
    
- **Problemes:** Escalabilitat.
    

### C. Model Peer-to-Peer (P2P)

- **Arquitectura:** Rols simètrics. Cada node (_Peer_) fa de computació i comunicació. No hi ha distinció client-servidor.
    
- **Problemes:**
    
    - Major complexitat (lògica i dades totalment distribuïdes).
        
    - **Bootstrap problem:** Dificultat per localitzar el servei inicialment.
        

---

## 3. Reptes dels Sistemes Distribuïts

Per garantir un bon funcionament, cal solucionar 8 reptes:

1. **Heterogeneïtat:** Gestionar diferents protocols, middleware i fer codi portable.
    
2. **Accessibilitat (Openness):** Publicar protocols, APIs i documentació clara.
    
3. **Seguretat:** Encriptació de dades sensibles.
    
4. **Escalabilitat:** Gestionar recursos HW/SW per controlar la pèrdua de rendiment en créixer.
    
5. **Tractament d'errors:** Detectar, tolerar i recuperar-se de fallades.
    
6. **Concurrència:** Controlar l'accés simultani a recursos compartits.
    
7. **Transparència:** Que la localització i l'accés siguin invisibles per a l'usuari.
    
8. **Qualitat del servei (QoS):** Garantir confiabilitat, seguretat i rendiment.

---

## 4. Middleware


**Definició de Middleware:** Capa que ofereix un alt nivell d'abstracció per desenvolupar aplicacions distribuïdes.

---

## 5. Patrons d'Arquitectura Multi-capa

Es passa d'aplicació monolítica a modular. Les capes lògiques són:

1. **Usuari:** Presentació i navegació.
    
2. **Negoci:** Lògica, validació i gestió d'esdeveniments.
    
3. **Dades:** CRUD (Create Retrieve Update Delete) i integritat.
    
4. **Sistema:** Accés a fitxers, autenticació, logs, errors.
    

### Capes Físiques (Deployment)

- **Single-Tiered:** 1 màquina. Poc flexible i mono-usuari.
    
- **2-Tier (Client/Servidor):** Multi-usuari. La capa de negoci queda dividida (part al client, part al servidor).
    
- **3-Tier:** Client / Negoci / Dades. Cada màquina té una responsabilitat clara, però augmenta la complexitat i el nombre de missatges.
    
- **N-Tier:** Múltiples servidors per capa. Molt escalable.
    

---

## 6. Tipologia de Clients

- **Client Gruixut (Thick):** Conté 1 o 2 capes senceres (molta funcionalitat). Requereix bon hardware.
    
- **Client Prim (Thin):** Només capa d'usuari (ex: navegador web). Interfície senzilla d'entrada/sortida.
    
- **Client Intermig (Pump Client):** Capa d'usuari + una petita part de la capa de negoci (validacions simples).




---
# Tema 2 - Client/Servidor

## Pas de missatges
El pas de missatges és el paradigma més bàsic per a les aplicacions
distribuïdes:

1. Un procés envia un missatge que representa una petició.
2. El missatge es lliura a un receptor, que processa la sol.licitud, i envia un missatge en resposta.
3. Al seu torn, la resposta pot desencadenar una nova sol.licitud, la qual condueix a una resposta posterior, i aixı́ successivament.

## Model Client-servidor
el model **Client-Servidor**, que és el paradigma dominant a Internet.

Aquest model es basa en l'assignació de **rols asimètrics** a dos processos que col·laboren:
- **El Servidor:** Actua com un proveïdor de serveis que espera passivament les sol·licituds. La seva funció principal és escoltar i acceptar peticions.
   
- **El Client:** És qui inicia la comunicació fent sol·licituds específiques i espera la resposta del servidor

>[!info] Enrecordat
>Aquesta asimetria simplifica enormement la sincronització d'esdeveniments a la xarxa.

Les operacions bàsiques que es requereixen per donar suport
tant a pas de missatge com client-servidor són:

- enviar 
- rebre.

Per comunicacions **orientades a la connexió**, les operacions de:
- connexió 
- desconnexió 
també es requereixen.

>[!tip] Similitud
Amb  aquest model, els processos interconnectats realitzen operacions d’entrada/sortida d’una manera similar a E/S amb fitxers. 


## API de Sockets i Tipologies

L'API de sockets és el mecanisme que permet la comunicació entre processos situats en màquines diferents, encapsulant els detalls del sistema operatiu.

>[!tip] Disseny
>L’API està dissenyada per:
> 1. Acomodar múltiples protocols de comunicació (TCP / IP, UNIX, APPLETALK)
> 2. Implementar codi servidor que queda a l’espera de connexions i codi client que inicia aquestes connexions
> 3. Ser coherent amb l’ús de fitxers en Unix.

>[!info] Socket
> Un **socket** es defineix com el punt final d'un enllaç de comunicació.
> 
>- Aquesta API està dissenyada per ser coherent amb l'ús de fitxers en Unix, facilitant operacions similars a l'entrada/sortida de dades estàndard

Els sistemes operatius suporten principalment tres tipus de sockets segons el protocol de transport:

- **Stream (SOCK_STREAM):** 
	- Utilitzen el protocol **TCP**. Proporcionen un flux de dades bidireccional, fiable, seqüencial i sense duplicats. En Java, es gestionen mitjançant les classes `ServerSocket` (per acceptar connexions) i `Socket` (per a l'intercanvi de dades).

- **Datagram (SOCK_DGRAM):** 
	- Utilitzen el protocol **UDP**. Són fluxos de missatges bidireccionals on no es garanteix l'ordre ni l'arribada, però són més ràpids per a comunicacions unicast o multicast.

- **Raw (SOCK_RAW):** 
	- Utilitzen **ICMP** i normalment només són accessibles per a l'usuari root per al desenvolupament de nous protocols.


## Stream mode i Gestió de Dades

El flux de treball d'un servidor orientat a la connexió segueix un ordre estricte: 

1. crear el socket de connexió,
2. escoltar, 
3. acceptar la petició (creant un nou socket de dades), 
4. realitzar l'I/O 
5. finalment tancar 

![[Pasted image 20260219092320.png]]

Un mètode crític és `accept()`, que és **bloquejant**; el procés s'atura fins que arriba un client.

>[!warning] Error comú
>Un dels errors més comuns en l'enginyeria de software és no gestionar les **recepcions parcials**. 
>- Les funcions `read` no garanteixen rebre tots els caràcters sol·licitats de cop; per tant, s'ha d'implementar un bucle que llegeixi fins a completar el nombre de bytes esperats .


A l'hora de transmetre dades, cal considerar:
- **Ordre de bytes (Endianness):** Per a enters, se sol utilitzar **BigEndian** per a la xarxa.

- **Cadenes de caràcters:** Poden ser de mida fixa o variable. En les variables, és necessari enviar primer una "capçalera" que indiqui la longitud de la cadena que vindrà a continuació.

- **Classes de suport:** Java ofereix `DataInputStream` i `DataOutputStream` per facilitar la lectura i escriptura de tipus primitius (com `read_int32` o `writeBytes`).

#### Endianess
La memòria no és una caixa màgica, sinó una seqüència de bytes.
- Com ordenem aquests bytes quan una dada ocupa més d'una posició (com un sencer de 32 bits) és el que anomenem **Endianness**.

Quan treballem amb dades com un sencer de 4 bytes (32 bits), tenim dues maneres principals d'organitzar-los en la memòria o en un enviament per xarxa:

- **Big-Endian (BE):** És l'ordre que ens resulta més "natural" als humans. El byte més significatiu (el que té més valor o la part "alta" del número) s'emmagatzema o s'envia primer.
    - En el codi de `ComUtils`, quan volem passar un sencer a bytes en format BE, veiem que el primer byte de la matriu (`bytes[0]`) s'omple amb els 8 bits més alts del número, obtinguts mitjançant un desplaçament de 24 bits a la dreta: `(number >> 24) & 0xFF`.
    
    - Aquest és l'estàndard habitual per a les comunicacions a Internet, sovint anomenat _Network Byte Order_.
    
- **Little-Endian (LE):** Aquí el byte menys significatiu (la part "baixa") es guarda primer.
    
    - Segons la implementació de l'assignatura, en aquest cas el primer byte de la matriu (`bytes[0]`) simplement rep els darrers 8 bits del número sense cap desplaçament: `number & 0xFF`.
    
    - Aquesta és l'arquitectura que fan servir, per exemple, els processadors Intel (x86).

### Codi Exemple De DataInput i Endianess
![[Pasted image 20260219092419.png]]


## 4 Topologia de Servidors i Datagram-Mode

![[Pasted image 20260220200038.png]]
![[Pasted image 20260220200154.png]]
>[!tip] Java
>En Java, l’API de sockets Datagram-mode proveix dues classes:
>- DatagramSocket: per als sockets.
>- DatagramPacket: per intercanviar datagrames.
>
Un procés que vulgui enviar o rebre dades fent servir aquesta API ha de crear una instància d’un objecte DatagramSocket. Cada socket està enllaçat a un port UDP de l’equip local.

### Sockets

### No orientats a connexió
Amb sockets sense connexió, és possible que diversos processos
enviïn simultàniament datagrames al mateix socket establert per un
procès de recepció.
	- En aquest cas l’ordre de l’arribada d’aquests missatges serà impredictible, d’acord amb el protocol UDP

### Servers
Els servidors es poden classificar segons diversos criteris de disseny:

- **Amb estat vs. Sense estat:** Un servidor **amb estat** manté informació de cada client, cosa que pot millorar el temps de resposta però dificulta la recuperació davant d'errors (si el client cau, l'estat queda inconsistent). Els servidors **sense estat** són més senzills de codificar i mantenir.
![[Pasted image 20260220201647.png]]

- **Orietats i no Orientats a Connexió**: No orientats a la connexió Utilitza API Datagram-mode. 
	- Les sessions amb clients simultanis es poden intercalar.
Orientat a la connexió Utilitza API Stream-mode.

- **Iteratius vs. Concurrents:** L'iteratiu només serveix un client a la vegada, mentre que el concurrent permet múltiples sessions simultànies.

### Datagrames
En el **Datagram-Mode (UDP)**, la comunicació no és orientada a la connexió. 

- No hi ha un `accept()`; el servidor simplement rep paquets (`DatagramPacket`) a través d'un `DatagramSocket`. 
- Un detall vital per a l'examen: si un datagrama s'envia abans que el receptor hagi llançat l'operació de rebre, les dades es descarten i es perden per sempre. 
A més, amb UDP l'ordre d'arribada és totalment impredictible si diversos processos envien dades simultàniament al mateix socket.


## Concurrència, Selectors i Multicast

Per gestionar múltiples clients de manera eficient, recorrem als **Servidors Concurrents**, que utilitzen fils d'execució (Threads) o processos per a cada client. 

- Això permet que el fil principal continuï acceptant connexions mentre els "fills" gestionen el protocol de cada client. 
- Una alternativa a l'ús massiu de threads és el **Non-blocking I/O (nio)** de Java, que utilitza un **Selector** per gestionar múltiples canals amb un sol fil, evitant el bloqueig en les operacions de `read` o `accept`.


Altres consideracions d'implementació crítiques inclouen:

- **Gestió d'excepcions:** És obligatori usar blocs `try-catch` i, especialment, el bloc **finally** per assegurar que els sockets es tanquen sempre, fins i tot si hi ha errors.

- **Timeouts:** Tots els sockets de dades han de tenir un temps d'espera limitat per detectar fallades en la connexió i no quedar-se bloquejats indefinidament.
- **Diversos tipus de cast**:
	- **Multicast**
		- Es defineix com el paradigma d'enviament de dades cap a múltiples receptors de manera simultània.
		- A diferència de l'Unicast (1 a 1), permet optimitzar el trànsit de xarxa en no haver de duplicar el missatge per a cada destinatari.
		    
		- En l'àmbit de transport, s'utilitza exclusivament el protocol UDP, la qual cosa implica que la comunicació no és fiable i no s'estableix una connexió prèvia.
	- **IP Multicast**
		- Aquest mecanisme es construeix directament sobre l'Internet Protocol (IP), operant en les capes baixes del model de xarxa.
	    
		- La seva funció principal és permetre l'enviament d'un paquet IP a un conjunt determinat de màquines que s'han organitzat en un grup.
	    
		- És important destacar que només està disponible a través d'UDP; no existeix una versió de Multicast amb les garanties de TCP.
	    
		- A causa de la seva naturalesa UDP, no ofereix cap garantia que el paquet arribi a tots els destinataris o que ho faci en l'ordre correcte.
	    
	
	- **Grup Multicast**
		- Un grup multicast es diferencia d'un procés individual per la seva adreça d'Internet de la Classe D, compresa entre la 224.0.0.0 i la 239.255.255.255.
		   	 
		- El funcionament és dinàmic: quan una màquina s'afegeix formalment a un grup, el seu sistema operatiu comença a acceptar i processar tots els missatges enviats a aquella adreça.
		   	 
		- Existeix una asimetria interessant: un procés pot enviar paquets a un grup multicast sense necessitat de ser-ne membre.
		   	 
		- Per a proves en xarxes locals, s'utilitza habitualment l'adreça reservada 224.0.0.1, que identifica totes les màquines de la subxarxa local.

---

# Tema 3 - Threads

## Threads a Java i JVM
Aquí ens centrem en com la Màquina Virtual de Java (JVM) gestiona aquests fils i quines són les regles del joc dins d'aquest entorn.

- **Suport natiu a la JVM:** Java permet que una aplicació tingui múltiples fils d'execució corrent de manera concurrent directament sobre la seva màquina virtual.

- **La classe Thread:** Java encapsula tota la funcionalitat dels fils en la classe `Thread`, la qual hereta d' `Object` i implementa la interfície `Runnable`.

- **Cicle de vida i finalització:** Normalment, en engegar la JVM, només existeix un fil. L'execució de l'aplicació continua fins que es compleix una de les següents condicions:
    
    - Es fa una crida explícita al mètode `exit()` de la classe `Runtime`.
        
    - **Tots els fils han acabat** la seva tasca, ja sigui perquè el mètode `run()` ha retornat un valor (ha finalitzat el codi) o perquè s'ha produït una excepció no controlada que ha propagat fora d'aquest mètode.
        
- **Mecanismes de creació:** Java ofereix dues vies principals per definir el comportament d'un nou fil, permetent flexibilitat segons el disseny de la teva aplicació:
    
    1. Crear una classe que **hereti directament de la classe Thread**.
        
    2. Crear una classe que **implementi la interfície Runnable** i passar aquesta instància al constructor d'un objecte `Thread`.

## Opcions d'Implementació
Aquesta part és la més pràctica i la que segurament hauràs d'aplicar directament al teu codi de sockets per a la pràctica.

- **Opció 1: Herència de Thread:**
    
    - Cal declarar una subclasse de `Thread` i sobreescriure obligatòriament el mètode `run()`, que contindrà el codi que volem que s'executi concurrentment.
        
    - **Punt clau d'examen:** Per iniciar el fil, s'instancia la subclasse i es crida al mètode `start()`. Mai s'ha de cridar a `run()` directament, ja que llavors no es crearia un fil nou, sinó que s'executaria com un mètode normal.
        
    - Mètodes útils inclouen `sleep()` per pausar l'execució i `getName()` per identificar el fil.
![[Pasted image 20260225091551.png]]
- **Opció 2: Implementació de Runnable (Recomanat):**
    
    - Aquesta forma és més flexible perquè permet que la teva classe hereti d'una altra classe (com una classe base del teu projecte) mentre implementa el comportament de fil.
        
    - S'ha d'implementar el mètode `run()`.

    - Per engegar-lo, es crea un objecte `Thread` passant-li la teva classe `Runnable` com a argument al constructor: `new Thread(new LaTevaClasse()).start()`.
![[Pasted image 20260225091607.png]]
- **Comportament en execució:** En els exemples proporcionats ("Jamaica" i "Fiji"), es veu com els fils s'intercalen. Com que utilitzen un temps de "dormida" aleatori (`Math.random() * 1000`), l'ordre de sortida pel terminal no és predictible, demostrant la naturalesa no determinista de la concurrència.

---

# Tema 4 - Threads 2

## Problemes Fonamentals i Seguretat en la Concurrència

En l'àmbit de la programació multithread, ens enfrontem a tres tipus de problemes crítics que afecten la integritat del sistema:

#### Problemes

1. **Problemes de seguretat**: Hem de garantir que l'accés simultani a zones de memòria no corrompi les dades. La solució principal són les **regions d'exclusió mútua**, que eviten que diversos fils executin simultàniament instruccions que comprometin la integritat de la informació.

2. **Problemes d'esperes**: Es defineixen tres estats patològics:
    
    - **Deadlock**: Bloqueig mutu entre dos o més processos que s'esperen l'un a l'altre.
        
    - **Starvation**: Un procés no pot avançar mai perquè els recursos s'assignen de forma injusta a daltres.
        
    - **Livelock**: Els processos estan actius i realitzen còmput, però no són capaços de progressar cap als seus objectius.
        
3. **Problemes d'eficiència**: Cal maximitzar el còmput simultani real per aprofitar el maquinari.
    
4. **Extra - Condició de carrera (Race Condition)**: Passa quan el resultat final depèn de l'ordre d'execució dels fils. Un exemple típic és un comptador compartit:
    
    - Si dos fils llegeixen el valor "0" alhora , ambdós l'incrementen a "1" i el tornen a guardar , el resultat final serà "1" en lloc de "2".
	
    - Això demostra que la modificació de dades compartides, com un `count++`, ha de ser operació **sincronitzada**.

## 2. Sincronització en Java: Locks i Regions Crítiques

Java proporciona mecanismes natius per gestionar l'accés concurrent mitjançant el concepte de bloqueig o "lock":

 >[!info] **El concepte de Lock**: 
 >Cada objecte a Java té associat un lock únic que pot ser reclamat per qualsevol fil. Si un fil $t_1$ té el lock, qualsevol altre fil $t_2$ que el reclami quedarà bloquejat fins que $t_1$ el retorni.

- **Tipus de sincronització**:
    
    - **Implícita**: Es defineix un mètode amb la paraula clau `synchronized`. El fil obté el lock de l'objecte (`this`) automàticament abans d'executar el mètode.
	
    - **Explícita**: Es defineix un bloc `synchronized(objecte)` dins d'un mètode. Això permet bloquejar només una part específica del codi o bloquejar un objecte diferent a `this`.
![[Pasted image 20260225092218.png]]
- **Estratègies per sincronitzar un comptador (Exemple Servlet)**:
    
    - **Alternativa 1 (Mètode complet)**: Sincronitzar tot el mètode `doGet`. És segur però poc eficient, ja que bloqueja tot el servei per a cada petició.
    ![[Pasted image 20260225092239.png]]
    - **Alternativa 2 (Bloc synchronized)**: Sincronitzar només el bloc que incrementa i imprimeix. Millora lleugerament el control però encara manté el lock durant l'E/S (PrintWriter).
    ![[Pasted image 20260225092255.png]]
    - **Alternativa 3 (Secció crítica mínima)**: Sincronitzar només l'increment de la variable compartida i guardar-lo en una variable local (`local_count`). És la més eficient perquè el lock s'allibera immediatament després de la modificació, permetent que altres fils continuïn mentre s'imprimeix la resposta.
    ![[Pasted image 20260225092309.png]]

#### 3. Gestió del Deadlock i Cicle de Vida del Thread

Un dels errors més comuns i difícils de depurar és el bloqueig mutu o Deadlock:

- **Definició de Deadlock**: Situació on un conjunt de fils estan esperant esdeveniments (alliberament de recursos) que només poden ser causats per altres fils del mateix conjunt, generant una espera infinita.
    
- **Prevenció de Deadlocks**: Una estratègia clàssica és l'**ordenació de recursos**. Si tots els fils sol·liciten els recursos (locks) exactament en el mateix ordre, és impossible que es produeixi una espera circular.
![[Pasted image 20260225092500.png]]
- **Exemple de risc**: Si el fil $T_1$ agafa el lock de l'objecte 1 i després de l'objecte 2 , mentre que el fil $T_2$ agafa primer el de l'objecte 2 i després el de l'objecte 1, es pot produir un Deadlock si ambdós agafen el seu primer lock simultàniament.

- **Finalització de Threads**:
    
    - Els fils s'han d'acabar de manera **natural**, retornant del mètode `run()`.
        
    - **Regla d'or**: Un fil no pot finalitzar-ne un altre de manera forçada.
        
    - Per aturar un fil, se li ha d'enviar una **senyal d'interrupció**, i és el propi fil receptor qui ha de gestionar aquesta senyal i decidir acabar la seva execució.

## Coordinació de Threads: Wait, Notify i Join

Més enllà de l'exclusió mútua, els fils necessiten coordinar-se per col·laborar en tasques complexes:

- **Mecanisme wait/notify**: És un sistema d'esperes i notificacions vinculat a cada objecte.
    
    - **`wait()`**: Bloqueja el fil actual, allibera el lock i l'envia a una llista d'espera de l'objecte fins que algú el desperti o s'esgoti un timeout.
	![[Pasted image 20260225092644.png]]
    - **`notify()` / `notifyAll()`**: Desperta un (aleatori) o tots els fils que estan esperant en la llista de notificació d'aquell objecte.
	
    - **Condició d'ús**: Per fer un `wait` o `notify`, el fil **ha de tenir el lock** de l'objecte per evitar condicions de carrera en la pròpia llista de notificació.
        
    - **Aplicacions**: Útil per a cues bloquejants (esperar si la cua és buida), protocols productor-consumidor i per eliminar les costoses "esperes actives" (bucles que consumeixen CPU sense fer res).
        
- **Mètode `join()`**: S'utilitza quan un fil (per exemple, el pare) ha d'esperar que un altre fil acabi la seva feina abans de continuar. És comú en estructures on es llancen diversos "fills" i el pare recull els resultats al final.

- **API `java.util.concurrent`**: Java ofereix una biblioteca completa amb col·leccions concurrents i mecanismes avançats de planificació de tasques que faciliten la programació multithread moderna.

#### Exemple wait i notify
![[Pasted image 20260225092731.png]]

#### Exemple de join:
![[Pasted image 20260225092749.png]]


---

# Tema 5 -  Client/Servidor 2

# Paradigmes de Comunicació i Client-Servidor

L'arquitectura base que ens permet comunicar processos. Entendre això és fonamental abans de baixar al codi.

- El pas de missatges és el paradigma més bàsic per a les aplicacions distribuïdes.
    
- La dinàmica és simple: 
	1. un procés envia un missatge que representa una petició.
	2. aquest es lliura a un receptor que el processa i respon amb un altre missatge. 
	3. Aquesta resposta pot desencadenar noves sol·licituds successives.

>[!info] Rols
>- El model client-servidor es construeix sobre això assignant rols asimètrics a dos processos col·laboradors. 
>	- El servidor actua com a proveïdor i espera passivament l'arribada de les sol·licituds
>	- El client fa sol·licituds específiques i n'espera la resposta.
    
- Aquest model proporciona una abstracció eficient que simplifica la sincronització d'esdeveniments.

>[!tip] Operacions de cada integrant 
>- Les operacions del servidor inclouen escoltar i acceptar sol·licituds
> - Les del client, emetre peticions i rebre respostes.
>En resum: **Enviar/Rebre** i **Connexio/Desconexio**



- Tota aquesta comunicació en xarxa s'encapsula a nivell de sistema operatiu mitjançant operacions d'Entrada/Sortida similars a les de fitxers.
- Gran part dels serveis d'Internet com HTTP, FTP, o DNS funcionen com a aplicacions client-servidor.
    

---

# Conceptes i Tipus de Sockets

El socket és la nostra porta d'entrada i sortida cap a la xarxa. 

>[!tip] Pregunta segura d'examen
>Les diferències entre TCP i UDP a nivell d'API:.
>- **TCP (Streams):** Utilitza un model de **flux de bytes** (_Byte Stream_). L'API no manté els límits dels missatges. Si envies 100 bytes i després 100 més, el receptor pot llegir-ne 200 de cop.
>
>- **UDP (Datagrams):** Utilitza un model de **datagrames**. L'API manté els límits. Cada `send()` correspon exactament a un `recv()`. Si envies un paquet de 512 bytes, el receptor rep exactament aquest paquet o res.

- Un socket és el punt final d'un enllaç de comunicació entre dos processos que poden residir en diferents màquines.

- Els sistemes operatius suporten principalment tres tipus de sockets: Datagram (UDP), Stream (TCP) i Raw (ICMP).

## Tipus de Socket
### **Sockets Stream-mode (TCP):** 
Són orientats a la connexió. 

Proveeixen un flux de dades bidireccional, fiable, seqüencial i sense duplicació d'informació. 

>[!quote] Implementació 
>En Java s'usa la classe `ServerSocket` per acceptar connexions (creant el que anomenem un socket de connexió) i la classe `Socket` per a l'intercanvi de dades. 

El servidor utilitza sempre dos sockets: un per acceptar (que es manté escoltant) i un de nou que es crea per a l'enviament/recepció específica amb cada client. Al finalitzar, el servidor tanca el socket de dades però manté el de connexió.

- Mètodes crítics de l'API Stream: `accept()` bloqueja fins que hi ha connexió, i `setSoTimeout()` estableix un límit de temps de bloqueig generant una excepció `InterruptedIOException` si expira.
    
### **Sockets Datagram-mode (UDP):** 
No orientats a la connexió. 
Un socket Datagram proveeix un flux de missatges on no es garanteix ni seqüencialitat ni duplicació.

>[!quote] Implementació
>En Java utilitzen les classes `DatagramSocket` i `DatagramPacket`. 
>Amb ells, diversos processos poden enviar datagrames al mateix temps al mateix socket, fent que l'ordre d'arribada sigui impredictible. 

És molt important recordar que si el datagrama s'envia abans que el receptor hagi llançat l'operació de rebre, les dades seran descartades pel sistema.


### Sockets Raw mode (ICMP)
Permeten als processos comunicar-se utilitzant ICMP. 
- Normalment són orientats a datagrama. 
Només el root pot usar-los i serveixen per desenvolupar protocols

# Flux de connexións

## TCP
Entendre l'ordre d'execució entre client i servidor en un entorn TCP és fonamental per evitar bloquejos (deadlocks) en les teves aplicacions.

- La comunicació requereix una coreografia estricta on el servidor sempre ha d'estar preparat abans que el client actuï.

### **Cicle de vida del Servidor:**
    
1. Primer de tot, crea un socket de connexió (`ServerSocket`).
	- Es posa a escoltar peticions entrants (`Listen`).
	
	- Entra en un bucle infinit on accepta una connexió (`Accept`). Aquesta acció bloqueja l'execució fins que un client es connecta, moment en què crea un _nou_ socket de dades específic per a aquest client.
	
2. A partir d'aquest socket de dades, obté els fluxos per llegir (`InputStream`) i escriure (`OutputStream`).
	
	- Executa el protocol de l'aplicació en un bucle fins a acabar.
	
>[!warning] Obligatori: 
>Al finalitzar, tanca el socket de dades i, quan correspongui, el de connexió mitjançant un bloc `finally`.

### **Cicle de vida del Client:**
- Crea un socket de dades sol·licitant directament la connexió a la IP i port del servidor.
	
- Extreu els `InputStream` i `OutputStream` per poder comunicar-se.
	
- Realitza el protocol de comunicació.
	
- Finalment, tanca el socket de dades de forma neta.

### Mètodes Clau 

- **Mètodes clau `ServerSocket`:** El constructor `ServerSocket(int port)` crea el socket al port indicat. El mètode `accept()` és bloquejant, i el mètode `setSoTimeout(int timeout)` permet definir un temps màxim d'espera; si s'esgota, llança una `InterruptedIOException`.
    
- **Mètodes clau `Socket`:** El constructor `Socket(InetAddress address, int port)` s'encarrega de connectar-se al servidor. Disposa de `getInputStream()` i `getOutputStream()` per transferir la informació.
![[Pasted image 20260306181954.png]]

## UDP
Quan prioritzem la velocitat per sobre de la fiabilitat o enviem dades soltes, el paradigma canvia completament utilitzant el mode Datagram.

- En aquest model no hi ha establiment de connexió previ. La unitat bàsica és el datagrama.
    
- L'API de Java ens proporciona dues classes principals: `DatagramSocket` (per obrir el port) i `DatagramPacket` (l'envolcall que conté les dades, la IP i el port de destinació).
    
### **Cicle del Servidor (Receptor):**
- Crea un `DatagramSocket` i l'enllaça a un port local.
	
- Construeix un `DatagramPacket` amb un array de bytes buit que servirà de memòria intermèdia (buffer).
	
- Invoca el mètode `receive(DatagramPacket p)`, el qual bloqueja fins que arriba un paquet.
        
### **Cicle del Client (Emissor):**
    
- Crea el seu propi `DatagramSocket` i l'enllaça a qualsevol port local disponible.
	
- Prepara les dades en un array de bytes i crea un `DatagramPacket` especificant l'adreça i el port del servidor.
	
- Utilitza el mètode `send(DatagramPacket p)` per enviar-lo a la xarxa.
        
>[!warning] **Comportament crític a recordar:** 
>En ser sense connexió, diversos processos poden enviar datagrames simultàniament al mateix socket del servidor. 
>- A causa del protocol UDP, l'ordre d'arribada d'aquests missatges serà totalment impredictible. 
>- A més, si un client envia el datagrama abans que el servidor hagi llançat l'operació `receive`, aquestes dades seran descartades pel sistema operatiu i es perdran.


## Implementacio

#### 1. Gestió d'Enviaments Parcials (`InputStream`)

- **El problema:** El mètode `read(byte[] b)` bloqueja l'execució fins a rebre dades, però **no garanteix** llegir tots els bytes demanats d'una sola vegada. Només retorna els bytes llegits en aquell instant.
    
- **La solució:** Cal utilitzar un bucle `do-while` que vagi acumulant les lectures consecutives (`len += dis.read(...)`) fins que s'arribi al total de bytes esperats (`len < numBytes`).
    

#### 2. Tipus de Dades i _Endianness_

- **El problema:** Les dades primitives no es poden enviar de manera transparent. Un enter de 32 bits (4 bytes) s'ha de transmetre obligatòriament en format **BigEndian** (el byte més significatiu primer).
    
- **Codificació (Enter → Bytes):** S'utilitzen desplaçaments de bits (`>>`) combinats amb màscares (`& 0xFF`) per aïllar els bytes i assignar-los a l'array.
    
- **Descodificació (Bytes → Enter):** Es reverteix el procés aplicant desplaçaments a l'esquerra (`<<`) combinats amb operadors lògics OR (`|`) per reconstruir el nombre.
    

#### 3. Gestió de Cadenes de Caràcters (_Strings_)

Com que el canal de comunicació només entén bytes, s'han de definir regles clares per processar el text:

- **Mida Fixa:** Es converteix cada `char` a `byte`. Si el text original és més curt que la longitud fixada, l'espai sobrant s'ha d'omplir amb **espais en blanc**.
    
- **Mida Variable (Més robust):**
    
    - **Emissor:** Calcula la longitud exacta de la cadena. Construeix una **capçalera** de mida coneguda i fixa (ex. 4 bytes, omplint amb '0's al davant) que indica la longitud. S'envia primer aquesta capçalera i després els bytes del text.
        
    - **Receptor:** Llegeix exclusivament els bytes de la capçalera, en fa l'extracció (`Integer.parseInt`) per saber la longitud de la càrrega útil, i instancia el buffer final només per a la lectura d'aquell text.
---

# Arquitectures i Tipus de Servidors

Com dissenyem el cervell del servidor depenent del cas d'ús. Però tenim varies categoritzacions:
- Amb estat vs Sense estat
- Orientats a connexió vs No orientats
- Iteratius vs Concurrents.

## **Amb estat vs. Sense estat:** 

- Un servidor amb estat manté informació de l'estat de cada client actiu, la qual cosa pot reduir el temps de resposta i la quantitat de dades intercanviades. 
- No obstant, mantenir aquest estat és dificultós si hi ha errors a la xarxa. Codificar un servidor sense estat, per contra, és més senzill.

# Orientats a connexió vs No orientats
- Un servidor no orientat a connexió utilitza **Datagram-mode**
	- Les sessions amb clients simulltanis es poden intercalar

- Un servidor orientat a connexió utilitza **Stream-mode**
(Als pdf no posa més)
## **Concurrents vs. Iteratius:** 
- Un servidor concurrent fa servir diferents fils d'execució (o processos) per donar servei a diversos clients alhora, delegant la gestió del protocol a un fil fill per client. 
- Un servidor iteratiu només fa servir un sol fil d'execució, podent-ho fer de manera seqüencial o mitjançant operacions no-bloquejants.

#### **Gestió no-bloquejant amb Selectors:** 
- El principal problema dels servidors iteratius és la gestió d'operacions bloquejants com `accept` o `read`. 

>[!done] La solució 
>La llibreria NIO (Nonblocking InputOutput) de Java utilitzant un `Selector`. D'aquesta manera es crea un `ServerSocketChannel` configurat com a no bloquejant (`configureBlocking(false)`) i es registra al selector, permetent gestionar múltiples canals eficientment amb un únic fil.



---

# Comunicació Multicast

Com enviar missatges a múltiples destinataris de cop.

- Mentre l'Unicast s'encarrega d'enviar informació a un únic receptor (sigui per TCP o UDP), el Multicast permet l'enviament cap a múltiples receptors.
    
- Aquesta tecnologia només està disponible via UDP, pel que no hi ha garanties de recepció, i està construïda a sobre del protocol IP.
    
- Permet enviar un paquet IP a un conjunt de màquines que formen un grup. Aquests grups s'identifiquen amb adreces d'internet de Classe D, que van des de la 224.0.0.0 fins a la 239.255.255.255.
    
- Quan una màquina s'afegeix al grup rep tots els missatges; tanmateix, és possible enviar-hi paquets sense formar-ne part.
    

---
## Implementacio
#### 1. Gestió de Dades i Enviaments Parcials (Repàs)

- **Lectures incompletes:** L'API de lectura a baix nivell no garanteix omplir el buffer de cop. És imprescindible dissenyar **bucles `do-while`** per sumar els bytes rebuts fins a assolir la mida de càrrega útil esperada.
    
- **Codificació estricta:** Manteniment del rigor en les conversions: **BigEndian** per als enters i **capçaleres de mida** per delimitar les cadenes de text variables.
    

#### 2. Gestió d'Excepcions

La resiliència del codi depèn d'un tractament granular dels errors. Cal utilitzar blocs `try-catch` específics per a cada cas:

- **`IOException` (_Broken pipe_):** Indica que l'escriptura ha fallat perquè l'extrem remot de la connexió s'ha desconnectat bruscament.
    
- **`SocketException`:** L'error es troba en el _socket_ local (ha estat tancat manualment, no s'hi té accés o no s'ha pogut instanciar).
    
- **`InterruptedIOException`:** S'ha esgotat el temps d'espera màxim definit per a una operació (ha saltat el _Timeout_).
    
- **`ProtocolException`:** S'han detectat anomalies o problemes directament a la capa TCP.
    

#### 3. Cicle de Vida: _Timeouts_, _Threads_ i _Sockets_

La gestió de la memòria i els recursos de xarxa ha de ser impecable per evitar fuites (_leaks_) o bloquejos (_deadlocks_):

- **Tancament innegociable:** S'ha d'utilitzar sempre l'estructura `finally` per invocar el tancament dels _sockets_. Això garanteix l'alliberament del recurs tant si l'operació té èxit com si falla.
    
- **Temporitzadors (_Timeouts_):** Cap operació de lectura (`read`) s'ha de fer a cegues. Tot _socket_ receptor ha de tenir un _timeout_ configurat amb un llindar de temps equilibrat per detectar caigudes de connexió sense asfixiar la xarxa.
    
- **Tractament de l'espera natural:** Si l'arquitectura del programa preveu que el client trigui a respondre i s'esgota el _timeout_, la interrupció no ha de ser fatal. Cal verificar si l'embut d'entrada té dades latents (mitjançant `available()`) per reprendre la lectura si és procedent.
    
- **Finalització neta de Fils (_Threads_):** Els fils d'execució han d'assolir la seva finalització de manera orgànica i natural, garantint el tancament de tots els _sockets_ associats abans de destruir-se.

---

# Tema 6 - Web HTTP


### **Funcionament WWW:** 
La WWW és una aplicació **client-servidor orientada a la connexió** que es basa íntegrament en l'HyperText Transfer Protocol (HTTP).
- Per defecte, els servidors web corren sobre el port 80. 
- L'usuari sol·licita un document mitjançant el navegador i, si aquest es troba al servidor, el contingut és retornat i presentat a l'usuari.

#### **Els Tres Elements Clau (URL, HTTP, HTML):** 
El sistema web combina tres peces clau per funcionar:
- l'URL per localitzar
- l'HTTP per transmetre
- l'HTML per estructurar.

##### **URL (Uniform Resource Locator) o URI:** 
Constitueix el sistema de noms i adreces. Identifica recursos a la web (documents, imatges o serveis) i permet el seu accés sota mètodes com HTTP o FTP. L'esquema d'una URI és: `protocol://username:passwd@hostname:port/path/subdirs/resource?param1=value1&param2=value2`.
    
##### **HTML (HyperText Markup Language):**
És el llenguatge de marcatge utilitzat per crear documents per a la WWW. Es basa en el format SGML, amb semàntiques dissenyades per representar diversos tipus d'informació, i està formalment definit pel W3C (tot i que molts navegadors són permissius a l'hora de llegir-lo).
![[Pasted image 20260314105644.png]]

---

## 2. El Protocol HTTP: Fonaments i Trames

### **Característiques de l'HTTP:**
L'HTTP és un protocol:
	- orientat a la connexió
	- sense estat
	- d'anada i tornada (petició-resposta). 

   
### **Estructura de les Trames HTTP:**
L'HTTP és un protocol basat en text. Tant les peticions (request) com les respostes (response) segueixen un ordre estricte: 
1. Línia inicial (request/response)
2. Secció de capçalera
3. Línia en blanc 
4. el Cos (Entity Body).

#### Linia Request
S'envia un cop el client estableix la connexió, amb la forma:
`<HTTP method> <Request-URI> <protocol specification>\r\n`. 
![[Pasted image 20260314110035.png]]

Els mètodes principals són:
1. `GET` (segur i idempotent, per recuperar contingut)
2. `HEAD` (segur i idempotent, recupera només la capçalera)
3. `POST` (no segur ni idempotent, per enviar dades a un procés del servidor)
4. `PUT` (per emmagatzemar contingut a la URI especificada).

>[!tip] Què fan?
>- GET: per a recuperar el contingut de l’objecte web al que fa
referència la URI especificada.
>- HEAD: per a recuperar tan sols la capçalera d’un objecte web
des del servidor, no el propi objecte.
> - POST: utilitzat per a enviar dades a un procés del servidor web.
> + PUT: s’utilitza per demanar al servidor emmagatzemar el
contingut que s’adjunta amb la petició, a la ubicació del fitxer
especificat per la URI en el servidor.


- **Capçaleres i Cos del Client:** Les capçaleres afegeixen informació d'interès com:
- l'entorn de l'usuari, navegador(`User-Agent`), 
- els tipus de dades acceptades, pel client (`Accept`) 
- si es desitja mantenir la connexió oberta, després de fer un request (`Connection: "Keep-Alive"`).
- El nom del amfitrió (`Host`)
- i més

El cos del request, opcional, conté les dades a transferir, com quan s'usa el mètode `POST`.

#### **La Resposta HTTP (Response):**
Es  compon per:
1. Línia de resposta (estat)
2. Secció de capçalera
3. Un espai en blanc 
4. el Cos (Entity Body).

La línia de resposta té la forma:
`<protocol> <status-code> <description>\r\n`. 

Els codis d'estat es divideixen en:
- 100-199 (Informatiu), 
- 200-299 (Èxit), 
- 300-399 (Redirecció), 
- 400-499 (Error de petició, no acomplerta) 
- 500-599 (Error intern del servidor). 

La resposta també inclou capçaleres (com `Content-Type`) i el cos, que conté l'objecte Web demanat.

Hi ha dos tipus de lı́nies de capçalera de resposta:
- de resposta: Retorna informació sobre la resposta, el servidor o successius accessos al recurs sol·licitat
	- Refresh, Retry-After, Server, Set-Cookie ...
- de l’entitat: Retorna informació sobre els continguts del recurs sol·licitat pel client.
	- Content-Type, Content-Length, Content-Encoding, Content-Language ..

---

## 3. Aplicacions Web i Contingut Dinàmic

### **Necessitat de Contingut Dinàmic:** 

Originàriament, l'HTTP només transferia continguts estàtics (textes, imatges). 
- Amb l'evolució web, es va fer necessari que els usuaris poguessin recuperar dades basant-se en informació dinàmica introduïda durant la sessió.
    
>[!warning] **Limitacions del Servidor Web Pur:** 
>Un servidor HTTP genèric manca de la lògica d'aplicació necessària per buscar dades dinàmiques en un model de dades.
    
#### **L'Intermediari (Scripting Engine):**
Per resoldre això, s'utilitza un **procés extern** a la màquina del servidor que fa d'intermediari i conté la lògica d'aplicació. 
- Aquest procés accepta les dades d'entrada des del servidor web, executa la lògica per obtenir dades, i retorna el resultat al servidor web perquè aquest últim el transmeti al client.

- **Mecanisme d'Execució:** El procediment clàssic per invocar aquests programes web des de la part del client és a través del camp `ACTION` dins d'un formulari HTML, que enllaça directament amb l'script (com ara un fitxer .php o .cgi).
![[Pasted image 20260314113446.png]]


---

## 4. Formularis Web i Gestió de Dades (Query Data)

- **Definició de Formularis:** Els formularis s'encabeixen entre les etiquetes `<FORM>...</FORM>`. 
	- L'atribut `ACTION` defineix la URL absoluta o relativa on aniran destinades les dades. 
	- L'atribut `METHOD` especifica la forma en què s'enviaran aquestes dades (típicament GET o POST). 
Finalment, es requereix un element d'entrada del tipus "submit" (botó) per emetre la petició HTTP.


### **Query Data (Dades de Consulta):**
Són les dades introduïdes per l'usuari als elements del formulari (identificats pel seu atribut `name`). 

- Aquestes dades es codifiquen en una "Query String", que és una seqüència de parells `name=value` separats per `&`. El navegador transforma els caràcters reservats en ASCII hexadecimal mitjançant codificació URL.
    
#### Enviaments

##### **L'Enviament amb GET:** 
Si s'usa GET, la Query Data s'afegeix directament al final de la URL del request, precedida pel caràcter `?`. 
- Degut a què la longitud de la línia de request és limitada en l'HTTP, aquest mètode no és adequat per enviar grans volums de dades.

#####  **L'Enviament amb POST:**
Si s'usa POST, la URL queda inalterada i la Query Data s'envia oculta a l'interior del cos (body) de la petició HTTP.
    
##### **Patró POST-Redirect-GET:** 

>[!warning] Important
>Serveix per evitar que el navegador mostri el molest avís de "reenviament de dades" quan un usuari refresca una pàgina després d'un POST.

El patró consisteix en enviar dades amb POST, actualitzar-les al servidor, retornar un codi de redirecció (3xx) cap a una nova URL, i finalment fer que el navegador faci un GET cap a aquesta adreça de resultat.

![[Pasted image 20260314114909.png]]
