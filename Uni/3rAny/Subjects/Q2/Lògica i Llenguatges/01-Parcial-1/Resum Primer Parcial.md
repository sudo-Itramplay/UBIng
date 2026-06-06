# Tema 1 Llenguatge Proposicions

## 1. Introducció i Aplicacions de la Lògica

- **Definició:** Estudi dels raonaments i processos d'inferència per obtenir conclusions correctes a partir de premisses.
    
- **En Informàtica:** Ens centrem en inferències implementables en computadors.
    
- **Aplicacions principals:**
    
    1. Disseny de **SAT-solvers** (resolució de problemes pràctics).
        
    2. Verificació de **circuits**.
        
    3. Verificació de **programari**.
        
    4. Programació **declarativa**.
        

---

## 2. Proposicions i Connectives Bàsiques

Abans de construir fórmules complexes, hem de definir què és una proposició i com les unim.

- **Proposició:** Frase declarativa de la qual té sentit dir si és **Veritable (V)** o **Falsa (F)**.
    
    - _Exemples:_ "7 > arrel de 50", "Avui és festiu".  

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
> 1. **"Plourà, si hi ha núvols"**: $N \rightarrow L$. (Fals, perquè pot haver-hi núvols i no ploure) .
>     
> 2. **"Plourà, només si hi ha núvols"**: $L \rightarrow N$. (Verdader, és impossible que plogui sense núvols. La pluja _implica_ l'existència de núvols) .
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
    


# Exercicis
### Exemple: $\neg P \rightarrow (Q \leftrightarrow \neg T)$

L'objectiu de l'arbre és descomposar la fórmula fins a arribar als seus **àtoms** (les parts indivisibles).

#### 1. Representació Visual 

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
> 
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


# Tema 2 - Demostrador (proposicions)

## 1. Introducció als Demostradors i les seves Aplicacions

- Els demostradors són programes dissenyats per determinar si una fórmula és conseqüència lògica d'un conjunt de premisses determinat.

- En l'àmbit de l'enginyeria informàtica, s'utilitzen per a la **verificació de sistemes**, permetent demostrar que tant el programari com el maquinari (com els circuits d'una CPU) estan lliures d'errors de disseny.
   
### Mètode de la resolució 

- La necessitat d'aquests mètodes sorgeix perquè el nombre d'interpretacions creix de manera exponencial, fent inviable comprovar tautologies mitjançant mètodes semàntics manuals en sistemes complexos.
	- Per tant, el demostrador actua com un mecanisme de validació de raonaments automatitzable en un ordinador.

>[!tip] Recorda
> demostrador ens permet saber si $\{\varphi_{1},...,\varphi_{n}\}\models\varphi$ és cert.

- Aquesta capacitat és el que ens permet passar d'una col·lecció de fets a una conclusió validada formalment.

- L'objectiu final és trobar un mètode algorítmic que un computador pugui executar sense ambigüitat.


---

## 2. La Forma Normal Conjuntiva (FNC)

- Per utilitzar el mètode de resolució, és imprescindible que les fórmules estiguin en **Forma Normal Conjuntiva (FNC)**.
	
	- Un **literal** es defineix com un àtom (variable proposicional) o la seva negació.
	
	- Una **clàusula** és una disjunció de literals (per exemple, $P \vee \neg Q$).
    
- Una fórmula es troba en FNC si és una conjunció de clàusules de la forma $\phi_{1}\wedge...\wedge\phi_{n}$. (sense implicacions)

### Tipus de Clausules

- La **clàusula buida** ($\square$) representa una contradicció, ja que no existeix cap interpretació que pugui satisfer una disjunció buida de literals.

- Per transformar qualsevol fórmula a FNC, seguim un algorisme de tres passos basat en equivalències lògiques:
    
    1. Eliminar implicacions ($\rightarrow$) i coimplicacions ($\leftrightarrow$) usant les definicions clàssiques ($\neg\varphi\vee\psi$).
        
    2. Introduir les negacions cap a l'interior dels parèntesis aplicant les **Lleis de De Morgan** i eliminant la doble negació.
        
    3. Aplicar la **propietat distributiva** de la disjunció respecte a la conjunció ($\vee$ sobre $\wedge$).

- Un exemple clar és la fórmula $(P\vee\neg Q)\rightarrow R$, que es transforma en $(\neg P\vee R)\wedge(Q\vee R)$ després d'aplicar aquests passos.
    

---

## 3. Conseqüència Lògica i la Regla de Resolució

- Diem que una fórmula $\varphi$ és **conseqüència lògica** d'un conjunt de premisses si la implicació formada per la conjunció de les premisses cap a la conclusió és una tautologia.
	- S'utilitza la notació $\{\varphi_{1},...,\varphi_{n}\}\models\varphi$ per expressar aquesta relació.


- El **mètode de resolució** és un procediment sintàctic que busca validar aquesta relació de manera eficient.
    
