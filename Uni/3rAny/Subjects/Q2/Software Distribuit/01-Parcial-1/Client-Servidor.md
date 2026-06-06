# Pas de missatges
El pas de missatges és el paradigma més bàsic per a les aplicacions
distribuïdes:

1. Un procés envia un missatge que representa una petició.
2. El missatge es lliura a un receptor, que processa la sol.licitud, i envia un missatge en resposta.
3. Al seu torn, la resposta pot desencadenar una nova sol.licitud, la qual condueix a una resposta posterior, i aixı́ successivament.

# Model Client-servidor
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

Per comunicacions orientades a la connexió, les operacions de:
- connexió 
- desconnexió 
també es requereixen.

>[!tip] Similitud
Amb  aquest model, els processos interconnectats realitzen operacions d’entrada/sortida d’una manera similar a E/S amb fitxers. 


# API de Sockets i Tipologies

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


# Stream mode i Gestió de Dades

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


# 4 Topologia de Servidors i Datagram-Mode

![[Pasted image 20260220200038.png]]
![[Pasted image 20260220200154.png]]
>[!tip] Java
>En Java, l’API de sockets Datagram-mode proveix dues classes:
>- DatagramSocket: per als sockets.
>- DatagramPacket: per intercanviar datagrames.
>
Un procés que vulgui enviar o rebre dades fent servir aquesta API ha de crear una instància d’un objecte DatagramSocket. Cada socket està enllaçat a un port UDP de l’equip local.

## Sockets

### No orientats a connexió
Amb sockets sense connexió, és possible que diversos processos
enviïn simultàniament datagrames al mateix socket establert per un
procès de recepció.
	- En aquest cas l’ordre de l’arribada d’aquests missatges serà impredictible, d’acord amb el protocol UDP

## Servers
Els servidors es poden classificar segons diversos criteris de disseny:

- **Amb estat vs. Sense estat:** Un servidor **amb estat** manté informació de cada client, cosa que pot millorar el temps de resposta però dificulta la recuperació davant d'errors (si el client cau, l'estat queda inconsistent). Els servidors **sense estat** són més senzills de codificar i mantenir.
![[Pasted image 20260220201647.png]]

- **Orietats i no Orientats a Connexió**: No orientats a la connexió Utilitza API Datagram-mode. 
	- Les sessions amb clients simultanis es poden intercalar.
Orientat a la connexió Utilitza API Stream-mode.

- **Iteratius vs. Concurrents:** L'iteratiu només serveix un client a la vegada, mentre que el concurrent permet múltiples sessions simultànies.

## Datagrames
En el **Datagram-Mode (UDP)**, la comunicació no és orientada a la connexió. 

- No hi ha un `accept()`; el servidor simplement rep paquets (`DatagramPacket`) a través d'un `DatagramSocket`. 
- Un detall vital per a l'examen: si un datagrama s'envia abans que el receptor hagi llançat l'operació de rebre, les dades es descarten i es perden per sempre. 
A més, amb UDP l'ordre d'arribada és totalment impredictible si diversos processos envien dades simultàniament al mateix socket.


# Concurrència, Selectors i Multicast

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
	- IP Multicast
		- Aquest mecanisme es construeix directament sobre l'Internet Protocol (IP), operant en les capes baixes del model de xarxa.
	    
		- La seva funció principal és permetre l'enviament d'un paquet IP a un conjunt determinat de màquines que s'han organitzat en un grup.
	    
		- És important destacar que només està disponible a través d'UDP; no existeix una versió de Multicast amb les garanties de TCP.
	    
		- A causa de la seva naturalesa UDP, no ofereix cap garantia que el paquet arribi a tots els destinataris o que ho faci en l'ordre correcte.
	    
	
	- **Grup Multicast**
		- Un grup multicast es diferencia d'un procés individual per la seva adreça d'Internet de la Classe D, compresa entre la 224.0.0.0 i la 239.255.255.255.
		   	 
		- El funcionament és dinàmic: quan una màquina s'afegeix formalment a un grup, el seu sistema operatiu comença a acceptar i processar tots els missatges enviats a aquella adreça.
		   	 
		- Existeix una asimetria interessant: un procés pot enviar paquets a un grup multicast sense necessitat de ser-ne membre.
		   	 
		- Per a proves en xarxes locals, s'utilitza habitualment l'adreça reservada 224.0.0.1, que identifica totes les màquines de la subxarxa local.