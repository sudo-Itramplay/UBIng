**EDA**: alternativa asíncrona a les crides síncrones de [[Comunicació Inter-Servei]], usant missatgeria distribuïda.

**Avantatges:** desacoblament temporal absolut, millor tolerància a fallades, processament en _background_, escalat elàstic.

- **Esdeveniment:** representació d'un fet que **JA ha succeït** (immutable, en passat: `UserRegistered`, `OrderCreated`, `PaymentCompleted`).

**Model Productor-Consumidor** (els serveis no es coneixen directament):
- **Productor:** publica l'esdeveniment en un _topic_.
- **Consumidor:** subscrit al _topic_, el processa quan té recursos.

> Tecnologies: **Apache Kafka**, **RabbitMQ**, AWS SNS/SQS.

Relacionat: [[Comunicació Inter-Servei]] · [[Microserveis]] · [[Tolerància a Fallades]]

#assignatura/SD #tipus/teoria
