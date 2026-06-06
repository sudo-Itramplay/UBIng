Protocol de la [[Web]]: orientat a la connexió, **sense estat**, petició-resposta (anada i tornada) i basat en **text**. HTTP/1.0 una ronda per connexió; HTTP/1.1 introdueix persistència.

**Estructura de les trames** (request i response): 1) línia inicial, 2) capçaleres, 3) línia en blanc, 4) cos (Entity Body).

**Mètodes:**
- `GET` (segur i **idempotent**, recuperar) · `HEAD` (només capçalera) · `POST` (no segur ni idempotent, enviar dades) · `PUT` (emmagatzemar a la URI).

**Codis d'estat:** 1xx informatiu · 2xx èxit · 3xx redirecció · 4xx error de petició · 5xx error del servidor.

**Capçaleres:** `User-Agent`, `Accept`, `Host`, `Connection: Keep-Alive` (request); `Content-Type`, `Content-Length`, `Set-Cookie` (response).

Relacionat: [[Web]] · [[Contingut Dinàmic Web]] · [[REST]]

#assignatura/SD #tipus/teoria
