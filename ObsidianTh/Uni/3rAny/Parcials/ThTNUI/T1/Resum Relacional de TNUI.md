
### Tags: #Resum #IA #Recomanadors #Optimització #Modelització

# Síntesi: Del Coneixement a la Recomanació Personalitzada

El nostre objectiu en l'anàlisi de dades és anar de la [[Dades|dada]] fins al [[Coneixement]]. Aquest procés d'[[Inferir]] es recolza en [[Algorisme|algorismes]] que transformen registres bruts en accions o decisions.

## 1. Fonaments: Dades, Algorismes i Models

Tot comença amb les [[Dades/Dades|Dades]], que són simples registres del món. Quan les dotem de context, es converteixen en [[Informació]]. El veritable salt es produeix quan un [[Algorisme amb Context]] analitza aquesta informació per generar [[Coneixement]], és a dir, la capacitat de prendre decisions.

Un [[Algorisme]] és un conjunt de passes per resoldre un problema. En l'aprenentatge automàtic, l'objectiu de molts d'aquests algorismes és convertir una matriu de dades en un [[Model]].

> [!tip] Algorisme vs. Model
> 
> L'[[Algorismes de predicció|algorisme de predicció]] és el procediment que aprèn de les dades (la recepta), mentre que el [[Model]] és el resultat d'aquest aprenentatge, llest per a ser utilitzat (el plat cuinat).

## 2. El Procés d'Aprenentatge: L'Optimització

Com aprenem el millor [[Model]]? A través de l'[[Optimització/Optimització|Optimització]]. Aquest procés busca ajustar els paràmetres del model per minimitzar una [[Funció de Pèrdua]], que mesura l'error entre les prediccions i la realitat.

