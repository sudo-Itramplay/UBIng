## Introducció als Llenguatges de Predicats

>[!question] Pq els volem?
>Ofereixen una capacitat d'expressió superior als llenguatges de proposicions. Són la base de paradigmes com la **programació lògica**, sent el llenguatge **Prolog** l'exemple més destacat.

---

### 1. Concepte de Predicat

Un predicat és una expressió formal que retorna un valor de tipus **booleà** (cert o fals).

- **Exemples:**
    
    - $x + y = 2$
        
    - $x + y \le z$
        
    - Existeix un enter $i$ tal que l'element d'un vector $A[i] > 100$.
    

---

### 2. Símbols del Llenguatge

Els llenguatges de predicats es construeixen a partir d'un **vocabulari** (conjunt finit de constants, operadors i predicats) i diversos tipus de símbols:

|**Tipus de Símbol**|**Exemples / Descripció**|
|---|---|
|**Variables**|$x, y, z, u, v \dots$|
|**Constants**|$a, b, c, d \dots$|
|**Operadors (Funcions)**|$f, g, h \dots$ (tenen una **aritat** o nombre d'arguments).|
|**Predicats (Relacions)**|$A, B, \dots, Z$ (tenen una **aritat** associada).|
|**Connectives Lògiques**|$\neg, \vee, \wedge, \rightarrow, \leftrightarrow$|
|**Quantificadors**|Existencial ($\exists$) i Universal ($\forall$).|
|**Auxiliars**|Parèntesis $($ $)$, comes $,$ etc.|

---

### 3. Definició de Terme

Els termes s'utilitzen per descriure els elements del domini. Es generen mitjançant aquestes regles:

1. **(T1)** Tota variable és un terme.

2. **(T2)** Tota constant del vocabulari és un terme.

3. **(T3)** Si $f$ és una funció d'$n$ arguments i $t_1, \dots, t_n$ són termes, llavors $f(t_1, \dots, t_n)$ és un terme.


> [!IMPORTANT]
> 
> Un **símbol de predicat MAI pot formar part d'un terme**. Els termes només contenen variables, constants i funcions.

---

### 4. Àtoms i Fórmules

La construcció del llenguatge segueix una jerarquia: de termes a àtoms, i d'àtoms a fórmules.

#### Àtom (o Fórmula Atòmica)

És una expressió de la forma $R(t_1, \dots, t_n)$, on $R$ és un símbol de relació (predicat) i $t_1, \dots, t_n$ són termes.

#### El Llenguatge de Predicats ($\sigma$-fórmules)

El conjunt de fórmules es genera amb les regles següents:

- **(F1)** Tot àtom és una fórmula.
    
- **(F2)** Si $\phi$ és una fórmula, $\neg \phi$ també ho és.
    
- **(F3)** Si $\phi$ i $\psi$ són fórmules, les combinacions amb connectives $(\phi \vee \psi, \phi \wedge \psi, \phi \rightarrow \psi, \phi \leftrightarrow \psi)$ són fórmules.
    
- **(F4)** Si $\phi$ és una fórmula i $x$ una variable, $\exists x \phi$ i $\forall x \phi$ són fórmules.
    
