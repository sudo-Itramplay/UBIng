---
data: 2026-10-05
assignatura: AA
parcial: 
tags:
  - tipus/teoria
  - assignatura/AA
---

# ML3 — Resum per PPT
Fitxa de repàs de [[ML3 — Regressió]]. Per anar ràpid: el que cal saber, diapositiva a diapositiva.

---

## D1-4 · Introducció
- **Regressió lineal** = model de referència del ML supervisat: senzill, interpretable, efectiu.
- Assumeix **dependència lineal** de $Y$ en $X_1, \dots, X_p$.
- La **funció real mai és lineal** — i tot i així funciona molt bé.
- Serveix per veure **correlacions**, **no causes**.

## D5-8 · Regressió lineal simple
$$Y = \beta_0 + \beta_1 X + \epsilon$$
- $\beta_0$ intercept · $\beta_1$ pendent · $\epsilon$ error (el que el model no captura).
- Predicció: $\hat{y} = \hat{\beta}_0 + \hat{\beta}_1 x$
- Estimació: minimitzar $RSS = \sum (y_i - \hat{y}_i)^2$ via **Equació Normal** o **Gradient Descent**.
- Exemple TV: $\widehat{\text{sales}} = 7,0325 + 0,0475 \times \text{TV}$

## D9-15 · Avaluació dels coeficients
- **Error estàndard (SE)**: com varia $\hat\beta$ amb mostreigs diferents → dona el **rang probable** del valor real.
- **Interval confiança 95%**: $\hat\beta_1 \pm 2 \cdot SE(\hat\beta_1)$
- **Test t**: $t = \hat\beta_1 / SE(\hat\beta_1)$, amb $n-2$ gl. (distribució **t de Student**)
- **p-value**: probabilitat d'un resultat tan extrem si $H_0$ fos certa.
  - < 0,05 → rebutgem $H_0$ · < 0,01 → molt significatiu
- ⚠️ p-value baix **≠ causalitat**, només relació lineal estadística.
- **Signe negatiu** de $\beta$ o $t$ = **impacte negatiu** (com més $X$, menys $Y$).

## D16-21 · Ajust del model
- **RSE** $= \sqrt{RSS/(n-2)}$ → error absolut, en les **unitats de Y** (no sempre clar si és "bo").
- **$R^2$** $= 1 - RSS/TSS$ → **proporció de la variància de Y explicada** per X.
  - En regressió simple: $R^2 = r^2$ (correlació de Pearson).
  - **Major = millor**. $R^2 \gtrsim 0,7$ ja és "bo i útil", **però depèn de l'ús**.
  - ⚠️ $R^2$ alt **no garantitza** un bon model: pot ser **overfitting** → comparar amb **test**.
  - Exemple TV: $R^2 = 31,2\%$ (dèbil).

## D22-26 · Regressió múltiple
$$Y = \beta_0 + \beta_1 X_1 + \dots + \beta_p X_p + \epsilon$$
- $\beta_j$ = canvi mitjà en $Y$ per unitat de $X_j$ **mantingudes les altres fixades**.
- ⚠️ Features **correlacionades** → interpretacions hazardoses; res de **causalitat** en dades observacionals.

## D27-34 · Les 4 preguntes clau
| Pregunta | Mètode |
|---|---|
| Almenys una feature és útil? | **Test F** |
| Quines importen? | **Forward / Backward selection** |
| Com s'ajusta? | $R^2$, RSE, residus |
| Com prediure i amb quina precisió? | Interval confiança / predicció |

- **Test F**: $H_0: \beta_1 = \dots = \beta_p = 0$ vs. $H_A$: almenys un $\neq 0$
$$F = \frac{(TSS-RSS)/p}{RSS/(n-p-1)} \sim F_{p,\,n-p-1}$$
- **Forward**: del model nul, afegir el que més redueix RSS. **Backward**: de tots, treure el menys significatiu.

## D35-43 · Categòriques → dummies
- $k$ nivells → **$k-1$ dummies** ($k-1$ de la regressió clàssica) — el **baseline** no en té.
- Ex. gènere (2 nivells → 1 dummy) · Ex. ètnia (3 nivells → 2 dummies: Asian, Caucasian).
- **One-hot** (classe): passa cada categòrica a un vector 0/1; per a 3 valors → **3 columnes**. Diu que **3 és millor per a estadística**. ⚠️ *Confirmar.*

## D44-51 · Interaccions (synergy)
- Model additiu → efectes **independents**. Sovint una feature **canvia l'efecte** d'una altra.
$$\widehat{\text{sales}} = \beta_0 + \beta_1 \text{TV} + \beta_2 \text{radio} + \beta_3 (\text{TV} \times \text{radio}) + \epsilon$$
- **Jerarquia**: si poses interacció, **has de posar també els efectes principals**, siguin significatius o no.
- **Reals**: sense interaccions $R^2 = 89,7\%$ · amb interaccions $R^2 = 96,8\%$.
- **Qualitativa × quantitativa**: cada grup té **pendent** i **intercept** diferents ($\beta_1$ vs. $\beta_1+\beta_3$).

## D52-59 · Exemple Patient cost
- 1338 exemples · `sex`, `bmi`, `children`, `smoker`, `region` → `charges`.
- 3 categòriques → encoding · **sense missing values**.
- Train 75% / test 25% → $R^2 = 0,7314$, RMSE = 6009,79.
- Amb interaccions (`smoker × bmi`): $R^2$ **molt més alt**.

## D60-64 · Regularització
- **Regularitzar** = fer el model **menys complex** → millor **generalització**, menys **overfitting**.

| | Ridge (L2) | Lasso (L1) |
|---|---|---|
| Penalitza | $\sum \beta_j^2$ | $\sum \|\beta_j\|$ |
| Coeficients | redueix, **mai 0** | pot **ser 0** |
| Selecció features | no | **sí** |
| Features correlacionades | les **reparteix** | n'escull **una** |

- **Elastic Net** = L1 + L2 → supera les dues limitacions del Lasso (màx. $n$ variables; grups correlacionats).
- **Quina triar?** poques i útils → Ridge · moltes i potser inútils → Lasso · correlacionades → Elastic Net · xarxes → early stopping.

## D65 · Cierre
- "Any idea of **non-linear** methods?" → porta cap a models no lineals (ML següent).

---

## Del que va dir el professor (classe4)
- Estem a la **part de descens estocàstic** del temari.
- **$R^2$**: "quan major, millor" — pregunta típica d'examen.
- **SE/std**: serveix per veure el **rang probable** on és el valor.
- Valors **negatius** = **impacte negatiu**; $t$ o $\beta$ molt negatiu → relació **inversa**.
- **One-hot** amb 3 valors → **3 columnes** és millor per a estadística.
- La part d'**avaluació** no diu res nou respecte a l'anterior → es pot resumir.
