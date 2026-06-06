Restriccions (_constraints_) que defineixen la integritat de les dades en crear taules amb [[DDL]].

**Referència: Diapositives 28-35**

**De columna:**
- `NOT NULL`: impedeix valors buits.
- `UNIQUE`: no permet duplicats.
- `DEFAULT`: assigna un valor si no se n'indica cap.
- `CHECK`: valida una condició (p. ex. `preu > 0`).

**De clau:**
- `PRIMARY KEY`: identificador únic ([[Clau Primària]]); pot ser composta.
- `FOREIGN KEY`: estableix la relació entre taules i garanteix la [[Restriccions d'Integritat|integritat referencial]] ([[Clau Estrangera]]).

Relacionat: [[DDL]] · [[Clau Primària]] · [[Clau Estrangera]] · [[Restriccions d'Integritat]]

#assignatura/BD #tipus/teoria
