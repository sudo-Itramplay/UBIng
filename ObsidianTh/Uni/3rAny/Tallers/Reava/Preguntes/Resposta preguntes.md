
## Optimització - L'aprenentatge a partir de dades no és un procés purament d'optimització

L'optimització es defineix com el procés de seleccionar el millor element d'un conjunt d'acord amb un criteri determinat, generalment cercant el màxim o el mínim d'una funció. Tot i així, en l'aprenentatge de dades, aplicar un algorisme d'optimització de manera directa pot ser perillós per les següents raons:

* **Sobre-estimació (Overfitting)**: Es pot trobar un model que aproximi extremadament bé les dades d'entrenament (error quasi zero), però que predigui molt malament valors de dades que no estaven al conjunt inicial.


* **Generalització**: L'objectiu real no és només representar el conjunt de dades passat, sinó ser capaç de generalitzar i predir valors per a dades futures o desconegudes.


* **Metodologia**: Per controlar això, s'utilitzen tècniques com la **validació encreuada (cross-validation)**, on el model només s'ajusta amb un subconjunt d'entrenament i es valida amb un de prova.


>[!example] **Exemple il·lustratiu**:
Si volem predir el preu dels pisos a Barcelona segons els metres quadrats, un algorisme d'optimització pura podria crear una corba complexa que passi exactament per cada punt de la nostra taula. Tanmateix, si aquesta corba és massa ajustada, podria donar un preu absurd per a un pis nou que simplement tingui una mida lleugerament diferent, fallant en la seva funció predictiva.

## Recomanadors - Càlcul de distància entre usuaris

En un recomanador col·laboratiu basat en la semblança d'usuaris, s'utilitzen principalment dues tècniques per calcular la "distància" o similitud entre els vectors de preferències:

1. **Semblança del Cosinus (Cosine Similarity)**:
* **Funcionament**: Mesura l'angle entre els vectors d'usuaris en un espai multidimensional.


* **Aplicació**: S'aplica quan les dades són esparses o binàries (per exemple, si un usuari ha comprat un producte o no), ja que no té en compte la magnitud absoluta de les valoracions, sinó la seva direcció.




2. **Correlació de Pearson**:
* **Funcionament**: Centra les dades restant la mitjana de les valoracions de cada usuari abans de calcular la similitud.


* **Aplicació**: És ideal quan els usuaris tenen biaixos en la seva forma de puntuar (inflació de notes). Per exemple, un usuari que sempre posa entre 4 i 5 serà comparat correctament amb un que és més estricte i posa entre 1 i 2, si els seus gustos relatius coincideixen.





## Recomanadors - Per què Factorization Machine és un model lineal

Les Factorization Machines (FM) es consideren models lineals perquè la seva formulació base és una combinació lineal de característiques.

* **Incorporació de característiques**: Poden incloure atributs arbitraris (com gènere, dia de la setmana, etc.) representats com a vectors binaris.


* **Interaccions de factors latents**: Tot i que capturen interaccions entre parelles de característiques, ho fan modelant aquestes interaccions com un producte escalar de vectors latents. Aquesta estructura permet que el model es comporti linealment respecte als paràmetres apresos, facilitant l'optimització i la incorporació de feedback implícit per a rànquings.



## Problema de les pomes i la cervesa (Bolquers i cervesa) - Heurística de la funció d'utilitat

Encara que l'exemple clàssic del document menciona **bolquers i cervesa** (no pomes), l'heurística utilitzada es basa en el model de la "bossa de la compra":

* **Suport**: És el nombre o fracció de bosses que contenen un conjunt d'ítems determinat.


* **Confiança**: Probabilitat que una bossa contingui l'ítem  si ja conté l'ítem .


* **Interès**: Es defineix com la diferència entre la confiança de la regla () i la probabilitat basal de trobar l'ítem  en qualsevol bossa.


* Una regla és "interessant" si té un valor d'interès molt alt (positiu o negatiu), indicant que la presència d'un producte influeix significativament en la compra de l'altre.





## Inferència - Model Bootstrapping

* **Funcionament**: Consisteix a crear una aproximació de la distribució mostral mitjançant un **mostreig aleatori amb reemplaçament** a partir del conjunt de dades original. Si tenim  elements, seleccionem  elements a l'atzar on alguns es poden repetir.


* **Per a què serveix**: Permet mesurar la incertesa d'estadístics complexos (com mitjanes o quantils) quan no disposem d'un model teòric o generador de les dades.


