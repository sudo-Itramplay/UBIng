Quan una [[Capa|capa]] superior transfereix dades a una capa inferior per a la seva transmissió. [[Peer-to-Peer]]


### Procès:
##### De l'SDU a la PDU

1. **[[N-SDU]]** com a Càrrega Útil: La [[N-SDU]] és la dada que la capa N rep de la capa superior (N+1). Per a la capa N, és la càrrega útil que ha de lliurar sense alteració.

2. **[[N-PCI]] com a Embolcall:** La capa N afegeix la seva **Informació de Control de Protocol (N-PCI)** (l'encapçalament/cua) a la N-SDU. Aquesta N-PCI conté les regles i controls propis del protocol de la capa N.

3. **Creació de la [[N-PDU]]** La suma de l'[[N-SDU]] i la [[N-PCI]] forma la **Unitat de Dades del Protocol (N-PDU)**, que és el missatge que la capa N utilitzarà per comunicar-se amb la seva capa homòloga remota.


$N-PDU=N-PCI+N-SDU$

### El Cicle d'Encapsulació

Una característica clau és que la **N-PDU** esdevé la **(N−1)-SDU** (la càrrega útil) de la capa inferior immediata (N−1). Aquest cicle es repeteix fins a la capa física:

$N-PDU=(N−1)-SDU$
