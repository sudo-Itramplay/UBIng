Jocs de suma 0, pq tot el que guanya l'oponent, és el que perds tu

minimax és tal que anem alternant el maximitzar amb minimitzar.
	PQ?
	Perque quan juga el meu rival, em minimitza a mi
	Quan jugo contraa el meu rival, em maximitzo a mi


-> La dreta min
->La esquerra max

El primer estadi és maximitzar, el segon minimitzar (diapo 24)

Comença minimax per l'esquerra

Minimax, donat num estats, és inviable
	Tot ique es pot limitar la profunditat

## Poda alfa beta
Tenim dos valors provisionals, alfa beta, iniciats en infinit (alfa en menys inf)

- En una capa max nomes es toca alfa
- - En una capa min nomes es toca beta
Si trobem que $\alpha >= \beta$ No explorem

Els valors del node pare els propaguem-> Hem d'anar reutilitzant les sortides
	DFS, però pensa que alfa i beta van cambiant enmig de la exploració dels fills
	Hi ha branques que, per ser massa poc optimes, les tallem
		QUan alfa més gran que beta
