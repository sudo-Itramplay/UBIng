## 1. Problemàtica dels Sistemes Distribuïts Tradicionals

### Intenció

La programació i gestió de sistemes distribuïts sota els paradigmes tradicionals presenta una complexitat inherent molt elevada a causa de factors físics i temporals de la xarxa. Quan escalem els sistemes per processar grans volums d'informació, els models clàssics fallen en la gestió dels recursos.

### Definicions i Conceptes de Referència

- **Sincronització de Dades**: L'intercanvi de dades entre nodes independents requereix protocols estrictes de sincronització que afegeixen sobrecàrrega (_overhead_) al sistema.
    
- **Restriccions d'Amplada de Banda**: La transferència de dades a través de la xarxa està limitada per la capacitat física dels canals de comunicació.
    
- **Dependències Temporals**: La coordinació de l'ordre d'execució de tasques paral·leles i concurrents esdevé altament complexa de gestionar.
    
- **Fallades Parcials**: En un entorn distribuït, la probabilitat que un o diversos nodes caiguin és alta; gestionar aquestes fallades sense aturar el sistema complet és un dels grans reptes de l'enginyeria.
    
![[Pasted image 20260518182956.png]]
### L'Emmagatzemament Clàssic i el Coll d'Ampolla

Tradicionalment, les dades en un sistema distribuït es guarden de forma centralitzada en una unitat de dades en xarxa (com un NAS o un servidor de fitxers compartit). En el moment en què es requereix realitzar una computació, les dades es copien des d'aquesta unitat central cap als diferents nodes de computació.

```
[ Unitat de dades en xarxa ] --( Còpia de dades per xarxa )--> [ Nodes de Computació ]
```

Aquest enfocament és funcional i eficient únicament quan treballem amb una quantitat relativament limitada de dades.

### El Problema del Big Data

Els sistemes moderns han de processar volums massius d'informació diàriament. Sota aquest escenari, l'acció de transferir i proporcionar les dades als processadors a través de la xarxa ha esdevingut l'autèntic **coll d'ampolla** dels sistemes distribuïts actuals. 
	Per tant, es fa totalment necessària una nova aproximació arquitectònica a la distribució del sistema.

---

## 2. Requeriments i Fonaments del Nou Paradigma

### Intenció

Per solucionar el coll d'ampolla del Big Data, qualsevol nova arquitectura de programari distribuït d'alta capacitat ha de complir de manera nativa amb una sèrie de requeriments de robustesa, consistència i escalabilitat.

### Requeriments del Sistema

- **1.-Robustesa a Fallades Parcials**: 
	- El sistema ha de ser resilient. No es pot permetre en cap cas que tot el sistema caigui completament a causa de la fallada d'uns quants components o nodes.
    
- **2.-Recuperació i Tolerància a la Pèrdua de Dades**:
    
    - Si un component del sistema falla, la seva càrrega de treball s'ha d'assumir de manera automàtica i transparent per una altra unitat del sistema.
        
    - Sota cap concepte es pot permetre la pèrdua de dades com a conseqüència d'una fallada de maquinari o programari.
        
- **3.-Recuperació Calenta d'un Component**: 
	- Si un node que ha fallat es recupera, ha de ser capaç d'ajuntar-se de nou al clúster de forma dinàmica, sense que sigui necessari reiniciar el sistema sencer.
    
- **4.-Consistència d'Execució**: 
	- La fallada de qualsevol component durant l'execució d'un treball (_job_) no ha d'afectar mai el resultat o la sortida final d'aquest treball.
    
- **5.-Escalabilitat**:
    
    - **Escalabilitat en Càrrega**: Afegir més càrrega de treball al sistema no ha de provocar una fallada general, sinó un descens controlat i proporcional en el rendiment global dels treballs individuals.
        
    - **Escalabilitat en Recursos**: L'increment de recursos físics (afegir més nodes al clúster) ha de repercutir directament en un augment equivalent de la capacitat de càrrega del sistema.
        

### Teorema de CAP

En l'àmbit dels sistemes distribuïts, el Teorema de CAP és una veritat de disseny fonamental que postula que un sistema distribuït només pot garantir simultàniament dues de les següents tres propietats:

1. **Consistència (Consistency)**: Tota operació de lectura ha de rebre l'escriptura més recent o, en el seu defecte, un error.
    
2. **Disponibilitat (Availability)**: Cada petició rebuda per un node actiu (no caigut) en el sistema ha de retornar una resposta obligatòriament (sense garantia de si conté l'escriptura més recent).
    
3. **Tolerància a Particions (Partition Tolerance)**: El sistema continua funcionant i operant encara que hi hagi pèrdues de paquets o retards en les comunicacions entre els nodes.
    
![[Pasted image 20260518183310.png]]

>[!important] Fallada de xarxa
>En cas que hi hagi una fallada en la xarxa, s’ha d’escollir entre consistència o disponibilitat (o rebre una dada no actualitzada o esperar per assegurar-se que hi ha consistència)
### Error Comú de Disseny

Un error típic d'estudiant és creure que es pot dissenyar un sistema Big Data que sigui completament consistent, sempre disponible i tolerant a particions (CA+P). 

En entorns reals amb milers de nodes connectats per xarxa, les fallades de xarxa són inevitables. Per tant, la tolerància a particions (P) és un requisit obligatori. En cas d'una fallada en la xarxa, l'enginyer ha d'escollir de manera estricta entre **Consistència (CP)** o **Disponibilitat (AP)**; és a dir, o es rep una dada potencialment no actualitzada o es bloqueja la petició esperant assegurar la consistència.

---

## 3. Arquitectura d'Apache Hadoop

### Intenció

Apache Hadoop sorgeix per donar resposta pràctica als requeriments anteriors, basant-se en el treball d'enginyeria publicat per Google a principis dels anys 2000 per al seu motor de cerca. L'objectiu de Hadoop és oferir una plataforma escalable, robusta i fiable.

### La Idea Bàsica de Disseny

La idea disruptiva de Hadoop consisteix a **distribuir les dades tan bon punt aquestes es guarden en el sistema**. En lloc de moure les dades cap a la computació, Hadoop mou el codi de computació cap on resideixen les dades.

### Conceptes Clau d'Arquitectura

- **Abstracció d'Alt Nivell**: Les aplicacions es programen abstretes dels detalls de baix nivell com la gestió de la xarxa, el control de dependències o les sincronitzacions complexes.
    
- **Minimització de Comunicacions**: Els nodes es comuniquen entre ells tan poc com sigui possible durant l'execució per evitar saturar la xarxa.
    
- **Distribució a Priori**: Les dades es reparteixen de manera anticipada entre les diferents màquines de l'entorn.
    
- **Localització de la Computació**: La computació s'executa, sempre que sigui possible, en el node físic exacte on estan emmagatzemades les dades a processar.
    
- **Replicació de Dades**: Per assegurar l'alta disponibilitat i la fiabilitat de la informació, les dades es repliquen múltiples vegades al llarg del clúster.
    

### Components del Clúster

Un clúster de Hadoop està compost per un conjunt de màquines individuals de propòsit general denominades **nodes**. El clúster pot escalar des d'un únic node de desenvolupament fins a milers de nodes en producció. A nivell de programari, l'ecosistema es fonamenta en dos components bàsics indispensables:

1. **Hadoop Distributed File System (HDFS)**: El sistema de fitxers distribuït encarregat de l'emmagatzemament.
    
2. **MapReduce Software Framework**: L'entorn de programari encarregat de la computació distribuïda.
    

> _Nota_: Tot i que l'ecosistema de Hadoop inclou moltes altres eines com Pig, Hive, HBase, Flume, Oozie, Sqoop o Mahout, el nucli del temari se centra exclusivament en HDFS i MapReduce.

---

## 4. El Sistema de Fitxers Distribuït: HDFS

### Intenció

Entendre el funcionament de l'HDFS és crucial per als exàmens, especialment com gestiona la divisió de fitxers i la seva topologia de replicació per aconseguir tolerància a fallades catastròfiques de maquinari.

### Mecànica d'Emmagatzemament i Blocs

L'HDFS és un sistema de fitxers virtual escrit en Java que s'executa posicionant-se per sobre del sistema de fitxers natiu de cada sistema operatiu del node (com ext4 o NTFS).

Quan un fitxer es carrega a l'HDFS, aquest es divideix automàticament en porcions de mida fixa anomenades **blocs**, la mida típica dels quals és de **64 MB o 128 MB**.
	- Les Tasques de mapping treballen en porcions petites de dades (1 bloc)

Aquests blocs es distribueixen de forma asíncrona i immediata entre les diferents màquines (DataNodes) del clúster. Diferents blocs que pertanyen a un mateix fitxer s'emmagatzemen intencionadament en diferents màquines per maximitzar el paral·lelisme.

### Ràtio de Replicació per Defecte

Per defecte, cada bloc de dades es replica en **3 màquines diferents** del clúster. Això garanteix que, davant la caiguda simultània de dos nodes que continguin el mateix bloc, la informació romangui accessible al tercer node sense corrupció.

### Disseny i Optimització de l'HDFS

L'HDFS presenta unes característiques de disseny molt particulars que solen preguntar-se en els exàmens teòrics:

- **Fitxers Grans**: Està optimitzat per treballar millor amb un nombre moderat de fitxers de gran mida (milions de fitxers de 100 MB o superiors). No està dissenyat per gestionar milers de milions de fitxers petits a causa de la saturació de la memòria de metadades.
    
- **Lectures Consecutives**: Està altament optimitzat per a fitxers llargs i operacions d'accés seqüencial a les dades (_streaming de dades_), penalitzant l'accés aleatori (_random access_).
    

### Serveis de l'Arquitectura HDFS (Master/Slave)

L'arquitectura d'emmagatzemament utilitza un patró mestre-esclau molt definit amb els següents serveis en execució:

- **NameNode (Mestre)**: És el node crític del sistema. S'encarrega de mantenir i gestionar de forma centralitzada totes les metadades de l'HDFS. El NameNode sap quins blocs formen un fitxer determinat i en quines màquines físiques estan emmagatzemats exactament.
    
- **Secondary NameNode**: Realitza tasques periòdiques de manteniment de la imatge de metadades de l'HDFS per alleugerir la càrrega del NameNode principal. **Atenció**: No funciona en cap cas com un servidor de _backup_ actiu o de recuperació immediata (_failover_).
    
- **DataNode (Esclaus)**: Són els nodes encarregats de l'emmagatzemament físic pur. S'ocupen de desar i llegir els blocs de dades reals a les unitats de disc locals segons les ordres del mestre.


![[Pasted image 20260518184654.png]]


![[Pasted image 20260518184632.png]]
### Interacció amb l'HDFS via API de Línia de Comandes

Per interactuar amb el sistema de fitxers s'empra el comando d'alt nivell `hadoop fs`. Les dues instruccions bàsiques d'ingrés i extracció d'informació són:

- **Còpia de local cap a l'HDFS**:

    ```bash
    hadoop fs -copyFromLocal local_dir/ hdfs_dir
    
    ```

### Característiques del Framework

- **Paral·lelització automàtica**: Distribueix la feina entre múltiples nodes sense intervenció del programador.
    
- **Abstracció completa**: Amaga de l'enginyer tota la infraestructura de baix nivell de la xarxa, permetent programar en llenguatges com Java o Python.
    
- **Eines de Monitorització**: Proporciona telemetria integrada per auditar el progrés de les tasques en temps real.
    

### Tractament Robust de Fallades en MapReduce

Hadoop inverteix un gran esforç arquitectònic en la gestió de fallades, prioritzant sempre la **Consistència** i el **Tractament de fallades** per sobre de la disponibilitat immediata de recursos:

- **Caiguda d'un Node de Computació**: El programa Màster detecta la caiguda del node i reassigna immediatament la tasca de mapping o reducció a un altre node del clúster que tingui una rèplica d'aquest mateix bloc de dades.
    
- **Aïllament de Reinici**: Tornar a engegar o reassignar una tasca fallida és una operació independent que no implica cap mena de comunicació ni alteració dels altres nodes que segueixen treballant de forma normal amb les seves porcions de dades.
    
- **Reincorporació Dinàmica**: Si el node caigut es reinicia o es recupera el seu enllaç, s'afegeix de forma completament automàtica al clúster i se li comencen a assignar noves tasques sense necessitat d'intervenció manual.
    
- **Execució Especulativa per Nodes Lents**: Si el mestre detecta que un node s'està executant amb un rendiment degradat o anormalment lent, pot aixecar una instància paral·lela i idèntica d'aquesta mateixa tasca en un altre node alternatiu. El primer node que finalitzi l'execució lliurarà els seus resultats al sistema, i l'altra instància serà descartada.
    




---

## 6. Anatomia d'un Clúster Hadoop i Execució d'un Treball

### Intenció

És fonamental conèixer quines entitats de programari interactuen quan un client llança una petició de computació (_job_) cap al clúster de producció.

### Flux de Funcionament d'un Job

Quan una aplicació client desitja realitzar una lectura de dades o executar un processament, el cicle de vida es divideix en els següents passos ordinals:

1. **Petició del Client**: El Client de Hadoop envia el codi font compilat (un fitxer `.jar` en Java) juntament amb la configuració de l'entorn (un fitxer `.xml`) cap al clúster.
    
2. **Planificació pel JobTracker (Mestre)**: El servei **JobTracker** (situat al Master Node) rep la petició del client, avalua el volum de dades, determina el pla d'execució òptim i comença a distribuir les tasques individuals. Per fer-ho de forma eficient, es comunica prèviament amb el **NameNode** per obtenir la informació exacta de localització (_file location info_) dels blocs que formen els fitxers d'entrada.
    
3. **Execució en els TaskTrackers (Esclaus)**: El JobTracker assigna les tasques de Map i Reduce individuals als serveis **TaskTracker** de cada node esclau (_Slave Node_). El TaskTracker és el responsable directe d'instanciar, executar i monitorar les tasques de Map i Reduce dins d'aquella màquina específica.
    
4. **Lectura Directa de dades en l'HDFS**: Per a l'execució de la tasca o quan una aplicació client simplement requereix fer una lectura d'un fitxer (per exemple, el fitxer `/user/eloi/bar`):
    
    - El client demana al NameNode la llista de blocs i la seva ubicació.
        
    - Un cop obtinguda la metadada, el client o el procés de mapping es comunica **directament amb els DataNodes físics** pertinents (per exemple, els nodes N2, N1 o N3) per extreure o escriure la informació. Això evita que el tràfic de dades massiu hagi de passar pel NameNode mestre, evitant la seva saturació.



![[Pasted image 20260518184841.png]]
![[Pasted image 20260518184854.png]]

---

## 7. MapReduce: L'Algorisme WordCount

### Intenció

L'algorisme de comptar paraules és l'exemple acadèmic per excel·lència (_Hello World_) dels sistemes distribuïts Big Data, utilitzat per il·lustrar la potència de la paral·lelització en MapReduce.

### El Repte del Volum


Comptar la freqüència d'aparició de cada paraula en un text de dimensions colossals és una tasca inviable de realitzar de manera seqüencial en una sola màquina. Tot i així, és un problema conceptualment senzill de paral·lelitzar si distribuïm adequadament els fragments del text al llarg del clúster.

### Desenvolupament de les Fases de WordCount

1. **Descomposició de Dades**: Hadoop s'encarrega de rebre el fitxer de text de l'usuari i descompondre'l de forma totalment automàtica en blocs de l'HDFS.
    
2. **Fase Map**: Cada node esclau agafa un bloc de text i processa l'entrada línia a línia. Per cada paraula que troba, emet una parella clau-valor simple on la clau és la paraula en si i el valor és el número 1 de forma individual (per exemple, `(paraula, 1)`), sense realitzar sumes en aquest punt.
    
3. **Fase de Shuffle & Sort**: El motor de Hadoop agrupa totes les paraules idèntiques provinents de tots els mapatges, ordenant el llistat per la clau (la paraula).
    
4. **Fase Reduce**: La funció Reduce rep com a entrada la paraula i un llistat amb tots els valors unitaris associats (ex: `(paraula, [1, 1, 1, 1])`). La funció procedeix a executar l'operació d'agregació sumant tots els valors per obtenir el recompte absolut final d'aquella clau en tot el fitxer.
    
