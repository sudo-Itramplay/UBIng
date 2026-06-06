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

- **Gestió d'Enviaments Parcials:** L'API de Java per a `InputStream` té un comportament específic: el mètode `read(byte[] b)` es bloqueja fins a tenir dades disponibles, però _no garanteix_ llegir tots els bytes demanats (la longitud del buffer) d'una sola vegada.
    
- Retorna el nombre de bytes que s'han llegit realment. Per solucionar-ho (com es veu a la funció `read_bytes` de `ComUtils`), cal implementar un bucle `do-while` que vagi acumulant les lectures (`len += dis.read(...)`) fins que s'arribi a la quantitat total esperada (`len < numBytes`).
    
- **Tipus de Dades i Endianness:** No podem enviar un sencer de Java per la xarxa tal qual. Un sencer (int32) ocupa 4 bytes i per la xarxa l'hem d'enviar i rebre ordenant-los en format _BigEndian_.
    
- En el codi d'implementació, transformar un enter a bytes implica fer servir operadors de desplaçament de bits (`>>`) combinats amb màscares bit a bit (`& 0xFF`) per aïllar cada byte, assignant el byte més significatiu a la primera posició de l'array (`bytes[0]`). Desfer aquest procés (`bytesToInt32`) implica desplaçar els bytes cap a l'esquerra (`<<`) i sumar-los amb operadors `OR` lógics (`|`).
    
- **Gestió de Cadenes de Caràcters (Strings):** Com que la xarxa envia bytes, les cadenes s'han de gestionar acuradament.
    
    - _Mida Fixa:_ Si enviem una cadena que sempre ha de fer 'X' bytes, cal convertir cada `char` a `byte` (ignorant el byte més alt). Si la cadena és més curta que la mida especificada, el buffer sobrer s'ha d'omplir amb espais en blanc.
        
    - _Mida Variable:_ Aquesta és l'arquitectura més robusta. L'emissor primer ha de calcular la longitud de la cadena. Seguidament crea i envia una "capçalera" d'una mida coneguda i fixa (per exemple, 4 bytes) que codifica aquesta longitud en format text numèric (rellenant amb '0's si cal). Una vegada enviada la capçalera, s'envien els bytes de la cadena.
        
    - El receptor, per la seva banda, llegeix primer exactament els bytes de la capçalera, en fa un parsing a enter (`Integer.parseInt`), coneix així quants bytes exactes té la cadena i instància un nou array per rebre exclusivament la càrrega útil (el text).
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

_(Referència: Diapositives 52-54)_

Com enviar missatges a múltiples destinataris de cop.

- Mentre l'Unicast s'encarrega d'enviar informació a un únic receptor (sigui per TCP o UDP), el Multicast permet l'enviament cap a múltiples receptors.
    
- Aquesta tecnologia només està disponible via UDP, pel que no hi ha garanties de recepció, i està construïda a sobre del protocol IP.
    
- Permet enviar un paquet IP a un conjunt de màquines que formen un grup. Aquests grups s'identifiquen amb adreces d'internet de Classe D, que van des de la 224.0.0.0 fins a la 239.255.255.255.
    
- Quan una màquina s'afegeix al grup rep tots els missatges; tanmateix, és possible enviar-hi paquets sense formar-ne part.
    

---

# Consideracions d'Implementació

Aquest és l'apartat vital per no fallar a les pràctiques i demostrar que saps com es comporta la xarxa al món real.

- **Enviaments parcials i Dades:** En Java de baix nivell, les funcions `read` no garanteixen la recepció de tots els caràcters sol·licitats de cop; llegeixen un nombre indeterminat limitat per la longitud del buffer i retornen el nombre realment llegit. 

>[!warning] Bucles
>- Això requereix crear bucles (`do-while`) que vagin sumant els bytes llegits fins a arribar a la quantitat esperada. 
>- Cal també processar correctament els formats (BigEndian per enters i la creació de capçaleres de longitud per cadenes de caràcters variables).

- **Gestió d'excepcions:** És obligatori que totes les excepcions es tractin amb `try-catch` i cadascuna amb el seu propi bloc. Excepcions clau:
    
    - `IOException` (Broken pipe): No s'ha pogut escriure perquè l'altra part s'ha desconnectat.
        
    - `SocketException`: El socket propi està tancat, no s'hi pot accedir o no es pot crear.
        
    - `InterruptedIOException`: S'ha excedit el temps d'espera (Timeout).
        
    - `ProtocolException`: Problemes a la capa de TCP.
        
## **Timeouts i Cicles de Vida (Threads i Sockets):**
El bloc `finally` s'ha d'usar sempre per tancar els sockets, independentment de si hi ha hagut error o no. 

- Tot socket que realitzi un `read` ha de tenir un TimeOut per detectar fallades, però el temps no ha de ser massa elevat. 

>[!tip] Revisa i Implementa
> Si el programa espera de manera natural que el client trigui, en saltar el TimeOut s'hauria de comprovar si l'stream d'entrada està `available` i llavors tornar a llegir. 

- Finalment, els threads han d'acabar-se de forma natural i sempre han de tancar els sockets oberts abans de fer-ho.

