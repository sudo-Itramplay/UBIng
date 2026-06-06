Originàriament l'[[HTTP]] només transferia contingut estàtic. Per al contingut dinàmic cal un **procés extern (scripting engine)** amb la lògica d'aplicació, que rep dades del servidor web, les processa i en retorna el resultat (s'invoca via el camp `ACTION` d'un formulari → `.php`, `.cgi`).

**Formularis** (`<FORM>`): `ACTION` (URL destí) + `METHOD` (GET/POST) + botó submit.

**Query Data:** parells `name=value` separats per `&` (codificació URL).
- **GET:** la query data s'afegeix a la URL després de `?` (limitada en mida).
- **POST:** la query data va oculta al cos; la URL no canvia.
- **POST-Redirect-GET:** evita el reenviament de dades en refrescar → POST → resposta 3xx → GET a la URL de resultat.

Relacionat: [[HTTP]] · [[MVC]] · [[Web]]

#assignatura/SD #tipus/teoria
