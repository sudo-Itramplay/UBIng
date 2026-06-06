Un **microservei** és un servei petit, desplegable de manera **independent**, amb una responsabilitat acotada ([[Monòlit vs Microserveis]]).

**Característiques:** procés independent, **Single Responsibility**, exposa una **API**, desplegament i escalat individuals, completament **desacoblat**. Cada servei té la seva **persistència pròpia** (BD per servei); **mai** es comparteix memòria ni BD → tot per xarxa via API.

**Costos ocults:** complexitat de codi/infra, debugging difícil, consistència de dades distribuïda, monitorització (Prometheus, Grafana, Jaeger/Zipkin).

Conceptes: [[Comunicació Inter-Servei]] · [[Tolerància a Fallades]] · [[API Gateway]] · [[Arquitectura Basada en Esdeveniments]] · [[Docker i Kubernetes]].

Relacionat: [[Monòlit vs Microserveis]] · [[Reptes dels Sistemes Distribuïts]]

#assignatura/SD #tipus/teoria
