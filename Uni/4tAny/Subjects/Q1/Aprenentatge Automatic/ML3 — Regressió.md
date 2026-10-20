---
data: 2026-10-05
assignatura: AA
parcial: 
tags:
  - tipus/teoria
  - assignatura/AA
---

# ML3 — Regressió
**Referència: ML3-2026_1.pdf (D1-65)** — Fusiona [[Classes/classe4|Classe 4]] (part estocàstica, R², SE, one-hot).

---

## Regressió Lineal

# Regressió Lineal
**Referència: Diapositives 1-21**

## Idees clau
- La **regressió lineal** és el model de referència en ML supervisat: senzill, interpretable i sovint sorprenentment efectiu.
- Assumeix **dependència lineal** entre les features ($X_1, X_2, \dots, X_p$) i el target ($Y$).
- **La funció de regressió real mai és lineal!** Encara així, la regressió lineal és extremadament útil tant conceptualment com a la pràctica.
- Serveix per veure **correlacions**, no causes: només podem dir *què* passa, no *per què*.

## Regressió Lineal Simple (una feature)

### Model
$$Y = \beta_0 + \beta_1 X + \epsilon$$

- $\beta_0$ = **intercept** (on talla l'eix Y)
- $\beta_1$ = **pendent** (efecte de X sobre Y)
- $\epsilon$ = terme d'error (allò que el model no pot fer res per capturar; com més dades tinguem, millor estimarem $\beta_0$ i $\beta_1$)

> [!note] Dit a classe ([[Classes/classe3|Classe 3]])
> - Ens quedem amb el **"model patata"** de l'apunt: $Y = \beta_0 + \beta_1 X + \epsilon$.
> - L'$\epsilon$ és **allò que el model no pot fer res**: com **més dades** tinguem, **millor estimarem** $\beta_0$ i $\beta_1$.

### Predicció
$$\hat{y} = \hat{\beta}_0 + \hat{\beta}_1 x$$

### Estimació dels paràmetres
- Minimitzar la **suma de quadrats dels residus** (RSS):
$$RSS = \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$$
- Dues vies: **Equació Normal** (àlgebra lineal) o **Gradient Descent** (optimització iterativa).

> [!tip] Exemple: Advertising data
> $$\widehat{\text{sales}} = 7.0325 + 0.0475 \times \text{TV}$$
> Cada unitat addicional de pressupost en TV → $+0.0475$ de vendes (de mitjana).

---

## Descens del Gradient Estocàstic (SGD)

**Referència: [[Classes/classe4|Classe 4]]** — el professor hi insisteix; el PDF només el menciona com a opció.

En lloc de l'equació normal, minimitzem la pèrdua de manera **iterativa**: anem ajustant els paràmetres en la direcció oposada al gradient.

### Les tres variants

| Variant | Quantes dades per pas | Caràcter |
|---------|----------------------|----------|
| **Batch GD** | Totes ($n$) | Precís, lent, costós |
| **Stochastic GD (SGD)** | **1 sola mostra** | Ràpid, ruidós, escapa mínims locals |
| **Mini-batch GD** | Un lot petit (p. ex. 32) | Equilibri — el que es fa servir de veritat |

### Per què l'SGD interessa
- Cada pas només mira **una mostra**: molt més ràpid per pas i permet entrenar amb **massa dades per cabre en memòria**.
- El soroll de cada pas fa que no es quedi **atrapat en mínims locals**.
- Convergència menys estable: la corba d'error "sarasseja" en lloc de baixar suau.

> [!warning] **Learning rate**
> - Massa gran → pot **divergir** (els paràmetres exploten).
> - Massa petit → tarda una eternitat.
> - És l'hiperparàmetre clau a ajustar (p. ex. *learning rate scheduling*, *decay*).

---

## Avaluació de la precisió

### Error Estàndard dels coeficients
$$SE(\hat{\beta}_1)^2 = \frac{\sigma^2}{\sum_{i=1}^{n}(x_i - \bar{x})^2}$$
- Reflecteix com varia l'estimador sota mostreig repetit.
- **La std serveix per veure quin és el rang probable on és el valor real** de $\beta_1$: és una mesura de com de fiable és l'estimació.
- Serveix per calcular **intervals de confiança** i **test d'hipòtesi**.

### Interval de confiança al 95%
$$[\hat{\beta}_1 - 2 \cdot SE(\hat{\beta}_1),\ \hat{\beta}_1 + 2 \cdot SE(\hat{\beta}_1)]$$
- Com més **petita** la SE → interval més estret → estimació més **segura**.

### Test d'hipòtesi
- **H0**: $\beta_1 = 0$ (no hi ha relació entre X i Y)
- **HA**: $\beta_1 \neq 0$ (hi ha relació)
- **Estadístic t**: $t = \frac{\hat{\beta}_1 - 0}{SE(\hat{\beta}_1)}$, amb $n-2$ graus de llibertat (distribució **t de Student**).
- **p-value**: probabilitat d'observar un valor tan extrem si H0 fos certa.
  - p-value < 0.05 → rebutgem H0 (relació significativa)
  - p-value < 0.01 → molt significatiu

> [!warning] Un p-value baix **no vol dir causalitat** — vol dir que hi ha evidència estadística d'una relació lineal.

### Signe dels coeficients
- Un **coeficient negatiu** (o un $t$ negatiu) indica un **impacte negatiu**: com més gran la feature, més petit el target.
- Els **valors negatius** (de $\beta$ o $t$) es poden interpretar igual que els positius: només canvien el sentit de la relació, no la importància.

---

## Mètriques d'ajust

### Residual Standard Error (RSE)
$$RSE = \sqrt{\frac{1}{n-2} RSS}$$
- Mesura **absoluta** de l'error del model (falta d'ajust).
- En les **mateixes unitats que Y** → no sempre és clar què és "bo".

