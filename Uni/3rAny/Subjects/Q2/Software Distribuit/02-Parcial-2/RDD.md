**Resilient Distributed Dataset**: l'abstracció central de [[Spark]]. Col·lecció de dades distribuïda en la memòria del clúster.

**Propietats:**
- **Immutabilitat:** un cop construït no es pot modificar.
- **Traçabilitat (lineage):** recorda com s'ha construït → recomputa fragments perduts sense replicació física.
- **Execució paral·lela** sobre elements distribuïts.

**Construcció:** paral·lelitzant una col·lecció en memòria, transformant un RDD previ, o llegint fitxers (HDFS).

- **Particionament:** més **particions** = més paral·lelisme (equilibrar amb nodes/threads reals).
- **Caching:** `.persist()` / `.cache()` el mantenen en memòria (recalculable si es perd).

Relacionat: [[Transformacions i Accions]] · [[Variables Compartides]] · [[Spark]]

#assignatura/SD #tipus/teoria
