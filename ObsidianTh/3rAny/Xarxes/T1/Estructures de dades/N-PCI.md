La **Informació de Control de Protocol (PCI)** de la capa N és l'encapçalament (i/o cua) de dades que l'entitat de la capa N **afegeix a la [[N-SDU]]** que ha rebut de la capa superior.

- Conté tota la informació de control necessària per al protocol de la capa N: adreces lògiques, números de seqüència, camps de control d'errors, indicadors de segmentació/reassemblatge, etc.

El propòsit de la N-PCI és permetre que la capa N gestioni les funcions del seu protocol, assegurant la **correcta comunicació** amb la seva capa homòloga remota. Essencialment, és la "informació de gestió" per a la capa.

_Relació:_ N-PDU = N-PCI + N-SDU.