### R-squared ($R^2$)
$$R^2 = 1 - \frac{RSS}{TSS} = \frac{TSS - RSS}{TSS}$$
- On $TSS = \sum(y_i - \bar{y})^2$ és la **variància total** (tot el que hi ha dins Y).
- $R^2$ = **proporció de la variància de Y explicada** per X.
- En regressió simple: $R^2 = r^2$ (on $r$ és la correlació de Pearson entre X i Y).

> [!important] Interpretació del $R^2$ (de classe)
> - **Quan major, millor** — és la pregunta típica d'examen, així que assegura't de saber-ho.
> - **$R^2 > 0 \approx 0,7$** comença a ser **bo i útil**, però **depèn de l'ús**: un $R^2$ "baix" pot ser perfectament acceptable segons el context, i un de potser massa alt pot ser sospitós.
> - $R^2$ alt **no vol dir que el model sigui bo**: pot ser **overfitting**. Cal comparar amb les dades de **test**.

---

## Regressió Lineal Múltiple

# Regressió Lineal Múltiple
**Referència: Diapositives 22-34**

## Idees clau
- Quan tenim **més d'una feature**, parlem de regressió lineal múltiple.
- Cada coeficient $\beta_j$ representa l'efecte de $X_j$ sobre Y, **mantingudes les altres variables fixades**.

## Model
$$Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \dots + \beta_p X_p + \epsilon$$

### Interpretació
- $\beta_j$ = **canvi mitjà en Y** per una unitat de $X_j$, **mantingudes totes les altres variables fixades**.
- Predicció: $\hat{y} = \hat{\beta}_0 + \hat{\beta}_1 x_1 + \dots + \hat{\beta}_p x_p$

> [!warning] Si les features estan **correlacionades** entre si, les interpretacions es tornen hazardoses: quan $X_j$ canvia, les altres també canvien. **Cal evitar declaracions de causalitat en dades observacionals.**

## Preguntes clau

| Pregunta | Mètode |
|----------|--------|
| Almenys una feature és útil? | Test F |
| Quines features són importants? | Forward / Backward selection |
| Com s'ajusta el model? | $R^2$, RSE, gràfics de residus |
| Com prediure i amb quina precisió? | Interval de confiança / predicció |

### Test F (almenys un predictor útil?)
- **H0**: $\beta_1 = \beta_2 = \dots = \beta_p = 0$ (cap predictor no ajuda) — el **model nul** (només intercept).
- **HA**: almenys un $\beta_j \neq 0$
$$F = \frac{(TSS - RSS) / p}{RSS / (n - p - 1)} \sim F_{p, n-p-1}$$
- Un **F gran** → rebutgem H0 → el model té poder predictiu.

