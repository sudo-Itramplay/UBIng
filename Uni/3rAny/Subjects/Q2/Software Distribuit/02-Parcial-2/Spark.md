
## 1. Introducció i Motivació de Spark

### Intenció - Perquè es fa Spark?

L'evolució de l'anàlisi de dades massives (_Big Data_) ha requerit el disseny de nous models de programació distribuïda que superin les limitacions dels frameworks tradicionals (MapReduce), garantint alhora la tolerància a fallades.

### Motivació i Limitacions de MapReduce

L'objectiu fonamental de Spark és suportar una gamma més àmplia d'aplicacions que el model MapReduce, mantenint el seu sistema automàtic de tolerància a fallades. MapReduce esdevé altament ineficient per a programes de múltiples passades que no requereixen d'un intercanvi massiu de dades entre múltiples operacions paral·leles.

Aquestes ineficiències afecten directament tasques molt comunes en Big Data, tals com:

- **Algorismes Iteratius:** Inclouen la gran majoria de fluxos de treball d'Aprenentatge Automàtic (_Machine Learning_) i els algorismes de grafs.

- **Mineria de Dades Interactiva:** Escenaris on un usuari carrega un conjunt de dades en memòria mitjançant un _cluster_ i hi realitza consultes repetides.

- **Aplicacions d'Streaming:** Sistemes que requereixen mantenir i actualitzar un estat agregat de les dades al llarg del temps.

---

## 2. Característiques Fonamentals i Arquitectura Spark vs. Hadoop

### Intenció

Comprendre la diferència arquitectònica en la gestió del flux de dades i de l'emmagatzematge intermedi entre els frameworks clàssics basats en disc i els moderns basats en memòria distribuïda.

> **Referència:** Diapositives 3 i 4.

### Spark vs. Hadoop (MapReduce)

Mentre que MapReduce es basa en fer córrer una sèrie de tasques independents on cadascuna d'elles llegeix obligatòriament d'un disc físic (com HDFS) i torna a escriure-hi els resultats intermedis, Spark optimitza radicalment aquest procés. El fet de llegir i escriure les dades de forma replicada a cada pas computacional afegeix un cost de latència i d'E/S (_I/O_) molt significatiu.

Spark introdueix una abstracció central anomenada **Resilient Distributed Datasets (RDD)**, la qual es manté resident en la memòria distribuïda del _cluster_ entre les diferents peticions. Això elimina la necessitat de persistir i replicar estats intermedis a disc de forma contínua. En lloc de dependre de la replicació física per a la tolerància a fallades, Spark fa servir la **traçabilitat** (_lineage_): cada RDD recorda exactament com va ser construït a partir d'altres _datasets_ primigenis o operacions prèvies (com `map`, `join` o `groupBy`), permetent recomputar de forma aïllada i sota demanda qualsevol fragment de dades perdut.

A nivell de construcció tecnològica, Spark està implementat nativament utilitzant el llenguatge **Scala**, i ofereix de base APIs completament funcionals per a **Python** i **Java**.

---

## 3. Arquitectura del Cluster: Driver i Workers

### Intenció

Estudiar la topologia mestre-esclau de l'entorn d'execució de Spark i com es distribueixen les tasques i el cicle de vida de les aplicacions de programari distribuït.

> **Referència:** Diapositives 5 i 6.

### Components de la Topologia

L'execució de qualsevol codi Spark requereix el desplegament coordenat de dos tipus de programes diferenciats:

- **Driver Program (Programa Driver):** És el procés central que s'executa en un node passarel·la (_gateway node_). S'encarrega d'orquestrar l'aplicació i de controlar el flux d'execució general.

- **Worker Nodes (Nodes Treballadors):** Són els nodes encarregats d'executar les tasques reals de computació. Es poden executar directament en nodes dedicats del _cluster_ o instanciar-se mitjançant fils locals (_local threads_). Cada Worker allotja un procés **Executor** que gestiona una **Cache** de memòria i executa diferents unitats de treball anomenades **Tasks** (Tasques). Els objectes RDD es troben fragmentats i distribuïts de forma horitzontal al llarg de la memòria d'aquests workers.

Entre el Driver i els Workers actua el **Cluster Manager**, que s'encarrega de l'assignació física de recursos.

### L'Objecte SparkContext

Abans de realitzar qualsevol computació, un programa Spark ha d'instanciar obligatòriament un objecte **SparkContext**. Aquest objecte actua com el punt d'entrada principal de l'aplicació i compleix les següents funcions crítiques:

