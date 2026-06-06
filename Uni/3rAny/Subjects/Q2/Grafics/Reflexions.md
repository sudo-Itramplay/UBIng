Rajos secundaris del [[Ray Tracing]]. No totes les superfícies reflecteixen igual segons el [[Materials|material]]:

- **Especulars (metalls):** reflexió perfecta, angle d'incidència = angle de reflexió:
$$r_{out} = r_{in} - 2(r_{in}\cdot N)\cdot N$$
- **Fuzzy (especularitat rugosa):** afegeix aleatorietat → $v = r + fuzzy\cdot randomInSphere()$ (paràmetre _fuzzy_ entre 0 i 1).
- **Difuses:** la llum rebota en qualsevol direcció (punt aleatori dins una esfera tangent a la [[Normal]]).

> [!warning] Surface Acne
> Per precisió numèrica, un raig reflectit pot intersectar la mateixa superfície (taques negres). **Solució:** desplaçar l'origen en la direcció de la normal o usar un $t_{min}$ petit (cf. [[Shadow Acne]]).

Relacionat: [[Transparències]] · [[Equació de Color]] · [[Algorisme Recursiu de Ray Tracing]] · [[Normal]]

#assignatura/Grafics #tipus/teoria
