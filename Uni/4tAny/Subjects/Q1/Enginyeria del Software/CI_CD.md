---
id: CI_CD
aliases:
  - CI/CD
tags:
  - assignatura/ES
  - tipus/teoria
---

# CI / CD

**Referència: Diapositives 1-28** (`PDFs/6-CI_CD.pdf` — Eloi Puertas)

El PDF presenta el cicle sencer **"Continuous..."**: Design → DEV → Testing → Integration → Delivery/Deployment.

## Continuous Design

- **Crear i modificar el disseny** d'un sistema **a mesura que es desenvolupa**.
- Continuous Design i Development implica:
  - **TDD** (Test Driven Development).
  - **Refactoring**.

**Referència: Diapositiva 2**

## Continuous Testing

- Procés d'execució de **tests automatitzats** com a part del procés àgil de desenvolupament (**Self-Testing Code**).
- Proveeix **feedback ràpid i continu**.
- Inclou la validació de **dúes** coses:
  - **Requisits funcionals**: unit test, API testing, integration testing, system testing...
  - **Requisits no funcionals**: static code analysis, security testing, performance testing...

**Referència: Diapositiva 3**

## Estratègia de repositoris

| | **Mono-repo** | **Multi-repo** |
|---|---|---|
| Definició | **Tot** el projecte en **un** repo | **Un repo per servei o llibreria** |
| Filosofia | Afavoreix la **consistència** | Es concentra en el **decoupling** |
| Ideal per a | Refactoring, canvis grans | **Microserveis** |

### Mono-Repo

- Un **sol lloc** per emmagatzemar tot el codi del projecte, accessible per **tothom** de l'equip.
- Fàcil **reutilitzar i compartir** codi, col·laborar amb l'equip.
- Fàcil entendre l'**impacte** del teu canvi a tot el projecte.
- Millor opció per a **code-refactoring** i **canvis grans**.
- Els membres de l'equip tenen una **vista general** de tot el projecte.
- Fàcil **gestionar dependències**.
- ➖ **Rendiment**: les operacions poden esdevenir **lentes**.

### Multi-Repo

- Cada servei i llibreria té el seu **versioning** propi.
- Els **check-outs i pulls són petits i separats**: **no hi ha problemes de rendiment** ni si el projecte creix.
- Els equips treballen **independentment** i no necessiten accés a tot el codebase.
- **Desenvolupament més ràpid** i flexibilitat.
- Cada servei es pot **alliberar per separat** i té el seu **cicle de desplegament**, fent **CI i CD més fàcils** d'implementar.
- Millor **access control**: no tots els equips necessiten accés complet, però poden tenir **read access**.
- ➖ Les **dependències i llibreries** compartides s'han de **sincronitzar regularment** per tenir l'última versió.
- ➖ Encoratja una **cultura siloed** en algun punt → **codi duplicat** i equips intentant resoldre el **mateix problema**.
- ➖ Cada equip pot seguir **best practices diferents** → dificultats per seguir practices comuns.
- ➖ **Els tests end-to-end poden ser difícils**.

> [!note] Nota al PDF: **meta** — "a tool for managing multi-project".

**Referència: Diapositives 4-6**

## Branching i integració de codi

- **Source Branching**: crear una **còpia** i registrar-hi **tots els canvis** d'aquella còpia. **Branch per persona**, per evitar **conflicts**.
- **Mainline**: una branch **única i compartida** que actua com l'**estat actual** del producte.
- **Healthy Branch**: a cada commit, fer **automated checks** (normalment **build** i **tests**) per assegurar que **no hi ha defects** a la branch.

> [!warning] *"Branching is easy, merging is harder."*

- **Feature Branching**: tota la feina d'una **feature** va a la **seva branch**, i s'integra a la **mainline** quan la feature està **completa**.
- **Freqüència d'integració**: la integració **freqüent** augmenta la **freqüència de merges** però **redueix la seva complexitat i risc**.

**Referència: Diapositives 7-9** → [[Branching i mainline]]

## Continuous Integration (CI)

- Els desenvolupadors fan **mainline integration** tan aviat com tenen un **healthy commit** que poden compartir — normalment **menys d'un dia de treball** — assolint punts d'integració **freqüents** amb una feature **parcialment construïda**.
- Per **amagar** la feature parcialment construïda, podem usar **feature flags**.
- La diferència entre feature branching i CI **no és** si hi ha o no una feature branch, sinó **quan integren els desenvolupadors amb la mainline**.

### Feature Branching vs Continuous Integration

