# Introducció
La formalització és el procés de traduir expressions del llenguatge natural a fórmules del llenguatge de predicats. 

>[!info] Pq és important?
>Una mala interpretació inicial invalida qualsevol deducció posterior. Disposem de quatre regles fonamentals per a estructures categòriques:

# Interpretacions
- **Universals Afirmatives:** "Tot A és B":
    
    $$\forall x(Ax\rightarrow Bx)$$

   Per exemple, "A tots els esquiadors ($Ex$) els agrada la neu ($Nx$)" esdevé $\forall x(Ex\rightarrow Nx)$.

![[Pasted image 20260307193500.png]]
![[Pasted image 20260307193535.png]]
- **Universals Negatives:** "Cap A és B" s'expressa com la inexistència de la propietat B per a tot element de A:
    
    $$\forall x(Ax\rightarrow\neg Bx)$$
    
    Un cas pràctic seria "A cap montanyer li agrada la pluja": $\forall x(Mx\rightarrow\neg Lx)$.
    
- **Existencials Afirmatives:** "Algún A és B" requereix l'ús de la conjunció per indicar que existeix almenys un individu que compleix ambdues propietats:
    
    $$\exists x(Ax\wedge Bx)$$
    
- **Existencials Negatives:** "Algún A no és B" es formalitza com:
    
    $$\exists x(Ax\wedge\neg Bx)$$
    
### **Complexitat i Constants:**
Quan apareixen relacions entre objectes (com "clients de bancs"), utilitzem:
- predicats n-aris 
	- ($Cxy$ per "$x$ és client de $y$") 
	
- quantificadors niats:
	- $\forall x(Bx\rightarrow\exists z(Czx\wedge Dz))$. 
	
Si ens referim a un individu concret (com en Joan), utilitzem constants ($c$): $\forall x(Axc\rightarrow Lx)$.


---

# Variables i Fórmules Tancades

Dins d'una fórmula, la funció de les variables pot variar segons la seva interacció amb els quantificadors. 

- **Aparició Lliure:** Una variable $x$ és lliure en una fórmula si no està dins de l'abast d'un quantificador ($\forall$ o $\exists$) que l'afecti directament. En cas contrari és lligada

- **Aparició Lligada:** Es diu que una aparició és lligada quan està afectada per un quantificador.
![[Pasted image 20260307193647.png]]

- **Fórmules Tancades (Sentències):** Una fórmula es considera tancada si no conté cap variable lliure. 
	- Per exemple, $$\forall x\forall y(Rxy\rightarrow\exists z(Rxz\wedge Rzy))$$ és tancada perquè totes les instàncies de $x$, $y$, $z$ estan lligades.
	- En canvi, si tenim $\forall x(Rxy\wedge\exists z(Pz\vee Rxz))$, la variable $y$ és lliure, fent que la fórmula no sigui tancada.
    
>[!warning] Important
>Sovint se us demanarà classificar variables; recordeu que una mateixa variable pot aparèixer com a lliure i lligada en diferents subfórmules, però la fórmula només és tancada si totes les seves aparicions estan lligades.


---

# Interpretacions i Avaluació de Termes

La semàntica ens permet donar significat real als símbols abstractes. 

>[!info] Interpretació
>Una interpretació ($I$) és una estructura que defineix el context on operem

- **Domini ($D$):** Un conjunt no buit d'elements sobre els quals parlem (ex: els enters, els humans, etc.).
	- $D^n$ Denota el producte cartesia de D n cops

- **Assignacions de la Interpretació:**
    
    - A cada variable $x$, se li assigna un element $I(x)\in D$.
    
    - A cada constant $c$, se li assigna un element fix $I(c)\in D$.
    
    - A cada símbol de funció $f$ de $n$ arguments, se li associa una funció real sobre el domini ($I(f):D^n\rightarrow D$).
    
    - A cada símbol de predicat $R$, se li associa una relació o subconjunt del domini ($I(R)\subseteq D^n$).
        
## **Avaluació de Termes:** 
Per avaluar un terme $t$, substituïm els seus components per les seves interpretacions. 

>[!quote] Per exemple
> si $$I(a)=2$$, $$I(v_2)=6$$ i $I(f)$ és la suma, 
> 
> llavors $I(f(a,v_2))=2+6=8$. 
> 
> - El resultat d'avaluar un terme és sempre un element del domini $D$.
>  $$I(g(b, v3)) = 3 × 9 = 27$$
> $$I(f (a, g(b, v3))) = 2 + 27 = 29.$$



---

# Avaluació de Fórmules i Veritat

A diferència dels termes, l'avaluació d'una fórmula dóna com a resultat un valor de veritat: Vertader ($V$) o Fals ($F$).

- **L'assignació modificada $I_x^a$:** És una eina tècnica fonamental. Defineix una nova interpretació que és idèntica a $I$, excepte que a la variable $x$ se li assigna l'element $a$ del domini. Això és crucial per avaluar quantificadors.
![[Pasted image 20260307195437.png]]
- **Regles d'Avaluació:**
	![[Pasted image 20260307195505.png]]
	![[Pasted image 20260307195641.png]]
