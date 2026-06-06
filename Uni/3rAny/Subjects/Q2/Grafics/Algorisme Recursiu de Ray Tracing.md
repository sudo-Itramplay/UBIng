El [[Ray Tracing]] és recursiu (`computeRayColor`). Opera en tres nivells de rajos:

1. **Rajos primaris (eye rays):** llançats des de l'observador per cada píxel → [[Raig Primari]].
2. **Rajos d'ombra (shadow rays):** del punt d'intersecció cap a les llums per saber si està il·luminat o en [[Ombres|ombra]].
3. **Rajos secundaris:** de **[[Reflexions|reflexió]]** (direcció de mirall) i de **[[Transparències|transparència]]/refracció**.

![[Pasted image 20260221094014.png]]

**Casos base** (no podem llançar rajos infinitament):
- **Profunditat màxima** (_depth_): límit de rebots.
- **Acabament adaptatiu:** aturar quan la contribució és insignificant.

El color es combina amb l'[[Equació de Color]].

Relacionat: [[Equació de Color]] · [[Raig Primari]] · [[Reflexions]] · [[Transparències]]

#assignatura/Grafics #tipus/teoria
