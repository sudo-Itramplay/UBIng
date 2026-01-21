**Escenari**
- Plantejat una situació que, un cop donada una oferta a un usuari (ofertes de vols, productes neteja, alimentació, ...). 

- Depenen l'acció del usuari donarem una recompensa o una altre en funció al que ens vagi bé (l'usuari ha clicat, ha gastat més de X diners, ...)

- Cada recompensa, per a cada opció, es pot modelar com una funció de probabilitats
	- La recompensa és una variable aleatoria

Com que el nostre objectiu és maximitzar la recompensa total al cap del temps, triariem d'oferir sempre la millor acció. (algorisme optim $A_{opt}$)

>[!info] OJO
>Per fer això necessitariem saber la mitxana real, cosa generalment noaccesible

Com que coneixer la mitjana real és molt poc probable, l'altre opció més realista seria trobar un algorisme $A$ que maximitzi **La recompensa total esperada sobre un periode de temps**  ($T$)

>[!tip] Vist des de un altre punt:
>Volem minimitzar la perdua (regret)
>$$
>R(T = Guanys_{A_{opt}}(T) - Guanys_{A}(T))
>$$

En el nostre cas, cada acció té una _recompensa esperada_ o _recompensa mitja_ donada l'acció que es selecciona. Aquest concepte s'anomena **_valor_** de l'acció.

>[!Warning] Tragaperras
>Pensa que estem parlant d'un tipus de problema on tenim un únic accionan (la palanca) i una sortida amb recompensa aleatoria
> - Comencem no sabent el valor de l'acció, però podem acabar fent estimacions

Per moldelar això necessitarem anar fent decisions entre **Explotar** o **Explorar** 

- Explorar: Millorar les nostres estimacions sobre el valor de les recompenses
- Explotar: Triar la opció que _Creiem_ que té millor recompensa

## Com i Quan escollir:


### Com estimar els valors de les accions

#### Mètode mostra promitjada

- Anomenarem $Q^*(a)$ al valor real de l'acció $a$ (valor de la mitja de recompenses rebudes al fer l'acció $a$), que començarà sent desconegut
- Anomenarem $Q_t(a)$ al seu valor estimat després de $t$ jugades

$$
Q_t(a) = \frac{r_1 + _2 + \dots + r_{k_a}}{K_a0}
$$


Quan $K_a$ sigui 0, assignarem un valor per defecte (0 o -1) segons el que ens interessi, sabent que si $k_a \to \infty$ més s'aproparà $Q_t(a)$ a $Q^*(a)$  

>[!warning] OJO
>Podriem pensar que la millor manera de resoldre això és fent $t$ jugades _Explorant_ i a partir de llavors fer nomes _Explotació_, però això ens donaria massa informació de jugades no optimes i poca d'altres més optimes més llunyanes al inici.
>

##### **$\epsilon$** Voraç
Afegir un component $\epsilon$ que per escollir entre explotació i exploració

Això permetrà que al llarg del temps explorem totes les opcions  que  $Q_t(a)$ s'apropi a $Q^*(a)$  

>[!fail] Problema 
>És un mètode simple i efectiu però dona igual probabilitats tant a un com a l'altre de ser escollits

###### **Softmax** (amb temperatura)
Escull una acció $a$ a la jugada $t$ segons:
$$
σ(z)_i​= \frac{ e^{Q_t(a)/ \tau}}{ \sum^n_{b=1} e^{Q_t(b)/ \tau}}​
$$

On:

- $\tau$ : Temperatura
- n : numero de classes (accions)
- $z_i$ : és el valor d'entrada per la classe $i$
Axiò provoca que totes les accions siguin equiprobables

>[!tip] Com afecta la temperatura?

1. **Temperatura baixa (T<1):**

Les diferències entre els logits es **magnifiquen**.

- **Efecte:** La distribució es torna més **apuntada** (_peaky_).

- **Resultat:** El model assigna gairebé tota la probabilitat a la classe amb el logit més alt (s'aproxima a una funció `argmax`).

- **Ús:** Quan volem respostes deterministes, precises i conservadores.

2. **Temperatura Estàndard (T=1):**

Equival a la funció Softmax normal.

- **Efecte:** Respecta la distribució natural apresa pel model durant l'entrenament.

3. **Temperatura Alta (T>1):**

Quan T és gran, les diferències entre els logits es **redueixen** (es divideixen per un nombre gran).

- **Efecte:** La distribució s'** aplana** (_flattening_). Les probabilitats s'acosten les unes a les altres.

- **Resultat:** Augmenta l'entropia. Les classes menys probables guanyen opcions de ser escollides. S'acosta a una distribució **uniforme** si T→∞.

- **Ús:** Per afegir diversitat, creativitat o exploració (ex: Generació de text, Reinforcement Learning).


### Problemes No estacionaris

>[!summary] Problema No Estacionari
> Definició Un problema és **no estacionari** quan la distribució de probabilitat o les recompenses de l'entorn **canvien amb el temps**.

En contrast amb un entorn _estacionari_ (on les regles són fixes), aquí el que era una bona decisió ahir, pot ser una mala decisió avui.

