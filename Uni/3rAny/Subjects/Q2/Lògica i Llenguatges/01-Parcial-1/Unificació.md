Procés de fer **idèntiques** dues expressions ([[Terme|termes]] o àtoms) mitjançant una **substitució** $\lambda = \{x_i = t_i\}$ (reemplaçar variables per termes). És el "motor" de la [[Resolució en Predicats]].

**Algorisme** (pila d'igualtats $P$):
- Igualtat de variables/constants idèntiques → continuar.
- Variable $e$ i terme $e'$ amb $e\notin e'$ → aplicar la substitució a tota la pila i guardar-la.
- Funcions/predicats iguals $f(s_1,...,s_n)=f(t_1,...,t_n)$ → descomposar en $s_i = t_i$.
- Conflicte de símbols (ex: $f(a)=g(x)$) → **"fallo"**.

El resultat és el **unificador** que cancel·la literals oposats.

Relacionat: [[Resolució en Predicats]] · [[Forma Clausal]] · [[Terme]]

#assignatura/LL #tipus/teoria
