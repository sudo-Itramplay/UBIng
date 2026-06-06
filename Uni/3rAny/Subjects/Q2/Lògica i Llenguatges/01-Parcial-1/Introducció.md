## 1. Introducció i Aplicacions de la Lògica

La lògica no és només filosofia; és la base del càlcul. Ens interessa com implementar processos d'inferència en un ordinador.

- **Definició:** Estudi dels raonaments i processos d'inferència per obtenir conclusions correctes a partir de premisses.
    
- **En Informàtica:** Ens centrem en inferències implementables en computadors.
    
- **Aplicacions principals:**
    
    1. Disseny de **SAT-solvers** (resolució de problemes pràctics).
        
    2. Verificació de **circuits**.
        
    3. Verificació de **programari**.
        
    4. Programació **declarativa**.
        

> [!INFO] Nota del Professor
>  Per entendre llenguatges de programació basats en lògica (com Prolog), és imprescindible dominar aquests fonaments proposicionals.

---

## 2. Proposicions i Connectives Bàsiques

Abans de construir fórmules complexes, hem de definir què és una proposició i com les unim.

- **Proposició:** Frase declarativa de la qual té sentit dir si és **Veritable (V)** o **Falsa (F)**.
    
    - _Exemples:_ "7 > arrel de 50", "Avui és festiu".
        
- **Valors de Veritat:** $V$ (Verdader) i $F$ (Fals).
    

### Connectives (Taules de Veritat)

1. **Negació ($\neg \varphi$):** Inverteix el valor. Si $\varphi$ és V, $\neg \varphi$ és F.
    
2. **Disjunció ($\varphi \vee \psi$):** "OR" lògica. És V si **almenys una** és V.
    
3. **Conjunció ($\varphi \wedge \psi$):** "AND" lògica. És V només si **totes dues** són V.
    

> [!EXAMPLE] Exemple de Taula de Veritat (Conjunció)
>
>
>

| $\varphi$ | $\psi$ | $\varphi \wedge \psi$ |
| --------- | ------ | --------------------- |
| V         | V      | V                     |
| V         | F      | F                     |
| F         | V      | F                     |
| F         | F      | F                     |

---

## 3. Implicació i Equivalència

Aquestes són les connectives més importants per a la formalització de regles.

- **Condicional ($\varphi \rightarrow \psi$):** Es llegeix "Si $\varphi$, llavors $\psi$".
    
    - $\varphi$: Antecedent.
        
    - $\psi$: Conseqüent.
        
    - **Regla d'or:** Només és Falsa si l'antecedent és V i el conseqüent és F (V $\rightarrow$ F = F). La resta de casos són V.
        
- **Bicondicional / Equivalència ($\varphi \leftrightarrow \psi$):** Es llegeix "$\varphi$ si i només si $\psi$".
    
    - És V quan $\varphi$ i $\psi$ tenen el **mateix valor** de veritat (totes dues V o totes dues F).

---

## 4. Sintaxi: El Llenguatge de Proposicions

Aquí definim formalment com es construeixen les fórmules vàlides.

- **Àtom:** Frase declarativa indivisible (ex: $P, Q, R$).
    
- **Regles de generació de fórmules:**
    
    1. Tot àtom és una fórmula.
        
    2. Si $\varphi$ és fórmula, $\neg \varphi$ també.
        
    3. Si $\varphi, \psi$ són fórmules, llavors $(\varphi \vee \psi)$, $(\varphi \wedge \psi)$, $(\varphi \rightarrow \psi)$, $(\varphi \leftrightarrow \psi)$ també ho són.
        

### Arbres Genealògics

Podem representar l'estructura d'una fórmula mitjançant un arbre que mostra com s'ha construït pas a pas.

