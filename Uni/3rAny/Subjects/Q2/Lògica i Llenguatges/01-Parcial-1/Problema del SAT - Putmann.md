
>[!info] Recordem
> El problema SAT consisteix a decidir si una fórmula proposicional en Forma Normal Conjuntiva (FNC) és satisfactible.
 >
>- Un SAT-solver és el programa informàtic dissenyat específicament per resoldre aquest problema SAT.

---

# Els Límits de la Força Bruta

Per entendre per què necessitem algorismes complexos, primer hem d'avaluar les limitacions dels enfocaments més simples i ingenus (força bruta).

>[!note] Exercici
>- És un exercici relativament fàcil escriure un programa bàsic en Java per determinar la satisfactibilitat d'una fórmula del llenguatge de proposicions.

![[Pasted image 20260228092945.png]]

- Per a fórmules petites compostes només per tres variables, podem introduir la fórmula lògica $(P_{1}\vee P_{2})\wedge(\neg P_{1}\vee P_{3})$ directament com a entrada al codi.
>[!tip] Recorda
>És la formula d'expansió de Shannon utilitzada en els exercicis
>
   
- Tanmateix, aquest programa educatiu només té utilitat pràctica per a fórmules que tinguin molt poques clàusules.
	El nombre total d'interpretacions creix de manera exponencial respecte a la quantitat de símbols de proposició involucrats.

- Per tant, si desitgem escriure programes SAT-solvers capaços de resoldre problemes reals amb milers de clàusules, estem obligats a utilitzar estratègies matemàtiques intel·ligents.

>[!info]  La Solució
>El mètode de **Davis-Putnam**, el qual constitueix la pedra angular del disseny dels SAT-solvers actuals.

---
# Fonaments i Regles de Davis-Putnam


> [!info] Definicions Prèvies
>  Per introduir les regles de Davis i Putnam, necessitem algunes definicions prèvies essencials.
> 
> - Si $\psi$ és un literal, escrivim $\sim\psi=\neg\psi$ en cas que $\psi$ sigui estrictament un àtom. 
> - Inversament, escrivim $\sim\psi=\chi$ si tenim que $\psi=\neg\chi$, on $\chi$ és l'àtom base.
> - Denotem per $\Box$ a la clàusula buida. Com que és una disjunció buida, representa una contradicció, ja que no hi ha cap interpretació I que la pugui satisfer.
> - Denotem per $\mathbb{I}$ a la conjunció buida. Per la seva naturalesa, és una tautologia, atès que tota interpretació possible I la satisfà.
> 

El mètode s'estructura al voltant de tres regles de simplificació deductiva:
## Fonaments 
### 1. Regla de la Tautologia
La primera és la **regla de la tautologia**, que denotem formalment per (TAU). 

- L'entrada d'aquesta regla és una fórmula en FNC, i la seva sortida és la fórmula resultant d'eliminar completament aquelles clàusules que continguin un parell complementari de literals. 

>[!info] Assegura que:
>S'assegura que la fórmula original és satisfactible si i només si la nova fórmula ho és.


> [!quote] Exemple (TAU) 
> Si $$\varphi=(P\vee Q\vee\neg S)\wedge(P\vee\neg P\vee R)\wedge\neg Q$$ en aplicar la regla (TAU) a la clàusula central, obtenim la fórmula simplificada $$\varphi^{*}=(P\vee Q\vee\neg S)\wedge\neg Q$$


### 2. Regla de la Clàusula elemental
La segona és la **regla de la clàusula elemental**, que denotarem per $(CE)_{\psi}$ on $\psi$ és un literal aïllat. 

Aquesta regla construeix primer una fórmula eliminant les clàusules on apareix directament $\psi$.
	Posteriorment, s'elimina el literal oposat $\sim\psi$ de l'interior de les clàusules restants. També manté intacta la condició de satisfactibilitat.
    

> [!quote] Exemple (CE) 
> Si tenim $$\varphi=P\wedge(P\vee\neg Q)\wedge(\neg P\vee\neg Q\vee R)$$ i hi apliquem la regla $(CE)_{P}$, aconseguim una dràstica reducció fins a obtenir $$\varphi^{*}=\neg Q\vee R$$



### 3. La **regla del literal pur**
 $(PU)_{\psi}$. Aquesta regla s'activa quan una fórmula en FNC conté un literal $\psi$ en alguna de les seves clàusules, però el seu complementari $\sim\psi$ no és membre de cap clàusula en absolut. 
 - La sortida resulta de la simple eliminació de les clàusules on aquest $\psi$ apareix.


