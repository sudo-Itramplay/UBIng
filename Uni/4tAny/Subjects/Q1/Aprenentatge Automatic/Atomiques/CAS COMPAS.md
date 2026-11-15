---
data: 2026-11-15
assignatura: AA
parcial: 
tags:
  - tipus/teoria
  - assignatura/AA
---

# CAS COMPAS

**ProPublica, maig 2016**: publica *Machine Bias* → **COMPAS** (eina de **predicció de reincidència** de **Northpointe**, usada als EUA) resulta **esbiaixada contra els afroamericans**.

- Dades: **>10.000 acusats** del comtat de **Broward County (Florida)**; reincidència predita vs real a **2 anys**.
- **La raça NO és una entrada** (~137 preguntes del qüestionari) — però el biaix hi és: **proxy features** + **label bias** ($Y = $ "re-arrestat", no "ha comès un delicte"; els arrestos depenen d'on i a qui patrulla la policia).

Accuracy global (7.214 acusats) = 65,37%

| Mètrica | White | Black |
|---|---|---|
| $P(\text{High})$ | 35% | **59%** |
| $FPR$ | 23% | **45%** |
| $TPR$ | 52% | **72%** |
| $PPV$ | 59% | 63% ≈ **igual** |
| Accuracy | 67% | 64% ≈ **igual** |
| **Base rate** $p = P(Y=1)$ | 39% | **51%** |

- **Dues lectures de la mateixa matriu**: ProPublica discuteix amb **Separation** (FPR/TPR), Northpointe amb **Sufficiency** (PPV) i accuracy. Conflicte de **criteris**, no de dades.

**Veure també:** [[ML6 — Machine Bias]] · [[Criteris de Fairness]] · [[Avaluació de Classificadors]]
