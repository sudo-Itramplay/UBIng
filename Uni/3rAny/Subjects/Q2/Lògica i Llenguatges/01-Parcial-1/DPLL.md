Algorisme de cerca per al [[Problema SAT]], basat en les regles de [[Davis-Putnam]] + el **Lema de Davis-Putnam**.

> [!info] Lema de Davis-Putnam
> $\varphi$ és satisfactible ⟺ $\varphi\wedge\psi$ ho és **o bé** $\varphi\wedge\sim\psi$ ho és.

**Funció recursiva DPLL($\chi$):**
1. Aplicar les 3 regles de [[Davis-Putnam]] exhaustivament.
2. Si queda la conjunció buida ($\mathbb{I}$) → **true**; si la clàusula buida ($\square$) → **false**.
3. Si és inconclús, elegir un literal $\psi$ i ramificar: $DPLL(\chi\wedge\psi)\vee DPLL(\chi\wedge\sim\psi)$.

Relacionat: [[Davis-Putnam]] · [[Clàusula vs Conjunció Buida]] · [[Problema SAT]]

#assignatura/LL #tipus/teoria
