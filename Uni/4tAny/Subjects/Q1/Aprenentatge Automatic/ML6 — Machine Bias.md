---
data: 2026-11-15
assignatura: AA
parcial: 
tags:
  - tipus/teoria
  - assignatura/AA
---

# ML6 — Machine Bias
**Referència: ML6 MachineBias.pdf (D1-50)**

---

## Què és un classificador ML

# Què és un classificador ML
**Referència: Diapositives 1-5**

## Idees clau
- Un **classificador ML apren de (dades històriques)**: no el programem amb regles, el **deixem que el trobi** el model.
- En molts dominis aconsegueix una **accuracy** millor que altres enfocaments (incloses les **decisions humanes**).
- Però **no és lliure d'errors** (i els humans tampoc).

### Tipus de classificació

| Tipus | Què prediu | Exemple |
|---|---|---|
| **Binària** | 2 classes | infectat / no infectat |
| **Multiclasse** | 1 de k | gat, gos, cavall, persona, peix, ocell… |
| **Multietiqueta** | Diverses a la vegada | gat + gos + … |

### Aprenentatge a partir de dades
- Les **dades d'entrenament es prenen com la *ground truth***: durant l'aprenentatge són la **representació completa del món real** que l'algorisme intenta aproximar.
- Dependència **forta** de les dades → si contenen **biaix no desitjat**, l'algorisme **l'incorpora i el reforça**.
- Pitjor: sense explicacions robustes, els humans **no poden reconèixer les prediccions esbiaixades com a tals**.

> [!important] **Les dades no són neutrals**: el model **hereta i amplifica** el biaix de les dades d'entrenament.

---

## Com avaluem un classificador

# Com avaluem un classificador
**Referència: Diapositives 6-19**

## Idees clau
- Exemple de referència: un model que **diagnostica càncer de còlon** (10 pacients positius, 90 negatius).
- **FP** = negatiu classificat positiu (**tractament innecessari**) · **FN** = positiu classificat negatiu (**es perd una intervenció beneficiosa**).
- Quin és pitjor? **Depèn del problema.**

### Exemple: matriu de confusió (càncer de còlon)
(fileres = realitat Y, columnes = predicció Ŷ)

| Real \ Predicció | Positiu | Negatiu |
|---|---|---|
| **Positiu** | TP = 7 | FN = 3 |
| **Negatiu** | FP = 9 | TN = 81 |

### Mètriques

| Mètrica | Fórmula | Exemple |
|---|---|---|
| **Accuracy** | $(TP+TN)/(TP+FP+TN+FN)$ | $(7+81)/100 = 0.88$ |
| **Precision** | $TP/(TP+FP)$ | $7/16 = 0.4375$ |
| **Recall / Sensitivity** | $TP/(TP+FN)$ | $7/10 = 0.7$ |
| **Specificity** | $TN/(TN+FP)$ | $81/90 = 0.9$ |

> [!tip] **Calibra el model**: dona més pes a allò que et fa més mal.
> - Model A: acc 0.88 / prec 0.43 / recall 0.70 / spec 0.90
> - Model B: acc 0.87 / prec 0.42 / recall 0.90 / spec 0.86
> - *Què pesa més?* **Depèn de l'ús.**

> [!note] Detalls complets (TP/FP/FN/TN, precision, recall, specificity, ROC) → veure **[[Avaluació de Classificadors]]**. Aquí només el mínim per parlar de fairness.

---

## Models que prenen decisions

# Models que prenen decisions
**Referència: Diapositives 20-22**

## Idees clau
- Hi ha models que prenen **decisions crítiques que afecten vides**:
  - diagnòstic mèdic, admissió a la universitat, concessió de préstecs, **predicció de reincidència**, selecció de personal, anuncis online, reconeixement facial, traducció automàtica, motors de recomanació, detecció de frau, límits de crèdit, *pricing*, detecció de notícies falses…
- **No només accuracy… és just el nostre model?** → la pregunta pivot de la resta de l'apunt.

---

## Biaix no desitjat

# Biaix no desitjat
**Referència: Diapositives 22-26**

## Idees clau
- El **biaix no desitjat** pot anar dirigit contra **subgrups sensibles** (gènere, ètnia, edat).
- Consens ampli: distingir per una característica que **normalment no és una elecció** és **injust** → lleis antidiscriminació.
- Estàndard legal actual: **excloure l'atribut sensible** de les dades. **Això no és suficient!**

### Dues fonts de biaix no desitjat
1. Les dades d'entrenament són **incorrectes o no prou representatives** en algun aspecte.
2. Les dades d'entrenament **representen fidelment el món real, però el *status quo* no és ideal** → sense correcció, l'algorisme **reprodueix el *status quo*** i manifesta així una injustícia **existent**.

### Treure race/gender no és suficient
- **Proxy features**: altres features **correlacionen** amb el grup (arrestos previs, antecedents familiars, consum de drogues dels amics…) → el model **recupera A sense veure'l**.
- **Label bias**: la pròpia etiqueta Y pot estar esbiaixada. COMPAS: $Y = $ "re-arrestat en 2 anys", **no** "ha comès un delicte"; els arrestos també depenen **d'on i a qui patrulla la policia**.

