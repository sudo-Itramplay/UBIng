La **simplificació** millora el disseny final reduint el nombre total de taules **sense pèrdua d'informació**, valorant les restriccions de [[Cardinalitat]].

**Regles de combinació:**
- **1:1** → la taula associativa es combina lliurement amb qualsevol de les dues entitats (s'afegeix la PK d'un conjunt a l'altre).
- **1:N o N:1** → es trasllada la PK del conjunt amb cardinalitat **1** a la taula del conjunt amb cardinalitat **N**.

![[Pasted image 20260303181851.png]]
![[Pasted image 20260303181905.png]]

> [!fail] Cas N:N
> Les taules que provenen de relacions **N:N no es poden recombinar** de cap manera. En relacions múltiples (>2 entitats) sempre hi haurà una taula extra independent.

Relacionat: [[Transformació de Relacions a Taules]] · [[Passant els ER a MR]] · [[Cardinalitat]]

#assignatura/BD #tipus/teoria
