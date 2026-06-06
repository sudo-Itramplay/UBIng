
## Perquè cal fer inferències?

>[!Note] Perquè cal fer inferències?
>Les dades, de per si, no parlen, és l'analista qui els hi dona un sentit
>
>Normalment hi ha moltes explicacions possibles amb les mateixes dades

-> Les dades no sempre són concloents
>[!danger] La trampa de la Correlació 
>**Correlació $\neq$ Causalitat.** El fet que dues variables es moguin juntes no vol dir que una causi l'altra.

- **Variable de Confusió (Confounding Variable):** Sovint existeix un "tercer element" ocult que és la causa real d'ambdues condicions observades.

- _Exemple clàssic:_ El consum de gelats i els ofegaments a la platja tenen correlació positiva. 
	- Causa? No. 
	- El tercer element és la **Calor (Estiu)**.



Per intentar evitar la sobre-interpretació i donar conclusions el més marcades a unes dades possible s'ha de seguir una metodologia

>[!tip] Metodologia
>1- Formular Hipòtesis
>2- Recollir dades
>3- Validar i interpretar resultat
>4- Tornar al primer punt refinant hipòtesis

-> Una hipòtesis es formula **ABANS** de fer l'experiment
Les dades es seleccionen sempre en base a la hipòtesis, i aquesta es valida usant tècniques metodològiques i estadístiques

# Maneres de validar hipòtesis

>[!question] Com es valida una hipòtesi?
>Hi ha dos tipus de raonament en el que ens basarem per fer la validació:
>	- **Estadística Freqüentista**
>	- **Estadística Bayesiana**


## Estadística Freqüentista

>[!summary] Resum
> Es basa en la freqüència relativa a llarg termini.
>  La "veritat" ve donada per una **població infinita** i un valor únic($\mu$),
>   de la que nosaltres sabem que nomes tenim una **mostra**,
>    en la que hi calculem **estimacions** ($\hat{x}$). 
>
>    Les dades (mostra) que nosaltres agafem són aleatòries.

El concepte del que parteix aquesta noció és el de **funció de distribució mostral**
#### Com obtenim la Distribució Mostral?
Com que a la realitat només tenim **una mostra** i no podem repetir l'experiment 10.000 vegades (és infactible), necessitem aproximar aquesta distribució per mesurar la incertesa.

Tenim dos camins per generar aquesta aproximació:

1. **Mètode Teòric (Clàssic):** Ús de teoremes matemàtics (com el Teorema del Límit Central) que ens diuen quina forma _hauria_ de tenir la distribució (N(μ,σ)).

2. **Mètode Computacional (Modern):** Ús de potència de càlcul (ex: _Bootstrapping_) per simular el re-mostreig i construir la distribució empíricament a partir de l'única mostra que tenim.

La **Validació** d'una hipòtesis es fa mitjançant el `p-value` , aquest tranforma una intuïció en una mètrica, per tal de mesurar la incompatibilitat.

- **p-value Alt (ex: 0.60):** "El que he vist és súper normal. Cap sorpresa." → Les dades són compatibles amb H0​.

- **p-value Baix (ex: 0.03):** "El que he vist és molt estrany. Si H0​ fos certa, això seria una casualitat raríssima." → Les dades són incompatibles amb H0​.

>[!fail] Warning
>Això no vol dir que la hipòtesis contraria tingui un 97% de ser certa




>[!warning] Ojo 
>El matís clau En l'estadística freqüentista, **mai assignem una probabilitat a la hipòtesi**. La hipòtesi és certa o falsa (binari). La probabilitat s'assigna a les **dades**.

### 3. Exemple Pràctic: Llançar Moneda

> [!example] Cas d'estudi: 
> Moneda trucada o atzar? 
> Volem saber quina probabilitat hi ha de que una moneda llançada a l'aire dongui cara o creu

##### **1. Plantejament (Posició Escèptica)**
Davant una moneda, assumim la posició escèptica per defecte:

 - **Hipòtesi Nul·la ($H_0​$):** La moneda és equilibrada ($P=0.5$).
   
 - **Hipòtesi Alternativa ($H_1$​):** La moneda està trucada $(P^I=0.5)$.

##### **2. L'Experiment** 
Llencem la moneda $n=250$ vegades i obtenim **140 cares**.


 ##### **3. El Model (Mètode Clàssic)** 
 Assumim que, sota H0​, la variable "nombre de cares" segueix una distribució coneguda (**Binomial**):
 
$$
X∼B(250,0.5)
$$

 ##### **4. Càlcul del p-value** 
 Calculem la probabilitat d'obtenir aquest resultat (o un de més extrem) si la moneda fos bona:
$$ 
P(X≥140∣H0​)≈0.0333(3,33%) 
$$

##### **5. Conclusió** 
Com que 3,33%<5% (llindar estàndard), el resultat és massa improbable per ser casualitat. **Rebutgem H0​**; la moneda probablement està trucada.


# A/B Testing

