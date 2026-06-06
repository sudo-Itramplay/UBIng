La **Unitat de Dades de la Interfície (IDU)** de la capa N (N-IDU) és el bloc de dades que es transfereix **físicament a través de la interfície** entre dues capes adjacents **en el mateix sistema** (la capa N i la capa inferior N−1).

- La N-IDU està composta per la [[N-SDU]] (que la capa N vol enviar) i la [[N-ICI]].



El propòsit de la N-IDU és ser el **format de dades** que s'utilitza per a la **interacció de servei** entre capes adjacents dins d'un mateix ordinador. Serveix com el _missatge_ enviat entre la capa client (N) i la capa servidora (N−1).

_Relació:_ N-IDU = N-ICI + N-SDU (aquí, N-SDU és la dada que N vol que N−1 transmeti).