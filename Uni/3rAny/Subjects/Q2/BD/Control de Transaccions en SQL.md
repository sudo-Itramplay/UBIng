A la pràctica, el [[SQL]] (MySQL) ofereix eines per gestionar l'**atomicitat** ([[Propietats ACID]]) de les [[Transacció|transaccions]].

**Flux i sintaxi:**
- **Inici:** `START TRANSACTION` per a una transacció explícita.
- **Finalització:** `COMMIT` (canvis permanents) o `ROLLBACK` (desfer tota l'activitat).
- **Autocommit:** per defecte cada sentència és una transacció independent; es desactiva amb `SET autocommit = 0` per agrupar operacions.

> [!warning] COMMIT
> Recorda fer `COMMIT` perquè els canvis siguin permanents.

**Exemple clàssic:** trasllat de fons entre comptes; si la segona operació falla, el `ROLLBACK` garanteix que els diners no "desapareguin".

L'aïllament es configura amb `SET TRANSACTION` → [[Nivells d'Aïllament]].

Relacionat: [[Transacció]] · [[Nivells d'Aïllament]] · [[Propietats ACID]] · [[SQL]]

#assignatura/BD #tipus/teoria
