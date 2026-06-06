Framework de [[Big Data i Teorema CAP|Big Data]] que supera les limitacions de [[MapReduce]] per a programes de **múltiples passades** (algorismes iteratius de ML, grafs, mineria interactiva, streaming).

**Spark vs Hadoop:** MapReduce llegeix/escriu a **disc** (HDFS) a cada pas (latència alta). Spark manté les dades en **memòria distribuïda** mitjançant els [[RDD]], usant la **traçabilitat (lineage)** per a la tolerància a fallades en lloc de la replicació física.

Implementat en **Scala**; APIs per a Python i Java.

**Topologia:** **Driver Program** (orquestra) + **Worker Nodes** (executen Tasks, cada Worker té un Executor amb Cache). El **Cluster Manager** assigna recursos. L'objecte **SparkContext** (`sc`) és el punt d'entrada.

Conceptes: [[RDD]] · [[Transformacions i Accions]] · [[Variables Compartides]].

Relacionat: [[Hadoop]] · [[MapReduce]] · [[RDD]]

#assignatura/SD #tipus/teoria
