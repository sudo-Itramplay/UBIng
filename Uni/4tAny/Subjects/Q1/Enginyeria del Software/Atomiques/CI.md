---
id: CI
aliases:
  - Continuous Integration
tags:
  - assignatura/ES
  - tipus/teoria
---

# CI (Continuous Integration)

**Referència: [[CI_CD]] Diapositives 9-11**

Els desenvolupadors fan **mainline integration** tan aviat com tenen un **healthy commit** que poden compartir.

- Normalment **menys d'un dia de treball** → punts d'integració **freqüents** amb una feature **parcialment construïda**.
- Per **amagar** la feature parcialment construïda: **feature flags**.
- **No és** si hi ha o no feature branch: la diferència entre feature branching i CI és **quan integren els devs amb la mainline**.

Comparació amb Feature Branching:

| Feature Branching *(pull request)* | Continuous Integration |
|---|---|
| Avaluar la feature **com a unitat** | Integració a **freqüència més alta** que la durada de la feature |
| Codi afegit quan la feature és **completa** | **Menys temps** per trobar **conflicts** |
| Merges **menys freqüents** | **Merges més petits** |
| | Encoratja **refactoring** |
| | Requereix **healthy branches** (= **self-testing code**) |
| | **Evidència científica** de millor **software delivery performance** |

> [!warning] *"Frequent integration increases the frequency of merges but reduces their complexity and risk."*

Vegeu també: [[Branching i mainline]] · [[CD]] · [[KANBAN]]
