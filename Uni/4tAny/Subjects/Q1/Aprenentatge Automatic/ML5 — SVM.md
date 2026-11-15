---
data: 2026-11-15
assignatura: AA
parcial: 
tags:
  - tipus/teoria
  - assignatura/AA
---

# ML5 — SVM
**Referència: ML5 SVM.pdf (D1-38)**

---

## SVM: la idea

# SVM: la idea
**Referència: Diapositives 1-2**

- L'**SVM** ataca directament la **classificació binària**: trobar un pla que **separi les classes** a l'espai de features.
- Si no ho pot fer, té **dues escapatòries creatives**:
  1. **Suavitzar** el que significa "separar" → **marge suau** (slack).
  2. **Enriquir/ampliar** l'espai de features perquè la separació esdevingui possible → **kernels**.
- Aquestes dues idees organitzen tota la nota.

---

## Hiperplans i vector normal

# Hiperplans i vector normal
**Referència: Diapositives 3-4**

- Un **hiperpla** en $p$ dimensions és un subespai afí de dimensió $p-1$:
$$\beta_0 + \beta_1 X_1 + \beta_2 X_2 + \dots + \beta_p X_p = 0$$
- En $p=2$ → una **recta**. Si $\beta_0 = 0$ passa per l'**origen**.
- $\beta = (\beta_1, \dots, \beta_p)$ és el **vector normal**: els punts **ortogonals** a la superfície de l'hiperpla.
- Exemple de diapositiva: $\beta_1 = 0.6$, $\beta_2 = 0.8$ (hiperpla en 2D).

---

## Hiperpla separador

# Hiperpla separador
**Referència: Diapositives 5**

- Amb $f(X) = \beta_0 + \beta_1 X_1 + \dots + \beta_p X_p$: $f(X) > 0$ a un costat, $f(X) < 0$ a l'altre.
- Codifiquem les classes com $Y_i = +1$ / $Y_i = -1$.
- **Definició**: si $Y_i \cdot f(X_i) > 0$ per a **tots** els punts, aleshores $f(X) = 0$ és un **hiperpla separador**.

---

## Classificador de marge màxim (Maximal Margin Classifier)

# Classificador de marge màxim (Maximal Margin Classifier)
**Referència: Diapositives 6-7**

- Entre tots els hiperplans separadors, busquem el que té el **forat/marge més gran** entre les dues classes.
- **Optimització restringida**:
$$\text{maximize}_{\beta_0,\dots,\beta_p} M \quad \text{s.t.} \quad \sum_{j=1}^{p} \beta_j^2 = 1, \quad y_i(\beta_0 + \beta_1 x_{i1} + \dots + \beta_p x_{ip}) \ge M \ \ \forall i$$
- **Forma equivalent** (més fàcil de resoldre):
$$\text{minimize}_{\beta_0,\dots,\beta_p} \|\beta\|^2 \quad \text{s.t.} \quad y_i(\beta_0 + \beta \cdot x_i) \ge 1 \ \ \forall i$$
- L'objectiu és **convex i diferenciable** → es resol amb programari estàndard.
- Els punts que **toquen el marge** defineixen l'hiperpla (futurs **support vectors**; formalitzats més endavant via $\alpha$).

> [!warning] **Fràgil**
> Si les dades són separables però **sorolloses** (un punt al costat equivocat), el marge màxim queda **arruïnat per un únic punt** → motiva el marge suau.

---

## Dades no separables i sorolloses

# Dades no separables i sorolloses
**Referència: Diapositives 8-11**

- Sovint **cap** hiperpla lineal separa les dades (excepte si $N < p$, on gairebé sempre és possible).
- Cas no separable: algun punt té $y_i(\beta \cdot x_i) < 1$ passi el que passi amb $w$.
- Voldríem minimitzar el **nombre de punts mal classificats**, però això és **NP-hard** → fem servir **variables slack**.
- El slack permet que **totes les restriccions es satisfacin**, i un **terme de penalització** a l'objectiu fa que "com més slack s'utilitzi, pitjor l'objectiu".

---

## Marge suau: variables slack i C

# Marge suau: variables slack i C
**Referència: Diapositives 12-17**

