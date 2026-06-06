L'[[HTTP]] és **stateless**, però les aplicacions necessiten continuïtat (sessions) i autenticació ([[Web Services]]).

**Estratègies de sessió:**
- **Camps ocults** (`<input type="hidden">`): insegur (visible al codi).
- **Cookies:** el servidor envia `Set-cookie`, el client la retorna a cada petició.
- **URL Rewriting:** identificador com a paràmetre a cada enllaç.
> Poc segurs: usar IDs que **expirin** i no enviar mai info sensible en text pla.

**Autenticació:**
- **Basic Auth:** usuari:contrasenya en Base64; trivial de descodificar → només segur sota **HTTPS**.
- **JWT (JSON Web Token):** token signat i **autocontingut** (RFC 7519). Parts: **Header** (algorisme), **Payload** (dades), **Signature** (hash signat). Flux: login → servidor genera JWT → client l'envia a la capçalera d'autorització de cada petició.

Relacionat: [[REST]] · [[Web Services]] · [[AJAX i WebSockets]]

#assignatura/SD #tipus/teoria
