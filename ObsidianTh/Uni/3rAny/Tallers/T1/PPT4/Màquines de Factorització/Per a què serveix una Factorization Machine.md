
## 1. Les Limitacions del Model Anterior: Factorització de Matrius (MF)

La Factorització de Matrius és una tècnica potent, però presenta dues mancances principals que motiven la creació de models més avançats com les Màquines de Factorització.

### Problema 1: El Feedback Implícit

La formulació clàssica de MF funciona excel·lentment quan tenim **feedback explícit**, és a dir, valoracions numèriques directes que un usuari ha donat a un ítem 
	(p. ex., 1 a 5 estrelles ⭐).

No obstant això, la majoria de dades generades avui dia són de **feedback implícit**. Aquestes no són valoracions directes, sinó inferències basades en el comportament de l'usuari.
- **Exemples:** Clics, compres, visualitzacions de pàgines, temps passat en un article, cançons escoltades.


La MF clàssica "es trenca" en aquest escenari per dues raons:

1. **Absència de senyal negatiu clar:** 
	Si un usuari no ha comprat un producte, significa que no li agrada? O simplement no l'ha vist? La manca d'interacció és una dada ambigua.

2. **Naturalesa de les dades:** 
	Aquestes dades no són escales numèriques (com les estrelles), sinó sovint esdeveniments binaris (ha fet clic / no ha fet clic) o recomptes.


### Problema 2: L'Objectiu Real és el Rànquing

Pensem en com es presenta una recomanació a un usuari: gairebé sempre com una **llista ordenada** d'ítems.

- A l'usuari final no li importa si el sistema prediu una valoració de 4.5 o 4.2 per a una pel·lícula.

- El que realment importa és **quin ítem apareix abans que un altre** a la llista de recomanacions.

Per tant, l'objectiu fonamental d'un sistema recomanador no hauria de ser predir amb precisió una valoració numèrica, sinó **construir un rànquing correcte** dels ítems per a cada usuari.

>[!warning] Problema
>La MF tradicional optimitza per a l'error de predicció (regressió), no directament per a la qualitat de l'ordenació.

