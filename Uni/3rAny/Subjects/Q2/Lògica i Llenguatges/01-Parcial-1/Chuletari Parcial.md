> [!note] Vegeu [[Equivalència Lògica]] · [[Equivalències en Predicats]] · [[Forma Normal Conjuntiva]] · [[Regla de Resolució]] · [[Davis-Putnam]] · [[CHULETARI EQUIVALÈNCIES]]

## Ⅰ. Taula d'Equivalències Lògiques

### 1. Regles de la Implicació i Doble Implicació

- **Implicació:** $\varphi\rightarrow\psi\equiv\neg\varphi\vee\psi$. Transforma una condicional en una disjunció; pas clau per eliminar fletxes en FNC.
    
- **Contrapositiva:** $\varphi\rightarrow\psi\equiv\neg\psi\rightarrow\neg\varphi$. Inverteix el sentit de la implicació negant ambdós termes.
    
- **Doble Implicació:** $\varphi\leftrightarrow\psi\equiv(\varphi\rightarrow\psi)\wedge(\psi\rightarrow\varphi)$. Descompon l'equivalència en dues implicacions mútues.
    

### 2. Regles de la Negació

- **Doble Negació:** $\neg(\neg\varphi)\equiv\varphi$. Dues negacions s'anul·len.
    
- **De Morgan (Disjunció):** $\neg(\varphi\vee\psi)\equiv\neg\varphi\wedge\neg\psi$. La negació d'un "O" passa a ser un "I" de negats.
    
- **De Morgan (Conjunció):** $\neg(\varphi\wedge\psi)\equiv\neg\varphi\vee\neg\psi$. La negació d'un "I" passa a ser un "O" de negats.
    
- **Negació de la Implicació:** $\neg(\varphi\rightarrow\psi)\equiv\varphi\wedge\neg\psi$. Útil per trobar contraexemples on l'antecedent és V i el conseqüent F.
    

### 3. Lleis de l'Àlgebra Proposicional

- **Llei Distributiva:** $\varphi\vee(\psi\wedge\chi)\equiv(\varphi\vee\psi)\wedge(\varphi\vee\chi)$. Fonamental per portar fórmules a FNC (separar els "I").
    
- **Llei d'Absorció:** $(\varphi\vee\psi)\wedge\varphi\equiv\varphi$ i $(\varphi\wedge\psi)\vee\varphi\equiv\varphi$. Simplificació directa de termes redundants.
    
- **Simplificació amb Constants:** $\varphi\vee V\equiv V$, $\varphi\vee F\equiv\varphi$, $\varphi\wedge V\equiv\varphi$, $\varphi\wedge F\equiv F$.
    

### 4. Equivalències de Predicats (Quantificadors)

- **Negació de Quantificadors:** $\neg\forall x\varphi\equiv\exists x\neg\varphi$ i $\neg\exists x\varphi\equiv\forall x\neg\varphi$.
    
- **Distribució Pura:** $\forall x(\varphi\wedge\psi)\equiv\forall x\varphi\wedge\forall x\psi$ i $\exists x(\varphi\vee\psi)\equiv\exists x\varphi\vee\exists x\psi$.
    
- **Moviment de Quantificador:** Si $x$ no apareix lliure en $\psi$, llavors $Qx(\varphi \circ \psi) \equiv (Qx \varphi) \circ \psi$.
    

---

## Ⅱ. Metodologies per Temes

### 1. Formalització de Llenguatge Natural

- **Suficiència ("Si A, llavors B"):** $A\rightarrow B$.
    
- **Necessitat ("A només si B"):** $A\rightarrow B$. L'acció de ploure (A) obliga a que hi hagi núvols (B).
    
- **Universals:** "Tot A és B" $\rightarrow \forall x(Ax\rightarrow Bx)$.
    
- **Existencials:** "Algún A és B" $\rightarrow \exists x(Ax\wedge Bx)$.
    

### 2. Obtenció de la Forma Normal Conjuntiva (FNC)

1. **Eliminar fletxes:** Substituir $\rightarrow$ i $\leftrightarrow$ per $\neg$ i $\vee$.
    
2. **Interioritzar negacions:** Aplicar De Morgan fins que les negacions només afectin a àtoms (literals).
    
3. **Distribuir:** Aplicar $\vee$ sobre $\wedge$ per tenir una llista de clàusules unides per "I".
    

### 3. Mètode de Resolució (Algorisme)

Per demostrar que $\{\varphi_1, \dots, \varphi_n\} \models \psi$:

1. **Negar la conclusió:** Afegir $\neg\psi$ al conjunt de premisses.
    
2. **Passar a FNC:** Convertir tot a clàusules.
    
3. **Aplicar Regla de Resolució:** Buscar literals oposats ($L$ i $\neg L$) en dues clàusules i crear el resolvent amb la resta de literals.
    
4. **Èxit:** Si arribes a la **clàusula buida** $()$, el raonament és vàlid (contradicció trobada).
    

### 4. Simplificació Davis-Putnam (DPLL)

S'apliquen tres regles recursivament:

- **TAU (Tautologia):** Elimina qualsevol clàusula que contingui $P \vee \neg P$.
    
- **CE (Clàusula Elemental):** Si hi ha un literal sol $L$, elimina les clàusules que el contenen i esborra $\neg L$ de les altres.
    
- **PU (Literal Pur):** Si un literal $L$ apareix en la fórmula però $\neg L$ no apareix mai, elimina totes les clàusules que contenen $L$.
    

### 5. Skolemització (Predicats a Forma Clausal)

Per eliminar $\exists x$ en un conjunt de quantificadors:

- **Si $\exists x$ NO està sota cap $\forall$:** Substitueix $x$ per una constant nova ($a, b, c$).
    
- **Si $\exists x$ està sota $\forall y_1, \dots, \forall y_n$:** Substitueix $x$ per una funció $f(y_1, \dots, y_n)$.
    

### 6. Autòmates (AFD/AFN)

- **AFD (Determinista):** Per cada estat i símbol només hi ha una transició possible.
    
- **AFN (Indeterminista):** Pot haver-hi múltiples camins o transicions buides ($\lambda$).
    
- **Criteri d'acceptació:** Una paraula s'accepta si almenys un camí possible acaba en un estat final ($F$).
    
- **Simplificació:** Fusió d'estats indistingibles (equivalents) per reduir memòria.
    

---

> [!TIP]
> 
> **Recordatori Semàntic:** 
> - **Clàusula buida ()** = Contradicció (Impossible de complir). 
> - **Conjunció buida (I)** = Tautologia (Sense restriccions, sempre Cert).