- **Formulació del Support Vector Classifier**:
$$\text{minimize}_{\beta_0,\beta,\xi} \ \frac{1}{2}\|\beta\|^2 + C\sum_{i=1}^{N} \xi_i \quad \text{s.t.} \quad y_i(\beta \cdot x_i) \ge 1 - \xi_i, \ \ \xi_i \ge 0 \ \ \forall i$$
- Cada $\xi_i$ = "**quant**" viola el punt la seva restricció de marge. $\xi_i = 0$ → costat correcte, **sense penalització**; $\xi_i > 0$ → penalització lineal $C \xi_i$.
- **Com hinge loss**:
$$\xi_i = \max\bigl(0,\ 1 - y_i(\beta \cdot x_i)\bigr)$$
- **C és un hiperparàmetre de regularització**:

| Valor de C | Efecte |
|---|---|
| **C gran** | Penalització alta → marge **estret**, **pocs errors de train** → possible **overfitting** |
| **C petit** | Marge **ample**, tolera errors → més **suau** |
| **C → ∞** | Cas **separable** (marge màxim) |

> [!note] (connexió amb ML3)
> La penalització $C\sum\xi$ és la mateixa idea **loss + penalty** que la regularització Ridge → veure [[ML3 — Regressió]].

---

## Límits lineals i expansió de features

# Límits lineals i expansió de features
**Referència: Diapositives 18-21**

> [!tip] Il·lustració
> Hi ha dades que **cap frontera lineal** separa bé.

- **Expansió de features**: ampliar l'espai amb transformacions ($X_1, X_1^2, X_1X_2, X_1X_2^2, \dots$), de $p$ a $M > p$ dimensions, i ajustar-hi l'SVM → **fronteres de decisió no lineals** a l'espai original.
- Exemple quadràtic fent servir $(X_1, X_2, X_1^2, X_2^2, X_1X_2)$:
$$\beta_0 + \beta_1 X_1 + \beta_2 X_2 + \beta_3 X_1^2 + \beta_4 X_2^2 + \beta_5 X_1 X_2 = 0$$
- Exemple cúbic: de 2 variables a **9** (afegeix $X_1^3$, $X_2^3$, $X_1^2X_2$, $X_1X_2^2$).

> [!warning] **Problema**
> Els polinomis (sobretot en dimensió alta) **exploten en mida** molt ràpid ($\binom{p+d}{d}$ funcions base) → cal una via més elegant → **kernels**.

---

## Productes interiors i forma dual

# Productes interiors i forma dual
**Referència: Diapositives 22-28**

- **Producte interior**: $\langle x_i, x'_i \rangle = \sum_{j=1}^{p} x_{ij} x_{i'j}$.
- **L'SVM lineal es pot escriure amb productes interiors**:
$$f(x) = \beta_0 + \sum_{i=1}^{n} \alpha_i \langle x, x_i \rangle$$
- Té **n paràmetres** (un per observació) en comptes de $p$. Per estimar $\alpha_1, \dots, \alpha_n$ i $\beta_0$ només calen els $\binom{n}{2}$ productes interiors entre parells de training.
- **Support vectors**: la majoria de $\hat\alpha_i$ són **zero**:
$$f(x) = \beta_0 + \sum_{i \in S} \hat\alpha_i \langle x, x_i \rangle, \quad S = \{i : \hat\alpha_i > 0\}$$
- $S$ = **support set**: només els punts que **toquen/violen el marge** decideixen la frontera.
- **Primal** $f(x) = w^T x + b$ vs **Dual**:
$$f(x) = \sum_{i=1}^{N} \alpha_i y_i (x_i^T x) + b, \qquad \beta = \sum_{i=1}^{N} \alpha_i y_i x_i$$
- **Problema dual**:
$$L(\alpha) = \sum_{i=1}^{N} \alpha_i - \frac{1}{2} \sum_{i,j} \alpha_i \alpha_j y_i y_j\, x_i^T x_j$$
- (amb restriccions) — també es resol fàcilment amb programari estàndard.

---

## El truc del kernel (Kernel trick)

# El truc del kernel (Kernel trick)
**Referència: Diapositives 29-31**

