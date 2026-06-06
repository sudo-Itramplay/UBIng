
## 1. Conceptes Fonamentals de les Transaccions

>[!info] **Definició**: 
>Una transacció és un mecanisme per descriure unitats lògiques de processament de bases de dades que s'han de completar en la seva totalitat per garantir la correcció.

- Normalment s'executen mitjançant programes d'ordinador que inclouen operacions:
	- de recuperació (read),
	- inserció, 
	- eliminació i 
	- actualització (write) 

Però per tal d'assegurar la seva correctesa han d'haver acabat enterament
### **Sistemes de Processament**
Són sistemes amb grans bases de dades i centenars d'usuaris concurrents 
	(ex: banca, mercat de valors, reserves aèries) .

- **Requisits del Sistema**: Aquests sistemes exigeixen alta disponibilitat, temps de resposta ràpids i suport per a la concurrència massiva .

#### Hi ha dos tipus de sistema:
- **Single-user DBMS**
	- Com a molt, un usuari pot fer servir el sistema alhora
	- Restringit a sistemes d'ordinadors personals
- **Multiuser DBMS**
	- Varis usuaris concurrents hi poden accedir
	- Milers d'usuaris operant alhora
	- El més fet servir
	- 
 > S'expliquen a més detall més endavant

- **Granularitat de les Dades**: Els conceptes de processament s'apliquen independentment de si l'ítem de dades és un camp individual, un registre sencer o un bloc de disc complet .
    
- **Operacions Bàsiques**: Tota transacció es redueix a dues operacions fonamentals: 
	- `read_item(X)` (llegir de la BD a una variable) 
	- `write_item(X)` (escriure de la variable a la BD) .
    ![[Pasted image 20260415191350.png]]
![[Pasted image 20260415191407.png]]
## 2. Concurrència i Execució

En el món real, els sistemes no són monousuaris; la potència de les bases de dades modernes rau en la multiusuarietat.
#### Existeixen dos tipus de processat

##### 1. Processament Intercalat (Interleaved Processing)

És la forma clàssica de concurrència en sistemes amb **un sol CPU**. La sensació de simultaneïtat és una il·lusió creada per la velocitat de commutació del sistema.

- **Mecànica de funcionament**: El CPU executa unes quantes instruccions d'un procés, el suspèn, i passa a executar instruccions del següent procés .
    
- **Continuïtat**: Quan un procés es reprèn, ho fa exactament en el punt on es va suspendre, garantint que la lògica de la transacció no es perdi.
    
- **Eficiència de Recursos**: Aquest mètode és vital per mantenir el CPU ocupat mentre altres processos esperen operacions d'E/S (I/O), com llegir un disc.
    
- **Justícia (Fairness)**: Evita que processos molt llargs bloquegin el sistema, permetent que les transaccions curtes avancin per les "escletxes" de temps.
    
- **Focus acadèmic**: És important notar que la majoria de la teoria de control de concurrència (com la serialitzabilitat) es basa en aquest model intercalat .
    

##### 2. Processament Paral·lel (Parallel Processing)

Aquí parlem de **concurrència real i física**. No hi ha commutació per compartir un recurs, sinó que hi ha múltiples recursos disponibles.

- **Requisit de Maquinari**: Exigeix obligatòriament la presència de **múltiples CPUs** o processadors físics .
    
- **Execució Simultània**: Els processos s'executen realment al mateix instant de temps, cadascun en el seu propi processador.
    
- **Paral·lelisme Real**: Es considera una execució paral·lela "vera" (true parallel execution), eliminant la necessitat d'intercalar instruccions per simular velocitat.
    
>[!tip] **Focus Teòric**: 
>La major part de la teoria de control de concurrència es centra en la concurrència intercalada.


## 3. Problemes del Control de Concurrència

Quan les transaccions s'executen sense control, poden sorgir fenòmens que corrompen la lògica de les dades. 

Aquests punts són crítics(4):

- **Lost Update (Actualització Perduda)**: Ocorre quan dues transaccions accedeixen als mateixos ítems i les seves operacions s'intercalen, provocant que una actualització sigui sobreescrita per l'altra .
![[Pasted image 20260415191444.png]]
- **Dirty Read (Lectura Bruta/Temporal)**: Una transacció llegeix un valor actualitzat per una altra transacció que encara no ha confirmat (commit) i que finalment falla i fa un rollback .
![[Pasted image 20260415191459.png]]

