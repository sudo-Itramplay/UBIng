Operació binària de l'[[Àlgebra Relacional]] ($\times$) que concatena **totes** les files de $R$ amb **totes** les de $S$ (tots els parells possibles).

> Sintaxi: $R \times S$

- L'esquema resultant és la unió dels esquemes de $R$ i $S$.
- És la base del [[Join]] (un join és una [[Selecció]] sobre un producte cartesià).

![[Pasted image 20260310162156.png]]
![[Pasted image 20260310162223.png]]

> Quan hi ha atributs amb noms idèntics a ambdues taules, es desambigua amb `RELATION_NAME.attribute` (p. ex. `CLIENT.client_id = VIEWING.client_id`).

Relacionat: [[Join]] · [[Selecció]] · [[Àlgebra Relacional]]

#assignatura/BD #tipus/teoria