| Feature Branching *(pull request)* | Continuous Integration *(GitHub Actions)* |
|---|---|
| Tot el codi d'una feature es pot avaluar per qualitat **com a unitat** | Suporta integració a **freqüència més alta** que la durada de la feature |
| El codi de la feature s'afegeix al producte quan la feature està **completa** | **Redueix el temps** per trobar **conflicts** |
| Merges **menys freqüents** | **Merges més petits** |
| | Encoratja el **refactoring** |
| | Requereix compromís amb **healthy branches** (i per tant **self-testing code**) |
| | **Evidència científica** que contribueix a un **software delivery performance** més alt |

**Referència: Diapositives 10-11** → [[CI]]

## Workflows de branching

El PDF mostra els dos diagrames clàssics: **GitFlow Workflow** i **GitHub Workflow**.

PAS A PAS del workflow (**del commit a CI**):

1. **Run tests localment**: executa i passa **tots els unit tests**.
2. **Compile code in CI**: a **cada commit**, compila al **build server**.
3. **Run tests in CI**: unit tests, integration tests, static analyses, profile performance... al **build server**.
4. **Ready for Deploy**: un **artefacte** del build server **està llest per CD**.

**Referència: Diapositives 12-16**

## Continuous Delivery / Deployment (CD)

- **Continuous Delivery**: assegura que el programari check-inat a la línia **"dev"** sempre està en un estat que **es pot desplegar**.
- **Continuous Deployment**: fa que el procés de **desplegament** sigui **totalment automatitzat**.

> [!note] Detall del PDF (exemple Azure): amb **required reviewers** al environment de **production** això és **Continuous Delivery**; **sense aprovació**, és **Continuous Deployment**.

**Referència: Diapositiva 17** → [[CD]]

## Estratègies de desplegament

Incloure un **stage de desplegament** abans del **release** que utilitza un **entorn de testing realista**.

- **Blue/green deployment**: instal·lar **dos entorns idèntics**, amb **només un live** en cada moment. Inicialment es desplega a l'entorn **offline**; si té èxit, es **canvia** a l'entorn nou i el de production original queda **idle**. El primer entorn serveix de **backup**, permetent **tornar enrere** si hi ha problema amb el nou release.
- **Canary Release**: alliberar una **actualització nova a un subconjunt d'usuaris** per testejar-lo en un entorn real **limitat**. Si té èxit, es fa **rollout** a més usuaris; si no, es **roll back**.
- **Deployment with A/B testing**: desplega **versions diferents** d'una feature per verificar **performance i usabilitat**. S'usa principalment per revisar l'**efectivitat** d'un canvi i **com el mercat hi reacciona**.
- **Feature Flags**: permet **enable o disable** una feature durant el **runtime**, per a **algun(s) o tots** els usuaris.

> [!warning] On es confonen:
> - **Blue/green** = dos **entorns** (infraestructura) — canvi d'entorn.
> - **Canary** = **subconjunt d'usuaris** — rollout gradual.
> - **A/B testing** = **dues versions** per mesurar la **reacció** — experiment.
> - **Feature flags** = **switch en runtime** — sense redeploy.

**Referència: Diapositiva 18** → [[Estratègies de desplegament]]

## Millors pràctiques CI/CD

- **Automate the build** — automatitza el build.
- **Make the build self-testing** — que el build sigui **auto-verificable**.
- **Everyone integrates to the baseline every day** — tothom integra a la baseline **cada dia**.
- **Every merge (to baseline) should be built** — cada merge s'ha de **buildar**.
- **Every bug-fix commit should come with a test case** — cada commit de bug-fix **amb un test**.
- **Keep the build fast** — mantén el build **ràpid**.
- **Test in a clone of the production environment** — testeja en una **còpia de l'entorn de production**.
- **Make it easy to get the latest deliverables** — que sigui **fàcil** obtenir els últims deliverables.
- **Everyone can see the results of the latest build** — **tothom** veu els resultats de l'últim build.
- **Implement Continuous Delivery first** — implementa **CD primer**.
- **Implement progressive delivery** (feature flags) — després, **progressive delivery**.

**Referència: Diapositiva 19**

## Serveis cloud per a CI/CD

| Model | Què és | Exemples |
|---|---|---|
| **SaaS** (Software as a Service) | Web application | — |
| **PaaS** (Platform as a Service) | Web app per **deployment** | Dynamic: **Heroku** · Static: **Netlify**, **Vercel** |
| **IaaS** (Infrastructure as a Service) | Web app per **infra management** | **AWS, Azure, Google Cloud, DigitalOcean** |

- **CI/CD**: CI: **GitHub Actions** / CD: **Azure**.

**Referència: Diapositives 20-21**

## GitHub Actions

### Conceptes

