**Representational State Transfer**: no és un protocol sinó un **estil d'arquitectura** que aprofita les capacitats natives de l'[[HTTP]] ([[Web Services]]).

**Principis:** ús explícit dels mètodes HTTP, **stateless**, URIs estructurades com directoris, dades en XML/JSON.

**Mètodes HTTP:** `GET` (recuperar, idempotent) · `POST` (crear, **no** idempotent) · `PUT` (actualitzar, idempotent) · `DELETE`.

**Stateless i Caché:** el servidor no manté sessions; cada petició és completa. Capçaleres `Cache-Control` (`max-age`, `Expires`).
- **Requests condicionals:** `Last-Modified`/`If-Modified-Since` → **304 Not Modified**; o **ETag** (hash) amb `If-None-Match`.

**URIs:** intuïtives i predictibles, evitar query strings (ex: `/discussion/2026/04/15/topic`).

Relacionat: [[Web Services]] · [[HTTP]] · [[Sessions i Autenticació]]

#assignatura/SD #tipus/teoria
