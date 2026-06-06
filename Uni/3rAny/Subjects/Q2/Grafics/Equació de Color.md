El color final d'un punt en [[Ray Tracing]] és la suma del **color local** ([[Models d'Il·luminació]]) més les contribucions de [[Reflexions|reflexió]] i [[Transparències|transparència]], atenuades per coeficients del [[Materials|material]]:

$$color = colorLocal(point, normal, material) + K \cdot colorReflexió + K' \cdot colorTransparència$$

**Forma recursiva en cadena** (cada terme multiplicat pel coeficient d'atenuació anterior):
$$I = I_{local} + K_r(I'_{local} + K'_r(I''_{local} + ...))$$

Relacionat: [[Algorisme Recursiu de Ray Tracing]] · [[Models d'Il·luminació]] · [[Reflexions]] · [[Transparències]]

#assignatura/Grafics #tipus/teoria
