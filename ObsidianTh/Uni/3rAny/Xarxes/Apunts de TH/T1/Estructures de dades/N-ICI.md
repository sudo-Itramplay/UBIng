La **Informació de Control de la Interfície (ICI)** de la capa N (N-ICI) és la informació de control que la capa N (client) envia a la capa N−1 (servidora) **a través de la interfície entre elles**, dins del mateix sistema.

- Aquesta informació **NO** es transmet a través de la xarxa, sinó que s'utilitza per demanar o coordinar un servei específic entre les dues capes adjacents.



El propòsit de la N-ICI és especificar els **paràmetres o opcions del servei** sol·licitat per la capa superior a la inferior. Per exemple, pot contenir informació sobre la prioritat, la qualitat de servei, o l'adreça de destinació que N−1 ha d'utilitzar (però que N−1 potser no inclou en la seva PDU).