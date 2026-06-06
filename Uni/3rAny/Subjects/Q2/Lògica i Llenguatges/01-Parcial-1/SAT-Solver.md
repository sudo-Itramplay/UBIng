
### Introducció i Conceptes Fonamentals dels SAT-solvers

Un dels pilars d'aquesta part del temari és la definició i aplicabilitat dels solucionadors de satisfactibilitat. 

L'objectiu d'aquesta secció és establir la base de coneixement teòric que us permetrà abordar els exercicis de modelització pràctica posteriors.

- SAT-solvers
	- programes fonamentats en la lògica de proposicions per resoldre problemes pràctics.
    
- El nucli de la qüestió teòrica és el Problema SAT, el qual consisteix a decidir si una fórmula proposicional estructurada en Forma Normal Conjuntiva (FNC) és satisfactible.

- La importància cabdal del problema SAT rau en la capacitat de representar múltiples problemes pràctics mitjançant fórmules d'un llenguatge de proposicions.

- La lògica subjacent ens dicta que, si la fórmula associada aconsegueix ser satisfactible, això significa irremeiablement que el problema modelat té solució.

>[!remember] Recorda
>- Un SAT-solver és, per definició, l'eina de programari que resol aquest problema SAT.
   
- Aquests programes informàtics han estat àmpliament estudiats per la comunitat acadèmica i tenen la capacitat computacional de processar fórmules lògiques de grans dimensions.

>[!quote] Exemples i utilitats
>- A efectes pràctics, els SAT-solvers poden resoldre l'assignació de portàtils a docents d'una escola garantint que aquells amb hores coincidents no els comparteixin.
  >  
>- Són capaços d'abordar el clàssic problema topològic de colorejar mapes emprant quatre colors sense que països fronterers coincideixin en la tonalitat.
  >  
>- A nivell de sistemes, permeten resoldre la instal·lació de paquets d'actualització de programari tot complint els seus arbres de restriccions i dependències.
  >  
>- A nivell d'organització, faciliten la configuració d'equips humans de mida mínima per a la realització de tasques.
  >  
>- En l'àmbit logístic i de control, permeten el traçat de rutes de comunicacions o transport, així com l'assignació de recursos dins de procediments industrials.
>
>- També resolen l'elaboració d'horaris altament complexos en entorns crítics com línies aèries, centres de salut i escoles.

   

> **Consell de professor:** Memoritzant un parell d'aquests exemples pràctics podreu justificar l'ús d'aquests sistemes teòrics en preguntes de desenvolupament o de reflexió dins de l'avaluació.

---

### Cas Pràctic: El Problema de la Coloració de Mapes


El problema de la coloració de grafs planars (mapes) és un exercici d'avaluació recurrent. 

Ens exigeix definir un alfabet proposicional clar i dissenyar conjunts de clàusules que limitin el comportament del sistema únicament a allò que considerem solucions vàlides. 
	Presteu especial atenció als subíndexs i a la traducció de condicions d'exclusivitat (que una cosa passi o no passi de manera excloent).

- Per il·lustrar la potència de l'eina, s'exposa el problema d'assignar quatre colors a un mapa continental, sent resoluble per un SAT-solver.

### Resolució
La regla fonamental del problema dicta que cap parell de països veïns pot tenir assignat el mateix color.

- A nivell de notació matemàtica, establim P com el conjunt de països del continent i representem els quatre colors a utilitzar mitjançant els dígits numèrics 1, 2, 3 i 4.

L'objectiu informàtic és expressar aquest repte mitjançant una fórmula proposicional en Forma Normal Conjuntiva (FNC) per tal que la màquina (el SAT-solver) ho entengui i ho resolgui.

- Per estructurar l'alfabet de variables, es pren per a $i\in P$ i $j\in\{1,2,3,4\}$ la proposició $Rij$, que adquireix el significat semàntic de "al país i se li assigna el color j".
    
- El procediment de formalització s'ha de dividir lògicament en diverses asseveracions imprescindibles.
	
	- Primera condició: S'ha de garantir que, sense excepció, a cada país se li assigni efectivament un color.
	    
	- Per complir aquesta primera premissa, introduïm per a cada $i\in P$ una clàusula de disjunció: $Ri1\vee Ri2\vee Ri3\vee Ri4$.
	    
	- Segona condició: S'ha de prohibir estrictament que a un mateix país se li assigni més d'un color de manera simultània.
	    
	- Per aconseguir aquesta exclusivitat, per a tot $i\in P$ i qualsevol parell de colors $j,j'\le4$ on $j\ne j'$, s'imposa la clàusula: $\neg Rij\vee\neg Rij'$.
	    
	- Tercera condició: S'ha de traduir a nivell lògic el fet que els països que són fronterers no poden tenir colors compartits.

- Així, per a qualsevol parell de països $i,i'\in P$ que constin com a veïns, i per a tots els colors possibles $j\le4$, es dictamina la clàusula de prevenció: $\neg Rij\vee\neg Ri'j$.

- El model complet a introduir al solucionador s'obté realitzant la conjunció global de totes les clàusules generades a les passes (1), (2) i (3).


---

### Cas Pràctic: Resolució de Sudokus mitjançant SAT-solvers

