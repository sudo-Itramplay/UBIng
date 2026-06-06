# Introducció i Conceptes Bàsics de l'Esquema ER

## **Motivació i Utilitat** 
Els diagrames Entitat-Relació (ER) s'utilitzen en l'enginyeria de bases de dades principalment durant les etapes de planificació d'un projecte. 
- El seu objectiu principal és identificar els diferents elements del sistema i entendre les seves relacions mútues. 
Aquest model proporciona una representació visual molt intuïtiva que facilita enormement la comunicació i permet modelar l'estructura de les dades amb independència del SGBD escollit. 

>[!fail] Carències
>De cara a la validació, ajuden a detectar inconsistències, redundàncies i elements que podrien faltar en els requisits inicials.



## **Procés de Creació i Elements** 
Dibuixar un diagrama ER és un procés iteratiu clàssic. 
1. Comença per identificar totes les entitats i crear-ne rectangles amb noms adequats, tenint en compte que una entitat només ha d'aparèixer una vegada al diagrama. 
2. Seguidament, s'identifiquen les relacions connectant les entitats amb una línia i un rombe central que descrigui la interacció. 
3. Per últim, s'hi afegeixen els atributs, donant-los noms significatius perquè l'esquema s'entengui fàcilment.


## Perque fem aquests diagrames?

- Donen una respresentació que facilita la communicació
- és independent de la DBMS
- Ajuda a detectar errors (carències) de disseny en una fase prematura i variable
- Serveix com a documentació
-  Fàcilment es pot convertir a un esquema relacional


### 2. Transformació a Representació Tabular (Entitats i Atributs)


Per convertir l'esquema conceptual a taules relacionals, s'han d'avaluar:
- les entitats fortes
- les entitats febles
- els diferents tipus d'atributs 
- l'herència.

## **Entitats Fortes i Febles** 
Per a una entitat forta, es crea directament una taula amb tantes columnes com atributs tingui. 

La seva clau primària se selecciona d'entre les claus de l'entitat i es representa sempre subratllada.
- En canvi, una entitat feble no es pot identificar unívocament sola i depèn d'una altra per existir. 
- La seva taula contindrà els seus propis atributs al costat dels de la clau primària de l'entitat forta propietària. 
- La clau primària resultant es crea combinant la seva pròpia clau parcial i la primària del propietari (la qual, a més, actua com a clau forana, en cursiva).

>[!quote] Exemple
>![[Pasted image 20260303180912.png]]


## **Atributs Compostos i Multivariats** 
Els atributs comporten regles de conversió diferents segons la seva naturalesa. 

- Pels atributs **compostos** (com una adreça dividida en carrer i pis), no s'ha de crear cap taula separada; la solució és crear una columna per a cada sub-atribut dins la taula original de l'entitat. 
- Per contra, quan un atribut és **multivariat**, exigeix la creació d'una taula pròpia.
	- Aquesta nova taula inclou la clau primària de l'entitat com a clau forana. La clau primària d'aquesta taula és la unió d'aquesta clau forana amb cadascun dels possibles valors de l'atribut multivariat.

**Herència** Si l'esquema inclou herència (com una superclasse _Person_ amb subclasses _Employee_ i _Customer_), es construeix una taula per a l'entitat pare i taules individuals per a les entitats filles. Les taules de les filles compartiran el mateix identificador original del pare com a clau primària.
![[Pasted image 20260303181019.png]]

# Representació Tabular de les Relacions i les Claus

En un diagrama no ens trobem en la necessitat d'identificar les relacions ja que es veu a simple vista
	Al passar a un model relacional necessitem una manera d'identificar-ho

## **Relacions generals i generació de Claus** 

Una taula de relació s'estructura agrupant els atributs que formen les claus primàries de les entitats participants, sumats als atributs propis que descriguin la relació. 

>[!info] Per l'examen
>En teoria d'exàmens, és clau recordar que mentre en el model ER no existeixen les claus foranes ni les claus de relació, en el moment de la transformació tabular sí que apareixen obligatòriament.

## **El paper crucial de la Cardinalitat** 
La clau d'un conjunt de relacions ve exclusivament determinada per la cardinalitat:

- En relacions **1:1**, podem utilitzar la clau primària de qualsevol de les dues entitats per fer de clau primària de la nova taula.
![[Pasted image 20260303181436.png]]
- Per a les relacions **1:N o N:1**, la clau primària de la taula serà la clau primària del conjunt d'entitats amb cardinalitat N.
![[Pasted image 20260303181449.png]]
- En les relacions **N:N**, la clau primària s'obté irremediablement de la unió de les claus primàries d'ambdues entitats participants. Totes les claus procedents de les entitats són claus foranes.
>[!warning] Ojo cuidao
>Cal anar amb compte perquè, de vegades, una relació N:N necessita incloure un atribut propi de la relació (ex: un curs acadèmic) a la clau primària per identificar correctament els registres.


![[Pasted image 20260303181501.png]]

![[Pasted image 20260303181607.png]]

## **Relacions Febles i Múltiples** 

### Relacio Feble 
Una relació feble és un cas especial: 
- no té cap taula associada perquè la seva informació ja s'ha absorbit dins la taula de l'entitat feble. 
![[Pasted image 20260303181624.png]]


### Relacio Multiple
Quan la relació afecta més de dues entitats (n-ària), es dissenya una taula on les claus primàries de totes les participants figuren com a claus foranes, i la clau primària global s'estableix unint-les totes (tret que es pugui reduir per dependències internes).

# Simplificació i Combinació de Taules

## **Objectiu i Procés de la Simplificació**
La simplificació pretén millorar el disseny final valorant les restriccions de cardinalitat. 

>[!tip] Objectiu
>L'objectiu és reduir el nombre total de taules sense tenir cap pèrdua d'informació. Amb això, s'aconsegueix un entorn que facilitarà molt les tasques pràctiques de consulta i manipulació de bases de dades en el futur.

**Regles pràctiques de Combinació**

- En escenaris **1:1**, la taula associativa es pot combinar lliurement amb qualsevol de les taules d'entitats. S'executa afegint la clau primària d'un conjunt al de l'altre.
![[Pasted image 20260303181851.png]]
- Per als casos **1:N o N:1**, l'optimització requereix traslladar la clau primària del conjunt d'entitats amb cardinalitat 1 directament a la taula del conjunt d'entitats que posseeix la cardinalitat N.
![[Pasted image 20260303181905.png]]

>[!fail] Cas N:N
>**Restriccions Inviolables** És un concepte altament avaluable: les taules que provenen de relacions **N:N** no es poden recombinar de cap manera. Igualment, en les relacions múltiples que afecten més de dues entitats, la norma dicta que sempre hi haurà una taula extra independent.
>
