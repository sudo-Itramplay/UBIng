#  Optimització
Procès de selecció del millor element (o conjutn) respecte un criteri

>[!info] info
>Moltes vegades el procès es redueix a la cerca d'un màxim o mínim d'una funció que representa el criteri


## Mètodes clàssics 
Mètodes per trobar el model més optim:

- **[[Unimodals Continues]]**
	Fem ús de mètodes centrats en la derivada o gradient
	- Hi ha garanties de trobar solució
- **[[Multimodal Continua]]**
	Fem servir mètodes estocàstics basats en derivades
	- **NO** hi ha garanties de trobar solució
- **Discretes**
	Hi ha mètodes especifics, com el _Simplex_ 

>[!info] Extra
>Hi ha mètodes estocàstics que serveixen per a qualsevol funció

- Representem vlors en conjunts de dades de:
	- $m$ Elements
	- $n$ Característiques

### Model
Expressió matemàtica $f_w$ que depen d'uns quants paràmetres $w$ i que representa de forma fidel i compacte un  aspecte de la matriu
- Ha de dependre d'un paràmetre per tal de ser un model


>[!tip] Idea Clau
>Al final optimitzem un model per obtenir els valors a i b que fàcin que $L$ sigui mínim

### Tenir en compte per un model

Aplicar directament un model d'optimització pot ser perillòs: **Overfitting**

- En general apendre de les dades vol dir Inferir

>[!todo] Millorar Defiició

>[!summary] Inferir
>Construir de baix cap a dalt
> de les dades cap el model
> - Una inferència pot ser estimar un model d'utilitat



Volem un model Compacte que ens permeti generalitzar dades

## Aprenentage de dades
### No supervisat

Donat un conjunt de dades **no etiquetades**, l'objectiu és trobar l'estructura subjacent o la distribució de les dades. Volem construir la funció més simple (model) que permeti **sintetitzar**, predir patrons o **generar noves mostres** coherents amb les originals.

### Supervisat
Donat un conjunt de dades **etiquetades** (parells entrada-sortida), volem construir una funció que realitzi un **mapeig** entre elles. L'objectiu és que, en rebre una dada nova no vista, la funció realitzi una predicció amb un **error mínim** (generalització).


## Sobre-estimació

Per evitar el problema de la sobre estimació utilitzem una metodologia adequada d'aprenentatge durant l'optimització

- Cross -Validation (grups test i set)

Per tal de fer la optimització la mètodologia més utilitzada és el descens del gradient


---

# Recomanadors

Amb lo d'adalt  com a base, fem una aplicació.

- Els recomanadors han de cercar i descobir (els cercadors nomes cerquen)

>[!summary] Descobir
>Trobar algo que no sabies que existia

- $C$ Espai usuaris
- $S$ Espau ítems

Amb els recomanadors intentem màximitzar la funció d'utilitat

$$
argmax[ u(c,s)]
$$

La funció d'utilitat és discreta, és una matriu $U$
$U$ No existeix, per lo que hem d'inferir  en els seus valors

## Tipus de Recomanadors

- [[ObsidianTh/Uni/3rAny/Tallers/1rParcial/PPT3/Tipus Recomanadors/Recomanacions colaboratives|Colaboratius]] - Utilitat a traves d'anàlisi de matriu
- [[ObsidianTh/Uni/3rAny/Tallers/1rParcial/PPT3/Tipus Recomanadors/Recomanacions NO colaboratives|No colaboratius]] - Utilitat a traves de descripció del contingut dels ítems
- Híbrids

Hi ha 2 tipus de colaboratius
[[ObsidianTh/Uni/3rAny/Tallers/1rParcial/PPT3/Tipus Recomanadors/Recomanacions colaboratives basats en semblança d'usuari|Recomanacions colaboratives basats en semblança d'usuari]]
[[ObsidianTh/Uni/3rAny/Tallers/1rParcial/PPT3/Tipus Recomanadors/Recomanacions colaboratives basats en semblança d'ítem|Recomanacions colaboratives basats en semblança d'ítem]]


### Semblança users
![[Pasted image 20260125115933.png]]
Recorrem Sp buscant usuaris semblants, multiplicarem la utilitat usuari amb semblança i farem suma
	La predicció es fa sobre un usuari que no té utilitat d'un item
	La semblança es fa sobre el conjunt on ELS DOS USUARIS tenen utilitat


### Espai preferències

Espai dels usuaris que han valorat ítems

Evaluarem distàncies dins aquest espai per determinar la similitud

##### Mètodes
- Distància euclidiana: $d(\mathbf{p}, \mathbf{q}) = \sqrt{\sum_{i=1}^{n} (q_i - p_i)^2}$
- Correlació de Pearson: $r_{xy} = \frac{\sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^{n} (x_i - \bar{x})^2 \sum_{i=1}^{n} (y_i - \bar{y})^2}}$

El coeficient de correlació de Pearson calcula una mesura de
l'ajust d'un conjunt de punts a una recta. Funciona millor que la
distància euclidiana si les components no estan ben calibrades.

#### 1. Correlació de Pearson: L'invariant lineal

La correlació de Pearson és extremadament robusta davant de transformacions lineals.

- **Invariant a la translació:** Si sumes una constant a totes les dades ($x + a$), la correlació no canvia. Això vol dir que no li importa on és "el centre" de les dades.
    
