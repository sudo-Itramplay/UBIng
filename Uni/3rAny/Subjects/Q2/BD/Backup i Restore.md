La preservació de les dades és prioritària; el backup és un requisit abans de qualsevol operació crítica i part de la [[Recuperació de Transaccions]].

**Operacions de terminal (MySQL):**
- **Còpia de seguretat:** `mysqldump -u usuari -p dbname > fitxer.sql`
- **Restauració:** `mysql -u usuari -p dbname < fitxer.sql`

> [!tip] Consell
> En restaurar, fes-ho sempre en una BD nova amb un nom diferent per no sobreescriure dades actives per accident. MySQL Workbench també ofereix Data Export/Import gràfic.

Relacionat: [[Recuperació de Transaccions]] · [[Transacció]] · [[SQL]]

#assignatura/BD #tipus/teoria
