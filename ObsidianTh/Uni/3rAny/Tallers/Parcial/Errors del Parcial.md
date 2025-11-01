
# Preguntes
[[#1]]
---

- **Pregunta 1 (Optimització):** Quina és la diferència clau en el càlcul del gradient entre el Descens de Gradient (Batch) i el Descens de Gradient Estocàstic (SGD)?
    
- **Pregunta 2 (Recomanadors):** Quan és preferible utilitzar la Distància Euclidiana en lloc de la Correlació de Pearson per calcular la similitud, i quin concepte clau distingeix els dos escenaris?
    
- **Pregunta 3 (Ítems freqüents):** Per què la mètrica de "Confiança" no és suficient per avaluar una regla d'associació i quin concepte s'introdueix per resoldre el problema de les regles òbvies?
    
- **Pregunta 4 (Recomanadors):** Anomena dues limitacions clau de la Factorització de Matrius (MF) tradicional que les Màquines de Factorització (FM) estan dissenyades per superar.
    
- **Pregunta 5 (Fonaments):** Explica breument la diferència conceptual entre Dades, Informació i Coneixement.
    
- **Pregunta 6 (Recomanadors):** Escriu la fórmula de la funció Softmax (softmax(z)i​) i explica quina transformació aplica a un vector de valoracions z.
    
- **Pregunta 7 (Optimització):** Quin és l'objectiu de la funció de pèrdua Bayesian Personalized Ranking (BPR) i quin tipus de triplet de dades (u,i,j) utilitza per a l'entrenament?
    
- **Pregunta 8 (Recomanadors):** Per què s'afirma que les recomanacions col·laboratives basades en ítems són generalment més estables en el temps que les basades en usuaris?
    
- **Pregunta 9 (Models):** Explica la diferència fonamental entre un "algorisme de predicció" i un "model", segons els apunts.
    
- **Pregunta 10 (Recomanadors):** Quina és la diferència principal entre la "Recol·lecció Explícita" i la "Recol·lecció Implícita" de dades?
    
- **Pregunta 11 (Fonaments):** Segons l'anàlisi de les matemàtiques en IA, quins són els tres pilars fonamentals i quin rol juga cadascun (el llenguatge, el motor i el marc)?
    
- **Pregunta 12 (Recomanadors):** En les Màquines de Factorització, per què el terme d'interacció Wij​ es factoritza com el producte escalar viT​vj​? Quin avantatge computacional s'aconsegueix?



# Correccions
## 1
[[#1]]
#### 1. Pregunta 7 (BPR)

> (No contestada)

**Correcció: MOLT MALAMENT.** La resposta és inexistent. S'esperava una explicació de la funció de pèrdua del _Bayesian Personalized Ranking_ (BPR).

- **Què és?** És una funció de pèrdua dissenyada per a tasques de rànquing, especialment útil amb feedback implícit.
    
- **Triplet de dades:** Utilitza triplets (u,i,j), on u és l'usuari, i és un ítem vist (preferit) i j és un ítem no vist.
    
- **Funció:** L'objectiu és minimitzar ∑−lnσ(y^​ui​−y^​uj​). Això s'aconsegueix quan la puntuació predita per a l'ítem vist (y^​ui​) és més gran que la de l'ítem no vist (y^​uj​).
    

---

#### 3. Pregunta 6 (Softmax)

> softmax el que fa és calcular diferents paràmetres per ajudatr millor una funció

**Correcció: MOLT MALAMENT.** La resposta és conceptualment errònia.

- Softmax **no calcula paràmetres**. És una funció d'activació.
    
- La seva única funció és **transformar un vector de valoracions** (scores o _logits_) en un **vector de probabilitats**, on la suma de tots els elements és 1.
    
- La fórmula és: softmax(z)i​=∑j=0K−1​ezj​ezi​​.
    

---

#### 4. Pregunta 1 (SGD vs. Batch)

> Que per trobar el mínim el batch fa ús d'una pool reduida de dades, mentres que SGD fa ús de totes les dades, però les agafa de manera aleatoria

**Correcció: MOLT MALAMENT.** La resposta **inverteix completament** les definicions.

- **Batch Gradient Descent** (Descens del Gradient tradicional) calcula el gradient utilitzant **TOTES** les dades de l'entrenament per a cada actualització.
    
- **Stochastic Gradient Descent (SGD)** (Descens de Gradient Estocàstic) calcula el gradient utilitzant només **UNA ÚNICA DADA** seleccionada aleatòriament (o un petit _mini-batch_).
    

---

#### 5. Pregunta 4 (MF vs. FM)

> Les dues limitacions clau de les FM és que factoritzen molt bé una matriu gran, però a,mb poca informació Les MF ppermeten posar un concepte "Features" per fer molt més exactes les recomanacions, tot i que llavors tarden molt Al final, unint els dos conceptes obtenim una matriu molt bona per recomanar, i menys computacionalment pesada pq factoritzem la matriu

**Correcció: MOLT MALAMENT.** La resposta demostra una confusió total entre Factorització de Matrius (MF) i Màquines de Factorització (FM).

- La resposta **confon les limitacions de MF amb FM**. Les limitacions són de **MF**, no de FM.
    
- Les limitacions clau de **MF** són:
    
    1. No funciona bé amb **feedback implícit** (clics, compres).
        
    2. Optimitza per a l'error de predicció (regressió), quan l'objectiu real hauria de ser el **rànquing** (ordenació).
        
- Les **FM** són les que generalitzen el model i permeten incorporar característiques addicionals (context, atributs, etc.), anomenades _features_.
    
- La resta de l'explicació és incoherent.
    

---

#### 6. Pregunta 12 (FM Factorització)

> Aconsegueixes reduir la mida de processament en moltisism exponent

**Correcció: MALAMENT.** La resposta és extremadament vaga i tècnicament imprecisa.

- El que es redueix no és la "mida de processament", sinó el **nombre de paràmetres** a estimar.
    
- El problema és que la part quadràtica de la FM (∑∑Wij​xi​xj​) té una complexitat de O(d2) paràmetres.
    
- En factoritzar Wij​≈viT​vj​, el nombre de paràmetres es redueix dràsticament a O(d⋅k), on k (la dimensió dels factors latents) és molt més petit que d.
    

---

#### 7. Pregunta 3 (Confiança vs. Interès)

> La confiança no és suficient perquè caba no filtrant bé, i fent moltes relacions que no tenen valor (si tothom que compra compra llet, no podem treure conclusions entre un ítem i llet) així que s'han d'augmentar els paràmetres

**Correcció: REGULAR.** La resposta identifica correctament el _problema_, però falla en la _solució_.

- **Correcte:** La identificació del problema és excel·lent. Efectivament, una regla com X→Llet pot tenir una confiança alta simplement perquè la llet és un ítem molt freqüent (té un suport alt), independentment de X.
    
- **Incorrecte:** La solució no és "augmentar els paràmetres". La solució és introduir una nova mètrica anomenada **Interès** (Interest), definida com I=p(j∣i1​,...,ik​)−p(j). Aquesta mètrica mesura quant més probable és j donat i, en comparació amb la probabilitat base de j.
    

---

#### 8. Pregunta 5 (Dades, Informació, Coneixement)

> Les dades són un recull de unitat amb mesura (1 metre) la informació és aquell context que rodeja la dada, una petjada fa un metre, i el coneixement seria aquesta aplicació si ha fet 32 petjades, ha recorregut 32 mentres

**Correcció: BÉ.** La resposta captura la jerarquia conceptual correctament, alineant-se amb les definicions del temari.

- **Dades:** Registres (ex: "1 metre").
    
- **Informació:** Dades + Context (ex: "una petjada fa 1 metre").
    
- **Coneixement:** Anàlisi, aplicació o presa de decisions (ex: "32 petjades impliquen 32 metres recorreguts").
    

---

#### 9. Pregunta 9 (Algorisme vs. Model)

> Un algorisme de predicció és un model sense entrenar ni acotar, és la base. el model és l'algorisme ja preparat per ser utilitzat

**Correcció: BÉ.** La resposta és conceptualment correcta i utilitza la mateixa analogia del temari (recepta vs. plat cuinat).

- **Algorisme:** És el procediment o el mètode d'aprenentatge; "la recepta de cuina". La resposta ho defineix bé com "la base".
    
- **Model:** És el resultat de l'aprenentatge (l'algorisme ja entrenat amb dades); "el pastís acabat" o "llest per fer prediccions". La resposta ho defineix bé com "ja preparat per ser utilitzat".
    

---

#### 10. Pregunta 10 (Recol·lecció Explícita vs. Implícita)

> Com demanes les dades, amb explícita li fas preguntes al usuari i amb implicita toques nomes dades més pures, num de visualitzacions, temps que un usuari aguanta abans no treu una serie, etc

**Correcció: MOLT BÉ.** La resposta és clara, concisa i precisa, aportant exemples correctes per a ambdós mètodes.

- **Explícita:** Demanar activament l'opinió a l'usuari (ex: puntuacions).
    
- **Implícita:** Inferir preferències del comportament (ex: compres, visualitzacions, temps, comparticions).
    

---

#### 11. Pregunta 8 (Estabilitat Item-based vs. User-based)

> ja que els usuaris d'un dia per l'altre canvien molt, no són estables, i el que t'agrada avui al mati (o lo que et ve de gust) és diferent a la tarda, i per aquests recomanadors es consideren due spersones diferents Amb els íteems això no passa, i encara que les recomanacions siguin menys acurades, solen aguantar millor el temps

**Correcció: MOLT BÉ.** La resposta és excel·lent i reflecteix perfectament l'explicació del temari.

- **Basat en Usuari:** És molt inestable perquè els gustos dels usuaris canvien molt ràpidament ("d'un dia a l'altre").
    
- **Basat en Ítem:** És més estable, ja que les comparacions i relacions entre ítems (ex: dues pel·lícules del mateix director) canvien molt més lentament en el temps.
    

---

#### 12. Pregunta 2 (Euclidiana vs. Pearson)

> Depen de si les dades estàn o no calibrades. Farem ús de la distància Euclidiana si ho estàn, sinó prearson

**Correcció: MOLT BÉ.** Resposta perfecta. És concisa i identifica el concepte clau.

- **Distància Euclidiana:** S'utilitza per a sistemes **calibrats** (on una distància de 2 és el doble que 1, ex: minuts escoltats, distància a recórrer).
    
- **Correlació de Pearson:** S'utilitza per a sistemes **no calibrats** (on hi ha opinions subjectives, ex: valoracions d'1 a 5 estrelles).
# LLM

## Preguntes

### 1
Quina és la funció de l'entropia creuada en el context de l'aprenentatge atomàtic?
	- És una funció de perdua utilitzada en problemes de classificació.
	- Mesura la diferència entre distribució predita i real

>[!tip]
>El seu objectiu és quantificar com de "lluny" està la predicció del model (en termes de probabilitats) de la veritat absoluta (de les dades de prova).

### 2
Què distingeix un algorisme "amb context" d'un sense?
	- sense context: Processa les dades només sintàcticament
	- amb context: considera la relació de les dades amb el mon real
>[!tip]
>La diferència clau és si l'algorisme necessita entendre el significat o la semàntica de les dades per funcionar correctament 