- La **regla de resolució** funciona amb dues clàusules (anomenades pares) que contenen un literal complementari (per exemple, $P$ i $\neg P$).
	
	- El resultat de l'operació és una nova clàusula anomenada **resolvent**, que consisteix en la disjunció de tots els literals de les clàusules pare excepte els literals complementaris que s'han suprimit.

>[!quote] Per Exemple
 Si tenim $\neg P\vee Q\vee S$ i $\neg Q\vee T$, el resolvent és $\neg P\vee S\vee T$ (suprimint $Q$ i $\neg Q$).
>   
>- Si tenim dos literals directament oposats com $P$ i $\neg P$, el seu resolvent és la clàusula buida ($\square$).
>    
>- Utilitzem el símbol $\vdash_{R}$ per indicar que una clàusula es pot derivar d'un conjunt d'entrada mitjançant la regla de resolució.
  
- Aquest mètode evita l'explosió exponencial de les interpretacions centrant-se només en les combinacions de literals que poden generar contradiccions.

- És la base de la demostració automàtica de teoremes moderna.


---

## 4. El Teorema de Resolució i l'Algorisme Pràctic


- El **Teorema de Resolució** estableix el lligam definitiu: $\{\varphi_{1},...,\varphi_{n}\}\models\varphi$ si i només si de la FNC de $(\varphi_{1}\wedge...\wedge\varphi_{n}\wedge\neg\varphi)$ es pot deduir la clàusula buida ($\square$).

- Això es basa en el mètode de **reducció a l'absurd**: si la negació de la conclusió juntament amb les premisses ens porta a una contradicció, aleshores el raonament original és vàlid.

- L'algorisme de resolució segueix aquests passos:
    
    1. Negar la conclusió ($\neg\varphi$).
        
    2. Calcular la FNC de les premisses i la conclusió negada.
        
    3. Aplicar la regla de resolució de manera iterativa fins a obtenir $\square$ ("èxit") o fins que no es puguin generar més resolvents ("fallo").
        

- Un cas d'aplicació real és el raonament sobre bancs i interessos: transformem el llenguatge natural a àtoms ($P, Q, R$), formalitzem les premisses, neguem la conclusió i resolem.

- Si s'arriba a la clàusula buida, podem afirmar amb total seguretat que el raonament és correcte.


# Tema 3 - SAT Solvers (proposicions)

## Introducció i Conceptes Fonamentals dels SAT-solvers

Un dels pilars d'aquesta part del temari és la definició i aplicabilitat dels solucionadors de satisfactibilitat. 

- SAT-solvers
	- programes fonamentats en la lògica de proposicions per resoldre problemes pràctics.
    
- El nucli de la qüestió teòrica és el Problema SAT, el qual consisteix a decidir si una fórmula proposicional estructurada en Forma Normal Conjuntiva (FNC) és satisfactible.

- La importància cabdal del problema SAT rau en la capacitat de representar múltiples problemes pràctics mitjançant fórmules d'un llenguatge de proposicions.

- La lògica subjacent ens dicta que, si la fórmula associada aconsegueix ser satisfactible, això significa irremeiablement que el problema modelat té solució.

>[!remember] Recorda
>- Un SAT-solver és, per definició, l'eina de programari que resol aquest problema SAT.
   
- Aquests programes informàtics han estat àmpliament estudiats per la comunitat acadèmica i tenen la capacitat computacional de processar fórmules lògiques de grans dimensions.

>[!quote] Exemples i utilitats
>- A efectes pràctics, els SAT-solvers poden resoldre l'assignació de portàtils a docents d'una escola garantint que aquells amb hores coincidents no els comparteixin.
  >  

   >[!info] Utilitat
   > Resoldre instalacions i conflictes de dependències, traçar rutes de transport, elaboració d'horaris amb condicions complexes
   
   
> **Consell de professor:** Memoritzant un parell d'aquests exemples pràctics podreu justificar l'ús d'aquests sistemes teòrics en preguntes de desenvolupament o de reflexió dins de l'avaluació.

---

### Casos pràctics
#### Cas Pràctic: El Problema de la Coloració de Mapes

El problema de la coloració de grafs planars (mapes) és un exercici d'avaluació recurrent. 

### Resolució
La regla fonamental del problema dicta que cap parell de països veïns pot tenir assignat el mateix color.

- A nivell de notació matemàtica, establim P com el conjunt de països del continent i representem els quatre colors a utilitzar mitjançant els dígits numèrics 1, 2, 3 i 4.

L'objectiu informàtic és expressar aquest repte mitjançant una fórmula proposicional en Forma Normal Conjuntiva (FNC) per tal que la màquina (el SAT-solver) ho entengui i ho resolgui.

##### 1r formalització del llenguatge
- Per estructurar l'alfabet de variables, es pren per a $i\in P$ i $j\in\{1,2,3,4\}$ la proposició $Rij$, que adquireix el significat semàntic de "al país i se li assigna el color j".

