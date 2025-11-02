# Kernels de Edge Extraction
- Sobel
- Prewitt
- Derivative of Gaussian
- Laplacian of Gaussian
- Canny edges

### Explicació de Kernels
#### Basats en la 1a Derivada (Detectors de Gradient)
Detecten la **magnitud i direcció** del canvi. Són bons per trobar la presència d'una vora.

* **Sobel:** Utilitza kernels de 3x3 que donen més pes als píxels centrals. És molt comú.
* **Prewitt:** Similar a Sobel, però amb un pes uniforme (tots '1' a les files/columnes exteriors).

#### Basats en la 2a Derivada (Detectors de Creuament per Zero)
Detecten el punt exacte de màxim canvi (el "creuament per zero" de la 2a derivada). Són excel·lents per **localitzar** la vora amb precisió.

* **Laplacian of Gaussian (LoG):** Primer aplica un filtre Gaussià (per suavitzar el soroll) i després el Laplacià (un kernel de 2a derivada).

#### Mètodes Multi-etapa
Són algorismes complets que combinen tècniques.

* **Canny:** És considerat l'estàndard "gold". No és un kernel, sinó un procés:
    1.  **Suavitzat:** Filtre Gaussià per eliminar soroll.
    2.  **Gradient:** Ús de Sobel per trobar magnitud i direcció.
    3.  **Supressió de No-Màxims:** Aprimar les vores a un sol píxel de gruix.
    4.  **Llindarització per Histeresi:** Utilitza dos llindars (alt i baix) per connectar vores fortes amb les febles, eliminant les febles aïllades.


## Què és o  perquè segmentar?
Volem segmentar per separar imatges i obtenir objectes
#### Estratègies
- Bottom-up
- Top-down
>[!example] Exemple de segmentació
>![[Pasted image 20251102130754.png]]
>![[Pasted image 20251102130811.png]]


>[!tip] Estratègia Bottom-Up 
>Comencem pels detalls (píxels) i els agrupem per formar regions més grans, sense un coneixement previ de l'objecte.

 >[!fail] **Problema:** 
 >La "coherència local" és subjectiva
 

 #### **Fitting (Top-Down)**
  Els píxels es queden junts perquè pertanyen a un mateix objecte (o model). 
  
  >[!tip] Estratègia Top-Down 
  >Comencem amb un model i trobem els píxels que millor s'ajusten (fit) a aquest model.
  >>(ex: "estic buscant una línia", "estic buscant una cara") 
  
    
# Clustering el plantejament
Agrupar punts similars i representar-los com a un simple token

