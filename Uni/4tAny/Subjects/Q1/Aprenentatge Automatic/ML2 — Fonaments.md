---
data: 2026-09-21
assignatura: AA
parcial: 
tags:
  - tipus/teoria
  - assignatura/AA
---

# ML2 — Fonaments d'Aprenentatge Automàtic
**Referència: ML2-2026.pdf**

---


---

## Tipus ML

# Tipus d'Aprenentatge Automàtic

**Referència: Diapositives 1-4**

## Idees clau

- Hi ha **4 grans famílies** de problemes d'aprenentatge automàtic.
- Cada família té un tipus d'entrada, un tipus de sortida i un mètode d'aprenentatge diferent.

## Classificació dels tipus

| Tipus | Dades | Feedback | Què fa | Exemples |
|-------|-------|----------|--------|----------|
| **Supervisat** | Etiquetades | Directe | Predir sortida a partir d'entrada | Classificació, regressió |
| **No supervisat** | Sense etiquetes | Cap | Trobar estructura oculta | Clustering, reducció de dimensionalitat |
| **Semisupervisat** | Poc etiquetades + moltes sense | Mixt | Combinar ambdues per millorar | CV amb pocs labels, descobriment de fàrmacs |
| **Per reforç** | Seqüències d'accions | Sistema de recompensa | aprendre d'errors i maximitzar recompensa | Robots, videojocs |

## Sub-tipus dins de cada família

### Supervisat