- Indica formalment a l'aplicació Spark com i a on s'ha d'accedir al _cluster_ de nodes.

- S'utilitza de forma explícita mitjançant la variable de referència `sc` per a la creació inicial dels RDDs.

- El seu paràmetre configuatiu anomenat `master` determina de manera unívoca el tipus i la mida de la topologia del _cluster_ utilitzat.

---

## 4. L'Abstracció RDD (Resilient Distributed Datasets)

### Intenció

Analitzar formalment el funcionament intern, les propietats de disseny de la col·lecció de dades distribuïda de Spark i el seu model de particionament.

> **Referència:** Diapositives 7, 8 i 11.

### Propietats Core de l'RDD

L'RDD és la principal abstracció de dades dins de l'ecosistema Spark. Les seves característiques fonamentals de disseny programàtic són:

- **Immutabilitat:** Un cop un RDD ha estat construït, el seu estat és absolutament immutable i no pot ser modificat.

- **Traçabilitat Integrada:** Monitoritza i enregistra tota l'activitat i transformacions que s'apliquen sobre ell, permetent recomputar eficientment qualsevol pèrdua parcial o total de dades en cas d'avaria en algun node.

- **Execució Paral·lela:** Permet l'execució d'operacions concurrents i paral·leles sobre col·leccions d'elements distribuïts.

Un RDD pot ser construït seguint tres mecanismes principals: paral·lelitzant una col·lecció de dades en memòria que ja existeixi en el programa driver, transformant un RDD preexistent, o mitjançant la lectura directa de fitxers emmagatzemats en un sistema de fitxers distribuït (com HDFS o qualsevol altre emmagatzematge compatible).

### Particionament i Paral·lelisme

El programador té la potestat d'especificar explícitament el nombre de **particions** en què es divideix lògicament un RDD. Com a regla general d'arquitectura de programari distribuït, un **major nombre de particions es tradueix en un major nivell de paral·lelisme** potencial. Això obstant, en fase de disseny cal equilibrar acuradament aquesta relació tenint en compte el nombre de nodes físics reals i els fils de processament (_threads_) disponibles al sistema.

### Mecanismes de Caching

Un RDD es pot fer persistent de forma explícita a la memòria dels workers invocant els mètodes `.persist()` o `.cache()` sobre el propi objecte. Aquesta memòria cache manté la propietat de tolerància a fallades: si qualsevol fragment o partició es perd, l'arquitectura el recalcula automàticament de manera transparent fent servir el seu historial de transformacions original.

---

## 5. Operacions sobre RDDs: Transformacions i Accions

### Intenció

Classificar els dos tipus d'operacions en Spark, entenent el paradigma d'avaluació mandrosa (_lazy evaluation_) i les funcions de transformació i agregació de dades.

> **Referència:** Diapositives 8, 9, 10 i 12.

### Transformacions i Avaluació Mandrosa

Les **Transformacions** s'encarreguen de crear nous conjunts de dades distribuïts agafant com a origen un RDD preexistent. Operen sota el paradigma de l'**avaluació mandrosa (_lazy evaluation_)**, cosa que significa que els resultats de les funcions no es computen de manera immediata quan es declaren al codi. En el seu lloc, Spark construeix i guarda internament el graf o conjunt de transformacions ordenades que caldrà aplicar al dataset. Aquesta estratègia permet:

- Optimitzar de forma global els càlculs i els plans d'execució necessaris abans d'executar-los.

- Facilitar la recuperació automàtica davant de caigudes del sistema o de la presència de workers lents (_stragglers_).

Arquitectònicament, es pot conceptualitzar una transformació com una **recepta** conceptual per a obtenir un resultat final.

| Transformation | Description                                                                                                       |
| -------------- | ----------------------------------------------------------------------------------------------------------------- |
| `map(func)`    | Retorna un nou dataset distribuït format en passar cada element de la font original a través d'una funció `func`. |

|
| `filter(func)` | Retorna un nou dataset format seleccionant només aquells elements de la font on la funció `func` retorna l'estat _true_.

|
| `distinct([numTasks])` | Retorna un nou dataset distribuït que conté els elements únics (sense duplicats) de la font original.

|
| `flatMap(func)` | Similar a `map`, però cada element d'entrada es pot mapejar a 0 o més elements de sortida (la funció `func` ha de retornar una seqüència `Seq` en lloc d'un únic ítem).