- L'SVM original (Vapnik, 1963) era un classificador **lineal**, però el **dual només fa servir productes interiors** ($x_i^T x_j$).
- **Truc**: substituir $x_i^T x_j$ per una funció $K(x_i, x_j)$ que **correspon al producte interior** en un espai de dimensió superior → SVM **no lineal sense mai calcular** l'expansió de features.
- Amb kernel:
$$L(\alpha) = \sum_{i=1}^{N} \alpha_i - \frac{1}{2} \sum_{i,j} \alpha_i \alpha_j y_i y_j K(x_i, x_j)$$
- L'**optimització no canvia de forma**.

### Kernels habituals

| Kernel | Fórmula | Efecte |
|---|---|---|
| **Lineal** | $K(x_i, x_j) = x_i^T x_j$ | SVM lineal (cas base) |
| **Polinòmic** | $K = (1 + \sum_{j} x_{ij} x_{i'j})^d$ | equival a l'expansió polinòmica de grau $d$ → $\binom{p+d}{d}$ funcions base **sense calcular-les** |
| **Radial (RBF)** | $K = \exp(-\gamma \sum_{j} (x_{ij} - x_{i'j})^2)$ | espai implícit de dimensió **molt alta**; $\gamma$ **aplana** la majoria de dimensions → controla la **variància** |

- Al kernel radial: **γ petit** → frontera més **suau**; **γ gran** → frontera molt **flexible** (pot fer overfitting).

---

## Exemple: Heart data (ROC)

# Exemple: Heart data (ROC)
**Referència: Diapositives 32-34**

- Comparació **SVC lineal vs LDA** i **SVM amb $\gamma = 10^{-3}, 10^{-2}, 10^{-1}$** via corbes ROC (train i test). ROC: variar el llindar $t$ a $\hat{f}(X) > t$, registrar TPR/FPR.

> [!note] Lectura de l'exemple
> **NO recrear** la teoria de matrius de confusió/ROC → veure [[Avaluació de Classificadors]]. Només la lectura: un **kernel radial amb γ ben escollit** supera el lineal i la LDA; un γ **massa gran** fa **overfitting** (millor a train, pitjor a test).

---

## SVM amb més de 2 classes (OVA / OVO)

# SVM amb més de 2 classes (OVA / OVO)
**Referència: Diapositives 35-36**

- L'SVM tal com el definim funciona per $K = 2$. Per $K > 2$:

| Estratègia | Com funciona | Classificació |
|---|---|---|
| **OVA (One-vs-All)** | Entrenar **K** SVMs binaris $\hat{f}_k(x)$, cada classe **contra la resta** | $x^*$ a la classe amb el màxim $\hat{f}_k(x^*)$ |
| **OVO (One-vs-One)** | Entrenar $\binom{K}{2}$ SVMs per parelles $\hat{f}_{kl}(x)$ | $x^*$ a la classe que guanya **més** competicions |

- **Quina triar?** Si $K$ **no és massa gran** → **OVO** (segons la diapositiva).

---

## SVM vs Regressió Logística

# SVM vs Regressió Logística
**Referència: Diapositives 37-38**

- Amb $f(X) = \beta_0 + \beta_1 X_1 + \dots + \beta_p X_p$, l'optimització de l'SVM es reescriu com:
$$\text{minimize}_{\beta_0,\dots,\beta_p} \left\{ \sum_{i=1}^{n} \max\bigl[0,\ 1 - y_i f(x_i)\bigr] + \lambda \sum_{j=1}^{p} \beta_j^2 \right\}$$
- Forma **"loss + penalty"** (igual que Ridge): la loss és la **hinge loss**.
- La hinge loss és **molt semblant** a la loss de la regressió logística (negative log-likelihood): totes dues són zero quan es classifica bé amb confiança; però la hinge és **exactament zero** a partir de $yf = 1$ (→ solució **sparse**, support vectors), mentre que la log-loss **mai és exactament zero** (tots els punts contribueixen).
- Veure [[Regressió Logística]].

---

## Enllaços relacionats
- [[Hiperpla Separador]]
- [[Marge Suau (Slack)]]
- [[Kernel (Truc del Kernel)]]
- [[Avaluació de Classificadors]]
- [[Regressió Logística]]
- [[ML3 — Regressió]]

---

## Dubtes / a revisar
- Rang de diapositives (D1-38) és una estimació del text extret; verificar.
- Restriccions del dual no detallades al PDF ($\alpha_i \ge 0$, $\sum_i \alpha_i y_i = 0$); confirmar a classe.
