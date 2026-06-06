---
data: 2026-05-27
assignatura: SD
tags:
  - tipus/parcial
  - assignatura/SD
---

# SD Final — Repassada ràpida

---

## 1. P2P

**Idea**: cada node (peer) fa el mateix paper, sense servidor central obligatori. Per trobar-se usen **directoris centralitzats** (Napster) o **DHT**.

**DHT**: autònom, cost $O(\log n)$, hash consistent (redistribueix mínim quan entren/surten nodes), overlay network = xarxa lògica de veïns.

**BitTorrent**: fitxer `.torrent` → Tracker → llista de Seeds (complet) i Leechers. Peces de 256KB: descàrrega paral·lela, **Rarest First** (prioritza les peces més escasses), **Choking** (els 4 millors uploaders), **Optimistic Upload** (1 aleatori cada 30s).

**Blockchain**: transaccions signades digitalment, cada bloc conté el hash de l'anterior (immodificable), **Proof of Work** per crear blocs, acceptació amb **51% de consens**.

**Java RMI**: invocar mètodes remots com si fossin locals. Interfície estén `Remote`, cada mètode llança `RemoteException`. **RMIRegistry** al port 1099: servidor fa `rebind`, client fa `lookup` → *cast* a la **interfície** (mai a la implementació!). Arguments normals → **per còpia** (cal `Serializable`). Objectes remots → **per referència** (Stub). Servidor concurrent per naturalesa → cal sincronització.

---

## 2. Docker i Microserveis

**Monòlit**: tot en un procés → si un mòdul falla, cau tot; per escalar un mòdul cal escalar-ho tot; qualsevol canvi = redeploy complet.

**Microserveis**: servei petit, independent, Single Responsibility, BD pròpia, comunicació **exclusivament per API**. Mai memòria compartida.

**Comunicació**:
- **Síncrona (REST)**: el client espera → perill de *coupling temporal* (si un cau, cau la cadena sencera).
- **Asíncrona (Kafka/RabbitMQ)**: desacoblada, esdeveniments en passat (`OrderCreated`), productor publica a *topic*, consumidor llegeix quan pot.
- **Mesh (gRPC)**: P2P entre serveis.

**Tolerància a fallades**: **Timeouts** (no esperar indefinidament) → **Retries** (amb cura, han de ser idempotents) → **Circuit Breaker** (talla el circuit si un servei falla repetidament) → **Fallback** (resposta degradada).

**API Gateway**: punt d'entrada únic → routing, autenticació, rate limiting, logs, agregació.

**Docker vs VM**: contenidor comparteix el Kernel de l'host (lleuger, MB, arrenca en ms); VM emula hardware complet (pesat, GB, arrenca en 30-45s). Docker = aïllament menor però molt més eficient.

**Kubernetes**: orquestra contenidors → scheduling, self-healing, escalat elàstic, load balancing.

**Fal·làcies**: mai assumir que la xarxa és fiable, la latència zero o l'ample de banda infinit.

---

## 3. Hadoop

**Problema**: copiar dades de la xarxa cap als nodes de computació és el **coll d'ampolla** amb Big Data. Solució de Hadoop: **moure el codi cap a les dades**, no al revés.

**Teorema CAP** (saber-lo de memòria): un sistema distribuït només pot tenir **2 de 3**:
- **C**onsistència, **A**vailabilitat, **P**artition Tolerance.
- En entorns reals P és **obligatòria** → has de triar entre **CP** o **AP**.

**HDFS**: fitxers dividits en blocs de **64/128 MB**, replicats a **3 nodes**. Optimitzat per fitxers grans i lectures seqüencials (no accés aleatori).
- **NameNode** (mestre): guarda les metadades (on és cada bloc).
- **DataNode** (esclau): guarda els blocs físics.
- **Secondary NameNode**: manteniment de metadades. **NO és un backup actiu**.

**MapReduce**: client envia `.jar` → **JobTracker** planifica i consulta el NameNode → **TaskTrackers** executen les tasques. Les dades es llegeixen **directament dels DataNodes** (no pel NameNode).

**WordCount**: Map → emet `(paraula, 1)` per cada paraula → Shuffle & Sort → Reduce suma tots els 1 d'una mateixa paraula.

**Fallades**: reassignació automàtica al node amb rèplica. Node lent → **execució especulativa** (còpia paral·lela, guanya el primer).

---

## 4. Spark

**Problema de MapReduce**: escriu resultats intermedis a disc en cada pas → molt lent per algorismes iteratius (ML), consultes repetides o streaming.

**Solució Spark**: **RDD** (Resilient Distributed Dataset) en **memòria distribuïda**. Tolerància a fallades via **lineage** (recorda com es va construir, no replicant).

**Arquitectura**: **Driver** (orquestra) + **Workers** (executen, cada un té un Executor amb Cache + Tasks) + **Cluster Manager** (assigna recursos). El Driver crea el `SparkContext` (`sc`).

**RDD**: immutable, traçable, paral·lel. Es crea des d'una col·lecció, d'un altre RDD, o llegint d'HDFS.

**Transformacions** (*lazy*, no s'executen fins que hi ha una acció):
- `map`, `filter`, `flatMap`, `distinct`

**Accions** (força l'execució de tot el graf):
- `reduce`, `collect` (**COMPTE**: ha de cabre a memòria del driver!), `take(n)`, `takeOrdered(n)`

**Variables compartides**:
- **Broadcast**: driver envia dades de només lectura als workers eficientment.
- **Accumulators**: workers només escriuen, driver llegeix el resultat. **Només garantits en Accions**, no en Transformacions.

---

## 5. Web Services

**REST**: estil (no protocol) sobre HTTP. **Stateless** (cada petició és autocontinguda), URIs com directoris, dades en JSON o XML.

**Mètodes HTTP**:
- **GET**: llegir (idempotent). **POST**: crear (NO idempotent). **PUT**: actualitzar (idempotent). **DELETE**: eliminar (idempotent).

**Caché**: `Cache-Control` amb `max-age` o `Expires`. Condicionals:
- *Time-based*: `Last-Modified` + `If-Modified-Since` → **304 Not Modified**.
- *Content-based*: `ETag` + `If-None-Match`.

**Sessions** (HTTP és stateless per defecte):
- Camps ocults (insegur), Cookies (`Set-cookie`), URL Rewriting. → Sempre fer expirar els IDs, mai enviar info sensible.

**JWT**: Header (algoritme) + Payload (dades) + Signature (signat amb clau privada). Generat pel servidor, enviat al client, el client l'inclou a la capçalera `Authorization` de cada petició. Les dades estan en Base64, **no xifrades** (només signades).

**Asincronia**:
- **AJAX**: peticions HTTP no bloquejants (`XMLHttpRequest`).
- **WebSockets**: full-duplex sobre TCP. Handshake HTTP inicial → protocol propi al port 80. Per xats, jocs en viu, etc.