- **Incorrect Summary (Resum Incorrecte)**: Mentre una transacció calcula una funció agregada (com una suma), altres transaccions actualitzen els valors, fent que el resultat final sigui inconsistent .
![[Pasted image 20260415191511.png]]    
- **Unrepeatable Read (Lectura no repetible)**: Una transacció llegeix el mateix ítem dues vegades i rep valors diferents perquè una altra transacció l'ha modificat entremig .
    

## 4. Recuperació i Fallades de Transacció

El sistema ha de garantir que les transaccions siguin "tot o res".
![[Pasted image 20260415191717.png]]
- **Necessitat de Recuperació**: Si una transacció falla després d'executar algunes operacions, aquestes s'han de desfer (undo) per evitar estats parcials.


- **Tipus de Fallades**:
    
    1. **Fallada de l'ordinador**: Crash del sistema o error de maquinari/xarxa.
        
    2. **Errors lógics**: Divisió per zero o paràmetres erronis .
        
    3. **Errors locals**: Condicions com saldo insuficient que obliguen a cancel·lar.
        
    4. **Control de concurrència**: Abortar per resoldre un deadlock o violar la serialitzabilitat .
        
    5. **Fallada de disc**: Pèrdua de dades en els blocs de disc .
        
    6. **Catàstrofes**: Incendis, robatoris o inundacions .


## 5. Nivells d'Aïllament en SQL

No sempre necessitem el màxim rigor; de vegades prioritzem el rendiment.

- **Nivells (de menys a més restrictiu)**:
    
    1. **READ UNCOMMITTED**: Permet Dirty Reads, Nonrepeatable Reads i Phantoms.
        
    2. **READ COMMITTED**: No permet Dirty Reads, però sí la resta.
        
    3. **REPEATABLE READ**: (Per defecte en molts sistemes) No permet Dirty ni Nonrepeatable Reads.
        
    4. **SERIALIZABLE**: El més restrictiu, prevé tots els problemes.
![[Pasted image 20260415192014.png]]
- **Fantasmes (Phantoms)**: Ocorre quan una transacció llegeix files que compleixen una condició i una altra transacció n'insereix una de nova que també la compleix entremig .
    
## 6. Estats i el Log del Sistema

>[!tip] Recordem: Transacció
>És una unitat de treball atòmica, que ha de fer-se completament, o no fer-se, però no es pot deixar a mitges


El DBMS utilitza un diari de bord per gestionar la recuperació.
- **Operacions clau**:
	- `BEGIN_TRANSACTION` : Marka l'inici d'execució
	- `READ` / `WRITE` : Especifica operació a la base de dades de ítems
	- `END_TRANSACTION` : Marka el final DE LES OPERACIONS
	- `COMMIT_TRANSACTION` : Senyal d'operació exitosa
	- `ROLLBACK (ABORT)` : Senyal d'operació fallida


- **Estats**: Una transacció passa per estats: Activa → Parcialment Commesa → Commesa → Terminada. Pot fallar des de l'estat activa o parcialment commesa.
    
- **Log del Sistema**: Fitxer seqüencial (append-only) que registra totes les operacions (start, write, read, commit, abort) .
![[Pasted image 20260418091826.png]]

   
- **Punt de Commit**: Es llança quan totes les operacions s'han executat amb èxit i s'han registrat al log .
    
- **Force-writing**: És vital que el buffer del log s'escrigui al disc abans de fer el commit de la transacció.
## 6. Propietats ACID

Són propietats desitjables en un sistema d'aquest tipus 
 Qualsevol sistema de transaccions digne ha de complir aquests quatre pilars:

- **Atomicitat**: La transacció és una unitat atòmica; s'executa tota o no es fa res.
    
- **Consistència (Consistency)**: Una transacció porta la base de dades d'un estat consistent a un altre estat consistent, respectant totes les restriccions d'integritat.
    
- **Aïllament (Isolation)**: Una transacció ha de semblar que s'executa sola, sense interferències de transaccions concurrents.
    
- **Durabilitat**: Un cop confirmada (commit), els canvis han de persistir permanentment, fins i tot davant de fallades del sistema.
    
![[Pasted image 20260418092108.png]]


    

## 7. Caracterització de Schedules (Planificacions)


- Un _schedule_ és l'ordre d'execució de les operacions de diverses transaccions concurrents.

- **Operacions en Conflicte**: Dues operacions entren en conflicte si:
	- pertanyen a diferents transaccions, 
	- accedeixen al mateix ítem 
	- i almenys una és una escriptura (write) .
