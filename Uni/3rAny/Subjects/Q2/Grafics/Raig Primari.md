El **raig primari** va de l'observador a l'escena ([[Ray Tracing]]). Cal saber on està l'observador i quina part del món es veu.

**Recta paramètrica:** $p = A + t \cdot \vec{B}$, on **A** és l'origen (observador) i **B** el vector director (cap al píxel).

> [!warning] Crucial
> Si la intersecció dona una **$t$ negativa**, l'objecte està **darrere** de l'observador → descartar.

**Configuració estàndard d'exemple:** sistema de la mà dreta (món a Z negatives), observador a (0,0,0), viewport 200×100, distància focal 1 (pla de projecció a Z=-1), vfov=90°, aspect ratio 2 → window de (-2,-1) a (2,1).

Relacionat: [[Model de Càmera]] · [[Coordenades Homogènies]] · [[Intersecció Raig-Objecte]] · [[Ray Tracing]]

#assignatura/Grafics #tipus/teoria
