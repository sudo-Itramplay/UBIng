
## 2 preguntes sobre capes tcp

Hola. Com a professor, m'agrada veure interès en l'arquitectura fonamental de les xarxes. Aquests models no són només teoria; són el llenguatge universal que permet que internet funcioni.

Aquí tens l'explicació estructurada com a apunts tècnics per a la teva base de coneixement (Obsidian).

---

# 🖧 Arquitectura de Xarxes: OSI vs. TCP/IP

Etiquetes: #xarxes #arquitectura #OSI #TCPIP #protocols

Data: 2025-11-21

## 1. El Model OSI (Open Systems Interconnection)

Aquest és el model teòric de referència (estàndard ISO). Divideix la comunicació en 7 capes d'abstracció.

> [!INFO] Regla mnemotècnica
> 
> "All People Seem To Need Data Processing" (Application, Presentation, Session, Transport, Network, Data Link, Physical).

|**Capa**|**Nom**|**PDU (Unitat de Dades)**|**Funció Principal**|
|---|---|---|---|
|**7**|**Aplicació**|Dades|Interfície amb l'usuari (HTTP, FTP, SMTP). On interactues amb la xarxa.|
|**6**|**Presentació**|Dades|Traducció de formats, xifratge i compressió (ex: convertir ASCII a EBCDIC, SSL/TLS).|
|**5**|**Sessió**|Dades|Estableix, gestiona i tanca sessions entre aplicacions (control de diàleg).|
|**4**|**Transport**|**Segment** (TCP) / Datagrama (UDP)|Fiabilitat extrem a extrem, control de flux i multiplexació (Ports).|
|**3**|**Xarxa**|**Paquet**|Enrutament lògic i direccionament (IP). Determina el millor camí a través de la xarxa.|
|**2**|**Enllaç de Dades**|**Trama** (Frame)|Accés al mitjà físic, direccionament físic (MAC) i detecció d'errors local.|
|**1**|**Física**|**Bit**|Transmissió binària (senyals elèctrics, llum, ràdio) a través del cable o medi.|

---

## 2. El Model TCP/IP (Internet Protocol Suite)

Aquest és el model pràctic que s'implementa realment a Internet. És més compacte i agrupa algunes capes de l'OSI.

![Imagen de OSI vs TCP/IP model comparison diagram](https://encrypted-tbn1.gstatic.com/licensed-image?q=tbn:ANd9GcQhEVpr2F56ZZNLGXZ33l8hZmgVR6-7-AisSF4iqlhBKrMhgDExwrrb_W8u4tU4MU0IHn9EDT7JR-VCm5OborLO3J0mApHoSnEF70jzjlyolbxjsK4)

Shutterstock

L'estructura (normalment de 4 capes) és:

1. **Capa d'Aplicació (Capa 4 TCP/IP):**
    
    - Engloba les capes OSI 5, 6 i 7 (Sessió, Presentació, Aplicació).
        
    - Tots els protocols d'alt nivell viuen aquí (HTTP, DNS, SSH).
        
2. **Capa de Transport (Capa 3 TCP/IP):**
    
    - Equivalent directe a la capa 4 de l'OSI.
        
    - Gestiona la comunicació Host-to-Host (TCP, UDP).
        
3. **Capa d'Internet (Capa 2 TCP/IP):**
    
    - Equivalent a la capa 3 de l'OSI (Xarxa).
        
    - El protocol rei és l'IP (Internet Protocol).
        
4. **Capa d'Accés a la Xarxa (Capa 1 TCP/IP):**
    
    - Combina les capes 1 i 2 de l'OSI (Física i Enllaç).
        
    - No defineix protocols estrictes, sinó com connectar-se al mitjà (Ethernet, Wi-Fi).
        

---

## 3. Anàlisi: Relació entre Enllaç (L2) i Transport (L4)

Aquesta és la part crítica on molts estudiants es confonen. La diferència clau és l'**abast** de la responsabilitat.

### A. El Concepte: Hop-by-Hop vs. End-to-End

- **Capa d'Enllaç (L2) → Hop-by-Hop (Salt a Salt):**
    
    - La seva feina és moure la informació d'un dispositiu al _següent_ dispositiu immediatament connectat (ex: del teu PC al Router de casa).
        
    - No li importa el destí final, només el següent salt.
        
    - Utilitza adreces **MAC**.
        
    - _Analogia:_ El camió que porta un paquet del magatzem de Barcelona al magatzem de Madrid. Només es preocupa d'arribar a Madrid.
        
- **Capa de Transport (L4) → End-to-End (Extrem a Extrem):**
    
    - La seva feina és garantir que les dades arribin des de l'origen fins al destí final, sense importar quants routers (salts) hi hagi entremig.
        
    - Ignora els detalls físics del camí.
        
    - Utilitza **Ports** per saber a quina aplicació entregar les dades.
        
    - _Analogia:_ El cap de logística que verifica que el paquet enviat pel client A ha arribat intacte al client B, encara que hagi passat per 5 camions diferents.
        

### B. La Cooperació

Si la capa d'Enllaç detecta un error (ex: interferència al cable), normalment descarta la trama (o demana reenviament local). Si la trama es descarta, la capa de Transport (TCP) a l'extrem final se n'adonarà que falta un tros de l'arxiu i demanarà el reenviament des de l'origen.

> [!SUMMARY] Resum per a examen
> 
> - **Enllaç:** Responsable del camí físic immediat (cable).
>     
> - **Transport:** Responsable de la conversa lògica completa.
>     

---

## Problema

Què és dbi? max vel


## crc
