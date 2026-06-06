Classificacions del servidor en el [[Model Client-Servidor]]:

- **Amb estat vs Sense estat:** amb estat manté info de cada client (millor temps de resposta però difícil recuperació davant errors); sense estat és més senzill de codificar.
- **Orientat a connexió ([[TCP Stream-mode|Stream]]) vs No orientat ([[UDP Datagram-mode|Datagram]]).**
- **Iteratius vs Concurrents:** l'iteratiu serveix un client a la vegada; el **concurrent** atén múltiples sessions amb [[Threads]] (un fil per client).

**Gestió no-bloquejant (NIO):** alternativa als threads massius → un **Selector** gestiona múltiples canals amb un sol fil (`configureBlocking(false)`).

Relacionat: [[Model Client-Servidor]] · [[Threads]] · [[Multicast]]

#assignatura/SD #tipus/teoria
