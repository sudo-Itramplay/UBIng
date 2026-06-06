Desplegament de [[Microserveis]]: amb dotzenes de serveis sorgeixen problemes (versions, ports, escalabilitat, logs). Solució: **Contenidors (Docker) + Orquestradors (Kubernetes)**.

**Docker (contenidització a nivell d'OS):** empaqueta un microservei amb el seu runtime i dependències en un **contenidor** lleuger → comportament **idèntic a qualsevol entorn**. El `Dockerfile` defineix la construcció de la imatge.

| | Màquina Virtual | Contenidor (Docker) |
| --- | --- | --- |
| Abstracció | Hardware (OS convidat complet) | OS (comparteix Kernel del host) |
| Mida | Gigabytes | Megabytes |
| Arrencada | 30-45 s | < 50 ms |
| Aïllament | Molt alt | Menor |

**Kubernetes (K8s):** orquestra **centenars** de contenidors en múltiples servidors: **Scheduling**, **Self-Healing** (reinici automàtic), **Escalat elàstic**, **Load Balancing**, observabilitat.

Relacionat: [[Microserveis]] · [[Monòlit vs Microserveis]]

#assignatura/SD #tipus/teoria
