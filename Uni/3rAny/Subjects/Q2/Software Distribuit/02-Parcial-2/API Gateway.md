En una arquitectura de [[Microserveis]], el frontend no parla amb tots els serveis: s'usa un **API Gateway** com a **punt d'entrada únic i centralitzat** per a totes les peticions dels clients.

**Responsabilitats** (tasques transversals, descarregant els serveis de negoci):
- **Enrutament (Routing):** derivar cada petició al microservei correcte.
- **Autenticació i seguretat** a la porta d'entrada.
- **Rate Limiting:** controlar el volum de peticions.
- **Logs:** traça centralitzada.
- **Agregació de respostes:** combinar dades de diversos serveis en una sola resposta per al frontend.

Relacionat: [[Microserveis]] · [[Comunicació Inter-Servei]] · [[Sessions i Autenticació]]

#assignatura/SD #tipus/teoria
