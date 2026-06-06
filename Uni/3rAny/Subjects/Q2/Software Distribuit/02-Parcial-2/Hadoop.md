Plataforma escalable i robusta per a [[Big Data i Teorema CAP|Big Data]], basada en el treball de Google. **Idea clau:** en lloc de moure les dades cap a la computació, **mou la computació cap on resideixen les dades** (distribuir les dades en guardar-les).

**Principis:** abstracció d'alt nivell, minimitzar comunicacions, distribució a priori, localització de la computació, **replicació** de dades.

Un **clúster** és un conjunt de **nodes** (màquines de propòsit general), escalable fins a milers. Dos components bàsics:
1. **[[HDFS]]** — emmagatzematge distribuït.
2. **[[MapReduce]]** — computació distribuïda.

> Prioritza **Consistència + Tolerància a fallades** sobre la disponibilitat ([[Big Data i Teorema CAP|CP]]).

Relacionat: [[HDFS]] · [[MapReduce]] · [[Spark]] · [[Big Data i Teorema CAP]]

#assignatura/SD #tipus/teoria