![[Pasted image 20260418092908.png|578]]

![[Pasted image 20260418092936.png]]

- **Recuperabilitat** (Schedule): Un schedule és **recuperable** si cap transacció fa commit fins que totes les transaccions de les que ha llegit dades hagin fet commit.
    
- **Cascadeless** (Schedule): Evita els "aborts en cadena" fent que les transaccions només llegeixin dades ja commeses.

![[Pasted image 20260418092957.png]]

![[Pasted image 20260418093013.png]]

- **Serialitzabilitat**: Un schedule és serialitzable si és equivalent a algun ordre serial (un darrere l'altre). Això garanteix la correcció sense perdre els avantatges de la concurrència .

![[Pasted image 20260418093032.png]]

- **Graf de Precedència**: Eina per testar la serialitzabilitat. Si el graf (nodes = transaccions, arestes = conflictes) no té cicles, el schedule és serialitzable .
	- ![[Pasted image 20260418093210.png]]
    

## 8. Control de Transaccions en SQL (MySQL)

A la pràctica, SQL ens proporciona les eines per gestionar la **atomicitat** (tot o res) de les nostres unitats de treball.

**Flux de Treball i Sintaxi:**

- **Inici:** Es pot utilitzar `START TRANSACTION` per començar una transacció explícita.
    
- **Finalització:** Useu `COMMIT` per fer els canvis permanents o `ROLLBACK` per desfer tota l'activitat de la transacció si es detecta un error.
    
- **Autocommit:** Per defecte, MySQL executa cada sentència com una transacció independent. Es pot desactivar amb `SET autocommit = 0` per agrupar múltiples operacions manualment.
    
- **Exemple Clàssic:** El trasllat de fons entre comptes. Si la segona operació falla (ex: falta de saldo o error de xarxa), el `ROLLBACK` garanteix que els diners no "desapareguin" del sistema.
    
>[!warning] COMMIT
>Recorda de fer commit per tal que els canvis siguin permanents



## 9. Característiques i Nivells d'Isolació

Podem configurar el comportament de les transaccions mitjançant la sentència `SET TRANSACTION`. 
Les tres característiques principals són:
- el mode d'accés (READ ONLY/WRITE), 
- la mida de l'àrea de diagnòstic
- i, la més important, el **Nivell d'Isolació**.

**Acces Mode**
Especifiquem COM es poden accedir les dades

![[Pasted image 20260418094844.png]]

**Diagnostic Area Size**
Indica el numero de condicions simultanies 

![[Pasted image 20260418094941.png]]

**Viles de la Isolació (Fenòmens anòmals):**

1. **Dirty Read (Lectura Bruta):** Llegir dades d'una transacció que encara no ha fet commit.
    
2. **Nonrepeatable Read (Lectura No Repetible):** Llegir el mateix registre dues vegades i obtenir valors diferents perquè algú l'ha modificat entremig.
    
3. **Phantoms (Fantasmes):** Una consulta que retorna un conjunt de files canvia perquè una altra transacció ha inserit o eliminat registres que compleixen la condició.
    

Taula Comparativa de Nivells:

|**Nivell**|**Dirty Read**|**Nonrepeatable Read**|**Phantom**|
|---|---|---|---|
|**READ UNCOMMITTED**|Permès|Permès|Permès|
|**READ COMMITTED**|No|Permès|Permès|
|**REPEATABLE READ**|No|No|Permès|
|**SERIALIZABLE**|No|No|No|


![[Pasted image 20260418095211.png]]

![[Pasted image 20260418095316.png]]
## 6. Còpia de Seguretat i Restauració (Backup & Restore)

Com a enginyers responsables, la preservació de les dades és la nostra màxima prioritat. El backup no és només una mesura de seguretat, sinó un requisit abans de qualsevol operació crítica.

**Operacions de Terminal:**

- **Còpia de Seguretat:** S'utilitza l'eina `mysqldump`.
    
    - `mysqldump -u usuari -p dbname > fitxer.sql`.
        
- **Restauració:** S'utilitza el client estàndard de `mysql`.
    
    - `mysql -u usuari -p dbname < fitxer.sql`.
        
- **Consell de Professional:** Quan restaureu una base de dades, feu-ho sempre en una base de dades nova amb un nom diferent per evitar sobreescriure dades actives per accident. MySQL Workbench també ofereix interfícies visuals per a aquestes tasques (Data Export/Import).