
## 1
Filtrar data frame amb dos filttres amb pandas

- No fer servir and, &
- amb els parentesis definim les diferents condicions


## 2
Counting, o num tickets

count = df.groupby()[].count()

.count()
	Conta tota les rows que no tenen NaN



## 3
Pandas permet fer operacions amb vectors
Si volem canviar una columna sencera per a totes les files es pot fer bastant simplement

## 4
inplace-> Ns que fa, però no li agrada
df.dropna() és més fàcil de llegir

## 5
df['x'] = df.aply(lambda )
lambda aplica funcio inside

Al fer coses així mirar si panda ja ho té implementatg

## 6
Un None no és un NaN
Panda no ho interpreta igual

Fer servir NaN si el que vull és buidar

## 7
Diferència entre `loc` i `iloc`
loc get row and columns with particular label
iloc get rows at integer locatio 

## 8
Compte amb els warning alhora d'afegir columnes

loc per afegir columnes
sino fes un copy de la taula i afegeix la columna

## 9
Explicar les gràfiques mirant el max, el min, la comparació directa
i dir què creiem nosaltres que passaria

## 10
Mirar si mateixa graella comparteixen eixos o no
	A vegades interessa i a vgeades no

## 11
Descriure de manera qualitativa i quantitativa

Raonar Qualitativament
	Sense numeros
	Raonarme el comportament sense numeros
Raonar quantitativament
	Si cal, mirar i fer Ratios

## 12
A la hora de descirue o raonar intentar adivinar coses, fer relacuons, o lo que sea
s