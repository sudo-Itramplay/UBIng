---
data: 2026-11-15
assignatura: AA
parcial: 
tags:
  - tipus/teoria
  - assignatura/AA
---

# ML4 — Classificació
**Referència: ML4 Classification.pdf (D1-60)**

---

## Regressió Logística

# Regressió Logística
**Referència: Diapositives 1-28**

## Idees clau
- La **classificació** prediu una resposta **qualitativa (categòrica)**, no contínua com a la regressió.
- Tres tipus de tasca:

| Tipus | Descripció | Exemple |
|-------|-----------|---------|
| **Binària** | 2 classes: la **normal** = 0, l'**anormal** = 1 | spam / no spam |
| **Multiclasse** | Més de 2 classes, **una i només una** per mostra | classificar imatges de fruits (poma / plàtan / taronja) |
| **Multilabel** | Un **conjunt d'etiquetes** per mostra, aïllades (no es consideren relacions) | etiquetar un blog amb diversos temes |

- També hi ha classificació **jeràrquica**: categories agrupades en **meta-classes** que es tornen a agrupar fins a l'arrel (ex. text, espècies).
- **Model de referència**: la **regressió logística** (també KNN, Naive Bayes, SVM, Decision Tree, Random Forest, Boosting, GBM, Neural Networks).

> [!warning] **Per què NO regressió lineal?**
> - Si codifiquem $Y = 1$ si Yes, $0$ si No, i classifiquem Yes si $\hat{Y} > 0.5$, sembla perfecte: a la població $E(Y|X) = \Pr(Y=1|X)$.
> - **Però** la regressió lineal pot produir **probabilitats < 0 o > 1** → no té sentit.
> - **Multiclasse encara pitjor**: codificar stroke $= 1$, overdose $= 2$, seizure $= 3$ implica un **ordre i distància falsos** entre categories.

## Funció logística (sigmoide)
$$f(x) = \frac{1}{1 + e^{-x}} = \frac{e^x}{e^x + 1}$$
- Fa un **squeeze** d'una equació lineal **entre 0 i 1** per a qualsevol valor de X.