La metodologia més comuna és el [[Descens del gradient]], un [[Algorisme d'optimització]] iteratiu que ajusta els paràmetres en la direcció oposada al [[Gradient]] (la direcció de màxim error). Per a grans volums de dades, es fa servir la seva variant [[Algorisme Descens del gradient Estocastic|SGD]], que aproxima el gradient amb mostres petites de dades, fent el procés molt més ràpid.

> [!warning] El Risc de l'Optimització
> 
> Un [[Algorisme d'optimització]] massa agressiu pot portar a l'[[Overfitting]]: un model que funciona perfectament amb les dades d'entrenament ([[Grup de Prova]]) però falla estrepitosament amb dades noves ([[Grup de Test]]).

## 3. Aplicació Avançada: Sistemes Recomanadors

Un [[Recomanador/Recomanador|Recomanador]] és un exemple perfecte d'[[Algorisme amb Context]]. El seu objectiu és predir la utilitat d'un ítem per a un usuari, definida per una [[Funció d'utilitat]] $u: C \times S \to \mathbb{R}$, on $C$ és el conjunt d'usuaris i $S$ el d'ítems. El gran repte és que aquesta funció és desconeguda i l'hem d'[[Inferir]] a partir d'una mostra molt petita de valoracions.

### 3.1. Enfocaments Basats en Semblança (Filtres Col·laboratius)

Els mètodes de [[Recomanacions colaboratives]] es basen en la [[Semblança en Recomanadors|semblança]] entre usuaris o ítems.

- **[[Recomanacions colaboratives basats en semblança d'usuari|Basats en Usuari]]**: Recomanem a un usuari allò que ha agradat a usuaris similars. La similitud es calcula comparant els vectors de valoracions a l'[[Espai de Preferències]].
    
- **[[Recomanacions colaboratives basats en semblança d'ítem|Basats en Ítem]]**: Recomanem ítems similars als que ja han agradat a l'usuari. Aquest mètode és més estable, ja que les relacions entre ítems canvien més lentament que els gustos dels usuaris.
    

> [!info] Com mesurem la semblança?
> 
> La mètrica depèn de si les dades estan [[Calibració|calibrades]] o no.
> 
> - Per a dades calibrades (ex: distància, temps), fem servir la [[Distància Euclidiana]].
>     
> - Per a opinions subjectives (no calibrades), la [[Correlació de Pearson]] és superior, ja que és insensible a la tendència de cada persona a puntuar més alt o més baix.
>     

### 3.2. Models Latents: Factorització de Matrius (MF)

Un enfocament més potent és la [[Factoritzar les matrius|Factorització de Matrius (MF)]]. La idea és que les preferències dels usuaris estan guiades per un nombre petit de factors latents o [[Features]] (ex: gèneres, actors, estils).

- Descomponem la matriu d'utilitat $R$ en dues matrius més petites, $P$ (preferències dels usuaris per aquests factors) i $Q$ (presència d'aquests factors en els ítems), tal que $P \times Q^T \approx R$.
    
- Aquest problema és, de nou, un problema d'[[Optimització/Optimització|optimització]]: trobar $P$ i $Q$ que minimitzin l'error entre les valoracions reals i les predites pel producte $P \times Q^T$.
    

### 3.3. Més Enllà de MF: Les Màquines de Factorització (FM)

La MF clàssica té limitacions: no gestiona bé el feedback implícit (clics, compres) i optimitza la predicció de valors, quan l'objectiu real és crear un bon **rànquing**.

Les [[Màquines de Factorització|Màquines de Factorització (FM)]] superen aquests problemes:

1. **Generalitzen la MF**: Poden incorporar qualsevol tipus de característica addicional (context, atributs d'usuari/ítem).
    
2. **Modelen Interaccions**: La seva fórmula $ŷ(x) = w_0 + \sum w_i x_i + \sum \sum W_{ij} x_i x_j$ captura no només l'efecte de cada característica individual sinó també el de les seves interaccions.
    
3. **Són Eficients**: Per evitar el cost computacional de la matriu d'interaccions $W$, [[La Factorització de les FM|factoritzen]] aquest terme ($W_{ij} \approx v_i^T v_j$), reduint la complexitat de $O(d^2)$ a $O(d \cdot k)$.
    

### 3.4. Optimitzant per al Rànquing: BPR

Per entrenar les FM amb l'objectiu correcte, canviem la [[Funció de Pèrdua]]. En lloc de minimitzar l'error de predicció, aprenem a ordenar directament.

- Fem servir el [[Bayesian Personalized Ranking|Bayesian Personalized Ranking (BPR)]], una funció de pèrdua que treballa amb triplets de dades: $(usuari, ítem\_vist, ítem\_no\_vist)$.
    
- L'objectiu és que la puntuació predita per a l'ítem vist ($\hat{y}_{ui}$) sigui sempre més alta que la de l'ítem no vist ($\hat{y}_{uj}$). La funció $\sum - \ln \sigma(\hat{y}_{ui} - \hat{y}_{uj})$ s'encarrega d'això.
    

Finalment, tot aquest procés es pot veure també com un problema de [[Classificació]], on per a cada usuari volem classificar els ítems en "recomanables" o "no recomanables". Per a això, funcions com [[Softmax]] (per convertir puntuacions en probabilitats) i funcions de pèrdua com [[Cross-Entropy]] són eines fonamentals.


## 4. Detalls Addicionals sobre Recomanadors

- **Recollida de Dades**: La [[Funció d'utilitat]] es construeix a partir d'una mostra de dades. Aquesta [[Recolecció de Dades]] pot seguir dues estratègies:
    
    - **[[Recolecció Explícita]]**: Demanar activament a l'usuari que doni la seva opinió (ex: puntuacions amb estrelles). El principal inconvenient és el [[Problema Polarització|problema de la polarització]], ja que les dades poden estar esbiaixades.
    
    - **[[Recolecció Implícita]]**: Inferir la preferència a partir del comportament de l'usuari (clics, compres, temps de visualització).
    
- **Tipus de Recomanadors**: A més dels mètodes col·laboratius (basats en usuari o ítem), existeixen:
    
    - **[[Recomanacions NO colaboratives]]**: Basades purament en el contingut. Es recomanen ítems amb característiques similars als que ja han agradat a l'usuari (ex: llibres de la mateixa temàtica).
    
    - **[[Recomanacions amb model Hibrid]]**: Combinen estratègies col·laboratives i no col·laboratives.
    
- **Avaluació**: Per mesurar la precisió de les prediccions d'un recomanador, una mètrica habitual és l'**Error Absolut Mig (MAE)**, que calcula la diferència absoluta mitjana entre les valoracions reals i les predites.


## 5. Un Nou Enfocament: Regles d'Associació

Un enfocament diferent per trobar patrons és el [[Problema dels ítems Freqüents]], sovint exemplificat amb el problema de la cistella de la compra.

1. **Plantejament**: Es defineix un llindar de **suport** (un nombre mínim de bosses) i es busquen tots els subconjunts d'ítems que apareixen junts superant aquest llindar.

2. **[[Generació de regles d'associació]]**: A partir d'aquests conjunts freqüents, es generen regles d'associació amb format `If-Then` (Si A, llavors B).

3. **[[Confiança]]**: La "força" d'una regla es mesura amb la confiança, que és la probabilitat condicional $p(B | A)$.

4. **[[Interès]]**:

> [!bug] Problema
> No totes les regles amb confiança alta són interessants. Per exemple, $X \to Llet$ pot tenir una confiança alta simplement perquè molta gent compra llet, independentment de X.


>[!done] **Solució**: 
>Es calcula l'**[[Interès]]** de la regla, definit com $I = p(B | A) - p(B)$. Un interès alt (molt positiu o molt negatiu) indica una correlació real i, per tant, una regla valuosa.
   

## 7. Validació i Incertesa (PPT6)

Finalment, cal recordar que qualsevol conclusió extreta de les dades ha de ser validada. L'estadística freqüentista proporciona eines per validar hipòtesis, però sempre s'ha d'assumir un cert grau d'incertesa en els resultats.

---

# ANOTACIONS Pilars Matemàtics Fonamentals (Ampliació de les Anotacions)

L'anàlisi del fitxer `T1/Anotacions/Anàlisi Profund de la Matemàtica en IA.md` revela que tot aquest procés es recolza en tres pilars matemàtics interconnectats:

1. **Àlgebra Lineal**: És el **llenguatge de la representació**. Les dades i els pesos s'emmagatzemen com a vectors, matrius i tensors. La sortida bàsica d'una neurona és un **Producte Escalar** (Dot Product) entre el vector d'entrades i el de pesos, que mesura com d'alineats estan.
    
2. **Càlcul Diferencial**: És el **motor de l'aprenentatge**. L'aprenentatge és un problema d'optimització que es resol amb el [[Optimització/Descens del gradient|Descens de Gradient]] per trobar el mínim de la [[Funció de Pèrdua]].
    
3. **Probabilitat i Estadística**: És el **marc per a la incertesa**. Permet mesurar el rendiment i la confiança, sovint transformant les sortides en probabilitats mitjançant [[Softmax]].
    

### 4.1. Refinant l'Optimització

- El càlcul del [[Gradient]] en xarxes amb múltiples capes es realitza de manera eficient gràcies a l'algorisme de **Backpropagation**, que és una aplicació intel·ligent de la **Regla de la Cadena** del càlcul.
    
- Per prevenir l'[[Overfitting]], s'afegeixen termes de **Regularització** (com les **Normes L1 i L2**) a la [[Funció de Pèrdua]], que penalitzen els models amb pesos massa grans.
    
- Moltes funcions de pèrdua, incloent la [[Cross-Entropy]], són una conseqüència directa del principi d'**Estimació de Màxima Versemblança (MLE)**, que busca els paràmetres del model que fan que les dades observades siguin el més probables possible.
    
- Encara que el [[Optimització/Descens del gradient|Descens de Gradient]] és fonamental per a funcions contínues [[Optimització Unimodal|unimodals]], existeixen altres enfocaments:
    
    - **[[Optimització discreta]]**: Per a valors enters, s'utilitzen algorismes específics com l'algorisme [[Simplex]].
        
    - **[[Algorisme d'optimització directe|Optimització directa]]**: Quan la funció és difícil o impossible de derivar analíticament, s'usen mètodes com l'[[Algorisme Nelder-Mead]], que opera modificant iterativament una forma geomètrica (un [[Simplex]]) per convergir cap al mínim.