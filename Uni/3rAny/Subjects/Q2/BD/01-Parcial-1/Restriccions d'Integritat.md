Regles que mantenen la qualitat de les dades en el [[Model Relacional]]:

- **Integritat d'Entitat:** cap atribut de la [[Clau Primària]] pot ser [[NULL]] (si ho fos, no podríem identificar la fila).
- **Integritat Referencial:** el valor d'una [[Clau Estrangera]] ha de coincidir amb una PK existent de la taula referenciada, o bé ser [[NULL]] (si la lògica de negoci ho permet).
- **Restriccions de [[Domini]]:** els valors han de pertànyer al domini de l'atribut.

**Exemple:** un empleat nou pot no tenir oficina assignada → la seva FK `branch_id` pot ser NULL fins que se li assigni.

Relacionat: [[Clau Primària]] · [[Clau Estrangera]] · [[NULL]] · [[Domini]]

#assignatura/BD #tipus/teoria
