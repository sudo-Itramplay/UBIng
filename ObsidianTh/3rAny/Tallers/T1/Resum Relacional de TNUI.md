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