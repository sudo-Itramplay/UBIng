# 1. Introducció a la World Wide Web i Conceptes Bàsics

- **Història i Evolució:** La World Wide Web (WWW) de lluny, representa el sistema distribuït més ben conegut del món, estant format fonamentalment per servidors HTTP (web servers) i clients (web browsers).

## **Funcionament WWW:** 
La WWW és una aplicació client-servidor orientada a la connexió que es basa íntegrament en l'HyperText Transfer Protocol (HTTP).
- Per defecte, els servidors web corren sobre el port 80. 
- L'usuari sol·licita un document mitjançant el navegador i, si aquest es troba al servidor, el contingut és retornat i presentat a l'usuari.

### **Els Tres Elements Clau (URL, HTTP, HTML):** 
El sistema web combina tres peces clau per funcionar:
- l'URL per localitzar
- l'HTTP per transmetre
- l'HTML per estructurar.

#### **URL (Uniform Resource Locator) o URI:** 
Constitueix el sistema de noms i adreces. Identifica recursos a la web (documents, imatges o serveis) i permet el seu accés sota mètodes com HTTP o FTP. L'esquema d'una URI és: `protocol://username:passwd@hostname:port/path/subdirs/resource?param1=value1&param2=value2`.
    
#### **HTML (HyperText Markup Language):**
És el llenguatge de marcatge utilitzat per crear documents per a la WWW. Es basa en el format SGML, amb semàntiques dissenyades per representar diversos tipus d'informació, i està formalment definit pel W3C (tot i que molts navegadors són permissius a l'hora de llegir-lo).
![[Pasted image 20260314105644.png]]

---

# 2. El Protocol HTTP: Fonaments i Trames

## **Característiques de l'HTTP:**
L'HTTP és un protocol:
	- orientat a la connexió
	- sense estat
	- d'anada i tornada (petició-resposta). 

- La versió inicial (HTTP/0.9) era un protocol molt simple per transferir dades sense format. La versió HTTP/1.0 permet només una sola ronda de petició-resposta per cada connexió, mentre que la versió HTTP/1.1 va introduir la persistència de connexions.
    
## **Estructura de les Trames HTTP:**
L'HTTP és un protocol basat en text. Tant les peticions (request) com les respostes (response) segueixen un ordre estricte: 
1. Línia inicial (request/response)
2. Secció de capçalera
3. Línia en blanc 
4. el Cos (Entity Body).

### Linia Request
S'envia un cop el client estableix la connexió, amb la forma:
`<HTTP method> <Request-URI> <protocol specification>\r\n`. 
![[Pasted image 20260314110035.png]]

Els mètodes principals són:
1. `GET` (segur i idempotent, per recuperar contingut)
2. `HEAD` (segur i idempotent, recupera només la capçalera)
3. `POST` (no segur ni idempotent, per enviar dades a un procés del servidor)
4. `PUT` (per emmagatzemar contingut a la URI especificada).

>[!tip] Què fan?
>- GET: per a recuperar el contingut de l’objecte web al que fa
referència la URI especificada.
>- HEAD: per a recuperar tan sols la capçalera d’un objecte web
des del servidor, no el propi objecte.
> - POST: utilitzat per a enviar dades a un procés del servidor web.
> + PUT: s’utilitza per demanar al servidor emmagatzemar el
contingut que s’adjunta amb la petició, a la ubicació del fitxer
especificat per la URI en el servidor.


- **Capçaleres i Cos del Client:** Les capçaleres afegeixen informació d'interès com:
- l'entorn de l'usuari, navegador(`User-Agent`), 
- els tipus de dades acceptades, pel client (`Accept`) 
- si es desitja mantenir la connexió oberta, després de fer un request (`Connection: "Keep-Alive"`).
- El nom del amfitrió (`Host`)
- i més

El cos del request, opcional, conté les dades a transferir, com quan s'usa el mètode `POST`.
    
### **La Resposta HTTP (Response):**
Es  compon per:
1. Línia de resposta (estat)
2. Secció de capçalera
3. Un espai en blanc 
4. el Cos (Entity Body).

La línia de resposta té la forma:
`<protocol> <status-code> <description>\r\n`. 

Els codis d'estat es divideixen en:
- 100-199 (Informatiu), 
- 200-299 (Èxit), 
- 300-399 (Redirecció), 
- 400-499 (Error de petició, no acomplerta) 
- 500-599 (Error intern del servidor). 
La resposta també inclou capçaleres (com `Content-Type`) i el cos, que conté l'objecte Web demanat.

