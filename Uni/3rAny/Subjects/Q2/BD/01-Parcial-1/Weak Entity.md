Una **entitat feble (weak entity)** no té prou atributs per ser identificada de forma única per si mateixa.

- La seva existència depèn d'una altra entitat, l'**entitat propietària** (_owner entity_).
- Utilitza una **clau parcial** per distingir-se dins del mateix propietari.
- Per identificar-la completament cal la [[Clau Estrangera|clau de l'entitat propietària]].

![[Pasted image 20260217165233.png]]
![[Pasted image 20260217165333.png]]

**Exemple:** les oficines d'un departament numerades 101, 102… El número per si sol no és únic a tota l'empresa; depèn del codi de departament.

> En convertir a taules, la seva relació feble no genera taula pròpia → [[Transformació de Relacions a Taules]].

Relacionat: [[Entitat]] · [[Clau Estrangera]] · [[Model Entitat-Relació]]

#assignatura/BD #tipus/teoria
