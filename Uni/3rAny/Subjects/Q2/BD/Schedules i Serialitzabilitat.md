Un **schedule** (planificació) és l'ordre d'execució de les operacions de diverses [[Transacció|transaccions]] concurrents.

**Operacions en conflicte** — quan dues operacions:
- pertanyen a transaccions diferents,
- accedeixen al mateix ítem,
- i almenys una és una escriptura (write).

![[Pasted image 20260418092908.png]]

**Propietats d'un schedule:**
- **Recuperable:** cap transacció fa commit fins que totes les que ha llegit hagin fet commit.
- **Cascadeless:** evita aborts en cadena fent que només es llegeixin dades ja commeses.
- **Serialitzable:** equivalent a algun ordre serial (un darrere l'altre) → correcció sense perdre concurrència.

**Graf de Precedència:** eina per testar la serialitzabilitat (nodes = transaccions, arestes = conflictes). Si **no té cicles**, el schedule és serialitzable.

![[Pasted image 20260418093032.png]]
![[Pasted image 20260418093210.png]]

Relacionat: [[Concurrència]] · [[Problemes de Concurrència]] · [[Log del Sistema]]

#assignatura/BD #tipus/teoria
