Defineix el punt de vista de l'escena en [[Ray Tracing]].

**Paràmetres:**
- **lookFrom** (ull) i **lookAt** (on mirem) · **VUP** (verticalitat) · **vfov** (angle de visió vertical).
- **Clipping planes** (near i far) delimiten el camp de visió.
- **VFOV:** decrementar-lo fa **zoom in**. Un **travelling** canvia `lookFrom`; un **zoom** òptic només canvia el vfov.
- **Aspect ratio** = amplada/alçada del viewport.

> **Viewport:** imatge final de píxels. **Frame buffer** (window): representació en memòria on s'emmagatzemen els colors calculats.

Genera el [[Raig Primari]] per a cada píxel.

Relacionat: [[Raig Primari]] · [[Coordenades Homogènies]] · [[Elements Gràfics]] · [[Ray Tracing]]

#assignatura/Grafics #tipus/teoria
