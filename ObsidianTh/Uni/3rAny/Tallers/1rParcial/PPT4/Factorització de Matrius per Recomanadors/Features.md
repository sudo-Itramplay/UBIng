Relació entre elements donada [[Uni/3rAny/Tallers/1rParcial/PPT4/Factorització de Matrius per Recomanadors/Factoritzar les matrius|de factoritzar matrius]]

- Cada Fila de $P$ representaria la força d'associació entre user i feature
- Cada columna de $Q$ representaria a força entre item i feature

Per fer la predicció de ratingd'un ítem ($d_j$) per $u_i$ calculem el producte de dos vectors corresponents a aquests dos amb un [[Producte Escalar]]

$$
\hat r_{ij} = p_i^Tq_j = \sum_{k=1}^K p_{ki}q_{kj}
$$
on k=el num de feature, K la dimensió de les features

>[!info] Què defineix això?
Com d'alineades estàn les preferències del usuari amb les característiques del ítem
