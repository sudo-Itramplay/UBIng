
# [[Machine Learning]] > Tipus d'Aprenentatge

## 1. Aprenentatge Supervisat

> [!SUMMARY] Concepte Clau
> 
> Disposem d'un conjunt de dades etiquetat (Ground Truth). L'objectiu és aprendre una funció que mapegi entrades a sortides.

- **Exemple:** Classificador d'imatges.
    
    - **Input ($x$):** Imatge (píxels).
        
    - **Output ($y$):** Etiqueta (ex: "Gat", "Gos").
        
- **Mecanisme:** Minimitzar l'error entre la predicció i l'etiqueta real.
    

---

## 2. Aprenentatge per Reforç (Reinforcement Learning - RL)

> [!ABSTRACT] Definició
> 
> Un agent aprèn a prendre decisions seqüencials en un entorn incert per maximitzar una recompensa acumulada a llarg termini. És com aprendre un joc de taula sense saber les regles: proves, t'equivoques, i recordes què t'ha donat punts.

### Components del Problema (MDP)

El problema es modela com un **Procés de Decisió de Markov (MDP)** definint la tupla $<S, A, T, R, \gamma>$:

- **$S$ (Estats):** On soc? La situació actual de l'agent.
    
- **$A$ (Accions):** Què puc fer? Ex: $A = \{\text{Nord, Sud, Est, Oest}\}$.
    
- **$T$ (Funció de Transició):** $T(s, a, s') = P(s' | s, a)$.
    
    - Si faig l'acció $a$ a l'estat $s$, quina probabilitat tinc d'acabar a $s'$?
        
    - _Nota:_ Si és **determinista** (probabilitat 1), sempre vaig on vull. Si és estocàstic, hi ha incertesa.
        
- **$R$ (Funció de Recompensa):** $R(s, a, s')$. El reforç immediat (pot ser positiu o negatiu).
    
    - _Living Penalty:_ Sovint s'assigna una petita recompensa negativa (-0.01) per cada pas per incentivar l'agent a trobar l'objectiu ràpidament.
        
- **$\gamma$ (Factor de Descompte):** $0 \leq \gamma \leq 1$. Valora més les recompenses immediates vs. les futures.
    

### El Problema de l'Aprenentatge (Model-Free vs Model-Based)

Al principi, sovint **no coneixem** ni $T$ (la física del món) ni $R$ (què és bo o dolent).

- **Objectiu:** Trobar una **Política ($\pi$)** òptima sense tenir el mapa complet inicialment.
    
- **Exploració vs. Explotació:** Al principi l'agent actua aleatòriament (exploració) per descobrir el mapa. Més tard, usa el coneixement adquirit (explotació).
    

---

## 3. Funcions de Valor i Actualització

### Funció de Valor ($V$)

- **Definició:** $V(s)$ ens diu "que tan bo és estar a l'estat $s$".
    
- **Inicialització:** Sol ser un vector amb valors petits o zero (ex: $\vec{V} = [0.01, \dots, 0.01]$).
    
- **Limitació:** $V(s)$ per si sol **no ens diu quina acció prendre** si no coneixem la funció de transició $T$. Només ens diu com de bo és l'estat.
    

### Temporal Difference (TD) Learning

Aquí és on corregim la teva fórmula. Utilitzem l'**Error de Predicció de Recompensa (RPE)**.

Quan l'agent es mou de $s_t$ a $s_{t+1}$ i rep una recompensa $r$, s'adona que la seva estimació anterior $V(s_t)$ era incorrecta.

**Fórmules clau:**

1. Objectiu TD (Target): La realitat observada + el valor futur descomptat.
    
    $$\text{Target} = r + \gamma V(s_{t+1})$$
    
2. TD Error ($\delta$): La diferència entre la realitat (Target) i el que esperàvem.
    
    $$\delta = (r + \gamma V(s_{t+1})) - V(s_t)$$
    
3. Regla d'Actualització: Corregim el valor anterior amb una taxa d'aprenentatge $\alpha$ (alfa).
    
    $$V(s_t) \leftarrow V(s_t) + \alpha \cdot \delta$$
    

> [!NOTE] Interpretació
> 
> Si $\delta > 0$, el resultat ha estat millor de l'esperat $\to$ pugem el valor de $V(s_t)$.
> 
> Si $\delta < 0$, el resultat ha estat pitjor $\to$ baixem el valor.

---

## 4. Política ($\pi$) vs. Valor ($V$)

És crucial diferenciar aquests dos conceptes:

|**Concepte**|**Símbol**|**Descripció**|
|---|---|---|
|**Value Function**|$V(s)$|**Predicció**. Quant de retorn espero obtenir des d'aquí? Aprens la distribució de la recompensa.|
|**Policy**|$\pi(s)$|**Control**. El "cervell" o estratègia. Mapeja Estats $\to$ Accions.|

- **Policy Iteration:** Tenim una política fixa, avaluem el seu valor $V_{\pi}$, i després millorem la política per ser més "garrepa" (greedy) respecte a aquests valors.
    
- **Value Iteration:** Iterem directament sobre els valors fins a convergir.
    

> [!WARNING] Matís Important
> 
> Has anotat: "V no dona cap criteri per triar".
> 
> - Correcte si **no tens model ($T$)**: Necessites aprendre $Q(s,a)$ (Q-Learning) en lloc de només $V(s)$.
>     
> - Si **tens model ($T$)**: Amb $V(s)$ pots triar mirant quin estat següent té el $V$ més alt (Lookahead).
>     

[[Implementacio RL]]
[[Implementació Q-learning]]

MAI POSAR epsilon a 1 pq sempre necessitem cert grau d'aprenentatge

Acabarem quan la delta sigui 0

Per veure si hem après hem de mirar quan els valors de les taules s'estabilitzim

cada 100 iteracions mostrar, inicial, més propera i final (creo)