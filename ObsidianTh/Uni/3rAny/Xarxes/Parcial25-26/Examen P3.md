# Quina és la funció de la interfície fast ethernet en un router cisco dins el simulador cisco packet tracer?

Dins de **Cisco Packet Tracer** (i en equips reals), aquesta interfície actua com a porta d'enllaç o **Gateway**.

- **Definició:** És un port físic de capa 3 ([[Model OSI]]) dissenyat per transmetre dades a una velocitat de **100 Mbps**.
    
- **Funció Principal:** Connectar el router amb una xarxa d'àrea local ([[LAN]]) o amb un altre router.
    
- **Requisit Crític:** A diferència dels switchos, en els routers Cisco les interfícies venen "apagades" per defecte. Cal configurar-hi una [[Adreça IP]] i aixecar-la amb la comanda `no shutdown`.
    


DEFINEIX EL NUMERO DE Dispositius QUE Poden conectar-se via ethernet (en el cas de la pràctica)
Aquest s'encarrega de transmetre les dades d'anada i tornada 

> [!NOTE] Nota del Professor 
> Avui dia, FastEthernet (100Mbps) està sent substituït per **GigabitEthernet** (1000Mbps), però la lògica de configuració és idèntica.







# Quina comanda permet verificar a connectivitat entre dos ordinadors dins els simulador?
-->Ping

# Què indica el triangle vermell a les connexions del simulador?

#### 2. El Triangle Vermell

Aquest indicador visual en la topologia del Packet Tracer assenyala l'estat de l'enllaç (**Link Status**).

- **Significat:** L'enllaç està **DOWN**. No hi ha comunicació de capa 1 (física) o capa 2 (enllaç de dades).
    
- **Causes habituals:**
    
    1. **Interfície administrativa apagada:** Com he esmentat abans, oblidar la comanda `no shutdown` al router.
        
    2. **Cable incorrecte:** Utilitzar un cable directe quan cal un creuat (o viceversa).
        
    3. **Dispositiu apagat:** Un dels extrems no té corrent.




# Quina diferència hi ha entre connexió UTP i UTP creuada?

La necessitat de cable directe o creuat depèn de com està configurada la targeta de xarxa (NIC) de cada dispositiu. Existeixen dos tipus de configuració de ports:

1. **MDI (Media Dependent Interface):** Transmeten pels pins 1 i 2. Reben pels 3 i 6.
    
    - _Dispositius:_ PC, Router, Servidor.
        
2. **MDI-X (Media Dependent Interface Crossover):** Tenen el creuament fet internament. Reben pels pins 1 i 2. Transmeten pels 3 i 6.
    
    - _Dispositius:_ Switch, Hub.
        

---

#### Regles de connexió física

L'objectiu és connectar sempre els pins de **Transmissió (TX)** d'un costat amb els de **Recepció (RX)** de l'altre.

**1. Connexió Dispositius Diferents (MDI ↔ MDI-X)**

- **Escenari:** PC (MDI) connectat a Switch (MDI-X).
    
- **Cable:** **Directe** (Straight-through).
    
- **Motiu:** Els pins ja estan alineats. El PC envia per l'1 i el 2; el Switch escolta per l'1 i el 2. El cable no ha de modificar res.
    

**2. Connexió Dispositius Iguals (MDI ↔ MDI o MDI-X ↔ MDI-X)**

- **Escenari:** Router connectat a Router, o PC connectat a PC.
    
- **Cable:** **Creuat** (Crossover).
    
- **Motiu:** Ambdós dispositius transmeten pels mateixos pins (1 i 2). Si uses un cable directe, la transmissió xoca (TX contra TX). El cable ha de creuar físicament els fils perquè el TX d'un extrem vagi al RX de l'altre.





# Quina és la funció d'un switch en una xarxa d'area local?
-->Commutar trames a nivell de MAX i augmentar velocitat de xarxa

