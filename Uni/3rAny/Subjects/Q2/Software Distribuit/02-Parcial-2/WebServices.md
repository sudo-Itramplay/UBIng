## 1. Introducció als Web Services

Els Web Services representen l'evolució dels objectes distribuïts aplicada a l'escala global d'Internet.


>[!info] Extres: **Paradigmes de Programació Distribuïda**: 
>S'emmarquen dins d'una jerarquia que inclou el pas de missatges, arquitectures client-servidor, aplicacions web (MVC sobre HTTP), RMI/RPC i sistemes P2P .
>
   
- **Definició**: Proveeixen una interfície de servei equivalent a objectes distribuïts sobre el web, garantint la interoperabilitat total a Internet .
    
- **Ús i Propòsit**: Són essencials per a la integració B2B (_business-to-business_) i actuen com a _middleware_ per al _Cloud Computing_ .
    
- **Accés**: No estan dissenyats per a ser accedits directament per usuaris via navegador, sinó per aplicacions client dedicades.

#### Creació: 
- **Components de Disseny**: Al crear-los, s'ha d'especificar:
- la representació de dades (JSON, XML, SOAP), 
- la descripció del servei (WSDL, API), 
- el directori de serveis (UDDI) 
- el protocol d'accés (HTTP, TCP) .
    
- **Arquitectures Principals**: Destaquen XML-RPC, SOAP+WSDL i, sobretot, l'estil RESTful .
    

## 2. RESTful Web Services

REST (_Representational State Transfer_) no és un protocol, sinó un estil d'arquitectura que aprofita les capacitats nadiues de l'HTTP.
![[Pasted image 20260418100232.png]]

- **Filosofia**: Es basa en una aproximació amb un estil d'operacions molt restrictiu on s'emfatitza la manipulació dels recursos .
    
- **Principis Bàsics**:
    
    - Ús explícit dels mètodes HTTP.
        
    - Independència d'estats (_Stateless_).
        
    - URIs estructurades com directoris.
        
    - Transferència de dades en XML o JSON.
        
- **Mètodes HTTP Explícits**:
    
    - **GET**: Recuperar un recurs (segur i idempotent).
        
    - **POST**: Crear un nou recurs (no és idempotent).
        
    - **PUT**: Actualitzar o canviar l'estat d'un recurs (idempotent).
        
    - **DELETE**: Eliminar un recurs.
        
- **Exemple de flux**: Un recurs creat amb POST obté una nova URL, que després pot ser consultada amb GET o modificada amb PUT.
![[Pasted image 20260418100358.png]]



#### Exemples - POST

![[Pasted image 20260418100533.png]]

#### Exemples - PUT
![[Pasted image 20260418100607.png]]

## 3. El Servidor Stateless i el Sistema de Caché

L'escalabilitat de REST prové de traslladar la responsabilitat de l'estat al client i optimitzar la xarxa mitjançant cachés.

- **Disseny Stateless**: El servidor no manté sessions; cada petició ha de ser completa i independent.
    
- **Control de Caché**: El servidor utilitza capçaleres com `Cache-Control` per indicar si un recurs es pot guardar localment.
    
- **Paràmetres Clau**:
    
    - `max-age`: Temps en segons que el recurs és vàlid a la caché.
        
    - `Expires`: Data específica de caducitat.
        
- **Requests Condicionals**: Permeten estalviar amplada de banda preguntant si el recurs ha canviat.
    
    - **Time-based**: Ús de `Last-Modified` al servidor i `If-Modified-Since` al client. Si no ha canviat, el servidor respon amb un codi **304 Not Modified** .
        
    - **Content-based**: Ús d'**ETag** (un hash del contingut). El client envia `If-None-Match` per verificar si la versió local coincideix amb la del servidor .
        
![[Pasted image 20260418100754.png]]
## 4. Estructura de URIs i Representació de Recursos

La interfície ha de ser "neta" i les dades han de ser fàcilment processables per màquines.

- **URIs Intuïtives**: Han de ser directes, predictibles i evitar els _query strings_ (paràmetres `?id=...`) sempre que sigui possible.
    
- **Exemple de bona URI**: `http://www.myservice.org/discussion/2026/04/15/topic`.
    
- **Representació**: Reflecteix l'estat del recurs en el moment de la petició, normalment mitjançant JSON (`application/json`) o XML (`application/xml`) .
    
- **Llibreries**: Existeixen eines com GSON per passar d'objectes natius (com Java) a estructures JSON automàticament .
    

## 5. Gestió de Sessions i Limitacions HTTP

HTTP és un protocol _stateless_, però les aplicacions necessiten continuïtat (sessions).

- **El rastre de l'usuari**: El navegador ha de mantenir un identificador de sessió que el servidor pugui reconèixer .
    
- **Estratègies de Sessió**:
    
    - **Camps Ocults**: `<input type="hidden">`. Insegur, ja que és visible al codi font .
	    ![[Pasted image 20260418101148.png]] 
    - **Cookies**: Peça d'informació enviada pel servidor (`Set-cookie`) que el client torna a cada petició a una URL vàlida .
	    ![[Pasted image 20260418101208.png]]
        
    - **URL Rewriting**: Passar l'identificador com a paràmetre a cada enllaç. Si el client perd el paràmetre, perd la sessió .

>[!warning] SEGURETAT!
>Tots els sistemes anteriors són poc segurs, evita enviar informació compromerssa per mantenir la sessió, i fes-los que expirin (els id de sessió)

- **Seguretat**: Les dades de sessió poden ser manipulades o capturades si s'envien en text pla. És vital fer servir identificadors que expirin i no enviar mai informació sensible directament .
    

## 6. Autentificació: De l'Accés Bàsic al JWT

Com garantim que l'usuari és qui diu ser en un entorn distribuït.

- **Accés Bàsic (Basic Auth)**: Concatena usuari i passaport amb ":" i ho codifica en Base64. És trivial de descodificar i només és segur sota **HTTPS** .
    
- **JSON Web Token (JWT)**: Estàndard modern (RFC 7519) per transmetre dades sensibles de forma autocontinguda i signada .
	- Són generats per servidor, i les dades estàn autocontingdes al token
    
- **Parts d'un JWT**:
    
    1. **Header**: Algorisme de signatura i tipus.
        
    2. **Payload**: Dades de l'usuari (issuer, subject, expire, etc.) .
        
    3. **Signature**: Hash del header i payload signat amb una clau privada.
        
- **Flux JWT**: El client fa login, el servidor genera el JWT i el retorna; a partir d'aquí, el client l'envia a la capçalera d'autorització de cada petició .
    

## 7. Asincronia i Comunicació Bidireccional


HTTP tradicional no permet que el servidor iniciï comunicació, però hi ha solucions.

- **AJAX (Asynchronous JavaScript and XML)**: Permet recepció de dades no bloquejant al client-side usant l'objecte `XMLHttpRequest`. Associa una funció a l'esdeveniment `onreadystatechange` per processar la resposta quan arribi .
    
- **WebSockets**: Canal bidireccional i _full-duplex_ sobre un únic socket TCP. Permet interacció en viu (jocs, xats). Només el _handshake_ inicial és HTTP; després es passa a un protocol TCP propi al port 80 .
    
- **Ecosistema**: Llibreries com JQuery o React, i frameworks com Vue o Angular faciliten la gestió de l'asincronia i la manipulació del DOM .
    
