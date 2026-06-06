El cor del [[Ray Tracing]]: determinar quin [[Objectes|objecte]] colpeja primer un [[Raig Primari|raig]]. Es busca la **intersecció més propera** (la $t > 0$ més petita).

**Contracte del mètode `Hit`:** `hit(ray, tmin, tmax)` retorna `cert` si hi ha intersecció vàlida dins $[t_{min}, t_{max}]$, amb la $t$ més propera, el punt $P$, la [[Normal]] $\vec{N}$ i el [[Materials|material]].

- **Esfera:** equació quadràtica de $(P - C)^2 - R^2 = 0$. El discriminant dona 0, 1 o 2 solucions; ens quedem amb la $t$ positiva més petita.
- **Pla:** $(P - P_0) \cdot \vec{N} = 0$; si el denominador ≈ 0, el raig és paral·lel.
- **Triangle:** intersecció amb el pla + test de **coordenades baricèntriques** → [[Intersecció Raig-Triangle]].

S'optimitza amb [[Estructures d'Acceleració]].

Relacionat: [[Intersecció Raig-Triangle]] · [[Objectes Paramètrics]] · [[Estructures d'Acceleració]] · [[Normal]]

#assignatura/Grafics #tipus/teoria
