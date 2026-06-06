Pedra angular dels SAT-solvers ([[Problema SAT]]). Tres **regles de simplificació** que preserven la satisfactibilitat:

- **(TAU) Regla de la tautologia:** elimina les clàusules amb un parell complementari de literals.
	- Ex: $(P\vee Q\vee\neg S)\wedge(P\vee\neg P\vee R)\wedge\neg Q \Rightarrow (P\vee Q\vee\neg S)\wedge\neg Q$.
- **(CE)$_\psi$ Clàusula elemental:** amb un literal aïllat $\psi$, elimina les clàusules on apareix $\psi$ i treu $\sim\psi$ de la resta.
	- Ex: $P\wedge(P\vee\neg Q)\wedge(\neg P\vee\neg Q\vee R) \Rightarrow \neg Q\vee R$.
- **(PU)$_\psi$ Literal pur:** si $\psi$ apareix però $\sim\psi$ no és a cap clàusula, elimina les clàusules amb $\psi$.

> $\square$ = [[Forma Normal Conjuntiva|clàusula buida]] (contradicció); $\mathbb{I}$ = conjunció buida (tautologia) → [[Clàusula vs Conjunció Buida]].

S'integren a l'[[DPLL|algorisme DPLL]].

Relacionat: [[DPLL]] · [[Problema SAT]] · [[Clàusula vs Conjunció Buida]]

#assignatura/LL #tipus/teoria