- **Classificació**: a quina categoria pertany un punt? (diagnòstic mèdic, detecció de frau, reconeixement d'objectes)
- **Regressió**: quin valor numèric tindrà? (preu d'habitatge, preacció de borsa, data de collita)

### No supervisat

- **Clustering**: quins punts són similars entre si? (comportament de clients, gèneres de vídeos)
- **Reducció de dimensionalitat**: quins són els trets més significats i com es poden resumir? (gens humans, comportament de clients)

### Semisupervisat

- Combina **poc** dades etiquetades amb **moltes** sense etiquetes.
- Casos: detecció d'objectes amb pocs dades d'entrenament, descobriment de fàrmacs amb només uns quants tests fets.

### Per reforç

- L'agent aprèn per **prova i error**, rebent recompenses o càstigs.
- Casos: robots que mouren pel seu entorn, jocs on es premien certes jugades.

## Taules de mètodes per tipus

| Regressió | Classificació | Clustering | Reducció dim. |
|-----------|---------------|------------|---------------|
| Regressió lineal | KNN | K-Means | PCA |
| Regressió bayesiana | SVM lineal | Clustering jeràrquic | MDS |
| SVR | Naive Bayes | K-Medians | NMF |
| Arbres de decisió | Regressió logística | Fuzzy C-Means | LDA |
| Random Forest | Arbres de decisió | K-Medoids | Selecció endavant |
| Xarxes neuronals | Random Forest | Bi-clustering | Selecció enrere |
| KNN | Boosting | Co-clustering | Anàlisi de factors |
| Lasso, Ridge, Elastic Net | Xarxes neuronals | … | … |

> [!tip] Aquests mètodes s'estudiaran en detall més endavant. Per ara, cal memoritzar **a quina taula pertany cada un**.

## Enllaços relacionats

- [[Projecte ML]]
- [[Definicions de Dades]]

---

## Projecte ML

# El Projecte típic d'Aprenentatge Automàtic

**Referència: Diapositives 5-12**

## Idees clau

- Tot projecte d'AA segueix **8 passes**. Cal memoritzar-les en ordre.
- El model no és sempre l'objectiu final: primer cal entendre què vol la "empresa".

## Les 8 passes

1. **Mirar el panorama general** (*Look at the big picture*)
2. **Obtenir les dades** (*Get the data*)
3. **Descobrir i visualitzar** les dades per guanyar intuïció
4. **Preparar les dades** per als algorismes
5. **Seleccionar un model** i entrenar-lo
6. **Ajustar el model** (*fine-tune*)
7. **Presentar la solució**
8. **Llançar, monitorar i mantenir** el sistema

## Passa 1: Mirar el panorama general

### 1.1 Encarar el problema (*Frame the Problem*)

- Primera pregunta: **quin és exactament l'objectiu de negoci?**
- Construir un model no sempre és la fi: com s'espera usar-lo i treure'n profit?
- Saber l'objectiu determina:
  - Quins algorismes seleccionar
  - Quina mesura de rendiment usar
  - Quant esforç / precisió cal
- **Hi ha un mètode actual?** Si no, quina ha de ser la referència?

### 1.2 Seleccionar la mesura de rendiment

Per a problemes de **regressió**, les típiques són:

**RMSE** (Root Mean Square Error):
$$RMSE(X, h) = \sqrt{\frac{1}{m}\sum_{i=1}^{m}(h(x^{(i)}) - y^{(i)})^2}$$

**MAE** (Mean Absolute Error):
$$MAE(X, h) = \frac{1}{m}\sum_{i=1}^{m}|h(x^{(i)}) - y^{(i)}|$$

> [!note] RMSE penalitzar més els errors grans (per l'arrel quadrada), mentre que MAE tracta tots els errors per igual.

### 1.3 Comprovar les suposicions

- Les prediccions del model han de seguir la **mateixa convenció** que les dades reals.
- Si la companyia assumeix errors de cert tipus (p. ex., falsos positius importen més que falsos negatius), cal definir-ho aquí.

## Passa 2: Obtenir les dades

- Les dades poden venir de diferents fonts i formats: txt, csv, xls, xlsx, bases de dades estructurades i no estructurades…

## Passa 3: Descobrir i visualitzar

- Objectiu: guanyar **intuïció** sobre les dades abans de modelar.
- Buscar correlacions, outliers, distribucions, patrons.

## Passa 4: Preparar les dades

> [!warning] Aquesta passa és la més important de totes i la que més temps consumeix.

- Veure [[Preprocessament de Dades]] per als detalls.

## Passa 5: Seleccionar model i entrenar

- Tornem a la taula de [[Tipus ML]] per escollir el mètode adequat.
- Entrenem amb les **dades d'entrenament** (70%).

## Passa 6: Ajustar el model

- Veure [[Ajust del Model (Fine-tuning)]].

## Passa 7: Presentar la solució

- Agafar **només el model escollit** i avaluar-lo amb les **dades de test**.
- Els resultats al test haurien de ser similars als de validació. Si no ho són, hi pot haver un problema al pipeline.
- Presentar resultats al client / cap.

## Passa 8: Llançar, monitorar i mantenir

- Posar en producció i vigilar el rendiment amb el pas del temps.
- Les dades poden canviar → cal anar **actualitzant el model periòdicament**.

> [!tip] Aprendre amb poques dades i, a mesura que es millora, augmentar el volum → mantenir actualitzat.

## Enllaços relacionats

- [[Tipus ML]]
- [[Definicions de Dades]]
- [[Preprocessament de Dades]]
- [[Ajust del Model (Fine-tuning)]]

---

## Definicions de Dades

# Definicions de Dades

**Referència: Diapositives 13-18**

## Idees clau

- Les dades es prediuen a partir de **features** (característiques) per a un conjunt d'**objectes/instàncies**.
- No definim coneixement amb fórmules → busquem **patrons**.

## Vocabulari bàsic

| Terme | Sinònim | Significat |
|-------|---------|------------|
| **Features** | Característiques, predictors, variables independents | Les mesures que tenim (p. ex., metres quadrats, habitacions) |
| **Target / Output** | Resposta, variable dependent | El que volem predir (p. ex., preu de l'habitatge) |
| **Training data** | Dades d'entrenament | Les observacions amb què aprenem el model |
| **Objects / Instances** | Mostres, registres | Cada fila del dataset (p. ex., una casa) |
| **Estimator** | Model predictor | La funció/aprenentatge que hem construït |

> [!note] La **feature dependent** és el que volem predir (el target). Les **features independents** són les que fem servir per predir.

## Tipus de dades

### Quantitatives (numèriques)

- Tenen **ordre** i **distància** significativa entre valors.
- Exemples: edat, preu, mida del terreny, pressió arterial.

> [!warning] Codi postal és **categòric**, no quantitatiu! Encara que sigui un número, no té ordre ni distància real: un CP més gran no vol dir res "més gran" → és com un ID aleatori.

### Categòriques (discretes)

- Categories sense ordre numèric intrínsec.
- Exemples: grup sanguini, ciutat, sí/no, càncer/no càncer.

### Altres tipus

- Imatges
- Vídeos
- Text
- Gens

> [!tip] El David diu que els tipus de dades també surten a Gràfics → fer una diapositiva atòmica d'això.

### Representació de text: Bag of Words

- Cada document es representa com un vector on cada posició és una paraula del diccionari.
- $x_\alpha$ = nombre d'ocurrències de la $\alpha$-èsima paraula en el document $i$.
- Resultat: $x_i = (x_{1i}, x_{2i}, \dots, x_{di})$.

## Dades d'entrenament vs. realitat

- Les dades de **test** són **molt més importants** que les d'entrenament: se'ls dóna prioritat, inclús si hi ha poques dades (fins i tot un 50-50).
- Les dades d'entrenament i les reals han de seguir la **mateixa convenció** (mateix format, mateixes features, mateixa distribució).

## Enllaços relacionats

- [[Tipus ML]]
- [[Revisió Estadística]]
- [[Preprocessament de Dades]]

---

## Revisió Estadística

# Revisió Estadística

**Referència: Diapositives 19-24**

## Idees clau

- Conceptes estadístics bàsics que apareixen arreu en AA.
- **Molt importants** per entendre les dades abans de modelar.

## Mitjana (Mean)

$$\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i$$

- S'anomena $\mu$ quan treballem amb la població sencera.
- **Sensible als outliers**: un valor extrem desplaça molt la mitjana.

## Mediana (Median)

- Valor central quan les dades estan ordenades.
- **Més robusta** que la mitjana: no es veu afectada per outliers.

> [!tip] Si hi ha outliers significatius, la mediana és millor resum que la mitjana.

## Variància (Var(X))

- Mesura com de **dispersos** estan els valors respecte a la mitjana.
- $Var(X) = \frac{1}{n}\sum_{i=1}^{n}(x_i - \bar{x})^2$
- Unitats al quadrat → per tornar a les unitats originals fem servir la **desviació estàndard** ($\sigma = \sqrt{Var(X)}$).

## Covariància (Cov(X, Y))

- Mesura com **canviem conjuntament** dues variables aleatòries.
- Positiva → mouen en la mateixa direcció. Negativa → en direccions oposades.
- El problema: depèn de l'escala → no és interpretada fàcilment.

## Correlació ($\rho$)

$$\rho = \frac{Cov(X, Y)}{\sigma_X \cdot \sigma_Y}$$

- Valor entre **-1** i **+1**:
  - **+1**: correlació lineal positiva total
  - **0**: **no vol dir que no hi hagi correlació!** Pot haver-hi correlació **no lineal**.
  - **-1**: correlació lineal negativa total

> [!warning] **Correlació 0 ≠ cap correlació.** Si les dades formen una bola estranya o tenen una relació no lineal, la correlació de Pearson pot ser 0 malgrat que existeixi una relació real.

## Distribució normal (gaussianiana) $\mathcal{N}(\mu, \sigma^2)$

- Campana de Gauss simètrica al voltant de la mitjana.
- Funció de densitat:

$$f(x|\mu, \sigma^2) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$$

- Propietat clau: aproximadament el **68%** de les dades cauen dins $\mu \pm \sigma$, el **95%** dins $\mu \pm 2\sigma$, i el **99.7%** dins $\mu \pm 3\sigma$.

> [!note] **Outliers**: es defineixen sovint com a punts que cauen **fora de $\mu \pm 2\sigma$** (o 3σ segons el criteri).

## Què s'assumeix vs. realitat

- **Assumpció típica**: les dades segueixen una distribució normal i són **independents**.
- **Realitat**: les dades sovint NO són normals ni independents (p. ex., dades de sèries temporals, dades amb correlació espacial).
- Això afecta quins models funcionen millor i quines mètriques són vàlides.

## Enllaços relacionats

- [[Definicions de Dades]]
- [[Preprocessament de Dades]]

---

## Preprocessament de Dades

# Preprocessament de Dades

**Referència: Diapositives 25-30**

## Idees clau

- És la passa **més important** i que més temps consumeix en un projecte d'AA.
- Tres grans branques: **neteja**, **transformació** i **reducció**.

## Visió general

```
Preprocessament de Dades
├── Neteja de Dades (Data Cleaning)
│   ├── Dades mancants
│   ├── Dades sorolloses (outliers / errors)
│   └── Dades inconsistents
├── Transformació (Data Transformation)
│   ├── Normalització
│   ├── Discretització
│   ├── Encoding de categoriques
│   └── Creació de features
└── Reducció (Data Reduction)
    ├── Agregació
    ├── Selecció de subset de features
    ├── Reducció de mostres
    ├── Reducció de dimensionalitat
    └── Generació de jerarquies de conceptes
```

## 1. Neteja de Dades

### Dades mancants (NaN / missing values)

- **Eliminar el registre**: funciona si les dades mancants són poques i aleatòries.
- **Omplir manualment**: si tenim coneixement del domini.
- **Omplir amb la mitjana / mediana / moda**: mètode automàtic.

> [!tip] **Quan eliminar o quan imputar?**
> - Si la feature té **molts NaN** i no és crucial → eliminar la feature.
> - Si el NaN és puntual → imputar amb mitjana/mediana.
> - Si **cada valor NaN té significat** (p. ex., un any de construcció buit vol dir que no es va construir aquell any) → crear una nova feature categòrica que indiqui "era NaN".

> [!warning] **Mitjana vs. mediana per a imputar**: la mitjana es veu afectada per outliers. Si la feature té outliers (p. ex., mida del terreny), la **mediana** és més segura. No confondre: la mitjana per LandSize, no la mitjana general!

### Dades sorolloses (Noisy Data)

- **Outliers**: valors molt allunyats de la resta. Poden ser errors o dades legítimes.
- **Errors de mesura**: dades incorrectes per fallada instrumental o d'entrada.
- Estratègies: [[Normalització]] (clipping), detecció estadística ($\mu \pm 2\sigma$), o eliminació manual.

### Dades inconsistents

- Tipus de dada inconsistent (p. edat en una columna en anys i en una altra en mesos).
- Categories amb ortografia diferent ("Barcelona" vs "bcn").

## 2. Transformació

- Veure [[Normalització]] per al detall de les tècniques.
- Veure [[Discretització i Encoding]] per a bucketing i encoding categòric.

### Creació de features (*Feature Creation / Feature Engineering*)

- Crear **noves features** a partir de les existents.
- Exemple: si tenim amplada i alçada → crear superfície = amplada × alçada.
- Les **relacions entre dues features** sovint donen una de nova molt més informativa.

> [!note] El professor destaca que la feature creation és una de les parts més creatives i importants del preprocessament.

## 3. Reducció de Dades

- **Agrupació** (*aggregation*): combinar registres (p. ex., dades diàries → mensuals).
- **Selecció de subset de features**: quedar-se només amb les més rellevants.
- **Reducció de mostres** (*sample reduction*): treballar amb una mostra representativa.
- **Reducció de dimensionalitat**: PCA, t-SNE, etc. (es veurem més endavant).
- **Generació de jerarquies de conceptes**: agrupar categories en nivells més alts (p. ex., "carrer" → "barri" → "ciutat").

## Importància per la pràctica

> [!warning] Aquest apartat és **clau per la pràctica**. Cal saber triar correctament:
> - Quan eliminar NaN vs. imputar
> - Quan normalitzar i amb quin mètode
> - Quan crear noves features

## Enllaços relacionats

- [[Normalització]]
- [[Discretització i Encoding]]
- [[Definicions de Dades]]
- [[Revisió Estadística]]

---

## Normalització

# Normalització

**Referència: Diapositives 31-33**

## Idees clau

- Posar totes les features en una **escala similar** millora l'estabilitat i rendiment de molts models.
- Hi ha diferents tècniques segons el tipus de dades i la presència d'outliers.

## Per què normalitzar?

- Si una feature va de 1.000 a 2.000 i una altra de 1 a 3, la primera dominarà el model només per l'escala.
- Els algorismes que depenen de la distància (KNN, SVM, xarxes neuronals) són especialment sensibles a l'escala.

> [!note] Les arbres de decisió i Random Forest **no** necessiten normalització (treballen amb llindars, no amb escales).

## Tècniques

### Min-Max Scaling (a rang [0,1])

$$x' = \frac{x - \min}{\max - \min}$$

- Fa que tots els valors quedin entre 0 i 1.
- **Sensible a outliers**: un sol valor extrem comprimeix la resta.

### Clipping

- Si hi ha outliers extrems, es pot **tallar** (*clip*) tot valor per sobre o per sota d'un llindar a un valor fix.
- Exemple: tota temperatura per sobre de 40 es posa a 40.

### Log Scaling

$$x' = \log(x)$$

- Comprimeix un rang ampli a un de més estret.
- Útil quan la feature segueix una **llei de potència** (power law).
- Canvia la distribució de la feature, millorant models lineals.

### Z-Score Normalization (Standardization)

$$x' = \frac{x - \mu}{\sigma}$$

- Centra les dades al voltant de 0 amb desviació estàndard 1.
- Útil quan hi ha **pocs outliers** (però no tan extrems que calgui clipping).

> [!tip] **Quina triar?**
> - Amb outliers extrems → **clipping** primer, després z-score.
> - Sense outliers significatius → **z-score** (el més habitual).
> - Quan cal rang [0,1] explícit → **Min-Max**.
> - Dades amb llei de potència → **Log scaling**.

## Enllaços relacionats

- [[Preprocessament de Dades]]
- [[Discretització i Encoding]]
- [[Revisió Estadística]]

---

## Discretització i Encoding

# Discretització i Encoding

**Referència: Diapositives 34-35**

## Idees clau

- **Discretitzar** = convertir dades numèriques contínues en categories (buides).
- **Trade-off**: es perd riquesa a canvi de menys granularitat → més fàcil d'aprendre pel model.
- **Encoding categòric** = convertir categories en nombres que el model pugui processar.

## Discretització (Bucketing)

Transformar dades numèriques contínues en **categories** (*buckets*).

### Buides amb límits igualment espaiats

- El rang es divideix en seccions de la mateixa amplada.
- **Problema**: alguns buits poden tenir molts punts i d'altres cap.

### Buides amb límits de quantils

- Cada buit té el **mateix nombre de punts**.
- Els límits no són fixes i poden abastar rangs diferents.

## Encoding de categoriques

### Ordinal Encoding

- Assigna un número enter a cada categoria.
- Funciona quan hi ha **ordre natural** (p. ex., petit=0, mitjà=1, gran=2).
- **Problema**: implica una distància que pot no existir.

### One-Hot Encoding

- Crea una **columna binària** per a cada categoria.
- Exemple: "color" amb valors {vermell, blau, verd} → 3 columnes: `es_vermell`, `es_blau`, `es_verd`.
- **No implica ordre** entre categories.

> [!warning] One-Hot Encoding amb moltes categories pot crear un vector molt llarg i escàs (*sparse*).

### Target Encoding
- En lloc de crear una columna per cada categoria, assignar una **estadística** (mitjana, mediana) del target a cada valor de la categoria.
- Exemple: en lloc de barri → preu mitjà del barri.
- Funciona molt bé amb **moltes característiques** (evita l'explosió dimensional del one-hot).
- S'utilitza especialment quan tenim moltes categories (p. ex., molts carrers diferents).

> [!warning] Cal usar les estadístiques **només del conjunt d'entrenament** per evitar data leakage.

### Target Encoding aplicat a lat/long
- Les coordenades lat/long defineixen **dependència espacial** (bandes més barates i més cares).
- Amb regressió lineal, es pot fer servir la distància al centre o el target encoding per zona.

### Embeddings

- Representació **densa** i de dimensions baixes d'una categoria o paraula.
- S'aprendrà més endavant al curs (NLP, xarxes neuronals).

## Resum

| Mètode | Quan usar-lo | Risc |
|--------|--------------|------|
| Ordinal | Categories amb ordre clar | Distància artificial |
| One-Hot | Categories sense ordre, poques categories | Vector llarg si n'hi ha moltes |
| Target Encoding | Moltes categories, evita esparsitat | Data leakage si no es fa bé |
| Embeddings | Moltes categories, relacions semàntiques | Més complex d'entendre |

## Enllaços relacionats

- [[Normalització]]
- [[Preprocessament de Dades]]
- [[Definicions de Dades]]

---

## Teorema No Free Lunch

# Teorema del No Free Lunch

**Referència: Diapositives 6, 28**

## Idea clau

**No existeix un model que funcioni millor que tots els altres per a qualsevol situació.**

## Per què?

- Tot model és una **simplificació de la realitat**.
- La simplificació es basa en **suposicions** (bias).
- Aquestes suposicions fallen en determinades situacions.

> [!note] Cada model té un **bias propi**: serà millor per a certes coses i pitjor per a d'altres. No hi ha un model perfecte.

## Conseqüències pràctiques

- Cal provar **diversos models** i avaluar quin funciona millor per al nostre problema concret.
- No es pot dir "aquest model és el millor" sense contextualitzar-lo.
- La selecció de model és un procés **empíric**, no teòric.

## Enllaços relacionats

- [[Generalització]]
- [[Ajust del Model (Fine-tuning)]]
- [[Tipus ML]]

---

## Generalització

# Generalització

**Referència: Diapositives 28-30**

## Idees clau

- **Generalització** = la capacitat del model de funcionar bé amb dades que **no ha vist mai**.
- Els dos extrems negatius: **underfitting** i **overfitting**.

## Underfitting (subajustament)

- El model és **massa simple** per capturar el patró real.
- Error alt tant en entrenament com en test.
- Causa: model inadequat, poques features, massa regularització.

## Overfitting (sobreajustament)

- El model **memoritza** el soroll de les dades d'entrenament en lloc d'aprendre el patró real.
- Error baix en entrenament, **alt en test**.
- Causa: model massa complex, poques dades, massa features.

> [!warning] Overfitting és el problema més comú en AA. Si el model funciona "perfecte" a entrenament però malament a test → probable overfitting.

## Gràfiques clau

### Error vs. Mostres d'entrenament

- Amb poques mostres: overfitting fàcil (poc per aprendre).
- A mesura que augmenten les mostres: l'error de test **baixa** i s'aprop al d'entrenament.
- Si les corves no convergeixen → cal més dades o un model diferent.

### Error vs. Nombre de features

- Poques features → underfitting (no hi ha prou informació).
- Moltes features → overfitting (el model aprèn soroll).
- Hi ha un **punt òptim** al mig.

## Conjunts de dades

| Conjunt | Propòsit | Regla |
|---------|----------|-------|
| **Entrenament** (70%) | Entrenar el model | Qualsevol decisió es pot prendre amb aquestes dades |
| **Test** (30%) | Avaluar el rendiment real | **Cal amagar-lo!** No es pot usar fins al final |

> [!warning] Les **dades de test** són les més importants. Si tens poques dades, fins i tot un **50-50** pot ser acceptable: el test ha de tenir prou pes.

## Enllaços relacionats

- [[Teorema del No Free Lunch]]
- [[Ajust del Model (Fine-tuning)]]
- [[Projecte ML]]

---

## Ajust del Model (Fine-tuning)

# Ajust del Model (Fine-tuning)

**Referència: Diapositives 30-35**

## Idees clau

- Els models tenen **diversos paràmetres**. L'ajust consisteix a trobar la **millor configuració** de paràmetres.
- Cal avaluar quin model i quina configuració és la millor **abans** de posar-lo en producció.

## Processos d'avaluació

### Train-Validation Split

- El 70% d'entrenament es divideix en:
  - **Entrenament**: per ajustar els paràmetres del model.
  - **Validació**: per comparar diferents configuracions i escollir la millor.
- És el mètode més senzill.

### Cross-Validation

- Les dades es divideixen en **k parts** (folds).
- Entrenem k vegades, cadascuna amb un fold diferent de test i la resta d'entrenament.
- El resultat final és la **mitjana** dels k intents.
- Més robust que el simple split, però més costós computacionalment.

## Quin model triar?

> Segons el [[Teorema del No Free Lunch]], cal provar-ne diversos i comparar.

1. Entrenar cada model amb les dades d'entrenament.
2. Avaluar-los amb les dades de **validació**.
3. Escollir el que tingui millor rendiment.
4. Fer un **últim test** amb les dades de test (amagades fins ara).

## Errors comuns

- **Usar les dades de test durant l'ajust**: invalida l'avaluació. Les dades de test són sagrades.
- **No actualitzar el model**: les dades canvien amb el temps → cal re-entrenar periòdicament.

> [!warning] Els resultats al test haurien de ser **similars** als de validació. Si no ho són → possible overfitting a la validació o problema al pipeline.

## Enllaços relacionats

- [[Generalització]]
- [[Teorema del No Free Lunch]]
- [[Projecte ML]]
