Millor algoritme de [[Path-finding]]

## Base
Evitar expandir els camins més costosos

## Funcio avaluacio

$$
f(n) = g(n) + h(n)
$$
- g(n) = cost des de l’inici i fins a assolir el node n
- h(n) = cost estimat des del node n fins a l’objectiu
- f(n) = cost estimat de la millor solució que passi per n

>[!warning] Compte Sobre estimar
>Per garantir que l'A* trobi el camí **òptim** (el realment menys costós), l'heurística h(n) ha de ser **admissible**.

- [[Heurística Admissible]]


## LLista oberta

### **Què hi ha?**:
Conté els nodes que **ja s'han descobert** (visitats) però que **encara no s'han expandit** (és a dir, els seus veïns encara no s'han avaluat). Són la **frontera** entre els nodes explorats i els no explorats.

#### **Com s'utilitza?**: 
La llista oberta es gestiona com una **cua de prioritat**, on el node amb el valor **f(n) més baix** (la millor estimació de cost total) sempre té la màxima prioritat i és el següent a ser seleccionat per a l'expansió.

## LLista tancada
### **Què hi ha?**: 
Conté els nodes que **ja s'han expandit completament**. Un cop un node ha passat de la Llista Oberta a la Tancada, vol dir que ja s'ha trobat el camí **més curt conegut** des de l'inici fins a ell.
    
### **Com s'utilitza?**: 
S'utilitza per **evitar bucles infinits** i, crucialment, per **evitar processar el mateix node diverses vegades**. Si un node ja és a la llista tancada, se'l ignora, tret que es trobi un **camí més curt** (amb un g(n) més petit) fins a ell; en aquest cas, es pot reobrir per actualitzar els seus veïns.