### Selecció de variables
- **Forward selection**: començar amb el model nul (sense predictors), afegir-ne un a un (el que redueix més RSS) fins a un criteri de parada.
- **Backward selection**: començar amb tots, eliminar-ne un a un (el de p-value més gran) fins a significativitat.
- **Best subsets**: provar totes les combinacions (exponencial → inviable si $p > 20$).

---

## Categorical Predictors (Dummy / One-Hot)

**Referència: Diapositives 35-43 + [[Classes/classe4|Classe 4]]**

- Les features categòriques s'han de convertir en **valors numèrics** abans de fer regressió.
- Per $k$ nivells → es creen **$k-1$ dummy variables** (el nivell **baseline** no en té) — és l'aproximació clàssica de la regressió lineal, que evita **col·linealitat** perfecta.

### Exemple: gènere (2 nivells → 1 dummy)
$$y_i = \beta_0 + \beta_1 x_i + e_i, \quad x_i = \begin{cases} 1 & \text{si dona} \\ 0 & \text{si home} \end{cases}$$

### Exemple: ètnia (3 nivells → 2 dummies)
- Es creen 2 dummies: `Asian` i `Caucasian`.
- L'**baseline** (African American) **no té dummy** → el $\beta_0$ representa la seva mitjana.

### One-Hot Encoding — de classe
- L'**one-hot** passa cada categòrica a un **vector** de 0/1: si tenim 3 valors, la feature es transforma en **3 columnes** (una per valor, 1 si hi pertany i 0 si no).
- El professor diu que per a **3 valors, fer servir 3 columnes (one-hot complet) és millor per a estadística** que no pas la variant dummy $k-1$ de la regressió clàssica.

> [!warning] **A revisar** — La nota de classe diu "3 o 4 (crec) i diu que 3 és millor". S'ha interpretat com $k$ columnes per $k$ valors. Confirmar a classe si es refereix a one-hot complet vs. dummy $k-1$, o a alguna altra cosa.

---

## Interaccions (Synergy Effects)

**Referència: Diapositives 44-51**

- El model **additiu** assumeix que l'efecte de cada feature és **independent** de la resta.
- Però sovint **una feature canvia l'efecte d'una altra**: en marketing es diu **synergy effect**, en estadística **interaction effect**.
- Per capturar-ho → afegir **termes d'interacció**:
$$\widehat{\text{sales}} = \beta_0 + \beta_1 \text{TV} + \beta_2 \text{radio} + \beta_3 (\text{TV} \times \text{radio}) + \epsilon$$
- Exemple: gastar **meitat en TV i meitat en radio** pot donar **més vendes** que gastar-ho tot en un sol canal.

### Jerarquia d'interaccions
- Si incloem un terme d'interacció, **també cal incloure els efectes principals** ($\beta_1$ i $\beta_2$), **encara que no siguin significatius**.

### Exemple real (Advertising)
- Model **sense interaccions**: $R^2 = 89,7\%$ — subestima les vendes quan el pressupost es reparteix entre dos mitjans.
- Model **amb interaccions** ($\text{TV} \times \text{radio}$): $R^2 = 96,8\%$ — evidència estadística contra $H_A: \beta_3 = 0$.

### Interacció qualitativa × quantitativa
$$\text{balance}_i \approx \begin{cases} (\beta_0 + \beta_2) + (\beta_1 + \beta_3) \times \text{income} & \text{si student} \\ \beta_0 + \beta_1 \times \text{income} & \text{si no student} \end{cases}$$
- Els dos grups tenen **pendent** ($\beta_1$ vs. $\beta_1+\beta_3$) i **intercept** ($\beta_0$ vs. $\beta_0+\beta_2$) diferents.

---

## Exemple: Patient Cost Estimation

**Referència: Diapositives 52-59**

- **Dataset**: 1338 exemples, features: `sex`, `bmi`, `children`, `smoker`, `region` → target `charges`.
- **3 features categòriques** (`sex`, `smoker`, `region`) → cal encoding (dummies).
- **Sense missing values**.
- **Divisió**: train 75% / test 25%.
- **Model lineal**: $R^2 = 0,7314$, RMSE = 6009.79.
- **Amb interaccions** (ex. `smoker × bmi`): $R^2$ molt més alt → les interaccions **ajuden molt** en aquest cas.

