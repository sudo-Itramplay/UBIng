---
id: GitHub Actions
aliases: []
tags:
  - assignatura/ES
  - tipus/teoria
---

# GitHub Actions

**Referència: [[CI_CD]] Diapositives 22-28**

Plataforma **CI/CD integrada a GitHub** que **automatitza build, test i deployment**.

Conceptes:

- **Workflow**: procés automatitzat definit en **YAML** a `.github/workflows/`.
- **Event**: què el **dispara** (push, pull_request, schedule, manual...).
- **Job**: conjunt de **steps** en un **runner fresc**. Corren **en paral·lel** per defecte, o en **seqüència amb `needs`**.
- **Action**: **step reutilitzable** (ex. `actions/checkout`) del **Marketplace**.

Papers:

| Paper | Què fa | Trigger típic |
|---|---|---|
| **CI** | Verificar **cada canvi** (compile, lint, test) | push, pull_request |
| **CD a Azure** | **dockerize** + registry + Azure App Service | push to main |
| **Board flows** | Sincronitzar el **tauler** | issues, pull_request |

Detealls clau:

- Resultat al PR = **status check**; fes-lo **required** amb **branch protection** → **main sempre green**.
- `strategy.matrix` = **versions múltiples en paral·lel** · `cache: npm` = **build ràpid**.
- CD a Azure: **OIDC** recomanat per Microsoft; imatge etiquetada amb **`github.sha`** = artefacte **immutable** → **rollback trivial**; **environments + slots** per staging/aprovacions/blue-green.
- Gestió de tauler: automations **built-in sense YAML**; fluxos custom = workflow + **Projects GraphQL API** + PAT/App token; `actions/add-to-project`.

Millors pràctiques:

- **Branch protection** + **required status checks**.
- **Pin** actions a **versió major** o **SHA** i revisar-les periòdicament.
- Secrets a *Settings → Secrets*; prefereix **OIDC** sobre credencials estàtiques.
- **`concurrency`** evita **deployments simultanis**.
- Objectiu: **CI < 10 minuts**.

> [!tip] Resum del pipeline: **push/PR → CI (lint, build, test) → merge to main → Docker image (SHA) → registry → staging (slot) → optional approval → production**.

Vegeu també: [[CI]] · [[CD]] · [[Branching i mainline]]
