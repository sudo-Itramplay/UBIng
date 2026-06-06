Format imprescindible per al [[Regla de Resolució|mètode de resolució]] i el [[Problema SAT|SAT]].

- **Literal:** un àtom o la seva negació.
- **Clàusula:** una **disjunció** de literals ($P\vee\neg Q$).
- Una fórmula és en **FNC** si és una **conjunció de clàusules** ($\phi_1\wedge\dots\wedge\phi_n$).
- **Clàusula buida ($\square$):** disjunció buida = **contradicció** (cap interpretació la satisfà).

**Algorisme de transformació (3 passos):**
1. Eliminar $\rightarrow$ i $\leftrightarrow$ ($\neg\varphi\vee\psi$).
2. Interioritzar negacions ([[Equivalència Lògica|De Morgan]], doble negació).
3. Aplicar la **distributiva** ($\vee$ sobre $\wedge$).

> Per a predicats cal la [[Forma Clausal]] (amb Skolemització).

Relacionat: [[Regla de Resolució]] · [[Equivalència Lògica]] · [[Forma Clausal]] · [[Problema SAT]]

#assignatura/LL #tipus/teoria
