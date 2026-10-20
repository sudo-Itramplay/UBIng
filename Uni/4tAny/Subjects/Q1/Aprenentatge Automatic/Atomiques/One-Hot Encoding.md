---
data: 2026-10-05
assignatura: AA
tags:
  - tipus/teoria
  - assignatura/AA
---

# One-Hot Encoding

Passar una **feature categòrica** a un **vector** de 0/1: cada valor de la categoria es converteix en la seva **pròpia columna**, amb 1 si la mostra hi pertany i 0 si no.

## Exemple
`color` amb valors `{vermell, blau, verd}` → 3 columnes:

| color | vermell | blau | verd |
|-------|---------|------|------|
| vermell | 1 | 0 | 0 |
| blau | 0 | 1 | 0 |
| verd | 0 | 0 | 1 |

## Dummy ($k-1$) vs. One-hot ($k$)

| | Dummy ($k-1$) | One-hot ($k$) |
|---|---|---|
| Columnes | $k-1$ (baseline sense dummy) | $k$ (una per valor) |
| Ús típic | **Regressió lineal** clàssica | Xarxes, KNN, etc. |
| Perill | — | **Col·linealitat** perfecta si totes les columnes són linealment independents |

> [!warning] **De classe**: el professor diu que per a **3 valors, fer servir 3 columnes (one-hot complet) és millor per a estadística** que no pas la variant dummy $k-1$. ⚠️ *A confirmar exactament a classe.*

> [!note] **Eliminació de la dependència lineal**: en regressió lineal, si posem $k$ columnes one-hot amb intercept, són **linealment dependents** (la suma de les $k$ columnes = 1 = intercept). Per això la regressió clàssica usa $k-1$.

**Veure també:** [[ML3 — Regressió]] · [[Uni/4tAny/Subjects/Q1/Aprenentatge Automatic/Classes/classe3|Classe 3 (altres encoders)]]
