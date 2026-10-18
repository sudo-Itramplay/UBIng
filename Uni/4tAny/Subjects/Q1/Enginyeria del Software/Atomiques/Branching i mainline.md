---
id: Branching i mainline
aliases: []
tags:
  - assignatura/ES
  - tipus/teoria
---

# Branching i mainline

**Referència: [[CI_CD]] Diapositives 7-9**

Conceptes bàsics d'integració de codi:

- **Source Branching**: crear una **còpia** i registrar-hi **tots els canvis** d'aquella còpia. **Branch per persona**, per **evitar conflicts**.
- **Mainline**: branch **única i compartida** = **estat actual** del producte.
- **Healthy Branch**: a cada **commit**, **automated checks** (**build** + **tests**) per assegurar que **no hi ha defects**.
- **Feature Branching**: tota la feina d'una feature a la **seva branch**; s'integra a la mainline quan la feature està **completa**.

> [!warning] *"Branching is easy, merging is harder."*

- **Freqüència d'integració**: integrar **sovint** → més **merges**, però **menys complexitat i risc**.

Workflows que n'existeixen (el PDF només en dona els **diagrames**): **GitFlow Workflow** i **GitHub Workflow**.

Vegeu també: [[CI]] · [[Definition of Done]]
