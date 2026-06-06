Transformar un autòmata indeterminista (NFA) en un de determinista (DFA), molt més senzill d'implementar. Es basa en la **construcció de subconjunts** i el [[λ-tancament]].

- **Estat inicial:** $q'_0 = \Lambda(q_0)$ (el [[λ-tancament]] de l'inicial).
- **Transició $\delta'(X,a)$:** tots els estats assolibles des de qualsevol $p\in X$ amb el símbol $a$, aplicant-hi després el $\lambda$-tancament.
- **Procés iteratiu:** es calculen transicions per als nous estats fins que no en surti cap de nou.
- **Acceptació:** un estat del DFA és acceptador si conté algun estat acceptador original ($X\cap F\ne\emptyset$).
- **Estat d'error:** les transicions no definides ($\emptyset$) van a un estat no acceptador del qual no se surt.

Relacionat: [[λ-tancament]] · [[Anàlisi Lèxic]] · [[Fases d'un Compilador]]

#assignatura/LL #tipus/teoria
