Model d'il·luminació estàndard ([[Models d'Il·luminació]]). El color és la suma de tres components:

$$I = k_a I_a + k_d I_d \cos(\vec{L},\vec{N}) + k_s I_s \cos(\vec{N},\vec{H})^{\beta}$$

- **Ambient ($K_a I_a$):** il·luminació base constant.
- **Difusa ($K_d I_d (N\cdot L)$):** depèn de l'angle entre la [[Normal]] $N$ i la llum $L$; simula superfícies mat.
- **Especular ($K_s I_s (N\cdot H)^\beta$):** la brillantor; usa el vector **Halfway** $H$ (mitjana entre $L$ i la visió $V$).

> Amb [[Ombres]]: s'afegeix un **factor d'ombra** que multiplica les components difusa i especular de cada llum.

Relacionat: [[Models d'Il·luminació]] · [[Ombres]] · [[Normal]] · [[Transparències]]

#assignatura/Grafics #tipus/teoria
