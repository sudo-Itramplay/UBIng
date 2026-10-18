---
id: Mono-repo i Multi-repo
aliases: []
tags:
  - assignatura/ES
  - tipus/teoria
---

# Mono-repo i Multi-repo

**Referència: [[CI_CD]] Diapositives 4-6**

Estratègia de **com s'organitzen els repositoris** d'un projecte.

| | **Mono-repo** | **Multi-repo** |
|---|---|---|
| Definició | **Tot** el projecte en **un** repo | **Un repo per servei o llibreria** |
| Filosofia | Afavoreix la **consistència** | Es concentra en el **decoupling** |
| Ideal per a | Refactoring, canvis grans | **Microserveis** |

**Mono-repo** ✅
- Sol lloc per a **tot** el codi, accessible per tothom.
- Fàcil **reutilitzar/compartir** codi i **col·laborar**.
- Fàcil entendre l'**impacte** del canvi a tot el projecte.
- **Millor per a refactoring** i canvis grans.
- **Vista general** del projecte + fàcil **gestionar dependències**.
- ❌ **Rendiment**: les operacions poden esdevenir **lentes**.

**Multi-repo** ✅
- **Versioning** propi per servei/llibreria.
- Check-outs/pulls **petits i separats** → **sense problemes de rendiment**.
- Equips **independents**, sense accés a tot el codebase.
- **Desenvolupament més ràpid** i flexibilitat.
- Cada servei es **llança per separat** → **CI i CD més fàcils**.
- Millor **access control** (read access).
- ❌ Dependències compartides a **sincronitzar regularment**.
- ❌ **Cultura siloed** → **codi duplicat**, problemes resolts **en duplicat**.
- ❌ **Best practices diferents** per equip.
- ❌ **Tests end-to-end difícils**.

> [!warning] Truc d'examen: **Mono = consistència/refactoring** · **Multi = decoupling/microserveis**. I compte: el **contra** de multi-repo és que el **CI/CD hi surt guanyant** (cadascú desplega al seu ritme).

*(Nota al PDF: **meta** — "a tool for managing multi-project".)*

Vegeu també: [[CI]] · [[CD]] · [[GitHub Actions]]
