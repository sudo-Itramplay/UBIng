L'[[HTTP]] tradicional no permet que el servidor iniciï la comunicació; solucions per a asincronia i bidireccionalitat ([[Web Services]]):

- **AJAX (Asynchronous JavaScript and XML):** recepció de dades **no bloquejant** al client amb `XMLHttpRequest`; una funció associada a `onreadystatechange` processa la resposta quan arriba.
- **WebSockets:** canal **bidireccional full-duplex** sobre un únic socket TCP (jocs, xats en viu). Només el _handshake_ inicial és HTTP; després passa a un protocol TCP propi (port 80).

> Ecosistema: jQuery, React, Vue, Angular faciliten l'asincronia i la manipulació del DOM.

Relacionat: [[REST]] · [[Sessions i Autenticació]] · [[Web Services]]

#assignatura/SD #tipus/teoria
