> [!info] Definició
> Regions de l'escena **no visibles des de les fonts de llum**. No és un objecte geomètric, sinó l'**absència d'il·luminació directa** per una oclusió.

**Utilitat:** donen sensació de 3D i pistes visuals sobre formes i posicionament.

**Shadow Rays:** des del punt d'intersecció $P$ es llança un raig cap a la llum $L$. Si colpeja **qualsevol** objecte entre $P$ i la llum ($0 < t < dist\_llum$), el punt està a l'ombra.
- En llums puntuals el factor d'ombra és **binari**: 0.0 (ocluït) o 1.0 (lliure). S'aplica a [[Blinn-Phong]].

Problemes i extensions: [[Shadow Acne]] · [[Soft Shadows]] · ombres amb [[Transparències|objectes transparents]] (atenuació segons el gruix $d'$).

Relacionat: [[Blinn-Phong]] · [[Shadow Acne]] · [[Soft Shadows]] · [[Algorisme Recursiu de Ray Tracing]]

#assignatura/Grafics #tipus/teoria