## Model
$$p(X) = \Pr(Y = 1 \mid X) = \frac{e^{\beta_0 + \beta_1 X}}{1 + e^{\beta_0 + \beta_1 X}}$$
- $e \approx 2.718$ (nombre d'Euler). Amb qualsevol $\beta_0, \beta_1, X$, $p(X) \in [0,1]$.

## Logit (log-odds)
$$\log\left(\frac{p(X)}{1 - p(X)}\right) = \beta_0 + \beta_1 X$$
- Reordenant: les **odds** són $p/(1-p) = e^{\beta_0 + \beta_1 X}$.
- És **lineal en X**: $+1$ unitat de X **multiplica les odds** per $e^{\beta_1}$.

### Multivariable
$$\log\left(\frac{p(X)}{1 - p(X)}\right) = \beta_0 + \beta_1 X_1 + \dots + \beta_p X_p \quad\Rightarrow\quad p(X) = \frac{e^{\beta_0 + \beta_1 X_1 + \dots + \beta_p X_p}}{1 + e^{\beta_0 + \beta_1 X_1 + \dots + \beta_p X_p}}$$

## Estimació: Maximum Likelihood
- Busquem els $\beta$ tals que les probabilitats predites $\hat{p}(x_i)$ s'ajustin el màxim possible a l'estat observat de cada individu.
$$l(\beta_0, \beta_1) = \prod_{i:\,y_i=1} p(x_i) \prod_{i:\,y_i=0} (1 - p(x_i))$$
- La likelihood dona la **probabilitat dels 0/1 observats** → maximitzar-la (a la pràctica la **log-likelihood**, ja que $\log(\prod A) = \sum \log A$).
- Optimització: **gradient descent** → veure [[Descens del Gradient Estocàstic]].
$$\frac{\partial}{\partial \theta_j} J(\theta) = \frac{1}{m} \sum_{i=1}^{m} \left(\sigma(\theta^T x^{(i)}) - y^{(i)}\right) x_j^{(i)}$$

> [!tip] **Exemple numèric** (Default data, predictor `balance`, $\hat{\beta}_0 = -10.65$, $\hat{\beta}_1 = 0.0055$)
> - Balance **1000$** → $\hat{p} = 0.006$ · Balance **2000$** → $\hat{p} = 0.586$ (creix molt de pressa).
> - Només amb `student`: Yes → $\hat{p} = 0.0431$, No → $\hat{p} = 0.0292$ (coeficient **positiu**).

---

## Confounding i Case-Control Sampling

# Confounding i Case-Control Sampling
**Referència: Diapositives 29-39**

## Idees clau
- Afegint predictors (`balance`, `income`, `student`), el coeficient de `student` passa de **positiu a negatiu**. Per què?

> [!important] **Confounding**
> - El **signe d'un coeficient depèn de quines altres variables** hi ha al model.
> - Els estudiants tenen **balances més alts** → taxa *marginal* de default més alta (regressió simple → **positiu**).
> - Però **al mateix balance**, els estudiants fan default **menys** (regressió múltiple → **negatiu**).
> - **Conclusió**: un estudiant és **menys arriscat** que un no-estudiant **amb el mateix balance**.

## Exemple: South African Heart Disease
- **160 casos** (MI, infart) + **302 controls**, tots homes 15–64 anys, Western Cape, principis dels 80.
- **Prevalença molt alta** a la regió: $\pi = 5.1\%$.
- **7 predictors** (factors de risc); `famhist` és binària (història familiar d'MI).
- Objectiu: identificar la **força relativa i direcció** dels factors de risc (no predir).

## Case-Control Sampling
- A la mostra hi ha $\tilde{\pi} = 0.35$ casos, però la prevalença real és $\pi = 0.05$ → **la mostra no reflecteix la proporció real**.
- Podem estimar bé els $\beta_j$ (si el model és correcte), però el **terme constant $\beta_0$ queda mal estimat**.
- **Correcció de l'intercept**:
$$\hat{\beta}^*_0 = \hat{\beta}_0 + \log\frac{\pi}{1-\pi} - \log\frac{\tilde{\pi}}{1-\tilde{\pi}}$$
- Els casos són rars → agafem-los **tots**; amb unes **5×** tants controls n'hi ha prou.

---

## Avaluació de Classificadors

# Avaluació de Classificadors
**Referència: Diapositives 40-53**

## Idees clau
- La **matriu de confusió** binària: files Real × columnes Predicció.

| | Pred. Positive | Pred. Negative |
|---|---|---|
| **Real Positive** | TP | FN |
| **Real Negative** | FP | TN |

- **FP** (negatiu classificat positiu) = **Error Tipus I**.
- **FN** (positiu classificat negatiu) = **Error Tipus II**.

> [!tip] **FP o FN? Depèn del problema**
> - Un **FP** pot portar a un **tractament innecessari**; un **FN** pot perdre una **intervenció beneficiosa**.
> - Diagnòstic de càncer → prioritzem **minimitzar FN** (maximitzar recall).

## Exemple Default (llindar 0.5)
- Error d'entrenament: $(23+252)/10000 = 2.75\%$ (és *training error*; amb $n = 10000$, $p = 4$ l'overfitting no és preocupant).
- Classificar sempre "No" (el *prior*): $333/10000 = 3.33\%$ — **només una mica pitjor!**
- Dels No reals: $23/9667 = 0.2\%$ (**FPR**); dels Yes reals: $252/333 = \mathbf{75.7\%}$ (**FNR**).
- El **llindar és ajustable**: classifiquem Yes si $\Pr(\text{Yes}|X) \geq \theta$. Baixar $\theta$ (p. ex. $0.1$) redueix el **FNR** a costa del FPR (**trade-off**).

## Mètriques (exemple càncer de còlon: 10 positius, 90 negatius; TP=7, FN=3, FP=9, TN=81)

| Mètrica | Fórmula | Valor exemple |
|---|---|---|
| **Accuracy** | (TP+TN)/N | (7+81)/100 = 0.88 |
| **Precision** | TP/(TP+FP) | 7/16 = 0.4375 |
| **Recall / Sensitivity** | TP/(TP+FN) | 7/10 = 0.7 |
| **Specificity** | TN/(TN+FP) | 81/90 = 0.9 |
| **F1-Score** | $2 \cdot \frac{\text{precision} \cdot \text{recall}}{\text{precision} + \text{recall}}$ | 0.538 |

## Comparar dos models

| | Model A | Model B |
|---|---|---|
| Accuracy | 0.88 | 0.87 |
| Precision | 0.43 | 0.42 |
| Recall/Sensitivity | 0.70 | **0.9** |
| Specificity | 0.90 | 0.86 |
| F1-Score | 0.53 | **0.58** |

> [!important] **L'accuracy sola enganya**
> - El Model B té accuracy **més baixa** però recall i F1 **molt més alts** → per detectar malaltia, **el Model B és millor**.
> - Cal considerar sempre el **context** del problema.

## ROC curve & AUC
- El **trade-off** entre sensitivity i specificity el controla el **llindar $\theta$** → es mostra gràficament amb la **corba ROC**.
- **AUC** (àrea sota la corba) = mesura del rendiment **sobre tots els valors de $\theta$**.
- L'AUC és **independent** de la quantitat de positius/negatius → **robust a l'imbalance**.

---

## Classificació Multiclasse

# Classificació Multiclasse
**Referència: Diapositives 54-60**

## Idees clau
- Amb $k$ classes la matriu de confusió és **k×k** (la diagonal = correctes).
- Exemple: predir el tipus de càncer de còlon (A, B, C, D), 40 mostres:
  - **Model A**: accuracy $= (10+5+8+9)/40 = 0.8$.
  - **Model B**: accuracy $= (8+7+9+5)/40 = 0.725$.

## Dataset imbalanced — l'accuracy enganya
- La classe **dominant absorbeix l'accuracy**. Exemple (Model A, imbalanced): recall mitjà per classe $= (0.5+0.9+0.8+0.9)/4 = 0.775$ però **precision mitjana = 0.492**.
- Un model que gairebé sempre prediu "Type A" té accuracy alta però precision/recall **desastroses** per a la resta (Model B: recall mitjà per classe = 0.3225).

## Micro vs Macro average

| Mètode | Com es calcula | Quan preferir-lo |
|---|---|---|
| **Micro-average** | **Sumar** tots els TP, FP, FN de totes les classes i calcular la mètrica global | Quan totes les mostres pesen el mateix |
| **Macro-average** | Calcular la mètrica **per classe** i després **fer la mitjana** | **Class imbalance** (cada classe pesa el mateix) |

> [!important] **Macro-average és preferible amb desbalanceig de classes**
> Tracta cada **classe** com igualment important, no cada **mostra**.

---

## Enllaços relacionats
- [[Regressió Logística]]
- [[Avaluació de Classificadors]]
- [[ML3 — Regressió]]
- [[Descens del Gradient Estocàstic]]
- [[ML5 — SVM]]
- [[ML6 — Machine Bias]]

---

## Dubtes / a revisar
- Rangs de diapositives aproximats (60 en total); ajustar si cal.
- Confirmar si cal practicar el càlcul d'AUC.
