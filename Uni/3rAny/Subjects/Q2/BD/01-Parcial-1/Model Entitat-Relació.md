El Model Entitat-Relació és una eina de **disseny conceptual**. El seu objectiu principal és reduir un problema del món real a objectes bàsics (entitats) i les connexions que els uneixen (relacions). Aquesta abstracció permet simplificar significativament el disseny abans d'entrar en detalls d'implementació.


>[!tip] Tipus de models:
>- **Model ER (Conceptual):** S'utilitza per al disseny inicial, representant entitats i atributs de forma visual.
>- **Model Relacional (Lògic):** És la implementació real on les dades s'organitzen en taules amb files i columnes gestionades per un DBMS.

![[Pasted image 20260217162601.png]]

# Entitats
-  Qualsevol objecte del món real que es pot distingir de la resta
	- com un cotxe o una persona, 
- Té una serie de propietats. 
- Poden anar de lo concret a lo més abstracte. 
Un conjunt d'entitats (entity set) és el grup d'entitats del mateix tipus que comparteixen propietats. 

Aquestes propietats s'anomenen **atributs**.

Representació d'una entitat:

![[Pasted image 20260217162754.png]]


## Atributs
Propietat d'una entitat

### Tipus d'Atributs
- Simples:
	- No són divisibles 
- Compostos:
	- Són una representació de varis elements, però que formenn un concepte:
	Adreça: Carrer, número, pis, ...
![[Pasted image 20260217164016.png]]

- Univalued:
	- És un atribut amb un sol valor
- Multivalued
	- Té més d'un valor per al mateix atribut
	Una persona pot tenir més d'un número de telèfon
![[Pasted image 20260217164149.png]]

- Derivats
	- El seu valor es calcula a partir d'altres atributs
	La edat es calcula a traves de la data de naixement
![[Pasted image 20260217164325.png]]

- Key atributtes:
	- És atribut diferenciatori a un altre entitat, que nomes té aquesta
![[Pasted image 20260217165045.png]]


## Weak Entiti

Aquelles que no tenen prou atributs per ser identificades de forma única per si mateixes. 
- La seva existència depèn d'una altra entitat anomenada **entitat propietària** (owner entity).

- Utilitzen una **clau parcial** per distingir les entitats dins del mateix propietari.

- Per identificar-les completament, cal la clau de l'entitat propietària (foreign key).
- 
![[Pasted image 20260217165233.png]]

Un exemple clar és el d'un departament i les seves oficines. Si cada departament té oficines numerades (101, 102...), el número d'oficina per si sol no és únic a tota l'empresa (diversos departaments poden tenir una oficina 101). Per tant, l'oficina és una entitat feble que depèn del codi del departament per ser identificada unívocament.

![[Pasted image 20260217165333.png]]


- Les weak entities necessiten weak relations???

>[!tip] OJO
>• Para atenció als seus atributs


>[!warning] Ningú té rols estaàtics
>Depenent del tipus de bases de dades que tingui, per exemple, el rol de telèfon i persona es pot invertir, ja que el sentit de entitat i atribut se li dona segons què estem modelant

# Relacions
Una **relació** és una associació entre entitats
- Generalment etiquetada amb un verb. 
- Un conjunt de relacions agrupa associacions del mateix tipus.
- **Pot ser que siguin recursives**

![[Pasted image 20260217165553.png]]

Podem trobar estructures complexes de relacions:

- **Atributs descriptius:** Les relacions també poden tenir atributs propis. Per exemple, la relació entre "Estudiant" i "Assignatura" pot tenir l'atribut "nota".

![[Pasted image 20260217165834.png]]
![[Pasted image 20260217165847.png]]
- **Relacions recursives:** Una entitat es relaciona amb si mateixa jugant rols diferents, com un empleat que supervisa altres empleats.

- **Relacions múltiples (n-àries):** Relacions que connecten més de dues entitats simultàniament. En aquests casos, la cardinalitat s'avalua fixant totes les entitats menys una.
![[Pasted image 20260217165905.png]]

## Restriccions 
Les restriccions defineixen com les entitats interactuen entre elles en el model.


### Cardinalitat
 La **cardinalitat** indica el nombre màxim d'instàncies d'una entitat que es poden relacionar amb una altra.

- **1:1 (un a un):** Un tutor té un grup, i un grup té un sol tutor.

- **1:N (un a molts):** Un departament té molts professors, però un professor pertany a un sol departament.

- **N:N (molts a molts):** Un estudiant pot fer moltes activitats, i una activitat pot tenir molts estudiants.

*Exemple:*
![[Pasted image 20260217170105.png]]
### Participació
indica si l'existència d'una entitat depèn de la seva relació amb una altra:
- **Total:** Totes les entitats del conjunt han de participar en la relació (doble línia). Per exemple, cada préstec ha d'estar associat obligatòriament a un client.

- **Parcial:** Només algunes entitats participen en la relació. Per exemple, podem tenir clients que no tenen cap préstec actiu.

![[Pasted image 20260217170202.png]]


## Exemple final:

El concepte de **Generalització/Especialització** és molt similar a l'herència de la programació orientada a objectes. Permet crear jerarquies on una entitat de nivell superior (superclasse) comparteix atributs comuns amb entitats de nivell inferior (subclasses).

En l'exercici del FC Barcelona (diapositiva 81), s'aplica aquest concepte de la següent manera:

- L'entitat **Persona** actua com a base amb atributs generals (DNI, nom, cognoms, data de naixement).

- D'aquesta es deriven **Jugador**, **Treballador** i **Entrenador**, que hereten els atributs de Persona però tenen els seus propis (com "anys d'experiència" per a l'entrenador o "demarcació" per al jugador).

Aquest model final integra tots els conceptes apresos: relacions N:N (Sponsor-Equip), entitats febles (si escau), atributs en relacions (data_assig a la capitania) i la jerarquia de classes per optimitzar l'estructura de dades.


- Hi ha un exercici d'una dream house, aquest és el resultat final

![[Pasted image 20260217170237.png]]
