Aquest resum és un recull de la teoria que sol preguntar en el primer parcial. Per tant tot està enfocat als diferents exercicis que ell planteja.
- [[#Model OSI]]
	- [[#Capa d'Aplicació (Capa 7)|Capa d'Aplicació (Capa 7)]]
			- [[#Protocols comuns|Protocols comuns]]
	- [[#Capa Presentació (Capa 6)|Capa Presentació (Capa 6)]]
	- [[#Capa de Sessió (Capa 5)|Capa de Sessió (Capa 5)]]
			- [[#Protocols comuns|Protocols comuns]]
	- [[#Capa de Transport (Capa 4)|Capa de Transport (Capa 4)]]
			- [[#Protocols comuns|Protocols comuns]]
	- [[#Capa de Xarxa (Capa 3)|Capa de Xarxa (Capa 3)]]
			- [[#Protocols comuns|Protocols comuns]]
	- [[#Capa d'Enllaç (Capa 2)|Capa d'Enllaç (Capa 2)]]
			- [[#Hardware i Protocols comuns|Hardware i Protocols comuns]]
	- [[#Capa Física (Capa 1)|Capa Física (Capa 1)]]
			- [[#Hardware comú|Hardware comú]]
	- [[#Diferència entre la Capa Xarxa I Transport|Diferència entre la Capa Xarxa I Transport]]
		- [[#Diferència entre la Capa Xarxa I Transport#1. L'Analogia de l'Edifici d'Oficines|1. L'Analogia de l'Edifici d'Oficines]]
		- [[#Diferència entre la Capa Xarxa I Transport#2. L'Explicació Tècnica|2. L'Explicació Tècnica]]
		- [[#Diferència entre la Capa Xarxa I Transport#En resum|En resum]]
- [[#Model TCP/IP (Arquitectura d'Internet)]]
	- [[#1. Capa d'Aplicació|1. Capa d'Aplicació]]
	- [[#2. Capa de Transport (Host-to-Host)|2. Capa de Transport (Host-to-Host)]]
	- [[#3. Capa d'Internet (Xarxa)|3. Capa d'Internet (Xarxa)]]
	- [[#4. Capa d'Accés a la Xarxa|4. Capa d'Accés a la Xarxa]]
- [[#Flux de Dades El Procés d'Encapsulament]]
	- [[#1. L'Origen: Capa d'Aplicació (Layer 7)|1. L'Origen: Capa d'Aplicació (Layer 7)]]
	- [[#2. Preparació: Capa de Transport (Layer 4)|2. Preparació: Capa de Transport (Layer 4)]]
	- [[#3. L'Encaminament: Capa de Xarxa (Layer 3)|3. L'Encaminament: Capa de Xarxa (Layer 3)]]
	- [[#4. El Tram Local: Capa d'Enllaç (Layer 2)|4. El Tram Local: Capa d'Enllaç (Layer 2)]]
	- [[#5. La Transmissió: Capa Física (Layer 1)|5. La Transmissió: Capa Física (Layer 1)]]
- [[#PROBLEMES]]
	- [[#CRC]]
		- [[#Càlcul del CRC: Pas a pas|Càlcul del CRC: Pas a pas]]
			- [[#Càlcul del CRC: Pas a pas#1. Traducció del Polinomi Generador|1. Traducció del Polinomi Generador]]
			- [[#Càlcul del CRC: Pas a pas#2. Preparació de la Trama (Padding)|2. Preparació de la Trama (Padding)]]
			- [[#Càlcul del CRC: Pas a pas#3. Divisió Binària (XOR)|3. Divisió Binària (XOR)]]
			- [[#Càlcul del CRC: Pas a pas#Resultat Final|Resultat Final]]
	- [[#Transmissió de Senyal i Capacitat de Canal]]
		- [[#1. Conceptes Fonamentals i Fórmules|1. Conceptes Fonamentals i Fórmules]]
			- [[#1. Conceptes Fonamentals i Fórmules#A. Teorema de Shannon-Hartley|A. Teorema de Shannon-Hartley]]
			- [[#1. Conceptes Fonamentals i Fórmules#B. Relació Senyal-Soroll (SNR)|B. Relació Senyal-Soroll (SNR)]]
			- [[#1. Conceptes Fonamentals i Fórmules#C. Model de Propagació en l'Espai Lliure (Llei de Friis)|C. Model de Propagació en l'Espai Lliure (Llei de Friis)]]
		- [[#2. Resolució de l'Exercici de Laboratori|2. Resolució de l'Exercici de Laboratori]]
			- [[#2. Resolució de l'Exercici de Laboratori#1. Determinació de la velocitat (Shannon)|1. Determinació de la velocitat (Shannon)]]
			- [[#2. Resolució de l'Exercici de Laboratori#2. Codificació i Velocitat Final|2. Codificació i Velocitat Final]]
			- [[#2. Resolució de l'Exercici de Laboratori#3. Potència de Soroll ($N$)|3. Potència de Soroll ($N$)]]
			- [[#2. Resolució de l'Exercici de Laboratori#4. Distància màxima (sense considerar soroll)|4. Distància màxima (sense considerar soroll)]]
			- [[#2. Resolució de l'Exercici de Laboratori#5. Distància màxima (considerant soroll)|5. Distància màxima (considerant soroll)]]
		- [[#Resolució mecànica|Resolució mecànica]]
			- [[#Resolució mecànica#1. Capacitat de Shannon (Velocitat Teòrica)|1. Capacitat de Shannon (Velocitat Teòrica)]]
			- [[#Resolució mecànica#2. Codificació i Velocitat Real|2. Codificació i Velocitat Real]]
			- [[#Resolució mecànica#3. Potència de Soroll ($N$)|3. Potència de Soroll ($N$)]]
			- [[#Resolució mecànica#4. Distància Màxima (Espai Lliure)|4. Distància Màxima (Espai Lliure)]]
			- [[#Resolució mecànica#5. Distància amb Soroll|5. Distància amb Soroll]]





# Model OSI

És un model de referència per establir bases normatives per tal d'evitar els  sistemes propietaris


>[!abstract] Definició 
>És una normativa que descriu com les dades i la informació de xarxa s'han de moure des de l'aplicació d'un ordinador fins a l'aplicació d'un altre ordinador a través d'un mitjà físic.


- Aquest Model es divideix en **7 Capes** diferenciades.
	Sent la superior la més propera al usuari i la inferior la menys
- Cada capa és totalment independent en implementació i ofereix serveis a la capa superior.

Les diferents capes són:
1. [[#Capa d'Aplicació (Capa 7)]]
2. [[#Capa Presentació (Capa 6)]]
3. [[#Capa de Sessió (Capa 5)]]
4. [[#Capa de Transport (Capa 4)]]
5. [[#Capa d'Entorn de Xarxa (Capa 3)]]
6. [[#Capa d'Enllaç (Capa 2)]]
7. [[#Capa Física (Capa 1)]]


---
## Capa d'Aplicació (Capa 7)

>[!summary] Resum
>- Interfíce entre l'aplicació i la xarxa
>	--> NO és l'aplicació en si
>
>- Defineix Els protocols per a l'intercanvi de dades
>	--> Del significat de les coses , no de moure els bits
>
>- Utilitza estandaritzacions com el HTTPS


Interfície responsable de la comunicació entre el programari de l'usuari final (webs, clients de correu, ...) i la xarxa amb la que es comuniquen.

>[!info] Ojo
>No és l'aplicació en si, són els protocols i interrfícies que les aplicacions utilitzen

Defineix _Protocols_ per a l'intercanvi de dades i traca aspectes de semàntica (significat d'informació)

- **Semàntica (Capa d'Aplicació):** Tracta sobre el **significat** i la interpretació de les comandes i les dades.
	- _Exemple:_ 
		Quan envies un "GET" en HTTP, la capa d'aplicació entén que "vol dir" que demanes un recurs.

- **Sintaxi (Capa de Presentació):** Tracta sobre la **forma**, la codificació i la representació.
	- _Exemple:_
		Si les dades estan en ASCII o EBCDIC, o si estan xifrades/comprimides. 
		- La capa de presentació s'assegura que la sintaxi sigui comprensible, però no n'interpreta el significat profund (això ho fa l'aplicació).

#### Protocols comuns
- HTTP/HTTPS - Per a navegadors web
- SMTP - Per intercanvi i gestió de correus electrònics
- FTP - Per la transferenica de fitxers
- Telnet/SSH - Per al accès remot als terminals
- DNS - Resolució/traducció noms de domini

>[!tip] Curiositat
>La capa aplicació, normalment se li fa accès mitjançant sockets, 

- L'aplicació (espai d'usuari) utilitza la _Socket Interface_ per comunicar-se amb el _Kernel_ (on resideix la pila de protocols TCP/IP).

- Un socket permet a l'aplicació enviar i rebre dades com si escrivís o llegís en un fitxer, abstraient-se de la complexitat de les capes inferiors .


>[!example] Visió de Laboratori: 
> Payloads i APIs (Pràctica 4 IoT)

- **Format de Dades:** La xarxa transporta bits, però l'aplicació necessita estructura. A la pràctica IoT, vam usar **JSON** (`{"field1": 25}`) per enviar dades a ThingSpeak. Això és purament Capa 7.


- **Client-Servidor:** L'ESP8266 actuant com a client HTTP (enviant un `POST`) o com a petit servidor Web. La teoria diu "petició-resposta"; la pràctica és enviar un string de text que comença per `GET / HTTP/1.1` i esperar un string de tornada `HTTP/1.1 200 OK`.




---
## Capa Presentació (Capa 6)

> [!summary] Resum
> 
> - Es centra en la **Sintaxi** i la representació 
> 	--> La forma de les dades, no el significat
>     
> - Garanteix la **llegibilitat** entre sistemes heterogenis
> 	--> Que un Linux pugui entendre un fitxer enviat des d'un Windows
>     
> - Ofereix serveis de **Traducció**, **Xifratge** i **Compressió**
>    

Aquesta capa s'encarrega de garantir que la informació que envia la capa d'aplicació d'un sistema sigui llegible per la capa d'aplicació d'un altre. Actua com a **traductor** de la xarxa.

> [!info] Ojo 
> Proporciona independència respecte a la representació interna de les dades (com es guarden els bits a la memòria de cada màquina).

Les seves funcions principals són:

- **Traducció de codis:** Adapta la codificació de caràcters o números.
    
    - _Exemple:_ Convertir d'ASCII a EBCDIC, o gestionar problemes de _Little-endian_ vs _Big-endian_.


- **Criptografia (Xifrat i Desxifrat):** Protegeix la informació perquè no pugui ser llegida per tercers no autoritzats.


- **Compressió de dades:** Redueix el nombre de bits necessaris per transmetre la informació, optimitzant l'amplada de banda.

---
## Capa de Sessió (Capa 5)

> [!summary] Resum
> 
> - Estableix, gestiona i tanca les **connexions** (sessions) 
> 	 --> Entre aplicacions locals i remotes
>     
> - Controla el **Diàleg** 
> 	--> Qui parla i quan (Simplex, Half-Duplex, Full-Duplex)
>     
> - Afegeix mecanismes de **Sincronització** 
> 	--> Punts de control per no haver de reiniciar des de zero si falla
>     

Aquesta capa permet que usuaris de diferents màquines estableixin sessions entre ells. Ofereix diversos serveis crucials per organitzar la comunicació, més enllà de simplement moure dades.

> [!info] Ojo 
> No es tracta només d'enviar paquets (això és més a baix), sinó de gestionar **la conversa** entre les aplicacions.

Funcions principals:

- **Control de Diàleg:** Determina el torn de paraula.
    
    - _Exemple:_ Pot forçar que la comunicació sigui **Half-Duplex** (com un walkie-talkie, un parla i l'altre escolta) o permetre **Full-Duplex** (com un telèfon, els dos parlen alhora).
        
- **Sincronització (Token Management):** Permet inserir punts de verificació (_checkpoints_) dins del flux de dades.
    
    - _Exemple:_ Si estàs transferint un fitxer de 100 MB i la xarxa cau al MB 95, gràcies a la capa de sessió pots reprendre la transferència des de l'últim punt de control (per exemple, el MB 90) en lloc de tornar a començar des del principi.
        

#### Protocols comuns

- RPC (Remote Procedure Call)
   
- NetBIOS

- SQL (gestió de sessions amb bases de dades)


---
## Capa de Transport (Capa 4)

> [!summary] Resum
> 
> - Comunicació **Extrem a Extrem** (_End-to-End_) 
> 	--> Connexió lògica entre processos, no només màquines
>     
> - **Segmentació** i Reassemblatge 
> 	--> Trosseja les dades de sessió en paquets més petits (segments)
>     
> - **Multiplexació** de serveis
> 	--> Utilitza **Ports** per saber a quina aplicació van les dades
>     

Aquesta capa és la responsable de lliurar les dades al procés d'aplicació correcte dins de l'ordinador de destí. És la frontera entre les capes orientades a l'aplicació (superiors) i les capes orientades a la transmissió de dades (inferiors).

> [!info] Ojo 
> Mentre que la capa de Xarxa envia paquets d'un ordinador a un altre, la capa de Transport els envia **d'un procés (programa) a un altre**, utilitzant **ports**.

Per aprofundir: [[#Diferència entre la Capa Xarxa I Transport]]


Funcions principals:

- **Segmentació:** Divideix les dades rebudes de la capa de Sessió en unitats més petites anomenades _Segments_ per facilitar-ne la transmissió. A la recepció, els torna a unir.
    
- **Control de Flux i Errors (en protocols fiables):** Assegura que les dades arribin sense errors, en ordre i sense saturar el receptor.
    
    - _Mecanismes:_ ACKs (confirmacions de recepció), finestres lliscants.
    
- **Multiplexació/Demultiplexació:** Permet que múltiples aplicacions (navegador, email, spotify) utilitzin la xarxa simultàniament distingint-les pel número de **Port**.
    

#### Protocols comuns

- **TCP (Transmission Control Protocol):** Fiable, orientat a connexió. Garanteix que les dades arriben i en ordre. (Ex: Web, Email).

- **UDP (User Datagram Protocol):** No fiable, sense connexió. Més ràpid, però pot perdre paquets. (Ex: Streaming, Jocs online, DNS).

>[!example] Visió de Laboratori: 
>Sockets (Pràctica 4) La Capa de Transport a nivell de programació és un **Socket**.

- **La tupla de connexió:** Quan programes un xat en Python/C, defineixes `(IP Destí, Port Destí)`. Això _és_ la capa de transport.
    
- **TCP vs UDP al codi:**
    
    - `SOCK_STREAM` = TCP (Connexió fiable, Handshake, com vam veure al codi del Xat).
        
    - `SOCK_DGRAM` = UDP (Enviar i oblidar, sense `connect`).
        
- **Three-Way Handshake:** Al Wireshark (P5) es veu físicament l'intercanvi `SYN` -> `SYN-ACK` -> `ACK` abans de poder enviar cap dada del xat. Això confirma que la connexió s'ha establert abans de fer l'`accept()` al codi.



---

## Capa de Xarxa (Capa 3)

> [!summary] Resum
> 
> - Proporciona **Adreçament Lògic** (IP) 
> 	--> Identifica màquines en xarxes diferents (Internet)
>     
> - Realitza l'**Encaminament** (_Routing_) 
> 	--> Troba el millor camí per arribar al destí
>     
> - Connecta xarxes heterogènies 
> 	--> Permet que una xarxa Ethernet parli amb una xarxa Wi-Fi o Fibra
>     

Aquesta capa és la responsable de permetre la comunicació entre dispositius que **no** estan connectats directament al mateix cable o xarxa local. És la capa que fa possible "Internet" (Inter-Networking).

> [!info] Ojo 
> Mentre la Capa 2 utilitza adreces físiques (MAC) que són planes i locals, la Capa 3 utilitza adreces lògiques (IP) que són **jeràrquiques** i permeten l'encaminament global.

Funcions principals:

- **Adreçament Lògic:** Assigna una adreça IP única a cada dispositiu.
    
    - A diferència de la MAC (que va gravada al hardware), la IP es pot canviar segons on et connectis.
    
    - _Analogia:_ És com l'adreça postal (Carrer, Ciutat, País).
    
- **Encaminament (_Routing_):** Els dispositius anomenats **Routers** operen en aquesta capa. Decideixen per quin cable han d'enviar el paquet perquè arribi al seu destí final.
    
    - Utilitzen taules d'encaminament i protocols dinàmics per evitar congestions o talls de xarxa.
    
- **Fragmentació i Reassemblatge:** Si un paquet és massa gran per passar per un tipus de xarxa concret (MTU), la capa de xarxa el pot dividir en trossos més petits i tornar-los a muntar al destí (encara que es tracta d'evitar).


#### Protocols comuns

- **IPv4 / IPv6:** El protocol estàndard d'Internet.

- **ICMP:** Protocol de control i missatges d'error (utilitzat pel `ping`).

- **OSPF / BGP:** Protocols que utilitzen els routers per "parlar" entre ells i decidir les rutes.

- **IPsec:** Per a seguretat a nivell de xarxa (VPNs).

>[!example] Visió de Laboratori:
> Configuració i NAT (Pràctica 3) A la teoria, els routers "envien paquets". A la pràctica (Packet Tracer/Cisco IOS), això implica:

- **Interfícies:** Un router no funciona si no li assignes una IP i una Màscara a cada "pota" (`int fa0/0`, `ip address ...`).
    
- **NAT (Network Address Translation):** A la teoria parlem d'IPs úniques. A la realitat, els equips del laboratori tenen IPs Privades (192.168.x.x) que no poden navegar. El NAT (configurat al Router) "enganya" a Internet substituint la teva IP privada per la Pública del router.
    
- **DHCP:** És el mecanisme (Layer 7 que configura Layer 3) que automàticament et dóna IP, Màscara i Gateway (`default-router`). Sense això, hauries de posar la IP a mà a cada PC.



---

## Capa d'Enllaç (Capa 2)

> [!summary] Resum
> 
> - Comunicació **Node a Node** (salt a salt) 
> 	--> Entre dispositius connectats al mateix mitjà físic
>     
> - Utilitza **Adreces Físiques** (MAC) 
> 	--> Identificadors únics gravats al maquinari
>     
> - Organitza els bits en **Trames** (_Frames_)
> 	--> Afegeix capçalera i cua per detectar on comença i acaba el missatge
>     

Aquesta capa és la responsable de la transferència fiable d'informació a través d'un circuit de transmissió de dades. Agafa els bits "crus" de la capa física i els estructura perquè tinguin sentit.

> [!info] Ojo 
> Mentre la Capa 3 connecta xarxes diferents (Internet), la Capa 2 connecta dispositius dins de la **mateixa xarxa local** (LAN).

Funcions principals:

- **Emmarcat (_Framing_):** Agrupa els bits rebuts de la capa física en unitats lògiques anomenades _Trames_.
    
- **Adreçament Físic (MAC):** Utilitza l'adreça MAC (Media Access Control) per identificar l'emissor i el receptor dins del segment de xarxa local.
    
    - _Format:_ 48 bits, hexadecimal (ex: `00:1A:2B:3C:4D:5E`).
    
- **Control d'Accés al Mitjà:** Defineix qui pot utilitzar el cable (o l'aire en Wi-Fi) en cada moment per evitar col·lisions.
    
    - _Exemple:_ CSMA/CD en Ethernet (escoltar abans de parlar).
    
- **Detecció d'Errors:** Afegeix un codi al final de la trama (FCS/CRC) per comprovar si algun bit s'ha corromput pel camí (per soroll elèctric, etc.). Si està malament, la trama es descarta.


#### Hardware i Protocols comuns

- **Switch (Commutador):** És el dispositiu rei d'aquesta capa. Aprèn les adreces MAC dels equips connectats i envia les trames només al destinatari correcte (a diferència del Hub).

- **Ethernet (IEEE 802.3):** L'estàndard cablejat més comú.

- **Wi-Fi (IEEE 802.11):** L'estàndard sense fils (també té capa d'enllaç, tot i que l'accés al mitjà és més complex).

- **ARP (Address Resolution Protocol):** El pont entre Capa 2 i Capa 3. Pregunta: "Qui té la IP X?" i algú respon "Jo, i tinc la MAC Y".

>[!example] Visió de Laboratori: 
>Anàlisi de Trames (Pràctica 5) Quan captures trànsit amb **Wireshark**, la Capa 2 és la capçalera Ethernet II.

- **Adreçament:** Aquí veus la `Source MAC` i `Destination MAC` reals (6 bytes hexadecimals).
    
- **Encapsulament:** El camp `Type` (ex: 0x0800) és vital: li diu a la targeta de xarxa "el que hi ha a dins és un paquet IPv4". Sense això, la capa 2 no sabria a qui passar-li les dades a la capa 3.
    
- **Promiscuous Mode:** Perquè Wireshark vegi paquets que no són per a tu, la targeta s'ha de posar en mode promiscu (ignorant el filtre de MAC de destí del hardware).




---

## Capa Física (Capa 1)

> [!summary] Resum
> 
> - Transmissió de **Bits purs**
> 	--> Flux no estructurat de dades (0s i 1s) a través del mitjà
>     
> - Defineix especificacions **Elèctriques, Mecàniques i Funcionals** 
> 	--> Voltatges, tipus de cables, formes dels connectors, pins
>     
> - És tot **Hardware** 
> 	--> Aquí parlem de física, no de lògica
>     

És la capa més baixa del model OSI. S'encarrega de la transmissió i recepció de la seqüència de bits sense format a través d'un mitjà físic.

> [!info] Ojo 
> Aquesta capa **no entén res**. No sap què és una adreça IP, ni una MAC, ni una lletra. Només sap si ha d'enviar +5 volts o 0 volts (o llum/no llum).

Funcions i característiques principals:

- **Representació dels Bits (Codificació):** Defineix com es tradueixen els 0s i 1s en senyals físics.
    
    - _Exemple:_ Si el voltatge és alt, és un 1; si és baix, és un 0 (o codificacions més complexes com Manchester).
        
- **Taxa de Dades (Amplada de banda):** Defineix el nombre de bits que s'envien per segon.
    
- **Topologia Física:** Com estan connectats els dispositius físicament (Bus, Estrellla, Anell).
    
- **Mitjans de Transmissió:**
    
    - _Guiats:_ Cable de parell trenat (UTP), Cable coaxial, Fibra òptica (llum).
        
    - _No guiats:_ Wi-Fi (ones de ràdio), Bluetooth, Infrarojos.
        

#### Hardware comú

- **Hub (Concentrador):** Dispositiu "tonto". Rep un senyal elèctric per un port i el repeteix per tots els altres sense mirar res. Simplement amplifica el senyal (repetidor).
    
- **Cables i Connectors:** RJ45, USB, Cables de fibra.
    
- **Targetes de Xarxa (NIC):** La part del transceiver que transforma les dades digitals de l'ordinador en senyals elèctrics.

>[!example] Visió de Laboratori: 
>La realitat del Wireless (Pràctica 2) Al laboratori, la **potència** no és un valor teòric ideal, sinó que es mesura en **RSSI** (Received Signal Strength Indicator).

- **Atenuació Real:** A la teoria, l'atenuació és constant segons el medi. A la pràctica, l'RSSI cau dràsticament amb la distància seguint una escala logarítmica (dBm).

- **Sensibilitat:** El hardware (l'ESP8266 de la pràctica) té un límit físic (ex: -90dBm). Si el senyal rebut baixa d'aquí, encara que hi hagi "bits", el xip no els pot descodificar (Pèrdua de paquets).

- **Llei de Friis:** És l'equació que vam utilitzar per relacionar la pèrdua de potència amb la distància i la freqüència (2.4GHz).




---

## Diferència entre la Capa Xarxa I Transport

### 1. L'Analogia de l'Edifici d'Oficines

- **Capa de Xarxa (Adreça IP):** És com l'**adreça postal d'un edifici** (Carrer Major, 15).
    
    - La missió de la Capa de Xarxa és fer arribar la carta fins a la porta de l'edifici correcte. Un cop allà, la seva feina s'ha acabat. Ha connectat **Màquina amb Màquina**.
    
- **Capa de Transport (Port):** És com el **número de despatx** o el **nom del departament** dins de l'edifici (Despatx 404, Departament de Vendes).
    
    - Un cop la carta és a l'edifici, algú l'ha de recollir i portar-la a la persona concreta que l'espera. Aquesta és la Capa de Transport. Connecta **Procés amb Procés**.
    

### 2. L'Explicació Tècnica

Quan tens l'ordinador encès, no tens només "una connexió". Tens molts programes (processos) utilitzant la xarxa alhora:

1. El navegador (Chrome) carregant una web.

2. L'Spotify reproduint música.

3. El client de correu sincronitzant emails.


Totes aquestes dades arriben pel mateix cable (o Wi-Fi) a la teva targeta de xarxa. Totes venen a la teva **IP**.

- Si només existís la **Capa de Xarxa**, l'ordinador rebria un munt de bits i no sabria què fer-ne: _"Això és un tros de cançó o un tros de pàgina web?"_.
    
- La **Capa de Transport** posa una etiqueta a cada paquet: el **Port**.
    
    - Dades pel port 443 -> Envia-ho al procés del navegador.
        
    - Dades pel port 53 -> Envia-ho al procés de resolució de noms (DNS).
        

### En resum

> [!important] Diferència Clau
> 
> - **Capa de Xarxa (IP):** Porta el paquet del punt A al punt B (d'ordinador a ordinador). Respon a la pregunta: _"A quina màquina va això?"_
>     
> - **Capa de Transport (Ports):** Porta el paquet de la porta de l'ordinador al programa concret. Respon a la pregunta: _"A quina aplicació va això?"_
>



---

# Model TCP/IP (Arquitectura d'Internet)

A diferència del [[Model OSI]] (que és teòric i de 7 capes), el **TCP/IP** és el model pràctic sobre el qual funciona Internet. Simplifica l'estructura en **4 capes**.

> [!abstract] Diferència Clau OSI vs TCP/IP 
> Mentre l'OSI diu "què s'ha de fer" (estàndard), el TCP/IP és la "implementació real" que fem servir cada dia.
> 
> - Les capes **Física** i **Enllaç** de l'OSI s'agrupen en **Accés a la Xarxa**.
>     
> - Les capes **Aplicació**, **Presentació** i **Sessió** de l'OSI s'agrupen en **Aplicació**.
>     


Les diferents capes són:
1. [[#1. Capa d'Aplicació| Capa d'Aplicació (Capa 1)]]
2. [[#2. Capa de Transport (Host-to-Host)| Capa de Transport (Capa 2)]]
3. [[#3. Capa d'Internet (Xarxa)| Capa d'Internet (Capa 3)]]
4. [[#4. Capa d'Accés a la Xarxa| Capa d'Accés de Xarxa (Capa 4)]]



---

## 1. Capa d'Aplicació

Agrupa les capes 5, 6 i 7 de l'OSI. Aquí és on viuen les dades de l'usuari i els protocols que utilitzem directament.

- **Protocols Clau:** HTTP/HTTPS (Web), FTP (Fitxers), SMTP (Correu), DNS (Noms), Telnet/SSH.
    
- **Unitat de Dades:** Dades / Missatge.
    

> [!example] Visió de Laboratori (Pràctica 4 & 1)
> 
> - **Sockets:** Quan programem, no ens preocupem de la presentació o sessió. Simplement obrim un socket i enviem un buffer de dades (JSON, text).
>     
> - **Formats:** A la pràctica IoT, el format **JSON** (`{"sensor": 25}`) és el que defineix aquesta capa.
>     
> - **Eines:** Comandes com `lynx` (navegador text) o clients FTP operen exclusivament aquí.
>     

---

## 2. Capa de Transport (Host-to-Host)

Equivalent a la Capa 4 de l'OSI. S'encarrega de la fiabilitat i de connectar aplicacions (ports) entre màquines.

- **Protocols Clau:**
    
    - **TCP (Transmission Control Protocol):** Orientat a connexió, fiable, reordena paquets. (Ex: Web, Correu).
        
    - **UDP (User Datagram Protocol):** Sense connexió, ràpid, no fiable. (Ex: Streaming, DNS).
        
- **Unitat de Dades:** Segment (TCP) / Datagrama (UDP).
    

> [!important] Conceptes d'Examen
> 
> - **Ports:** Identifiquen _quina aplicació_ rep les dades (ex: Port 80 per Web, Port 22 per SSH).
>     
> - **Sockets:** La combinació `IP : Port` defineix un punt final únic de comunicació.
>     

> [!example] Visió de Laboratori (Pràctica 4)
> 
> - **Implementació:** Al codi, escollim el protocol al crear el socket:
>     
>     - `SOCK_STREAM` --> TCP (Fem servir `connect()` i `accept()`).
>         
>     - `SOCK_DGRAM` --> UDP (Enviem directament).
>         
> - **Handshake:** Amb **Wireshark** (P5) veiem els paquets `SYN`, `SYN-ACK`, `ACK` que TCP envia sol _abans_ que la nostra aplicació enviï cap dada.
>     

---

## 3. Capa d'Internet (Xarxa)

Equivalent a la Capa 3 de l'OSI. S'encarrega de l'adreçament lògic i l'encaminament (trobar el camí) a través de xarxes diferents.

- **Protocols Clau:**
    
    - **IP (Internet Protocol):** IPv4 / IPv6. Porta les dades d'origen a destí.
        
    - **ICMP:** Control i errors (el que fa servir el `ping`).
        
    - **ARP:** Tradueix IP (lògica) a MAC (física). _Nota: A vegades es posa a la capa inferior, però treballa per a IP._
        
- **Unitat de Dades:** Paquet / Datagrama IP.


> [!example] Visió de Laboratori (Pràctica 1 & 3)
> 
> - **Configuració:** Assignar una IP, Màscara i Gateway (`default-router`) a una interfície.
>     
> - **NAT:** Transformació de la IP Privada (capçalera IP interna) a Pública per sortir a Internet.
>     
> - **Diagnòstic:** `ping` (mira si hi ha connectivitat IP) i `tracert` (mira els salts/routers pels que passa el paquet IP).
>     

---

## 4. Capa d'Accés a la Xarxa

Agrupa les capes 1 i 2 de l'OSI (Física + Enllaç). S'encarrega de moure els bits físicament entre dos dispositius connectats al mateix cable o mitjà (Wi-Fi).

- **Tecnologies:** Ethernet (Cable), 802.11 (Wi-Fi), Fibra òptica.
    
- **Adreçament:** Adreça MAC (Física).
    
- **Unitat de Dades:** Trama (Frame).
    

> [!example] Visió de Laboratori (Pràctica 2 & 5)
> 
> - **Física Real:** Aquí és on parlem de **RSSI** (potència Wi-Fi), atenuació i cables connectats al switch.
>     
> - **Wireshark:** Quan captures, veus la capçalera "Ethernet II".
>     
>     - Si la `Dest MAC` no és la teva (i no estàs en mode promiscu), la targeta de xarxa descarta el paquet _abans_ que arribi a la CPU.
>         
> - **Encapsulament:** La trama Ethernet té un camp `Type` que diu: "Ei, el que porto a dins és un paquet IP".
>

# Flux de Dades: El Procés d'Encapsulament

El secret de la comunicació en xarxa és l'**Encapsulament**. Imagina-ho com una nina russa (Matryoshka): amaguem la informació dins de capes protectores successives, on cada capa afegeix instruccions específiques per a una tasca concreta.

## 1. L'Origen: Capa d'Aplicació (Layer 7)

Tot comença quan l'usuari (tu) o un programa vol enviar informació.

- **Acció:** Generar les dades pures.
    
- **Unitat:** **Dades** (Payload).
    
- **Exemple Pràctic:** El teu navegador fa una petició `GET /index.html`. O el teu codi Python fa `socket.send("Hola")`.
    

> [!abstract] El paquet ara mateix és:
> 
> [ Dades de l'Usuari ]

---

## 2. Preparació: Capa de Transport (Layer 4)

Les dades poden ser massa grans, així que cal trossejar-les i assegurar-se que arribin a l'aplicació correcta.

- **Acció:** Segmentació.
    
- **Afegeix:** La **Capçalera TCP** (o UDP).
    
- **Dades Clau:**
    
    - **Port Origen:** (Ex: 51345, dinàmic). Qui envia?
        
    - **Port Destí:** (Ex: 80 HTTP, 443 HTTPS). A quina aplicació va?
        
    - **Control:** Número de Seqüència (per reordenar trossos) i Checksum.
        
- **Unitat resultant:** **Segment**.
    

> [!abstract] El paquet ara és:
> 
> [ Capçalera TCP | Dades de l'Usuari ]

> [!example] Visió Pràctica (Pràctica 4 Sockets)
> 
> Quan fas connect((IP, PORT)) al codi, estàs definint aquesta capçalera. Si t'equivoques de port, el segment arriba al PC destí però el SO no sap a quin programa entregar-lo i el descarta.

---

## 3. L'Encaminament: Capa de Xarxa (Layer 3)

El segment necessita viatjar a través d'Internet fins a l'altra punta del món. Necessitem una adreça global.

- **Acció:** Adreçament Lògic.
    
- **Afegeix:** La **Capçalera IP**.
    
- **Dades Clau:**
    
    - **IP Origen:** La teva IP (Ex: 192.168.1.15).
        
    - **IP Destí:** La IP del servidor (Ex: 8.8.8.8).
        
    - **TTL (Time To Live):** Per evitar que el paquet doni voltes per sempre.
        
- **Unitat resultant:** **Paquet**.
    

> [!abstract] El paquet ara és:
> 
> [ Capçalera IP | [ Capçalera TCP | Dades de l'Usuari ] ]

---

## 4. El Tram Local: Capa d'Enllaç (Layer 2)

El paquet IP sap que ha d'anar a Google, però per sortir de la teva habitació, primer ha d'arribar al teu Router. La IP no entén de cables, l'Ethernet/Wi-Fi sí.

- **Acció:** Adreçament Físic (Salt a salt).
    
- **Afegeix:** La **Capçalera Ethernet** (o 802.11 Wi-Fi) al principi i el **FCS (CRC)** al final.
    
- **Dades Clau:**
    
    - **MAC Origen:** La teva targeta de xarxa.
        
    - **MAC Destí:** La MAC del teu Router (Gateway). _Nota: No la del servidor final!_
        
    - **EtherType:** Codi que diu "a dins porto un paquet IPv4".
        
    - **FCS (Frame Check Sequence):** Càlcul matemàtic per veure si hi ha hagut errors al cable.
        
- **Unitat resultant:** **Trama** (Frame).
    

> [!abstract] El paquet ara és:
> 
> [ Cap. Ethernet | [ Cap. IP | [ Cap. TCP | Dades ] ] | FCS ]

> [!tip] Detall important (Pràctica 3 & ARP)
> 
> Com sap el teu PC la MAC del Router? Utilitza el protocol ARP (Address Resolution Protocol): "Qui té la IP 192.168.1.1?" -> El router respon "Soc jo, i la meva MAC és AA:BB:CC...".

---

## 5. La Transmissió: Capa Física (Layer 1)

La trama és només informació lògica (0s i 1s) a la memòria de la targeta de xarxa. Ara cal llançar-la al món real.

- **Acció:** Senyalització i Modulació.
    
- **Procés:**
    
    - Si és **Cable (Ethernet):** Els 1s i 0s es converteixen en voltatges elèctrics (+5V, -5V).
        
    - Si és **Wi-Fi:** Els 1s i 0s modulen una ona de ràdio (Canvis de fase/amplitud, com vas veure amb PSK a l'examen).
        
    - Si és **Fibra:** Polsos de llum.
        
- **Unitat:** **Bits / Senyals**.
    

---

# El Viatge (Nodes Intermedis)

Quan el senyal arriba al teu **Router**:

1. **Capa 1:** Transforma el voltatge en bits.
    
2. **Capa 2:** Llegeix la MAC Destí. _És per a mi?_ Sí. Treu l'embolcall Ethernet.
    
3. **Capa 3:** Llegeix la IP Destí. _És per a mi?_ No, és per a Google (8.8.8.8). Mira la seva **Taula d'Encaminament**.
    
4. **Re-encapsulament:**
    
    - Baixa el TTL de la IP.
        
    - Posa una **NOVA Capçalera Ethernet**:
        
        - MAC Origen: La MAC de sortida del Router.
            
        - MAC Destí: La MAC del següent router de l'operadora (ISP).
            
5. **Envia:** Torna a convertir en senyal elèctric/òptic cap a Internet.
    

> [!important] Regla d'Or
> 
> Les IPs (Capa 3) es mantenen d'origen a destí final (excepte si hi ha NAT).
> 
> Les MACs (Capa 2) canvien a cada salt (cada router) pel camí.

---

# Recepció al Destí (Desencapsulament)

Quan el senyal arriba finalment al servidor de Google:

1. **Capa Física:** Rep el senyal, recupera els bits `10101...`.
    
2. **Capa Enllaç:**
    
    - Verifica el FCS (no hi ha errors).
        
    - Mira la MAC. És la meva? Sí.
        
    - _Treu la capçalera Ethernet._
        
3. **Capa Xarxa:**
    
    - Mira la IP. És la meva? Sí.
        
    - _Treu la capçalera IP._
        
4. **Capa Transport:**
    
    - Mira el Port Destí (80). Hi ha algun procés escoltant? Sí, el servidor web (Apache/Nginx).
        
    - Revisa el Checksum TCP. Tot correcte.
        
    - _Treu la capçalera TCP._
        
5. **Capa Aplicació:**
    
    - El servidor web rep les dades pures: `GET /index.html`.
        
    - Processa la petició i **comença tot el procés al revés** per enviar-te la resposta.



---
# PROBLEMES


# CRC

Per calcular el **CRC (Cyclic Redundancy Check)**, seguirem una sèrie de passos sistemàtics basats en l'aritmètica modular en base 2 (operacions **XOR** sense ròssec).

---

## Càlcul del CRC: Pas a pas

### 1. Traducció del Polinomi Generador

El polinomi generador $G(X) = X^5 + X + 1$ s'ha de convertir a format binari. Cada potència de $X$ representa la posició d'un bit (començant per 0 a la dreta).

- $X^5$ $\rightarrow$ bit a la posició 5: **1**
    
- $X^4$ $\rightarrow$ bit a la posició 4: **0**
    
- $X^3$ $\rightarrow$ bit a la posició 3: **0**
    
- $X^2$ $\rightarrow$ bit a la posició 2: **0**
    
- $X^1$ $\rightarrow$ bit a la posició 1: **1**
    
- $X^0$ ($1$) $\rightarrow$ bit a la posició 0: **1**
    

> [!important] Divisor Binari
> 
> El divisor per a l'operació serà: 100011.
> 
> El grau del polinomi és $n = 5$.

### 2. Preparació de la Trama (Padding)

Afegim tants zeros al final de la trama original com el grau del polinomi ($n = 5$).

- Trama original: `10110011101`
    
- Trama amb padding: `10110011101` + `00000` = **`1011001110100000`**
    

### 3. Divisió Binària (XOR)

Realitzem la divisió de la trama amb padding pel divisor binari. Recorda: **1 XOR 1 = 0**, **0 XOR 0 = 0**, **1 XOR 0 = 1**.

Plaintext

```
1011001110100000 | 100011
100011           |--------------
------           | 10111101011 (Quocient, no el necessitem)
00111111         |
  100011         | (XOR quan el bit a l'esquerra és 1)
  ------         |
  0111001        |
   100011        |
   ------        |
   0110101       |
    100011       |
    ------       |
    0101100      |
     100011      |
     ------      |
     00111100    | (Baixem un zero, no cap, en baixem un altre)
      0111100    |
       100011    |
       ------    |
       0111110   |
        100011   |
        ------   |
        0111010  |
         100011  |
         ------  |
         0110010 |
          100011 |
          ------ |
          010021 (Error de càlcul visual, fem-ho net a sota)
```

**Desenvolupament net de la resta:**

1. `101100` XOR `100011` = `001111`
    
2. Baixem l'`1`: `11111` (massa petit, baixem un altre `1`) $\rightarrow$ `111111`
    
3. `111111` XOR `100011` = `011100`
    
4. Baixem el `0`: `111000` XOR `100011` = `011011`
    
5. Baixem l'`1`: `110111` XOR `100011` = `010100`
    
6. Baixem l'`1`: `101001` XOR `100011` = `001010`
    
7. Baixem el `0`: `10100` (massa petit, baixem un altre `0`) $\rightarrow$ `101000`
    
8. `101000` XOR `100011` = `001011`
    
9. Baixem el `0`: `10110` (massa petit, baixem un altre `0`) $\rightarrow$ `101100`
    
10. `101100` XOR `100011` = `001111`
    
11. Baixem l'últim `0`: **`11110`**
    

---

### Resultat Final

> [!success] Valor del CRC
> 
> El residu de la divisió és 11110.
> 
> Aquest és el codi que s'adjuntarà a la trama original per a la detecció d'errors.

- **Trama a transmetre:** `10110011101` + `11110` = **`1011001110111110`**

# Transmissió de Senyal i Capacitat de Canal

En aquesta secció analitzem els límits físics de la transmissió de dades, especialment en entorns sense fils (Wi-Fi), utilitzant les lleis de Shannon i Friis.

## 1. Conceptes Fonamentals i Fórmules

### A. Teorema de Shannon-Hartley

Defineix la capacitat màxima teòrica d'un canal de comunicació en presència de soroll.

$$C = B \cdot \log_2(1 + SNR_{lineal})$$

- **$C$**: Capacitat del canal (bits per segon).
    
- **$B$**: Ample de banda (Hertz).
    
- **$SNR_{lineal}$**: Relació senyal-soroll en valor lineal (no en dB).
    

### B. Relació Senyal-Soroll (SNR)

Mesura la qualitat del senyal respecte al soroll de fons.

- **Conversió de dB a Lineal:** $SNR_{lineal} = 10^{\frac{SNR_{dB}}{10}}$
    
- **Càlcul en dBm:** $SNR_{dB} = P_{recapció}(dBm) - P_{soroll}(dBm)$
    

### C. Model de Propagació en l'Espai Lliure (Llei de Friis)

Calcula la pèrdua de potència del senyal segons la distància i la freqüència.

$$L_{FS} (dB) = 32.44 + 20 \log_{10}(d_{km}) + 20 \log_{10}(f_{MHz})$$

- **$L_{FS}$**: Pèrdua en l'espai lliure ($P_{transmissió} - P_{recepció}$).
    
- **$d$**: Distància en quilòmetres.
    
- **$f$**: Freqüència en Megahertz.
    

---

## 2. Resolució de l'Exercici de Laboratori

**Dades de partida:**

- Ample de banda ($B$): $40 \text{ MHz} = 40 \cdot 10^6 \text{ Hz}$
    
- Freqüència ($f$): $5 \text{ GHz} = 5000 \text{ MHz}$
    
- Potència de transmissió ($P_t$): $17 \text{ dBm}$
    
- Sensibilitat ($P_{min}$): $-90 \text{ dBm}$
    
- $SNR$ objectiu: $20 \text{ dB}$
    
- Guany antenes ($G$): $0 \text{ dB}$
    

### 1. Determinació de la velocitat (Shannon)

Primer passem el $SNR$ a valor lineal: $SNR_{lin} = 10^{20/10} = 100$.

Apliquem Shannon:

$$C = 40 \cdot 10^6 \cdot \log_2(1 + 100) \approx 40 \cdot 10^6 \cdot 6.658 \approx 266.32 \text{ Mbps}$$

> [!success] Conclusió
> 
> Sí, podem assolir els 150 Mbps del protocol 802.11n, ja que el límit físic del canal amb aquest soroll és de ~266 Mbps.

### 2. Codificació i Velocitat Final

Quants bits per senyal (símbol) podem fer servir?

$n = \log_2(1 + SNR_{lin}) = \log_2(101) \approx 6.65 \text{ bits/símbol}$.

En la pràctica, s'utilitzen nombres enters de bits (com 64-QAM). Per tant, agafem 6 bits per símbol.

La velocitat final efectiva seria:

$$V = B \cdot n = 40 \text{ MHz} \cdot 6 \text{ bits/símbol} = 240 \text{ Mbps}$$

### 3. Potència de Soroll ($N$)

El soroll es calcula a partir de la potència que rebem i la relació que volem mantenir. Si considerem que el senyal arriba just al límit de la sensibilitat:

$$SNR_{dB} = P_{recepció} - N \rightarrow 20 \text{ dB} = -90 \text{ dBm} - N$$

$$N = -90 - 20 = -110 \text{ dBm}$$

### 4. Distància màxima (sense considerar soroll)

Utilitzem la sensibilitat del dispositiu com a límit de pèrdua.

Pèrdua màxima permesa ($L_{max}$): $17 \text{ dBm} - (-90 \text{ dBm}) = 107 \text{ dB}$.

Apliquem Friis:

$107 = 32.44 + 20 \log_{10}(d) + 20 \log_{10}(5000)$

$107 = 32.44 + 20 \log_{10}(d) + 73.98$

$107 = 106.42 + 20 \log_{10}(d)$

$0.58 = 20 \log_{10}(d) \rightarrow \log_{10}(d) = 0.029$

$d = 10^{0.029} \approx 1.069 \text{ km} \rightarrow \mathbf{1069 \text{ metres}}$

### 5. Distància màxima (considerant soroll)

Si el soroll ambiental fos més alt que la sensibilitat (per exemple, si el soroll fos de $-100 \text{ dBm}$), la potència mínima de recepció per mantenir el $SNR$ de $20 \text{ dB}$ hauria de ser major:

$P_{req} = N + SNR = -110 \text{ dBm} + 20 \text{ dB} = -90 \text{ dBm}$.

En aquest cas concret, com que el soroll calculat és coherent amb la sensibilitat, la distància es manté igual (**1069 m**). Si el soroll pugés, la distància de cobertura cauria dràsticament.



## Resolució mecànica

### 1. Capacitat de Shannon (Velocitat Teòrica)

**Objectiu:** Determinar si 150 Mbps és físicament possible.

- **Pas A (SNR lineal):** $SNR_{lin} = 10^{\frac{SNR_{dB}}{10}} = 10^{\frac{20}{10}} = 100$
    
- **Pas B (Càlcul):** $C = B \cdot \log_2(1 + SNR_{lin}) = 40 \cdot \log_2(101)$
    
- **Càlcul ràpid:** $40 \cdot 6.658 = 266.32 \text{ Mbps}$
    

> [!success] Resultat
> 
> Sí, és possible perquè $266.32 \text{ Mbps} > 150 \text{ Mbps}$.

### 2. Codificació i Velocitat Real

**Objectiu:** Ajustar els bits teòrics a un valor enter (com s'implementa al hardware).

- **Pas A (Bits per símbol):** $n = \lfloor \log_2(1 + SNR_{lin}) \rfloor = \lfloor 6.65 \rfloor = \mathbf{6 \text{ bits/símbol}}$
    
- **Pas B (Velocitat final):** $V = B \cdot n = 40 \text{ MHz} \cdot 6 = \mathbf{240 \text{ Mbps}}$
    

### 3. Potència de Soroll ($N$)

**Objectiu:** Trobar el soroll de fons del sistema en dBm.

- **Dada:** El senyal mínim detectable ($P_{rec}$) és la sensibilitat: $-90 \text{ dBm}$.
    
- **Fórmula mecànica:** $N = P_{rec} - SNR_{dB}$
    
- **Càlcul:** $N = -90 \text{ dBm} - 20 \text{ dB} = \mathbf{-110 \text{ dBm}}$
    

### 4. Distància Màxima (Espai Lliure)

**Objectiu:** Trobar $d$ usant la pèrdua màxima permesa ($L_{FS}$).

- **Pas A (Pèrdua màxima):** $L_{FS} = P_{transmissió} - P_{sensibilitat} = 17 - (-90) = \mathbf{107 \text{ dB}}$
    
- **Pas B (Fòrmula de Friis):** $107 = 32.44 + 20\log(d_{km}) + 20\log(f_{MHz})$
    
- **Pas C (Substitució):** $107 = 32.44 + 20\log(d) + 20\log(5000)$
    
- Pas D (Aïllar): 1. $107 = 32.44 + 20\log(d) + 73.98$
    
    2. $107 = 106.42 + 20\log(d)$
    
    3. $0.58 = 20\log(d) \rightarrow \log(d) = 0.029$
    
- **Resultat:** $d = 10^{0.029} = \mathbf{1.069 \text{ km}}$
    

### 5. Distància amb Soroll

**Objectiu:** Verificar si el soroll limita la cobertura més que la sensibilitat.

- **Pas A:** Calcular $P_{rec\_necessària} = N + SNR = -110 + 20 = -90 \text{ dBm}$.
    
- Pas B: Comparar amb la sensibilitat. Com que coincideix amb els $-90 \text{ dBm}$ anteriors, la distància és la mateixa: 1.069 km.
    
    (Si el soroll fos més alt, la $P_{rec\_necessària}$ seria més gran i la distància disminuiria).
    


# Modulació Digital

## 1. Què és?

La **Modulació Digital** és el procés de transformar una seqüència de bits (0s i 1s) en un senyal analògic (ona portadora) adequat per viatjar a través d'un medi físic (aire, cable, fibra)1.

- **Objectiu Principal:** Adaptar la informació digital a les característiques del canal de transmissió perquè arribi el més lluny i ràpid possible sense errors.
    
- **Concepte Clau:** Modifiquem paràmetres de l'ona portadora (sinusoïdal) en funció de les dades.
    

## 2. Tipus de Modulació (Què fan?)

Es modifiquen tres paràmetres bàsics de l'ona portadora:

- **[[ASK]] (Amplitude Shift Keying):**
    
    - **Mecanisme:** Modifica l'**amplitud** de l'ona. (Ex: Amplitud alta = 1, Amplitud baixa = 0).
        
    - **Característiques:** Senzilla però molt sensible al soroll (el soroll afecta directament l'amplitud).
        
- **[[FSK]] (Frequency Shift Keying):**
    
    - **Mecanisme:** Modifica la **freqüència**. (Ex: Freqüència alta = 1, Freqüència baixa = 0).
        
    - **Característiques:** Més immune al soroll que ASK.
        
- **[[PSK]] (Phase Shift Keying):**
    
    - **Mecanisme:** Modifica la **fase** de l'ona. (Ex: Desfasament de $180^{\circ}$ quan canviem de bit).
        
    - **Característiques:** És la més robusta contra el soroll.
        
- **[[QAM]] / QPSK (Quadrature Amplitude Modulation):**
    
    - **Mecanisme:** Combina canvis d'**amplitud** i de **fase** per enviar més bits per cada símbol (augmenta l'eficiència espectral).
        

## 3. Problemes i Limitacions

Els senyals reals s'enfronten a fenòmens físics que degraden la comunicació:

1. **Soroll (Noise):** Senyals externs indesitjats que se sumen al nostre.
    
    - _Tipus:_ Tèrmic (inevitable, depèn de la temperatura), Impulsiu, Diafonia (crosstalk)3.
        
    - _Efecte:_ Si el soroll és molt alt respecte al senyal ($S/N$ baixa), el receptor confon un 1 amb un 0.
        
2. **Atenuació:** Pèrdua de potència del senyal a mesura que avança per la distància ($d$)4.
    
    - _Resolució:_ Ús d'amplificadors o repetidors.
        
3. **Interferència Intersimbòlica (ISI):** Distorsió que fa que un símbol es "barregi" amb el següent, fent-lo il·legible (visible al "Diagrama d'Ull")5.
    
4. **Ample de Banda Limitat (Bandwidth):** El canal només deixa passar un rang de freqüències. Això limita la velocitat màxima (Teorema de Nyquist/Hartley)6.
    

---

# [[Resolució Mecànica d'Exercicis]]

Aquesta és la guia pas a pas per resoldre els problemes típics d'examen de la Capa Física (Shannon, Balanç de Potències, etc.).

### A. Preparació Prèvia (Unitats)

Abans de tocar la calculadora, **revisa les unitats**. És l'error més comú.

- **Decibels (dB) a Lineal:** Moltes fórmules (com Shannon) necessiten valors lineals, no dB.
    
    - $SNR_{lineal} = 10^{(SNR_{dB}/10)}$
        
- **dBm a mW:**
    
    - $P_{mW} = 10^{(P_{dBm}/10)}$
        
- **Longitud d'ona ($\lambda$):** Sovint et donen la freqüència ($f$). Calcula $\lambda$ en metres.
    
    - $\lambda = \frac{c}{f}$ (on $c \approx 3\cdot10^8$ m/s).
        

### B. Tipologia d'Exercicis

#### 1. Càlcul de Velocitat Màxima (Teoremes)

Et demanaran "quina és la velocitat màxima teòrica" o "quants bits/nivells necessitem".

- **Cas 1: Canal ideal (sense soroll) -> Llei de Hartley/Nyquist**
    
    - Ús: Quan et parlen de nivells ($M$) o bits per símbol ($n$).
        
    - Fórmula: $C = 2 \cdot B \cdot \log_2(M)$
        
        - $C$: Capacitat (bps).
            
        - $B$: Ample de banda (Hz).
            
        - $M$: Nombre de nivells (Ex: QPSK té 4 nivells). Si tens bits ($n$), $M = 2^n$.
            
- **Cas 2: Canal amb soroll -> Teorema de Shannon** 777
    
    - Ús: Quan et donen la relació Senyal-Soroll ($SNR$ o $S/N$).
        
    - Fórmula: $C = B \cdot \log_2(1 + \frac{S}{N})$
        
    - **Mecànica:**
        
        1. Converteix la SNR de dB a lineal (veure apartat A).
            
        2. Aplica la fórmula.
            
        3. El resultat és el límit absolut. Mai podràs transmetre més ràpid que això.
            

#### 2. Balanç de Potències (Enllaç sense fils)

Et demanaran "arriba el senyal?", "quina distància màxima?", "quina potència d'emissió cal?".

- **Equació Bàsica (en dB/dBm és només sumar i restar):**
    
    - $P_{RX} = P_{TX} + G_{TX} + G_{RX} - \text{Pèrdues}$
        
    - _Condició d'èxit:_ $P_{RX} \ge \text{Sensibilitat del Receptor}$.
        
- **Càlcul de Pèrdues (Atenuació en espai lliure):** 8
    
    - Si no et donen l'atenuació directa, has de calcular-la:
        
    - $L_{dB} = 20 \cdot \log_{10}\left(\frac{4 \cdot \pi \cdot d}{\lambda}\right)$
        
        - _Nota:_ Vigila que $d$ i $\lambda$ tinguin les mateixes unitats (metres).
            

#### 3. Càlcul de "Bits per Símbol" en Modulacions

Et donen una modulació (ex: 64-QAM) i et pregunten velocitat o bits.

- **Mecànica:**
    
    1. Mira el número del nom (ex: 64). Això és $M$ (nivells).
        
    2. Nombre de bits ($n$) = $\log_2(M)$. (Ex: $\log_2(64) = 6$ bits/símbol).
        
    3. Velocitat ($R_b$) = $n \times \text{Velocitat de modulació (bauds)}$.
        

Exemples de "Trampes" d'Examen 9999

1. **Et donen la SNR en dB:** Si la poses directament dins del $\log_2$ de Shannon, el resultat serà incorrecte. Passa-la a lineal primer.
    
2. **Et donen la distància en km i la $\lambda$ en m:** Passa-ho tot a metres abans de calcular pèrdues.
    
3. **Et demanen "Eficiència":** Sol ser la relació entre la velocitat real aconseguida i la màxima teòrica (Shannon), o l'ús dels bits de dades vs bits totals (overhead).


## 1. Què són les Topologies de Xarxa?

La topologia defineix com es connecten els nodes al medi físic. Cal distingir entre dues visions:

- **Topologia Física:** Com està muntat realment el cablejat (la "forma" dels cables).
    
- **Topologia Lògica:** Com els nodes interpreten que estan connectats i com viatgen les dades (el flux d'informació)1.
    

### A. Topologia en BUS

És la configuració clàssica (i ara obsoleta per a LANs d'oficina, però usada en sistemes industrials/multimèdia)2.

- **Funcionament:**
    
    - Tots els nodes comparteixen un únic cable (medi compartit).
        
    - Quan un node transmet, el senyal viatja en totes direccions.
        
    - **Tots** els nodes reben la informació, però només el destinatari la processa; la resta la descarta3.
        
- **Problema Principal:** Les **col·lisions**. Si dos nodes parlen alhora, els senyals es barregen i la informació es perd4.
    
- **Solució del Protocol (CSMA/CD):** S'utilitza en Ethernet sobre Bus. El node "escolta" abans de parlar. Si detecta una col·lisió, para i espera un temps aleatori5.
    

### B. Topologia en ANELL (Ring)

Consisteix en un conjunt de repetidors units punt a punt formant un bucle tancat6.

- **Funcionament:**
    
    - Els enllaços són unidireccionals (les dades giren en un sentit).
        
    - Cada estació té un repetidor que llegeix el bit, el pot modificar i el retransmet al següent7.
        
    - L'estació origen és l'encarregada d'eliminar les dades de l'anella quan li tornen (després de fer la volta completa)8.
        
- **Mecanisme d'Accés (Token):** Per evitar col·lisions, circula una trama especial anomenada "Token". Qui té el Token, té permís per parlar9.
    
- **Estats del Repetidor:**
    
    1. **Espera/Recepció:** Mira si passa el Token o dades per a ell10.
        
    2. **Transmissió:** Envia dades pròpies (si té el Token)11.
        
    3. **Desviament (Bypass):** Si l'estació cau, el repetidor deixa passar el senyal directament per no tallar l'anella12.
        

### C. Topologia en ESTEL (Star)

És l'estàndard actual (Ethernet modern). Cada estació es connecta individualment a un node central13.

- **El Node Central és la clau:**
    
    - **HUB (Concentrador - Capa Física):** Rep un senyal i el repeteix a _tots_ els ports. Actua com un Bus lògic (tothom rep tot, hi ha col·lisions)1414.
        
    - **SWITCH (Commutador - Capa MAC):** És intel·ligent. Rep un senyal i l'envia _només_ al port del destinatari. Elimina les col·lisions i permet comunicació simultània15151515.
        

---

## 2. Tipologia de Problemes i Reptes

En els exàmens i disseny de xarxes, els problemes se centren en les limitacions físiques i la lògica del protocol MAC.

### Problema 1: Detecció de Col·lisions (CSMA/CD)

En un BUS, per a què funcioni la detecció de col·lisions (CD), l'emissor ha de continuar transmetent durant el temps suficient perquè el senyal vagi fins a l'altre extrem, xoqui, i l'avís de xoc torni.

- **Repte:** Si la trama és massa curta o el cable massa llarg, l'emissor acabarà d'enviar abans de saber que hi ha hagut un accident. Es pensaria que tot ha anat bé quan en realitat s'han perdut dades.
    
- **Condició crítica:** $T_{trama} \ge 2 \cdot T_{propagació}$16.
    

### Problema 2: Prioritats en Token Ring

En una anella, com garantim que les dades urgents passin primer?

- **Repte:** Un node amb dades poc importants no hauria d'agafar el Token si un altre node té una emergència.
    
- **Mecanisme:** El sistema de **Reserva i Prioritat** (bits en la trama del Token). Un node pot "reservar" el pròxim Token escrivint en els bits de reserva de la trama que passa, sempre que la seva prioritat sigui major17171717.
    

### Problema 3: Atenuació i Potència (Wireless)

En topologies sense fils (Wireless), el medi (aire) atenua molt el senyal.

- **Repte:** Calcular si la potència que arriba al receptor ($P_{RX}$) és superior a la sensibilitat mínima del xip.
    
- **Equació:** Balanç de potències (Fórmula de Friis adaptada)1818.
    

---

## 3. Resum "Obsidian" (Punts Clau)

Aquí tens l'esquema de conceptes per a les teves notes:

- **Topologia Física vs Lògica:** Connexió real vs. Flux de dades.
    
- **BUS:**
    
    - Medi compartit, tots reben tot.
        
    - Control d'accés: **CSMA/CD** (escoltar abans de parlar + detectar xoc).
        
    - Condició vital: La trama ha de durar més que el viatge d'anada i tornada del senyal ($RTT$).
        
- **ANELL (Token Ring):**
    
    - Enllaços punt a punt, bucle tancat.
        
    - Control d'accés: **Token** (testimoni).
        
    - Gestió: Sistema de prioritats i reserves en la capçalera.
        
- **ESTEL:**
    
    - Node central.
        
    - Hub = Bus lògic (col·lisions).
        
    - Switch = Connexions dedicades (sense col·lisions).
        

---

## 4. Resolució MECÀNICA d'Exercicis

Aquesta és la part més important per aprovar. Segueix aquests passos algoríthmics davant dels problemes típics dels documents .

### TIPUS A: Càlcul de CSMA/CD (Col·lisions)

**Enunciat típic:** "Tenim una xarxa de longitud $L$, velocitat $v$, i ample de banda $BW$. Quina és la mida mínima de la trama per detectar col·lisions?"

1. **Pas 1: Calcular el Temps de Propagació ($T_{prop}$)**
    
    - Fórmula: $T_{prop} = \frac{\text{Distància (m)}}{\text{Velocitat (m/s)}}$
        
    - _Nota:_ Si no et donen la velocitat, en coure sol ser $\approx 2/3$ de $c$ ($2 \cdot 10^8$ m/s), però busca la dada.
        
2. **Pas 2: Calcular el RTT (Round Trip Time)**
    
    - Fórmula: $RTT = 2 \cdot T_{prop}$
        
    - _Explicació:_ El pitjor cas és xocar al final del cable i que l'avís torni.
        
3. **Pas 3: Aplicar la condició de seguretat**
    
    - Condició: $T_{trama} \ge RTT$
        
4. **Pas 4: Calcular els bits mínims**
    
    - Sabem que $T_{trama} = \frac{\text{Bits}}{\text{Velocitat Transmissió (BW)}}$
        
    - Per tant: $\text{Bits Mínims} = RTT \cdot BW$
        
    - _Unitats:_ Assegura't que el BW estigui en bits/s (no Mb/s).
        

### TIPUS B: Exercicis de Token Ring (Prioritats)

**Enunciat típic:** "Dissenyar un protocol Token Ring, explicar com funciona la prioritat o reservar torn"19191919.

1. **Mecànica de la Reserva:**
    
    - Node A rep una trama de dades (ocupada) que passa per allà.
        
    - Node A vol transmetre amb prioritat $P_{A}$.
        
    - Node A mira el camp "Reserva" ($R$) de la trama que passa.
        
    - **Condició:** SI $P_{A} > R$, aleshores A sobrescriu $R$ amb el seu valor $P_{A}$.
        
    - _Resultat:_ Quan el Token s'alliberi, tindrà la prioritat que ha reservat A.
        
2. **Mecànica de l'Alliberament:**
    
    - L'estació que ha emès les dades, quan les rep de tornada, les treu.
        
    - Genera un nou Token LLIURE.
        
    - **Important:** Copia al camp "Prioritat" del nou Token el valor que hi havia al camp "Reserva" (el que ha escrit el Node A en el pas anterior).
        

### TIPUS C: Wireless i Potència (Friis)

**Enunciat típic:** "Calcula la distància màxima donada una potència i sensibilitat"20.

1. **Pas 1: Identificar les variables**
    
    - $P_{TX}$ (Potència Transmesa, passar a dBm sovint ajuda).
        
    - $G_{TX}, G_{RX}$ (Guanys antenes).
        
    - $\text{Sensibilitat}$ (Potència mínima necessària $P_{RX}$).
        
    - $\lambda$ (Longitud d'ona $= c / f$).
        
2. **Pas 2: Plantejar l'equació de pèrdues**
    
    - L'equació base és: $P_{RX} = P_{TX} \cdot G_{TX} \cdot G_{RX} \cdot \left( \frac{\lambda}{4 \pi d} \right)^2 \cdot \xi$21.
        
3. **Pas 3: Aïllar la incògnita (normalment $d$)**
    
    - Sovint és més fàcil treballar en dB (sumes i restes) i al final passar a lineal, o aïllar $d$ directament de l'arrel quadrada.
        
    - Si $Att$ (Atenuació) és el límit: $Att_{max} = 10 \log \left( \frac{P_{TX}}{P_{min}} \right)$.
        

### 📝 Enunciat de l'Exercici (Model Examen)

> Tenim un punt d'accés que transmet a una freqüència de **2.4 GHz** amb una potència d'emissió de **100 mW**. Els guanys de les antenes (transmissor i receptor) són de **2 dB** cadascuna (factor lineal de 1.58).
> 
> Si la **sensibilitat mínima** del receptor és de **-80 dBm**, quina és la **distància màxima** teòrica a la qual ens podem connectar? (Considera un medi ideal sense pèrdues addicionals, $\xi = 1$).

---

### ⚙️ Resolució Mecànica

#### Pas 1: Extracció i Unificació de Dades

El primer error sol ser barrejar unitats (lineals vs logarítmiques/dB). Ho passem tot a **unitats lineals (Wats i nombres naturals)** per aplicar l'equació de l'examen.

- **Freqüència ($f$):** $2.4 \text{ GHz} = 2.4 \cdot 10^9 \text{ Hz}$.
    
- **Potència Transmissió ($P_{TX}$):** $100 \text{ mW} = 0.1 \text{ W}$.
    
- **Guany ($G_{TX}$ i $G_{RX}$):** L'enunciat ens diu 2 dB. Si ens donen dB, ho passem a lineal:
    
    - $G = 10^{(dB/10)} \rightarrow G = 10^{(2/10)} \approx 1.58$.
        
- **Sensibilitat ($P_{RX}$):** Ens la donen en dBm ($-80 \text{ dBm}$). Això és la potència mínima que ha d'arribar. La passem a mW i després a W:
    
    - $P_{mW} = 10^{(dBm/10)} \rightarrow P_{mW} = 10^{(-80/10)} = 10^{-8} \text{ mW}$.
        
    - $P_{RX} = 10^{-11} \text{ W}$.
        

#### Pas 2: Calcular la Longitud d'Ona ($\lambda$)

Necessitem $\lambda$ per a la fórmula. Sabem que la velocitat de la llum $c \approx 3 \cdot 10^8 \text{ m/s}$.

$$\lambda = \frac{c}{f} = \frac{3 \cdot 10^8}{2.4 \cdot 10^9} = 0.125 \text{ metres}$$

#### Pas 3: Plantejar l'Equació de Friis

Segons el formulari de l'examen2, la fórmula és:

$$P_{RX} = P_{TX} \cdot G_{TX} \cdot G_{RX} \cdot \left( \frac{\lambda}{4 \pi d} \right)^2 \cdot \xi$$

_(Nota: En aquest cas $\xi = 1$, així que l'ignorem)._

#### Pas 4: Aïllar la Incògnita (Distància $d$)

Volem trobar $d$. Aquesta és la manipulació algebraica que has de memoritzar o saber deduir ràpidament:

1. Passem els termes de l'esquerra a dividir/multiplicar:
    
    $$\frac{P_{RX}}{P_{TX} \cdot G_{TX} \cdot G_{RX}} = \left( \frac{\lambda}{4 \pi d} \right)^2$$
    
2. Fem l'arrel quadrada a banda i banda:
    
    $$\sqrt{\frac{P_{RX}}{P_{TX} \cdot G_{TX} \cdot G_{RX}}} = \frac{\lambda}{4 \pi d}$$
    
3. Aïllem la $d$:
    
    $$d = \frac{\lambda}{4 \pi} \cdot \sqrt{\frac{P_{TX} \cdot G_{TX} \cdot G_{RX}}{P_{RX}}}$$
    

#### Pas 5: Substitució i Càlcul Final

Posem els números que hem preparat al Pas 1 i 2.

$$d = \frac{0.125}{4 \pi} \cdot \sqrt{\frac{0.1 \cdot 1.58 \cdot 1.58}{10^{-11}}}$$

- Càlcul del terme exterior: $\frac{0.125}{12.566} \approx 0.009947$
    
- Càlcul de l'interior de l'arrel:
    
    - Numerador: $0.1 \cdot 1.58 \cdot 1.58 \approx 0.2496$
        
    - Divisió: $\frac{0.2496}{10^{-11}} = 0.2496 \cdot 10^{11} = 2.496 \cdot 10^{10}$
        
- Arrel quadrada: $\sqrt{2.496 \cdot 10^{10}} \approx 157987$
    

Multipliquem:

$$d \approx 0.009947 \cdot 157987 \approx 1571.5 \text{ metres}$$

---

### ✅ Resultat Final

La distància màxima teòrica és de **1.57 km**.

---

### 💡 Consell de Professor

Si a l'examen et donen un factor d'eficiència o pèrdues (per exemple $\xi = 0.75$ com a 3), simplement afegeix aquest número multiplicant dins de l'arrel quadrada al numerador (juntament amb $P_{TX}$).
