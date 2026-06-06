## 1. Context i Exemples

- **Definició bàsica:** Sistemes on ordinadors independents col·laboren per a una tasca comuna.
- **Exemples quotidians:**
    - Aplicacions web (Banca, Google), Jocs _Multiplayer_ (MMOGs, Casinos), Comunicacions (Skype, Whatsapp), Streaming i P2P (Spotify, Netflix, Torrent).
    
- **Tendències tecnològiques:**
     **Accés universal:** Internet of Things (IoT), **Mobilitat:** Computació ubiqua i mòbil, Multimèdia:** Sistemes distribuïts per a contingut audiovisual, **Cloud Computing:** SaaS (_Software As A Service_) i serveis de maquinari

---

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

## 4. Middleware i Tecnologies


**Definició de Middleware:** Capa que ofereix un alt nivell d'abstracció per desenvolupar aplicacions distribuïdes.

### A. Evolució de Tecnologies

1. **RPC (Remote Procedure Calls):**
    
    - _No OO (orientat objectes):_ 
	    - Crides a procediments en altres màquines.
        
    - _OO (Finals '80):_ 
	    - Invocació de mètodes en objectes remots.
        
	    - **Objectes Distribuïts:** Tots els objectes són clients i servidors alhora.
        
2. **Tecnologies d'Objectes Distribuïts (Comparativa):**
    
    - **RMI (Remote Method Invocation):** 
	    - Independent del SO, però **dependent del llenguatge (Java)**.
        
    - **DCOM(Distribuited Component Object Model):** 
	    - **Dependent del SO (Windows)**, però independent del llenguatge (C, C++, VB).
        
    - **CORBA(Common Object Request Broker Architecture):** 
	    - Independent tant del SO com del llenguatge.
        
3. **Components Distribuïts (Finals '90):**
    
    - Els objectes passen a ser components dins d'un **Servidor d'Aplicacions** (contenidor).
        
    - **Avantatges:** Persistència, transaccions i cicle de vida automàtics.
        
    - **Plataformes:**
        
        - **J2EE:** Usa JSP i Servlets.
            
        - **Windows DNA:** Usa ASP.
            
4. **Serveis Web (Actualitat):**
    
    - Comunicació via **HTTP**.
        
    - Crides remotes: **SOAP, XML-RPC, RESTful**.
        
    - Descripció del servei: **WSDL**.
        
    - Directori de serveis: **UDDI** (Universal Description Discovery and Integration).
        

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


