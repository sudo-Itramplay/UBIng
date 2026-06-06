El [[Ray Tracing]] "ingenu" té cost $O(N_{pixels} \times N_{objectes})$, insostenible per a escenes complexes. Optimitzacions:

- **Volums Contenidors (Bounding Volumes):** formes simples que engloben objectes complexos; si el raig no toca el volum, no toca l'objecte.
- **AABB (Axis-Aligned Bounding Box):** definida pel mínim i el màxim. **Mètode dels Slabs:** intersecció de 3 parells de plans paral·lels; impacte si $\max(t_{enter}) < \min(t_{exit})$.
- **BVH (Jerarquies de Volums):** agrupació jeràrquica en arbre; si el raig no toca un node, es descarta tota la branca → cost $O(\log N)$ en el cas mig.
- **Cost vs benefici:** una **AABB** és ràpida però amb espai buit; una **OBB** (orientada) s'ajusta millor però és més cara.

Relacionat: [[Intersecció Raig-Objecte]] · [[Scene Graph i CSG]] · [[Ray Tracing]]

#assignatura/Grafics #tipus/teoria
