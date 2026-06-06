Operació de l'[[Àlgebra Relacional]] que combina informació de diferents relacions. En essència és una **[[Selecció]] aplicada sobre un [[Producte Cartesià]]**.

Tipus bàsics:
- **Theta Join ($\gg_F$):** files que satisfan un predicat genèric $F$ dins de $R \times S$.
- **Equi Join:** Theta Join on $F$ conté només l'operador d'igualtat ($=$).

**Procediment:** primer $R \times S$, després $\sigma_F$.
**Ordre del resultat:** suma dels ordres de $R$ i $S$.

![[Pasted image 20260321104409.png]]
![[Pasted image 20260321104458.png]]

Variants: [[Natural Join]] · [[Outer Join]].

Relacionat: [[Producte Cartesià]] · [[Selecció]] · [[Natural Join]] · [[Outer Join]]

#assignatura/BD #tipus/teoria