* **Exemple d'escenari**: Estimar quants clients entren de mitjana cada dissabte a una botiga. Com que no tenim un model matemàtic de "com entren els clients", fem "bootstrap" sobre les dades de dissabtes passats per veure com varia la mitjana.



## Exploració-Explotació - Mètode de mostreig de Thompson (Thompson Sampling)

* **Funcionament**: Modela la incertesa construint una distribució de probabilitat a partir de les recompenses rebudes. En el cas de recompenses binàries (èxit/fracàs), s'utilitza la **distribució Beta**.


* **Procediment**: Per cada acció possible, es fa un mostreig aleatori de la seva distribució Beta i es selecciona l'acció que retorna el valor màxim.


* **Actualització de paràmetres**:
  * La distribució Beta té dos paràmetres:  (èxits) i  (fracassos).
  * Si triem una acció i la recompensa és 1 (èxit), s'incrementa el seu .
  * Si la recompensa és 0 (fracàs), s'incrementa el seu .


---

# Preguntes 2n Parcial

## Bayes - Exercici de Probabilitat

El Teorema de Bayes s'utilitza per actualitzar la nostra creença (hipòtesi ) en funció de noves dades ():



En un context acadèmic o mèdic:

* és la probabilitat **a priori** (per exemple, la taxa base d'una malaltia o d'un aprovat).


*  és la **versemblança** (probabilitat de donar positiu si tens la malaltia).


*  és la probabilitat **a posteriori** (la probabilitat real d'estar malalt un cop tens el resultat positiu).



## Perceptró i limitacions (Notebook 1)

Les xarxes neuronals totalment connectades (Fully Connected - FC) tenen limitacions crítiques per a imatges (com el dataset MNIST):

* **Explosió de paràmetres**: En imatges d'alta resolució, el nombre de pesos creix de forma insostenible (ex: una imatge de 1MP requeriria milers de milions de paràmetres).


* **Pèrdua d'informació espacial**: L'operació de "flattening" (convertir la imatge en un vector 1D) destrueix la relació estructural entre píxels adjacents.


* **Inestabilitat**: Són molt sensibles a petites translacions o rotacions de l'objecte dins la imatge.



## Com solucionar FC amb CNN (Convolutional Neural Networks)

Les CNN resolen els problemes de les xarxes FC mitjançant tres mecanismes clau:

1. **Camps receptius locals (LRF)**: Cada neurona només es connecta a una petita regió local de la imatge, reduint dràsticament el nombre de paràmetres.


2. **Compartició de pesos**: S'aplica el mateix filtre a tota la imatge, assumint que una característica (com una vora) és rellevant en qualsevol posició.


3. **Pooling (Max-Pooling)**: Redueix la mida de les representacions i proporciona una certa invariància a petites translacions.


4. **Padding**: S'afegeixen vores a la imatge per evitar que es redueixi massa ràpidament després de moltes capes de convolució.



## Ètica: Separació i Independència - Exemple Universitats

L'equitat en algoritmes de decisió es pot mesurar de diverses maneres:

* **Independència (Paritat Estadística)**: El resultat de l'algoritme és independent del grup protegit. Exemple: La universitat admet el mateix percentatge d'estudiants de dos grups diferents, independentment de les seves notes.


* **Separació**: Es demana que les taxes de "True Positives" siguin iguals per a tots els grups. Exemple: Dos estudiants (un de cada grup) que tenen el mateix potencial real d'èxit han de tenir la mateixa probabilitat de ser admesos per l'algoritme.


* **Incompatibilitat**: Es pot demostrar matemàticament que en un problema de decisió binari no es poden mantenir la independència i la separació al mateix temps.

## Com entrenar un LLM

L'entrenament d'un Large Language Model segueix tres fases principals:

1. **Pre-entrenament**: El model aprèn a predir el següent token de forma autoregressiva utilitzant milions de dades de text. S'utilitza la funció de pèrdua d'**entropia creuada (cross-entropy)**.


2. **Supervised Fine-Tuning (SFT)**: S'ajusta el model amb parelles d'instrucció-resposta escrites per humans per aprendre a seguir ordres útils.


3. **RLHF (Reinforcement Learning from Human Feedback)**: S'utilitza un model de recompensa (jutge) basat en preferències humanes per refinar el comportament del xatbot cap a respostes més segures i elegants.
