El **Hadoop Distributed File System**: sistema de fitxers virtual en Java, per sobre del SO natiu de cada node ([[Hadoop]]).

- Un fitxer es divideix en **blocs** de mida fixa (típic **64/128 MB**), distribuïts entre màquines (DataNodes) per maximitzar el paral·lelisme.
- **Replicació per defecte: 3 màquines** per bloc → tolerància a la caiguda de 2 nodes.
- **Optimitzat per:** fitxers grans i accés **seqüencial** (penalitza l'accés aleatori i molts fitxers petits).

**Arquitectura Master/Slave:**
- **NameNode (mestre):** gestiona les **metadades** (quins blocs formen cada fitxer i on són). Node crític.
- **Secondary NameNode:** manteniment de la imatge de metadades (NO és un backup/failover).
- **DataNode (esclaus):** emmagatzematge físic dels blocs.

> CLI: `hadoop fs -copyFromLocal ...`

Relacionat: [[Hadoop]] · [[MapReduce]] · [[Big Data i Teorema CAP]]

#assignatura/SD #tipus/teoria