### Cas 1: Avaluació en Dominis Finits (Mètode Exhaustiu)

Quan el domini té un nombre reduït i discret d'elements, podem avaluar quantificadors existencials ($\exists$) i universals ($\forall$) simplement iterant sobre tots els possibles valors.

Considerem l'exemple on el domini de $I=\{0,1\}$ , la constant $\overline{a}=0$ , i la fórmula a avaluar és $\varphi_1=\exists x(Px\wedge Qxa)$. A més, l'enunciat ens indica que $\overline{P}0=F$ i $\overline{Q}10=F$.

- **Pas 1 (Traducció):** Com que tenim un quantificador existencial, la fórmula s'interpreta mitjançant l'expressió "existeix $n\in\{0,1\}$ tal que $\overline{P}n=V$ i $\overline{Q}n0=V$".
    
- **Pas 2 (Avaluació per $n=0$):** Substituïm la variable per l'element $0$. Verifiquem la primera part de la conjunció: $\overline{P}0$. Com que la nostra interpretació diu que $\overline{P}0=F$, la conjunció ja és falsa.
    
- **Pas 3 (Avaluació per $n=1$):** Substituïm la variable per l'element $1$. Verifiquem la segona part de la conjunció: necessitem que $\overline{Q}10=V$. Però el nostre model estableix que $\overline{Q}10=F$.
    
- **Conclusió:** Com que hem esgotat tots els elements del domini $\{0,1\}$ i cap d'ells fa certa la conjunció, podem concloure de manera determinant que $I(\varphi_1)=F$.
    

### Cas 2: Avaluació en Dominis Infinits (Mètode de Raonament i Contraexemples)

Davant d'un domini infinit, l'avaluació exhaustiva és impossible computacionalment. Cal analitzar les condicions lògiques globals que imposen els quantificadors per trobar o bé una regla general que demostri la veritat, o bé un contraexemple que invalidi la fórmula.

Considerem el domini dels nombres enters , on el predicat $I(P)$ simbolitza la relació "$\le$" , i la fórmula és $\varphi_5=\forall v_0\forall v_1\exists v_2(Pv_0v_2\wedge Pv_2v_0)$.

- **Pas 1 (Traducció):** Amb tres variables lligades, el significat de $\varphi_5$ és la condició general: "per a tot enter $n_0$ i per a tot enter $n_1$ existeix un enter $n_2$ tal que $n_0\le n_2$ i $n_2\le n_1$".
    
- **Pas 2 (Anàlisi lògica):** La fórmula afirma que, trieu quins trieu com a enters $n_0$ i $n_1$, **sempre** podreu trobar un altre enter $n_2$ que estigui al mig d'ells (o que sigui igual).
    
- **Pas 3 (Cerca del contraexemple):** Per desmentir un "per a tot" ($\forall$), només necessitem un cas concret on falli. Penseu en valors on l'ordre natural es contradigui. Aquesta condició és manifestament falsa si forcem que $n_0>n_1$. Per exemple, si triem $n_0=3$ i $n_1=2$.
    
- **Conclusió:** Amb aquests valors fixats, caldria trobar un enter $n_2$ tal que $3\le n_2$ i $n_2\le 2$. Com que això és matemàticament impossible en el domini dels enters, el contraexemple és ferm. Per tant, dictaminem que $I(\varphi_5)=F$.
    

---

## 5. Equivalències Lògiques

Dues fórmules són lògicament equivalents ($\varphi\equiv\psi$) si tenen el mateix valor de veritat en totes les interpretacions possibles.

- **Lleis de Negació (De Morgan per a quantificadors):**
    
    $$\neg\forall x\varphi\equiv\exists x\neg\varphi$$
    
    $$\neg\exists x\varphi\equiv\forall x\neg\varphi$$
    
- **Lleis de Distribució (amb restriccions):** Si $x$ no apareix lliure en $\psi$, podem "treure" el quantificador fora d'una conjunció o disjunció: $Qx(\varphi\wedge\psi)\equiv Qx\varphi\wedge\psi$.
    
- **Distribució Pura:**
    
    - $\forall x$ es distribueix sobre la conjunció ($\wedge$): $\forall x(\varphi\wedge\psi)\equiv\forall x\varphi\wedge\forall x\psi$.
        
    - $\exists x$ es distribueix sobre la disjunció ($\vee$): $\exists x(\varphi\vee\psi)\equiv\exists x\varphi\vee\exists x\psi$.
        
- **Demostració d'equivalència:** Per provar que $\neg\exists x\forall y(Px\wedge\neg Rxy)\equiv\forall x\exists y(Px\rightarrow Rxy)$, apliquem les lleis pas a pas: neguem el quantificador, apliquem De Morgan internament i usem la definició de l'implicador ($\neg A\vee B\equiv A\rightarrow B$).
    
- **Contraexemples:** Per demostrar que dues fórmules no són equivalents (ex: $Pc$ i $\exists xPx$), n'hi ha prou amb trobar una única interpretació on una sigui $V$ i l'altra $F$.
    
