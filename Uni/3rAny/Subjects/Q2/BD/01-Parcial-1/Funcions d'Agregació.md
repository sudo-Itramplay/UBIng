Extensió de l'[[Àlgebra Relacional]] ($\mathcal{G}$) per a càlculs estadístics i resums de dades.

- **Funcions comunes:** `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`.
- **Tractament de [[NULL]]:**
	- `COUNT(*)` compta totes les files, incloent NULLs.
	- `COUNT(A)` compta els valors **no-NULL** de l'atribut A.
	- La resta (`SUM`, `AVG`…) **ignoren** els NULL.

> Sintaxi de l'agrupament: $_{Atributs\_agrupament}\mathcal{G}_{Llista\_agregació}(R)$. Els atributs d'agrupament són opcionals.

![[Pasted image 20260321112720.png]]

- **Filtrat post-agregació** (equivalent al `HAVING` de [[SQL]]): s'aplica una [[Selecció]] $\sigma$ sobre el resultat de $\mathcal{G}$.

Relacionat: [[Àlgebra Relacional]] · [[DQL]] · [[NULL]]

#assignatura/BD #tipus/teoria