Passos:
- [[#Què és o perquè segmentar?|Segmentar]]
- Resumir informació
	- Amb tota la info que tenimm li fem un path compression o denoise
	- representem això amb un únic token

Els edges al final són linies, nosaltres amb la segmentació volem contorns que unir

## Com segmentem i decidim què unir?

Hem de decidir quins pixels són similars
![[Pasted image 20251102131236.png]]


#### Grouping vs Fitting
##### Fitting
Fitting és una estratègia Top-Down
- Els pixels es queden junts pq estàn en un mateix objecte 

##### Grouping/Clustering
Els pixels estàn junts pq són localment coherents

El problema amb localment coherents és subjectiu, i pot tenir varies representacions
![[Pasted image 20251102131907.png]]
![[Pasted image 20251102131918.png]]
Tots aquests conceptes són intuitius, però moltdificils de traduïr a algoritme

A més a això se li suma la oclussió
![[Pasted image 20251102132050.png]]

Aquesta imatge no té sentit (almenys no literal) però com a humans podem reconeixer un objecte i "emplenar els espais" encara que no tingui sentit

També ens ajuda a reconeixer objectes
![[Pasted image 20251102132140.png]]

Fent ara això és més fàcil reconeixer:
![[Pasted image 20251102132156.png]]

## Background substraction
Si sabem com és el fons, serà més fàcil identificar "interesting bits"

#### Solució 1 Mediana
El que sabem del fons és que és estatic, o té canvis mínims, Per aquesta raó podem aplicar un filtre de mediana, que accentuarà els "pixels interesants" i normalitzarà el fons

>[!done] Pros
>Fàcil i ràpid

>[!fail] Contras
>1.-Necessites varies imatges
>2.-el fons ha de ser MOLT estàtic
>3.-segmentació sorollosa


## Video Segmentation
Dividir el video segons fotogrames interessants

![[Pasted image 20251102151223.png]]

Aquí hi ha 3 clars segments

Mirant al histograma:
![[Pasted image 20251102151253.png]]

Es pot veure un pic en el canvi d'intensitat

LLavors sabem quan dividir

### Algoritme per obtindre fons de videos:


>[!Summary] Algorisme
>
>1.-Obtain the difference between consecutive frames (e.g. by histograms differences)
>
>2.-Decide where there is a jump in the frames appearance.
>
>3.-Cut video segments.
>
>4.-Obtain the foreground image (e.g. using the median filter).
>
>5.-Extract the foreground objects of the detected video segments.1.-


>[!done] Pros
>Fàcil i ràpid

>[!fail] Contras
>1.- Massa simple, volem capturar també transicions continues
>2.- No separa i trackea objectes

# Clustering La explicació

#### Feature Space
la informació que volem i fem servir d'un pixel per descriure'l i tractar-lo
![[Pasted image 20251102152821.png]]
![[Pasted image 20251102152826.png]]

Depenent del que escollim, els grups de pixels variaràn molt.
En aquest cas, com que ho distribuïm segons intensitat i 
posició:

$$
Z= \pmatrix{I \\ x \\ y}
$$
![[Pasted image 20251102152931.png]]

### Com fem els clusters?

Tenim 2 approaches
- [[#Agglomerative clustering]]
- [[#K-means]]

#### Agglomerative clustering
Comença suposant cada punt com un cluster i es va ampliant fins cert criteri on para

>[!done] Pros
>Simple

>[!fail] Contras
>1.- Quan parem?
>2.- Com calcules la distància?
>3.- No aconseguim informació sobre la distribució dels pixels

##### Felzenszwalb (Efficient Graph-Based Segmentation)
És un mètode de clustering aglomeratiu (bottom-up) que tracta la imatge com un graf. La seva gran aportació és un **predicat de fusió** molt eficaç que decideix si dos clústers s'han d'unir o no, basant-se en la variabilitat interna de cada clúster.

> [!Summary] Idea Clau 
> - L'algorisme tracta cada píxel com un node d'un graf.
> 
>  - Les arestes connecten píxels veïns, i el pes de l'aresta és una mesura de la **dissimilaritat** (p.ex., diferència d'intensitat o color).
>  
>   - L'algorisme itera sobre les arestes ordenades per pes (de menor a major) i decideix si fusionar les dues regions (clústers) que connecten.

##### 1. Representació com a Graf

- **Nodes (V):** Cada píxel de la imatge.

- **Arestes (E):** Connecten cada píxel amb els seus veïns (p.ex., 8 veïns en una graella).

- **Pesos (w(vi​,vj​)):** La dissimilaritat entre els píxels vi​ i vj​. Per exemple, la diferència absoluta d'intensitat w=∣I(vi​)−I(vj​)∣.


##### 2. El Predicat de Fusió (La Clau)

Aquí és on rau la intel·ligència de l'algorisme. Per decidir si fusionar dos clústers C1​ i C2​, no només mira la diferència _entre_ ells, sinó que la compara amb la diferència _dins_ d'ells.

- **Diferència Interna (Int(C)):**
    
    - Es defineix com la dissimilaritat més gran _dins_ d'un clúster C.
    
    - Concretament, és el pes més alt de l'aresta en el **Minimum Spanning Tree (MST)** del clúster C.
    
    - _Intuïció:_ Mesura com de "poc suau" o variable és el clúster per dins. Un clúster molt homogeni tindrà un Int(C) baix.
    
- **Diferència Externa (Dif(C1​,C2​)):**
    
    - És la dissimilaritat _entre_ els dos clústers.
    
    - Es defineix com el pes de l'aresta w(vi​,vj​) que connecta C1​ i C2​ (amb vi​∈C1​,vj​∈C2​).
    
- **El Predicat (D):**
    
    - L'algorisme fusionarà C1​ i C2​ si la diferència _externa_ és "petita" en comparació amb les diferències _internes_.
    
    - La condició de fusió depèn d'un llindar que es defineix en relació a la variabilitat interna de cada component.
    
![[Pasted image 20251102155743.png]]

```python
segments_fz = segmentation.felzenszwalb(img, scale=100, sigma=0.5, min_size=50)

plt.imshow(segmentation.mark_boundaries(img, segments_fz))
```

> [!quote] Regla de Fusió 
> Es fusionen C1​ i C2​ si la diferència entre ells (Dif) és més petita o igual que la diferència interna mínima d'algun dels dos clústers, ajustada per un llindar.
> 
> Formalment, es fusionen si: 
> $Dif(C1​,C2​)≤min(Int(C1​)+τ(C1​),Int(C2​)+τ(C2​))$
> 
> On $τ(C)=k/∣C∣$ és un **llindar adaptatiu**:
> 
> - k és un paràmetre constant que estableix l'escala de la segmentació (un valor k més gran afavoreix clústers més grans).
>     
> - ∣C∣ és la mida (nombre de píxels) del clúster.
>     
> 
> _Significat:_ Per a clústers petits, τ(C) és gran, la qual cosa permet que es fusionin fàcilment (permet més variabilitat interna). Per a clústers grans, τ(C) és petit, fent més difícil que es fusionin.

##### 3. Algorisme

> [!Summary] Passos de l'Algorisme
> 
> 1. S'aplica un filtre Gaussià (σ) per suavitzar lleugerament la imatge (opcional, però recomanat).
>     
> 2. Es construeix el graf G=(V,E) amb els pesos w calculats entre píxels veïns.
>     
> 3. S'ordenen totes les arestes E per pes w de forma no decreixent (de més similar a menys similar).
>     
> 4. S'inicialitza la segmentació: cada píxel v és el seu propi clúster Cv​.
>     
> 5. Es recorre la llista d'arestes ordenades. Per a cada aresta (vi​,vj​) amb pes w:
>     
> 
> - Identifica els clústers actuals Ci​ (que conté vi​) i Cj​ (que conté vj​).
>     
> - Si Ci​=Cj​ (no estan ja al mateix clúster) **I** el predicat D(Ci​,Cj​) és cert (és a dir, w≤min(Int(Ci​)+τ(Ci​),Int(Cj​)+τ(Cj​))), es fusionen els dos clústers (C=Ci​∪Cj​).
>     
> - En fusionar-se, es recalcula la nova Diferència Interna: Int(C)=w (ja que w és l'aresta més gran que connecta les dues sub-parts).
>     
> 
> 6. (Opcional) Després de l'algorisme, es fusionen totes les regions més petites que un `min_size` determinat amb les regions veïnes més similars.
>     

---

> [!done] Pros
> 
> 1. **Molt eficient:** Té una complexitat gairebé lineal (O(NlogN) on N és el nombre de píxels) gràcies a l'ordenació de les arestes i l'ús d'estructures de dades eficients (Disjoint-set).
>     
> 2. **Propietats globals:** Tot i prendre decisions "greedy" (locals), l'algorisme produeix segmentacions que respecten propietats globals de la imatge.
>     
> 3. **Preserva detalls:** És bo preservant detalls en regions de baixa variabilitat, mentre ignora detalls (soroll) en regions d'alta variabilitat.
>     

> [!fail] Contras
> 
> 4. **Sensible als paràmetres:** L'aparença final de la segmentació depèn molt dels paràmetres k (escala), σ (suavitzat inicial) i `min_size`. Trobar els valors correctes requereix ajust manual (tuning).
>     
> 5. **No és semàntic:** Com la majoria de mètodes "bottom-up", agrupa per aparença (color/intensitat), no per significat (no sap què és "cotxe" o "arbre").
>

#### K-means
Reassignant iterativament punts al centre de clúster més proper. És un mètode de partició, no aglomeratiu.

Inicia escollint punts d'inici de cluster de mmanera aleatoria

![[Pasted image 20251102160207.png]]

Post algorisme acaba obtenint punts que convergeixen en un minim loca
![[Pasted image 20251102160234.png]]

>[!Summary] Algorisme K-means
>
>1.  **Inicialització:** Escollir $K$ punts del *feature space* aleatòriament (o amb una estratègia) com a centroides inicials.
>2.  **Pas d'Assignació:** Per a cada píxel, calcular la distància al $K$ centroides. Assignar el píxel al clúster del centroide més proper.
>3.  **Pas d'Actualització:** Recalcular la posició de cada centroide com la **mitjana** de tots els píxels que li han estat assignats.
>4.  **Iterar:** Repetir els passos 2 i 3 fins que els centroides no es moguin (convergència) o s'arribi a un nombre màxim d'iteracions.

>[!done] Pros
>1.- Simple i ràpid de calcular, especialment per a grans conjunts de dades.
>2.- Convergeix generalment ràpid.

>[!fail] Contras
>1.- **Cal triar $K$ (el nombre de clústers) a priori.**
>2.- **Sensible a la inicialització:** Diferents inicialitzacions poden portar a resultats (mínims locals) diferents.
>3.- **Assumeix que els clústers són esfèrics** i de mida similar. No funciona bé amb formes complexes o densitats diferents.
>4.- **Requereix molta memòria**
>5.-**Sensitiu a elements llunyans** (outlier)
>
![[Pasted image 20251102161803.png]]

#### SLIC
>[!quote] Simple linear iterative clustering

Una implementació optimitzada del Kmeans

**SLIC** és un algorisme de segmentació que agrupa píxels en "superpíxels" (regions compactes i perceptivament homogènies). No és un algorisme de clustering general, sinó una adaptació dissenyada específicament per a imatges.

L'objectiu és reemplaçar la graella rígida de píxels per una representació de més alt nivell (els superpíxels), la qual cosa accelera molt els algorismes posteriors.

```python
segments_slic = segmentation.slic(img, n_segments=20, compactness=0.1, sigma=1)
plt.imshow(segmentation.mark_boundaries(img, segments_slic))
```
## Quick Shift
El millor 

**Quick Shift** és un algorisme de segmentació (mode-seeking) que connecta cada píxel amb el seu veí més proper (en l'espai i el color) que tingui una densitat de píxels més alta. Aquest procés crea un bosc d'arbres on cada arbre convergeix cap a un màxim local (un mode de densitat), i cada arbre representa un clúster.

>[!Summary] Algorisme
>1. **Càlcul de Densitat:** Per a cada píxel, s'estima la seva densitat (p.ex., utilitzant un filtre Gaussià) basant-se en els píxels veïns en l'espai de característiques (p.ex., 5D: Lab + xy).
>2. **Construcció de l'Arbre:** Cada píxel i s'enllaça amb el píxel j més proper que compleixi: Densitat(j)>Densitat(i).
>3. **Formació de Clústers:** Els píxels que són màxims locals de densitat (no tenen cap veí més dens) actuen com a arrels. Tots els píxels que s'enllacen (directament o indirectament) a la mateixa arrel formen un clúster.

>[!done] Pros
>- **Jeràrquic:** L'arbre resultant es pot tallar a diferents nivells per obtenir segmentacions a múltiples escales (més o menys clústers).
>    
>- **No requereix K:** El nombre de clústers es determina automàticament a partir de les dades.
>    
>- **Troba formes complexes:** Com que es basa en la densitat, no està limitat a clústers esfèrics.

>[!fail] Contras
>
>- **Sensible als Paràmetres:** El resultat és molt sensible a l'elecció de l'amplada de banda del filtre (sigma), que defineix què es considera "veí" per calcular la densitat.
>    
>- **Cost Computacional:** Calcular les densitats i trobar els veïns més propers per a cada píxel pot ser computacionalment costós.

![[Pasted image 20251102162416.png]]

```python

segments_quick = segmentation.quickshift(img, kernel_size=3, max_dist=6, ratio=0.5)

plt.imshow(segmentation.mark_boundaries(img, segments_quick))
"""
max_dist : 
float, optional, Cut-off point for data distances. Higher means fewer clusters.
"""

"""
ratio : 
float, optional, between 0 and 1, Balances color-space proximity and image-space proximity. Higher values give more weight to color-space.
"""
```

