L'algorisme de **Ray Tracing** considera la llum com un flux de fotons que viatgen en trajectòries rectilínies, no interfereixen entre ells i obeeixen les lleis de reflexió i refracció. 

>[!quote] Extra
>**Informació Mínima per a Visualització 3D**: No n'hi ha prou amb la geometria. Per percebre la dimensió 3D d'un objecte superficial de cares planes, cal definir:
>  
>- **Geometria i Topologia**: Els vèrtexs i com es connecten (la "forma"). * **Atributs Visuals**: El **material** (com reflecteix la llum) i la **il·luminació** (fonts de llum que generen ombres i matisos).
>        
  >  - **Configuració de Visualització**: La **càmera** (posició i orientació) i el **viewport** (la finestra de sortida de píxels). Sense aquests elements, només tindríem coordenades matemàtiques sense representació visual.


>[!info] Concepte Clau
> **principi de reciprocitat**, que ens permet fer **Backward Ray Tracing**: 
> - en lloc de traçar milions de rajos des de la font de llum (molts dels quals mai arribarien a l'ull), tracem rajos des de l'observador cap a l'escena.
> - És una alternativa al Z-Buffer

cal diferenciar clarament entre tres tecnologies:

- **Raycasting**: Es limita a simular el primer raig de llum per determinar la visibilitat (semblant al z-buffer).

- **Raytracing**: És un algorisme recursiu que calcula múltiples rebots per simular reflexions especulars, ombres i transparències.

- **Integradors**: Són les fórmules matemàtiques que modulen aquests rebots i determinen la il·luminació global final que arriba a cada píxel.

### Exemple Algorisme recursiu
L'algorisme recursiu `computeRayColor` opera en tres nivells:

1. **Rajos primaris (eye rays)**: Llançats des de l'observador a través de cada píxel.

2. **Rajos d'ombra (shadow rays)**: Llançats des del punt d'intersecció cap a les fonts de llum per saber si el punt està il·luminat o en ombra.

3. **Rajos secundaris**: Inclouen els de **reflexió** (direcció de mirall) i els de **transparència** o refracció.

![[Pasted image 20260221094014.png]]


# Model de Càmera i Càlcul del Raig Primari

Per generar la imatge, definim matemàticament cada raig mitjançant una **recta paramètrica**:
$$p = A + t \cdot \vec{B}$$
Aquí, **A** és el punt inicial (l'observador) i **B** és el vector director (la direcció que passa pel píxel). 

>[!Warning] Crucial 
>Si la intersecció ens dóna una **$t$ negativa**, vol dir que l'objecte està darrere de l'observador i, per tant, no l'hem de processar.


Per llançar un raig, utilitzem l'equació paramètrica $p = A + t \cdot \vec{B}$. La gestió de les coordenades i la posició de l'objecte és crítica per a l'eficiència:

- **Paràmetres de Càmera**: 
	- Definits per `lookFrom` (ull), `lookAt` (on mirem), `VUP` (verticalitat) i `vfov` (angle de visió). El camp de visió es delimita pels **clipping planes** (near i far).
    
- **Coordenades Homogènies**: Utilitzem $(x, y, z, w)$. Recorda: $w=1$ per a punts i $w=0$ per a vectors directors. Aquesta distinció permet aplicar transformacions lineals de forma consistent.
    
- **Transformacions i Eficiència (Pregunta 8)**: En carregar una malla, l'estratègia més eficient per aplicar transformacions (translacions, escalats) no és modificar cada vèrtex de la llista un per un cada vegada.
    
    - **Millor pràctica**: Utilitzar una **representació per vèrtexs indexats** on es guarden els vèrtexs originals i el **centre de l'objecte** com un atribut separat. Això permet moure l'objecte sencer manipulant només el seu punt de referència o aplicant matrius de transformació a la càmera/raig sense reconstruir la malla constantment.
        
- **Consideració de la $t$**: Qualsevol intersecció amb $t < 0$ s'ha de descartar immediatament, ja que l'objecte es troba darrere de l'observador.

En el càlcul vectorial, utilitzem **coordenades homogènies** $(x, y, z, w)$. 

>[!tip] Recorda 
> El valor de **$w$** és el que ens defineix si estem tractant amb un **punt** ($w=1$) o amb un **vector** ($w=0$). 
> - Aquesta distinció és vital quan apliquem transformacions geomètriques a l'escena. 
> - El **viewport** és la nostra imatge final de píxels, mentre que el **frame buffer** (o window) és la representació en memòria on anem emmagatzemant els colors calculats per cada raig.


## Raig Primari
El raig Primari és el raig que va de l'observador a la escena
	Per tant necessitem saber:
	- On està l'observador
	- Quina part del món es veurà (escena)

### Càlcul raig Primari

El càlcul del raig primari és el primer pas per determinar què hi ha en cada píxel de la nostra imatge. 

Per facilitar les operacions matemàtiques inicials, utilitzem una configuració de càmera estàndard:
- **La Convenció del Món 3D (Eix Z negatiu)**:
    - En gràfics per computador, sovint adoptem el sistema de la "mà dreta". Per convenció, situem tot el món que volem visualitzar a l'espai de les **Z negatives**. Això vol dir que, si l'observador mira cap endavant, tot el que veu té una coordenada Z menor que zero.
    
- **L'Observador a l'Origen**:
    
    - Situem l'observador (la càmera) exactament al punt **(0, 0, 0)** del món 3D. Aquest és el nostre punt de partida o origen de tots els rajos primaris.
    
- **Definició del Viewport (La Imatge)**:
    
    - Simplifiquem la nostra imatge final a una graella de **200x100 píxels**. L'origen de coordenades d'aquesta imatge (píxel 0,0) se sol situar a la cantonada inferior esquerra.
    
- **Distància Focal i Pla de Projecció**:
    
    - Fixem una **distància focal d'1**. Això situa el nostre "pla de projecció" (on "viuen" els píxels de la imatge en el món 3D) exactament a **Z = -1**. Així, qualsevol raig que surti de l'ull (0,0,0) passarà per un punt d'aquest pla abans d'endinsar-se en l'escena.
	
- **Camp de Visió i Geometria de la Finestra (Window)**:
    
    - **vfov = 90º**: Definim un angle de visió vertical de 90 graus. Aquesta obertura, combinada amb la distància focal, determina quant del món veiem verticalment.
	
    - **Aspect Ratio = 2**: Com que la imatge és el doble d'ampla que d'alta (200/100), la relació d'aspecte és 2.
	
    - **Dimensions de la Window**: Amb aquestes dades, la nostra "finestra" al món 3D s'estén des de **(-2, -1)** fins a **(2, 1)** sobre el pla Z = -1. Això vol dir que la finestra té una amplada total de 4 unitats i una alçada de 2 unitats.


**Per què fem tot això?** 
Aquesta configuració elimina variables complexes com la rotació de la càmera o posicions arbitràries en l'espai. Ens permet centrar-nos en la lògica pura del _ray-intersection_: llançar un raig des de `(0,0,0)` cap a una coordenada `(u, v, -1)` i veure amb què xoca.


# Càlcul del Color

## Interseccions amb l'escena

Una escena complexa no és només una llista d'objectes; s'organitza en estructures de dades per optimitzar el rendiment, com els **Scene Graphs** o els **Arbres CSG** (Constructive Solid Geometry).

- En els arbres CSG, creem objectes complexos mitjançant operacions booleanes: 
	- **Unió**
	- **Diferència**
	- **Intersecció**

Com vas anotar correctament, la unió de diversos punts per formar un model és el que anomenem **Topologia**.


Per determinar quin color té un píxel, l'algorisme ha de recórrer els objectes i trobar la **intersecció més propera** (la $t > 0$ més petita). Podem trobar dos tipus principals d'objectes:

- **Objectes superficials**: Només representen la closca o frontera exterior (ex: malles de triangles).

- **Objectes volumètrics**: Representen la densitat o temperatura de l'espai intern.


Dins d'aquestes estructures, a cada vèrtex o punt del model hi ha associats dos vectors o rajos potencials per al càlcul de la il·luminació. 



# Modelatge d'Objectes i Representació de Malles

El modelatge es pot fer mitjançant **objectes paramètrics** (com esferes definides per centre i radi) o **malles poligonals**. 

- Les malles de triangles són les més utilitzades perquè garanteixen que els tres punts sempre estiguin en un mateix pla. 

- Per contra, les malles de quadrilàters poden presentar problemes de coplanaritat, tot i que són millors per alineares a la curvatura o aplicar textures.

#### **Objectes paramètrics**
un objecte en el espai R3 està representat per un conjunt d’equacions
paramètriques

>[!Info] P. ex,
> - Esfera: definida per el centre C (cx, cy, cz) i el seu
radi R
>![[Pasted image 20260221100259.png]]
> - Pla: definit per la seva normal (nx, ny, nz) i un punt
de pas que determina d
> ![[Pasted image 20260221100321.png]]

>[!tip] Com es calcula la intersecció amb el Raig? I la normal?
>Substituïnt en la equació de l’objecte el punt p definit
per l’equació paramètrica del Raig
> ![[Pasted image 20260221100352.png]]


![[Pasted image 20260221095851.png]] ![[Pasted image 20260221100121.png]]


#### Malles Poligonals
Un objecte en el espai R3 (poliedre) que està representat per un conjunt
(tancat) de polígons:

-  Un **polígon** 
	- és l’interior d’un conjunt planar tancat i connectat d’arestes lineals.
-  Una **aresta** 
	- es defineix pels seus dos punts extrems o vèrtexs
-  Un **vèrtex** 
	- és un punt representat per les coordenades x, y, z.

Perquè una malla poligonal es consideri geomètricament correcta i computable, ha de complir estrictament dues condicions de topologia:
### Topologia
La topologia defineix com es connecten els punts. Perquè una malla sigui computable i no doni errors en Ray Tracing, ha de complir unes regles estrictes de coherència:

- **Interseccions Vàlides**: La intersecció de dos polígons en una malla ben definida **pot ser buida** (no es toquen), un vèrtex comú o una aresta comuna. El que mai pot passar és que es creuïn per l'interior de les cares.
    
- **Condició Manifold (2-Manifold)**:
    
    - Cada aresta ha de ser compartida per, com a màxim, **dues cares**.
    
    - Si una aresta és compartida per 3 o més polígons, la malla és **non-manifold** (físicament impossible en superfícies sòlides). 
    
    * **Malles Obertes vs. Tancades**:
	    - En una **malla tancada**, TOTES les arestes han de ser compartides per exactament dues cares.
	        
	    - En una **malla oberta** (com una superfície plana o una tela), existeixen **arestes de frontera** que només pertanyen a una cara. Per tant, l'afirmació que "totes les arestes han de ser compartides per dues cares" és falsa per a malles obertes.
        


#### Malla de Triangles
La malla de triangles és l'estàndard de la indústria perquè qualsevol polígon complex es pot subdividir sempre en un conjunt de triangles. 

>[!tip] Perquè és tant important?
>Aquesta unitat bàsica és la preferida en gràfics per computador per la seva propietat fonamental: 
>
> - tres punts en l'espai sempre defineixen un únic pla, garantint que la cara sigui perfectament plana.


Perquè una malla de triangles es consideri topològicament vàlida (el que anomenem una malla "sana" o _manifold_), ha de complir estrictament aquests requisits:
1. **Coherència de les Arestes**
	- **Compartició binària**: Totes les arestes de la malla han de pertànyer exactament a **2 triangles**.
	    
	- **Sentit físic**: Aquesta regla garanteix que no hi hagi "pàgines soltes" o triangles que surtin del mig d'una aresta, assegurant que la superfície sigui contínua i tancada.
	    
	- **Excepció de frontera**: Només en els casos on l'objecte és obert (com una tela), les arestes del contorn poden pertànyer a un sol triangle.
	    

2. **Continuïtat dels Vèrtexs** (Vertex Star)
	- **Conjunt continu**: Tots els vèrtexs de la malla han de tenir un conjunt **continu de triangles** al seu voltant.
	    
	- **Estructura en "ventall"**: Això significa que si recorres els triangles que toquen un vèrtex, has de poder passar d'un a l'altre seguint les arestes fins a tancar el cercle (o arribar al límit de la malla).
	    
	- **Evitar punts singulars**: Si un vèrtex unís dos volums separats només per la punta, la malla no seria _manifold_ i els càlculs de les **normals de vèrtex** (necessàries per matisar com arriba la llum) fallarien.



### La importància de la normal
En modelar, necessitem saber la normal de cada punt (o cara) per calcular amb precisió com arriba la llum i com es comporta el material (matisos).

- La normal es calcula mitjançant el producte vectorial de les arestes: $$n = (s-r) \times (t-r)$$
- És fonamental que els vèrtexs estiguin ordenats en **sentit anti-horari** per garantir que la normal apunti cap a l'exterior de l'objecte.

# Representacions de Dades (Estructures en Memòria)

Triar l'estructura de dades correcta depèn totalment de l'operació que vulguis optimitzar (temps d'intersecció, memòria o navegació topològica):

- **Explícita (STL)**: Llista de vèrtexs per a cada triangle. És redundant i no guarda connectivitat (no sap quins triangles són veïns).

- **Vèrtexs Indexats (OBJ/OFF)**:
    
    - **Avantatge**: És la més eficient en **memòria i temps** per fer Ray Tracing (test d'intersecció raig-malla).
        
    - **Motiu**: Evita redundància de vèrtexs i és prou simple perquè l'algorisme d'intersecció hi accedeixi ràpidament sense sobrecàrrega d'estructures complexes.
        
- **Adjacència de Cares**:
    
    - **Avantatge**: És el model més eficient en **memòria** per calcular quina cara és adjacent a una altra o per trobar tots els triangles que comparteixen un vèrtex.
        
    - **Funcionament**: Permet "saltar" d'un triangle a un altre de forma directa. En el cas de buscar els triangles d'un vèrtex $v$, només cal trobar un triangle i seguir els punters d'adjacència (màxim uns pocs accessos).
        
- **Winged-Edge**:
    
    - És l'estructura més potent per a **edició geomètrica** (afegir/treure vèrtexs o arestes), però és molt costosa en memòria.
        
    - **Atenció**: En Winged-Edge l'element central és l'**aresta**. No guarda les cares adjacents directament a la llista de cares; les troba navegant a través de les arestes.

|**Estructura**|**Millor per a...**|**Memòria**|
|---|---|---|
|**Explícita (STL)**|Impressió 3D simple|Molt redundant|
|**Vèrtexs Indexats**|**Ray Tracing** (Interseccions)|Eficient|
|**Adjacència de Cares**|Trobar veïns / Topologia|Equilibrada|
|**Winged-Edge**|Edició i modificació de malla|Cara (Molts punters)|