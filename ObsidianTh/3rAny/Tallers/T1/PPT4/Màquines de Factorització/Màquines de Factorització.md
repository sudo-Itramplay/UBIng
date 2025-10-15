---
aliases:
  - FM
  - Factorization Machine
---
Les Màquines de Factorització es van dissenyar per abordar directament aquestes dues limitacions. 🧠

1. **Generalitzen el Model:** A diferència de la MF que només modela la interacció `usuari-ítem`, les FMs poden incorporar un nombre arbitrari de característiques (context, atributs de l'ítem, dades demogràfiques de l'usuari, etc.) i modelar les seves interaccions. Això les fa extremadament flexibles per a dades disperses i variades com el feedback implícit.
    
2. **S'adapten a l'Objectiu:** El model de les FMs es pot entrenar amb diferents funcions de pèrdua, incloses aquelles dissenyades específicament per a **tasques de rànquing** (com BPR o WARP loss). Això permet optimitzar directament la qualitat de la llista ordenada que es presentarà a l'usuari.
    

En resum, les FMs representen un pas endavant perquè s'alineen millor amb la naturalesa de les dades del món real (implícites) i amb l'objectiu final de la majoria de sistemes de recomanació (el rànquing).