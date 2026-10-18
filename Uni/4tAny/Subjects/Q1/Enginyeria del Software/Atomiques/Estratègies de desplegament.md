---
id: Estratègies de desplegament
aliases: []
tags:
  - assignatura/ES
  - tipus/teoria
---

# Estratègies de desplegament

**Referència: [[CI_CD]] Diapositiva 18**

Incloure un **stage de desplegament** abans del **release** que utilitza un **entorn de testing realista**.

- **Blue/green deployment**: **dos entorns idèntics**, **només un live**. Es desplega a l'entorn **offline**; si té èxit, es **canvia** i l'original queda **idle**. L'entorn original serveix de **backup** per **tornar enrere**.
- **Canary Release**: alliberar a un **subconjunt d'usuaris** en un entorn real **limitat**. Èxit → **rollout** ampli; no → **rollback**.
- **A/B testing**: **dues versions** d'una feature desplegades per verificar **performance i usabilitat** — per revisar l'**efectivitat** del canvi i **com el mercat hi reacciona**.
- **Feature Flags**: **enable/disable** una feature en **runtime**, per a **algun(s) o tots** els usuaris.

> [!warning] On es confonen:
> - **Blue/green** = dos **entorns** (infraestructura).
> - **Canary** = **subconjunt d'usuaris** (rollout gradual).
> - **A/B** = **dues versions** per mesurar **reacció** (experiment).
> - **Flags** = **switch en runtime**, sense redeploy.

Vegeu també: [[CD]] · [[CI]]