> [!important] **Fairness through unawareness** (treure l'atribut sensible) **no elimina el biaix** — i de fet, per **mesurar-lo** **necessitem A**.

---

## Cas COMPAS

# Cas COMPAS
**Referència: Diapositives 27-35**

## Idees clau
- **Maig 2016**: ProPublica publica *Machine Bias* → COMPAS (eina de **predicció de reincidència** usada als EUA) resulta **esbiaixada contra els afroamericans**.
- **COMPAS** és de **Northpointe**. **La raça NO és una entrada** (~137 preguntes del qüestionari).
- Dades: **>10.000 acusats** del comtat de **Broward County (Florida)**; reincidència predita vs real a **2 anys**.
- Malgrat no usar raça: $P(\text{High} \mid \text{Black}) = 59\%$ vs $P(\text{High} \mid \text{White}) = 35\%$.

### Matriu global (7.214 acusats)
(fileres = realitat Y, columnes = predicció Ŷ)

| Real \ Predicció | Low | High |
|---|---|---|
| **No re-offend (Y=0)** | 2681 | 1282 |
| **Re-offend (Y=1)** | 1216 | 2035 |

- Accuracy = $(2681+2035)/7214 =$ **65.37%** — "demostrat" superior al dels jutges.

### Matrius per grup

| Grup | TN | FP | FN | TP |
|---|---|---|---|---|
| **White** (Y=0: 1139 Low / 349 High · Y=1: 461 Low / 505 High) | 1139 | 349 | 461 | 505 |
| **Black** (Y=0: 990 Low / 805 High · Y=1: 532 Low / 1369 High) | 990 | 805 | 532 | 1369 |

- Els ~1.000 acusats restants (7.214 − 2.454 − 3.696) són d'**altres ètnies** (no blancs ni negres): per això els subtotals dels grups no quadren amb la matriu global.

### La resposta de Northpointe
- Accuracy ≈ **60% igual per a blancs i negres** → "un test correcte en igual proporció per a tots els grups **no pot ser esbiaixat**".
- → ProPublica vs Northpointe: **dues lectures de la mateixa matriu** (resolt a "Tres maneres").

> [!note] Activitat de classe *The trial of COMPAS*: l'equip **ProPublica** ha de trobar una mètrica que mostri biaix contra els acusats negres; l'equip **Northpointe**, una que mostri tractament igualitari.

---

## Tres maneres de llegir la matriu de confusió

# Tres maneres de llegir la matriu de confusió
**Referència: Diapositives 36-39**

## Taula-resum
(el centre de l'apunt; fileres = realitat Y, columnes = predicció Ŷ)

| Criteri | Nom alternatiu | Pregunta | Condició | COMPAS | Visió de |
|---|---|---|---|---|---|
| **Independence** | demographic / statistical parity | Tothom és etiquetat High al mateix ritme? | $P(\hat{Y}=1 \mid A)$ | 35% vs 59% | **Ignora** què ha passat de veritat |
| **Separation** | equal error rates | Donat què ha passat de veritat, els dos grups reben el mateix tractament? | $FPR = P(\hat{Y}=1 \mid Y=0, A)$ (i TPR) | FPR 23% vs 45% | **La persona jutgada** (ProPublica) |
| **Sufficiency** | predictive parity | Donat el que diu el model, vol el mateix per als dos grups? | $PPV = P(Y=1 \mid \hat{Y}=1, A)$ | PPV 59% vs 63% | **Qui pren la decisió** (Northpointe) |

### Independence (demographic parity)
$$P(\hat{Y}=1 \mid A=0) = P(\hat{Y}=1 \mid A=1)$$

### Separation — 3 variants
- **Equal opportunity** (FN més sensibles; importa el *recall*):
$$P(\hat{Y}=1 \mid Y=1, A=0) = P(\hat{Y}=1 \mid Y=1, A=1)$$
- **Predictive equality** (FP més sensibles):
$$P(\hat{Y}=1 \mid Y=0, A=0) = P(\hat{Y}=1 \mid Y=0, A=1)$$
- **Equalized odds** (FP + FN):
$$P(\hat{Y}=y \mid Y=y, A=0) = P(\hat{Y}=y \mid Y=y, A=1), \ \forall y \in \{0,1\}$$

### Sufficiency (predictive parity)
(importa la *precision*)
$$P(Y=1 \mid \hat{Y}=1, A=0) = P(Y=1 \mid \hat{Y}=1, A=1)$$

### Exemple: admissió a un màster
(2 grups: UB vs altres universitats; Ŷ=1 admès, Y=1 aprovaria)

| Criteri | Regla | Problema / visió |
|---|---|---|
| **Independence** | Admetre el **mateix percentil de cada grup** (p. ex. 30%) | Si un grup ve millor preparat → rebutges bons / admetes febles |
| **Separation** | Dels que **aprovarien**, admetre el mateix percentil a cada grup | **Visió del sol·licitant**: "si prou bo, mateixa oportunitat vingu d'on vingu" |
| **Sufficiency** | Dels **admesos**, mateix percentil que aprova a cada grup | **Visió de la universitat**: "una admissió garanteix el mateix, vingu d'on vingu" |

---

## COMPAS sota els tres criteris

# COMPAS sota els tres criteris
**Referència: Diapositives 40-42**

| Criteri | Nom | Mètrica | White | Black | Es compleix? |
|---|---|---|---|---|---|
| **Independence** | Demographic parity | $P(\hat{Y}=\text{High})$ | 35% | 59% | ✗ |
| **Separation** | Equal opportunity | $TPR = P(\hat{Y}=\text{High} \mid Y=1)$ | 52% | 72% | ✗ |
| **Separation** | Predictive equality | $FPR = P(\hat{Y}=\text{High} \mid Y=0)$ | 23% | 45% | ✗ |
| **Separation** | Equalized odds | TPR i FPR, ambdós | 52% / 23% | 72% / 45% | ✗ |
| **Sufficiency** | Predictive parity | $PPV = P(Y=1 \mid \hat{Y}=\text{High})$ | 59% | 63% | ≈ ✓ |
| — | Accuracy (Northpointe) | $P(\hat{Y}=Y)$ | 67% | 64% | ≈ |
| **Base rate** | — | $p = P(Y=1)$ | **39%** | **51%** | — |

> [!note] **ProPublica discuteix amb Separation; Northpointe amb Sufficiency. Les mateixes dues matrius.** No és un conflicte de dades, és un **conflicte de criteris**.

---

## No ho podem tenir tot

# No ho podem tenir tot
**Referència: Diapositives 43-46**

- Lab de classe (`ML_MachineBias_COMPAS_lab.ipynb`, al Colab): moure els **llindars per grup**. Resultat:
  - **A** (FPR igual) ✓ (~4/6)
  - **B** (FPR + TPR = equalized odds) ✓ amb cost d'accuracy (64.3% vs 65.1%)
  - **C** (FPR igual **i** PPV igual) **✗ — impossible**

### Per què
- De la matriu de cada grup, amb base rate $p = P(Y=1)$:
$$FPR = \frac{p}{1-p} \cdot \frac{1-PPV}{PPV} \cdot TPR$$

| Grup | $p/(1-p)$ | $(1-PPV)/PPV$ | TPR | ⇒ FPR |
|---|---|---|---|---|
| White | 0.65 | 0.69 | 0.52 | 0.23 |
| Black | 1.06 | 0.59 | 0.72 | 0.45 |

> [!warning] Si les **base rates difereixen** (39% ≠ 51%) i la **PPV és igual** entre grups, **FPR i TPR no poden ser tots dos iguals** — llevat que el classificador sigui perfecte.
> **Chouldechova (2017)** · **Kleinberg, Mullainathan & Raghavan (2017)**.

---

## Llavors, qui té raó? Què podem fer?

# Llavors, qui té raó? Què podem fer?
**Referència: Diapositives 47**

| | Separation | Sufficiency |
|---|---|---|
| **Visió de** | **la persona jutgada** | **qui pren la decisió** |
| **Argument** | Els innocents haurien de tenir la mateixa oportunitat de ser assenyalats per error, siguin del grup que siguin | Una puntuació de "risc alt" hauria de voler dir el mateix per a tothom |

### Palanques tècniques
- **Pre-processing**: arreglar les **dades**.
- **In-processing**: afegir **restriccions de fairness** a la loss.
- **Post-processing**: **llindars per grup** (el que fa el lab).

> [!important] **Triar un criteri de fairness és un judici de valors, no tècnic.**

---

## Model precís vs model just

# Model precís vs model just
**Referència: Diapositives 48-49**

- Escenari: **epidèmia**; tractament nou — si estàs infectat i el prens **te curés**; si no ho estàs i el prens **pots morir**. El model d'infecció no és 100% precís però **salva vides**.

| Model precís | Model just |
|---|---|
| Salva el **85%** de vides (95% dones · 75% homes) | Salva el **80%** de vides (80% dones · 80% homes) |

> [!tip] Pregunta de reflexió (debat/examen típic): **què preferim — un model precís o un model just?** No hi ha resposta tècnica única: és el **judici de valors** de la secció anterior.

---

## Enllaços relacionats
- [[Criteris de Fairness]]
- [[CAS COMPAS]]
- [[Avaluació de Classificadors]]
- [[ML2 — Fonaments]]

---

## Dubtes / a revisar
- El PDF acaba amb una diapositiva de referències (D50) — mirar quins articles cita.
- Black base rate: diapo diu 51% però 1901/3656 ≈ 52% — usar el valor de la diapo (51%).
- Lab: confirmar nom exacte del notebook (ML_MachineBias_COMPAS_lab.ipynb).
