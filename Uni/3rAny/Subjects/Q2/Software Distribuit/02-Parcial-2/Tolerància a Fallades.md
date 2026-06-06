En [[Microserveis]] hem d'assumir que la xarxa no és fiable. La filosofia: no evitar l'error sinó **continuar funcionant de forma degradada** malgrat fallades parcials.

**Estratègies:**
- **Timeouts:** cap comunicació espera indefinidament (`timeout=3`).
- **Retries:** reintentar caigudes transitòries (amb compte amb els efectes secundaris).
- **Idempotència:** una operació idempotent dona el mateix resultat tant si s'executa un cop com molts → permet reintents segurs (`GET`/`PUT`/`DELETE` sí; un `POST /payments` no, podria cobrar dos cops).
- **Circuit Breakers:** si un servei falla repetidament, "s'obre el circuit" i es retorna error immediat un temps.
- **Fallbacks:** resposta alternativa quan el servei principal no està disponible (degradació acceptable).

> Recorda les **fal·làcies** de la computació distribuïda: la xarxa NO és fiable, la latència NO és zero, l'ample de banda NO és infinit.

Relacionat: [[Comunicació Inter-Servei]] · [[Microserveis]] · [[Reptes dels Sistemes Distribuïts]]

#assignatura/SD #tipus/teoria
