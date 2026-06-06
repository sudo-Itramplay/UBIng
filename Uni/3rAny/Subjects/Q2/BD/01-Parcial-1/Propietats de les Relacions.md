Perquè una taula es consideri formalment una [[Relació (Model Relacional)|relació]] ha de complir:

- **Unicitat del nom:** dues relacions no poden tenir el mateix nom dins una BD.
- **Unicitat de les files:** no es permeten [[Tupla|tuples]] duplicades.
- **Flexibilitat de l'ordre:** l'ordre de les columnes és lliure i no afecta la semàntica.
- **Consistència de tipus:** tots els valors d'una columna pertanyen al mateix [[Domini]].
- **Atomicitat:** els valors de les cel·les han de ser **atòmics** (un sol valor, sense llistes ni taules dins).
- **Noms d'atributs únics** dins la relació (relacions diferents sí que poden compartir noms: `HOTELS.City` i `CLIENTS.City`).

![[Pasted image 20260224162107.png]]

Relacionat: [[Relació (Model Relacional)]] · [[Atribut]] · [[Domini]]

#assignatura/BD #tipus/teoria