##### Condicions
- El procediment de formalització s'ha de dividir lògicament en diverses asseveracions imprescindibles.
	
	- Primera condició: S'ha de garantir que, sense excepció, a cada país se li assigni efectivament un color.
	    
	- Per complir aquesta primera premissa, introduïm per a cada $i\in P$ una clàusula de disjunció: $Ri1\vee Ri2\vee Ri3\vee Ri4$.
	    
	- Segona condició: S'ha de prohibir estrictament que a un mateix país se li assigni més d'un color de manera simultània.
	    
	- Per aconseguir aquesta exclusivitat, per a tot $i\in P$ i qualsevol parell de colors $j,j'\le4$ on $j\ne j'$, s'imposa la clàusula: $\neg Rij\vee\neg Rij'$.
	    
	- Tercera condició: S'ha de traduir a nivell lògic el fet que els països que són fronterers no poden tenir colors compartits.

- Així, per a qualsevol parell de països $i,i'\in P$ que constin com a veïns, i per a tots els colors possibles $j\le4$, es dictamina la clàusula de prevenció: $\neg Rij\vee\neg Ri'j$.

- El model complet a introduir al solucionador s'obté realitzant la conjunció global de totes les clàusules generades a les passes (1), (2) i (3).


# Tema 4 - Putmann

## Fonaments i Regles de Davis-Putnam


> [!info] Definicions Prèvies
>  Per introduir les regles de Davis i Putnam, necessitem algunes definicions prèvies essencials.
> 
> - Si $\psi$ és un literal, escrivim $\sim\psi=\neg\psi$ en cas que $\psi$ sigui estrictament un àtom. 
> - Inversament, escrivim $\sim\psi=\chi$ si tenim que $\psi=\neg\chi$, on $\chi$ és l'àtom base.
> - Denotem per $\mathbb{I}$ a la conjunció buida. Per la seva naturalesa, és una tautologia, atès que tota interpretació possible I la satisfà.
> 

El mètode s'estructura al voltant de tres regles de simplificació deductiva:
### Fonaments 
#### 1. Regla de la Tautologia
La primera és la **regla de la tautologia**, que denotem formalment per (TAU). 

- L'entrada d'aquesta regla és una fórmula en FNC, i la seva sortida és la fórmula resultant d'eliminar completament aquelles clàusules que continguin un parell complementari de literals. 

>[!info] Assegura que:
>S'assegura que la fórmula original és satisfactible si i només si la nova fórmula ho és.


> [!quote] Exemple (TAU) 
> Si $$\varphi=(P\vee Q\vee\neg S)\wedge(P\vee\neg P\vee R)\wedge\neg Q$$ en aplicar la regla (TAU) a la clàusula central, obtenim la fórmula simplificada $$\varphi^{*}=(P\vee Q\vee\neg S)\wedge\neg Q$$


#### 2. Regla de la Clàusula elemental
La segona és la **regla de la clàusula elemental**, que denotarem per $(CE)_{\psi}$ on $\psi$ és un literal aïllat. 

Aquesta regla construeix primer una fórmula eliminant les clàusules on apareix directament $\psi$.
	Posteriorment, s'elimina el literal oposat $\sim\psi$ de l'interior de les clàusules restants. També manté intacta la condició de satisfactibilitat.
    

> [!quote] Exemple (CE) 
> Si tenim $$\varphi=P\wedge(P\vee\neg Q)\wedge(\neg P\vee\neg Q\vee R)$$ i hi apliquem la regla $(CE)_{P}$, aconseguim una dràstica reducció fins a obtenir $$\varphi^{*}=\neg Q\vee R$$



#### 3. La **regla del literal pur**
 $(PU)_{\psi}$. Aquesta regla s'activa quan una fórmula en FNC conté un literal $\psi$ en alguna de les seves clàusules, però el seu complementari $\sim\psi$ no és membre de cap clàusula en absolut. 
 - La sortida resulta de la simple eliminació de les clàusules on aquest $\psi$ apareix.


> [!quote] Exemple (PU)
>  Donada $$\varphi=(\neg P\vee Q)\wedge(\neg P\vee R\vee S)\wedge(\neg Q\vee T)\wedge S$$ en aplicar $(PU)_{\neg P}$ a les dues primeres clàusules, obtenim àgilment $$\varphi^{*}=(\neg Q\vee T)\wedge S$$

---

#### L'Algorisme DPLL i Resolució de Problemes

Quan les regles de simplificació no són suficients per buidar el problema, necessitem un mecanisme de cerca estructurat.

> [!info] El Lema de Davis-Putnam 
> L'arquitectura del mètode de Davis-Putnam (algorisme DPLL), es basa en les tres regles anteriors i en el Lema de Davis-Putnam.
>
> - El lema decreta que si $\varphi$ és una fórmula en FNC i $\psi$ un literal, la fórmula $\varphi$ és satisfactible si i només si $\varphi\wedge\psi$ és satisfactible o bé $\varphi\wedge\sim\psi$ resulta ser satisfactible.

- La funció recursiva DPLL pren com a entrada una fórmula proposicional en FNC i retorna el valor booleà "true" si s'assoleix la satisfactibilitat, o bé "false" si s'arriba a una contradicció.