- **Invariant a l'escala (homotècia):** Si multipliques totes les dades per una constant positiva ($x \cdot b$, amb $b > 0$), la correlació es manté igual. Per això és ideal per comparar variables amb unitats diferents (ex: metres vs. quilograms).
    
- **Simetria:** $r(x, y) = r(y, x)$.
    
- **Límit:** Sempre està acotada en l'interval $[-1, 1]$.

#### 2. Distància Euclidiana: L'invariant rígid

La distància euclidiana conserva el valor real de l'espai físico-matemàtic, per tant, és invariant als anomenats **moviments rígids** (isometries):

- **Invariant a la translació:** Si mous tot el núvol de punts una distància fixa, la separació entre ells no canvia.
    
- **Invariant a la rotació:** Si gires l'espai respecte a un eix, la distància entre punts es manté (pensa en el teorema de Pitàgores).
    
- **Sensible a l'escala:** A diferència de Pearson, **NO és invariant a l'escala**. Si multipliques les dades per 2, la distància es multiplica per 2.
    
- **Propietats de mètrica:** Compleix la desigualtat triangular ($d(x, z) \le d(x, y) + d(y, z)$), cosa que Pearson no fa (Pearson no és una distància en el sentit mètric estricte).

>[!tip] Correlació negativa
>Recorda que n usuari que sigui invers al altree, és per tant molt semblant


### Semblança Items
![[Pasted image 20260125120826.png]]
Anirem recorrent, aquest cop, cp. 0 si no tenim u, si no farem la semblanca entre els ítems


## Recolecció de dades

#### 1. Recol·lecció Explícita

- **Definició**: Requereix que l'usuari expressi les seves preferències de manera directa i conscient.
   
- **Impacte**: Ofereix una millor personalització, però es considera intrusiva i pateix un biaix cap a usuaris amb opinions extremes (polaritzats).


>[!example] Exemple
> Ús d'escales numèriques, ordenació d'ítems per preferència, comparacions entre parells o creació de llistes de gustos. 
> 	**Exemple**: Demanar a l'usuari que puntue una pel·lícula de l'1 al 5.

#### 2. Recol·lecció Implícita

- **Definició**: Es basa en l'observació passiva de les interaccions de l'usuari sense que aquest hagi de fer un esforç addicional.

- **Impacte**: És un mètode simple i gens intrusiu que evita el biaix de polarització, tot i que no permet una personalització tan fina com l'explícita.

>[!Example] Exemple
> Registre d'ítems consultats, anàlisi del temps de permanència en cada consulta o estudi de la xarxa social de l'usuari. 
> **Exemple**: Anotar automàticament quins articles ha llegit un usuari en un blog.



## Mètriques d'avaluació

La qualitat d'un sistèma s'ha de poder representar.
Aquestes mètriques NO S'UTILITZEN EN L'ENTRENAMENT

**Mètrica de precisió de la predicció:**
La mètrica més usada és _l'error absolut mig_,
 - la diferència absoluta mitja entre les avaluacions predites i les reals:

$$
MAE = \frac{ \sum_{i,j} |u'(i,j) - u(i,j)|}{N}
$$

---

# Recomanador 2

## Funció de Pèrdua

Valor a pagar per la inexactitud de les prediccions



## Classificació
En machine learning, la classificació és:
-  classificar ítems en 2 o més classes

Per això entrenem models pq el output sigui un vector de de classificació amb valors per classes.
- Els interpretem passant-los a probabilitat

### Softmax
Passa Puntuacións a probabilitats
- Té millor comportament si desrpés s'utilitza el descens del gradient estocàstic

### Cross-Entropy
Serveix per mesurar què tant bona és la predicció del model respecte unes etiquetes

#### Binaria
Donat uns valors i dues classes dona dos probabilitats per cada´

#### Multiclasse



## Factorització de Matrius

A nosaltres les característiques per se dels usuaris i dels ìtmes ens donen igual,
Nosaltres volem aquells factors latents que els relacionen

A part, les matrius són esencialment matrius buides, ja que la majoria d'usuaris no té tot el cataleg puntuat:

Això ens és especialment útil amb feedback implicit, ja que és menys evident les relacions

![[Pasted image 20260125124424.png]]


Fem una matriu $R$ en base $U$ 
En aquesta matriu:
- Rows: Força de les associacions entre user i característica
- Col : Força entre ítem i característica


## Màquines de factorització

Les **Factorization Machines (FM)** es presenten com una evolució necessària per superar les limitacions dels models de Factorització de Matrius (MF) convencionals. Com a marc de treball general, la seva funció principal és:

## UItilitats

- **Generalització de Factors Latents**: Estenen l'enfocament de factors latents per permetre la integració de qualsevol **característica auxiliar** arbitrària que descrigui millor usuaris i ítems.

- **Optimització del Rànquing**: Implementen funcions de pèrdua especialitzades que optimitzen directament l'**ordre de preferència** (rank-order) dels productes.

- **Aprofitament del Feedback Implícit**: Estan especialment dissenyades per treballar amb dades d'interacció indirecta (com clics o temps de visualització), resolent el problema de la falta de valoracions explícites.


---

### Per què són superiors a la MF?

Mentre que la MF clàssica es limita a la interacció directa entre usuaris i ítems dins d'una matriu, les FM poden processar informació de context (com l'hora, el dispositiu o metadades de l'ítem) de manera eficient, oferint una recomanació molt més rica i precisa.

![[Pasted image 20260125125042.png]]

### Explicació Pràctica