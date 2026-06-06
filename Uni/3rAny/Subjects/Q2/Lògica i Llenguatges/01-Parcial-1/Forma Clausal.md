Versió de la [[Forma Normal Conjuntiva|FNC]] per al [[Llenguatge de Predicats]], necessària per a la [[Resolució en Predicats]]. Té l'aspecte $\forall x_1\dots\forall x_n(\psi_1\wedge\dots\wedge\psi_m)$, on cada $\psi_i$ és una clàusula.

**Algorisme (7 passos):**
1. Eliminar implicacions i co-implicacions.
2. Interioritzar negacions ([[Equivalències en Predicats|De Morgan + quantificadors]]).
3. Normalitzar variables.
4. **Skolemització:** eliminar $\exists$ → constant nova $c$ (si lliure) o funció $f(x_1,\dots,x_n)$ (si sota $\forall$).
5. Renombrar variables.
6. Extreure tots els $\forall$ a l'exterior.
7. Distributivitat.

> [!info] Teorema de la forma clausal
> $\varphi$ és contradicció ⟺ la seva forma clausal ho és (encara que **no són equivalents** en general).

Relacionat: [[Unificació]] · [[Resolució en Predicats]] · [[Forma Normal Conjuntiva]]

#assignatura/LL #tipus/teoria
