---
data: 2026-10-05
assignatura: AA
tags:
  - tipus/teoria
  - assignatura/AA
---

# Error Estàndard dels Coeficients

$$SE(\hat{\beta}_1)^2 = \frac{\sigma^2}{\sum_{i=1}^{n}(x_i - \bar{x})^2}$$

## Què diu
- Mesura **com varia l'estimador** $\hat\beta$ si repetim el mostreig moltes vegades.
- En altres paraules: el **rang probable** on és el **valor real** de $\beta$. Petita SE → estimació **segura**; gran SE → estimació **poc fiable**.

## Per a què serveix
- **Interval de confiança** (95%): $\hat\beta_1 \pm 2 \cdot SE(\hat\beta_1)$
- **Test d'hipòtesi**: $t = \hat\beta_1 / SE(\hat\beta_1)$ amb $n-2$ gl. (distribució **t de Student**)
  - $H_0: \beta_1 = 0$ (sense relació) vs. $H_A: \beta_1 \neq 0$
  - **p-value** < 0,05 → rebutgem $H_0$

> [!warning] p-value baix **no vol dir causalitat** — només evidència d'una **relació lineal**.

## Signe dels coeficients
- $\beta$ o $t$ **negatiu** → **impacte negatiu**: com més gran la feature, més petit el target (relació **inversa**).
- El **signe** no afecta la importància, només el **sentit** de la relació.

**Veure també:** [[ML3 — Regressió]] · [[R-quadrat]]
