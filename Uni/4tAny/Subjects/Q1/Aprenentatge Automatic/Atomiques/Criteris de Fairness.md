---
data: 2026-11-15
assignatura: AA
parcial: 
tags:
  - tipus/teoria
  - assignatura/AA
---

# Criteris de Fairness

**Tres maneres de llegir la mateixa matriu de confusió** per comparar grups definits per un atribut sensible $A$ (gènere, ètnia…). (fileres = realitat Y, columnes = predicció $\hat{Y}$)

| Criteri | Nom alternatiu | Condició | Visió de |
|---|---|---|---|
| **Independence** | demographic / statistical parity | $P(\hat{Y}=1 \mid A)$ igual per a tots els grups | Ignora què ha passat de veritat |
| **Separation** | equal opportunity / predictive equality / equalized odds | $TPR$ i $FPR$ iguals entre grups | **La persona jutgada** |
| **Sufficiency** | predictive parity | $PPV = P(Y=1 \mid \hat{Y}=1, A)$ igual entre grups | **Qui pren la decisió** |

- **Independence**: $P(\hat{Y}=1 \mid A=0) = P(\hat{Y}=1 \mid A=1)$
- **Separation**: $P(\hat{Y}=1 \mid Y=y, A=0) = P(\hat{Y}=1 \mid Y=y, A=1)$, per $y \in \{0,1\}$ (TPR i/o FPR)
- **Sufficiency**: $P(Y=1 \mid \hat{Y}=1, A=0) = P(Y=1 \mid \hat{Y}=1, A=1)$

> [!warning] **Teorema d'impossibilitat** (Chouldechova 2017): si les **base rates** ($p = P(Y=1)$) difereixen entre grups, **Separation i Sufficiency no poden coexistir** — llevat que el classificador sigui perfecte.

**Veure també:** [[ML6 — Machine Bias]] · [[CAS COMPAS]] · [[Avaluació de Classificadors]]
