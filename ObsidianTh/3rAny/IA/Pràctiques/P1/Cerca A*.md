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

# Pseudocodi
## Components

**`oberts`** Llista de nodes a ser avaluats (amb prioritat segons f(n)).

**`tancats`** Llista de nodes que ja han estat avaluats.


**`g_cost`** Diccionari/Mapa per emmagatzemar el cost g(n) de cada node.


**`pare`** Diccionari/Mapa per emmagatzemar el predecessor de cada node per reconstruir el camí.


### Pseudocodi
```
Funció A_estrella(inici, objectiu):
    // 1. Inicialització
    Inicialitza llista 'oberts' amb el node 'inici'
    Inicialitza llista 'tancats' buida
    
    Per a cada node n:
        g_cost[n] = Infinit
        pare[n] = indefinit
    
    g_cost[inici] = 0
    f_cost[inici] = g_cost[inici] + h(inici, objectiu)

    // 2. Bucle principal
    Mentre 'oberts' no estigui buida:
        // Selecciona el node amb el f_cost més baix
        node_actual = node a 'oberts' amb f_cost mínim
        
        Si node_actual és igual a 'objectiu':
            Retorna Reconstruir_cami(pare, objectiu) // Objectiu trobat
            
        Elimina node_actual de 'oberts'
        Afegeix node_actual a 'tancats'
        
        // 3. Processa veïns
        Per a cada veí de node_actual:
            Si veí està a 'tancats':
                Continua al següent veí // Ignora nodes ja avaluats
            
            // Calcula el g_cost provisional per al veí
            g_provisional = g_cost[node_actual] + Coste_entre(node_actual, veí)
            
            // 4. Actualitza camí
            Si g_provisional < g_cost[veí] O veí NO està a 'oberts':
                // S'ha trobat un camí millor o és un node nou
                pare[veí] = node_actual
                g_cos(t[veí] = g_provisional
                f_cost[veí] = g_cost[veí] + h(veí, objectiu)
                
                Si veí NO està a 'oberts':
                    Afegeix veí a 'oberts'
    
    // 5. No s'ha trobat cap camí
    Retorna Falla

```