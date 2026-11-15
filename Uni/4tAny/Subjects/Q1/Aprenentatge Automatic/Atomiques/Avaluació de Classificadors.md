---
data: 2026-11-15
assignatura: AA
parcial: 
tags:
  - tipus/teoria
  - assignatura/AA
---

# Avaluació de Classificadors
- **Matriu de confusió** binària:

| | Pred. Positive | Pred. Negative |
|---|---|---|
| **Real Positive** | TP | FN |
| **Real Negative** | FP | TN |

| Mètrica | Fórmula |
|---|---|
| **Accuracy** | (TP+TN)/N |
| **Precision** | TP/(TP+FP) |
| **Recall / Sensitivity** | TP/(TP+FN) |
| **Specificity** | TN/(TN+FP) |
| **F1-Score** | $2 \cdot \frac{\text{precision} \cdot \text{recall}}{\text{precision} + \text{recall}}$ |

- **FP** = Error **Tipus I** (negatiu classificat positiu); **FN** = Error **Tipus II** (positiu classificat negatiu).
- **ROC/AUC**: el trade-off sensitivity–specificity el controla el llindar $\theta$; l'**AUC** resumeix el rendiment sobre **tots** els llindars i és **independent** del balanceig de classes.

> [!important] **Amb dades desbalancejades l'accuracy enganya**: mirar precision/recall i fer servir el **macro-average** entre classes (cada classe pesa igual, no cada mostra).

**Veure també:** [[ML4 — Classificació]] · [[ML5 — SVM]] · [[ML6 — Machine Bias]]
