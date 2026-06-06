## 1. Naturalesa i Evolució del SQL

**Referència: Diapositives 4-6**

El SQL no és només un llenguatge de consulta, és l'estàndard universal per a les bases de dades relacionals.

- **Definició**: El _Structured Query Language_ és el llenguatge estàndard de l'ANSI per operar amb servidors de BD.
    
- **Objectius**: Permet crear bases de dades, definir taules i restriccions, i realitzar operacions de recuperació (consultes) i manipulació (inserir, actualitzar, esborrar).
    
- **Importància**: Redueix els problemes de migració entre diferents productes DBMS i ofereix una interfície declarativa (especifiquem _què_ volem, no _com_ obtenir-ho).
    
- **Evolució**: Originat com a SEQUEL a IBM, ha passat per diverses versions (SQL-86, SQL-92, SQL:1999) fins a les actualitzacions modernes.
    

## 2. L'Estructura del Servidor MySQL

**Referència: Diapositives 10-14**

Abans de programar, cal entendre on estem treballant.

- **Sistema Client-Servidor**: MySQL funciona amb un servidor central que gestiona les dades i diversos clients (com el terminal o el Workbench) que s'hi connecten.
    
- **Estructura Jeràrquica**: Un servidor pot allotjar múltiples **Bases de Dades** (esquemes), i cada base de dades conté un conjunt de **Taules**.
    
- **MySQL Workbench**: És l'eina gràfica (IDE) oficial que facilita el disseny, la creació i l'administració de la BD.
    

## 3. Definició de Dades (DDL): Bases de Dades

**Referència: Diapositives 16-18**

El primer pas és crear el contenidor principal.

- **Creació**: S'utilitza la comanda `CREATE DATABASE nom_bd;`.
    
- **Selecció**: Per indicar al sistema quina BD volem utilitzar: `USE nom_bd;`.
    
- **Eliminació**: Compte amb aquesta! `DROP DATABASE nom_bd;` esborra tot el contingut permanentment.
    

## 4. Tipus de Dades en SQL

**Referència: Diapositives 22-26**

Triar el tipus de dades correcte és vital per a l'eficiència del sistema.

- **Numèrics**: `INT` (enters), `DECIMAL(p,s)` (per a precisió fixa com diners), `FLOAT`.
    
- **Cadenes de text**:
    
    - `CHAR(n)`: Longitud fixa (més ràpid).
        
    - `VARCHAR(n)`: Longitud variable (estalvia espai).
        
- **Data i Hora**: `DATE` (YYYY-MM-DD), `TIME`, `DATETIME`.
    

## 5. Creació de Taules i Restriccions (Constraints)

**Referència: Diapositives 28-35**

Aquesta és la part més crítica per definir la integritat de les dades.

- **Sintaxi Bàsica**: `CREATE TABLE nom_taula (columna1 tipus restricció, ...);`.
    
- **Restriccions de Columna**:
    
    - `NOT NULL`: Impedeix valors buits.
        
    - `UNIQUE`: No permet duplicats en aquesta columna.
        
    - `DEFAULT`: Assigna un valor si no se n'indica cap.
        
    - `CHECK`: Valida que el valor compleixi una condició (ex: `preu > 0`).
        
- **Claus Primàries (`PRIMARY KEY`)**: Identificador únic per a cada fila. Pot ser una sola columna o una combinació (clau composta).
    
- **Claus Estrangeres (`FOREIGN KEY`)**: Estableix la relació entre taules i garanteix la integritat referencial.
    

## 6. Manipulació de Dades (DML): Inserció

**Referència: Diapositives 41-45**

Un cop tenim l'estructura, cal omplir-la.

- **Insert Bàsic**: `INSERT INTO taula (columnes) VALUES (valors);`.
    
- **Variants**: Es poden ometre les columnes si es donen valors per a totes en l'ordre original, o fer insercions múltiples en una sola sentència.
    

## 7. Operacions de Consulta (DQL)

**Referència: Diapositives 48-61**

La funció principal del SQL és extreure informació útil.

- **Estructura SELECT**:
    
    - `SELECT`: Quines columnes volem.
        
    - `FROM`: De quina taula.
        
    - `WHERE`: Quines files han de complir la condició.
        
- **Filtrat Avançat**: Ús d'operadors com `AND`, `OR`, `NOT`, `BETWEEN`, `IN` i `LIKE` (per a patrons de text amb `%` o `_`).
    
- **Ordenació**: `ORDER BY columna ASC|DESC` per presentar els resultats ordenats.
    

## 8. Modificació d'Estructures (ALTER TABLE)

**Referència: Diapositives 74-79**

Com a enginyers, sovint haurem de modificar sistemes ja existents.

- **Afegir/Eliminar Columnes**: `ALTER TABLE taula ADD/DROP COLUMN nom;`.
    
- **Modificar Restriccions**: Es poden afegir o treure `UNIQUE`, `PRIMARY KEY` o `FOREIGN KEY` a taules ja creades.
    
- **Valors per Defecte**: `ALTER TABLE taula ALTER COLUMN col SET DEFAULT valor;`.
    
