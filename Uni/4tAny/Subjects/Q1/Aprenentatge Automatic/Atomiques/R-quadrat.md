---
data: 2026-10-05
assignatura: AA
tags:
  - tipus/teoria
  - assignatura/AA
---

# R-quadrat

$$R^2 = 1 - \frac{RSS}{TSS} = \frac{TSS - RSS}{TSS}$$

- $RSS = \sum(y_i - \hat y_i)^2$ (variància **no explicada**)
- $TSS = \sum(y_i - \bar y)^2$ (variància **total** de Y)

## Què diu
- **Proporció de la variància de Y que s'explica** amb les features. Entre 0 i 1; **com més alt, millor** l'ajust.
- En regressió **simple**: $R^2 = r^2$ ($r$ = correlació de Pearson entre X i Y).

## Interpretació (de classe)
- **$R^2 > 0 \approx 0,7$** comença a ser **bo i útil**, però **depèn de l'ús**: no hi ha un llindar universal. El professor insisteix que **"quan major, millor"** (pregunta típica d'examen) però que el "bo" depèn del context.

> [!warning] $R^2$ alt **no vol dir que el model sigui bo**
> Pot ser **overfitting**. Cal comparar amb les dades de **test** — un model amb $R^2$ altíssim a train pot anar pitjor a test que un de més senzill.

**Veure també:** [[ML3 — Regressió]] · [[Error Estàndard dels Coeficients]]
