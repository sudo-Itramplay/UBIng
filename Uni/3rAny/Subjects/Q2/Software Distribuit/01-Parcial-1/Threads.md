Els **fils (threads)** són la clau de la concurrència en el [[Model Client-Servidor]]. Un servidor d'un sol fil queda "segrestat" per un client lent (les operacions de xarxa són **bloquejants**).

**Estratègia:** un **Fil Principal (Listener)** només escolta i accepta connexions; per cada client delega la comunicació a un **fil Worker**. Així s'atenen múltiples clients de manera concurrent ([[Tipus de Servidors]]).

Un thread és una unitat dins d'un [[Procés i Thread|procés]] que **comparteix recursos** amb la resta. Útil per: aprofitar múltiples nuclis, modelar tasques independents, esdeveniments asíncrons i responsivitat (UI).

Conceptes: [[Threads a Java]] · [[Problemes de Concurrència]] · [[Sincronització en Java]] · [[Coordinació de Threads]].

Relacionat: [[Procés i Thread]] · [[Tipus de Servidors]] · [[Sincronització]]

#assignatura/SD #tipus/teoria
