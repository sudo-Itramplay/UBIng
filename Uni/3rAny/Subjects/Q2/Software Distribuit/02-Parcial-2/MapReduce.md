Framework de computació distribuïda de [[Hadoop]]: paral·lelització automàtica i abstracció de la infraestructura.

**Anatomia d'un job (Master/Slave):**
- **JobTracker (mestre):** rep el `.jar` + config del client, consulta el [[HDFS|NameNode]] per la localització dels blocs i distribueix les tasques.
- **TaskTracker (esclaus):** executen les tasques de Map i Reduce a cada node. Les dades es llegeixen **directament dels DataNodes** (evitant saturar el mestre).

**Tolerància a fallades:** reassignació de tasques de nodes caiguts (a una rèplica), aïllament del reinici, reincorporació dinàmica, **execució especulativa** (duplicar tasques de nodes lents).

**WordCount (exemple canònic):**
1. Descomposició en blocs.
2. **Map:** per cada paraula emet `(paraula, 1)`.
3. **Shuffle & Sort:** agrupa per clau.
4. **Reduce:** suma els valors → `(paraula, total)`.

Relacionat: [[HDFS]] · [[Hadoop]] · [[Spark]]

#assignatura/SD #tipus/teoria
