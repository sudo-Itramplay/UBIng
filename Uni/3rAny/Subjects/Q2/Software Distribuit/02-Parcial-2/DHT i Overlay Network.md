Les **Taules de Hash Distribuïdes (DHT)** fan que un sistema [[P2P]] sigui escalable i tolerant a fallades sense dependència central.

- **Autonomia:** sense coordinació central.
- **Escalabilitat:** cost de coordinació $O(\log n)$ per node → milions de nodes.
- **Tolerància a fallades:** es reconfigura automàticament en entrar/sortir nodes (**churn**).
- **Espai de claus:** cada node té un rang contigu de claus.
- **Hash consistent:** minimitza la redistribució de claus quan canvia el nombre de nodes (només afecta veïns).
- **Funció de distància:** mètrica lògica (no geogràfica).

**Overlay Network (xarxa superposada):** xarxa lògica d'enllaços entre veïns; defineix la topologia i els algorismes d'enrutament (_Nearest Neighbour_, broadcast/multicast).

Relacionat: [[P2P]] · [[BitTorrent]] · [[Blockchain]]

#assignatura/SD #tipus/teoria
