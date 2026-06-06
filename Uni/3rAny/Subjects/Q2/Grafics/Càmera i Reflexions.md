Per tal de decidir els elements que havia de tenir un objecte càmera es va fer això:

>[!quote] Atributs necessaris
> La **visió esteroscòpica** es construeix agafant dues imatges (càmeres representant un ull). Si volguessim visualitzar tota la escena i es considera $posicióCamera = p(x,y,z)$  i separció entre ulls $\delta x$ Quins atributs són diferents?:

**Paràmetres de la Càmera**:

- **VFOV (Vertical Field of View)**: Controla l'angle d'obertura vertical. Si decrementem el VFOV, fem "zoom in" (veiem menys escena, però més gran). Si augmentem la mida de la _window_, també fem efecte zoom.

- **LookAt i LookFrom**: Defineixen cap a on mirem i des d'on. Un _travelling_ (moviment físic de la càmera) implica canviar el `LookFrom` (i potser `LookAt`), mentre que un zoom òptic només canvia el VFOV.
- Pla Clipping Anterior


### 2. Càlcul d'Interseccions (Raig-Objecte)

El cor del _Ray Casting_ és determinar quin objecte colpeja primer un raig. En un examen, sovint es pregunta sobre la formulació matemàtica d'aquestes interseccions.

**Contracte del mètode `Hit`**: La funció `hit(ray, tmin, tmax)` ha de retornar `cert` si existeix una intersecció vàlida en l'interval $[t_{min}, t_{max}]$. Ha de retornar la $t$ més propera, el punt d'impacte $P$, la normal $\vec{N}$ i el material.

- **Intersecció amb Esferes**: Es resol una equació quadràtica derivada de substituir l'equació del raig en l'equació de l'esfera: $(P - C)^2 - R^2 = 0$.
    
    - El discriminant indica el nombre de solucions: $<0$ (cap), $=0$ (tangent), $>0$ (dues, entra i surt). Sempre ens quedem amb la $t$ més petita que sigui positiva i dins del rang.
        
- **Intersecció amb Plans**: Es basa en el producte escalar. Un pla es defineix com $(P - P_0) \cdot \vec{N} = 0$. Substituïm $P$ pel raig i aïllem $t$. Si el denominador és proper a zero, el raig és paral·lel al pla.
    
- **Intersecció amb Triangles:
    
    - Primer es calcula la intersecció amb el pla que conté el triangle.
        
    - Després, es verifica si el punt cau dins del triangle utilitzant **Coordenades Baricèntriques** $(u, v, w)$.
        
    - El punt és interior si $u \ge 0$, $v \ge 0$, $w \ge 0$ i $u+v+w = 1$. Aquestes coordenades també serveixen per interpolar normals o coordenades de textura als vèrtexs.

![[Pasted image 20260224153345.png]]

![[Pasted image 20260224153748.png]]

![[Pasted image 20260224153806.png]]
### 3. Optimització i Estructures d'Acceleració

El traçat de raigs "ingenu" té un cost de $O(N_{pixels} \times N_{objectes})$. Això és insostenible per a escenes complexes. Aquí és on l'enginyer ha de demostrar capacitat d'optimització.

- **Volums Contenidors (Bounding Volumes)**: Són formes geomètriques simples (esferes, capses) que engloben objectes complexos. Si el raig no toca el volum contenidor, segur que no toca l'objecte (estalviem càlculs cars).
    