|

### Accions

Les **Accions** són operacions que forcen a Spark a executar de manera efectiva tot el graf de transformacions acumulat sobre el conjunt de dades. Són l'únic mecanisme disponible per tal d'enviar o extreure resultats cap a l'exterior del framework (com ara retornar les dades al programa driver o escriure-les a un sistema de fitxers).

| Action           | Description                                                                                                                                                                                                     |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `$reduce(func)$` | Agrega els elements d'un dataset mitjançant una funció `func`. Aquesta funció pren dos arguments i en retorna un de sol; ha de ser commutativa i associativa per poder ser computada correctament en paral·lel. |

|
| `take(n)` | Retorna una matriu (_array_) que conté els primers $n$ elements del dataset.

|
| `collect()` | Retorna absolutament tots els elements del dataset en forma de matriu al programa principal.

<br>

<br>**AVÍS D'EXAMEN:** Cal assegurar-se prèviament que la mida del volum de dades hi cabrà físicament en la memòria del _driver program_ per evitar un col·lapse del sistema.

|
| `takeOrdered(n, key=func)` | Retorna $n$ elements del dataset ordenats de manera ascendent o segons s'especifiqui en una funció de clau (`key=func`) opcional.

|

### Cicle de Vida d'un Programa Spark

L'execució d'una aplicació en Spark descriu una seqüència de quatre fases ben definides:

1.  **Creació:** Es construeixen els RDDs originals a partir de fonts de dades externes o es paral·lelitza una col·lecció resident en la memòria del programa driver.

2.  **Transformació:** S'apliquen de manera mandrosa seqüències de transformacions sobre les dades per anar generant nous RDDs intermedis.

3.  **Persistència:** Es marquen de manera opcional aquells RDDs que es volen retenir en memòria mitjançant operacions de _caché_ per a optimitzar futures reutilitzacions.

4.  **Execució:** Es llança una acció final que executa de forma efectiva totes les computacions distribuïdes en paral·lel, produint els resultats desitjats pel flux de treball.

---

## 6. Model de Comunicació: Variables Compartides

### Intenció

Entendre la gestió de variables globals en un sistema distribuït de memòria compartida virtual, els problemes derivats dels tancaments (_closures_) de codi i les solucions de readifusió i acumulació.

> **Referència:** Diapositives 13 i 14.

### El Problema dels Closures en els Workers

Spark crea de manera completament automàtica **tancaments (_closures_)** quan s'envien funcions cap als workers (com per exemple en invocar un `map`). Aquests _closures_ encapsulen les funcions juntament amb el seu propi entorn de variables, incloent-hi qualsevol variable de caràcter global que estigui sent utilitzada pels nodes treballadors.

El model de disseny està pensat perquè **no es requereixi cap mena de comunicació de dades directa entre workers** durant l'execució d'aquestes funcions. Això comporta un problema d'estat inherent: **els canvis aplicats a les variables globals dins dels workers són completament locals i no es retornen mai ni es propaguen cap al programa driver** o cap a la resta de workers. Un exemple típic d'aquest problema és intentar incrementar un comptador global dins d'un worker amb l'objectiu de calcular el total global de dades processades de tot el clúster.

### Solucions Arquitectòniques

Per solucionar aquesta mancança de sincronització, Spark proveeix dos tipus específics de variables compartides:

- **Variables de Redifusió (Broadcast Variables):** Dissenyades per enviar de manera altament eficient grans volums de dades de **només lectura** des del node driver cap a cadascun dels workers del clúster. Es guarden de manera persistent en la memòria local dels nodes treballadors per a ser utilitzades de manera repetida en una o diverses operacions successives, evitant retransmissions ineficients.

- **Variables Acumuladores (Accumulators):** Dissenyades específicament per realitzar operacions d'agregació associativa i commutativa de valors numèrics (suporten tipus de dades com _integers_, _double_, _long_ i _float_) des dels diferents workers cap al driver. Tenen una restricció d'accés asimètrica: **només el programa driver té permís per llegir el valor final de l'acumulador**. Per als workers, l'acumulador és un element estrictament de **només escriptura**. Es poden declarar tant en accions com en transformacions, recordant però una regla de disseny crítica per a exàmens: **només l'execució d'accions garanteix de manera fefaent el processament correcte dels acumuladors**. Un comportament mandrós en una transformació pot provocar que l'acumulador no s'incrementi fins que no s'invoqui una acció sobre aquell flux d'execució.
