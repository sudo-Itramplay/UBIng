---
id: classe3
aliases: []
tags: []
---



 a partir de pg 35 de ML 2
# Data Transformation 


SI son molt diferents tenen més pes? Mirar al ppt a que es refereux


Num habitacoins i de banys no tindra cap efecte per veure si són similars (?) 

Vale, això ho diu que si no normalitzem les que tinguin més variança tindràn més força 

I per això volem Normalitzar 

Caracteristiques amb outliers ns que no es podra fer ns que normalitzacio 

Els nostres modesl treballen molt bé amb gauss, asumeixen que es així 


Per això volem intentar que la nostres dades accabin amb una distribucio normal d'alguna manera 



despre del log (?) podem tornar a fer l'scaling 


Si tenen formes molt rares es sol discretitzar, particionem les dades en x valors discrets segons la seva popularitat (per exemple) per espais quivalents o per quantils (els boundaries) 

Lo graciòs és quan tenim poques dades 


Categorical encoding:
- ----------
- One hot 
- Ordinal 
- Embeddings 


Les dades que tenim són de Melbourne 

Label encoder és posar simplement un ID 

Però amb la IA hem de posar, d'alguna manera , que un isgui millor qu el'altre o ordenable, perquè suposa que numeros aprop són semblants 

és a dir que el 4 és més semblant que el 3 que no pas del 1 


El onehot encoding passa els ids en una matriu --> Agafarem una feature (color) i si tenim 4 valors, passaran a ser 4 features i cada un dels vvalors dirà si forma o no forma part (creo, almenys així ho vaig entendre)



El profe diu que això és de putos noobs normies i que nosaltres serem super niche i performatics


Amb one hot no pot ser tot un o tot zeros, aquell el dichegem 


Target Encoder és molt guay i edgy 

Enlloc d agafar tantes feature ccom categires, posar una estadistica a cada valor, si tens casa de 2 habitacoins 1 bany i de st gervasi i 120 m2 El nostre factor serà(2,1,(onehot per gervasi), 120)


KNN asumim que les variables hauriem de notmalitzar ja que si no 120 tindrà més valor que el onehot encoder i no té pq 

Barrote del compai: [15:36, 28/9/2026] David Hidigeis: Mitja 0 variança 1
[15:36, 28/9/2026] David Hidigeis: Mitja 0 variança 1
Això per knn normalitzar



Però un cop normalitzat el one hot tindrà molt més valros pq son molt numero 

i llavors ens quedarem amb una unica variable (exemple, de st gervasi passarem al preu mitja o a la mediana de preus o el que sigui )

En comptes de barri pillem una estadistica de barri 


Target encoder funckona molt bé amb moltes caracteristiques 


Lat i long hi ha una banda més barate que l'altre 
Però lat long amb regressor lineal defineix DEPENDENCIA lineal --> Al dataset hi ha distancia del centre, ell sembla que vol fer servir un d'aquests encoders, però podriem fer distancia del centre i passaria a ser lineal i gaussia no?


Sembla que tenim 3400 dades i casi el mateix numero de carrers (Per la pràctica )

Embedding crec que és 

Per cada categoria el representem amb un factor numeric per al LLm (Eign, explica millor ) 
Volem definir uns vectors que defineixin paraules i que paraules intercanviarbles tinguin vector proper 

No free lunch therome: No hi ha un model millor

EL QUE SI: VOLEM GENERALITZAR EVITAR OVERFITTING A TOTA COSTA 

Nosaltres es perem que quantes mes dades l error ***PERO*** el edgy i guay del santi diu que però això serà pel meu model amb lo de testing, però amb les dades de test 

però veurem que amb poques dades hi haura molt poc errror però al final,s aplanara d alguna manera, i l'error de train i test s'aproparà cada cop més 
  
> PEro jo crec que el que ha dit no té sentit pq segons ell amb una dada tens 0 error sobre si mateix pq nomes hi ha una i a mesira que augmento sample puja error respecte ell mateix? No te sentit si jo per mirar error faré servir validació no? Quina merda de frase es aquesta?
  Això es veu que es complexitat en numero de columnes i model ns s'ha explicat fatal 


Model molt simple amb moltes dades te molt error i l'error baixa logaritmica ment (al principi millora molt dsps molt poc ) però la complexitat puja MOLTISSIM segons baixem l'error 

DE MODEL SIMPLE lINEAL MODEL -> svm-> Random forest -> NN 


grafics compllexitat error fara una parbola per alguna rao ns pq 


El millor model serà el minim de la linoia vermella pq ns patata 

Segons ell quant mes compllex mes overfiting



#### Feaure set size vs Error 

Hi ha un parell de columnes que son super chachis i moltes que son soroll i copies de les anteriors 

### Finetune your model és trobar els millors parametres per ser molt guays i tenir un model pila d'ajustat i sexy

test ha ser ser suficientment gran per testejar bé l'error 

Provar amb diferents tests per mirar que tant guay pot arribar a ser 

NO podem pendre decisions sobre test, si canviem una dada i resulta que test va super chachi pues mal no podem (I com hem de procedir? xdd )























ARA:
Cross validation sembla important, definir bé en aquests apunts el pq de train test i validation, MOLT Ben definit 


El test és el del public score, i hi ha un private score que és pel que volem fer amb validation, test nomes el tindrem pel final de la P1 

Si private i public son simiilars chachi, si no overfiting o underfitting 

Si prenem decisions amb validation ho farem malament i pues ho hem de fer poc pel que es veu podem reduir una mica el problema de la particio i overfiting amb el cross validation fent particio de dades en cert numero de grups i aleatoriament escull train i test per iteracio 



Un cop el model es validi presentem la solucio 



El test a prior ja està fet pq ja està creat en el kaggle



Jo agafaria distància del centr i longitud (si és la ohoritzontal ) per com funciona melbourne i inclouria any construit i habitacions ja que hi ha una relació MOLT directa 


# ML3 


Linear regression for advertising data: ës bona idea fer servir les dades per això? 

Linear és MOLT usat per simplicitat i facil de veure veurem correlacions, no causes (nomes podrem dir què passa no pq )


asumim el model patata que posa els apunts 

la e es algo que el model no pot fer res , quantes mes dades tinguiem millor estimarem els parametres B0 i B1 







