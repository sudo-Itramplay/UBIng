Evolució de l'**Equi Join** ([[Join]]) que combina taules pels **atributs amb el mateix nom** en ambdues relacions, **eliminant les columnes duplicades**.

**Algorisme en 3 passos:**
1. [[Producte Cartesià]] $R \times S$.
2. [[Selecció]] per igualtat dels atributs comuns.
3. [[Projecció]] per descartar els atributs repetits.

**Ordre final:** ordre de $R$ + ordre de $S$ − nombre d'atributs comuns.

S'usa quan no s'especifica un predicat $F$ explícit i es volen aprofitar les [[Clau Estrangera|claus foranes]] amb el mateix nom.

![[Pasted image 20260321104658.png]]
![[Pasted image 20260321104925.png]]

Relacionat: [[Join]] · [[Outer Join]] · [[Àlgebra Relacional]]

#assignatura/BD #tipus/teoria
