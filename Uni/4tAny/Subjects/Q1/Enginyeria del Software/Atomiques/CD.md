---
id: CD
aliases:
  - Continuous Delivery
  - Continuous Deployment
tags:
  - assignatura/ES
  - tipus/teoria
---

# CD (Continuous Delivery / Deployment)

**Referència: [[CI_CD]] Diapositives 17, 26**

Dues coses **diferents** amb la mateixa sigla:

| | Què és |
|---|---|
| **Continuous Delivery** | Assegura que el programari check-inat a la línia **"dev"** sempre està en un estat que **es pot desplegar** |
| **Continuous Deployment** | Fa que el procés de **desplegament** sigui **totalment automatitzat** |

> [!warning] Truc del PDF (exemple Azure): amb **required reviewers** al environment de **production** → és **Continuous Delivery** (hi ha **aprovació humana**); **sense aprovació** → **Continuous Deployment** (tot **automàtic**).

> [!tip] Millors pràctiques: **implementa Continuous Delivery primer**, i després **progressive delivery** (feature flags).

Vegeu també: [[CI]] · [[Estratègies de desplegament]] · [[GitHub Actions]]
