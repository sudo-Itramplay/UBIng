Com intercanvien informació els [[Microserveis]]:

1. **Síncrona (Request/Response):** el client es bloqueja esperant resposta (**REST sobre HTTP**, CRUD). Simple, interoperable, fàcil de depurar; ideal per a consultes immediates.
2. **Asíncrona (esdeveniments):** sense bloquejos, via un **Message Broker** (Kafka, RabbitMQ) → [[Arquitectura Basada en Esdeveniments]].
3. **Mesh de Serveis:** comunicació directa P2P amb descobriment (gRPC, Istio, Linkerd).

> [!warning] Coupling temporal (perill del síncron)
> Si A crida B i B crida C, es genera una dependència lineal: **si un servei cau o triga, tota la cadena es bloqueja** → errors en cascada per timeout.

> **Arquitectura híbrida (real):** REST per a respostes immediates + esdeveniments per a processos de _background_.

Relacionat: [[Microserveis]] · [[Tolerància a Fallades]] · [[Arquitectura Basada en Esdeveniments]]

#assignatura/SD #tipus/teoria
