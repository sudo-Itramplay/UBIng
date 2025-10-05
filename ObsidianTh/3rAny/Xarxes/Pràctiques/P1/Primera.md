
ip pública vol dir que amb aquesta accedeixes a internet
	IPv4
ip privada són les 192


## Part 1

- Si esteu fent servir Linux, la comanda ip correspon a les actualitzacions de kernel i
el moviment gradual que es produeix per impulsar les IoT a través de netlink.

- Ip ens permet veure també les propietats de les diferents interfícies amb la
comanda:

```
ip link show


1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
2: eno2: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc fq_codel state DOWN mode DEFAULT group default qlen 1000
    link/ether 50:eb:f6:da:63:55 brd ff:ff:ff:ff:ff:ff
    altname enp0s31f6
    altname enx50ebf6da6355
3: wlo1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP mode DORMANT group default qlen 1000
    link/ether c2:5a:ff:82:ec:3c brd ff:ff:ff:ff:ff:ff permaddr bc:09:1b:d6:e7:37
    altname wlp0s20f3
    altname wlxbc091bd6e737
```

### Apunts
Porta d'enllaç i ma
scara
	mascara és per identificar quin és el tros adreça que correspon a xarxa o interfície
	- 255 està en binari -> correspon a 1
	es fa and entre mascara   i porta
Adressa física és la MAC
ip és adreça lògica

#### JAJA
```
També es poden pujar o baixar interfícies de manera similar a ifconfig eth0 up o
ifconfig eth0 down simplement fent servir:


>>ip link set DEVICE up o ip link set DEVICE down

```
## Segona Part
[[Mascara]]


161 passa a binari 10
	(192 si estàs amb wifi privada)
	
La classe A té un 255.0.0.0
La classe B : 255.255.0.0
La classe C: 255255.255.0

Adreça classe B amb mascara classe C
	S ha fet subneting

Amb classe C agafem fins el 3r punt
161.116.52.84 -> 161.115.52
DHCP és l'adreça associada a la xarxa

DHCP és l'adreça del servidor- és un sistema amb memòria

Assignem les adreces 10.0.0.1 i 10.0.0.2. La
màscara serveix per identificar l’adreça de xarxa. Això es fa fent una AND de la
màscara i la IP que tenim. En aquest cas és senzill:

10.0.0.2 AND 255.0.0.0 = 10.0.0.0
	que és l’adreça associada a la xarxa, per tant, el nostre ordinador serà el 0.0.2

## Q1
### Enunciat
Feu servir per identificar la vostra adreça IP la comanda abans esmentada.
Normalment, aquesta IP no és una IP pública, sinó que és privada. Identifiqueu
si la IP que surt en el vostre PC és pública o privada fent una cerca a Internet i
indiqueu quines IPs són privades.
• Hi ha un protocol que s’encarrega de “traduir” la IP privada en una IP
pública. Aquest protocol s’anomena NAT. Busqueu la definició de NAT i
expliqueu breument com funciona.
Un altra comanda que pot ser interessant de testejar es netstat. Netstat s’obté de
les paraules NETwork i STATistics. Ofereix estadístiques bàsiques sobre totes les

### Resposta
La meva ip es troba fent:
```
ip address show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host noprefixroute 
       valid_lft forever preferred_lft forever
2: eno2: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc fq_codel state DOWN group default qlen 1000
    link/ether 50:eb:f6:da:63:55 brd ff:ff:ff:ff:ff:ff
    altname enp0s31f6
    altname enx50ebf6da6355
3: wlo1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
    link/ether c2:5a:ff:82:ec:3c brd ff:ff:ff:ff:ff:ff permaddr bc:09:1b:d6:e7:37
    altname wlp0s20f3
    altname wlxbc091bd6e737
    inet 10.111.151.111/17 brd 10.111.255.255 scope global dynamic noprefixroute wlo1
       valid_lft 1546sec preferred_lft 1546sec
    inet6 fe80::ea3:7d41:ba00:390e/64 scope link noprefixroute 
       valid_lft forever preferred_lft forever
```

Per tant->10.111.151.111, ja que estic conectat per wifi

## Seguim pdf

