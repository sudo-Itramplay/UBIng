Sistema $(x, y, z, w)$ usat en el càlcul vectorial del [[Ray Tracing]] per aplicar transformacions lineals de forma consistent.

- **$w = 1$** → és un **punt**.
- **$w = 0$** → és un **vector** director.

Aquesta distinció és vital quan s'apliquen transformacions geomètriques (translacions, escalats) a l'escena.

> Eficiència: per moure una malla, és millor guardar els vèrtexs originals + el **centre** com a atribut (o transformar la càmera/raig) que modificar cada vèrtex.

Relacionat: [[Raig Primari]] · [[Model de Càmera]] · [[Ray Tracing]]

#assignatura/Grafics #tipus/teoria
