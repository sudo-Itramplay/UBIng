La **Unitat de Dades del Protocol (PDU)** de la capa N (N-PDU) és la unitat fonamental d'informació que s'intercanvia **entre entitats (iguals) de la mateixa capa N** en màquines diferents.

- La seva funció principal és encapsular la informació que es transmet. 

- Una N-PDU està formada per la N-PCI i, normalment, la [[N-SDU]] que ha rebut de la capa superior (N+1).


El propòsit de la N-PDU és servir com a **paquet de dades autònom** que conté les dades de l'usuari (SDU) més la informació de control necessària perquè la capa N gestioni correctament la comunicació (adreçament, detecció d'errors, control de flux, etc.) amb la seva capa N homòloga remota.


El propòsit de la N-SDU és representar la **informació de l'usuari o de la capa superior** que es vol enviar a través de la xarxa. És la dada pura que necessita el servei de la capa N.

_Nota:_ Una N-SDU esdevé la N+1-PDU un cop arriba a la capa N+1 del destí.