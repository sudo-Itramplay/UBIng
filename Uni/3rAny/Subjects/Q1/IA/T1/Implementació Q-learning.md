Excel·lent decisió. El **Q-Learning** és l'algorisme _Model-Free_ per excel·lència.

La diferència fonamental amb el que t'he explicat abans és que ara no aprenem "com de bo és un estat" ($V(s)$), sinó "**com de bo és fer una acció concreta en un estat concret**" ($Q(s, a)$). Això elimina la necessitat de conèixer la funció de transició $T$ per prendre decisions.

Aquí tens el disseny modular per implementar Q-Learning.

---

# [[Implementació Q-Learning]] > Arquitectura

## 1. Estructura de Dades: La Q-Table

Aquesta és la memòria de l'agent. En lloc d'una llista per estats, necessitem una matriu o diccionari bidimensional.

- **Concepte:** Una taula de consulta (Lookup Table).
    
- **Clau (Key):** La parella `(estat, acció)`.
    
- **Valor (Value):** $Q(s, a)$ (Qualitat de l'acció). `Float`.
    
- **Implementació recomanada:** Un Diccionari (Hash Map) on la clau és una tupla.
    
    - `Q[(0,0), 'NORD'] = 0.5`
        
    - `Q[(0,0), 'SUD'] = -0.1`
        

> [!TIP] Inicialització
> 
> Si la parella (s, a) no existeix al diccionari, la teva funció ha de retornar 0.0 per defecte. Això és l'optimisme inicial (o neutralitat).

---

## 2. Hiperparàmetres (Configuració)

Defineix aquestes constants a l'inici de la classe Agent:

- **$\alpha$ (Alpha - Learning Rate):** (Ex: `0.1`). Com de ràpid oblidem el passat.
    
- **$\gamma$ (Gamma - Discount Factor):** (Ex: `0.99`). Importància del futur.
    
- **$\epsilon$ (Epsilon - Exploration Rate):** (Ex: `1.0` inicialment, baixant a `0.1`). Probabilitat de fer bogeries (explorar).
    

---

## 3. Funcions "Core" de l'Agent

Aquí tens les dues funcions que necessites programar.

### A. La Política: `choose_action(state)`

Aquesta funció decideix què fer basant-se en la Q-Table actual. Utilitzarem **Epsilon-Greedy**.

**Algorisme:**

1. Tira un dau (`random.uniform(0, 1)`).
    
2. **Branca Exploració (si dau < $\epsilon$):**
    
    - Retorna una acció aleatòria de l'espai d'accions (Ex: `random(['N', 'S', 'E', 'O'])`).
        
3. **Branca Explotació (si dau > $\epsilon$):**
    
    - Busca a la Q-Table totes les accions possibles per a l'estat actual `state`.
        
    - Troba quina acció té el **valor Q màxim**.
        
    - $$a^* = \arg\max_{a} Q(s, a)$$
        
    - Retorna aquesta acció.
        

> [!WARNING] Nota d'implementació
> 
> Si totes les accions tenen Q = 0 (al principi), l'explotació hauria de triar una a l'atzar entre elles, no sempre la primera de la llista, per evitar biaixos.

### B. L'Aprenentatge: `learn(state, action, reward, next_state)`

Aquesta funció actualitza la Q-Table després de cada pas. Implementa l'equació de Bellman per a Q-Learning.

Fórmula Matemàtica:

$$Q(s,a) \leftarrow Q(s,a) + \alpha \left[ r + \gamma \cdot \max_{a'} Q(s', a') - Q(s,a) \right]$$

**Passos d'Implementació:**

1. Recuperar el valor actual:
    
    q_actual = Q_table[(state, action)]
    
2. **Calcular el valor màxim futur (Max Q):**
    
    - Mira l'estat següent (`next_state`).
        
    - Quina és la millor acció possible des d'allà? No importa quina acció prenguis realment després, Q-Learning és _off-policy_, assumeix que en el futur jugaràs perfecte.
        
    - `max_q_futur = max([Q_table[(next_state, a)] for a in accions])`
        
3. Calcular l'Objectiu (Target):
    
    target = reward + (gamma * max_q_futur)
    
    (Nota: Si next_state és terminal, max_q_futur ha de ser 0).
    
4. Calcular l'Error (TD Error):
    
    error = target - q_actual
    
5. Actualitzar la Taula:
    
    Q_table[(state, action)] = q_actual + (alpha * error)
    

---

## 4. Integració al Bucle de Joc

Així és com crides les funcions des del teu `main`:

Python

```
# Dins del bucle de l'episodi...

# 1. L'agent decideix (sense saber on anirà a parar)
accio = agent.choose_action(estat_actual)

# 2. L'entorn respon
estat_seguent, recompensa, done = env.step(accio)

# 3. L'agent aprèn DE LA TRANSICIÓ COMPLETA
# Important: Passem 'estat_seguent' perquè la funció learn calculi el max_q_futur
agent.learn(estat_actual, accio, recompensa, estat_seguent)

# 4. Actualitzem índexs
estat_actual = estat_seguent

# 5. Decaïment de l'exploració (Opcional però recomanat)
# Al final de cada episodi, redueix epsilon lleugerament
# agent.epsilon = agent.epsilon * 0.995
```

---

**Vols que et doni un exemple concret de com gestionar el diccionari Q quan l'estat o l'acció encara no s'han visitat mai (per evitar errors de clau no trobada)?**



EXEMPLE 
rata en una cinta transportadora, on si tarda més de 7s en arribar donem recompensa


s=(posició, temps, velocitat)

acions = (incrmenetar velocitat en un cert delta), (quedarse parat), (disminuir velocitat en un cert delta)

$$
-x_k = x_0 t - v_k t
$$
