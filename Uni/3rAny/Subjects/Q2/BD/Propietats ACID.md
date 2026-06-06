Propietats que ha de complir tot sistema de [[Transacció|transaccions]] digne:

- **Atomicitat (Atomicity):** la transacció és una unitat atòmica; s'executa tota o no es fa res.
- **Consistència (Consistency):** porta la BD d'un estat consistent a un altre, respectant totes les [[Restriccions d'Integritat]].
- **Aïllament (Isolation):** una transacció ha de semblar que s'executa sola, sense interferències ([[Nivells d'Aïllament]]).
- **Durabilitat (Durability):** un cop fet commit, els canvis persisteixen permanentment, fins i tot davant fallades.

![[Pasted image 20260418092108.png]]

Relacionat: [[Transacció]] · [[Nivells d'Aïllament]] · [[Recuperació de Transaccions]]

#assignatura/BD #tipus/teoria