- **AABB (Axis-Aligned Bounding Box)**: És el volum més comú. Es defineix pels punts mínim $(x_{min}, y_{min}, z_{min})$ i màxim $(x_{max}, y_{max}, z_{max})$.
    
    - **Mètode dels "Slabs"**: Per calcular la intersecció amb una AABB, tractem la capsa com la intersecció de 3 parells de plans paral·lels (slabs).
        
    - Calculem $t_{entry}$ i $t_{exit}$ per a cada eix ($X, Y, Z$).
        
    - L'interval d'intersecció final és $[\max(t_{enter}), \min(t_{exit})]$.
        
    - Hi ha impacte només si $t_{enter} < t_{exit}$ (i l'interval és vàlid).
        
- **Jerarquies de Volums (BVH)**: No n'hi ha prou amb posar una capsa a cada objecte; cal agrupar-los jeràrquicament (com un arbre).
    
    - Si un raig colpeja el node arrel (caixa gran), descendim als fills (esquerra/dreta). Si no, descartem tota la branca.
        
    - Això redueix el cost de lineal a logarítmic ($O(\log N)$) en el cas mig.


>[!fail] Problema
>![[Pasted image 20260224154155.png]]


>[!tick] Solucions:
>AA-box i BOABB
>![[Pasted image 20260224154242.png]]


- **Cost vs. Benefici**: Una AABB és ràpida de calcular però no s'ajusta perfectament a l'objecte (massa espai buit). Una OBB (orientada) s'ajusta millor però és més cara de calcular. Cal trobar l'equilibri.



### 4. Models d'Il·luminació i Ombres

Un cop tenim la intersecció, hem de determinar el color del píxel. Això depèn del model d'il·luminació i la visibilitat de les llums.
![[Pasted image 20260224154556.png]]

### Models d'iluminació
Venen determinats per:
- Mecanismes de comportament de la llum
(absorció, emissió, reflexió (scatter), transmissió)

- Tipus de Reflexions: difuses/especulars

- Llum directa/indirecta
- Càlculs
	- locals
	- globals

- **Ombres (Shadow Rays)**:
    
    - Per saber si un punt està a l'ombra, llancem un "raig d'ombra" des del punt d'intersecció ($P$) cap a la llum ($L$).
        
    - Si aquest raig colpeja _qualsevol_ objecte entre $P$ i la llum ($0 < t < dist\_llum$), el punt està a l'ombra (factor d'ombra = 0).
        
    - **Shadow Acne**: Error numèric on el raig d'ombra colpeja el propi objecte d'origen. Solució: afegir un petit $\epsilon$ (epsilon) a l'origen del raig: 
    - Al Inici és: $$p0 = p0 + \lambda \cdot L$$
    - però passa a ser: $$p0 = p0 + \epsilon \cdot L$$
    ![[Pasted image 20260224153903.png]]




- **Model de Blinn-Phong**: És el model estàndard explicat a classe. El color final és la suma de tres components:
	- Essent la fòrmula: $$I = k_a I_a + k_d I_d cos( \vec{L} , \vec{N} ) + k_s I_s cos(\vec{N} , \vec{H} )^{\beta}$$
	
    ![[Pasted image 20260224154714.png]]
    ![[Pasted image 20260224154752.png]]
    ![[Pasted image 20260224155047.png]]
    - **Ambient ($K_a \cdot I_a$)**: Il·luminació base constant.
        
    - **Difusa ($K_d \cdot I_d \cdot (N \cdot L)$)**: Depèn de l'angle entre la normal $N$ i la llum $L$. Simula superfícies mat.
        
    - **Especular ($K_s \cdot I_s \cdot (N \cdot H)^\beta$)**: Simula la brillantor. Usa el vector _Halfway_ ($H$) que és la mitjana entre la Llum ($L$) i la Visió ($V$).
        
- **Atenuació**: La llum decau amb la distància al quadrat ($1/d^2$), tot i que sovint s'usa una fórmula $1 / (a + b \cdot d + c \cdot d^2)$ per tenir més control artístic.

>[!tip] Es a dir
>La intensitat total en un punt es calcula com la contribució de totes les llums de l’escena en el punt més la intensitat ambient global de l’escena.

### 5. Textures i Apèndixs

Aquests temes solen aparèixer com a preguntes curtes o conceptes complementaris.
#### Com es mapejen les textures als objectes?
- Enganxar’ o mapejar (fer mapping) una textura sobre un objecte
consisteix en definir una funció unívoca (funció de mapping) que a
cada punt d’un objecte (x, y, z) li fa correspondre un punt d’una
imatge (i, j).

•El mapping pot ser directa o en dues fases


- **Mapeig de Textures (UV Mapping)**: Consisteix a assignar a cada vèrtex 3D una coordenada 2D $(u, v)$ en l'espai de la imatge de la textura.
    
- **Projeccions**: Per objectes simples, podem projectar la textura de forma automàtica:
    
    - _Planar_: $u = x/width$, $v = y/height$.
        
    - _Esfèrica_: Es converteixen les coordenades cartesianes a polars (latitud/longitud) per obtenir $u, v$ basats en els angles $\theta$ i $\phi$.

- **Cell Shading (Toon Shading)**: És una tècnica no fotorealista. En lloc d'un gradient suau d'il·luminació, es quantitza la intensitat.
    
    - Es calcula el producte escalar $N \cdot L$ (intensitat).
        
    - S'assigna el color basant-se en llindars (ex: si $I > 0.95$ color clar, si $I < 0.25$ color fosc). Això crea l'efecte de dibuix animat amb bandes de color sòlid.