Un altra comanda que pot ser interessant de testejar es netstat. Netstat s’obté de
les paraules NETwork i STATistics. Ofereix estadístiques bàsiques sobre totes les
activitats de la xarxa i informa els usuaris sobre quins ports i adreces s’executen
les connexions corresponents (TCP, UDP) i quins ports estan oberts per a tasques.

```
netstat -nat -n
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State      
tcp        0      0 0.0.0.0:5355            0.0.0.0:*               LISTEN     
tcp        0      0 127.0.0.1:631           0.0.0.0:*               LISTEN     
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN     
tcp        0      0 127.0.0.54:53           0.0.0.0:*               LISTEN     
tcp        0      0 127.0.0.1:5054          0.0.0.0:*               LISTEN     
tcp        0      0 10.111.151.111:59374    34.107.243.93:443       ESTABLISHED
tcp6       0      0 :::5355                 :::*                    LISTEN     
tcp6       0      0 ::1:631                 :::*                    LISTEN  
```



## Q2
### Enunciat
En funció del router que ens proporciona la IP, és possible també que aquesta
sigui volàtil. Doneu una ullada al panel de control, i busqueu com teniu configurada
la vostra IP. Descriviu breument el que trobeu. (help: DHCP?

## Resposta


#### Configuració de la IPv4

- **Adreça IP:** 10.111.151.111
    
- **Màscara de subxarxa (Prefix):** /17 (Això es tradueix en una màscara de subxarxa de 255.255.128.0)
    
- **Adreça de Broadcast:** 10.111.255.255
    
- **Àmbit (Scope):** `global dynamic noprefixroute` (És una adreça assignada dinàmicament i accessible a la xarxa global).
    
- **Temps de vida vàlid (Valid Lifetime):** 1248 segons.
    
- **Temps de vida preferit (Preferred Lifetime):** 1248 segons.
    

---

#### Configuració de la IPv6

- **Adreça IP (Link-Local):** fe80::ea3:7d41:ba00:390e/64
    
- **Àmbit (Scope):** `link noprefixroute` (És una adreça local del segment, utilitzada per a comunicacions dins de la mateixa xarxa local).
    
- **Temps de vida vàlid i preferit:** `forever` (Són adreces permanents mentre la interfície estigui activa).
    

---

#### Configuració de la Interfície (`wlo1`)

- **Nom de la interfície:** `wlo1` (és una interfície **sense fil** o **Wi-Fi** com suggereix la 'w').
    
- **Estat:** **`UP`** (Activa i funcionant).
    
- **Adreça MAC (Hardware Address):** c2:5a:ff:82:ec:3c
    
- **MTU (Maximum Transmission Unit):** 1500
    

En resum, tens una adreça IP **privada** (10.x.x.x) assignada **dinàmicament** (mitjançant DHCP) a la teva targeta Wi-Fi.

En cas que la IP sigui volàtil provarem d’alliberar la IP actual. Per tal de fer això
fem:
• sudo dhclient -v -r eth0
• sudo dhclient -v eth0
Això el que fa és que, potser, al ser DHCP dinàmic, la ip pot canviar amb aquestes comandes, on la primera es desconecta i la seguent es reconecta

```
sudo dhclient -v -r wlo1
[sudo] contraseña para itramplay: 
Internet Systems Consortium DHCP Client 4.4.3-P1
Copyright 2004-2022 Internet Systems Consortium.
All rights reserved.
For info, please visit https://www.isc.org/software/dhcp/

Listening on LPF/wlo1/c2:5a:ff:82:ec:3c
Sending on   LPF/wlo1/c2:5a:ff:82:ec:3c
Sending on   Socket/fallback
```

```
sudo dhclient -v wlo1
Internet Systems Consortium DHCP Client 4.4.3-P1
Copyright 2004-2022 Internet Systems Consortium.
All rights reserved.
For info, please visit https://www.isc.org/software/dhcp/

Listening on LPF/wlo1/c2:5a:ff:82:ec:3c
Sending on   LPF/wlo1/c2:5a:ff:82:ec:3c
Sending on   Socket/fallback
DHCPDISCOVER on wlo1 to 255.255.255.255 port 67 interval 5 (xid=0xd9ff6a17)
DHCPOFFER of 10.111.167.253 from 10.111.255.254
DHCPREQUEST for 10.111.167.253 on wlo1 to 255.255.255.255 port 67 (xid=0xd9ff6a17)
DHCPACK of 10.111.167.253 from 10.111.255.254 (xid=0xd9ff6a17)
/usr/sbin/dhclient-script: line 706: /etc/resolv.conf: Permission denied
bound to 10.111.167.253 -- renewal in 741 seconds.
```

i ara si fem la funció d'abans
```
ip address show

#Borro les que no estic conectat

3: wlo1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
    link/ether c2:5a:ff:82:ec:3c brd ff:ff:ff:ff:ff:ff permaddr bc:09:1b:d6:e7:37
    altname wlp0s20f3
    altname wlxbc091bd6e737
    inet 10.111.151.111/17 brd 10.111.255.255 scope global dynamic noprefixroute wlo1
       valid_lft 1692sec preferred_lft 1692sec
    inet 10.111.167.253/17 brd 10.111.255.255 scope global secondary dynamic wlo1
       valid_lft 1831sec preferred_lft 1831sec
    inet6 fe80::ea3:7d41:ba00:390e/64 scope link noprefixroute 
       valid_lft forever preferred_lft forever
```
Segueixo igual

## Verificacions de ping

### Verificació del protocol intern del PC
Arribats a aquest punt podem mirar si el protocol TCP/IP que tenim instal·lat en el
nostre PC funciona correctament o hi ha algun problema a la nostra tarja de
connexió a la xarxa local (NIC). Per tal de veure això, farem primer una crida al
nostre servidor de DNS, o a la porta d’enllaç predeterminada que coneixem quan
fem ipconfig. Executem la comanda ping seguida de l’adreça IP, per exemple



➢ ping 161.116.95.254
En el meu cas:
ping 10.111.151.111

```
ping 10.111.151.111
PING 10.111.151.111 (10.111.151.111) 56(84) bytes de datos.
64 bytes desde 10.111.151.111: icmp_seq=1 ttl=64 tiempo=0.104 ms
64 bytes desde 10.111.151.111: icmp_seq=2 ttl=64 tiempo=0.106 ms
64 bytes desde 10.111.151.111: icmp_seq=3 ttl=64 tiempo=0.159 ms
64 bytes desde 10.111.151.111: icmp_seq=4 ttl=64 tiempo=0.110 ms
^C
--- 10.111.151.111 estadísticas ping ---
4 paquetes transmitidos, 4 recibidos, 0% packet loss, time 3095ms
rtt min/avg/max/mdev = 0.104/0.119/0.159/0.022 ms
```
## Q3
### Enunciat
Q3. Determineu si teniu connexió directa. 
Desconnecteu ara la vostra connexió a la LAN. Torneu a executar la instrucció. Què passa? Sense connectar el cable,
executeu ara el següent:
➢ ping 127.0.0.1
Expliqueu breument que és el que heu fet i que és aquesta IP. Busqueu què és
aquesta adreça i perquè serveix.

### Resposta
```
#Un cop desconectat
$ ping 10.111.151.111
ping: connect: La red es inaccesible
```

```
#amb la ip especificada
$ ping 127.0.0.1

PING 127.0.0.1 (127.0.0.1) 56(84) bytes de datos.
64 bytes desde 127.0.0.1: icmp_seq=1 ttl=64 tiempo=0.066 ms
64 bytes desde 127.0.0.1: icmp_seq=2 ttl=64 tiempo=0.087 ms
64 bytes desde 127.0.0.1: icmp_seq=3 ttl=64 tiempo=0.106 ms
64 bytes desde 127.0.0.1: icmp_seq=4 ttl=64 tiempo=0.102 ms
64 bytes desde 127.0.0.1: icmp_seq=5 ttl=64 tiempo=0.132 ms
^C
--- 127.0.0.1 estadísticas ping ---
5 paquetes transmitidos, 5 recibidos, 0% packet loss, time 4130ms
rtt min/avg/max/mdev = 0.066/0.098/0.132/0.021 ms

```

127.0.0.1 és una xarxa local "localhost" que serveix per provar si el software associat al protocol TCP/IP funciona correctament

### Verificació de la connexió amb l’exterior
Un cop verificat el funcionament intern, provem si la connexió amb l’exterior és
correcta. Accedirem a la pàgina de google per tal de fer la prova, tot i que es pot fer
amb qualsevol adreça IP. Farem un ping a l’adreça de google. Això el que fa és
enviar un senyal de ECO, que es reenviada per google fins a nosaltres i podem
veure el temps que triga en fer-se la connexió. En aquest cas fem:
➢ ping www.google.com

## Q4
### Enunciat
Q4. Verifiqueu que teniu resposta amb google. Quan triguen els paquets en fer tota
la ruta complerta (enviar ECO a google i detectar el retorn)? Raona la resposta.

### Resposta 1

#### comanda
```
ping www.google.com
PING www.google.com (142.250.200.68) 56(84) bytes de datos.
64 bytes desde mad07s24-in-f4.1e100.net (142.250.200.68): icmp_seq=1 ttl=119 tiempo=16.0 ms
64 bytes desde mad07s24-in-f4.1e100.net (142.250.200.68): icmp_seq=2 ttl=119 tiempo=16.8 ms
64 bytes desde mad07s24-in-f4.1e100.net (142.250.200.68): icmp_seq=3 ttl=119 tiempo=20.2 ms
64 bytes desde mad07s24-in-f4.1e100.net (142.250.200.68): icmp_seq=4 ttl=119 tiempo=12.5 ms
64 bytes desde mad07s24-in-f4.1e100.net (142.250.200.68): icmp_seq=5 ttl=119 tiempo=13.6 ms
64 bytes desde mad07s24-in-f4.1e100.net (142.250.200.68): icmp_seq=6 ttl=119 tiempo=13.3 ms
64 bytes desde mad07s24-in-f4.1e100.net (142.250.200.68): icmp_seq=7 ttl=119 tiempo=13.0 ms
64 bytes desde mad07s24-in-f4.1e100.net (142.250.200.68): icmp_seq=8 ttl=119 tiempo=14.1 ms
64 bytes desde mad07s24-in-f4.1e100.net (142.250.200.68): icmp_seq=9 ttl=119 tiempo=13.4 ms
64 bytes desde mad07s24-in-f4.1e100.net (142.250.200.68): icmp_seq=10 ttl=119 tiempo=13.8 ms
64 bytes desde mad07s24-in-f4.1e100.net (142.250.200.68): icmp_seq=11 ttl=119 tiempo=14.4 ms
64 bytes desde mad07s24-in-f4.1e100.net (142.250.200.68): icmp_seq=12 ttl=119 tiempo=14.0 ms
64 bytes desde mad07s24-in-f4.1e100.net (142.250.200.68): icmp_seq=13 ttl=119 tiempo=13.1 ms
64 bytes desde mad07s24-in-f4.1e100.net (142.250.200.68): icmp_seq=14 ttl=119 tiempo=14.0 ms
64 bytes desde mad07s24-in-f4.1e100.net (142.250.200.68): icmp_seq=15 ttl=119 tiempo=13.2 ms
64 bytes desde mad07s24-in-f4.1e100.net (142.250.200.68): icmp_seq=16 ttl=119 tiempo=13.0 ms
64 bytes desde mad07s24-in-f4.1e100.net (142.250.200.68): icmp_seq=17 ttl=119 tiempo=13.9 ms
64 bytes desde mad07s24-in-f4.1e100.net (142.250.200.68): icmp_seq=18 ttl=119 tiempo=14.0 ms
64 bytes desde mad07s24-in-f4.1e100.net (142.250.200.68): icmp_seq=19 ttl=119 tiempo=13.9 ms
64 bytes desde mad07s24-in-f4.1e100.net (142.250.200.68): icmp_seq=20 ttl=119 tiempo=13.8 ms
64 bytes desde mad07s24-in-f4.1e100.net (142.250.200.68): icmp_seq=21 ttl=119 tiempo=13.9 ms
64 bytes desde mad07s24-in-f4.1e100.net (142.250.200.68): icmp_seq=22 ttl=119 tiempo=13.4 ms
64 bytes desde mad07s24-in-f4.1e100.net (142.250.200.68): icmp_seq=23 ttl=119 tiempo=14.2 ms
64 bytes desde mad07s24-in-f4.1e100.net (142.250.200.68): icmp_seq=24 ttl=119 tiempo=13.1 ms
64 bytes desde mad07s24-in-f4.1e100.net (142.250.200.68): icmp_seq=25 ttl=119 tiempo=13.7 ms
64 bytes desde mad07s24-in-f4.1e100.net (142.250.200.68): icmp_seq=26 ttl=119 tiempo=13.2 ms
64 bytes desde mad07s24-in-f4.1e100.net (142.250.200.68): icmp_seq=27 ttl=119 tiempo=13.3 ms
64 bytes desde mad07s24-in-f4.1e100.net (142.250.200.68): icmp_seq=28 ttl=119 tiempo=13.4 ms
64 bytes desde mad07s24-in-f4.1e100.net (142.250.200.68): icmp_seq=29 ttl=119 tiempo=13.4 ms
64 bytes desde mad07s24-in-f4.1e100.net (142.250.200.68): icmp_seq=30 ttl=119 tiempo=13.6 ms
64 bytes desde mad07s24-in-f4.1e100.net (142.250.200.68): icmp_seq=31 ttl=119 tiempo=13.2 ms
64 bytes desde mad07s24-in-f4.1e100.net (142.250.200.68): icmp_seq=32 ttl=119 tiempo=13.5 ms
64 bytes desde mad07s24-in-f4.1e100.net (142.250.200.68): icmp_seq=33 ttl=119 tiempo=13.4 ms
64 bytes desde mad07s24-in-f4.1e100.net (142.250.200.68): icmp_seq=34 ttl=119 tiempo=13.2 ms
64 bytes desde mad07s24-in-f4.1e100.net (142.250.200.68): icmp_seq=35 ttl=119 tiempo=13.2 ms
64 bytes desde mad07s24-in-f4.1e100.net (142.250.200.68): icmp_seq=36 ttl=119 tiempo=12.8 ms
64 bytes desde mad07s24-in-f4.1e100.net (142.250.200.68): icmp_seq=37 ttl=119 tiempo=14.0 ms
64 bytes desde mad07s24-in-f4.1e100.net (142.250.200.68): icmp_seq=38 ttl=119 tiempo=12.5 ms
64 bytes desde mad07s24-in-f4.1e100.net (142.250.200.68): icmp_seq=39 ttl=119 tiempo=15.0 ms
64 bytes desde mad07s24-in-f4.1e100.net (142.250.200.68): icmp_seq=40 ttl=119 tiempo=13.1 ms
64 bytes desde mad07s24-in-f4.1e100.net (142.250.200.68): icmp_seq=41 ttl=119 tiempo=13.3 ms
64 bytes desde mad07s24-in-f4.1e100.net (142.250.200.68): icmp_seq=42 ttl=119 tiempo=13.1 ms
64 bytes desde mad07s24-in-f4.1e100.net (142.250.200.68): icmp_seq=43 ttl=119 tiempo=14.0 ms
64 bytes desde mad07s24-in-f4.1e100.net (142.250.200.68): icmp_seq=44 ttl=119 tiempo=13.2 ms
64 bytes desde mad07s24-in-f4.1e100.net (142.250.200.68): icmp_seq=45 ttl=119 tiempo=13.9 ms
64 bytes desde mad07s24-in-f4.1e100.net (142.250.200.68): icmp_seq=46 ttl=119 tiempo=13.9 ms
64 bytes desde mad07s24-in-f4.1e100.net (142.250.200.68): icmp_seq=47 ttl=119 tiempo=13.4 ms
^C
--- www.google.com estadísticas ping ---
47 paquetes transmitidos, 47 recibidos, 0% packet loss, time 46075ms
rtt min/avg/max/mdev = 12.488/13.782/20.204/1.209 ms
```

#### Raonament
La comanda `ping www.google.com` mesura el temps que triga un paquet ICMP (el paquet ECO) a arribar al destí (un servidor de Google) i el seu corresponent paquet de resposta ICMP (el retorn) a tornar a l'origen. Aquest és el **temps d'anada i tornada (RTT)**.

- A les línies de la sortida del ping, el temps per a cada paquet s'indica amb `tiempo=X.X ms`. Els valors observats estan majoritàriament al voltant de 13-14 ms.
    
- A la línia de resum final (`rtt min/avg/max/mdev`), s'indiquen els valors estadístics:
    
    - **Mínim (min):** 12.488 ms
        
    - **Mitjana (avg):** **13.782 ms** (Aquest és el valor més representatiu per a la pregunta).
        
    - **Màxim (max):** 20.204 ms
        

Per tant, es pot concloure que, de mitjana, un paquet triga uns **13.8 ms** a arribar a Google i tornar.



Fins ara hem vist com el servidor (en aquest cas google) respon a la nostra petició de ping. Es possible però que ens interessi conèixer per on han anat passant els
paquets, es a dir, la ruta que segueix el datagrama fins arribar a google. Per tal de veure això hem d’utilitzar una nova comanda: tracert.

➢ traceroute www.google.com

```
traceroute www.google.com
traceroute to www.google.com (142.250.200.68), 30 hops max, 60 byte packets
 1  _gateway (10.111.255.254)  3.961 ms  5.069 ms  6.502 ms
 2  * * *
 3  * * *
 4  * * *
 5  * * *
 6  * * *
 7  * * *
 8  mad07s24-in-f4.1e100.net (142.250.200.68)  13.176 ms  13.002 ms  13.110 ms
```

## Q5
### Enunciat
Q5. Indiqueu per quines adreces públiques circulen els datagrames. Apareix el
símbol “*”? Que indica?

### Resposta
La comanda `traceroute` mostra la llista d'encaminadors (routers) pels quals passen els paquets des de l'origen fins al destí (Google). Aquesta llista, excepte la primera adreça, són les **adreces IP públiques** per on circulen els datagrames.

#### Adreces Públiques

Les adreces públiques per on circulen els datagrames (després del primer salt, que és l'encaminador privat de la teva xarxa) són les corresponents als salts amb una adreça IP visible abans d'arribar al destí final:

1. **Salt 8 (Destí):** **142.250.200.68** (Que es resol com `mad07s24-in-f4.1e100.net`, un servidor de Google a Madrid - **mad**)
    

**Nota:** Els salts 2 a 7 no mostren una adreça IP pública a causa dels asteriscos.

#### Símbol "*" i la seva Indicació

Sí, el símbol `*` (asterisc) **apareix** a la sortida de `traceroute` als salts **2, 3, 4, 5, 6 i 7**.

#####
Què indica l'asterisc (∗)?

El símbol `*` indica un **temps d'espera esgotat (timeout)** ⏳ per a un o més paquets de sonda (tres per a cada salt) enviats al router d'aquell salt.

Això pot indicar que:

1. **L'encaminador (router) d'aquest salt no ha respost** al paquet de sonda ICMP (que és com `traceroute` rastreja la ruta).
    
2. **L'encaminador està configurat per no respondre** a peticions ICMP per motius de seguretat o política de xarxa (és la raó més freqüent en xarxes d'operadors grans).
    
3. **El paquet de resposta de l'encaminador s'ha perdut** en el camí de tornada.
    
4. **L'encaminador està saturat** i no prioritza la resposta al paquet de sonda.
    

En aquest cas, la presència de sis asteriscos consecutius (salts 2 a 7) és **típic** i gairebé segur que indica que els proveïdors de serveis d'Internet (ISPs) tenen els seus encaminadors de trànsit **configurats per no respondre** als paquets de sonda de `traceroute` (ICMP Time Exceeded) per protegir la seva infraestructura. Malgrat no respondre, el trànsit continua circulant a través d'aquests encaminadors.



## Coneixement de l’entorn proper
El nostre ordinador es connecta a la xarxa a través d’una xarxa cablejada Ethernet
o bé a través d’una xarxa sense fils WiFi. En els dos casos, fem servir un protocol de
l’estil 802.x on s’han d’especificar les adreces MAC del PC origen i destí.

## Q6
### Enunciat
Què és una adreça MAC? Puc tenir adreça MAC i no adreça IP? Raona la
resposta
Feu servir la comanda ipconfig per identificar la vostra adreça MAC. Quants bits té? 


---> Per fer qualsevol connexió amb un altre PC,
que estigui a la nostra xarxa local o en qualsevol altre lloc, necessitarem dos
adreces IP (origen i destí) i dos adreces MAC, especificades al protocol 802.x.
### Respostes
 Per tenir adreça MAC necessito tenir una interfície de xarxa, si aquesta no està conectada puc no tenir ip a cap xarxa
 igualment localhost, segons hem vist abans sempre és una ip que tenim "executatnt" pper tant entenc que no
 ```
 ~$ arp -a
_gateway (192.168.1.1) at cc:58:30:70:76:40 [ether] on wlo1
android-2.home (192.168.1.44) at 66:a0:b9:43:d3:10 [ether] on wlo1
 ```
```
arp –s
–s: Nombre de `host' no encontrado
```


## Q7


### Respostes

Un cop executada
```
arp -h
```
ens dona de sortida
```
arp -h
Usage:
  arp [-vn]  [<HW>] [-i <if>] [-a] [<hostname>]             <-Display ARP cache
  arp [-v]          [-i <if>] -d  <host> [pub]               <-Delete ARP entry
  arp [-vnD] [<HW>] [-i <if>] -f  [<filename>]            <-Add entry from file
  arp [-v]   [<HW>] [-i <if>] -s  <host> <hwaddr> [temp]            <-Add entry
  arp [-v]   [<HW>] [-i <if>] -Ds <host> <if> [netmask <nm>] pub          <-''-

        -a                       display (all) hosts in alternative (BSD) style
        -e                       display (all) hosts in default (Linux) style
        -s, --set                set a new ARP entry
        -d, --delete             delete a specified entry
        -v, --verbose            be verbose
        -n, --numeric            don't resolve names
        -i, --device             specify network interface (e.g. eth0)
        -D, --use-device         read <hwaddr> from given device
        -A, -p, --protocol       specify protocol family
        -f, --file               read new entries from file or from /etc/ethers

  <HW>=Use '-H <hw>' to specify hardware address type. Default: ether
  List of possible hardware types (which support ARP):
    ash (Ash) ether (Ethernet) ax25 (AMPR AX.25) 
    netrom (AMPR NET/ROM) rose (AMPR ROSE) arcnet (ARCnet) 
    dlci (Frame Relay DLCI) fddi (Fiber Distributed Data Interface) hippi (HIPPI) 
    irda (IrLAP) x25 (generic X.25) infiniband (InfiniBand) 
    eui64 (Generic EUI-64) 
```

Per lo que entenc que, per eliminar totes les entrades, seria tal que:
```
arp -d *
```

*Explicació*:
- El teu PC utilitza el protocol **ARP** (Address Resolution Protocol) per preguntar: "Qui té la IP del router (ex: `192.168.1.1`)?"

- El router respon amb la seva adreça MAC.

- Aquest parell **IP → MAC** es guarda a la **Taula ARP** del teu PC per a ús futur (entrada dinàmica).

Passos per trobar mac router:
1. `ip route`
	1. **Busca:** La línia que comença amb **`default`**.
 	_Exemple:_ `default via **192.168.1.1** dev enp0s3...`
 2. `ip neighbour show 192.168.1.1`
```
> _Exemple de sortida:_ `192.168.1.1 dev enp0s3 **lladdr 00:0a:95:9d:68:16** PERMANENT` **MAC del Router:** `00:0a:95:9d:68:16`
```


També es podia fer:
`ip neighbour show   # (Recomanat a Fedora)
	Opcional (Comanda clàssica): arp -a



->
El nombre d'entrades variarà en funció de l'activitat recent de la teva xarxa. Normalment, sempre hi ha com a mínim:

1. L'entrada del **Router/Passarel·la per Defecte**.
    
2. L'entrada d'altres equips amb els quals hagis comunicat recentment a la teva Xarxa Local (LAN).
    

_Després d'executar la comanda, simplement **compta les línies** que representen un veí actiu._


->
La comanda `arp -d *` que esborra totes les entrades és específica de Windows. A Linux, la manera de buidar una taula de veïns (ARP) és amb la comanda `ip neighbour flush all`.



Quan esborres la Taula ARP:

- **Pèrdua de Resolució:** El teu sistema perd el coneixement immediat de les adreces MAC de tots els dispositius propers, inclòs el router.
    
- **Restauració:** Quan intentes accedir a Internet (per exemple, fent un `ping 8.8.8.8`), el sistema ha de realitzar un nou procés **ARP Request** per tornar a descobrir la MAC del router.
    
- **Resultat:** La comunicació es retarda lleugerament la primera vegada, ja que es produeix aquesta nova resolució d'adreces, però la taula es torna a omplir **dinàmicament** immediatament amb les entrades que es necessiten


Un cop borrada la MAC, per asegurar :
`ping -c 1 192.168.1.1`

Consultem
`ip neighbour show 192.168.1.1`