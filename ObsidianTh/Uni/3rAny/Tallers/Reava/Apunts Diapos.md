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

## Explicació Pràctica

### 1. La Intuïció: Característiques Latents

Abans de parlar de matrius, hem d'entendre **què estem buscant**. A la teva pràctica, has calculat similituds basant-te directament en les votacions (Euclidiana). 

Però, per què un usuari vota alt una pel·lícula?
	La teoria de la Factorització de Matrius (MF) ens diu que hi ha **factors ocults** (latents) que determinen aquestes notes.

- **Exemple:** A l'usuari $U_1$ li agraden les pel·lícules d'acció. La pel·lícula $I_1$ té molta acció. Per tant, la nota serà alta.
    
- **El repte:** No tenim una columna que digui "Acció". Hem de _descobrir_ aquests factors automàticament a partir de les dades.
    

---

### 2. Descomposició de Matrius ($R \approx P \times Q^T$)

Aquesta és la base matemàtica dels recomanadors moderns (abans d'entrar en _Factorization Machines_).

#### La Matriu $R$ (La teva `df_counts`)

La matriu $R$ és la matriu d'interaccions Usuari-Ítem.

- A la teva pràctica, a l'**Exercici C**, has creat exactament aquesta matriu amb la funció `build_counts_table`.

- És una matriu de mida $|U| \times |D|$ (Usuaris $\times$ Items).

- **Problema:** És molt **dispersa** (_sparse_). La majoria de valors són `NaN` (buits) perquè cap usuari ha vist totes les pel·lícules.


#### Les Matrius $P$ i $Q$

L'objectiu és trobar dues matrius més petites, $P$ i $Q$, que quan es multipliquin, **omplin els forats** de $R$.

1. **Matriu $P$ (Usuaris):** De mida $|U| \times K$.
    
    - Cada fila representa un usuari.
        
    - Les $K$ columnes són els **factors latents** (ex: quant li agrada l'acció, el drama, etc.).
        
2. **Matriu $Q$ (Ítems):** De mida $|D| \times K$.
    
    - Cada fila representa una pel·lícula.
        
    - Les $K$ columnes són els mateixos factors latents, però aplicats a la pel·lícula (ex: quanta acció té, quant drama té...).
        

>[!example] Anotació
>Aquestes dues matrius, a la pràctica no s'han fet, és aproximació teorica



#### La Predicció

Per saber quina nota posaria l'usuari $u$ a la pel·lícula $i$, fem el **producte escalar** dels seus vectors de factors latents:

$$\hat{r}_{ui} = p_u \cdot q_i^T = \sum_{k=1}^{K} p_{uk} q_{ik}$$

> **En resum:** Estem comprimint la informació gegant i buida de la teva `df_counts` en dues taules compactes i denses que capturen l'essència (gustos i característiques).

---

### 3. Factorization Machines (FM): L'Evolució

La descomposició de matrius (MF) té un límit: només entén d'Usuaris i Ítems. Però, i si volem afegir **context** (hora del dia, dispositiu, edat, gènere)? 
	Aquí entren les **Factorization Machines.**

#### El problema de la regressió clàssica

Si volguéssim capturar la relació entre totes les variables (Usuari, Ítem, Context), necessitaríem una matriu de pesos $W$ gegantina ($O(d^2)$) per guardar el pes de cada parella possible. Això és incomputable i necessita massa memòria.

#### La Solució de les FM

Les FM utilitzen un truc: **Params d'interacció factoritzats**. En lloc de calcular un pes fix $W_{ij}$ per a la interacció entre la característica $i$ i la $j$, assignen a cada característica un vector latent $v$. La interacció es calcula com el producte escalar d'aquests vectors:

$$\hat{y}(x) = w_0 + \sum w_i x_i + \sum \sum (v_i \cdot v_j) x_i x_j$$

- **Avantatge:** Redueix dràsticament el nombre de paràmetres a estimar (de $O(d^2)$ a lineal respecte a $K$).
    
- **Connexió amb MF:** Si utilitzem FM només amb les dades d'Usuari ID i Movie ID (codificats en _one-hot_), el model és matemàticament idèntic a la Matrix Factorization.
    

---

### 4. Com triem la matriu R? (Teoria vs Pràctica)

A la teva pràctica has construït $R$ intuïtivament, però la teoria del PDF ens dona dues opcions segons el tipus de feedback:

#### A. Feedback Explícit (El que has fet)

- **Dades:** Votacions directes (estrelles de l'1 al 5).
    
- **La teva R:** A l'Exercici C (`Practica22025.ipynb`), la teva `df_counts` té valors reals (1.0, 5.0, etc.) i `NaN` on no hi ha informació.
    
- **Objectiu:** Predir els valors que falten minimitzant l'error (MSE) entre la predicció i la nota real.
    

#### B. Feedback Implícit (El que explica el PDF)

- **Dades:** Clics, visualitzacions, compres (_clicks, views, purchases_).
    
- **Problema:** No tenim "no m'agrada" (0 estrelles). Només sabem el que l'usuari HA vist. No sabem si el que NO ha vist és perquè no li agrada o perquè no ho coneix.
    
- **La nova R:** En lloc de fer regressió sobre notes, s'utilitza per a **rànquing** (ordenar productes).
    
- **Optimització:** S'utilitzen tècniques com **BPR (Bayesian Personalized Ranking)**, on l'objectiu no és encertar un número, sinó assegurar que els ítems vistos tinguin una puntuació més alta que els no vistos ($\hat{y}_{vist} > \hat{y}_{no\_vist}$).
    

### Resum Executiu

A la teva pràctica **has creat la matriu $R$** directament a partir de les dades. En canvi, **no has creat les matrius $P$ i $Q$**.

El motiu és que el teu codi implementa un **Recomanador Basat en Memòria** (veïns propers), que treballa directament amb $R$ i una matriu de similituds. Les matrius $P$ i $Q$ pertanyen als **Recomanadors Basats en Models** (Factorització de Matrius), que és la teoria explicada al PDF però no l'algoritme que has programat.

---

### 1. La Creació de $R$ (La Matriu d'Interaccions)

Segons la teoria (Pàgina 13 del PDF ), $R$ és la matriu de mida $|U| \times |D|$ que conté totes les puntuacions (ratings) que els usuaris han donat als ítems.

#### Quan i Com l'has creat al codi?

Has creat $R$ a l'**Exercici C**, dins de la funció `build_counts_table`.

1. **Origen:** Tens un DataFrame `data` (fruit del `merge` de ratings, users i movies) on cada fila és una interacció individual: _L'usuari X ha puntuat la peli Y amb un 5_.
    
2. **Transformació:** Utilitzes la funció `pivot_table` de Pandas. Aquesta funció agafa les files individuals i les "pivota" per crear una graella.
    
    - **Índex (Files):** `user_id` (Cada fila és un Usuari, $U$).
        
    - **Columnes:** `movie_id` (Cada columna és una Pel·lícula, $D$).
        
    - **Valors:** `rating` (El contingut de la cel·la $r_{ui}$).
        

**El teu codi:**

```python
# Això és exactament la creació de la matriu R
df_counts = data.pivot_table(index='user_id', columns='movie_id', values='rating', dropna=True, sort=True)
```

**Pas previ clau:** Abans de fer això fiable per a operacions matricials (Exercici D), vas aplicar `reset_id_index`. Això va transformar els IDs reals (ex: 1, 50, 6040) en índexs matricials consecutius (0, 1, 2... 6039), assegurant que la matriu $R$ no tingués forats als índexs.

---

### 2. I les matrius $P$ i $Q$?

A la teoria (Pàgina 13 del PDF ), l'objectiu de la Factorització de Matrius és trobar dues matrius petites ($P$ i $Q$) que, multiplicades, aproximin $R$:

$$R \approx P \times Q^T$$

- **$P$ (User Factors):** Representa els gustos dels usuaris (mida $|U| \times K$).
    
- **$Q$ (Item Factors):** Representa les característiques de les pel·lícules (mida $|D| \times K$).
    

#### Per què NO les tens al codi?

A la pràctica, **no has factoritzat la matriu**. En lloc de descompondre $R$ en $P$ i $Q$ (que requeriria un algoritme iteratiu com Gradient Descent, explicat a la pàgina 16 del PDF ), has optat per un camí diferent:

1. Has agafat $R$ (`df_counts`).
    
2. Has calculat una **Matriu de Similitud** (`similarity_matrix`, Exercici F.1). Aquesta matriu ($|U| \times |U|$) diu quan s'assembla l'usuari A a l'usuari B basant-se en les seves files a $R$.
    
3. Has fet prediccions fent una **mitjana ponderada** dels veïns (`weighted_average`, Exercici F.2).
    

### 3. Esquema Comparatiu: Teoria vs. La teva Pràctica

Perquè ho vegis clar, aquí tens la diferència estructural:

|**Pas**|**Mètode Teòric (Matrix Factorization)**|**El teu Mètode (User-Based Collaborative Filtering)**|
|---|---|---|
|**Entrada**|Dades crues (`ratings.dat`)|Dades crues (`ratings.dat`)|
|**Pas 1**|Construir $R$ (o iterar sobre les dades)|**Construir $R$ (`df_counts`)** ✅ _Fet_|
|**Pas 2**|**Crear $P$ i $Q$** (inicialitzats a l'atzar)|Calcular **Similitud entre Usuaris** (Euclidiana)|
|**Pas 3**|Ajustar $P$ i $Q$ per minimitzar l'error (Gradient Descent)|Seleccionar els $m$ usuaris més semblants|
|**Predicció**|Multiplicar $P_{u} \times Q_{i}^T$|Mitjana de les notes dels veïns semblants|

### Conclusió per a l'avaluació
- **"Com has creat R?"**: L'he creada pivotant el dataframe de logs (`data`) per tenir usuaris a les files i pel·lícules a les columnes (`df_counts`).
    
- **"On són P i Q?"**: En aquesta pràctica **no les he calculat**. He utilitzat un algorisme _Memory-Based_ (KNN) que treballa directament comparant les files de $R$, sense necessitat de reduir la dimensionalitat en factors latents ($P$ i $Q$) com faria un algorisme _Model-Based_.

## Perquè és un Model Lineal?
Aquí fem referència també a la eficiencia:
### 1. L'Equació del Model

L'equació d'una FM de grau 2 és:

$$\hat{y}(x) = \underbrace{w_{0} + \sum_{i=1}^{d}w_{i}x_{i}}_{\text{PART LINEAL}} + \underbrace{\sum_{i=1}^{d}\sum_{j=i+1}^{d} \langle v_i, v_j \rangle x_{i}x_{j}}_{\text{PART D'INTERACCIONS (FACTORITZADA)}}$$

On:

- $x$ és el vector de característiques (usuaris, ítems, context, etc.).

- $w_0$ és el biaix global.

- $w_i$ són els pesos de cada característica individual.

- $\langle v_i, v_j \rangle$ és el producte escalar dels vectors latents que modelen la interacció entre la característica $i$ i la $j$.

### 2. Per què diem que té un comportament "Lineal"?

Encara que captura interaccions complexes (no lineals respecte a les variables originals), FM es considera sovint dins la família de models lineals generalitzats per dos motius clau:

- **La base és lineal:** Si eliminem el segon terme (les interaccions), el model és exactament una **Regressió Lineal** tradicional ($w_0 + w \cdot x$). Això vol dir que FM aprèn el pes de cada característica per separat (com un model lineal) a més de les seves combinacions.


- **Complexitat Computacional Lineal ($O(n)$):** Aquesta és la clau de la seva eficiència. Un model polinòmic estàndard (que el PDF anomena "quadratic linear model" ) necessitaria calcular un pes independent $W_{ij}$ per a cada parella, la qual cosa té una complexitat quadràtica $O(d^2)$ i és inassumible amb moltes dades.

En canvi, gràcies al truc de la factorització ($W_{ij} \approx v_i \cdot v_j$), les FM poden calcular la part de les interaccions en **temps lineal** respecte al nombre de característiques ($O(k \cdot d)$).
  
>[!example]  **En resum:** 
>FM té la capacitat expressiva de capturar interaccions (com un nucli polinòmic) però manté l'eficiència i velocitat d'entrenament i predicció d'un model lineal.


### Com fer Que FM funcioni bé amb feedback implicit:

#### 1. Factorització de Matrius (MF): 

Problemes amb el feedback implícit La formulació estàndard de la MF no funciona bé amb aquest tipus de dades.

- **El problema:** La MF està dissenyada originalment per a valoracions explícites (estrelles, puntuacions). Amb el feedback implícit (clics, pàgines vistes, compres), no observem directament valoracions negatives, només inferències de comportament.

- **L'enfocament ingenu:** Si s'intenta adaptar la MF etiquetant totes les interaccions observades com a "1" i les no observades com a "0", es produeix un **desequilibri de classes sever**. Atès que la majoria d'interaccions són no observades, això requeriria crear milers de milions d'exemples d'entrenament "negatius", fent el procés computacionalment inviable.

- **Conclusió:** La formulació clàssica de MF "es trenca" o falla quan es tracta amb dades de feedback implícit.

#### 2. Màquines de Factorització (FM): 
Les FM es presenten com una solució per superar les limitacions de la MF, ja que permeten incorporar característiques auxiliars (atributs d'usuari, context, etc.).

- **Flexibilitat:** A diferència de la MF, les FM poden treballar amb vectors binaris que representen usuaris i ítems, i augmentar-los amb dades contextuals.

- **El repte compartit:** Tot i ser més potents, adaptar les FM directament al feedback implícit utilitzant funcions de pèrdua de classificació estàndard (marcant interaccions no observades com a 0) presenta els mateixos problemes de desequilibri i cost computacional que la MF.

#### Solució - Optimitzar el Ranking (BPR)

Perquè tant les MF com les FM funcionin bé amb feedback implícit, cal canviar l'objectiu: 
	en lloc d'intentar predir una puntuació o classificar l'error, s'ha d'aprendre l'**ordre relatiu (ranking)** dels ítems.

La tècnica clau descrita als apunts per aconseguir-ho és el **Bayesian Personalized Ranking (BPR)**:

- **Funcionament:** En lloc de mirar un sol ítem, el BPR entrena el model utilitzant **parelles d'ítems** $(i, j)$ per a un usuari $u$. Assumeix que l'usuari prefereix un ítem observat ($i$) per sobre d'un ítem no observat ($j$).

- **Resultat:** Això permet optimitzar directament l'ordenació dels ítems sense haver de generar milions de mostres negatives explícites, solucionant el problema del feedback implícit tant per a MF com, especialment, per a la formulació més avançada de les FM.

En resum, les **FM són superiors** perquè permeten incorporar més informació (context), però per gestionar el feedback implícit correctament, cal utilitzar una funció de pèrdua basada en el ranking com el **BPR**.


# Recomanadors per Session

Això és més que res anecdòtic. 
Hi ha webs que fan ús de recomanadors per sessió, ja que es considera igual d'important que els demés.
Solen jugar únicament amb el que veus en una única sessió i es restableix cada cop que es torna a la app

---

# Items frequents

## Possible EXC
Regles d'Associació.
## 1. Conceptes Clau i Fórmules

L'objectiu és trobar patrons freqüents en una base de dades de "bosses" (transaccions, documents, pacients).

### A. Definició de la Regla

Una regla té la forma $X \to Y$ (Exemple: $\{m, b\} \to c$).

- **Antecedent ($X$):** La part esquerra (condició).
    
- **Conseqüent ($Y$):** La part dreta (resultat).
    

### B. Les 3 Mètriques Sagrades

Per aprovar, has de saber calcular i distingir aquestes tres:

|**Mètrica**|**Fórmula**|**Significat**|
|---|---|---|
|**Suport ($s$)**|$\frac{\text{Nº bosses amb } X \cup Y}{\text{Nº Total Bosses}}$|Freqüència bruta. Com de comú és la combinació?|
|**Confiança ($C$)**|$\frac{\sigma(X \cup Y)}{\sigma(X)}$|Probabilitat condicional ($P(Y \mid X)$). Si tinc $X$, amb quina seguretat tinc $Y$?|
|**Interès ($I$)**|$\text{Confiança} - P(Y)$|Correlació real. Elimina l'efecte de la popularitat de $Y$.|

> [!WARNING] Atenció a l'examen
> 
> Un suport o confiança alts **no** garanteixen que la regla sigui útil. Podria ser una coincidència perquè $Y$ és molt popular. Per això calculem l'**Interès**.

---

## 2. Exemple de Càlcul d'Examen (Pas a Pas)

**Dades:** 8 Bosses totals ($N=8$).

**Regla a avaluar:** $\{m, b\} \to c$ ("Si tenim m i b, tindrem c?")

### Pas 1: Calcular Suport de l'Antecedent ($m, b$)

Busquem bosses que tinguin $m$ **i** $b$ alhora.

- Trobades a: B1, B3, B5, B6.
    
- $\sigma(m, b) = 4$
    

### Pas 2: Calcular Suport de la Unió ($m, b, c$)

De les anteriors, quantes tenen també $c$?

- Trobades a: B1, B6.
    
- $\sigma(m, b, c) = 2$
    

### Pas 3: Calcular la Confiança

$$C = \frac{\text{Suport Unió}}{\text{Suport Antecedent}} = \frac{2}{4} = 0.5 \quad (50\%)$$

### Pas 4: Calcular l'Interès

Primer necessitem la probabilitat base del conseqüent ($c$).

- $c$ apareix a: B1, B4, B6, B7, B8 (5 bosses).
    
- $P(c) = 5/8 = 0.625$
    

Ara restem:

$$I = \text{Confiança} - P(c) = 0.5 - 0.625 = -0.125$$

---

## 3. Interpretació dels Resultats

Com interpretem el número final?

- **Interès > 0 (Positiu):** **Associació útil.** La presència de $X$ fa augmentar la probabilitat de $Y$. (Ex: Bolquers $\to$ Cervesa).
    
- **Interès = 0:** **Independència.** No hi ha relació. (Ex: $X \to$ Llet, si tothom compra llet igualment).
    
- **Interès < 0 (Negatiu):** **Repulsió.** La presència de $X$ fa _menys_ probable $Y$. (Ex: Pepsi $\to$ Coke; si compres una, rarament compres l'altra).
    

_En el nostre exemple (-0.125), els ítems tenen una lleugera repulsió._

---

## 4. Aplicacions Teòriques (Per preguntes tipus test)

1. **Supermercats:** Col·locació de productes (cross-selling). _Ex: Cervesa i Bolquers._
    
2. **Plagi de Documents:** Si les "bosses" són frases i els ítems documents. Relació molts-a-molts.
    
3. **Medicina:** Detecció d'interaccions. Bosses = pacients amb efectes secundaris, Ítems = medicaments.
    


---

# Hipòtesis i Inferència 

- Suposem estadística freqüentista

## 1. A/B Testing (Triar la millor opció)

L'**A/B Testing** s'utilitza per determinar quina variant d'un element (ex: una pàgina web) funciona millor. (diferència de mitjanes)

- **Funcionament**: El trànsit s'assigna aleatòriament a cada variant (A o B) segons un pes predeterminat (ex: 50-50).
    
- **Persistència**: S'usen _cookies_ perquè l'usuari vegi sempre la mateixa versió.
    
- **Mètrica**: Es registra el temps o l'acció de l'usuari per prendre una decisió basada en dades.
    
- **Hipòtesi Nul·la ($H_0$)**: En aquest context, la posició escèptica és que el canvi de disseny **no té cap efecte**.
    

---

## 2. El Mètode del Shuffling (Validació de la Diferència)
- Complement A/B testing
Quan comparem dues mitjanes (A vs B) i no volem o no podem usar models teòrics rígids, usem el **Shuffling** (barrejar etiquetes).

- **Concepte**: Si la hipòtesi nul·la és certa, les etiquetes (A o B) no importen. Redistribuir-les no hauria de canviar la diferència entre mitjanes.
    
- **Procediment**:
    
    1. Es barregen (_shuffling_) les etiquetes de totes les mostres.
        
    2. Es recalculen les mitjanes i la seva diferència.
        
    3. Es repeteix el procés milers de vegades per construir la **distribució mostral** de la diferència.
        
- **Decisió**: Es compta quantes vegades surt una diferència més gran que l'observada originalment. Si aquesta probabilitat ($p\text{-value}$) és baixa (normalment $< 0.05$ o $5\%$), rebutgem la casualitat.
    

---

## 3. Bootstrapping (Mesurar la incertesa)

El **Bootstrapping** s'utilitza per crear una aproximació robusta de la distribució d'un paràmetre (com la mitjana o un quantil) quan no tenim un model generador de dades.

- **Tècnica Clau**: Es basa en el **mostreig aleatori amb reemplaçament**.
    
- **Procediment**:
    
    1. Tenim una mostra de $N$ elements.
        
    2. Seleccionem $N$ elements a l'atzar d'aquesta mostra, permetent que alguns es repeteixin i altres no surtin.
        
    3. Calculem l'estadístic d'interès (ex: la mitjana) per a aquesta nova "mostra bootstrap".
        
    4. Repetim milers de vegades per veure com varia el resultat.
        
- **Utilitat**: Permet calcular l'**error estàndard** i la incertesa d'estimacions complexes, com en la regressió lineal.
    

---

>[!info] 💡 Resum per a l'examen:
> - **A/B Testing**: El marc experimental per comparar variants. 
> - **Shuffling**: Tècnica per validar si la diferència entre dos grups (A i B) és real o casualitat. 
> - **Bootstrapping**: Tècnica per estimar la incertesa d'un paràmetre usant només les dades que ja tenim.

---

# Exploració Explotació

Fer simplement un mostreig, mitjana, i explotació infinita és molt porbable que ens quedem amb valors sub-optims, per això fem servir les seguents funcions, ja que en el temps donen millor resultts

## 1. La Teoria del Softmax

El mètode **Softmax** és una estratègia per convertir puntuacions numèriques (scores) en distribucions de probabilitat. En l'àmbit dels sistemes de recomanació i els _bandits_ (Tragaperras), s'utilitza principalment per balancejar l'exploració i l'explotació.

### Fonament Matemàtic

La funció Softmax transforma un vector de valors $z$ en probabilitats que sumen 1:

$$softmax(z) = \frac{e^z}{\sum_{j=0}^{K-1} e^{z_j}}$$

- **Per què no una normalització simple?** El Softmax té un millor comportament respecte al **Gradient Descendent Estocàstic (SGD)** que la normalització lineal.


### Softmax en el Problema del Bandit (tragaperra) (amb Temperatura)

En un escenari de _multi-armed bandits_, triem una acció $a$ en el moment $t$ segons la seva probabilitat, que depèn d'un paràmetre anomenat **temperatura** ($\tau$):

- **Temperatures altes ($\tau \to \infty$):** Les accions es tornen equiprobables (distribució uniforme), fomentant l'**exploració** pura.

- **Temperatures baixes ($\tau \to 0$):** El mètode es torna "voraç" (_greedy_), seleccionant gairebé sempre l'opció amb millor estimació, prioritzant l'**explotació**.

---

[[#OJO AMB NO ESTACIONARIS]]

---
## 2. UCB1 (Upper Confidence Bound)

L'algorisme **UCB1** busca una via intermèdia que variï automàticament entre exploració i explotació incorporant la **incertesa** estadísticament.

### La Regla de Decisió

Escollim l'acció $a^*$ que maximitzi la suma del valor estimat i la seva incertesa:

$$a^* = \arg \max_a (Q_t(a) + U_a)$$

### Càlcul de la Incertesa

Basat en la **cota de Hoeffding**, la incertesa ($U_a$) es calcula com:

$$U_a = \sqrt{\frac{2 \ln t}{t_a}}$$

- $t$: Nombre total de jugades fetes fins al moment.
    
- $t_a$: Nombre de vegades que hem triat l'acció $a$.
    

**Comportament:**

- Cada cop que triem $a$, $t_a$ augmenta i la incertesa **disminueix** (explotació).
    
- Quan triem altres accions, $t$ augmenta i la incertesa de $a$ **creix** logarítmicament, fent que eventualment la tornem a explorar.

---
## 3. Mostreig de Thompson (Thompson Sampling)

A diferència dels mètodes voraços que usen valors puntuals, el **Mostreig de Thompson** és un mètode **estocàstic** que modela la **incertesa** mitjançant distribucions de probabilitat.

### La Distribució Beta

Per a recompenses binàries (com _clic_ o _no clic_), s'utilitza la **distribució Beta**, definida en l'interval $[0, 1]$ per dos paràmetres: $\alpha$ (èxits) i $\beta$ (fracassos).

- **Valor mig:** Es calcula com $\frac{\alpha}{\alpha + \beta}$.

- **Inicialització:** Es comença amb $\alpha = 1, \beta = 1$, que equival a una distribució uniforme (incertesa total).


### Funcionament de l'Algorisme

A cada pas, l'algorisme segueix aquest procés:

1. **Mostreig:** Es genera un valor aleatori $v_i$ per a cada acció a partir de la seva funció Beta.

2. **Selecció:** S'executa l'acció amb el valor mostrejat més alt.

3. **Actualització:** Segons el resultat ($r$), s'actualitzen els paràmetres de l'acció triada:
    
    - Si hi ha èxit ($r=1$): $\alpha = \alpha + 1$.
    
    - Si hi ha fracàs ($r=0$): $\beta = \beta + 1$.
    

### Avantatges clau

- **Convergència:** A mesura que recollim dades, la distribució es fa més estreta, reduint naturalment l'exploració i augmentant l'explotació.

- **Retroalimentació retardada:** Supera l'algorisme UCB1 en sistemes reals on la recompensa no és immediata, ja que no és determinista i continua variant les accions fins i tot sense dades noves.


---

### Resum comparatiu per a l'examen

| **Algorisme** | **Tipus de tria** | **Punt fort**                                   |
| ------------- | ----------------- | ----------------------------------------------- |
| **Softmax**   | Probabilística    | Fàcil de tunar amb la temperatura ($\tau$).     |
| **UCB1**      | Determinista      | Molt sòlid estadísticament (cota de Hoeffding). |
| **Thompson**  | Estocàstica       | Supera UCB quan la retroalimentació es retarda. |

|**Característica**|**Softmax**|**Thompson Sampling**|
|---|---|---|
|**Naturalesa**|Probabilística basada en valor estimat.|Estocàstica basada en distribucions.|
|**Paràmetre clau**|Temperatura ($\tau$).|Paràmetres de forma ($\alpha, \beta$).|
|**Punt fort**|Simple de controlar el balanç exploració/explotació.|Gestiona molt bé la incertesa i el retard en les dades.|

### OJO AMB NO ESTACIONARIS
La resposta curta és: **no és que el Softmax sigui "pitjor" per si mateix, sinó que la seva eficàcia depèn de com gestionem les estimacions i la incertesa.**

En un escenari **no estacionari** (on la distribució de recompenses varia amb el temps), el rendiment de qualsevol algorisme canvia dràsticament. Aquí tens la comparativa tècnica segons la teoria:

---

### 1. El problema de la mitjana simple

Tots els mètodes d'acció-valor (inclòs el Softmax) fallen en problemes no estacionaris si utilitzen la **mostra promitjada** (mitjana simple).

- **Per què?** Perquè la mitjana simple dóna el mateix pes a una recompensa obtinguda fa 1.000 jugades que a una obtinguda ara mateix.
    
- **La solució:** Cal usar una **mida de pas constant** ($\alpha$). Amb aquesta formulació incremental, les recompenses més recents tenen més pes i les antigues decreixen exponencialment.
    

$$Q_{k+1} = Q_k + \alpha (r_{k+1} - Q_k)$$

---

### 2. Softmax vs. Mètodes d'Incertesa (UCB i Thompson)

Tot i que podem adaptar el Softmax amb $\alpha$, els mètodes que incorporen la **incertesa** solen ser superiors en la immensa majoria de casos.

- **Softmax (Limitació):** Explora de forma probabilística basant-se només en el valor estimat. Si una acció que era dolenta de sobte es torna bona (canvi no estacionari), el Softmax pot trigar molt a "redescobrir-la" si la seva temperatura $\tau$ és baixa.
    
- **UCB1 (Avantatge):** Incorpora la incertesa estadísticament. Si una acció no s'ha provat durant molt de temps, el seu terme d'incertesa $\sqrt{2 \ln t / t_a}$ creix, obligant l'algorisme a re-explorar-la automàticament.
    
- **Thompson Sampling (El guanyador):** És especialment eficaç en sistemes reals i quan la retroalimentació es retarda. Com que és **estocàstic** (mostreja una distribució), manté una exploració més dinàmica i adaptativa que el Softmax pur.
    

---

### 📊 Resum comparatiu en entorns no estacionaris

|**Algorisme**|**Adaptabilitat**|**Comportament davant canvis**|
|---|---|---|
|**Softmax**|Mitjana|Depèn totalment de la temperatura $\tau$ i de l'ús d'una $\alpha$ constant.|
|**UCB1**|Alta|Molt bo perquè la incertesa creix per a les accions no visitades.|
|**Thompson**|**Molt Alta**|El millor en casos complexos i amb retards en les dades.|

> [!IMPORTANT] En resum: 
> El Softmax és "pitjor" perquè és un mètode **cec a la incertesa**. Mentre que UCB i Thompson saben quina part del seu coneixement és "vell" o "incert", el Softmax només mira quina opció té millor puntuació en aquell moment.


---
# Bayes
El Teorema de Bayes és una eina fonamental per a qualsevol analista de dades, ja que permet actualitzar la nostra confiança en una hipòtesi a mesura que obtenim noves evidències.

### 1. Creences vs. Freqüències

La gran diferència entre l'estadística clàssica (freqüentista) i la bayesiana és la definició de "probabilitat":

- **Punt de vista Freqüentista:** 
	- Interpreta la probabilitat com la freqüència d'esdeveniments a llarg termini en una sèrie d'assaigs repetibles. 
	- Per a un freqüentista, no existeix la "probabilitat" que Bin Laden estigui mort: o ho està o no ho està, perquè no és un esdeveniment que puguis repetir mil vegades per veure quantes surt "mort".
    
- **Punt de vista Bayesià:** 
	- Defineix la probabilitat com el **grau de creença** o confiança que tenim en què un esdeveniment es produeixi. 
	- Això ens permet assignar un valor numèric a la nostra incertesa basant-nos en el nostre estat de coneixement actual.
    

### 2. L'exemple de Bin Laden

En el cas de Bin Laden, el bayesianisme és l'única eina que ens permet operar amb rigor:

- Com que no hi ha sèries d'assaigs idèntics, la noció clàssica de probabilitat no s'aplica.
    
- Un analista bayesià pot dir: "Amb la informació d'intel·ligència que tinc ara (evidències), la meva confiança en la hipòtesi que està mort és del 80%".
    
- Aquest estat de coneixement es **modifica** immediatament quan apareix nova informació (per exemple, un vídeo nou o una prova d'ADN).
    

### 3. La Interpretació Diacrònica (Actualització)

La utilitat fonamental de la fórmula és que ens dóna un mètode objectiu per modificar les nostres hipòtesis en funció de les dades:

> [!TIP] **L'Essència de Bayes** 
> Ens permet passar de $P(B|A)$ a $P(A|B)$. Això és útil quan és molt difícil calcular directament el que volem saber ($P(H|D)$), però és fàcil calcular com de bé la nostra hipòtesi explica les dades ($P(D|H)$).

En resum, Bayes serveix per **aprendre de l'experiència**. Cada vegada que rebem una dada nova, no llencem el que sabíem abans, sinó que ho fem servir com a "a priori" per calcular una nova "a posteriori" més precisa.

## 1. Fonaments de la Teoria Bayesiana

El Teorema de Bayes es deriva de les propietats bàsiques de la probabilitat, específicament de la probabilitat condicional i la regla de la cadena.

### Conceptes Crítics

- **Probabilitat Marginal $P(A)$:** La probabilitat que ocorri un esdeveniment independentment d'altres variables.
    
- **Probabilitat Conjunta $P(A,B)$:** La probabilitat que ocorrin $A$ i $B$ alhora.
    
- **Probabilitat Condicional $P(A|B)$:** La probabilitat que ocorri $A$ sabent que ja ha passat $B$.
    

### La Fórmula de Bayes

La forma general del teorema permet "invertir" les probabilitats condicionals:

$$P(H|D) = \frac{P(D|H)P(H)}{P(D)}$$

### Interpretació Diacrònica

>[!quote] Diacrònica
>Procés d'actualització d'una hipòtesi o creença a mesura que es disposa de nova informació al llarg del temps. Serveix per modificar de forma objectiva la probabilitat _a priori_ inicial i convertir-la en una probabilitat _a posteriori_ basada en les dades.

En l'anàlisi de dades, utilitzem una terminologia específica per descriure com canvia el nostre coneixement:

- **$P(H)$ (Priori):** El nostre grau de creença en la hipòtesi _abans_ de veure les dades.
    
- **$P(H|D)$ (Posteriori):** La probabilitat de la hipòtesi _després_ d'observar les dades.
    
- **$P(D|H)$ (Versemblança/Likelihood):** Com de bé explica la hipòtesi les dades observades.
    
- **$P(D)$:** Una constant de normalització que assegura que la suma de probabilitats sigui 1.
    

---

## 2. Exemple: El Test Mèdic

Aquest exemple és clàssic perquè demostra com la intuïció humana sovint falla davant les probabilitats baixes (prevalença).

### L'Escenari

Suposem una malaltia amb les següents dades estadístiques:

1. **Prevalença:** Només el **5%** de la població està malalta ($P(H_{sí}) = 0,05$).
    
2. **Precisió del test:** El test té una fiabilitat del **90%** tant per a positius com per a negatius ($P(E_{sí}|H_{sí}) = 0,9$ i $P(E_{no}|H_{no}) = 0,9$).
    

### El Problema

Volem saber: **Si un pacient dóna positiu ($E_{sí}$), quina és la probabilitat real que tingui la malaltia ($H_{sí}$)?**

### Càlcul

Aplicant el Teorema de Bayes i la llei de la probabilitat total per al denominador:

$$P(H_{sí}|E_{sí}) = \frac{P(E_{sí}|H_{sí})P(H_{sí})}{P(H_{sí})P(E_{sí}|H_{sí}) + P(H_{no})P(E_{sí}|H_{no})}$$

Substituint els valors:

- Numerador: $0,9 \times 0,05 = 0,045$
    
- Denominador (Probabilitat de donar positiu): $(0,9 \times 0,05) + (0,1 \times 0,95) = 0,045 + 0,095 = 0,14$
    

> [!IMPORTANT]
> 
> **Conclusió:** Tot i que el test té un 90% de precisió, si dónes positiu, la probabilitat d'estar malalt és només del **32%**. Això passa perquè la malaltia és molt rara (priori baixa) i el nombre de "falsos positius" de la gent sana (95% de la població) acaba superant els positius reals.



---
# Fully Connected (FC) vs. Convolutional Neural Networks (CNN)

Les xarxes **CNN** representen una evolució creativa de les **FC** per processar dades amb estructura espacial, com les imatges.

>[!quote] MNIST
>Nomes és un database d'imatges de números

# Fonaments d'Arquitectura Neuronal: Perceptró, Tensor i Activació

Per entendre com una **CNN** optimitza el processament d'imatges respecte a una **FC**, cal dominar aquests tres conceptes que defineixen com viatja i es transforma la informació.

## El Perceptró

El **perceptró** (també anomenat unitat o neurona artificial) és el component fonamental que processa la informació. La seva arquitectura determina com la xarxa aprèn i quina capacitat té per reconèixer patrons.

### 1. Estructura i Funcionament Matemàtic

Cada perceptró opera seguint una seqüència lògica de càlcul que transforma les dades d'entrada en una decisió o activació:

- **Entrades ($a$):** Rep els valors de la capa anterior (per exemple, la intensitat dels píxels de la imatge MNIST).
    
- **Pesos ($w$):** Cada entrada té un pes que determina la seva importància. En les CNN, aquests pesos es visualitzen com a filtres que busquen patrons concrets.
    
- **Biaix ($b$):** Un valor addicional que permet a la neurona ajustar el seu llindar d'activació independentment de les entrades.
    
- **Suma Ponderada:** El perceptró calcula la suma de totes les entrades multiplicades pels seus pesos més el biaix: $z = b + \sum_{l=0}^{4} \sum_{m=0}^{4} w_{l,m} a_{j+l,k+m}$.
    
- **Activació ($\sigma$):** El resultat de la suma es passa per una funció d'activació no lineal per determinar la sortida final de la unitat.
    

### 2. El Perceptró en FC vs. CNN: Diferències de Connectivitat

La gran diferència entre arquitectures no és el perceptró en si, sinó **com es connecta** a les dades:

#### A. Perceptró Fully Connected (FC)

- **Connectivitat Global:** Cada unitat està connectada a **tots** els elements de l'entrada.
    
- **Càrrega de Paràmetres:** En una imatge de MNIST ($28 \times 28$), un sol perceptró de la primera capa oculta ha de gestionar **784 pesos** més un biaix.
    
- **Limitació:** Ignora l'estructura espacial; si un patró es mou uns píxels, el perceptró FC no el reconeixerà com el mateix objecte.
    

#### B. Perceptró Convolucional (LRF - Local Receptive Field)

- **Connectivitat Local:** Inspirat en la neurociència, cada unitat només té una **"visió local"** de la imatge (una submatriu, normalment de $5 \times 5$ píxels).
    
- **Pesos Compartits:** Aquesta és la clau de la millora: tots els perceptrons d'un mateix mapa de característiques utilitzen els **mateixos pesos ($w$) i biaix ($b$)**.
    
- **Avantatge:** Això permet que la xarxa detecti una característica (com una aresta) en qualsevol lloc de la imatge amb un nombre mínim de paràmetres, aconseguint **invariància a la translació**.
![[Pasted image 20260125195302.png]]

L'**stride** (salt) determina quantes posicions es desplaça el filtre sobre la imatge d'entrada. Si el salt és d'1, el filtre avança píxel a píxel; si és de 2, se salta un píxel entremig.

Aquesta tècnica és útil per:

- **Reduir la dimensionalitat**: En saltar píxels, el "mapa de característiques" resultant és més petit, el que accelera el càlcul.
    
- **Eficiència de paràmetres**: Com que hi ha menys unitats a la capa de sortida, es redueix la quantitat total de pesos i biaixos necessaris.
    
- **Eliminar redundància**: En imatges naturals, els píxels veïns solen ser molt similars, per la qual cosa processar-los tots de vegades no aporta informació extra.
![[Pasted image 20260125195632.png]]

>[!WARNING]  IMPORTANT
> LRF no funcioa bé amb imatges naturals

>[!tip] Sharing LRF Weights
>Per a imatges el que fem és compartir pesos per cada pixel, en comptes de fer una convolució independent (Per exemple Sobel)
>- Convolució és multiplicar 2 matrius on s'estàn plicant 2 funcions alhora

Tot això pot fer que fem una reducció de dimensionalitat massa agressiva, per això existeix el pading

![[Pasted image 20260125200148.png]]

### Què és el Pooling?

L'objectiu principal del pooling és reduir la mida de les representacions intermèdies (els mapes de característiques) per disminuir el nombre de paràmetres i el cost computacional de la xarxa. Això també ajuda a fer que la detecció de patrons sigui més invariant a petites distorsions o canvis de posició.
#### Max Pooling

És el mètode de pooling més utilitzat en arquitectures com les destinades a **MNIST**.

- **Funcionament:** La capa divideix el mapa de característiques en regions (normalment de $2 \times 2$) i selecciona únicament el valor **màxim** de cada regió.
    
- **Lògica:** S'assumeix que el valor més alt representa la presència més forta d'una característica determinada (una aresta, un traç, etc.).
    
- **Resultat:** Redueix dràsticament la resolució. Per exemple, una sortida de $24 \times 24$ neurones es converteix en una de $12 \times 12$ després d'un max-pooling de $2 \times 2$.
    

---

#### Average Pooling

Encara que és menys comú en les primeres capes que el max-pooling, té la seva utilitat segons el tipus de dades.

- **Funcionament:** En lloc de buscar el valor màxim, calcula la **mitjana** aritmètica de tots els valors presents en la regió seleccionada.
    
- **Lògica:** Proporciona una visió més suau i global de la regió, mantenint una part de la informació de fons que el max-pooling podria descartar.
    

---
![[Pasted image 20260125200508.png]]
## ⚖️ Comparativa ràpida

|**Característica**|**Max Pooling**|**Average Pooling**|
|---|---|---|
|**Operació**|Selecciona el valor màxim.|Calcula la mitjana dels valors.|
|**Focus**|Detecta les característiques més destacades (activacions pic).|Suavitza la informació i manté el context general.|
|**Ús a MNIST**|Molt comú per detectar els traços definits dels números.|Menys habitual en aquest context específic.|

> [!NOTE] Càrrega de Paràmetres 
> És fonamental recordar que les capes de pooling **no tenen paràmetres entrenables** (no hi ha pesos ni biaixos a aprendre); només apliquen una regla fixa per reduir les dimensions de les dades.

---

## 🔄 El paper en la seqüència CNN

En una xarxa completa, el pooling actua com un pont:

1. Rep els mapes de **24x24** generats per la convolució.
    
2. Redueix la mida a **12x12**, simplificant la feina per a la següent capa.
    
3. Aquesta informació reduïda és la que finalment s'aplana (**flattening**) per entrar al classificador final.
    

Voldries que t'ajudés a calcular com quedaria una matriu de $4 \times 4$ si li apliquem un Max-Pooling de $2 \times 2$ amb un salt (stride) de 2?

### 3. Capacitat i Apilament

- **Múltiples respostes:** Per augmentar la capacitat del model, es calculen diversos perceptrons per a cada píxel (creant diversos mapes de característiques) per detectar diferents patrons simultàniament.
    
- **Jerarquia:** Quan apilem capes, els perceptrons de les capes superiors ja no miren píxels, sinó les activacions (característiques) detectades pels perceptrons de les capes inferiors, permetent una descomposició jeràrquica de la imatge.
    

## 2. El Tensor (L'Estructura de Dades)

Un tensor és un contenidor numèric multidimensional. En el reconeixement de dígits, és la forma en què la xarxa "veu" les dades:

- **Imatges com a Tensors:** Una imatge de MNIST és un tensor de $28 \times 28$ píxels. Si és en blanc i negre, és un tensor de 2D (o 3D amb 1 canal: $28 \times 28 \times 1$).
    
- **Pesos com a Tensors:** Els filtres de la CNN són tensors (ex. un filtre de $5 \times 5$). Els pesos d'una capa convolucional es visualitzen com a tensors que capturen característiques visuals.
    
- **Operació de Flattening:** És el procés de col·lapsar un tensor multidimensional en un de sola dimensió (vector) per poder entrar-lo a les capes final de classificació.
    

## 3. La Funció d'Activació (La Necessitat de la No-Linealitat)

Aquesta funció és el pas final dins de cada perceptró i és descrita com a **"estrictament necessària"** per al funcionament de la xarxa.

### Per què la necessitem?

- **No-linealitat:** Sense ella, una xarxa (per moltes capes que tingués) es comportaria com una simple operació lineal. No podria aprendre patrons complexos com les corbes o els traços d'un número manuscrit.
    
- **Decisió:** Ajuda a la xarxa a decidir quina informació és rellevant i ha de passar a la següent capa.
    

### Tipus i Diferències (Segons la teoria MNIST)

La teoria utilitza el símbol **$\sigma$** per representar aquesta funció. Tot i que n'existeixen moltes, les més habituals són:

1. **Sigmoide ($\sigma$):**
    
    - **Què fa:** Comprimeix qualsevol valor d'entrada en un rang entre 0 i 1.
        
    - **Ús:** Històricament molt utilitzada, especialment en les capes de sortida per a probabilitats.
        
2. **ReLU (Rectified Linear Unit):**
    
    - **Què fa:** Si l'entrada és negativa, la converteix en 0. Si és positiva, deixa el valor tal qual.
        
    - **Diferència:** És molt més ràpida de calcular que la sigmoide i ajuda a evitar problemes de gradient en xarxes profundes.
        
3. **Softmax:**
    
    - **Ús:** Típica de la capa final en classificació (com predir si un dígit és un 5 o un 8). Converteix les sortides en una distribució de probabilitat que suma 1.
        

---

## Connexió Conceptual

En una **CNN**, el **tensor** d'entrada és processat per **perceptrons** amb camps receptius locals que apliquen una **funció d'activació** $\sigma$. Aquesta combinació permet que la xarxa detecti característiques jeràrquiques (arestes, després formes, després números) de manera molt més eficient que una xarxa FC.


## 1. Per què la CNN és millor que la FC en imatges?

Les xarxes **Fully Connected (FC)** presenten dos problemes crítics quan escalem a imatges reals:

- **Explosió de paràmetres:** 
	- En una FC, cada neurona està connectada a **tots** els píxels de l'entrada. 
		- Per a una imatge d'1 megapixel ($10^6$), fins i tot una capa oculta petita de $1.000$ unitats requeriria $10^9$ paràmetres. 

>[!fail] Problema
>Això fa que el model sigui ineficient i requereixi conjunts de dades enormes per no sobreajustar-se.

- **Pèrdua d'estructura (Flattening):** 
	- Per entrar una imatge a una FC, primer cal fer una operació de **flattening** (aplanament), col·lapsant la matriu 2D en un vector d'una dimensió. Això destrueix la relació espacial entre píxels veïns.

>[!fail] Problema
>Això fa que els pixels perdin el context dels veins (super important)

### Com ho soluciona la CNN?

La CNN explota l'estructura de les imatges mitjançant tres conceptes:

1. **Camps Receptius Locals (LRF):** Les neurones només miren una petita subregió de la imatge ($f \times f$), anomenada camp receptiu local.
    
2. **Pesos Compartits:** Totes les unitats d'un "mapa de característiques" utilitzen exactament els mateixos pesos i biaix. Això permet la **invariància a la translació**: si un patró (com una aresta) apareix en qualsevol lloc de la imatge, el mateix filtre el detectarà.
    
3. **Pooling:** Simplifica la informació de sortida de les capes convolucionals, reduint la dimensió i mantenint les característiques més importants.

>[!info] És a dir
>Agafem cada pixel i li apliquem una convolució, permetent que mantingui context i reduim dimensionalitat

---

## 2. Teoria de Paràmetres (per a Tensorflow Playground)

Entendre el càlcul de paràmetres és clau per saber quants pesos estem entrenant realment.

### Capa Fully Connected (FC)

Cada connexió és un pes independent.

- **Fórmula:** $(\text{entrades} \times \text{unitats}) + \text{biaixos}$.
    
- _Exemple MNIST:_ Una capa FC amb 5 unitats i entrada de 784 píxels té $(784 \times 5) + 5 = 3.925$ pesos.

### Capa Convolucional (CNN)

Aquí el nombre de paràmetres no depèn de la mida de la imatge d'entrada, sinó de la mida del filtre.

- **Fórmula:** $(\text{filtre}_w \times \text{filtre}_h \times \text{canals\_entrada} \times \text{mapes\_característiques}) + \text{biaixos}$.
    
- _Exemple:_ Un filtre de $5 \times 5$ per a una imatge BN (1 canal) amb 3 mapes de característiques només té $(5 \times 5 \times 1 \times 3) + 3 = 78$ paràmetres.
    

> [!NOTE] Càlcul de dimensions de sortida 
> - Sense padding, la dimensió de sortida d'una convolució és $(n - f + 1) \times (n - f + 1)$, on $n$ és el costat de la imatge i $f$ el del filtre. 
> - El **padding** s'utilitza per evitar que la imatge s'encongeixi massa ràpidament i permetre xarxes més profundes.

---

## 3. Seqüència i Passos d'una CNN (Exemple MNIST)

Per a un examen, és vital conèixer l'ordre lògic del processament:

1. **Entrada (Input):** Imatge original (ex. $28 \times 28$ píxelsBN).
    
2. **Capa Convolucional:** S'apliquen $k$ filtres (ex. 3 mapes amb LRF de $5 \times 5$). Resultat: $3$ mapes de $24 \times 24$ (si no hi ha padding).
    
3. **Activació No Lineal:** S'aplica una funció (com ReLU) a cada activació (tot i que sovint s'omet en diagrames per simplicitat).
    
4. **Capa de Pooling (Max-Pooling):** Redueix la mida dels mapes (ex. de regions $2 \times 2$ agafa el valor màxim). Resultat: $3$ mapes de $12 \times 12$.
    
5. **Aplanament (Flattening):** Es converteixen els mapes 2D finals en un vector 1D (ex. $3 \times 12 \times 12 = 432$ unitats).
    
6. **Capa Fully Connected (Classifier):** Aquest vector s'envia a una o més capes FC per realitzar la classificació final (ex. 10 unitats per als dígits del 0 al 9).

![[Pasted image 20260125200607.png]]

L'**apilament** (stacking) d'aquestes capes permet que la xarxa aprengui una descomposició jeràrquica de la imatge, des d'arestes simples fins a formes complexes.
![[Pasted image 20260125200629.png]]

---


# GEN AI
## Entrenament de Models de Llenguatge Extens (LLM)

L'objectiu fonamental d'un model de llenguatge és actuar com un **model probabilístic autoregressiu**. Això implica que el model aprèn a calcular la probabilitat d'una seqüència de símbols (tokens) i, donada una cadena, predir el token més probable que la segueix.

### 1. Conceptes Fonamentals

Abans de l'entrenament, cal entendre com es tracten les dades:

- **Tokenització:** El text es descompon en unitats bàsiques anomenades tokens (paraules, subparaules o caràcters) mitjançant un algoritme predefinit que els converteix en nombres enters d'un vocabulari fix.
![[Pasted image 20260125201938.png]]

- **Arquitectura:** Els LLM actuals són xarxes neuronals de gran capacitat basades en l'arquitectura **Transformer**, amb bilions de paràmetres ($\theta$).
    

### 2. Fase I: Pre-entrenament (Pre-training)

En aquesta fase, el model adquireix coneixement general a partir de col·leccions massives de dades (bilions de tokens).

- **Objectiu:** Maximitzar la probabilitat que el model assigna a la paraula real de la mostra donat el seu context anterior.
    
- **Funció d'Optimització:** S'utilitza la log-versemblança: $\max_{\theta} \sum \log p_{\theta}(w_t | w_{<t})$.
    
- **Funció de Pèrdua:** Es minimitza l'**entropia creuada** (_cross-entropy loss_), que és equivalent a maximitzar la probabilitat esmentada.
    
- **Algoritme:** S'utilitza el **descens del gradient** de forma iterativa per modificar els pesos de la xarxa i reduir l'error.
    

>[!tip] Què tenim ara?
>Tenim una IA capaç d'escriure text, però no és capaç de seguir indicacions del usuari, Però falta més passos per tenir una bona base

![[Pasted image 20260125202033.png]]
### 3. Fase II: Ajustament Fí Supervisat (SFT)

El model pre-entrenat sap predir tokens, però no necessàriament seguir instruccions útils. El **Supervised Fine Tuning (SFT)** el converteix en un "model instruït".

- **Dades:** Es fan servir parelles de (instrucció/prompt, resposta ideal) creades normalment per humans.
    
- **Procés:** Es torna a entrenar el model amb aquest conjunt de dades de qualitat utilitzant la mateixa funció de pèrdua d'entropia creuada per forçar el model a imitar el format i el to desitjats.

Això crea datasets com:
![[Pasted image 20260125202145.png]]

### 4. Fase III: Aprenentatge per Reforç (RLHF)

Aquesta fase final ajusta el model a les preferències humanes complexes que són difícils de codificar en regles simples.

- Anirem fent varies respostes i intentarem anar-nos ajustant a les que més agraden

1. **Creació del Model de Recompensa (RM):** Es generen diverses respostes per a un mateix prompt i humans les classifiquen segons la seva qualitat. Una xarxa neuronal separada (RM) aprèn a predir aquestes preferències.
![[Pasted image 20260125202339.png]]


2. **Optimització de Polítiques:** S'utilitza el RM per entrenar l'LLM-SFT mitjançant algorismes com l'**Optimització de Polítiques Proximals (PPO)** o **GRPO**. L'objectiu és que l'LLM generi respostes que obtinguin la màxima puntuació del RM.
   
![[Pasted image 20260125202424.png]]
### 5. Mètodes de Generació i Mostreig (inferencia)

Un cop entrenat, per generar text s'utilitzen paràmetres que controlen l'estocasticitat (aleatorietat) del model:

- **Temperatura ($T$):** Reescala les probabilitats. Una $T > 1$ aplana la distribució (més creativitat), mentre que una $T < 1$ la fa més picada (més determinisme).
    ![[Pasted image 20260125202610.png]]
- **Top-k Sampling:** El model només tria entre els $k$ tokens més probables.
    ![[Pasted image 20260125202532.png]]
- **Top-p (Nucleus) Sampling:** Es tria el conjunt mínim de tokens que sumen una probabilitat acumulada $p$.
    ![[Pasted image 20260125202551.png]]

### 6. Xatbots
Per tenir un xatbot, i per tant un agent,  aquests tenen polítiques dins del procès.
Entre altres Està el anar guardant la conversa
![[Pasted image 20260125202844.png]]

#### Què és un agent:
Un **agent** és un sistema que utilitza un LLM com a **motor de raonament** central per completar tasques complexes mitjançant l'autonomia i l'ús d'eines externes.

A diferència d'un LLM estàndard, que només prediu el següent token, un agent té la capacitat de planificar i interactuar amb el món real.

##### 1. L'Arquitectura d'un Agent

Podem visualitzar un agent com un sistema amb quatre components principals:

- **Cervell (El LLM):** Actua com el nucli de control. Planifica els passos i decideix quines accions prendre.
    
- **Planificació (Planning):** L'agent desglossa una tasca gran en sub-tasques més petites i manejables (tècniques com _Chain of Thought_).
    
- **Memòria (Memory):**
    
    - _Memòria a curt termini:_ El context de la conversa actual.
        
    - _Memòria a llarg termini:_ L'ús de bases de dades vectorials (RAG) per recuperar informació externa.
        
- **Eines / Ús de recursos (Tool Use):** La capacitat de cridar APIs externes, consultar una base de dades SQL, fer càlculs matemàtics exactes o navegar per la web.
    

---

##### 2. El Cicle de Raonament: ReAct

La teoria destaca el patró **ReAct** (_Reason + Act_). En lloc de respondre directament, l'agent segueix un bucle iteratiu:

1. **Pensament (Thought):** El model descriu què creu que ha de fer.
    
2. **Acció (Action):** El model tria una eina (ex: `cerca_google("preu Nvidia avui")`).
    
3. **Observació (Observation):** L'agent rep el resultat de l'eina (el "feedback" del món real).
    
4. **Actualització:** L'agent torna al pas 1 fins que la tasca està completada.
    

---

##### 3. Diferències Clau

|**Característica**|**LLM Estàndard (Chatbot)**|**Agent**|
|---|---|---|
|**Objectiu**|Generar text coherent|Completar una tasca (Goal-oriented)|
|**Interacció**|Limitada al xat|Interactua amb programari extern|
|**Raonament**|Passiu (una sola passada)|Actiu i iteratiu|
|**Limitacions**|Coneixement tancat|Pot buscar dades actualitzades|

> [!TIP]
> 
> Un LLM es converteix en agent quan li passes el control d'un bucle `while`: "Mentre la tasca no estigui acabada, pensa, actua i observa".


### 6. Limitacions i Precaucions

Tot procés d'entrenament pot heretar o generar problemes que cal supervisar:

- **Al·lucinacions:** Generació de fets inventats amb aparença de veritat.
    
- **Biaixos:** El model pot perpetuar estereotips presents en les dades d'entrenament.
    
- **Sobre-estimació (_Overfitting_):** Risc de trobar un model que s'ajusti massa a les dades d'entrenament però no generalitzi bé.


 
## ✍️ Tècniques i Exemples de Prompts

El document destaca que els models responen millor quan se'ls dóna una estructura clara i context.

### Estratègies clau amb exemples:

- **Definició de Rol:** Actuar com un expert millora la qualitat.
    
    - _Exemple:_ "Actua com un professor de programació i explica’m Python amb exemples simples."
        
- **Especificitat i Format:** Evitar vagueses i demanar estructures concretes (JSON, llistes).
    
    - _Exemple:_ "Explica’m en 5 punts els avantatges del mètode bootstrap en estadística aplicada."
        
- **Raonament (Chain-of-Thought):** Demanar que el model pensi pas a pas ajuda en problemes complexos.
    
    - _Exemple:_ "Raona pas a pas i explica per què descartes opcions."
        

---

## 🧱 L'Estructura del Prompt Modular

La pràctica professional moderna divideix el prompt en 5 mòduls essencials per maximitzar la precisió:

|**Mòdul**|**Descripció**|**Exemple del PDF**|
|---|---|---|
|**Context**|Qui ets i què saps.|"Sóc estudiant de 3er d’Informàtica... no conec l’aprenentatge profund."|
|**Objectiu**|Què vols aconseguir.|"Necessito una explicació clara... per explicar-la a classe."|
|**Tasques**|Accions concretes.|"Explica què és un LLM en 6–8 frases. Inclou una analogia."|
|**Restriccions**|Què s'ha d'evitar.|"No facis servir equacions avançades. No donis info històrica."|
|**Format**|Com vols la sortida.|"Respon organitzat en 4 seccions: A, B, C i D."|
