Una **transacció** és una **unitat lògica de processament** atòmica: s'ha de completar **enterament** o no fer-se, per garantir la correcció de la [[Base de Dades]].

- Inclou operacions de lectura (`read`), inserció, eliminació i actualització (`write`).
- **Operacions bàsiques:** `read_item(X)` (BD → variable) i `write_item(X)` (variable → BD).
- **Granularitat:** s'aplica igual sigui un camp, un registre o un bloc de disc.

![[Pasted image 20260415191350.png]]

**Sistemes de processament:** grans BD amb centenars d'usuaris concurrents (banca, borsa, reserves aèries) que exigeixen alta disponibilitat i [[Concurrència]].
- **Single-user DBMS:** un usuari alhora (ordinadors personals).
- **Multiuser DBMS:** milers d'usuaris concurrents (el més usat).

**Conceptes clau:**
- [[Concurrència]] · [[Problemes de Concurrència]] · [[Recuperació de Transaccions]]
- [[Propietats ACID]] · [[Nivells d'Aïllament]] · [[Log del Sistema]]
- [[Schedules i Serialitzabilitat]] · [[Control de Transaccions en SQL]] · [[Backup i Restore]]

Relacionat: [[DBMS]] · [[Propietats ACID]] · [[SQL]]

#assignatura/BD #tipus/teoria
