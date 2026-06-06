Model, PersonaFiscal, Entrega i Lot# 1. El Model de Dades i el Model Relacional

>[!info] **Model**
> Una abstracció d'elements que interactuen amb un objectiu col·lectiu. 
> - Per a un enginyer, aquest model és una eina de comunicació fonamental entre dissenyadors i programadors.

No és el mateix a:

>[!info] Model de Dades
>És una col·lecció d'elements que permeten manipular (llegir/escriure) dades, establir relacions i definir restriccions d'integritat.


- **Context Històric i Tipologies**:
    
    - Models clàssics: Jeràrquic i de xarxa (basats en registres).
        
    - **Model Relacional**: Introduït per E.F. Codd el 1970, es basa en la noció matemàtica de **relació** (correspondència entre conjunts).
    
    - Models moderns: Orientat a objectes i NoSQL (documents, grafs, clau-valor).

## Relació
En un Model de Dades relacional:
- **La Relació com a Taula**: En aquest model, les dades es representen mitjançant taules bi-dimensionals compostes per files i columnes.
    
- **Exemples pràctics**: El material utilitza les taules `BRANCH` (sucursals amb id, carrer, ciutat, codi postal) i `STAFF` (empleats amb id, nom, càrrec, sexe, salari, etc.) per il·lustrar com es vinculen les entitats mitjançant claus.
### Atributs
- Propietats dels objectes representats per la relació
- Són les Columnes de les relacions

# 2. Estructura de les Dades Relacionals

Dins d'una base de dades, la relació és l'objecte principal que emmagatzema la informació. Per analitzar-la correctament, hem de distingir els següents components:

- **Atributs i Dominis**:
    
    - Un **atribut** és una propietat o característica de l'objecte representat (equival a una columna).
        
    - Cada atribut té un **domini**, que és el conjunt de valors vàlids que pot prendre.
        
    - Exemple: En una taula `STUDENT`, l'$ID$ podria ser una cadena de 9 caràcters, el $Nom$ text i l'$Edat$ un sencer positiu.
        
    - Els dominis són vitals per garantir la **integritat de les dades**, assegurant que només s'assignin valors coherents (ex: $Edat \geq 0$).
        
- **Tuples i Dimensions**:
    
    - Una **tupla** és cada una de les files de la relació.


>[!tip] Ordre i Cardinalitat
>- L'**Ordre** d'una relació és el seu nombre d'atributs (columnes).
>
>- La **Cardinalitat** és el nombre de tuples (files) que conté en un moment donat.

- És important notar que l'ordre i la cardinalitat no tenen per què coincidir. Per exemple, una taula amb 4 columnes i 5 files té $Ordre = 4$ i $Cardinalitat = 5$.

# 3. Propietats de les Relacions

Perquè una taula es consideri formalment una "relació" dins d'aquest model, ha de complir unes propietats estrictes que sovint són objecte de preguntes teòriques:

### Què es necessita per ser una relació?

- **Unicitat del Nom**: Dins d'una mateixa base de dades, dues relacions no poden tenir el mateix nom.

- **Unicitat de les Files**: No es permeten files duplicades; cada tupla ha de ser única.

- **Flexibilitat de l'Ordre**: L'ordre de les columnes (atributs) és lliure i no afecta la semàntica de la relació.

- **Consistència de Tipus**: Tots els valors d'una mateixa columna han de pertànyer al mateix domini.

- **Atomicitat**: Els valors de les cel·les han de ser **atòmics** (un sol valor). No poden contenir estructures de dades complexes com llistes o altres taules dins d'una cel·la

- **Noms d'Atributs**: Cada atribut ha de tenir un nom únic dins de la seva relació , tot i que relacions diferents poden compartir noms d'atributs (ex: `HOTELS.City` i `CLIENTS.City`).
![[Pasted image 20260224162107.png]]

# 4. Claus: Superclaus, Candidates, Primàries i Estrangeres

Les claus són el mecanisme que garanteix la consistència i permet identificar de manera unívoca cada fila.

### Super clau
 Atribut o conjunt d'atributs que identifica unívocament una fila. Pot contenir atributs redundants que no són estrictament necessaris per a la identificació.

- Candidates Vs SuperClau
	- Les candidates estàn optimitzades per fer-se servir com a Primarykey
	- Les superclaus són qualsevol combinació de columnes que pugui identificar-les
		- Però necessiten ser optimitzades

>[!tip] Pq té valor la super key?
>Pq diu que sempre hi ha una combina


![[Pasted image 20260224162309.png]]

### **Clau Candidata**: 
- Possible Clau primaria que hem decidit que no sigui primaria

És una **superclau mínima**. Significa que és irreduïble; si traguéssim qualsevol atribut, deixaria de ser una superclau. Una relació pot tenir diverses claus **candidates** (ex: `id` i `email`).
![[Pasted image 20260224162431.png]]
### **Clau Primària (PK)**:
És la clau candidata escollida pel dissenyador per identificar les files de la taula. Se sol representar **subratllada**. 
- La oficial i que s'ha decidit

>[!question] Només hi pot haver una PK per relació.
>
>Worst case scenario, a primary key may be formed by all the attributes in
the relationship
### **Clau Subrogada**: 

Una clau primària artificial (normalment un sencer autoincremental) sense significat semàntic, creada per garantir la unicitat de forma immutable.
##### Main characteristics:
- **Artificial**: Does not exist in the real world, generated solely for database purposes
-  Does not provide information about the entity (unlike an ID number or ISBN)
- Immutable: Does not change over time
- Unique: Generally an auto-incremental integer

### **Clau Estrangera (FK)**:
Atribut d'una relació A que referencia la clau primària d'una relació B. Actuen com a "punters" per relacionar dades i se solen representar en _cursiva_.

- Quan tens relacioons entre entitats, podem estalviarnos una una nova taula fent ús d'una d'aquestes

>[!tip] Representació
>The foreign keys are attributes of a relation A, that relate with a primary key of relation B
>- Foreign keys are ussually represented in italics

![[Pasted image 20260224162752.png]]



# 5. Restriccions d'Integritat i el valor NULL

L'últim pilar del model és el manteniment de la qualitat de les dades mitjançant restriccions:

- **El concepte de NULL**: Representa l'absència de valor o un valor desconegut/no aplicable. És crucial entendre que NULL no és el mateix que un zero o un espai en blanc.

- **Integritat d'Entitat**: Cap atribut que formi part de la clau primària pot ser NULL. Si la clau fos NULL, no podríem identificar la fila, contradient la seva definició.

- **Integritat Referencial**: Els valors d'una clau estrangera han de coincidir amb un valor existent de la clau primària de la taula referenciada, o bé ser NULL (si la lògica de negoci ho permet).

- **Exemple de flexibilitat del NULL**: Un empleat nou podria no tenir una oficina assignada inicialment; en aquest cas, la seva clau estrangera `branch_id` podria ser NULL fins que se li assigni una.