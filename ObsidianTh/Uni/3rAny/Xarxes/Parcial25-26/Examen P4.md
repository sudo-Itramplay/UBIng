Aquí tens la transcripció de les teves notes manuscrites (fitxer _2a part - Cisco..._). He utilitzat l'informe _Xarxes_P4.pdf_ per desambiguar certs termes i fragments on la cal·ligrafia era ràpida, assegurant que la sintaxi de les comandes Cisco i els conceptes teòrics siguin correctes.

Està estructurat en format Obsidian per a la teva base de coneixement.

---

# Apunts: Protocol DHCP i Configuració Cisco

## 1. Conceptes Bàsics DHCP

- **Funció:** Evita haver de configurar manualment cada dispositiu.
    
- **Objectiu:** Permet que els dispositius (clients) obtinguin automàticament:
    
    - Adreça IP.
        
    - Màscara de subxarxa.
        
    - Porta d'enllaç (Gateway).
        
    - Servidors DNS.
        
- **Capa:** Aplicació1.
    
- **Transport:** Utilitza **UDP** (User Datagram Protocol) en lloc de TCP.
    
- **Ports:**
    
    - Servidor: **67**2.
        
    - Client: **68**3.
        

---

## 2. Funcionament: El Procés DORA

L'assignació d'IP segueix el procés conegut com a **DORA**4:

### 1. **D**iscover

- **Estat:** No tenim IP assignada.
    
- **Acció:** El client envia un paquet `DHCPDISCOVER`.
    
- **Mètode:** Utilitza adreces de difusió (_broadcast_) perquè no sap on és el servidor5.
    

### 2. **O**ffer

- **Acció:** El servidor DHCP rep el missatge i envia un `DHCPOFFER`6.
    
- **Contingut:** Inclou una proposta amb:
    
    - La IP oferta.
        
    - La màscara de subxarxa7.
        
    - La IP del servidor DHCP.
        

### 3. **R**equest

- **Context:** Si hi ha diversos servidors, podem rebre diversos _Offers_. N'escollim un.
    
- **Acció:** El client envia un `DHCPREQUEST`.
    
- **Funció:**
    
    - Acceptar l'oferta.
        
    - Establir la "voluntat del lease" (temps de concessió)8.
        
    - Retornar les ofertes no volgudes al _pool_ de disponibles9.
        

### 4. **A**cknowledge

- **Acció:** El servidor envia un `DHCPACK`.
    
- **Resultat:** Finalitza el procés i la configuració s'aplica al client10.
    

---

## 3. Configuració en Router Cisco

Per configurar el servei DHCP en un router (actuant com a servidor), primer cal configurar la interfície del propi router com a porta d'enllaç estàtica.

### Configuració de la Interfície

Bash

```
Router> enable
Router# configure terminal
Router(config)# interface FastEthernet 0/0
Router(config-if)# ip address 192.168.0.254 255.255.255.0
Router(config-if)# no shutdown
Router(config-if)# exit
```

### Configuració del Servei DHCP

1. Reservar adreces (Excluded Addresses):
    
    Es reserven IPs per a dispositius estàtics (servidors, impressores, altres routers).
    
    Bash
    
    ```
    ip dhcp excluded-address 192.168.0.1 192.168.0.10
    ```
    
    [Nota: Això coincideix amb la Q7 de l'informe P4 11]
    
2. **Definir el Pool DHCP:**
    
    Bash
    
    ```
    ip dhcp pool XARXA-FA0-0
    ```
    
3. **Paràmetres del Pool:**
    
    Bash
    
    ```
    network 192.168.0.0 255.255.255.0
    default-router 192.168.0.254
    ```
    

---

## 4. Adreçament i Subnetting

### Anàlisi d'una xarxa /24

- **Prefix de màscara:** $/24$.
    
- **Significat:**
    
    - 24 bits per identificar la xarxa (Network).
        
    - Els bits restants identifiquen els Hosts.
        
- Càlcul d'Hosts:
    
    $$32 \text{ (total)} - 24 \text{ (xarxa)} = 8 \text{ bits per host}$$
    
    $$2^8 = 256 \text{ adreces totals}$$
    
- **Representació de la màscara:** `255.255.255.0` (els tres primers octets són 11111111 en binari)12.
    
- **Rang:** De `192.168.0.0` a `192.168.0.255` (on la última és l'adreça de _broadcast_).
    

### Subnetting (Divisió de Subxarxes)

- **Exemple:** Dividir la xarxa `192.168.2.0/24` en **2 subxarxes**.
    
- **Nova màscara:** $/25$ (prenem 1 bit prestat a la part de host).
    
    - Això divideix el rang en dos blocs de 128 adreces ($2^7 = 128$).
        

Esquema de la divisió13131313:

1. **Subxarxa A (Inferior):**
    
    - Xarxa: `192.168.2.0/25`
        
    - Rang usable: `.1` a `.126`
        
2. **Subxarxa B (Superior):**
    
    - Xarxa: `192.168.2.128/25`
        
    - Rang usable: `.129` a `.254`
        

- **Aplicació pràctica (referència a l'informe):**
    
    - Es configura `FastEthernet 0/0` per a una subxarxa.
        
    - Es configura `FastEthernet 1/0` per a l'altra subxarxa (o una xarxa diferent com `192.168.1.0/24` segons l'esquema de la pàgina 5).
        

---

**Vols que generi una taula comparativa entre la configuració teòrica d'aquests apunts i la implementació final que vas fer a l'informe P4 per veure si hi ha discrepàncies?**