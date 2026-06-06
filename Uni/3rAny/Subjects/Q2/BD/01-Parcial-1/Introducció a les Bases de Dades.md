## 1. Conceptes Fonamentals i Propietats

Una **Base de Dades (BD)** es defineix com una col·lecció de dades relacionades que tenen un significat implícit i poden ser enregistrades. 

- Les **dades** són fets coneguts que es poden guardar (noms, telèfons, transaccions).


Tota base de dades posseeix tres propietats clau:

- **Representació del món real:** Reflecteix un aspecte de la realitat, anomenat _miniworld_ o _universe of discourse_.
	- També reflecteixen el seu canvi
    
- **Col·lecció lògicament coherent:** Les dades tenen un sentit inherent i relacions entre elles; no és un conjunt aleatori.
    
- **Dissenyada per a un propòsit específic:** Es construeix per a uns usuaris i aplicacions concrets.
    

### DBMS

Un **DBMS** és un sistema informatitzat que permet als usuaris **crear i mantenir** una base de dades. És el programari que actua com a interfície entre les dades i els usuaris o les aplicacions.

### Funcions Clau del DBMS

Un DBMS complet ha de ser capaç de realitzar les següents tasques fonamentals:

- **Definir (Defining):** Especificar els tipus de dades, les estructures i les restriccions d'integritat que han de complir.

- **Construir (Constructing):** Gestionar el procés d'emmagatzemar físicament les dades en un mitjà d'emmagatzematge controlat pel programari.

- **Manipular (Manipulating):** Permetre funcions com la consulta (_query_) per recuperar dades específiques, l'actualització de la informació i la generació d'informes.

- **Compartir (Sharing):** Facilitar que múltiples usuaris i programes tinguin accés a les dades de forma simultània i segura.

- **Protegir (Protecting):** Garantir la seguretat del sistema contra accessos no autoritzats i la protecció de les dades davant de fallades de maquinari o programari.

- **Mantenir (Maintaining):** Permetre l'evolució del sistema a llarg termini per adaptar-se a nous requeriments o canvis en l'estructura.


El **DBMS (Database Management System)** és el sistema informàtic que permet definir, construir, manipular, compartir, protegir i mantenir una BD. 

>[!info] BD i DBMS
>El conjunt de la BD i el DBMS s'anomena **Sistema de Base de Dades**.

![[Pasted image 20260214113857.png]]

### Exemple: La Base de Dades UNIVERSITAT