- L'execució comença aplicant les tres regles de Davis-Putnam exhaustivament fins que ja no se'n pugui aplicar cap més. 
	- Si la fórmula obtinguda $\chi$ equival a la conjunció buida ($\mathbb{I}$), es retorna true; si esdevé la clàusula buida ($\Box$), es retorna false.


- Si l'estat és inconclús, el programa ha d'elegir un literal $\psi$ existent i procedir a retornar el càlcul dividit: $(DPLL(\chi\wedge\psi)\vee DPLL(\chi\wedge\sim\psi))$.


### Clausula vs Conjunció buida

> [!info] La Clàusula Buida (Contradicció) 
> - Una clàusula és, per definició, una disjunció lògica (un OR).
> - Per tant, la clàusula buida representa una **disjunció buida**. 
- Lògicament, una interpretació satisfà una disjunció de fórmules $\varphi_{1}\vee...\vee\varphi_{n}$ si i només si hi ha almenys un element que sigui cert. 

- En no haver-hi cap element dins la clàusula (està buida), és lògicament impossible trobar-ne un que sigui cert; per tant, **no hi ha cap interpretació que la pugui satisfer**. 

>[!question] **Conclusió:** 
>La clàusula buida equival sempre a una **contradicció**. Si el nostre algorisme de Davis-Putnam arriba a generar una clàusula buida, significa que les restriccions han xocat i aquell camí no té solució.
> 


> [!info] La Conjunció Buida (Tautologia)
> 
> - Una fórmula en Forma Normal Conjuntiva (FNC) és, globalment, una conjunció (un AND) de clàusules. 
> - Quan apliquem regles de simplificació i eliminem totes les clàusules de la fórmula, ens queda una **conjunció buida**. 
> 

- Lògicament, una interpretació satisfà una conjunció de fórmules $\varphi_{1}\wedge...\wedge\varphi_{n}$ si i només si per a tots els seus elements, la interpretació els fa certs. 

- Com que no hi ha cap element a avaluar (la conjunció està buida), no hi ha cap restricció que es pugui incomplir; en conseqüència, **tota interpretació la satisfà** de forma trivial. 

>[!question] **Conclusió:** 
>La conjunció buida equival a una **tautologia**. Si el nostre algorisme aconsegueix buidar completament la fórmula, significa que ha trobat una assignació vàlida i el problema és satisfactible.