> [!ABSTRACT] Exemple d'Arbre Per a la fórmula: $\neg P \rightarrow (Q \leftrightarrow \neg T)$
> 
> 1. L'arrel és la implicació ($\rightarrow$).
>     
> 2. La branca esquerra baixa a $\neg P$ i després a $P$.
>     
> 3. La branca dreta baixa a $(Q \leftrightarrow \neg T)$, que es divideix en $Q$ i $\neg T$ (i finalment $T$).
>     
> 
> _Això ens ajuda a veure l'ordre d'avaluació._.

---

## 5. Formalització del Llenguatge Natural

>[!info] Formalització
>Passar de llenguatge natural (ambigu) a llenguatge de la lògica proposicional (precís)


Com traduïm frases reals a lògica? Aquesta és una part crítica per a l'examen.

- **"A o B"** $\rightarrow A \vee B$.
    
- **"A i B"** $\rightarrow A \wedge B$.
    
- **"Si A, llavors B"** (Suficiència) $\rightarrow A \rightarrow B$.
    
- **"A si i només si B"** $\rightarrow A \leftrightarrow B$.
    
- **⚠️ CAS ESPECIAL:** **"B només si A"** (Necessitat) $\rightarrow B \rightarrow A$.
    

> [!TIP] Diferència clau: "Si" vs "Només si"
> 
> Mira aquests dos exemples de les diapositives:
> 
> 1. **"Plovarà, si hi ha núvols"**: $N \rightarrow L$. (Fals, perquè pot haver-hi núvols i no ploure) .
>     
> 2. **"Plovarà, només si hi ha núvols"**: $L \rightarrow N$. (Verdader, és impossible que plogui sense núvols. La pluja _implica_ l'existència de núvols) .
>     
> 
> _En el cas 2, la pluja (L) obliga a l'existència de núvols (N)._

---

## 6. Interpretacions i Avaluació

Una fórmula per si sola no és V ni F; necessita una interpretació.

- **Interpretació ($I$):** Assignació de valors de veritat (V/F) a cada àtom del conjunt.
    
- **Avaluació ($I(\varphi)$):** Substituir els àtoms pels seus valors en $I$ i calcular el resultat final.
    

> [!check] Exemple de Càlcul
> 
> Fórmula: $\varphi = (P \leftrightarrow Q) \wedge R$
> 
> Interpretació $I$: $P=F, Q=F, R=V$.
> 
> $$I(\varphi) = (F \leftrightarrow F) \wedge V$$
> 
> $$I(\varphi) = V \wedge V$$
> 
> $$I(\varphi) = V$$
> 
> Resultat: La fórmula és certa sota aquesta interpretació.

---

## 7. Propietats Semàntiques

Classifiquem les fórmules segons el seu comportament en **totes** les interpretacions possibles.

1. **Tautologia:** Certa en **totes** les interpretacions (sempre veritat).
    
    - _Ex:_ $P \vee \neg P$.
        
2. **Contradicció (Insatisfactible):** Falsa en **totes** les interpretacions (sempre fals).
    
    - _Ex:_ $P \wedge \neg P$.
        
3. **Satisfactible:** Certa en **almenys una** interpretació.
    
    - _Nota:_ Totes les tautologies són satisfactibles, però no totes les fórmules satisfactibles són tautologies (ex: $P \rightarrow \neg P$).
        

---

## 8. Equivalència Lògica i Àlgebra

Dues fórmules són equivalents ($\varphi \equiv \psi$) si tenen la **mateixa taula de veritat** (el mateix valor per a tota interpretació).

### Regles d'Equivalència Importants

Has de memoritzar aquestes transformacions per simplificar fórmules:

- **Implicació:** $\varphi \rightarrow \psi \equiv \neg \varphi \vee \psi$.
    
- **Contrarecíproc:** $\varphi \rightarrow \psi \equiv \neg \psi \rightarrow \neg \varphi$.
    
- **De Morgan:**
    
    - $\neg(\varphi \vee \psi) \equiv \neg \varphi \wedge \neg \psi$.
        
    - $\neg(\varphi \wedge \psi) \equiv \neg \varphi \vee \neg \psi$.
        
- **Negació de la Implicació:** $\neg(\varphi \rightarrow \psi) \equiv \varphi \wedge \neg \psi$.
    
- **Distributiva:** $\varphi \vee (\psi \wedge \chi) \equiv (\varphi \vee \psi) \wedge (\varphi \vee \chi)$.
    

> [!bug] Demostració d'Equivalència (Regla 12)
> 
> Volem demostrar que negar una implicació equival a afirmar l'antecedent i negar el conseqüent.
> 
> Comparem taules de veritat:
> 
> 1. $\varphi \rightarrow \psi$ és Fals només quan V $\rightarrow$ F.
>     
> 2. Per tant, $\neg(\varphi \rightarrow \psi)$ és Verdader només quan V $\rightarrow$ F.
>     
> 3. La fórmula $\varphi \wedge \neg \psi$ és Verdadera només quan $\varphi=V$ i $\neg \psi=V$ (és a dir, $\psi=F$).
>     
> 
> Com que les taules coincideixen, són equivalents.


# Exercicis
Aquí tens un exemple detallat de com construir un **Arbre de Generació**.

Farem servir l'exemple clau que apareix tant a la **Diapositiva 12-13** com a la **pàgina 3 del PDF de problemes**, ja que és el model canònic per al curs.

+1

---

### Exemple: $\neg P \rightarrow (Q \leftrightarrow \neg T)$

L'objectiu de l'arbre és descomposar la fórmula fins a arribar als seus **àtoms** (les parts indivisibles).

+1

#### 1. Representació Visual (ASCII Art)

Aquest és l'arbre resultant que has de saber dibuixar:

```
graph TD
    A["→ (Implicació)"] --> B["¬ (Negació)"]
    A --> C["↔ (Equivalència)"]
    B --> D[P]
    C --> E[Q]
    C --> F["¬ (Negació)"]
    F --> G[T]
```

> [!NOTE] Estructura en format text (per als teus apunts)
> 
> Plaintext
> 
> ```
>           →
>         /   \
>       ¬      ↔
>       |     /  \
>       P    Q    ¬
>                 |
>                 T
> ```

---

#### 2. Pas a pas: Com es construeix?

Per dibuixar l'arbre, has de seguir l'ordre invers a la construcció de la fórmula. Busquem la **connectiva principal** a cada pas.

1. **Nivell 1 (L'Arrel):**
    
    - Mirem la fórmula completa: $\neg P \rightarrow (Q \leftrightarrow \neg T)$.
    - La connectiva que uneix els dos blocs grans és la **implicació** ($\rightarrow$). Aquesta va a dalt de tot.
    
2. **Nivell 2 (Les branques principals):**
    
    - **Esquerra:** Tenim $\neg P$. La connectiva principal aquí és la **negació** ($\neg$).
    - **Dreta:** Tenim $(Q \leftrightarrow \neg T)$. La connectiva que uneix $Q$ amb la resta és l'**equivalència** ($\leftrightarrow$).

3. **Nivell 3 (Descomposició):**
    
    - A la branca esquerra, sota el $\neg$, ja ens queda l'àtom **$P$**. Aquí s'acaba aquesta branca.

    - A la branca dreta, sota el $\leftrightarrow$, tenim:
        
        - Costat esquerre: L'àtom **$Q$**.
            
        - Costat dret: La sub-fórmula $\neg T$.
            
4. **Nivell 4 (Fulles finals):**
    
    - Descomposem el $\neg T$. La connectiva és $\neg$ i a sota hi queda l'àtom **$T$**.


---

> [!TIP] Regla d'Or del Professor 
> Les **fulles** de l'arbre (els nodes finals de baix de tot) **SEMPRE** han de ser els **àtoms** ($P, Q, T$, etc.). Els nodes intermedis sempre són connectives lògiques ($\vee, \wedge, \rightarrow, \neg$, etc.).