Per gestionar l'entorn acadèmic, l'estructura s'organitza en fitxers interconnectats:
- **STUDENT:** Dades dels alumnes (Nom, número d'estudiant, classe, especialitat).
- **COURSE:** Detalls de les assignatures (Nom, número de curs, crèdits, departament).
    
- **GRADE_REPORT:** Notes dels estudiants (Número d'estudiant, ID de secció, nota).
    
- **PREREQUISITE:** Requisits previs per a cada curs.
    

> [!abstract] Relació
>  Les dades no estan aïllades. Per exemple, la nota d'en "Smith" a l'assignatura de "Bases de Dades" vincula els registres dels fitxers `STUDENT`, `SECTION` i `GRADE_REPORT`.
#### Manipulació de la Base de Dades

La interacció amb la BD es divideix en dues accions principals que s'han d'especificar amb precisió en el llenguatge de consulta del DBMS:

1. **Consultes (Queries):** Recuperació de dades específiques.
    
    - _Exemple:_ "Llistar els prerequisits del curs de Bases de Dades".
    
2. **Actualitzacions (Updates):** Modificació de l'estat de la BD per reflectir canvis en el món real.
    - _Exemple:_ "Canviar la classe de l'estudiant Smith a segon curs" o "Introduir un 'A' per a Smith".
    - 
---

## 2. Disseny i Desenvolupament de la BD

El camí des d'una idea fins a una BD funcional segueix quatre fases crítiques:

1. **Anàlisi de Requeriments:** Documentar detalladament què necessita el sistema.
    
2. **Disseny Conceptual:** Creació d'un model (com l'Entitat-Relació) fàcil de mantenir i entendre.
    
3. **Disseny Lògic:** Expressar el disseny conceptual en el model de dades d'un DBMS comercial (normalment relacional).
    
4. **Disseny Físic:** Especificar com s'emmagatzemaran i s'accediran les dades a nivell de maquinari.

---
## 3. L'Enfocament de Base de Dades vs. Fitxers

A diferència del processament de fitxers tradicional, on cada aplicació defineix els seus propis fitxers, l'enfocament de BD centralitza la gestió.

### Característiques Distintives

1. **Naturalesa auto-descriptiva:** El sistema conté la BD i el seu propi **catàleg**, on es guarden les **meta-dades** (definició d'estructures, tipus i restriccions).
    
2. **Independència de dades:**
    
    - **Independència Programa-Dades:** L'estructura de les dades es guarda al catàleg, no en el codi de l'aplicació.
        
    - **Independència Programa-Operació:** Les operacions es poden modificar sense afectar la seva interfície.
        
3. **Abstracció de dades:** S'utilitza un **model de dades** per oferir una representació conceptual als usuaris mentre s'amaguen els detalls de l'emmagatzematge físic.
    
4. **Múltiples vistes:** Diferents usuaris poden veure subconjunts de dades o dades virtuals derivades segons les seves necessitats.

->**Compartició de dades i processament de transaccions multiusuari**.


| **Característica** | **Processament de Fitxers Tradicional**                         | **Enfocament de Base de Dades**                                                 |
| ------------------ | --------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| **Definició**      | Cada aplicació defineix i manté els seus fitxers.               | Dipòsit únic gestionat centralment.                                             |
| **Redundància**    | Dades duplicades en diversos llocs (malbaratament d'espai).<br> | **Control de redundància:** Cada dada es guarda en un sol lloc (Normalització). |
| **Dependència**    | L'estructura de dades està dins del codi del programa.          | **Independència:** L'estructura es guarda separada al catàleg.                  |

---

## 4. Actors i Rols del Sistema

L'ecosistema de BD involucra diversos perfils amb responsabilitats diferenciades:

### Actors "On the Scene" (Interessats en les dades)

- **Administradors (DBA):** Responsables d'autoritzar l'accés, coordinar l'ús i gestionar recursos de programari/maquinari.
    
- **Dissenyadors de la BD (Database Designers)**
	Són els arquitectes de la informació. Les seves responsabilitats són:
	
	1. Identificar les dades que s'han d'emmagatzemar.
	    
	2. Triar les estructures adequades per representar-les.
	    
	3. Comunicar-se amb els usuaris per entendre les seves necessitats.
	    
	4. Desenvolupar vistes que s'ajustin als requeriments de cada grup.
	    

- **Analistes de Sistemes i Programadors**
	- **Analistes de Sistemes:** Determinen els requeriments dels usuaris finals, especialment els paramètrics.
	    
	- **Programadors d'Aplicacions:** Implementen, testegen i mantenen les "transaccions programades" (canned transactions).
    
- **Usuaris Finals:**
    
    - **Casuals:** Accedixen esporàdicament amb consultes complexes.
        
    - **Naive/Paramètrics:** Executen transaccions programades (canned transactions) com operacions bancàries o reserves.
        
    - **Sofisticats:** Analistes que implementen les seves pròpies aplicacions complexes.
        
    - **Standalone:** Mantenen BD personals.
           
| **Tipus d'Usuari**   | **Coneixement del DBMS necessari** | **Disseny de la Interfície**       |
| -------------------- | ---------------------------------- | ---------------------------------- |
| **Naive/Paramètric** | Molt poc o gens                    | Apps mòbils / Interfícies tancades |
| **Casual**           | Mitjà (pocs comandaments)          | Llenguatges de consulta            |
| **Sofisticat**       | Molt alt                           | Eines d'anàlisi i desenvolupament  |
| **Standalone**       | Expert en el seu paquet            | Menús i interfícies gràfiques      |
>[!tip] Principi de Disseny 
>El DBMS ha de proporcionar múltiples instal·lacions per acomodar diferents tipus d'usuaris amb diferents nivells d'expertesa tècnica.

### Workers "Behind the Scene" (Interessats en la infraestructura)

Aquests professionals no s'interessen pel contingut de la BD, sinó pel sistema:

- **Dissenyadors i Implementadors del DBMS:** Creen els mòduls, catàlegs i llenguatges del programari DBMS.
    
- **Desenvolupadors d'eines:** Creen paquets de disseny, monitoratge de rendiment i interfícies.
    
- **Operadors i Manteniment:** Garanteixen el funcionament del maquinari i l'entorn de programari.
    

---

## 5. Avantatges i Funcions Avançades del DBMS

- **Control de la Redundància:** Mitjançant la **normalització**, s'evita duplicar dades per estalviar espai i evitar inconsistències.
    
- **Restricció d'accés no autoritzat:** El sistema d'autorització garanteix que cada usuari només accedeixi al que té permès.
    
- **Emmagatzematge persistent:** Permet guardar objectes de programa de forma permanent.
    
- **Processament eficient:** Utilitza **índexs**, _buffering_ i optimització de consultes per accelerar les cerques.
    
- **Integritat de les dades:** Enforça restriccions de tipus, claus d'unicitat, integritat referencial i regles de negoci.
    
- **Transaccions i Concurrència:**
    
    - **Aïllament (Isolation):** Cada transacció sembla executar-se sola.
        
    - **Atomicitat (Atomicity):** O es fan totes les operacions de la transacció o no se'n fa cap.
        
- **Bases de Dades Actives:** Poden incloure triggers i regles per a accions automàtiques.
    

## 6. Quan utilitzar (o no) un DBMS

Per què SI fer-lo servir (Avantatges):
- **Enforçament de la Integritat:** El sistema valida automàticament tipus de dades, claus úniques i regles de negoci.
    
- **Còpies de Seguretat i Recuperació:** Protecció contra fallades de maquinari o programari.
    
- **Representació de Relacions Complexes:** Capacitat per gestionar milers de dades interconnectades de forma eficient.
    
- **Seguretat:** Restricció d'accés no autoritzat mitjançant comptes i permisos.
    

Per què NO fer-lo servir:

- **Sobrecàrrega (Overhead):** El DBMS consumeix recursos per seguretat, concurrència i integritat.
    
- **Costos Inicials:** Alta inversió en maquinari, llicències de programari i formació de personal.
    
- **Casos concrets:**
    
    - Aplicacions molt simples que no han de canviar mai.
        
    - Sistemes amb requeriments de **temps real** molt estrictes on el DBMS és massa lent.
        
    - Sistemes encastats (embedded) amb memòria molt limitada.
        
    - Aplicacions d'un sol usuari on no cal control de concurrència.
---

> [!IMPORTANT] Per a l'Examen
>  Recorda el concepte de **transacció** (Query vs Update) i la importància del **catàleg** per a la independència de dades.
> 