- Plataforma **CI/CD integrada a GitHub**: automatitza **build, test i deployment**.
- **Workflow**: procés automatitzat definit en **YAML** a `.github/workflows/`.
- **Event**: què el **dispara** (push, pull_request, schedule, manual...).
- **Job**: un conjunt de **steps** en un **runner fresc**. Els jobs corren **en paral·lel** per defecte, o en **seqüència amb `needs`**.
- **Action**: un **step reutilitzable** (ex. `actions/checkout`) del **Marketplace**.

### Exemple CI

- CI: **integrar sovint** i **verificar cada canvi automàticament**.
- Build process: **compile, lint, test** a cada **push** i **pull_request**.
- El resultat es mostra al **PR** com a **status check**; fes-lo **required** amb **branch protection** per mantenir una **healthy branch**.
- `strategy.matrix` **testa diverses versions en paral·lel** (ex. Node 20.x i 22.x).
- `cache: npm` **manté el build ràpid**.

### CD cap a Azure

Procés de desplegament: **dockerize** l'app, publicar la imatge a un **registry** i desplegar-la a **Azure App Service**.

- **Registry**: Azure Container Registry (`name.azurecr.io`) o GitHub Container Registry (`ghcr.io`).
- **Autenticació** Azure: publish profile, service principal o **OpenID Connect** (**OIDC**), el que Microsoft **recomana**.
- Imatge etiquetada amb **`github.sha`**: un artefacte **immutable**, així el **rollback és trivial**.
- **GitHub environments** i **Azure deployment slots** per a **staging**, **aprovacions** i **blue/green**.

### Gestió del tauler

- **GitHub Projects** té **automatitzacions built-in sense YAML**: ex. moure un item a **Done** quan un issue o PR es tanca.
- Els **built-in workflows** també poden afegir items que **coincideixin amb un filtre**.
- Fluxos **personalitzats**: un **Actions workflow** + la **Projects GraphQL API**, amb un **GitHub App token** o un **PAT**.
- `actions/add-to-project` **afegeix** issues i PRs nous al tauler.

### Resum: del commit a producció

**push/PR → CI (lint, build, test) → merge to main → Docker image (SHA) → registry → staging (slot) → optional approval → production**

| Tutorial | Goal | Trigger típic | Key actions | Result |
|---|---|---|---|---|
| Understanding GH Actions | Core concepts | Qualsevol event | actions/checkout | Workflow, job, step, runner |
| **CI** | Verificar **cada canvi** | push, pull_request | setup-node, matrix, cache | **Green status check = healthy branch** |
| **CD to Azure** | **Desplegar** l'artefacte | push to main | azure/login, webapps-deploy, Docker | App a **production** o **staging** |
| **Board flows** | Project management | issues, pull_request | add-to-project, GraphQL | Board **sincronitzada** amb la feina |

### Millors pràctiques amb Actions

- **Branch protection** i **required status checks**: **main sempre green**.
- **Pin** les actions a una **versió major** o un **SHA**, i revisa-les **periòdicament**.
- **Secrets** a *Settings → Secrets*; prefereix **OIDC** sobre **credencials estàtiques**.
- **`concurrency`** evita **dos deployments simultanis**.
- Objectiu: **CI en menys de 10 minuts** (*keep the build fast*).

**Referència: Diapositives 22-28** → [[GitHub Actions]]

## FITXA de repàs

| Element | Què és | Regla clau |
|---|---|---|
| **Continuous Design** | Disseny creat/modificat mentre es desenvolupa | Implica **TDD + Refactoring** |
| **Continuous Testing** | Tests automatitzats (self-testing code) | Funcionals **+ no funcionals** |
| **Mono vs Multi repo** | Consistència vs decoupling | Mono = refactoring · Multi = microserveis |
| **Healthy Branch** | Commit amb **checks automàtics** (build + tests) | *"Branching is easy, merging is harder"* |
| **CI** | Integrar a la mainline **< 1 dia** | La diferència és **quan** integres, no si hi ha branch |
| **CD** | Delivery = **sempre desplegable** · Deployment = desplegament **totalment automatitzat** | Aprovació = Delivery · Sense = Deployment |
| **Estratègies** | Blue/green · Canary · A/B · Flags | Entorns / usuaris / versions / switch |
| **GitHub Actions** | Workflow · Event · Job · Action | YAML a `.github/workflows/` |

## Dubtes / a revisar

- **GitFlow vs GitHub Workflow**: el PDF només en dona els **diagrames** sense text — repassar a classe o mirar la font (martinfowler.com).
- "meta: A tool for managing multi-project" — nota solta a la pàgina de Multi-Repo, **no es defineix**.
- La taula **Feature Branching vs CI** té files on la columna CI afegeix punts **sense contrapartida** — sembla intencionat (CI "guanya"), però confirmar.

---
[[_Index_ES]] · [[SCRUM]] · [[KANBAN]]
