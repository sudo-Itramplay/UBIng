Quan les [[Transacció|transaccions]] s'executen sense control de [[Concurrència]], poden sorgir fenòmens que corrompen les dades. Els quatre crítics:

- **Lost Update (Actualització Perduda):** dues transaccions intercalen operacions i una actualització en sobreescriu una altra.
- **Dirty Read (Lectura Bruta):** una transacció llegeix un valor d'una altra que encara no ha fet commit i que després fa rollback.
- **Incorrect Summary (Resum Incorrecte):** una transacció calcula una agregació mentre altres actualitzen els valors → resultat inconsistent.
- **Unrepeatable Read (Lectura No Repetible):** una transacció llegeix el mateix ítem dues vegades i rep valors diferents perquè una altra l'ha modificat entremig.

![[Pasted image 20260415191444.png]]
![[Pasted image 20260415191459.png]]
![[Pasted image 20260415191511.png]]

Es controlen amb els [[Nivells d'Aïllament]] i la [[Schedules i Serialitzabilitat|serialitzabilitat]].

Relacionat: [[Concurrència]] · [[Nivells d'Aïllament]] · [[Schedules i Serialitzabilitat]]

#assignatura/BD #tipus/teoria
