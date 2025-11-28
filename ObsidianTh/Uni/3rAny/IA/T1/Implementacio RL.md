
# [[Implementació RL]] > Arquitectura

L'arquitectura es divideix en dos blocs principals que han de interactuar: l'**Entorn** (El món) i l'**Agent** (El cervell).

## 1. Estructures de Dades (La Memòria)

Com representem $V(s)$ i la Política $\pi$?

- **L'Estat ($s$):** Ha de ser _hasheable_ (únic i immutable).
    
    - _Exemple GridWorld:_ Una tupla `(x, y)`.
        
- **La Taula de Valors ($V$):**
    
    - **Estructura:** Un Diccionari (Hash Map).
        
    - **Clau:** L'estat $s$.
        
    - **Valor:** Un `float` (l'estimació de recompensa futura).
        
    - _Per què?_ És ràpid $O(1)$ i permet estats dispersos. Si l'estat no existeix al diccionari, retorna $0$ (o valor inicial).
        
- **La Política ($\pi$):**
    
    - Pot ser una funció lògica o un altre diccionari si és una taula fixa.
        

---

## 2. L'Entorn (Environment)

Aquest bloc encapsula la funció de Transició $T$ i la de Recompensa $R$. L'agent **no** ha de saber com funciona per dins, només el crida.

### Funció Principal: `step(action)`

Aquesta és la funció més crítica. Simula el pas del temps.

- **Input:** L'acció triada per l'agent (ex: "NORD").
    
- **Lògica interna:**
    
    1. Calcula la nova posició basada en la física del joc (determinista o amb probabilitat).
        
    2. Comprova si hi ha recompensa en la nova casella ($R$).
        
    3. Comprova si el joc s'ha acabat (és terminal?).
        
- **Output (Return):** Una tupla `(next_state, reward, done)`.
    

> [!TIP] Implementació
> 
> Al teu codi, l'agent farà: s_nou, r, final = env.step(accio)

---

## 3. L'Agent (The Brain)

Aquí implementes les fórmules matemàtiques que tenies a la nota.

### A. Funció `predict_value(state)`

Simplement consulta la taula $V$.

- **Lògica:** `return V_table[state]` (si no existeix, retorna 0.0).
    

### B. Funció `update_value(s, s_next, r)` (El Core de l'Aprenentatge)

Aquí implementes la fórmula de **Temporal Difference**. És la funció que crides _després_ de moure't per aprendre de l'experiència.

**Pseudocodi conceptual:**

1. Obtenir predicció actual: `prediccio_actual = V[s]`
    
2. Obtenir predicció futura: `prediccio_futura = V[s_next]`
    
3. Calcular el Target (Realitat): `target = r + (gamma * prediccio_futura)`
    
4. Calcular l'Error (TD Error): `error = target - prediccio_actual`
    
5. Actualitzar taula: `V[s] = prediccio_actual + (alpha * error)`
    

### C. Funció `choose_action(state)` (La Política $\pi$)

Com tria l'agent què fer? Aquí necessitem l'estratègia **Epsilon-Greedy** que mencionaves ("arriscant-se per aprendre").

- **Input:** Estat actual.
    
- **Paràmetre $\epsilon$ (Epsilon):** Probabilitat d'explorar (ex: 0.1 o 10%).
    
- **Lògica:**
    
    1. Generar número aleatori entre 0 i 1.
        
    2. **Si numero < $\epsilon$ (Exploració):** Tria una acció a l'atzar de la llista d'accions disponibles.
        
    3. **Si numero > $\epsilon$ (Explotació):** Mira els estats veïns possibles, consulta els seus valors a $V$, i tria el que tingui el $V$ més alt.
        

---

## 4. El Bucle Principal (Training Loop)

Com s'uneix tot? Necessites un bucle que repeteixi "episodis" del joc.

Python

```
# Pseudocodi d'alt nivell

Per a cada episodi (1 a 1000):
    estat_actual = env.reset() # Reiniciem el joc
    fet = Fals
    
    Mentre no fet:
        # 1. DECIDIR (Política)
        accio = agent.choose_action(estat_actual)
        
        # 2. ACTUAR (Transició i Recompensa)
        estat_seguent, recompensa, fet = env.step(accio)
        
        # 3. APRENDRE (Actualització de V)
        # Important: Li passem el que ha passat per ajustar V(s)
        agent.update_value(estat_actual, estat_seguent, recompensa)
        
        # 4. AVANÇAR
        estat_actual = estat_seguent
```

---

## Resum d'Implementació

|**Funció**|**Responsabilitat**|**On viu?**|**Fórmula associada**|
|---|---|---|---|
|`step()`|Física del món i regles|Entorn|$T(s,a,s'), R(s,a)$|
|`update()`|Corregir l'error de predicció|Agent|$V(s) \leftarrow V(s) + \alpha(r + \gamma V(s') - V(s))$|
|`choose()`|Decidir moure's (Exploració vs Explotació)|Agent|$\pi(s) = \text{argmax}_a ...$|

---

**Vols que et detalli com implementar la funció `choose_action` específicament quan _no_ tens accés directe a la funció de transició $T$ (model-free)?** (Això sol requerir Q-Learning en lloc de només V).