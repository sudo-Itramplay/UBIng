No sempre cal el màxim rigor; de vegades es prioritza el rendiment. El nivell d'aïllament (_isolation_) controla quins [[Problemes de Concurrència]] es permeten. Es configura amb `SET TRANSACTION`.

**Fenòmens anòmals:** Dirty Read · Nonrepeatable Read · **Phantoms** (una consulta retorna files diferents perquè una altra transacció n'ha inserit/eliminat).

| Nivell | Dirty Read | Nonrepeatable | Phantom |
| --- | --- | --- | --- |
| READ UNCOMMITTED | Permès | Permès | Permès |
| READ COMMITTED | No | Permès | Permès |
| REPEATABLE READ | No | No | Permès |
| SERIALIZABLE | No | No | No |

![[Pasted image 20260415192014.png]]

`SET TRANSACTION` també controla l'**access mode** (READ ONLY/WRITE) i la mida de l'**àrea de diagnòstic**.

Relacionat: [[Problemes de Concurrència]] · [[Propietats ACID]] · [[Control de Transaccions en SQL]]

#assignatura/BD #tipus/teoria
