---
data: 2026-09-28
assignatura: AA
parcial: 
tags:
  - tipus/teoria
  - assignatura/AA
---

# ML3 — Regressió
**Referència: ML3-2026.pdf**

---


---

## Regressió Lineal

# Regressió Lineal
**Referència: ML3, pàgines 1-22**

## Idees clau
- La **regressió lineal** és el model de referència en ML supervisat: senzill, interpretable i sovint sorprenentment efectiu.
- Assumeix **dependència lineal** entre les features ($X_1, X_2, \dots, X_p$) i el target ($Y$).
- Encara que la relació real mai sigui totalment lineal, la regressió lineal és útil tant conceptualment com a la pràctica.

## Regressió Lineal Simple (una feature)

### Model
$$Y = \beta_0 + \beta_1 X + \epsilon$$

- $\beta_0$ = intercept (on talla l'eix Y)
- $\beta_1$ = pendent (efecte de X sobre Y)
- $\epsilon$ = terme d'error (allò que el model no captura)

### Predicció
$$\hat{y} = \hat{\beta}_0 + \hat{\beta}_1 x$$

### Estimació dels paràmetres
- Minimitzar la **suma de quadrats dels residus** (RSS):
$$RSS = \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$$
- Dues vies: **Equació Normal** (àlgebra lineal) o **Gradient Descent** (optimització iterativa).

## Avaluació de la precisió

### Error Estàndar dels coeficients
$$SE(\hat{\beta}_1)^2 = \frac{\sigma^2}{\sum_{i=1}^{n}(x_i - \bar{x})^2}$$
- Reflecteix com varia l'estimador sota mostreig repetit.
- Servix per calcular **intervals de confiança** i **test d'hipòtesi**.

### Interval de confiança al 95%
$$[\hat{\beta}_1 - 2 \cdot SE(\hat{\beta}_1),\ \hat{\beta}_1 + 2 \cdot SE(\hat{\beta}_1)]$$

### Test d'hipòtesi
- **H0**: $\beta_1 = 0$ (no hi ha relació entre X i Y)
- **HA**: $\beta_1 \neq 0$ (hi ha relació)
- **Estadístic t**: $t = \frac{\hat{\beta}_1 - 0}{SE(\hat{\beta}_1)}$, amb $n-2$ graus de llibertat.
- **p-value**: probabilitat d'observar un valor tan extrem si H0 fos certa.
  - p-value < 0.05 → rebutgem H0 (relació significativa)
  - p-value < 0.01 → molt significatiu

> [!warning] Un p-value baix **no vol dir causalitat** — vol dir que hi ha evidència estadística d'una relació lineal.

## Mètriques d'ajust

### Residual Standard Error (RSE)
$$RSE = \sqrt{\frac{1}{n-2} RSS}$$
- Mesura absoluta de l'error del model.
- En les mateixes unitats que Y → no sempre és clar què és "bo".

### R-squared ($R^2$)
$$R^2 = 1 - \frac{RSS}{TSS}$$
- On $TSS = \sum(y_i - \bar{y})^2$ és la variància total.
- $R^2$ = proporció de la variància de Y **explicada** per X.
- Sempre entre 0 i 1; com més alt, millor l'ajust.
- En regressió simple: $R^2 = r^2$ (on $r$ és la correlació de Pearson).

> [!note] $R^2$ alt no vol dir que el model sigui bo — pot ser overfitting. Cal comparar amb les dades de test.

## Exemple: Advertising Data
$$\text{sales} = 7.0325 + 0.0475 \times \text{TV}$$
- Cada unitat addicional de pressupost en TV → $+0.0475$ de vendes (de mitjana).

## Enllaços relacionats
- [[Revisió Estadística]]
- [[Regressió Lineal Múltiple]]
- [[Regularització]]

---

## Regressió Lineal Múltiple

# Regressió Lineal Múltiple
**Referència: ML3, pàgines 22-51**

## Idees clau
- Quan tenim **més d'una feature**, parlem de regressió lineal múltiple.
- Cada coeficient $\beta_j$ representa l'efecte de $X_j$ sobre Y, **mantingudes les altres variables fixades**.

## Model
$$Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \dots + \beta_p X_p + \epsilon$$

### Interpretació
- $\beta_j$ = canvi mitjà en Y per una unitat de $X_j$, **mantingudes totes les altres variables fixades**.

> [!warning] Si les features estan **correlacionades** entre si, les interpretacions es tornen hazardoses: quan $X_j$ canvia, les altres també canvien. Cal evitar declaracions de **causalitat** en dades observacionals.

## Preguntes clau

| Pregunta | Mètode |
|----------|--------|
| Almenys una feature és útil? | Test F |
| Quines features són importants? | Forward / Backward selection |
| Com s'ajusta el model? | $R^2$, RSE, gràfics de residus |
| Com prediure i amb quina precisió? | Interval de confiança / predicció |

### Test F (almenys un predictor útil?)
- **H0**: $\beta_1 = \beta_2 = \dots = \beta_p = 0$ (cap predictor no ajuda)
- **HA**: almenys un $\beta_j \neq 0$
$$F = \frac{(TSS - RSS) / p}{RSS / (n - p - 1)} \sim F_{p, n-p-1}$$
- Un F gran → rebutgem H0 → el model té poder predictiu.

### Selecció de variables
- **Forward selection**: començar sense predictors, afegir-ne un a un (el que redueix més RSS) fins a un criteri de parada.
- **Backward selection**: començar amb tots, eliminar-ne un a un (el de p-value més gran) fins a significativitat.
- **Best subsets**: provar totes les combinacions (exponencial → inviable si $p > 20$).

## Categorical Predictors (Dummy Variables)
- Les features categòriques s'han de convertir en **variables dummy** (0/1).
- Per $k$ nivells → $k-1$ dummy variables (el nivell **baseline** no en té).

### Exemple: gènere
$$y_i = \beta_0 + \beta_1 x_i + e_i, \quad x_i = \begin{cases} 1 & \text{si dona} \\ 0 & \text{si home} \end{cases}$$

### Exemple: ètnia (3 nivells)
- Es creen 2 dummies: `Asian` i `Caucasian`.
- L'**baseline** (African American) no té dummy → el $\beta_0$ representa la seva mitjana.

## Interaccions (Synergy Effects)
- El model **additiu** assumeix que l'efecte de cada feature és **independent**.
- Si volem capturar sinergies → afegir **termes d'interacció**:
$$\text{sales} = \beta_0 + \beta_1 \text{TV} + \beta_2 \text{radio} + \beta_3 (\text{TV} \times \text{radio}) + \epsilon$$
- Exemple: gastar meitat en TV i meitat en radio pot donar més vendes que gastar-ho tot en un sol canal.

### Jerarquia d'interaccions
- Si incloem un terme d'interacció, **també cal incloure els efectes principals** (encara que no siguin significatius).

### Interacció qualitativa × quantitativa
$$\text{balance}_i \approx \begin{cases} (\beta_0 + \beta_2) + (\beta_1 + \beta_3) \times \text{income} & \text{si student} \\ \beta_0 + \beta_1 \times \text{income} & \text{si no student} \end{cases}$$

## Exemple: Patient Cost Estimation
- **Dataset**: 1338 exemples, features: sex, bmi, children, smoker, region, charges.
- 3 features categòriques → cal encoding (dummies).
- **Sense interaccions**: $R^2 = 0.7314$, RMSE = 6009.79.
- **Amb interaccions** (smoker × bmi): $R^2$ molt més alt (les interaccions ajuden molt).

> [!tip] Abans d'aplicar regressió lineal, cal respondre:
> - Hi ha missing values? Quina distribució tenen les features?
> - Cal normalitzar? Cal encoding de categòriques?
> - Hi ha interaccions evidents?

## Enllaços relacionats
- [[Regressió Lineal]]
- [[Regularització]]
- [[Normalització]]
- [[Discretització i Encoding]]

---

## Regularització

# Regularització
**Referència: ML3, pàgines 60-65**

## Idees clau
- La **regularització** fa el model **menys complex** per evitar overfitting i millorar la generalització.
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
| Coeficients | Reduïts, mai zero | Poden ser zero |
| Selecció de features | No | Sí |
| Grups de features correlacionades | Les reparteix | N'escull una i ignora les altres |

## Limitacions del Lasso
- En dades **high-dimensional** ($n < p$): selecciona com a molt $n$ variables abans de saturar.
- Si hi ha grups de features **molt correlacionades**, n'escull una i ignora les altres.

## Elastic Net
$$\text{minimize}\left(RSS + \lambda_1 \sum|\beta_j| + \lambda_2 \sum\beta_j^2\right)$$

- Combina **L1 (Lasso) + L2 (Ridge)**.
- Supera les limitacions del Lasso:
  - Pot seleccionar més de $n$ variables.
  - Gestiona millor els grups de features correlacionades.
- En la pràctica, sovint és la **millor opció** de les tres.

## Early Stopping
- Alternativa a la regularització explícita.
- Entrenar el model i **aturar quan l'error de validació comença a pujar** (abans que faci overfitting).
- Comú en xarxes neuronals.

## Quina triar?

> [!tip]
> - **Poques features, totes potencialment útils** → Ridge
> - **Moltes features, moltes potencialment inútils** → Lasso
> - **Dades amb features correlacionades** → Elastic Net
> - **Xarxes neuronals** → Early stopping

## Enllaços relacionats
- [[Regressió Lineal]]
- [[Regressió Lineal Múltiple]]
- [[Generalització]]
- [[Ajust del Model (Fine-tuning)]]

---

## Train-Test-Validació

# Divisió Train / Test / Validació
**Referència: Diapositives ML2 37-43, classe3**

## Idees clau
- **No es poden prendre decisions basant-se en les dades de test** — un cop les uses, ja no serveixen per avaluar el model final.
- La divisió permet **separar l'aprenentatge de l'avaluació** i evita l'overfitting encobert.

## Conjunts de dades

| Conjunt | Propòsit | Regla |
|---------|----------|-------|
| **Entrenament** (70%) | Entrenar el model | Qualsevol decisió es pot prendre |
| **Validació** (part del train) | Comparar models i ajustar paràmetres | No es pot usar per decisions finals |
| **Test** (30%) | Avaluar el rendiment real | **Cal amagar-lo** fins al final |

> [!warning] Les **dades de test** són les més importants. Si n'hi ha poques, fins i tot un **50-50** pot ser acceptable.

## Per què no usar test per decisions?
- Si canviem el model perquè el test va bé, estem **memoritzant el test** en lloc d'aprendre.
- El test és el **public score** de Kaggle; el **private score** és el que realment importa.
- Si public i private són similars → el model generalitza bé.
- Si són diferents → probable overfitting o underfitting.

## Train-Validation Split
- Del 70% d'entrenament, se'n reserva una part per a **validació**.
- S'hi decideix quin model o quina configuració és la millor.
- **Problema**: la divisió depèn de l'atzar → pot ser que un split tingui millors dades que un altre.

## Cross-Validation
- Per reduir la variabilitat de la divisió.
- Es divideixen les dades en **k grups** (folds).
- Entrenem **k vegades**: a cada iteració, un fold diferent és de test i la resta d'entrenament.
- El resultat final és la **mitjana** dels k intents.
- Més robust que el split senzill, però més costós computacionalment.

> [!tip] **Quina estratègia triar?**
> - Poques dades → cross-validation (aprofitar al màxim el que hi ha).
> - Moltes dades → train-validation split senzill pot ser suficient.

## Presentació de la solució
- Un cop el model es valida → presentar la solució.
- Agafar **només el model escollit** i avaluar-lo amb les **dades de test**.
- Els resultats al test haurien de ser **similars** als de validació.
- Si no ho són → possible problema al pipeline o overfitting a la validació.

## Enllaços relacionats
- [[Generalització]]
- [[Ajust del Model (Fine-tuning)]]
- [[Projecte ML]]