> [!quote] Exemple (PU)
>  Donada $$\varphi=(\neg P\vee Q)\wedge(\neg P\vee R\vee S)\wedge(\neg Q\vee T)\wedge S$$ en aplicar $(PU)_{\neg P}$ a les dues primeres clàusules, obtenim àgilment $$\varphi^{*}=(\neg Q\vee T)\wedge S$$

---

### L'Algorisme DPLL i Resolució de Problemes

Quan les regles de simplificació no són suficients per buidar el problema, necessitem un mecanisme de cerca estructurat.

> [!info] El Lema de Davis-Putnam 
> L'arquitectura del mètode de Davis-Putnam (algorisme DPLL), es basa en les tres regles anteriors i en el Lema de Davis-Putnam.
>
> - El lema decreta que si $\varphi$ és una fórmula en FNC i $\psi$ un literal, la fórmula $\varphi$ és satisfactible si i només si $\varphi\wedge\psi$ és satisfactible o bé $\varphi\wedge\sim\psi$ resulta ser satisfactible.

- La funció recursiva DPLL pren com a entrada una fórmula proposicional en FNC i retorna el valor booleà "true" si s'assoleix la satisfactibilitat, o bé "false" si s'arriba a una contradicció.

- L'execució comença aplicant les tres regles de Davis-Putnam exhaustivament fins que ja no se'n pugui aplicar cap més. 
	- Si la fórmula obtinguda $\chi$ equival a la conjunció buida ($\mathbb{I}$), es retorna true; si esdevé la clàusula buida ($\Box$), es retorna false.


- Si l'estat és inconclús, el programa ha d'elegir un literal $\psi$ existent i procedir a retornar el càlcul dividit: $(DPLL(\chi\wedge\psi)\vee DPLL(\chi\wedge\sim\psi))$.


## Clausula vs Conjunció buida

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
# Casos Pràctics

## Cas Pràctic 1: Resolució per Literals Purs

- Ens plantegen determinar la satisfactibilitat de: $$\varphi=(P\vee Q)\wedge(P\vee\neg Q)\wedge(R\vee Q)\wedge(R\vee\neg Q)$$ 
- En primer lloc, apliquem $(PU)_{P}$ a la fórmula, aconseguint l'expressió: $$\varphi_{1}=(R\vee Q)\wedge(R\vee\neg Q)$$
- Si apliquem ara novament la regla del literal pur, aquesta vegada $(PU)_{R}$ a la nova fórmula $\varphi_{1}$, es redueix completament i podem concloure fermament que la fórmula és satisfactible.

## Cas Pràctic 2: Cascada de Clàusules Elementals

- Analitzem la fórmula més complexa:
$$\varphi=(\neg P\vee\neg Q\vee\neg R)\wedge(Q\vee\neg Q\vee R)\wedge(P\vee\neg Q\vee R)\wedge(\neg P\vee Q)\wedge P\wedge R$$

- Fent una neteja inicial amb la regla de la tautologia (TAU), obtenim la base:
$$\varphi_{1}=(\neg P\vee\neg Q\vee\neg R)\wedge(P\vee\neg Q\vee R)\wedge(\neg P\vee Q)\wedge P\wedge R$$

- Iniciem la resolució aplicant $(CE)_{P}$ a $\varphi_{1}$, la qual cosa ens dóna:
$$\varphi_{2}=(\neg Q\vee\neg R)\wedge Q\wedge R$$

- Continuant l'efecte cadena amb $(CE)_{Q}$ sobre $\varphi_{2}$, arribem a:
$$\varphi_{3}=\neg R\wedge R$$

- Finalment, aplicant l'última unitat amb $(CE)_{R}$ a $\varphi_{3}$, derivem inevitablement en la clàusula buida, dictaminant que el sistema és una contradicció absoluta.

## Cas Pràctic 3: Ramificació per Estancament

- Observem una situació de bloqueig a:
$$\varphi=(P\vee\neg Q)\wedge(\neg P\vee Q)\wedge(R\vee Q)\wedge(\neg R\vee\neg Q)$$

on és evident que cap de les tres regles es pot emprar directament de primeres.    
- En resposta, ens forcem a elegir el literal $P$ i ramificar aplicant les regles sobre la conjunció:  $$\varphi^{\prime}=\varphi\wedge P$$

- Gràcies a aquesta decisió, podem aplicar $(CE)_{P}$ per obtenir una nova base:  $$Q\wedge(R\vee Q)\wedge(\neg R\vee\neg Q)$$
- Seguidament, operant amb $(CE)_{Q}$, l'expressió queda reduïda a $\neg R$ (atès que $R\vee Q$ ja es satisfà per $Q$)
	- Acabant amb $(CE)_{\neg R}$, podem resoldre i afirmar que la fórmula original és **satisfactible**.