Segons ell classe + xula i difícil (examen, TOT)
Classificar en varies classes =<2 (comença amb index 0)

Aquest cop Veurem un recomanador com un problema de clasificació

Si en comptes d'una regressió (un valor) em dona una categoria
	Les classes són simbols

El que farem és un vector indicant la classe més X (Més gran o més guay)

- Per passar un vector de classes a prob hem d aplicar la formula de la diapo 3

- PQ volem fer això?
	Pq aquesta fòrmula funciona millor amb el ns estocàstic

# Cross Entropy
diapo 7
	les y són les classes
Depen de la classe agafem una o una altre


És una funció de K dimensions (K=num classes)

Si poses la classe que toca, pagaràs preu baix, i al contrari si t'equivoques

>[!info] Exemple
>Donat K=4
>Un objecte de classe 2 té aquesta representació:
>(0,1,0,0)
>I de classe 3
>(0,0,1,0)


>[!warning] OJO
>Les dimensions estaran barrejades, un director (cas de pelicules) no és dim 1
> i actor dim 2. Està tot barrejsat


diapo 12
Podem trobar versió petita de la matriu? que dongui resultats similars o iguals

Nosaltres fem factoritzacions en Matrius **QUE NO ESTAN PLENES** Té "forats"

Factoritzar una matriu és optimitzar
	(Minims quadrats)

-->Quan fem això, compte en no emplenar les caselles que no tenen res ( o si? no ho he sentit bé)
L'aproximació de la factorització de matrius no és la millor solució, soimplement dona una primera aproximació

# Factorization Machines

diapo 17

Perquè no recomanem series segons la hora del dia que s'obre la app, o quin dia de la setmana és, o des de on s'obre la app?

Ara si

Ara la [[Uni/3rAny/Parcials/ThTNUI/PPT3i4/Recomanacions colaboratives basats en semblança d'usuari|Matriu de recomanació]] Canvia, ja no és user-item
Ara la matriu 3x3 es converteix en 5 files, on cada fila representa una coordenada
-> Columnes verd fosc pot ser mati tarda nit (info extre -> Aux1)
->Columnes verd clar pot ser des de on s ha obert(info extra -> aux2)

Ara la metriu serà expressament binaria
	Si tinc 24h al dia necessitaré 24 columnes per cada "classe"

la y (vermell) serà la mateixa columna per tothom, que és lo que agrada


El Problema és que és poc escalable

### Factorization Machines amb factorització de matrius

Ara sumem les dues (diapo 22)

Això acponsegueix reduir l'exponent per Moltissim
de aporx $10^{10}$ Passes a $10⁶$ 


La funció de perdua, epr optimitzar serà diferent, no volem que s aproximi a 1, vull que ordeni


(diapo 28)
ha vist item 2, no el 1, suposem que agrada més el 2 que el 1
Està fent dataFrrame amb u,i i j


BPR loss function
Aquesta funcio es minimitza quan subi és gran i sub j petita

Així optimitzem el model tq ordeni bé



EL Model diapo 22 es pot fer per aproximar 1 o aproximar què agrada més


Aquest recomanador funciona MOLT bé

Se li han de donar les dades "Ben donades"
Res de posar primer 1 o primer 0 o coses així


>[!infp] Factorization machines és tipic recomanador de Netflix
> El recomanador de Amazon és un recomanador per sessió
> Ja que normalment compres més d'una cosa, 
> i el que compres avui, segurament no té res a veure amb demà o ahir

Diapo 34
Cada quadre és una sessió

En aqust tipus, l'ordre en que miro les coses, importa moltissim


Pq un model lineal no té sentit que passi per 0,0
	QUan tens un mode lineal sempre necessites un $\omega_0$ per evitar que passi per 0,0 

Si resulta ser que una columna no és important, posarà un 0, no posar unes columnes pot fer que perdi expressivitat ($w_i$) diapo 25
