Es passa d'aplicació monolítica a modular ([[Software Distribuït]]).

**Capes lògiques:**
1. **Usuari:** presentació i navegació.
2. **Negoci:** lògica, validació, esdeveniments.
3. **Dades:** CRUD i integritat.
4. **Sistema:** fitxers, autenticació, logs.

**Capes físiques (Deployment / Tiers):**
- **Single-Tier:** 1 màquina, mono-usuari.
- **2-Tier (Client/Servidor):** capa de negoci dividida client/servidor.
- **3-Tier:** Client / Negoci / Dades; responsabilitats clares, més missatges.
- **N-Tier:** múltiples servidors per capa; molt escalable.

> Versió moderna: [[Monòlit vs Microserveis]].

Relacionat: [[Tipologia de Clients]] · [[Monòlit vs Microserveis]] · [[Model Client-Servidor]]

#assignatura/SD #tipus/teoria