El segon model d'exemple que trobem augmenta lleugerament la complexitat dimensional. Mentre que als mapes operàvem amb dos índexs (país i color), en un sudoku operem amb tres (fila, columna i valor contingut). 


El raonament per excloure l'aparició de múltiples valors a la mateixa casella, o la repetició de valors a diferents coordenades, és exactament el mateix patró metodològic que ja hem vist. 

Aquest tipus de progressió analítica és la que diferencia un bon aprenent de programació lògica d'un de rutinari. Cal interioritzar molt bé els següents passos de definició espacial.


### Plantejament
- Per representar la matriu del sudoku s'estableix un àtom $Rijk$ per a cada fila $i$, per a cada columna $j$, i per a cada valor $k$, on els tres paràmetres oscil·len entre el número 1 i el 9.

- Semànticament, aquesta variable $Rijk$ equival a afirmar que "en la fila i columna j del sudoku està el valor k".

- Com és habitual, la codificació per al sistema requereix establir el trencaclosques sencer sota una fórmula en format FNC composta per una sèrie de regles estrictes.

### Resolució
Abans de començar a dictar regles, el primer pas de qualsevol formalització és definir el nostre alfabet lògic.

- Per a cada fila $i$, columna $j$ i valor $k$, on tots oscil·len entre 1 i 9, definim l'àtom $Rijk$.

- El significat semàntic d'aquesta variable és: "en la fila $i$ columna $j$ del sudoku està el valor $k$".


---

#### Fase 1: Restriccions Internes de la Casella

La matriu ha de contenir dades vàlides i aquestes no es poden encavalcar dins d'un mateix espai espacial.

- **Regla d'Existència:** La regla inicial estipula que cada unitat o casella de la matriu ha de contenir un valor de forma imperativa. Això requereix que per a qualsevol coordenada bidimensional $i,j$, hàgim d'escriure la clàusula: $Rij1\vee Rij2...\vee Rij9$.

- **Regla d'Exclusivitat:** La regla consegüent decreta que està prohibit que una única casella albergui de forma simultània més d'un dígit. La traducció lògica de l'exclusivitat s'aplica per a cada parell de valors diferents $k\ne k^{\prime}$, dictant l'equivalència clàusula: $\neg(Rijk\wedge Rijk^{\prime})\equiv\neg Rijk\vee\neg Rijk^{\prime}$.


> [!tip] Anotació del Professor: De Morgan a la pràctica
> 
> Fixeu-vos com traduïm una restricció verbal ("mai poden haver-hi dos números alhora") a una clàusula pura en Forma Normal Conjuntiva (FNC). Negar la conjunció lògica equival, matemàticament, a establir una disjunció d'elements negats. Aquesta és la clau de la mecanització teòrica per als SAT-solvers.

---

#### Fase 2: Restriccions Geomètriques del Tauler

La geometria del sudoku prohibeix que un valor estigui duplicat en el decurs de la mateixa fila, de la mateixa columna o de l'àrea quadrada de $3\times3$ on resideix.

- **Eix de Files:** Per garantir la unicitat a la fila de treball, amb columnes diferents $j\ne j^{\prime}$ i per a un mateix número $k$, extraiem la clàusula resolutiva: $\neg(Rijk\wedge Rij^{\prime}k)\equiv\neg Rijk\vee\neg Rij^{\prime}k$.

- **Eix de Columnes:** Aquesta mateixa tècnica de denegació de repetició s'ha de replicar de manera totalment anàloga operant sobre l'eix de les columnes.

- **Subquadrícules:** Tractant la parcel·la de $[1,3]\times[1,3]$, per a coordenades divergents on $(i,j)\ne(i^{\prime},j^{\prime})$, la unicitat del valor $k$ es blinda amb: $\neg(Rijk\wedge Ri^{\prime}j^{\prime}k)\equiv\neg Rijk\vee\neg Ri^{\prime}j^{\prime}k$.

- **Sistematització:** L'algorisme de restricció espacial ha d'ampliar-se de forma anàloga i sistemàtica per protegir la resta dels quadriculats de dimensions $3\times3$.


---

#### Fase 3: Inicialització i Clausura del Sistema

Amb les regles de l'univers ja definides, només ens falta carregar l'estat inicial de la partida i donar instruccions al nostre SAT-solver.

- **Estat Inicial:** Per inicialitzar adequadament l'execució del trencaclosques, és mandatari introduir en l'equació les xifres proporcionades per defecte. Tècnicament, si a la fila $i$ i columna $j$ ja hi figura un dígit $k$, s'adhereix l'àtom $Rijk$ directament al model com a veritat absoluta.

- **Macro-conjunció:** El sistema es tanca generant la conjunció ininterrompuda de cadascuna de les clàusules derivades a les tres fases descrites anteriorment.
    

> [!abstract] Resolució i Teorema Subjacent 
> El teorema que fa útil aquesta mecanització ens diu que la graella de sudoku tindrà solució si, i només si, aquesta grandiosa fórmula en FNC resulta ser satisfactible. 
> - A més, l'assignació concreta (interpretació) que fa que la fórmula esdevingui certa coincideix mil·limètricament amb la solució del trencaclosques.

