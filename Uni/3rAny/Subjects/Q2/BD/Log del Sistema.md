El DBMS utilitza un **log** (diari de bord) per gestionar la [[Recuperació de Transaccions|recuperació]].

**Operacions clau de la [[Transacció]]:**
- `BEGIN_TRANSACTION`: inici d'execució.
- `READ` / `WRITE`: operacions sobre ítems.
- `END_TRANSACTION`: final de les operacions.
- `COMMIT_TRANSACTION`: senyal d'èxit.
- `ROLLBACK (ABORT)`: senyal de fallada.

**Estats:** Activa → Parcialment Commesa → Commesa → Terminada (pot fallar des d'activa o parcialment commesa).

**Log del sistema:** fitxer seqüencial (append-only) que registra start, write, read, commit, abort.

![[Pasted image 20260418091826.png]]

- **Punt de commit:** quan totes les operacions s'han executat amb èxit i registrat al log.
- **Force-writing:** el buffer del log s'ha d'escriure a disc **abans** de fer commit.

Relacionat: [[Recuperació de Transaccions]] · [[Schedules i Serialitzabilitat]] · [[Transacció]]

#assignatura/BD #tipus/teoria
