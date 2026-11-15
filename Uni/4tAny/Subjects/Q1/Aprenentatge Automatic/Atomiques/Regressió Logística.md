---
data: 2026-11-15
assignatura: AA
parcial: 
tags:
  - tipus/teoria
  - assignatura/AA
---

# Regressió Logística
- Model de **classificació** que estima $\Pr(Y = 1 \mid X)$ amb la funció **sigmoide**, de manera que la sortida queda sempre **entre 0 i 1** (la regressió lineal no ho pot garantir: pot donar valors < 0 o > 1).
$$p(X) = \frac{e^{\beta_0 + \beta_1 X}}{1 + e^{\beta_0 + \beta_1 X}} \qquad \log\left(\frac{p(X)}{1-p(X)}\right) = \beta_0 + \beta_1 X$$
- El **logit** és **lineal en X**: $+1$ unitat de X multiplica les **odds** per $e^{\beta_1}$.
- Els coeficients s'estimen per **maximum likelihood** (maximitzar la probabilitat dels 0/1 observats) amb **gradient descent**.
- Exemple (Default): balance 2000$ → $\hat{p} = 0.586$.

> [!warning] Un coeficient només s'interpreta **mantingudes les altres variables fixades** (**confounding**): el signe de `student` canvia segons si `balance` és al model.

**Veure també:** [[ML4 — Classificació]] · [[Descens del Gradient Estocàstic]]
