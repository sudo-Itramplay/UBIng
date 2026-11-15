---
data: 2026-11-15
assignatura: AA
parcial: 
tags:
  - tipus/teoria
  - assignatura/AA
---

# Kernel (Truc del Kernel)

- El **dual** de l'SVM només fa servir **productes interiors** ($x_i^T x_j$): mai necessitem els vectors en cru.
- **Truc**: substituir $x_i^T x_j$ per una funció $K(x_i, x_j)$ que equival al **producte interior en un espai ampliat** de dimensió superior → SVM **no lineal sense calcular mai** l'expansió de features.
- El problema dual manté **exactament la mateixa forma**, només canviant el producte interior pel kernel:
$$L(\alpha) = \sum_{i=1}^{N} \alpha_i - \frac{1}{2} \sum_{i,j} \alpha_i \alpha_j y_i y_j K(x_i, x_j)$$
- **Kernels habituals**:
  - **Polinòmic**: $K = (1 + \sum_{j} x_{ij} x_{i'j})^d$ — equival a l'expansió de grau $d$ ($\binom{p+d}{d}$ funcions base) **sense calcular-la**.
  - **Radial (RBF)**: $K = \exp(-\gamma \sum_{j} (x_{ij} - x_{i'j})^2)$ — espai implícit de dimensió **molt alta**.
- **El paper de γ** (kernel radial): **γ petit** → frontera **suau**; **γ gran** → frontera molt **flexible** (pot fer **overfitting**). γ controla la **variància** del model.

**Veure també:** [[ML5 — SVM]] · [[Marge Suau (Slack)]] · [[Avaluació de Classificadors]]
