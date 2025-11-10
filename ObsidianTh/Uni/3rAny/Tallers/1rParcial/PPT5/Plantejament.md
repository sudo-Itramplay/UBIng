D'on surt el problema?

>[!note] Situació
>Estàs en un supermercat, com poses els ítems? què ha d'estar al cantó de què?

Primer ens preguntem:
	Quin és el subconjunt d'ítems més freqüents?
	$U$ conjunt ítems a la venta
	$I$ subconjunt de número de bosses amb els ítmes seleccionats
	s -> A partir de quin num de bosses considerem vàlid fixar-nos

- Ítems: {m,c,p,b,j}
- Suport: s= 3 bosses
- Bosses: 
	- B1= { m, c, b },
	- B2= { m, p, j }, 
	- B3= { m, b }, 
	- B4= { c, j }, 
	- B5= { m, p, b }, 
	- B6= { m, c, b, j }, 
	- B7 = { c, b, j }, 
	- B8= { b, c }.

![[Uni/3rAny/Tallers/1rParcial/PPT5/2025-10-19_18-34.png]]


>[!tip] No sempre és trobar x en un conjunt
>Exemple:

Si els ítems són documents, les bosses són frases, i definim que un ítem/document està a una bossa/frase si la frase està al document, els conjunts d'ítems freqüents poden indicar problemes de _plagiarisme_.

- Com podem veure en aquest exemple, ho estem aplicant a una relació de molts-a-molts que no és del tipus "_forma-part-de_": si hi ha un parell d'ítems que apareixen junts a varies bosses és que tenim documents amb les mateixes frases.