Hi ha dos tipus de lı́nies de capçalera de resposta:
- de resposta: Retorna informació sobre la resposta, el servidor o successius accessos al recurs sol·licitat
	- Refresh, Retry-After, Server, Set-Cookie ...
- de l’entitat: Retorna informació sobre els continguts del recurs sol·licitat pel client.
	- Content-Type, Content-Length, Content-Encoding, Content-Language ..

---

# 3. Aplicacions Web i Contingut Dinàmic

## **Necessitat de Contingut Dinàmic:** 

Originàriament, l'HTTP només transferia continguts estàtics (textes, imatges). 
- Amb l'evolució web, es va fer necessari que els usuaris poguessin recuperar dades basant-se en informació dinàmica introduïda durant la sessió.
    
>[!warning] **Limitacions del Servidor Web Pur:** 
>Un servidor HTTP genèric manca de la lògica d'aplicació necessària per buscar dades dinàmiques en un model de dades.
    
### **L'Intermediari (Scripting Engine):**
Per resoldre això, s'utilitza un **procés extern** a la màquina del servidor que fa d'intermediari i conté la lògica d'aplicació. 
- Aquest procés accepta les dades d'entrada des del servidor web, executa la lògica per obtenir dades, i retorna el resultat al servidor web perquè aquest últim el transmeti al client.

- **Mecanisme d'Execució:** El procediment clàssic per invocar aquests programes web des de la part del client és a través del camp `ACTION` dins d'un formulari HTML, que enllaça directament amb l'script (com ara un fitxer .php o .cgi).
![[Pasted image 20260314113446.png]]


---

# 4. Formularis Web i Gestió de Dades (Query Data)

- **Definició de Formularis:** Els formularis s'encabeixen entre les etiquetes `<FORM>...</FORM>`. 
	- L'atribut `ACTION` defineix la URL absoluta o relativa on aniran destinades les dades. 
	- L'atribut `METHOD` especifica la forma en què s'enviaran aquestes dades (típicament GET o POST). 
Finalment, es requereix un element d'entrada del tipus "submit" (botó) per emetre la petició HTTP.


## **Query Data (Dades de Consulta):**
Són les dades introduïdes per l'usuari als elements del formulari (identificats pel seu atribut `name`). 

- Aquestes dades es codifiquen en una "Query String", que és una seqüència de parells `name=value` separats per `&`. El navegador transforma els caràcters reservats en ASCII hexadecimal mitjançant codificació URL.
    
### Enviaments

#### **L'Enviament amb GET:** 
Si s'usa GET, la Query Data s'afegeix directament al final de la URL del request, precedida pel caràcter `?`. 
- Degut a què la longitud de la línia de request és limitada en l'HTTP, aquest mètode no és adequat per enviar grans volums de dades.

####  **L'Enviament amb POST:**
Si s'usa POST, la URL queda inalterada i la Query Data s'envia oculta a l'interior del cos (body) de la petició HTTP.
    
#### **Patró POST-Redirect-GET:** 

>[!warning] Important
>Serveix per evitar que el navegador mostri el molest avís de "reenviament de dades" quan un usuari refresca una pàgina després d'un POST.

El patró consisteix en enviar dades amb POST, actualitzar-les al servidor, retornar un codi de redirecció (3xx) cap a una nova URL, i finalment fer que el navegador faci un GET cap a aquesta adreça de resultat.

![[Pasted image 20260314114909.png]]

---

### 5. Frameworks d'Aplicacions Web i Arquitectura MVC

- **Arquitectura MVC:** Gran part dels Frameworks Web moderns es basen en el patró de disseny Model-View-Controller.
    
    - _Model:_ S'encarrega del model de dades, que es manipulen segons les accions de l'usuari.
        
    - _View (Vista):_ Són les diferents pàgines i components visuals on es mostren resultats i on s'hi produeix la interacció amb l'usuari.
        
    - _Controller (Controlador):_ És el punt central on es recullen totes les peticions. Gestiona tota la lògica de l'aplicació i, finalment, encamina el resultat cap a la vista adequada perquè es mostri.


- **Frameworks Especialitzats:** A banda dels genèrics, hi ha aplicacions ja preparades com els CMS (Wordpress, Drupal, Joomla!), paquets de comerç electrònic o entorns d'e-learning com Moodle.
    
