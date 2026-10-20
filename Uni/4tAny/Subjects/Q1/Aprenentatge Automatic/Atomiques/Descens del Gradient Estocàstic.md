---
data: 2026-10-05
assignatura: AA
tags:
  - tipus/teoria
  - assignatura/AA
---

# Descens del Gradient Estocàstic

Minimitzar una funció de pèrdua de manera **iterativa**: en lloc de resoldre'l d'un cop (equació normal), donem **passes** en la direcció oposada al **gradient** fins trobar el mínim.

## Les tres variants

| Variant | Quantes dades per pas | Caràcter |
|---------|----------------------|----------|
| **Batch GD** | **Totes** ($n$) | Precís i estable, però lent i costós |
| **Stochastic GD (SGD)** | **1 sola mostra** | Ràpid, **ruidós**, escapa mínims locals |
| **Mini-batch GD** | Un **lot petit** (p. ex. 32) | Equilibri — el que es fa servir de veritat |

## Per què l'SGD interessa
- Cada pas només mira **una mostra** → molt ràpid per pas i **entrena amb massa dades per cabre en memòria**.
- El **soroll** de cada pas fa que **no s'atrapi en mínims locals**.
- Convergència menys estable: la corba d'error "sarasseja" en lloc de baixar suau.

> [!warning] **Learning rate** (taxa d'aprenentatge)
> - Massa **gran** → pot **divergir** (els paràmetres exploten).
> - Massa **petit** → tarda una eternitat.
> - És l'hiperparàmetre clau a ajustar (*learning rate scheduling*, *decay*).

**Veure també:** [[ML3 — Regressió]] · [[Generalització]]
