Conversió de les [[Relació (ER)|relacions]] del [[Model Entitat-Relació]] a taules. En un diagrama no cal identificar les relacions; en el model relacional sí.

Una taula de relació agrupa les [[Clau Primària|claus primàries]] de les entitats participants més els atributs propis de la relació.

> [!info] Per l'examen
> En el model ER no existeixen les [[Clau Estrangera|claus foranes]] ni les claus de relació; en la transformació tabular apareixen obligatòriament.

**El paper de la [[Cardinalitat]]:**
- **1:1** → es pot usar la PK de qualsevol de les dues entitats com a PK de la taula.
- **1:N o N:1** → la PK és la del conjunt amb cardinalitat **N**.
- **N:N** → la PK és la **unió de les PK d'ambdues** entitats (totes són FK). De vegades cal afegir-hi un atribut propi de la relació.

![[Pasted image 20260303181436.png]]
![[Pasted image 20260303181449.png]]
![[Pasted image 20260303181501.png]]

**Casos especials:**
- **Relació feble:** no té taula pròpia; la info s'absorbeix dins la taula de l'entitat feble.
- **Relació múltiple (n-ària):** taula amb les PK de totes les participants com a FK; la PK global les uneix totes.

![[Pasted image 20260303181624.png]]

Relacionat: [[Transformació ER a Taules]] · [[Simplificació de Taules]] · [[Cardinalitat]]

#assignatura/BD #tipus/teoria
