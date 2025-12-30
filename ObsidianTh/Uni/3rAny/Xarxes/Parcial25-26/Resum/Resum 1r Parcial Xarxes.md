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