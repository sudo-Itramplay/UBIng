## **Visió General del Processament d'Imatges amb Scikit-image 🖼️**

El processament d'imatges digitals amb Python es recolza fonamentalment en tres llibreries clau:

- **[[Scikit-image]]**: És la biblioteca principal per a la manipulació i l'anàlisi d'imatges.
    
- **[[Numpy]]**: Proporciona l'estructura de dades subjacent, ja que les imatges es representen com a _arrays_ de Numpy.
    
- **[[Matplotlib]]**: S'utilitza per a la visualització de les imatges i els resultats.
    

### **Estructura Fonamental d'una Imatge**

Una imatge es representa com una matriu, normalment de 3 dimensions: **(alçada, amplada, canals)**.

- Els canals solen ser 3 (Vermell, Verd, Blau - RGB).
    
- El tipus de dades (`dtype`) més comú és `uint8`, que emmagatzema valors enters entre 0 i 255, perfecte per representar la intensitat de cada canal de color. Aquest és un dels [[Atributs Scikit-image|atributs]] bàsics d'una imatge.
    

---

## **El Cicle de Vida d'una Imatge: Manipulació i Anàlisi ⚙️**

El flux de treball típic en el processament d'imatges segueix uns passos lògics, des de la càrrega fins al desament, passant per diverses transformacions.

### **1. Càrrega i Creació**

El primer pas és obtenir una imatge. Podem fer-ho de dues maneres:

- **Carregar des d'un fitxer**: Utilitzant `io.imread('arxiu.png')`.
    
- **Crear una imatge des de zero**: Per exemple, per crear una imatge completament negra, fem servir `np.zeros()`, especificant les dimensions i el `dtype=np.uint8`.
    

### **2. Modificació i Transformació**

Un cop tenim la imatge carregada com un _array_ de Numpy, podem començar a manipular-la.

#### **Modificacions de Píxels i Valors**

Podem [[Com modificar Valors d'una imtge|modificar valors d'una imatge]] directament accedint a les seves coordenades com si fos una matriu. Per exemple, per posar la meitat dreta d'una imatge en blanc (valor 255), faríem `img[:, 50:] = 255`.

És crucial anar amb compte amb el tipus de dades en fer operacions aritmètiques:

- Si multipliquem (p. ex., per augmentar la brillantor), podem [[Excedir valor del uint8|excedir el valor màxim de `uint8` (255)]], causant un efecte de _wrapping_.
    
- Si dividim (p. ex., per enfosquir), el `dtype` canvia a `float64`, creant [[Decimals en Scikit|decimals en Scikit]]. Per visualitzar-la correctament, caldria reconvertir-la a enters amb `.astype(int)`.
    

#### **Transformacions Geomètriques**

- **[[Voltejar imatges]]**: Es pot fer fàcilment amb funcions de Numpy com `np.flipud(img)` o amb _slicing_ `img[::-1, :]`.
    
- **[[Reescalat Scikit]]**: La llibreria `skimage.transform` ofereix funcions com `rescale` o `resize` per canviar la mida de les imatges de manera eficient.
    

#### **Conversió de Color i Canals**

Les imatges es poden transformar a diferents espais de color. La conversió més comuna és a escala de grisos, que resulta en [[Imatges en 1 canal|imatges en 1 canal]].

- Això es fa amb la funció `rgb2gray` del mòdul `skimage.color`.
    
- Aquesta operació no és una simple mitjana, sinó una suma ponderada dels canals RGB per reflectir la lluminositat percebuda per l'ull humà.
    

### **3. Segmentació i Anàlisi**

Sovint, l'objectiu és aïllar objectes o regions d'interès.

- **[[Mascares]]**: Una màscara és un _array_ booleà (`True`/`False`) que ens permet seleccionar píxels que compleixen una certa condició (p. ex., que no siguin negres). Aplicant la màscara a una imatge (`img[mask]`), podem modificar només les parts seleccionades.
    
- **[[Binary thresholding]]**: És una tècnica senzilla per binaritzar una imatge. Es calcula un llindar (p. ex., la mitjana de grisos) i tots els píxels per sobre es converteixen en blanc (255) i els de sota en negre (0), creant una imatge binària.
    

### **4. Visualització i Desament**

Finalment, mostrem o guardem els resultats.

- **Visualització**:
    
    - S'utilitza `plt.imshow(img)`. En el cas d'imatges d'un sol canal, és important especificar `cmap='gray'` per evitar que Matplotlib apliqui un mapa de colors per defecte.
        
    - Per mostrar-ne diverses, podem crear una graella amb `plt.subplots()`. Això ens dona accés als eixos (`ax`) de cada subgràfic.
        
    - És una bona pràctica [[Matplotlib Amagar eixos|amagar els eixos]] amb `ax.axis('off')` per a una presentació més neta.
        
- **Desament**:
    
    - Per guardar la imatge resultant al disc, fem servir `io.imsave('nom_nou.png', img)`.
        

Aquest flux de treball, que combina les capacitats de càlcul de Numpy, les funcions especialitzades de [[Scikit-image]] i la potència de visualització de Matplotlib, constitueix la base del processament d'imatges en Python.