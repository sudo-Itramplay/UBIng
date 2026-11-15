---
data: 2026-11-15
assignatura: AA
parcial: 
tags:
  - tipus/teoria
  - assignatura/AA
---

# Marge Suau (Slack)

- Quan les dades **no són separables** (o són sorolloses), cap hiperpla satisfà $y_i(\beta \cdot x_i) \ge 1$ per a tots els punts → introduïm **variables slack** $\xi_i$ que **toleren violacions** del marge:
$$\xi_i = \max\bigl(0,\ 1 - y_i(\beta \cdot x_i)\bigr)$$
- Formulació del **Support Vector Classifier**:
$$\text{minimize}_{\beta_0,\beta,\xi} \ \frac{1}{2}\|\beta\|^2 + C\sum_{i=1}^{N} \xi_i \quad \text{s.t.} \quad y_i(\beta \cdot x_i) \ge 1 - \xi_i, \ \ \xi_i \ge 0 \ \ \forall i$$
- **C és un hiperparàmetre de regularització**:
  - **C gran** → penalització alta → marge **estret**, pocs errors de train → possible **overfitting**.
  - **C petit** → marge **ample**, tolera errors → més suau.
  - **C → ∞** → cas **separable** (marge màxim).
- Per què no minimitzar directament el nombre d'errors? Comptar punts mal classificats és **NP-hard** → el slack linealitzat amb penalització és la sortida computacional pràctica.

**Veure també:** [[ML5 — SVM]] · [[Hiperpla Separador]] · [[ML3 — Regressió]]
