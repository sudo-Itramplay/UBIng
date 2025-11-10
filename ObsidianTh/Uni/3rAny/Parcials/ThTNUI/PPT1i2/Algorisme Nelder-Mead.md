És un [[Uni/3rAny/Parcials/ThTNUI/PPT1i2/Algorisme d'optimització directe]] utilitzat per trobar un mínim local


> [!info] Tenir en compte
> Sobretot quan la funció és difícil o impossible de derivar analíticament

**Mou, reflecteix i redueix iterativament un [[Uni/3rAny/Tallers/1rParcial/PPT2/Simplex]]** per tal de fer-lo **convergir cap al punt de valor mínim** de la funció.

>[!example] Exemple
>En una corba tindriem una gràfica de 2dim, però la corba és de 1dim. 
>Això vol dir que necessitarem 1+1 punts


**Funcionament:** 
- En cada iteració, l'algorisme identifica el vèrtex amb el **pitjor valor** (el més alt) de la funció f(x). 
- A continuació, aplica una seqüència de transformacions geomètriques per substituir aquest pitjor vèrtex per un de nou i millor:
	- **Reflexió:** Prova un punt reflectit a través del centre de la cara oposada.
	
	- **Expansió:** Si la reflexió és molt bona, s'expandeix encara més en aquesta direcció.
	   
	- **Contracció:** Si la reflexió és pitjor, es contrau el símplex cap a dins.
	 
	- **Reducció:** Si tot falla, redueix tot el símplex cap al millor punt trobat.

>[!WARNING] Compte!
>Quantes més dimensions tenim, més avaluacions haurem de fer, això ens limita moltissim, perquè augmenta exponencialment el temps



>[!info] Link Algorisme interactiu
>https://www.benfrederickson.com/numerical-optimization/

