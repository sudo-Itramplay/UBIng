## Recomanador

Netflix
Cada fila és un genere segons el que t agrada, i d'esquerra a dreta de més a menys probable

## Descobroiment
cerca-> Saps que existeix

Els recomanadors volen donar-te algo que no saps que existeix



>[!info] Un recomanador és un prob d'optimització

És una funció que entra usuari i item i et dona un num Real que representa el que pot agradar a una persona aquell item
(Forma de matriu)
El recomanador asumeix una mostra, sinó no pots recomanar

Normalment a un recomanador retornarem una llista de $k$ items
pq normalment volem més d'una recomanació

Jo vull predir bé la diagonal 


## Semblança netre users

Sumatori on, 
- si hi ha interrogant->0
- Si hi ha estarà ponderat per alfa
	- Alfa depen de la fila del vermell i el valor que poso dins el sumatori
	- Si s'asembla molt $s_1$ i $c_1$ alfa serà gran, 
		- Si t agrada molt un llibre igual que a un altre user alfa serà gran
		- Si t agrada molt un llibre que a l'altre no, alfa serà petit

A mi no m interessa recomanar el que la gent Ja consumeix
Pq ho consumirà igualment

El que vull recomanar no és el més comprat #itemsPocFrequents



## Distàncies
Si valorem 10 coses en comú el vector tindra len = 10
Distància petita és igual a guay --> Amb això es calcula alfa
	Pensa que són vectorss
Se li pot aplicar la inversa($^{-1}$) 
>[!tip] En opinions, mai fer distàncies euclidianes
>Va molt millor Pearson
>Ja que normalment una persona opinara per extrems

Fer servir pearson nomes per sistèmes no calibrats
	On hi ha opinions


Fer Servir Euclidia per sistèmes calibrats
	Minuts escoltats d'una cançó
	Distància a recòrrer

## Inflació


-->Exemple de la Rose

lo d adalt són pelis (Night i tal)

a cada salt a la dreta anem calibrant alfa (blau és la similitud recalibrada)
## Recomanacions segons items

Tindre en compte la fila, no la columna

Si lítem $u_n$ s asembla a l'altre tindrà alfa alt

És el mateix que el d'abans però transposant la matriu


S'ha de mirar, segons el que volem recomanar si ho vull fer segons user o item

A la pràctica no és tant precís per items però és més estable

La recomanació per usuaris realment és amb poblacions petites

Normalment les recomanacions es fan nomes un cop a la nit, la resta del dia es tenen unes recomanacions guardades

## Recomanació
- Explicít: Demanes qque facin el rating
- Implícit: La gent normalemnt enganya
Per veure si va ve agafa el 30% del que recomanes i mira si va bé

No mirar aquest 30 %
Pq l'algorisme funcionarà molt bé per aquest 30%
Però no sabem si al canviar del 30 percent 