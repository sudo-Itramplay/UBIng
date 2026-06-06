El sistema ha de garantir que les [[Transacció|transaccions]] siguin **"tot o res"** ([[Propietats ACID|atomicitat]]). Si una transacció falla després d'executar operacions, aquestes s'han de **desfer (undo)** per evitar estats parcials.

![[Pasted image 20260415191717.png]]

**Tipus de fallades:**
1. **Fallada de l'ordinador:** crash o error de maquinari/xarxa.
2. **Errors lògics:** divisió per zero, paràmetres erronis.
3. **Errors locals:** condicions com saldo insuficient.
4. **Control de concurrència:** abortar per deadlock o violar la serialitzabilitat.
5. **Fallada de disc:** pèrdua de blocs.
6. **Catàstrofes:** incendis, robatoris, inundacions.

La recuperació es recolza en el [[Log del Sistema]].

Relacionat: [[Transacció]] · [[Log del Sistema]] · [[Propietats ACID]] · [[Backup i Restore]]

#assignatura/BD #tipus/teoria
