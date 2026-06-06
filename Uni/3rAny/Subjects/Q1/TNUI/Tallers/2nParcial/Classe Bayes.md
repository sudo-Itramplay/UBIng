Teorema de Bayes

Volem fer ús de Bayes per fer un model probabilistic a partir de dades

--> Pensare els problemes des del punt de vista Bayesià

Això és una EINA no una manera de pensar

ChatGPT modela la funció de distribució del llenguatge natural

és a dir, ha passat el com parlem a una funció de distribució

##### Conceptes
- Probabilitat marginal $P(A)$
- Probabilitat Conjunta $P(A, B)$
- Probabilitat condicional $P(A|B)$

El dibuix del ppt separa els numeros per grup, osigui, la gent que va aprovar algorismica són 6, no és que 6 sigui tot el conjunt suspens AA

>[!important]
>SEMPRE POSA AL EXANEB LO DELA PROBABILITAT CONDICIONAL

No sé que li passa que diu que no val la pena pensar la condicional pq és contre intuitiu

---

## Teorema de Bayes
#Frequentista
Les lleis de probabilitats compleixen unes lleis molt simples

el teorema de Bayes és la regla de la cadena
$$
P(B|A) \cdot P(A) = P(A,B)
$$

$$
P(B|A) \cdot P(B) = P(A,B)
$$


I ARA BAYES:
$$
P(A|B) = \frac{P(B|A) \cdot P(A) }{P(b)}
$$
Per invertir condicions de manera fàcil, donat que a vegades és més fàcil (o únicament factible) calcular una que l'altre

### Interpretació Diacrònica
#baysesia
(Diacrònica té en compte el temps, de si A va abans de B o no)
Aquesta interpretació de Bayes:

- El primer exemple, mira que la solució és o True o False (han estat discriminades o no)
Tot i rebre una base de dades immensa (com s'esmenta al enunciat) lo únic que pot fer és reduir o reforçar la nostra hipòtesi

La fermetat d'una hipotesis és com una probabilitat

Ara canvia el significat de:
- $P(H)$ Probabilitat de $H$ abans de dades $D$
-  $P(D|H)$ Probabilitat de $H$ DESPRES de dades $D$

La estadística Bayesiana interpreta les probabilitats en mesures de credibilitats

 HI HA probabilitats que puc repetir (frequentista) com la de tirar monedes x vegades

Hi ha probabilitats que no (està mort bin laden? Això no es pot repetir, nomes es pot mirar segons el que jo he vist)  aquesta creença fa que canviem de tipus de càlculs (bayesia - Hipotesis basat en dades) 

$$
P(H|D) = \frac{P(D|H) \cdot P(H) }{P(D)}
$$
La probabilitat d'una hipotesis que jo tenia com canvia després de veure les dades


### Com interpretem probabilitats bayesianament

- $P(H|E)$ Probabilitat després de veure dades 
-  $P(H)$ Probabilitat ABANS  de veure les dades
- $P(E|H)$ Versemblança de l'evidència
- $P(E)$ Constant de normalització

##### Versemblança
Què tant bé una hipòtesis explica unes dades

$$
\prod_i{p_H(x_i)}
$$
on $p_H$ representa una funció de distribució de dades segons probabilitat (hipòtesi?)

Les hipotèsis no canvien

Amb la linia vermella li restarem credibilitat, ja que la representen molt poc
a la verda li pujarem credibilitat

##### Constant de normalització

és exhaustiva si nomes pot estar viu o mort (Crec k és al reves)
és exclusiva si ...


$$
P(H_{si}|E_{si}) = \frac{P(E_{si}|H_{si}) \cdot P(H_{si}) }{P(E_{si})}
$$
Que és igual a fer
$$
P(H_{si}|E_{si}) = 
\frac{    
P( E_{si} | H_{si} ) \cdot P(H_{si}) 
}
{ 
P(H_{si}) \cdot P(E_{si}|H_{si}) + P(H_{no}) \cdot P(E_{si}|H_{no})
}
$$

>MIRAR FORMULA


# MONTY HALL PROBLEM



# Problema Locomotora
Estimar numero de locomotroa, nomes sabent $1,2,... N$ és el num k se li posa a cada locomotora

Per saber el número de locomotores que veiem

Veiem la locomotora 60, sabem que com a mínim té 60

Què sabiem de N abans de veure les dades?? Què sabem ara??

Si mai hem vist cap locomotora, podriem estimar un número

la $P(H_i) = cte$ totes valdràn el mateix pq encara no sé res, suposare que no tindra més de 1000 (però és arbitrari)

Si hem vist 60, sabem que tots els numeros inderiors el resultat serà 0, i a partir d'aquí serà $\frac{1}{Numero de tren max}$  En el cas aquest $P(H)=1/60$ i la seguent $P(H+1) = 1/H+1$

En comptes de calcular ns k podem normalitzar

LLavors un frequentista contestaria que la P més probable és la 60

Com que això, tot i ser la més probable, no sembla correcta, el Bayesià diu

Contesta amb la mitjana de la distribució a posteriori

això és la hipotesis que correspon a H max 333

Llavors aquesta no és la hipòtesis més probable
però si la més versemblant

A mesura que veiem locomotores, si només veiem numeros baixoss, els números baixos començaràn a tenir més probabilitat


## GOOGLE

uni grama és paraules diferents

bigrama és conjunts de paraules no repetides
.
.
.

Google ens dona la quantitat de x que apareixen, però no quins bigrames apareixen 

Tot i així podem fer models probabilistics en base el num

En comptes de calcular totes les probabilitats, si calculessim totes les probabilitats estartia fent cassos inútils o innecessaris (es pot solucionar amb prog dinàmica)

Puc anar unint com a probabilitat de les que la segueixen


Memo no és el que més li interessa

Pwords més
Pwords funciona semblant a
$$
\prod_i{p_H(x_i)}
$$

Aquesta simplificació fa que si en una frase surt

....tositdown...
el model fa
to sitdown


En comptes de fer les probabilitats de les pareules independentment, farem la probabilitat segons la paraula i la anterior o de les parelles

la segona donada la primera

la ultima donada la penultima

Això són aproximacions