>[!tip] Regla mnemotècnica per a l'examen
>
>- **Clàusula buida** = Disjunció sense opcions = Impossible de complir = **Contradicció** (S'atura i retorna Fals).
 >   
>- **Conjunció buida** = Conjunció sense restriccions = Totes les condicions superades = **Tautologia** (S'atura i retorna Cert).


# Tema 5 - Llenguatge de Predicats

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

# Tema 6 - Formalització de llenguatge

La formalització és el procés de traduir expressions del llenguatge natural a fórmules del llenguatge de predicats. 

## Interpretacions
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

## Variables i Fórmules Tancades

>[!warning] Cuidado
>Dins d'una fórmula, la funció de les variables pot variar segons la seva interacció amb els quantificadors. 

- **Aparició Lliure:** Una variable $x$ és lliure en una fórmula si no està dins de l'abast d'un quantificador ($\forall$ o $\exists$) que l'afecti directament. En cas contrari és lligada

- **Aparició Lligada:** Es diu que una aparició és lligada quan està afectada per un quantificador.
![[Pasted image 20260307193647.png]]

- **Fórmules Tancades (Sentències):** Una fórmula es considera tancada si no conté cap variable lliure. 
	- Per exemple, $$\forall x\forall y(Rxy\rightarrow\exists z(Rxz\wedge Rzy))$$ és tancada perquè totes les instàncies de $x$, $y$, $z$ estan lligades.
	- En canvi, si tenim $\forall x(Rxy\wedge\exists z(Pz\vee Rxz))$, la variable $y$ és lliure, fent que la fórmula no sigui tancada.
    
>[!warning] Important
>Sovint se us demanarà classificar variables; recordeu que una mateixa variable pot aparèixer com a lliure i lligada en diferents subfórmules, però la fórmula només és tancada si totes les seves aparicions estan lligades.


---

## Interpretacions i Avaluació de Termes

La semàntica ens permet donar significat real als símbols abstractes. 

>[!info] Interpretació
>Una interpretació ($I$) és una estructura que defineix el context on operem

Perquè una fórmula lògica tingui sentit, necessitem una **Interpretació ($\mathcal{I}$)** que connecti el llenguatge formal amb un univers real.

### 1. El Domini ($D$)

És el "univers del discurs". És el conjunt de tots els objectes que existeixen per a la nostra lògica.

- **Condició:** Ha de ser un conjunt **no buit**.
    
- **Exemples:** $\mathbb{Z}$ (els enters), el conjunt de tots els estudiants de la FIB, o les peces d'un tauler d'escacs.
    

### 2. El Producte Cartesià ($D^n$)

Representa seqüències de $n$ elements del domini.

- $D^1$: Elements individuals $(a)$.
    
- $D^2$: Parelles d'elements $(a, b)$.
    
- $D^n$: Tuples de $n$ elements.
    

### 3. Assignacions de la Interpretació

La interpretació $\mathcal{I}$ és una funció que "dóna vida" als símbols:

|**Símbol**|**Assignació de la Interpretació**|**Concepte**|
|---|---|---|
|**Variable ($x$)**|$I(x) \in D$|Un element variable de l'univers.|
|**Constant ($c$)**|$I(c) \in D$|Un element fix i específic (com un nom propi).|
|**Funció ($f^n$)**|$I(f): D^n \rightarrow D$|Una operació que agafa $n$ elements i retorna un altre element del domini.|
|**Predicat ($R^n$)**|$I(R) \subseteq D^n$|Una propietat o relació. Defineix quins elements compleixen la condició.|

---

#### Exemple Pràctic

Suposem que el nostre **Domini ($D$)** són els números naturals $\{0, 1, 2, \dots\}$.

1. **Constants:** Si tenim la constant $a$, podem definir $I(a) = 0$.
    
2. **Funcions:** Si tenim el símbol de funció $f$ d'aritat 1, podem definir $I(f)$ com "el següent número".
    
    - $I(f): n \rightarrow n + 1$.
        
3. **Predicats:** Si tenim el símbol de predicat $P$ d'aritat 2, podem definir $I(P)$ com la relació "és menor que".
    
    - $I(P) = \{(x, y) \in D^2 \mid x < y\}$.
        

> [!IMPORTANT] Definició
> 
> Una **Interpretació** és el parell $\mathcal{M} = \langle D, I \rangle$ on $D$ és el domini i $I$ és la funció d'interpretació que mapeja els símbols del llenguatge a objectes, funcions i relacions de $D$.
        
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



# Tema 7 - Demostradors (predicats)

## 1. Fonaments de la Lògica de Predicats

Avui el mètode de resolució es generalitza per a llenguatges de predicats. És crucial distingir tres tipus de fórmules segons la seva interpretació:

* **Tautologia**: Una fórmula que resulta certa en **totes** les interpretacions possibles.


* **Satisfactible**: Aquella que és certa en, almenys, **una** interpretació.


* **Contradicció**: La fórmula que és falsa en **totes** les interpretacions.


>[!tip] *Relació clau**: 
>Una fórmula $\varphi$ és una tautologia si i només si la seva negació $\neg\varphi$ és una contradicció.



## **Conseqüència lògica** ($\models$) 
La consequencia logica és el que ens permet validar raonaments. Diem que $\varphi$ és conseqüència lògica de un conjunt de premisses $\{\varphi_1, ..., \varphi_n\}$ si la implicació conjunta $(\varphi_1 \wedge ... \wedge \varphi_n) \rightarrow \varphi$ és una tautologia. 

---

## 2. Formes Clausals i Algoritme de Transformació

Per aplicar el mètode de resolució, primer hem de transformar les fórmules a una estructura estàndard anomenada **forma clausal**. 

>[!info] Formalitzacio
>Una fórmula està en forma clausal si té l'aspecte $\forall x_1 ... \forall x_n (\psi_1 \wedge ... \wedge \psi_m)$, on cada $\psi_i$ és una **clàusula** (una disjunció de literals). El nucli és la part sense els quantificadors universals.


# Mecanitzacio

L'algoritme per obtenir-la consta de 7 passos crítics per a l'examen:

1. **Eliminar implicacions i co-implicacions**: Substituir $\varphi \rightarrow \psi$ per $\neg\varphi \vee \psi$.


2. **Interioritzar negacions**: Aplicar lleis de De Morgan i les equivalències de negació de quantificadors ($\neg\exists x \varphi \equiv \forall x \neg \varphi$).


3. **Normalitzar variables**: Moure quantificadors si la variable no apareix lliure en l'altra part de la fórmula.


4. **Skolemització**: Eliminar quantificadors existencials ($\exists z$). Si $z$ no està sota un $\forall$, es canvia per una constant nova ($c$). Si està sota l'àmbit de variables $x_1, ..., x_n$ quantificades universalment, es substitueix per una funció $f(x_1, ..., x_n)$.


5. **Renombrar variables**: Evitar conflictes de noms entre variables lligades.


6. **Extracció de quantificadors**: Moure tots els $\forall$ cap a l'exterior.


7. **Distributivitat**: Aplicar regles distributives per obtenir una conjunció de clàusules al nucli.


És vital recordar el **Teorema de la forma clausal**: 
>[!info] **Teorema de la forma clausal**:
>una fórmula $\varphi$ és una contradicció si i només si la seva forma clausal $\varphi'$ també ho és, encara que **no són necessàriament equivalents** de forma general.

---

## 3. Unificació d'Expressions

L'algoritme de unificació utilitza una pila d'igualtats ($P$) i segueix aquestes regles:

* Si traiem una igualtat de variables o constants idèntiques, continuem.


* Si tenim una variable $e$ i un terme $e'$, i $e$ no apareix dins de $e'$, apliquem la substitució a tota la pila i la guardem al resultat.


* Si tenim funcions o predicats iguals $f(s_1, ..., s_n) = f(t_1, ..., t_n)$, descomposem i posem a la pila les igualtats dels seus arguments $s_i = t_i$.


* Si hi ha un conflicte de símbols (ex: $f(a) = g(x)$), l'algoritme retorna **"fallo"**.



Aquest procés és el "motor" que permet emparellar literals durant la resolució, trobant el **unificador** necessari per cancel·lar termes oposats.

---

## 4. El Mètode de Resolució en Predicats

El **resolvent** és la clàusula resultant de combinar-ne dues de preexistents que contenen literals oposats unificables. El procediment és:

1. **Renombrar variables**: Les dues clàusules no poden compartir noms de variables.


2. **Identificar literals**: Buscar un literal $\psi_1$ en $\varphi_1$ i un $\neg\psi_2$ en $\varphi_2$.


3. **Unificar**: Trobar el unificador $\lambda$ tal que $\psi_1\lambda = \psi_2\lambda$.


4. **Combinar**: El resolvent és $(\varphi_1' \vee \varphi_2')\lambda$, on $\varphi_i'$ són les clàusules originals sense els literals oposats.



Per demostrar que un conjunt de clàusules és inconsistent (i per tant, validar un raonament), apliquem la regla de resolució successivament fins a arribar a la **clàusula buida** ($\square$). Si arribem a la clàusula buida, hem demostrat que el conjunt original era una contradicció. L'exemple final de les transparències mostra com, a partir de 4 premisses (input), s'unifiquen termes com $\{x=a, y=b\}$ i $\{z=f(a)\}$ per anar derivant noves clàusules fins a la contradicció final .


# Tema 8

## 1. El Mètode de Resolució en Lògica de Predicats

A diferència de la lògica proposicional, aquí treballem amb variables i quantificadors, cosa que afegeix complexitat al procés de "aparellar" literals.

### Conceptes Clau: Resolvent i Unificació

- **Definició de Resolvent:** Donades dues clàusules $\varphi_{1}$ i $\varphi_{2}$ que no comparteixen variables (si en tenen de comunes, cal fer un **renombrament**), el resolvent es genera si existeix un literal $\psi_{1}$ en $\varphi_{1}$ i un literal $\neg\psi_{2}$ en $\varphi_{2}$ que siguin **unificables**.
    
- **El procés:** S'aplica l'algoritme d'unificació per trobar un unificador $\lambda$. El resolvent resultant és la unió de les clàusules restants aplicada la substitució: $(\varphi_{1}' \vee \varphi_{2}')\lambda$.
    
- **Regla de Resolució:** És la generalització del teorema de resolució proposicional al context de la lògica de predicats, permetent deduir noves clàusules a partir de les existents.
    

### L'Algoritme de Resolució

L'objectiu final és demostrar que una fórmula $\varphi$ és conseqüència de $\varphi_{1},...,\varphi_{n}$.

1. **Forma Clausal:** Es calculen les formes clausals de les premisses i de la **negació de la conclusió** ($\neg\varphi$).
    
2. **Cerca de la Clàusula Buida:** Es calculen resolventes successius. Si s'obté la clàusula buida ($\square$), l'algoritme retorna "èxit" (la fórmula és conseqüència lògica). Si no, pot donar "fallo" o no acabar (problema de la indecidibilitat).
    

---

## 2. Exemples d'Aplicació de Resolució

Aquests exemples són vitals per a l'examen, ja que mostren la traça de l'algoritme.

- **Exemple de Tautologia:** Per demostrar que $\forall x\exists yRxy\rightarrow\exists x\exists yRxy$ és una tautologia, es nega la fórmula, es passa a forma clausal (usant Skolem, com transformar $\exists y$ en $f(x)$) i es busca la contradicció.
    
- **Gestió de Variables:** És fonamental el **renombrament**. En sistemes amb múltiples clàusules (com l'exemple 2 i 3), les variables es consideren locals. S'utilitzen subíndexs ($x_1, x_2, ...$) per evitar col·lisions durant la unificació.
    
- **Derivació pas a pas:** L'èxit del mètode es visualitza quan, mitjançant unificadors (ex: $\{x_1=a, z=f(a)\}$), els literals oposats s'anul·len fins a arribar a la clàusula buida.
    

---

## 3. Introducció al Llenguatge PROLOG

PROLOG (_Programming in Logic_) és un llenguatge **declaratiu** basat en el mètode de resolució. A diferència dels llenguatges imperatius (com C++ o Java), en Prolog no expliquem "com" fer les coses, sinó "què" és cert.

- **Aplicacions:** Molt utilitzat en Intel·ligència Artificial i sistemes experts.
    
- **Sintaxi Bàsica:**
    
    - **Identificadors:** Seqüències de caràcters que no comencen per dígit.
        
    - **Variables:** Han de començar per **Majúscula** o per guió baix (`_`).
        
    - **Constants:** Poden ser enters, decimals, o identificadors que comencen per minúscula (àtoms).
        
- **Mecanisme d'Execució:** L'interpretador de Prolog és, en realitat, un demostrador de teoremes que utilitza l'algoritme de resolució per validar si un **objectiu** és conseqüència del **programa** (base de coneixement).
    

---

## 4. Fórmules, Programes i Objectius en Prolog

Un programa Prolog és un conjunt de clàusules de Horn (un tipus específic de clàusula amb, com a màxim, un literal positiu).

### Estructura d'una clàusula

- **Notació:** Una fórmula $(\varphi_{1}\wedge...\wedge\varphi_{n})\rightarrow\varphi$ s'escriu en Prolog com `H :- B1, B2, ..., Bn.` on:
    
    - `H` és el **cap** (conclusió).
        
    - `:-` representa la implicació (llegit com "si").
        
    - `,` representa la conjunció (I).
        
- **Punt final:** Tota clàusula i objectiu ha d'acabar obligatòriament amb un punt (`.`).
    

### Semàntica dels Quantificadors

- **Al Programa:** Les variables estan **cuantificades universalment** ($\forall$).
    
- **A l'Objectiu:** Les variables estan **cuantificades existencialment** ($\exists$). Prolog buscarà valors (instanciacions) que facin que l'objectiu sigui cert.
    

---

## 5. Exemples de Programació (Casos d'Estudi)

### Exemple 1: Sistema de Notes

Es defineix una base de dades amb fets (`nota(maria, 9).`) i una regla per definir qui aprova:

`aprovado(X) :- nota(X,Y), Y >= 5.` Si preguntem `aprovado(X).`, el sistema cercarà totes les `X` que compleixin la condició.

### Exemple 2: Arbre Genealògic i Recursivitat

És l'exemple clàssic per entendre com es defineixen relacions complexes:

- **Fets:** `padre(juan, pedro).`, `madre(maria, pedro).`
    
- **Regles base:** Un pare o una mare són antepassats.
    
- **Regles recursives:** La clau per definir "antepassat" en qualsevol grau:
    
    `antepasado(X,Y) :- antepasado(X,Z), padre(Z,Y).` Això permet que el sistema infereixi relacions que no estan explícitament escrites a la base de dades.
    


# Tema 9 - Llenguatge Regular

## 1. Introducció i Aplicacions dels Autòmates

Els autòmates són models computacionals utilitzats de forma extensiva en el disseny de programari de sistemes. 
	La seva funció principal és la de **reconeixedors de llenguatges**: reben una cadena de símbols i determinen si aquesta pertany o no a un llenguatge específic $L$.


---

## 2. Conceptes Fonamentals de Llenguatges Formals

Abans de construir l'arquitectura d'un autòmata, hem de dominar l'alfabet amb el qual treballarem.

### Alfabets i Paraules

- **Alfabet ($\Sigma$):** Un conjunt finit i no buit de símbols.
    
- **Paraula:** Una seqüència finita de símbols extrets d'un alfabet.
    
- **Paraula buida ($\lambda$):** Aquella que no conté cap símbol.
    
- **Longitud ($|x|$):** El nombre total de símbols d'una paraula, incloent repeticions.
    
- **Comptatge de símbols ($n_{a}(x)$):** Indica quantes vegades apareix un símbol concret en una paraula.
    
- **$\Sigma^{*}$:** El conjunt universal que conté totes les paraules possibles que es poden formar sobre l'alfabet $\Sigma$.
    

### El Concepte de Llenguatge

Un llenguatge no és més que un conjunt de paraules sobre un alfabet determinat. Alguns exemples pràctics inclouen el conjunt d'identificadors vàlids en **Java** o el conjunt de programes correctes d'un llenguatge de programació específic.

### Operacions amb Paraules i Llenguatges

- **Concatenació ($x \cdot y$):** Unió de dues paraules posant els símbols de la primera seguits dels de la segona. La identitat és $\lambda$, ja que $x \cdot \lambda = x$.
    
- **Potència ($x^n$):** Concatenació repetida d'una paraula amb ella mateixa.
    
- **Inversa ($x^I$):** La paraula escrita en ordre invers ($a_n...a_1$).
    
- **Operacions de Conjunts:** Els llenguatges accepten unió, intersecció, complementació i diferència.
    
- **Clausura de Kleene ($L^{*}$):** El llenguatge format per totes les concatenacions possibles (zero o més vegades) de paraules de $L$.
    

---

## 3. L'Autòmata Finit Determinista (AFD)

L'autòmata finit és el model més simple de computació. Està compost per una **cinta d'entrada** dividida en cel·les on es llegeix la informació mitjançant un puntero que es mou cap a la dreta, i una **unitat de control** que canvia d'estat a cada pas.

### Definició Formal

Un AFD es defineix com una estructura de 5 tuples $M=(K,\Sigma,\delta,q_{0},F)$:

1. **$K$:** Conjunt finit i no buit d'**estats**.
    
2. **$\Sigma$:** **Alfabet** d'entrada.
    
3. **$\delta$:** **Funció de transició** ($K \times \Sigma \rightarrow K$), que determina el següent estat segons l'actual i el símbol llegit.
    
4. **$q_{0}$:** **Estat inicial**.
    
5. **$F$:** Conjunt d'**estats aceptadors** o finals ($F \subseteq K$).
    

---

## 4. Representació i Còmput

Podem visualitzar els autòmates mitjançant **grafs**, on els nodes són estats i els arcs etiquetats representen la funció $\delta$.

- **Configuració:** Es representa com $px$, on $p$ és l'estat actual i $x$ és la part de la cadena que falta per llegir.
    
- **Producció ($\vdash_{M}$):** El pas d'una configuració a una altra mitjançant una transició.
    
- **Llenguatge reconegut $L(M)$:** És el conjunt de totes les paraules que, partint de l'estat inicial, porten a l'autòmata a un estat final o aceptador un cop s'ha llegit tota la cadena.
    

> **Exemple de l'examen:** Un autómata que accepta paraules amb un nombre **parell** d'uns o un que rebutja cadenes amb **tres b's consecutives**. Estudieu bé aquests diagrames de transició.

---

## 5. Implementació de Programari

Els AFD són especificacions directes per a programes. En Java o C, seguim aquest esquema d'enginyeria:

1. Assignar un número a cada estat (0 per a l'inicial).
    
2. Utilitzar un caràcter especial (com `$`) per marcar el final de l'entrada.
    
3. Implementar un bucle **`while`** que recorri la cadena.
    
4. Dins del bucle, utilitzar una estructura **`switch-case`** per gestionar els canvis d'estat segons la funció $\delta$.
    
5. En acabar, retornar un booleà comprovant si l'estat final és un dels estats aceptadors.
    

# Tema 10 - Teoria autòmata finit

## 1. Simplificació d'Autòmates Deterministes

L'objectiu de la simplificació és reduir el nombre d'estats d'un AFD eliminant redundàncies. Un autòmata amb menys estats és més fàcil d'implementar i consumeix menys memòria.

### Estats Equivalents (Indistingibles)

- **Concepte:** Dos estats $p$ i $q$ fan la mateixa funció si, per a qualsevol entrada $x$, ambdós porten a un estat aceptador o ambdós porten a un estat no aceptador.
    
- **Definició Formal:** Siguin $p, q \in K$. Són equivalents si per a tot $x \in \Sigma^{*}$, les configuracions $px \vdash_{M}^{*} p'$ i $qx \vdash_{M}^{*} q'$ compleixen que tant $p', q' \in F$ com $p', q' \notin F$.
    
- **Procés de Fusió:** Si identifiquem estats equivalents (com els estats $D$ i $E$ a l'exemple de la diapositiva 4), els podem "ajuntar" en un de sol. Aquest procés s'itera fins que ja no es poden simplificar més estats.
    

---

## 2. Autòmates Indeterministes (AFN)

Els autòmates indeterministes són models computacionals que, tot i ser equivalents en potència als deterministes, són molt més senzills de dissenyar per a problemes complexos.

### Diferències Principals amb l'AFD

- **Transicions Múltiples:** Des d'un mateix estat i amb el mateix símbol, es poden realitzar zero, una o més transicions.
    
- **Transicions amb la Paraula Buida ($\lambda$):** Es permet passar d'un estat a un altre sense llegir cap símbol de l'entrada.
    
- **Còmputs Múltiples:** Per a una mateixa entrada, poden existir diversos camins o còmputs possibles.
    
- **Criteri d'Acceptació:** Una paraula és reconeguda si **almenys un** dels còmputs possibles acaba en un estat aceptador.
    

### Definició Formal

L'AFN es defineix com $M=(K,\Sigma,\Delta,q_{0},F)$, on la principal variació és $\Delta$, un subconjunto de $K \times (\Sigma \cup \{\lambda\}) \times K$.

---

## 3. Exemples i Reconeixement en AFN

El no-determinisme permet modelar condicions "o" de manera molt intuïtiva.

- **Exemple de Subcadenes:** Un AFN que detecta si en una cadena apareix "bab" o "baab". El sistema pot estar en $q_0$ llegint brossa i, quan detecta l'inici del patró, "decidir" avançar cap a l'acceptació.
    
- **Exemple amb Transicions $\lambda$:** Un AFN que accepta la unió de dos llenguatges, com $\{(10)^n : n \ge 0\} \cup \{(010)^n : n \ge 0\}$. L'estat inicial $q_0$ té dues transicions $\lambda$ que actuen com una bifurcació immediata cap a dos sub-autòmates diferents.
    
- **Exemple de Posició Fixa:** Dissenyar un autòmata on el símbol 'a' sigui l'antepenúltim és trivial amb un AFN mentre que en un AFD requeriria molts més estats per "recordar" la posició.
    

---

## 4. Teorema d'Equivalència

**La potència de reconeixement és la mateixa.**

- **Teorema:** Per a tot llenguatge $L$, existeix un AFD que el reconeix si i només si existeix un AFN que el reconeix.
    
- **Estratègia de Disseny:** Quan sigui difícil construir un AFD per a un programa, primer es dissenya l'AFN i després s'aplica l'algoritme de transformació per obtenir l'AFD equivalent, que serà el que finalment programarem.
    