> [!tip] Abans d'aplicar regressió lineal, cal respondre:
> - Hi ha **missing values**? Quina **distribució** tenen les features?
> - Cal **normalitzar**? Cal **encoding** de categòriques?
> - Hi ha **interaccions** evidents?

---

## Regularització

# Regularització
**Referència: Diapositives 60-64**

## Idees clau
- La **regularització** fa el model **menys complex** per evitar **overfitting** i millorar la **generalització**.
- Funcionament: afegir una **penalització** als coeficients grans a la funció de pèrdua.

## Regressió Lineal (sense regularització)
$$\text{minimize}\left(\sum_{i=1}^{n}(y_i - \beta_0 - \sum_{j=1}^{p}\beta_j x_{ij})^2\right)$$

## Ridge Regression (L2)
$$\text{minimize}\left(\sum_{i=1}^{n}(y_i - \beta_0 - \sum_{j=1}^{p}\beta_j x_{ij})^2 + \lambda \sum_{j=1}^{p}\beta_j^2\right)$$
- Penalitza els **quadrats** dels coeficients ($\beta_j^2$).
- Els coeficients es redueixen però **mai arriben a zero**.
- $\lambda$ = hiperparàmetre que controla la força de la penalització:
  - $\lambda = 0$ → regressió lineal normal
  - $\lambda \to \infty$ → tots els coeficients $\to 0$

## Lasso Regression (L1)
$$\text{minimize}\left(\sum_{i=1}^{n}(y_i - \beta_0 - \sum_{j=1}^{p}\beta_j x_{ij})^2 + \lambda \sum_{j=1}^{p}|\beta_j|\right)$$
- Penalitza els **valors absoluts** dels coeficients ($|\beta_j|$).
- Pot portar coeficients **exactament a zero** → **selecció automàtica de features**.
- Útil quan tenim moltes features i sospitem que moltes no serveixen.

## Comparació Ridge vs. Lasso

| Característica | Ridge (L2) | Lasso (L1) |
|----------------|------------|------------|
| Penalització | $\beta_j^2$ | $|\beta_j|$ |
| Coeficients | Reduïts, **mai zero** | Poden ser **zero** |
| Selecció de features | No | Sí |
| Grups de features correlacionades | Les **reparteix** | N'**escull una** i ignora les altres |

## Limitacions del Lasso
- En dades **high-dimensional** ($n < p$): selecciona com a **màxim $n$ variables** abans de saturar.
- Si hi ha grups de features **molt correlacionades**, n'escull **una** i ignora les altres.

## Elastic Net
$$\text{minimize}\left(RSS + \lambda_1 \sum|\beta_j| + \lambda_2 \sum\beta_j^2\right)$$
- Combina **L1 (Lasso) + L2 (Ridge)**: afegeix una **part quadràtica** a la penalització L1.
- Supera les limitacions del Lasso:
  - Pot seleccionar **més de $n$ variables**.
  - Gestiona millor els grups de features **correlacionades**.
- En la pràctica, sovint és la **millor opció** de les tres.

> [!tip] Quina triar?
> - **Poques features, totes potencialment útils** → **Ridge**
> - **Moltes features, moltes potencialment inútils** → **Lasso**
> - **Dades amb features correlacionades** → **Elastic Net**
> - **Xarxes neuronals** → **Early stopping** (aturar l'entrenament quan l'error de validació puja; veure [[Classes/classe3|Classe 3]])

> [!info] El PDF **ML3-2026_1** ha **tret** les seccions "Early Stopping" i "Knn for Regression" que eren a l'índex de l'anterior versió (ML3-2026). Si encara es fan a classe, caldrà completar-ho.

---

## Enllaços relacionats
- [[Descens del Gradient Estocàstic]]
- [[R-quadrat]]
- [[Error Estàndard dels Coeficients]]
- [[One-Hot Encoding]]
- [[ML2 — Fonaments]]
- [[ML3 — Resum per PPT]]

---

## Dubtes / a revisar
- **One-hot amb 3 valors**: la nota de classe diu "3 o 4 (crec) i diu que 3 és millor per estadística". Interpretat com $k$ columnes per $k$ valors (one-hot complet) vs. $k-1$ dummies de la regressió. **Confirmar a classe.**
- Els apartats **Early Stopping** i **Knn for Regression** han desaparegut de l'índex del PDF nou (ML3-2026_1). Confirmar si s'han retirat del temari o es veuran igualment.
