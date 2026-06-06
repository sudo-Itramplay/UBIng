Operació unària de l'[[Àlgebra Relacional]] ($\sigma$) que reté les **files** d'una relació $R$ que satisfan un predicat.

> Sintaxi: $\sigma_{predicate}(R)$

- Exemple: pel·lícules de més de 150 min → $\sigma_{length>150}(MOVIES)$.
- Permet predicats compostos amb AND / OR ($\lor$).

> [!warning] Ordre amb la [[Projecció]]
> Primer s'aplica la **Selecció** (files), després la **Projecció** (columnes):
> $\pi_{fname,lname}(\sigma_{salary\ge10000}(STAFF))$

![[Pasted image 20260310160909.png]]
![[Pasted image 20260310160851.png]]

Relacionat: [[Projecció]] · [[Àlgebra Relacional]]

#assignatura/BD #tipus/teoria
