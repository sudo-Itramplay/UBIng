Conversió de l'esquema conceptual ([[Model Entitat-Relació]]) a taules relacionals, pel que fa a **entitats i atributs**.

**Entitats fortes i febles:**
- **[[Entitat]] forta:** una taula amb tantes columnes com atributs; la [[Clau Primària]] surt de les seves claus (subratllada).
- **[[Weak Entity|Entitat feble]]:** taula amb els seus atributs més la PK de l'entitat forta propietària; la PK resultant combina la clau parcial pròpia amb la del propietari (que actua com a [[Clau Estrangera]], en cursiva).

![[Pasted image 20260303180912.png]]

**Atributs** ([[Tipus d'Atributs]]):
- **Compostos:** no es crea taula; una columna per cada sub-atribut.
- **Multivariats:** exigeixen una taula pròpia amb la PK de l'entitat com a FK; la PK és la unió d'aquesta FK amb cada valor.

**Herència ([[Generalització i Especialització]]):** una taula per al pare i una per cada filla, compartint l'identificador del pare com a PK.

![[Pasted image 20260303181019.png]]

Relacionat: [[Passant els ER a MR]] · [[Transformació de Relacions a Taules]] · [[Clau Primària]]

#assignatura/BD #tipus/teoria
