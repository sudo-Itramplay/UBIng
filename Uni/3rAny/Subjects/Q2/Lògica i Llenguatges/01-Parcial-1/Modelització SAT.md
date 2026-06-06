Traduir un problema pràctic a una fórmula [[Forma Normal Conjuntiva|FNC]] perquè un [[Problema SAT|SAT-solver]] el resolgui. La interpretació que la fa certa **coincideix amb la solució**.

**Coloració de mapes** (4 colors, àtom $R_{ij}$ = "país $i$ té el color $j$"):
1. Cada país té un color: $R_{i1}\vee R_{i2}\vee R_{i3}\vee R_{i4}$.
2. No més d'un color: $\neg R_{ij}\vee\neg R_{ij'}$ ($j\ne j'$).
3. Veïns diferents: $\neg R_{ij}\vee\neg R_{i'j}$ (per a $i,i'$ veïns).

**Sudoku** (àtom $R_{ijk}$ = "fila $i$, columna $j$ té el valor $k$"): regla d'existència + exclusivitat per casella + unicitat per fila/columna/subquadrícula 3×3 + estat inicial. Aplica [[Equivalència Lògica|De Morgan]] ("no dos alhora" → disjunció de negats).

Relacionat: [[Problema SAT]] · [[Forma Normal Conjuntiva]] · [[Davis-Putnam]]

#assignatura/LL #tipus/teoria
