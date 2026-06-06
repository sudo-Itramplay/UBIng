- [[#Imports]]
- [[#AUX]]
	- [[#PLOT SIFT AUX|PLOT SIFT AUX]]
- [[#1.- Template Matching]]
	- [[#1.1.- SSD|1.1.- SSD]]
	- [[#1.2.-NCC|1.2.-NCC]]
	- [[#1.3.- Funcions auxiliars|1.3.- Funcions auxiliars]]
		- [[#1.3.- Funcions auxiliars#Extra:|Extra:]]
	- [[#1.4.- Explicacions|1.4.- Explicacions]]
		- [[#1.4.- Explicacions#1. Sensibilitat al Contrast|1. Sensibilitat al Contrast]]
		- [[#1.4.- Explicacions#2. Comportament de les Mètriques|2. Comportament de les Mètriques]]
			- [[#2. Comportament de les Mètriques#A. Distància Euclidiana (SSD - Sum of Squared Differences)|A. Distància Euclidiana (SSD - Sum of Squared Differences)]]
			- [[#2. Comportament de les Mètriques#B. NCC (Normalized Cross-Correlation)|B. NCC (Normalized Cross-Correlation)]]
		- [[#1.4.- Explicacions#3. Paràmetres i Millor Opció|3. Paràmetres i Millor Opció]]
			- [[#3. Paràmetres i Millor Opció#Paràmetres Clau|Paràmetres Clau]]
			- [[#3. Paràmetres i Millor Opció#La Millor Opció|La Millor Opció]]
		- [[#1.4.- Explicacions#1.5 Pq passa lo de la rotació?|1.5 Pq passa lo de la rotació?]]
			- [[#1.5 Pq passa lo de la rotació?#1. L'Algorisme (Fonaments)|1. L'Algorisme (Fonaments)]]
			- [[#1.5 Pq passa lo de la rotació?#2. Avaluació Tècnica|2. Avaluació Tècnica]]
				- [[#2. Avaluació Tècnica#Avantatges vs. Inconvenients|Avantatges vs. Inconvenients]]
			- [[#1.5 Pq passa lo de la rotació?#3. Sensibilitat i Mètriques|3. Sensibilitat i Mètriques]]
				- [[#3. Sensibilitat i Mètriques#Paràmetres Clau|Paràmetres Clau]]
- [[#2.- HOG]]
	- [[#2.1.-Conceptes|2.1.-Conceptes]]
		- [[#2.1.-Conceptes#HOG (Histogram of Oriented Gradients)|HOG (Histogram of Oriented Gradients)]]
			- [[#HOG (Histogram of Oriented Gradients)#1. Concepte Fonamental|1. Concepte Fonamental]]
			- [[#HOG (Histogram of Oriented Gradients)#2. Paràmetres Clau del Codi (`skimage.feature.hog`)|2. Paràmetres Clau del Codi (`skimage.feature.hog`)]]
			- [[#HOG (Histogram of Oriented Gradients)#3. Interpretació de la Visualització (`visualize=True`)|3. Interpretació de la Visualització (`visualize=True`)]]
			- [[#HOG (Histogram of Oriented Gradients)#4. Diferència en el Vector Resultant|4. Diferència en el Vector Resultant]]
	- [[#2.2.- HOG amb diferents paràmetres|2.2.- HOG amb diferents paràmetres]]
		- [[#2.2.- HOG amb diferents paràmetres#2.1.1.- Info per HOG|2.1.1.- Info per HOG]]
		- [[#2.2.- HOG amb diferents paràmetres#2.1.2.- Detectar persones donat template|2.1.2.- Detectar persones donat template]]
		- [[#2.2.- HOG amb diferents paràmetres#PQ faia HOG?|PQ faia HOG?]]
			- [[#PQ faia HOG?#🔴 Motius principals de fallada|🔴 Motius principals de fallada]]
	- [[#2.3 .-HOG VS TEMPLATE BASED:|2.3 .-HOG VS TEMPLATE BASED:]]
		- [[#2.3 .-HOG VS TEMPLATE BASED:#🔎 Anàlisi del Procés de Detecció d'Objectes|🔎 Anàlisi del Procés de Detecció d'Objectes]]
		- [[#2.3 .-HOG VS TEMPLATE BASED:#1. L'Algorisme HOG (Resum)|1. L'Algorisme HOG (Resum)]]
		- [[#2.3 .-HOG VS TEMPLATE BASED:#2. Comparativa: HOG vs. Template Matching|2. Comparativa: HOG vs. Template Matching]]
- [[#3.- ORB]]
	- [[#3.0.1.- DoG (diferences of gaussian)|3.0.1.- DoG (diferences of gaussian)]]
	- [[#3.1- ORB (Oriented FAST and Rotated BRIEF)|3.1- ORB (Oriented FAST and Rotated BRIEF)]]
	- [[#3.2 Implementació de ORB|3.2 Implementació de ORB]]
		- [[#3.2 Implementació de ORB#3.3.1 Característiques ORB vs HOG|3.3.1 Característiques ORB vs HOG]]
		- [[#3.2 Implementació de ORB#3.4 Anàlisi de tècniques i resultats (ORB)|3.4 Anàlisi de tècniques i resultats (ORB)]]
		- [[#3.2 Implementació de ORB#1. Avantatges d'ORB vs. HOG i _Template Matching_|1. Avantatges d'ORB vs. HOG i _Template Matching_]]
		- [[#3.2 Implementació de ORB#2. Anàlisi d'imatges sense l'objecte (Cas Negatiu)|2. Anàlisi d'imatges sense l'objecte (Cas Negatiu)]]
		- [[#3.2 Implementació de ORB#3. Definició d'una mesura de qualitat de correspondència|3. Definició d'una mesura de qualitat de correspondència]]
- [[#4 SIFT]]
	- [[#4.1.- Implementació SIFT|4.1.- Implementació SIFT]]
	- [[#4.2 Best match amb SIFT|4.2 Best match amb SIFT]]
	- [[#Exc 1 HOG amb angle i canvi de brightness|Exc 1 HOG amb angle i canvi de brightness]]
	- [[#Exc 2 Orb amb Noise, blur i rotation|Exc 2 Orb amb Noise, blur i rotation]]
	- [[#Exc 3 SIFT amb diferents sizes (100%, 75%, ...)|Exc 3 SIFT amb diferents sizes (100%, 75%, ...)]]
	- [[#Exc 4 Parameter optimization|Exc 4 Parameter optimization]]
	- [[#Exc 5 David - Best image|Exc 5 David - Best image]]

---
# Imports
```python
from skimage.feature import hog 
from skimage import exposure, io, color, transform, feature, measure 
from skimage.feature import ORB, match_descriptors from skimage.feature import SIFT 
from matplotlib import patches 
import matplotlib.pyplot as plt 
import numpy as np 
import os 
import glob 
import time
```


# AUX

Hi ha un mètode (Sobretot al final amb sift) que pot donar problemes

## PLOT SIFT AUX

```python
# In case the plot_matches() function gives you some problems, you can use the following one:

  

from skimage.util import img_as_float

import numpy as np

  

def plot_matches_aux(ax, image1, image2, keypoints1, keypoints2, matches,

keypoints_color='k', matches_color=None, only_matches=False):

  
  

image1 = img_as_float(image1)

image2 = img_as_float(image2)

  

new_shape1 = list(image1.shape)

new_shape2 = list(image2.shape)

  

if image1.shape[0] < image2.shape[0]:

new_shape1[0] = image2.shape[0]

elif image1.shape[0] > image2.shape[0]:

new_shape2[0] = image1.shape[0]

  

if image1.shape[1] < image2.shape[1]:

new_shape1[1] = image2.shape[1]

elif image1.shape[1] > image2.shape[1]:

new_shape2[1] = image1.shape[1]

  

if new_shape1 != image1.shape:

new_image1 = np.zeros(new_shape1, dtype=image1.dtype)

new_image1[:image1.shape[0], :image1.shape[1]] = image1

image1 = new_image1

  

if new_shape2 != image2.shape:

new_image2 = np.zeros(new_shape2, dtype=image2.dtype)

new_image2[:image2.shape[0], :image2.shape[1]] = image2

image2 = new_image2

  

image = np.concatenate([image1, image2], axis=1)

  

offset = image1.shape

  

if not only_matches:

ax.scatter(keypoints1[:, 1], keypoints1[:, 0],

facecolors='none', edgecolors=keypoints_color)

ax.scatter(keypoints2[:, 1] + offset[1], keypoints2[:, 0],

facecolors='none', edgecolors=keypoints_color)

  

ax.imshow(image, interpolation='nearest', cmap='gray')

ax.axis((0, 2 * offset[1], offset[0], 0))

  

for i in range(matches.shape[0]):

idx1 = matches[i, 0]

idx2 = matches[i, 1]

  

if matches_color is None:

color = np.random.rand(3)

else:

color = matches_color

  

ax.plot((keypoints1[idx1, 1], keypoints2[idx2, 1] + offset[1]),

(keypoints1[idx1, 0], keypoints2[idx2, 0]),

'-', color=color)
```

# 1.- Template Matching


## 1.1.- SSD 
Fem servir la distància euclidiana ($\sqrt{a^2 + b^2}$) del template a una regió de la imatge

**Importants**:
- **Normalització**: Divideix els valors dels píxels per 255.0 per tenir valors entre ​[0,1]
   
- **Finestra lliscant**: Desplaça la plantilla píxel a píxel per tota la imatge﻿ ( o cada dos, fes salts )
    

- **Càlcul de distància**: Utilitza﻿ `np.linalg.norm(region - template)` per cada posició﻿

 - **Millor coincidència**: La posició amb la distància **mínima** és la correcta
```python

# ssd distance
def ssd_template_matching(image, template, threshold=0.5):

h_img, w_img = image.shape

h_tpl, w_tpl = template.shape

# The result map will have dimensions (H_img - H_tpl + 1, W_img - W_tpl + 1)

h_res, w_res = h_img - h_tpl + 1, w_img - w_tpl + 1

ssd_result = np.zeros((h_res, w_res), dtype=np.float64)

  

# This loop is still necessary but the inner calculations are vectorized by numpy

for y in range(h_res):

	for x in range(w_res):
	# Extract the current window from the image
	window = image[y:y+h_tpl, x:x+w_tpl]
	
	
	"""
	AQUí ES FA EN ESSENCIA:
	`distance = np.linalg.norm(region - template)`
	
	"""
	
	# Calculate the Sum of Squared Differences (SSD) for this window	
	diff = window - template
	squared_diff = diff**2
		# Sum all elements in the squared difference matrix
	current_ssd = np.sum(squared_diff)
	"""
	FINS AQUI
	"""
	ssd_result[y, x] = current_ssd
	# For SSD, the best match is the MINIMUM value

thresholded = np.zeros_like(ssd_result).astype(np.uint8)

thresholded[ssd_result < threshold] = 1

# we want to get the central locations of each connected component

locations = get_connected_component_centroids(thresholded)

  

return locations, ssd_result, thresholded

```

## 1.2.-NCC
--Correlació creuada
Mesura la simlitud entre plantilla i regions d'imatge amb `skimage.features.match_template` 

```python
def ncc_template_matching(image, template, threshold=0.5):

	ncc_result = feature.match_template(image, template, pad_input=False)
	
	# For NCC, the best match is the MAXIMUM value
	
	thresholded = np.zeros_like(ncc_result).astype(np.uint8)
	
	thresholded[ncc_result > threshold] = 1
	
	locations = get_connected_component_centroids(thresholded)
	
	return locations, ncc_result, thresholded
```

## 1.3.- Funcions auxiliars 
```python
def ensure_gray(image):

	if image.ndim == 3:
	
		if image.shape[-1] == 4:
			image = color.rgba2rgb(image)
		
		if image.shape[-1] == 3:
			return color.rgb2gray(image)
	
	return image

  

def normalize(image):

	if image.max() > 1.:
		image = image.astype(np.float32) / 255.
	return image

  

def get_connected_component_centroids(binary_image):

	labeled_image = measure.label(binary_image)
	
	properties = measure.regionprops(labeled_image)
	
	centroids = []
	
	for prop in properties:
		centroids.append((int(prop.centroid[1]), int(prop.centroid[0]))) # (x, y)
	
	return centroids

  

  

def plot_template_matching(image, template, locations, result_map, thresholded, title):

	# Get the coordinates for drawing the rectangle
	w, h = template.shape[::-1] # Template width and height
	fig, axes = plt.subplots(1, 4, figsize=(13, 4), sharex=False, sharey=False)
	
	
	ax = axes.ravel()
	
	ax[0].imshow(template, cmap=plt.cm.gray)
	ax[0].set_title('Template')
	ax[0].set_axis_off()
	
	ax[1].imshow(image, cmap=plt.cm.gray)
	ax[1].set_title('Source Image')
	ax[1].set_axis_off()
	
	for top_left in locations:
		ax[1].add_patch(plt.Rectangle(top_left, w, h, edgecolor='r', facecolor='none', linewidth=2))
	
	  
	
	ax[2].imshow(thresholded, cmap='gray')
	ax[2].set_title("Thresholded")
	ax[2].set_axis_off()
	
	ax[3].imshow(result_map, cmap='viridis')
	ax[3].set_title('Result Map')
	ax[3].set_axis_off()
	
	plt.suptitle(title)
	plt.tight_layout()
	plt.show()

  

def run_template_matching(image_path, template_path, ssd_threshold=65, ncc_threshold=0.6):

	if isinstance(image_path, str):
		image = ensure_gray(io.imread(image_path))
	
	else:
		image = ensure_gray(image_path)
	
	if isinstance(template_path, str):
		template = ensure_gray(io.imread(template_path))
	
	else:
		template = ensure_gray(template_path)
	
	image, template = normalize(image), normalize(template)
	
	ssd_locations, ssd_result_map, ssd_thresholded = ssd_template_matching(image, template, threshold=ssd_threshold)
	
	plot_template_matching(image, template, ssd_locations, ssd_result_map, ssd_thresholded, "SSD")
	
	ncc_locations, ncc_result_map, ncc_thresholded = ncc_template_matching(image, template, threshold=ncc_threshold)
	
	plot_template_matching(image, template, ncc_locations, ncc_result_map, ncc_thresholded, "NCC")
	
	  
	
	return ssd_result_map, ncc_result_map
```

Aquests mapes proporcionen informació de la imatge
Com:
```python
print("Minimum SSD value:", ssd_result_map.min())

print("Maximum NCC value:", ncc_result_map.max())
```

Es veu que aquest ,mètode varia segons intensitat, fent servir una imatge amb un quadre negre trobem:
![[Pasted image 20251202113010.png]]


### Extra:
Patches
```python

x1, y1 = 160, 310 # approximate location of the left eye
x2, y2 = 290, 310 # approximate location of the right eye
eyes = [(x1, y1), (x2, y2)]
eye = ensure_gray(io.imread("images/eye.png"))
patch_w, patch_h = eye.shape[::-1]

fig, ax = plt.subplots(figsize=(8, 6))
ax.imshow(ssd_result_map, cmap='viridis')
ax.add_patch(
	plt.Rectangle(
		(x1-patch_w//2, y1-patch_h//2), 
		patch_w,
		patch_h,
		edgecolor='r', 
		facecolor='none', 
		linewidth=2
	)
)


ax.add_patch(
	plt.Rectangle(
		(x2-patch_w//2, y2-patch_h//2), 
		patch_w, 
		patch_h, 
		edgecolor='r', 
		facecolor='none', 
		linewidth=2
	)
)
```

## 1.4.- Explicacions

### 1. Sensibilitat al Contrast

> Pregunta: Els algorismes es veuen afectats pels canvis de contrast?
> 
> Resposta: Sí.

- **Explicació Tècnica:** El _Template Matching_ bàsic opera comparant directament els valors d'intensitat dels píxels (nivells de gris o RGB).

- **El Problema:** Un canvi de contrast és, matemàticament, una transformació lineal o no lineal dels valors del píxel ($I'(x,y) = \alpha \cdot I(x,y) + \beta$).

- **Conseqüència:** Si l'algorisme busca una coincidència exacta de valors (com fa la diferència absoluta), un simple canvi de llum farà que $Template \neq Image$, encara que la forma de l'objecte sigui idèntica. L'aparença de les característiques (_features_) es distorsiona numèricament.


---

### 2. Comportament de les Mètriques

> **Pregunta:** Com canvien la distància Euclidiana i la NCC? Hi ha grans diferències?

Aquí comparem dues aproximacions fonamentals: la **geomètrica** (Euclidiana) i l'**estadística** (NCC).

#### A. Distància Euclidiana (SSD - Sum of Squared Differences)

- **Fórmula Conceptual:** Es basa en la diferència resta directa: $\sum (T - I)^2$.
    
- **Comportament:** És **molt sensible** als canvis d'energia (brillantor/contrast).
    
- **Resultat:** Si augmenta el contrast, la diferència numèrica entre la plantilla i la imatge creix dràsticament.
    
    - _Mètrica:_ Valors molt **alts** (indica mala coincidència, tot i ser el mateix objecte).
        

#### B. NCC (Normalized Cross-Correlation)

- **Fórmula Conceptual:** Mesura la similitud de la "forma" del senyal, normalitzant la intensitat mitjançant la desviació estàndard.
    
- **Comportament:** Està dissenyada per ser invariant a canvis lineals de brillantor i contrast.
    
- **Resultat:** Tot i que en casos extrems o no lineals el valor pot baixar (indicant pitjor coincidència), la caiguda és molt menys severa que l'error en l'Euclidiana.
    
    - _Mètrica:_ Valors més propers a $1.0$ (o menys afectats) comparat amb SSD.
        

|**Mètrica**|**Sensibilitat al Contrast**|**Interpretació del valor**|
|---|---|---|
|**Euclidiana (SSD)**|Alta (Mala)|$\uparrow$ Valor = $\downarrow$ Similitud|
|**NCC**|Baixa (Bona)|$\uparrow$ Valor = $\uparrow$ Similitud|

---

### 3. Paràmetres i Millor Opció

> **Pregunta:** Quins paràmetres té i quina mesura funciona millor?

#### Paràmetres Clau

1. **Mètrica de Similitud:** L'elecció matemàtica de comparació (SSD, NCC, SAD, etc.). És el factor més determinant.
    
2. **Mida de la Plantilla ($T$):** Dimensions de la finestra lliscant. Una plantilla massa petita genera "falsos positius"; una massa gran és computacionalment costosa i sensible a oclusions.
    
3. **Threshold (Llindar):** El valor de tall per acceptar una coincidència com a vàlida.
    

#### La Millor Opció

- **Guanyador:** **NCC (Normalized Cross-Correlation)**.
    
- **Justificació:** En entorns reals (no controlats), la il·luminació rarament és constant. L'NCC ofereix la millor **robustesa** perquè prioritza la correlació estructural per sobre de la intensitat absoluta dels píxels. L'SSD només és útil si garantim que la il·luminació és idèntica entre la plantilla i la imatge objectiu.
    

---

> [!INFO] Resum pel Professor
> 
> L'ús de mètriques simples com la distància Euclidiana és ingenu en visió per computador real degut a la variabilitat de la llum. La normalització estadística (NCC) és un requisit gairebé obligatori per obtenir resultats fiables.


```python
# ROTACIONS
image = ensure_gray(io.imread("images/einstein.png"))

template = ensure_gray(io.imread("images/eye.png"))

  

for angle in [2, 5, 10, 15, 20]:

	rotated_template = transform.rotate(template, angle, resize=True)
	
	ssd_locations, ssd_result_map, ssd_thresholded = ssd_template_matching(image, rotated_template, threshold=65)
	
	plot_template_matching(image, rotated_template, ssd_locations, ssd_result_map, ssd_thresholded, f"SSD - Rotated {angle}")
	
	  
	
	ncc_locations, ncc_result_map, ncc_thresholded = ncc_template_matching(image, rotated_template, threshold=0.6)
	
	plot_template_matching(image, rotated_template, ncc_locations, ncc_result_map, ncc_thresholded, f"NCC - Rotated {angle}")
```


### 1.5 Pq passa lo de la rotació?
#### 1. L'Algorisme (Fonaments)

El **Template Matching** és una tècnica de força bruta per trobar una sub-imatge (plantilla) dins d'una imatge més gran.

- **Funcionament:** Es mou la plantilla ("sliding window") sobre la imatge original, píxel a píxel.
    
- **Càlcul:** A cada posició $(x, y)$, es calcula una mesura de similitud entre la plantilla i la regió coberta.
    

#### 2. Avaluació Tècnica

##### Avantatges vs. Inconvenients

|**Avantatges**|**Inconvenients**|
|---|---|
|✅ **Simplicitat:** Molt fàcil d'entendre i implementar.|❌ **Fragilitat:** No suporta canvis d'escala, rotació o il·luminació severa.|
||❌ **Cost Computacional:** Pot ser molt lent en imatges grans ($O(N \cdot M)$).|

#### 3. Sensibilitat i Mètriques

L'algorisme és **sensible als canvis de contrast**. Si la il·luminació canvia, els valors dels píxels canvien, i la comparació directa pot fallar.

##### Paràmetres Clau

L'èxit depèn principalment de la **mètrica de comparació** triada:

1. **SSD (Sum of Squared Differences):**
    
    - Més simple matemàticament.
        
    - Molt sensible a canvis de llum (no recomanat si el contrast varia).
        
2. **NCC (Normalized Cross Correlation):**
    
    - Més complexa de calcular.
        
    - **Més robusta:** Normalitza els valors, fent-la resilient a canvis de contrast i il·luminació.
        

> **Nota del Professor:** Si treballes en entorns on la llum no està controlada, utilitza sempre **NCC** en lloc de SSD o diferències absolutes.



# 2.- HOG
## 2.1.-Conceptes

### HOG (Histogram of Oriented Gradients)

#### 1. Concepte Fonamental

El descriptor HOG es basa en la hipòtesi que l'aparença i la forma dels objectes locals es poden caracteritzar per la distribució de **direccions de gradients d'intensitat** (vores). No mira el color, sinó "cap a on canvia la llum".

> **Analogia:** Imagina que dibuixes el contorn d'un objecte només amb petites línies rectes que indiquen la direcció de la vora. Això és el que veu HOG.

#### 2. Paràmetres Clau del Codi (`skimage.feature.hog`)

En el teu exercici estàs comparant dues configuracions. Aquests paràmetres defineixen la "resolució" i sensibilitat del descriptor:

- **`pixels_per_cell` (e.g., $8\times8$ vs $4\times4$):**
    
    - Divideix la imatge en una graella (cel·les).
        
    - Dins de cada cel·la, es calcula un **histograma** local.
        
    - **Efecte:** Cel·les més petites ($4\times4$) capturen detalls més fins però generen un vector de característiques molt més llarg (més cost computacional).
        
- **`orientations` (e.g., 9 vs 8):**
    
    - El nombre de "bins" o calaixos de l'histograma.
        
    - Divideix els $180^\circ$ (o $360^\circ$) en $N$ direccions.
        
    - **Efecte:** Més orientacions permeten discriminar millor la curvatura de les vores, però augmenten la mida del vector.
        
- **`cells_per_block` (e.g., $3\times3$ vs $2\times2$):**
    
    - Agrupació de cel·les per a **normalitzar** la il·luminació.
        
    - Es mou una finestra (bloc) sobre la graella de cel·les per contrastar els histogrames locals respecte als veïns.
        
    - **Important:** Això fa que el descriptor sigui robust a canvis d'il·luminació i ombres.
        

#### 3. Interpretació de la Visualització (`visualize=True`)

A les imatges generades (`hog_img_def` i `hog_img_cust`):

- **Les línies blanques:** Representen la direcció dominant del gradient en aquella cel·la.
    
- **La intensitat (brillantor) de la línia:** Representa la magnitud del gradient (com de forta és la vora).
    
    - _Línia brillant:_ Vora molt marcada (e.g., contorn de la persona).
        
    - _Negre:_ Zona plana/sense canvis (e.g., fons llis).
        

#### 4. Diferència en el Vector Resultant

El teu codi imprimeix `len={hog_cust.size}`. Notaràs una diferència massiva:

1. **Default ($8\times8$ px, $3\times3$ blocs):** Vector més compacte. Captura l'estructura general.
    
2. **Custom ($4\times4$ px, $2\times2$ blocs):** Vector molt més llarg (més cel·les = més histogrames). Captura detalls d'alta freqüència.
    

## 2.2.- HOG amb diferents paràmetres
```python
from skimage.feature import hog

from skimage import exposure

  

# read and prepare template (reuses ensure_gray and normalize from earlier cells)

tpl = ensure_gray(io.imread("images/person_template.bmp"))

tpl = normalize(tpl)

  

# default HOG (skimage default: orientations=9, pixels_per_cell=(8,8), cells_per_block=(3,3))

hog_def, hog_img_def = hog(tpl,

orientations=9,

pixels_per_cell=(8, 8),

cells_per_block=(3, 3),

visualize=True,

feature_vector=True,

block_norm='L2-Hys')

  

# custom HOG: 4x4 pixels per cell, 2x2 cells per block, 8 orientations

hog_cust, hog_img_cust = hog(tpl,

orientations=8,

pixels_per_cell=(4, 4),

cells_per_block=(2, 2),

visualize=True,

feature_vector=True,

block_norm='L2-Hys')

  

# rescale HOG visualizations for display

hog_img_def = exposure.rescale_intensity(hog_img_def, in_range=(0, hog_img_def.max()))

hog_img_cust = exposure.rescale_intensity(hog_img_cust, in_range=(0, hog_img_cust.max()))

  

# plot original + two HOG visualizations in a 1x3 grid

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

ax = axes.ravel()

ax[0].imshow(tpl, cmap='gray')

ax[0].set_title('Original template')

ax[0].axis('off')

  

ax[1].imshow(hog_img_def, cmap='gray')

ax[1].set_title(f'HOG (default)\nlen={hog_def.size}')

ax[1].axis('off')

  

ax[2].imshow(hog_img_cust, cmap='gray')

ax[2].set_title(f'HOG (4x4, 2x2, ori=8)\nlen={hog_cust.size}')

ax[2].axis('off')

  

plt.tight_layout()

plt.show()
```

### 2.1.1.- Info per HOG
```python
from skimage.feature import hog

from skimage import exposure
import os, glob

from matplotlib import patches

  

tpl = ensure_gray(io.imread("images/person_template.bmp"))

tpl = normalize(tpl)

h, w = tpl.shape

  

# HOG default params
orientations = 9
pixels_per_cell = (8, 8)
cells_per_block = (3, 3)

py, px = pixels_per_cell
cy, cx = cells_per_block
  
cells_y = h // py
cells_x = w // px

blocks_y = cells_y - cy + 1
blocks_x = cells_x - cx + 1

  

features_per_block = cy * cx * orientations
total_features_calc = blocks_y * blocks_x * features_per_block

  

# compute hog to compare
hog_def, hog_img_def = hog(
							tpl,
							orientations=orientations,
							pixels_per_cell=pixels_per_cell,
							cells_per_block=cells_per_block,
							visualize=True,
							feature_vector=True,
							block_norm='L2-Hys'
						)

  

print(f"template size: {w} x {h} (width x height) -> pixels = {w*h}")

print(f"pixels_per_cell: {pixels_per_cell}, cells_per_block: {cells_per_block}, orientations: {orientations}")

print(f"cells (x,y): {cells_x}, {cells_y}")

print(f"blocks (x,y): {blocks_x}, {blocks_y}")

print(f"features per block: {features_per_block}")

print(f"calculated total features = {total_features_calc}")

print(f"hog() returned feature vector length = {hog_def.size}")
```


### 2.1.2.- Detectar persones donat template

```python
import os, glob

from matplotlib import patches

  

def detect_person_hog(image, template, hog_params, step=8):

tpl_h, tpl_w = template.shape

# template feature

tpl_feat = hog(template, visualize=False, **hog_params)

h, w = image.shape

best = {'dist': np.inf, 'x': 0, 'y': 0}

for y in range(0, h - tpl_h + 1, step):

for x in range(0, w - tpl_w + 1, step):

window = image[y:y+tpl_h, x:x+tpl_w]

# compute HOG for window

win_feat = hog(window, visualize=False, **hog_params)

d = np.linalg.norm(win_feat - tpl_feat)

if d < best['dist']:

best.update({'dist': d, 'x': x, 'y': y})

return best

  

# params used for detection

hog_params = dict(orientations=9,

pixels_per_cell=(8, 8),

cells_per_block=(3, 3),

block_norm='L2-Hys',

feature_vector=True)

  

# read template

tpl = ensure_gray(io.imread("images/person_template.bmp"))

tpl = normalize(tpl)

tpl_h, tpl_w = tpl.shape

  

# run detection on all images in folder

img_paths = sorted(glob.glob("images/TestPersonImages/*"))

for p in img_paths:

img = ensure_gray(io.imread(p))

img = normalize(img)

  

# find best match

best = detect_person_hog(img, tpl, hog_params, step=8)

  

# compute HOG visualization for full image

_, hog_img_full = hog(img, visualize=True, **hog_params)

hog_img_full = exposure.rescale_intensity(hog_img_full, in_range=(0, hog_img_full.max()))

  

# plot template, image with bbox, hog image with bbox

fig, axes = plt.subplots(1, 3, figsize=(15, 6))

ax0, ax1, ax2 = axes.ravel()

  

ax0.imshow(tpl, cmap='gray')

ax0.set_title("Template")

ax0.axis('off')

  

ax1.imshow(img, cmap='gray')

rect = patches.Rectangle((best['x'], best['y']), tpl_w, tpl_h,

linewidth=2, edgecolor='r', facecolor='none')

ax1.add_patch(rect)

ax1.set_title(f"Image\nbest dist={best['dist']:.2f}\n{os.path.basename(p)}")

ax1.axis('off')

  

ax2.imshow(hog_img_full, cmap='gray')

rect2 = patches.Rectangle((best['x'], best['y']), tpl_w, tpl_h,

linewidth=2, edgecolor='r', facecolor='none')

ax2.add_patch(rect2)

ax2.set_title("HOG visualization (full image)")

ax2.axis('off')

  

plt.tight_layout()

plt.show()
```

### PQ faia HOG?

#### 🔴 Motius principals de fallada

Les limitacions intrínseques dels descriptors de gradients i el _template matching_ causen errors quan l'entrada difereix significativament del model entrenat:

- **💡 Condicions d'il·luminació**
    
    - Les variacions de llum (ombres dures, baix contrast) alteren la magnitud i direcció dels gradients, modificant l'aparença de la persona respecte al model.
        
- **🚧 Oclusions**
    
    - Interposició d'altres objectes que amaguen parts del cos. Si falten característiques clau (contorns de cames o espatlles), el descriptor no supera el llindar de detecció.
        
- **imits Variacions de Posa i Orientació**
    
    - El detector sol esperar una silueta estàndard (ex: vianant dret). Moviments atípics o canvis de perspectiva que difereixen significativament del _template_ causen fallades.
        
- **📐 Variacions d'Escala**
    
    - Discrepància entre la mida de la persona a la imatge i la mida de la finestra de detecció (o les escales de la piràmide d'imatges analitzades).
        

---

> **Nota del Professor:** En sistemes clàssics com HOG+SVM, la rigidesa del _template_ és el factor crític. A diferència de les xarxes convolucionals modernes (CNNs), HOG no té invariància "apresa" profunda per gestionar deformacions severes o oclusions parcials de manera robusta.


## 2.3 .-HOG VS TEMPLATE BASED:

### 🔎 Anàlisi del Procés de Detecció d'Objectes

### 1. L'Algorisme HOG (Resum)

L'algorisme **HOG** (_Histogram of Oriented Gradients_) es basa en la premissa que l'aparença i la forma d'un objecte local es poden descriure mitjançant la distribució dels gradients d'intensitat (direcció de les vores).

- **Mecanisme:** Divideix la imatge en petites regions (cel·les), calcula l'histograma de direccions de gradient per a cada cel·la i normalitza el resultat en blocs més grans.
    
- **Avantatges:**
    
    - **Robustesa:** Tolera bé canvis d'il·luminació (gràcies a la normalització) i petites variacions de posa.
        
    - **Estructura:** Captura la forma local (contorns) de manera eficient, ideal per a vianants.
        
- **Desavantatges:**
    
    - **Cost Computacional:** Pot ser intensiu (encara que optimitzable) comparat amb mètodes més simples.
        
    - **Limitacions:** Pateix amb oclusions severes o canvis d'escala dràstics si no s'utilitzen piràmides d'imatges.
        

---

### 2. Comparativa: HOG vs. Template Matching

**Avantatges del detector HOG respecte al basat en plantilles (Template-based):**

L'avantatge fonamental és la **capacitat de generalització**. El _template matching_ clàssic realitza una comparació "píxel a píxel" (correlació creuada), la qual cosa el fa extremadament rígid: si l'objecte gira lleugerament, canvia la llum o es deforma, la correlació cau en picat.

En canvi, el **HOG** treballa en l'espai de característiques (gradients), no de píxels. Això li permet:

1. **Invariància:** Ser molt més robust a variacions d'il·luminació i contrast (ja que els gradients capturen canvis relatius, no absoluts).
    
2. **Flexibilitat:** Detectar la _classe_ d'objecte (ex: "un humà") independentment de la seva roba o textura específica, capturant l'estructura subjacent, mentre que el _template_ sovint requereix una coincidència gairebé exacta de l'aparença.
    

---

> **Nota del Professor:** Si estàs implementant això en el teu sistema Fedora, recorda que OpenCV (`cv2.HOGDescriptor`) ja té una implementació optimitzada que utilitza instruccions SIMD per mitigar el cost computacional.


# 3.- ORB

## 3.0.1.- DoG (diferences of gaussian)
El primer exc va d'apligar DoG

Aproximació eficient del **Laplacià de Gaussià (LoG)** per detectar _blobs_ (regions d'interès) restant dues imatges suavitzades amb diferents sigmes

**Importants**:

- **Principi Center-Surround**: Calculem dues Gaussianes, una "central" (sigma petit) i una d'entorn (sigma gran). La diferència $DoG = G_{center} - G_{surround}$ ressalta els canvis d'intensitat locals.
    
- **Paràmetres d'Escala ($\sigma$)**:
    
    - `center_sigma`: Controla la detecció de detalls fins.
        
    - `surround_sigma`: Controla la supressió del fons.
        
    - _Nota_: Blobs més grans requereixen sigmes més grans.
        
- **Detecció de Pics**: S'utilitza `peak_local_max` sobre la imatge resultant (DoG) per trobar les coordenades $(x, y)$ dels punts més brillants (els centres dels blobs).
    
- **Neteja de Deteccions**:
    
    - `min_distance`: Imposa una distància mínima entre punts per evitar solapaments (Non-Maximum Suppression).
        
    - `threshold_rel`: Descarta els pics amb un contrast massa baix (elimina soroll).
        


```python
# Your solution here

from skimage.filters import gaussian

from skimage.feature import peak_local_max

  

def detect_censure_dog(image,

center_sigma=1.0,

surround_sigma=3.0,

min_distance=8,

threshold_rel=0.2,

num_peaks=300):

  

img = ensure_gray(image)

img = normalize(img)

g_center = gaussian(img, sigma=center_sigma, preserve_range=True)

g_surround = gaussian(img, sigma=surround_sigma, preserve_range=True)

dog = g_center - g_surround # center - surround

# detect local maxima on DoG response

peaks = peak_local_max(dog,

min_distance=min_distance,

threshold_rel=threshold_rel,

num_peaks=num_peaks,

exclude_border=False)

responses = dog[peaks[:, 0], peaks[:, 1]] if peaks.size else np.array([])

return peaks, responses, dog

  

def plot_censure_results(image_path, param_sets, figsize=(15, 5), circle_size=10):

img = io.imread(image_path)

imgg = ensure_gray(img)

imgg = normalize(imgg)

n = len(param_sets)

cols = min(3, n)

rows = (n + cols - 1) // cols

fig, axes = plt.subplots(rows, cols, figsize=(cols*5, rows*4))

axes = np.atleast_1d(axes).reshape(-1)

for ax, params in zip(axes, param_sets):

peaks, resp, dog = detect_censure_dog(imgg, **params)

ax.imshow(imgg, cmap='gray')

if peaks.size:

ax.scatter(peaks[:,1], peaks[:,0], s=circle_size, facecolors='none', edgecolors='r')

title = (f"center_sigma={params['center_sigma']}, surround_sigma={params['surround_sigma']}\n"

f"min_dist={params['min_distance']}, thr_rel={params['threshold_rel']}\n"

f"detected={len(peaks)}")

ax.set_title(title)

ax.axis('off')

# hide unused axes

for unused in axes[len(param_sets):]:

unused.axis('off')

plt.tight_layout()

plt.show()

  

# Example: run several parameter combinations on images/starbucks4.jpg

params_to_test = [

dict(center_sigma=0.8, surround_sigma=3.0, min_distance=6, threshold_rel=0.05, num_peaks=300),

dict(center_sigma=1.0, surround_sigma=3.0, min_distance=8, threshold_rel=0.1, num_peaks=300),

dict(center_sigma=1.5, surround_sigma=4.5, min_distance=10, threshold_rel=0.2, num_peaks=300),

dict(center_sigma=0.6, surround_sigma=2.0, min_distance=4, threshold_rel=0.02, num_peaks=300),

dict(center_sigma=2.0, surround_sigma=6.0, min_distance=12, threshold_rel=0.3, num_peaks=300),

]

  

plot_censure_results("images/starbucks4.jpg", params_to_test)
```



## 3.1- ORB (Oriented FAST and Rotated BRIEF)

És una alternativa molt ràpida i eficient (i lliure de patents) a SIFT o SURF. Combina un detector de cantonades (FAST) amb un descriptor binari (BRIEF), afegint-hi orientació.

**Importants**:

- **Detector (FAST millorat)**:
    
    - Utilitza l'algorisme FAST per trobar _keypoints_ (punts clau) ràpidament.
        
    - **Pyramid Scale**: Aplica FAST a diferents escales de la imatge per aconseguir invariància a l'escala (detectar objectes a prop i lluny).
        
- **Orientació (Intensity Centroid)**:
    
    - FAST original no té orientació. ORB calcula el "centre de massa" (intensitat) d'un pedaç voltant del punt.
        
    - El vector des del centre geomètric al centre de massa defineix l'angle $\theta$. Això permet que sigui **invariant a la rotació**.
        
- **Descriptor (Steered BRIEF)**:
    
    - Genera un string binari (ex: `101001...`) basat en tests simples de comparació d'intensitat entre parells de píxels $(p_1 < p_2)$.
        
    - Aquests patrons de comparació es roten segons l'angle $\theta$ calculat abans.
        
- **Matching (Distància de Hamming)**:
    
    - A diferència de SIFT/SSD (que usen distància Euclidiana), ORB utilitza la **Distància de Hamming** (comptar bits diferents fent un XOR).
        
    - Això és extremadament ràpid a nivell de processador.
        



## 3.2 Implementació de ORB

```python
# Your solution here

from skimage.feature import ORB, match_descriptors
from skimage.feature import SIFT
import time

  

def get_ORB(image, n_keypoints=1000, fast_threshold=0.08):

  

if image.ndim == 3:

image = color.rgb2gray(image)

orb = ORB(n_keypoints=n_keypoints, fast_threshold=fast_threshold)

orb.detect_and_extract(image)

# orb.keypoints are (row, col), orb.descriptors are binary

return orb.keypoints, orb.descriptors

  

def match_orb_images(model_path, scene_path,

n_keypoints=1000,

fast_threshold=0.08,

max_ratio=0.8,

cross_check=False,

plot_top=100):

  

# read and prepare images

model = io.imread(model_path) if isinstance(model_path, str) else model_path

scene = io.imread(scene_path) if isinstance(scene_path, str) else scene_path

# ensure grayscale for ORB

model_g = ensure_gray(model)

scene_g = ensure_gray(scene)

  

# detect ORB keypoints & descriptors

start = time.time()

kp1, desc1 = get_ORB(model_g, n_keypoints=n_keypoints, fast_threshold=fast_threshold)

kp2, desc2 = get_ORB(scene_g, n_keypoints=n_keypoints, fast_threshold=fast_threshold)

t_detect = time.time() - start

  

print(f"Model: {len(kp1)} keypoints, Scene: {len(kp2)} keypoints (detection time {t_detect:.2f}s)")

  

# match descriptors. ORB descriptors are binary -> use metric='hamming'

start = time.time()

matches = match_descriptors(desc1, desc2,

cross_check=cross_check,

max_ratio=max_ratio,

metric='hamming')

  

t_match = time.time() - start

print(f"Matches found: {matches.shape[0]} (cross_check={cross_check}, max_ratio={max_ratio}), (matching time {t_match:.2f}s)")

  

# Plot matches using helper plot_matches_aux (present in this notebook appendix).

fig, ax = plt.subplots(1, 1, figsize=(12, 6))

try:

from skimage.feature import plot_matched_features

plot_matched_features(model_g, scene_g, keypoints0=kp1, keypoints1=kp2, matches=matches[:plot_top], keypoints_color='r', ax=ax)

except Exception:

# fallback to provided auxiliary function plot_matches_aux

plot_matches_aux(ax, model_g, scene_g, kp1, kp2, matches[:plot_top], keypoints_color='r')

model_title = model_path if isinstance(model_path, str) else 'Model'

scene_title = scene_path if isinstance(scene_path, str) else 'Scene'

ax.set_title(f"ORB matches (N={matches.shape[0]})\nmodel: {model_title} scene: {scene_title}")

plt.show()

  

# return data for further analysis if needed

return dict(keypoints_model=kp1, desc_model=desc1,

keypoints_scene=kp2, desc_scene=desc2,

matches=matches)

  

res = match_orb_images("images/starbucks.jpg", "images/starbucks4.jpg",

n_keypoints=800, fast_threshold=0.08,

max_ratio=0.8, cross_check=False, plot_top=150)



# Your solution here

res = match_orb_images("images/starbucks.jpg", "images/starbucks2.png",

n_keypoints=800, fast_threshold=0.08,

max_ratio=0.8, cross_check=False, plot_top=150)
```

### 3.3.1 Característiques ORB vs HOG
### 3.4 Anàlisi de tècniques i resultats (ORB)

### 1. Avantatges d'ORB vs. HOG i _Template Matching_

ORB (_Oriented FAST and Rotated BRIEF_) supera els detectors clàssics en escenaris dinàmics gràcies a la seva arquitectura híbrida:

- **Robustesa Geològica:** A diferència del _Template Matching_ (que requereix píxels exactes) o HOG (sensible a rotacions sense ajustos complexos), ORB és **invariant a la rotació i a l'escala**.
    
- **Eficiència Computacional:** Combina el detector **FAST** (molt ràpid trobant punts clau) amb el descriptor **BRIEF** (cadenes binàries). Això permet una extracció de característiques i un aparellament (_matching_) extremadament ràpids, ideals per a **temps real**.
    
- **Resiliència:** Suporta millor les variacions d'il·luminació i les oclusions parcials de l'objecte.
    

### 2. Anàlisi d'imatges sense l'objecte (Cas Negatiu)

Si s'analitza una imatge on no hi apareix el logotip (ex: Starbucks):

- **Comportament:** L'algorisme seguirà detectant _keypoints_ i generant descriptors sobre el fons o altres objectes.
    
- **Resultat:** La fase de _matching_ donarà un nombre de coincidències **molt baix o nul**.
    
- **Filtrat:** Els pocs _matches_ que puguin aparèixer seran probablement "soroll" o _outliers_ geomètrics, que s'eliminen fàcilment aplicant un llindar mínim de coincidències o validació geomètrica (RANSAC).
    

### 3. Definició d'una mesura de qualitat de correspondència

Per avaluar numèricament com de bona és la correspondència entre dues imatges, podríem definir una mètrica composta ($Q$) que consideri:

1. **Densitat d'Inliers:** La ràtio entre _keypoints_ aparellats correctament i el total detectat ($N_{matches} / N_{total}$).
    
2. **Consistència Geomètrica:** Si els punts mantenen la seva estructura relativa (es pot verificar calculant la projecció de l'homografia i mesurant l'error de reprojecció).
    
3. **Distància dels Descriptors:** La mitjana de la distància de Hamming dels aparellaments (com més baixa, més similitud visual).
    
4. **Distribució Espacial:** Penalitzar si tots els _matches_ estan concentrats en una àrea petita (risc de fals positiu localitzat).
    

# 4 SIFT

## 4.1.- Implementació SIFT
El mateix que amb ORB però amb SIFT:

```python
# Your solution

from skimage.feature import SIFT

import time

  

def get_SIFT(image, n_octaves=4, n_scales=3, sigma=1.6):

  

# ensure grayscale

image = ensure_gray(image)

# normalize to range [0,1] (SIFT expects float input)

image = normalize(image)

  

# create SIFT object with the requested scale-space params

sift = SIFT(n_octaves=n_octaves, n_scales=n_scales, sigma_min=sigma)

# detect keypoints and compute descriptors

sift.detect_and_extract(image)

# keypoints are (row, col), descriptors are float arrays

return sift.keypoints, sift.descriptors

  

def match_sift_images(model_path, scene_path,

n_octaves=4, n_scales=3, sigma=1.6,

max_ratio=0.8, cross_check=False,

metric='euclidean', plot_top=150):

  

# load images (allow passing already-loaded arrays)

model = io.imread(model_path) if isinstance(model_path, str) else model_path

scene = io.imread(scene_path) if isinstance(scene_path, str) else scene_path

  

model_g = ensure_gray(model)

scene_g = ensure_gray(scene)

  

start = time.time()

kp1, desc1 = get_SIFT(model_g, n_octaves=n_octaves, n_scales=n_scales, sigma=sigma)

kp2, desc2 = get_SIFT(scene_g, n_octaves=n_octaves, n_scales=n_scales, sigma=sigma)

t_detect = time.time() - start

  

print(f"Detected SIFT: model {len(kp1)} kp, scene {len(kp2)} kp (detection time {t_detect:.2f}s)")

  

# matching (uses ratio test internally when max_ratio is set)

start = time.time()

matches = match_descriptors(desc1, desc2,

cross_check=cross_check,

max_ratio=max_ratio,

metric=metric)

t_match = time.time() - start

print(f"Matches: {matches.shape[0]} (cross_check={cross_check}, max_ratio={max_ratio}, metric={metric}) (matching time {t_match:.2f}s)")

  

# plot matches (use provided fallback plot_matches_aux if plot_matched_features unavailable)

fig, ax = plt.subplots(1, 1, figsize=(12, 6))

try:

from skimage.feature import plot_matched_features

plot_matched_features(model_g, scene_g, keypoints0=kp1, keypoints1=kp2, matches=matches[:plot_top], keypoints_color='r', ax=ax)

except Exception:

plot_matches_aux(ax, model_g, scene_g, kp1, kp2, matches[:plot_top], keypoints_color='r')

ax.set_title(f"SIFT matches (N={matches.shape[0]})\nmodel: {model_path if isinstance(model_path, str) else 'Model'} scene: {scene_path if isinstance(scene_path, str) else 'Scene'}")

plt.show()

  

return dict(keypoints_model=kp1, desc_model=desc1,

keypoints_scene=kp2, desc_scene=desc2,

matches=matches,

times=dict(detect=t_detect, match=t_match))

  
  

res_sift = match_sift_images("images/starbucks.jpg", "images/starbucks4.jpg",

n_octaves=4, n_scales=3, sigma=1.6,

max_ratio=0.8, cross_check=False, metric='euclidean', plot_top=200)

```

## 4.2 Best match amb SIFT
```python
def find_best_match_for_reference(reference_path,

folder="images/matches_SIFT",

n_octaves=8, n_scales=3, sigma=1.6,

upsampling=2, max_ratio=0.8,

metric='euclidean', top_plot=200):

  

# load reference

ref_im = io.imread(reference_path)

ref_im = transform.resize(ref_im, (256, 256), anti_aliasing=True) if max(ref_im.shape) > 512 else ref_im

ref_im_gray = ensure_gray(ref_im)

ref_im_gray = normalize(ref_im_gray)

ref_proc = ref_im_gray

  

# compute SIFT for reference

sift_ref = SIFT(n_octaves=n_octaves, n_scales=n_scales, sigma_min=sigma)

sift_ref.detect_and_extract(ref_proc)

kp_ref = sift_ref.keypoints

desc_ref = sift_ref.descriptors

  

# iterate folder images

import glob, os

paths = sorted(glob.glob(os.path.join(folder, "*")))

# exclude the reference image itself if present

paths = [p for p in paths if os.path.abspath(p) != os.path.abspath(reference_path)]

best = dict(count=-1, path=None, keypoints=None, descriptors=None, img=None, matches=None)

  

for p in paths:

im = io.imread(p)

im = transform.resize(im, (256, 256), anti_aliasing=True) if max(im.shape) > 512 else im

img = ensure_gray(im)

img_norm = normalize(img)

img_proc = img_norm

  

sift_i = SIFT(n_octaves=n_octaves, n_scales=n_scales, sigma_min=sigma)

sift_i.detect_and_extract(img_proc)

kp_i = sift_i.keypoints

desc_i = sift_i.descriptors

  

if desc_ref is None or desc_i is None or len(desc_ref)==0 or len(desc_i)==0:

cnt = 0

matches = np.zeros((0,2), dtype=int)

else:

matches = match_descriptors(desc_ref, desc_i, cross_check=False, max_ratio=max_ratio, metric=metric)

cnt = matches.shape[0]

  

print(f"matched ref <-> {os.path.basename(p)} : {cnt}")

if cnt > best['count']:

best.update(dict(count=cnt, path=p, keypoints=kp_i, descriptors=desc_i, img=img_proc, matches=matches))

  

if best['path'] is None:

print("No images found in folder or no descriptors extracted.")

return None

  

# visualize best match (limit plotted matches)

matches_plot = best['matches'][:top_plot] if best['matches'].shape[0] else best['matches']

fig, ax = plt.subplots(1,1, figsize=(12,6))

try:

from skimage.feature import plot_matched_features

plot_matched_features(ref_proc, best['img'], keypoints0=kp_ref, keypoints1=best['keypoints'], matches=matches_plot, keypoints_color='r', ax=ax)

except Exception:

plot_matches_aux(ax, ref_proc, best['img'], kp_ref, best['keypoints'], matches_plot, keypoints_color='r')

ax.set_title(f"Reference: {os.path.basename(reference_path)} <---> Best: {os.path.basename(best['path'])} (matches={best['count']})")

plt.show()

  

print(f"Best match: {os.path.basename(best['path'])} with {best['count']} matches")

return dict(reference=reference_path, best_path=best['path'], matches=best['count'],

keypoints_ref=kp_ref, keypoints_best=best['keypoints'], pair_matches=best['matches'])

  

result = find_best_match_for_reference("images/matches_SIFT/ciudad_ciencias_1.jpg", folder="images/matches_SIFT",

n_octaves=8, n_scales=3, sigma=1.6,

upsampling=2, max_ratio=0.8, metric='euclidean', top_plot=200)

```



# EXERCICIS INVENTATS


## Exc 1 HOG amb angle i canvi de brightness

```python
from skimage.feature import hog
from skimage import exposure, io, transform
import matplotlib.pyplot as plt
import numpy as np

def ensure_gray(image):
    if image.ndim == 3:
        from skimage import color
        if image.shape[-1] == 4:
            image = color.rgba2rgb(image)
        if image.shape[-1] == 3:
            return color.rgb2gray(image)
    return image

def normalize(image):
    if image.max() > 1.:
        image = image.astype(np.float32) / 255.
    return image

def apply_brightness_change(image, factor):
    """Multiply intensity by factor (e.g., 0.5 = darker, 1.5 = brighter)"""
    img = image * factor
    return np.clip(img, 0, 1)

def compare_hog_under_transformations(image_path):
    img = io.imread(image_path)
    img = ensure_gray(img)
    img = normalize(img)
    
    hog_params = dict(
        orientations=9,
        pixels_per_cell=(8, 8),
        cells_per_block=(3, 3),
        block_norm='L2-Hys',
        feature_vector=True
    )
    
    # Original HOG
    hog_orig = hog(img, visualize=False, **hog_params)
    
    # Test rotations
    angles = [5, 10, 15, 30, 45]
    rotation_dists = []
    
    for angle in angles:
        rotated = transform.rotate(img, angle, resize=True, preserve_range=True)
        # Need same size, so resize back
        rotated_resized = transform.resize(rotated, img.shape, anti_aliasing=True)
        hog_rot = hog(rotated_resized, visualize=False, **hog_params)
        dist = np.linalg.norm(hog_orig - hog_rot)
        rotation_dists.append(dist)
        print(f"Rotation {angle}°: HOG distance = {dist:.3f}")
    
    # Test brightness changes
    brightness_factors = [0.5, 0.7, 1.3, 1.5]  # -50%, -30%, +30%, +50%
    brightness_labels = ["-50%", "-30%", "+30%", "+50%"]
    brightness_dists = []
    
    for factor, label in zip(brightness_factors, brightness_labels):
        bright_img = apply_brightness_change(img, factor)
        hog_bright = hog(bright_img, visualize=False, **hog_params)
        dist = np.linalg.norm(hog_orig - hog_bright)
        brightness_dists.append(dist)
        print(f"Brightness {label}: HOG distance = {dist:.3f}")
    
    # Plot comparison
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    axes[0].plot(angles, rotation_dists, 'o-', linewidth=2, markersize=8)
    axes[0].set_xlabel('Rotation Angle (degrees)')
    axes[0].set_ylabel('HOG Distance from Original')
    axes[0].set_title('HOG Sensitivity to Rotation')
    axes[0].grid(True, alpha=0.3)
    
    axes[1].bar(brightness_labels, brightness_dists, color=['red', 'orange', 'lightblue', 'blue'])
    axes[1].set_xlabel('Brightness Change')
    axes[1].set_ylabel('HOG Distance from Original')
    axes[1].set_title('HOG Sensitivity to Brightness')
    axes[1].grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    plt.show()

# Example call:
# compare_hog_under_transformations("images/person_template.bmp")

```

## Exc 2 Orb amb Noise, blur i rotation

```python
from skimage.feature import ORB, match_descriptors
from skimage import io, transform, util
from skimage.filters import gaussian
import matplotlib.pyplot as plt
import numpy as np
import time

def get_ORB(image, n_keypoints=800, fast_threshold=0.08):
    from skimage import color
    if image.ndim == 3:
        image = color.rgb2gray(image)
    image = normalize(image)
    orb = ORB(n_keypoints=n_keypoints, fast_threshold=fast_threshold)
    orb.detect_and_extract(image)
    return orb.keypoints, orb.descriptors

def apply_gaussian_noise(image, var=0.01):
    """Add Gaussian noise"""
    return util.random_noise(image, mode='gaussian', var=var, clip=True)

def test_orb_robustness(image_path):
    img_orig = io.imread(image_path)
    img_orig = ensure_gray(img_orig)
    img_orig = normalize(img_orig)
    
    kp_orig, desc_orig = get_ORB(img_orig, n_keypoints=800)
    print(f"Original image: {len(kp_orig)} keypoints")
    
    # Create alterations
    alterations = {}
    
    # 1. Gaussian noise
    img_noise = apply_gaussian_noise(img_orig, var=0.02)
    alterations['Noise (σ²=0.02)'] = img_noise
    
    # 2. Gaussian blur
    img_blur = gaussian(img_orig, sigma=2.0, preserve_range=True)
    alterations['Blur (σ=2.0)'] = img_blur
    
    # 3. Rotation 30°
    img_rot = transform.rotate(img_orig, 30, resize=False, preserve_range=True)
    alterations['Rotation 30°'] = img_rot
    
    # 4. Scale 50%
    new_shape = (img_orig.shape[0] // 2, img_orig.shape[1] // 2)
    img_scale = transform.resize(img_orig, new_shape, anti_aliasing=True)
    # Resize back to original size for comparison
    img_scale = transform.resize(img_scale, img_orig.shape, anti_aliasing=True)
    alterations['Scale 50%'] = img_scale
    
    results = {}
    
    for name, img_altered in alterations.items():
        kp_alt, desc_alt = get_ORB(img_altered, n_keypoints=800)
        
        if desc_orig is None or desc_alt is None or len(desc_orig) == 0 or len(desc_alt) == 0:
            matches = np.zeros((0, 2), dtype=int)
        else:
            matches = match_descriptors(desc_orig, desc_alt,
                                       cross_check=False,
                                       max_ratio=0.8,
                                       metric='hamming')
        
        results[name] = {
            'keypoints': len(kp_alt),
            'matches': len(matches),
            'image': img_altered,
            'kp': kp_alt,
            'desc': desc_alt,
            'match_obj': matches
        }
        
        print(f"{name}: {len(kp_alt)} keypoints, {len(matches)} matches")
    
    # Visualize best and worst
    sorted_results = sorted(results.items(), key=lambda x: x[1]['matches'], reverse=True)
    best_name, best_data = sorted_results[0]
    worst_name, worst_data = sorted_results[-1]
    
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    
    # Original
    axes[0, 0].imshow(img_orig, cmap='gray')
    axes[0, 0].set_title(f'Original\n{len(kp_orig)} keypoints')
    axes[0, 0].axis('off')
    
    # Best case
    axes[0, 1].imshow(best_data['image'], cmap='gray')
    axes[0, 1].scatter(best_data['kp'][:, 1], best_data['kp'][:, 0], 
                       s=20, facecolors='none', edgecolors='r', linewidths=0.5)
    axes[0, 1].set_title(f'BEST: {best_name}\n{best_data["matches"]} matches')
    axes[0, 1].axis('off')
    
    # Worst case
    axes[0, 2].imshow(worst_data['image'], cmap='gray')
    axes[0, 2].scatter(worst_data['kp'][:, 1], worst_data['kp'][:, 0], 
                       s=20, facecolors='none', edgecolors='r', linewidths=0.5)
    axes[0, 2].set_title(f'WORST: {worst_name}\n{worst_data["matches"]} matches')
    axes[0, 2].axis('off')
    
    # All alterations comparison
    all_imgs = [alterations[name] for name in ['Noise (σ²=0.02)', 'Blur (σ=2.0)', 'Rotation 30°']]
    all_names = ['Noise (σ²=0.02)', 'Blur (σ=2.0)', 'Rotation 30°']
    
    for idx, (img_alt, name) in enumerate(zip(all_imgs, all_names)):
        axes[1, idx].imshow(img_alt, cmap='gray')
        axes[1, idx].set_title(f'{name}\n{results[name]["matches"]} matches')
        axes[1, idx].axis('off')
    
    plt.tight_layout()
    plt.show()
    
    # Bar chart
    fig, ax = plt.subplots(figsize=(10, 6))
    names = list(results.keys())
    match_counts = [results[n]['matches'] for n in names]
    
    ax.bar(names, match_counts, color='steelblue')
    ax.set_ylabel('Number of Matches')
    ax.set_title('ORB Matching Robustness Under Different Alterations')
    ax.grid(True, alpha=0.3, axis='y')
    plt.xticks(rotation=15, ha='right')
    plt.tight_layout()
    plt.show()
    
    return results

# Example call:
# results = test_orb_robustness("images/starbucks.jpg")


```

## Exc 3 SIFT amb diferents sizes (100%, 75%, ...)

```python
from skimage.feature import SIFT, match_descriptors
from skimage import io, transform
import matplotlib.pyplot as plt
import numpy as np

def get_SIFT(image, n_octaves=4, n_scales=3, sigma=1.6):
    image = ensure_gray(image)
    image = normalize(image)
    sift = SIFT(n_octaves=n_octaves, n_scales=n_scales, sigma_min=sigma)
    sift.detect_and_extract(image)
    return sift.keypoints, sift.descriptors

def match_sift_multiscale(reference_path, scene_path):
    ref_img = io.imread(reference_path)
    scene_img = io.imread(scene_path)
    
    ref_gray = ensure_gray(ref_img)
    ref_gray = normalize(ref_gray)
    scene_gray = ensure_gray(scene_img)
    scene_gray = normalize(scene_gray)
    
    # Get reference SIFT
    kp_ref, desc_ref = get_SIFT(ref_gray, n_octaves=6, n_scales=3)
    print(f"Reference: {len(kp_ref)} keypoints")
    
    # Create scale pyramid
    scales = [1.0, 0.75, 0.5, 0.25]
    results = {}
    
    for scale in scales:
        if scale == 1.0:
            scene_scaled = scene_gray
        else:
            new_h = int(scene_gray.shape[0] * scale)
            new_w = int(scene_gray.shape[1] * scale)
            scene_scaled = transform.resize(scene_gray, (new_h, new_w), 
                                           anti_aliasing=True, preserve_range=False)
        
        kp_scene, desc_scene = get_SIFT(scene_scaled, n_octaves=6, n_scales=3)
        
        if desc_ref is None or desc_scene is None or len(desc_ref) == 0 or len(desc_scene) == 0:
            matches = np.zeros((0, 2), dtype=int)
        else:
            matches = match_descriptors(desc_ref, desc_scene,
                                       cross_check=False,
                                       max_ratio=0.75,
                                       metric='euclidean')
        
        results[scale] = {
            'keypoints': len(kp_scene),
            'matches': len(matches),
            'image': scene_scaled,
            'kp': kp_scene,
            'match_obj': matches
        }
        
        print(f"Scale {scale*100:.0f}%: {len(kp_scene)} keypoints, {len(matches)} matches")
    
    # Visualization
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    
    # Reference
    axes[0, 0].imshow(ref_gray, cmap='gray')
    axes[0, 0].scatter(kp_ref[:, 1], kp_ref[:, 0], s=10, 
                       facecolors='none', edgecolors='r', linewidths=0.5)
    axes[0, 0].set_title(f'Reference\n{len(kp_ref)} keypoints')
    axes[0, 0].axis('off')
    
    # All scales
    for idx, scale in enumerate([1.0, 0.75, 0.5, 0.25]):
        row = (idx + 1) // 3
        col = (idx + 1) % 3
        
        data = results[scale]
        axes[row, col].imshow(data['image'], cmap='gray')
        axes[row, col].scatter(data['kp'][:, 1], data['kp'][:, 0], s=5, 
                              facecolors='none', edgecolors='g', linewidths=0.5)
        axes[row, col].set_title(f'Scale {scale*100:.0f}%\n{data["matches"]} matches')
        axes[row, col].axis('off')
    
    # Hide last subplot
    axes[1, 2].axis('off')
    
    plt.tight_layout()
    plt.show()
    
    # Plot matches vs scale
    fig, ax = plt.subplots(figsize=(10, 6))
    scale_percentages = [s*100 for s in scales]
    match_counts = [results[s]['matches'] for s in scales]
    
    ax.plot(scale_percentages, match_counts, 'o-', linewidth=2, markersize=10, color='darkblue')
    ax.set_xlabel('Scene Scale (%)')
    ax.set_ylabel('Number of SIFT Matches')
    ax.set_title('SIFT Scale Invariance Test')
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
    
    return results

# Example call:
# results = match_sift_multiscale("images/starbucks.jpg", "images/starbucks4.jpg")

```

## Exc 4 Parameter optimization

```python
from skimage.feature import hog
from skimage import io, transform
import matplotlib.pyplot as plt
import numpy as np
from itertools import product

def hog_parameter_optimization(template_path, degraded_image_path):
    tpl = io.imread(template_path)
    tpl = ensure_gray(tpl)
    tpl = normalize(tpl)
    
    img = io.imread(degraded_image_path)
    img = ensure_gray(img)
    img = normalize(img)
    
    # Ensure same size
    if img.shape != tpl.shape:
        img = transform.resize(img, tpl.shape, anti_aliasing=True, preserve_range=False)
    
    # Parameter grid
    pixels_per_cell_options = [(4, 4), (8, 8), (16, 16)]
    orientations_options = [6, 9, 12]
    
    results = []
    
    for ppc, ori in product(pixels_per_cell_options, orientations_options):
        hog_params = dict(
            orientations=ori,
            pixels_per_cell=ppc,
            cells_per_block=(2, 2),
            block_norm='L2-Hys',
            feature_vector=True
        )
        
        try:
            hog_tpl = hog(tpl, visualize=False, **hog_params)
            hog_img = hog(img, visualize=False, **hog_params)
            
            # Euclidean distance
            dist = np.linalg.norm(hog_tpl - hog_img)
            
            results.append({
                'ppc': ppc,
                'orientations': ori,
                'distance': dist,
                'feature_length': len(hog_tpl)
            })
            
            print(f"ppc={ppc}, ori={ori}: dist={dist:.3f}, feat_len={len(hog_tpl)}")
        
        except Exception as e:
            print(f"ppc={ppc}, ori={ori}: FAILED - {e}")
    
    # Find best (minimum distance)
    best = min(results, key=lambda x: x['distance'])
    print(f"\nBEST: ppc={best['ppc']}, ori={best['orientations']}, "
          f"dist={best['distance']:.3f}")
    
    # Visualization
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # Original template
    axes[0, 0].imshow(tpl, cmap='gray')
    axes[0, 0].set_title('Template')
    axes[0, 0].axis('off')
    
    # Degraded image
    axes[0, 1].imshow(img, cmap='gray')
    axes[0, 1].set_title('Degraded Image')
    axes[0, 1].axis('off')
    
    # Heatmap of distances
    ppc_labels = ['4×4', '8×8', '16×16']
    ori_labels = ['6', '9', '12']
    
    distance_matrix = np.zeros((len(orientations_options), len(pixels_per_cell_options)))
    for r in results:
        i = orientations_options.index(r['orientations'])
        j = pixels_per_cell_options.index(r['ppc'])
        distance_matrix[i, j] = r['distance']
    
    im = axes[1, 0].imshow(distance_matrix, cmap='RdYlGn_r', aspect='auto')
    axes[1, 0].set_xticks(range(len(ppc_labels)))
    axes[1, 0].set_yticks(range(len(ori_labels)))
    axes[1, 0].set_xticklabels(ppc_labels)
    axes[1, 0].set_yticklabels(ori_labels)
    axes[1, 0].set_xlabel('pixels_per_cell')
    axes[1, 0].set_ylabel('orientations')
    axes[1, 0].set_title('HOG Distance Heatmap\n(lower = better)')
    plt.colorbar(im, ax=axes[1, 0])
    
    # Bar chart
    labels = [f"ppc={r['ppc']}, ori={r['orientations']}" for r in results]
    distances = [r['distance'] for r in results]
    
    axes[1, 1].barh(range(len(labels)), distances, color='steelblue')
    axes[1, 1].set_yticks(range(len(labels)))
    axes[1, 1].set_yticklabels(labels, fontsize=8)
    axes[1, 1].set_xlabel('HOG Distance')
    axes[1, 1].set_title('Parameter Comparison')
    axes[1, 1].grid(True, alpha=0.3, axis='x')
    
    # Highlight best
    best_idx = results.index(best)
    axes[1, 1].get_children()[best_idx].set_color('red')
    
    plt.tight_layout()
    plt.show()
    
    return results, best

# Example call:
# results, best = hog_parameter_optimization("images/person_template.bmp",
#                                            "images/TestPersonImages/person_03.png")

```

## Exc 5 David - Best image

```python
import os, glob
from matplotlib import patches

def ensure_gray(image):
    if image.ndim == 3:
        if image.shape[-1] == 4:
            image = color.rgba2rgb(image)
        if image.shape[-1] == 3:
            return color.rgb2gray(image)
    return image

def detect_person_hog(image, template, hog_params, step=8):
    tpl_h, tpl_w = template.shape
    # template feature
    tpl_feat = hog(template, visualize=False, **hog_params)
    h, w = image.shape
    best = {'dist': np.inf, 'x': 0, 'y': 0}
    for y in range(0, h - tpl_h + 1, step):
        for x in range(0, w - tpl_w + 1, step):
            window = image[y:y+tpl_h, x:x+tpl_w]
            # compute HOG for window
            win_feat = hog(window, visualize=False, **hog_params)
            d = np.linalg.norm(win_feat - tpl_feat)
            if d < best['dist']:
                best.update({'dist': d, 'x': x, 'y': y})
    return best

def find_most_similar_image(template,image,hog_params):
    #template_preprocess_image(template)
    template_feat = hog(template,visualize=False, **hog_params)
    mind_dist = float('inf')
    best_image = None

    images = images_array()
    for img in images:
        current_img = img
        #current_img = preprocess_image(img,target_shape=template.shape)
        current_feat = hog(current_img,visualize = False, **hog_params)
        dist = np.linalg.norm(template_feat - current_feat)

        #Guardar el mejor
        if dist < min_dist:
            min_dist = dist
            best_image = current_img
    return template, min_dist, best_imge 

# params used for detection
hog_params = dict(orientations=9,
                  pixels_per_cell=(8, 8),
                  cells_per_block=(3, 3),
                  block_norm='L2-Hys',
                  feature_vector=True)

# read template
template = ensure_gray(io.imread("images/person_template.bmp"))
template = normalize(template)
tpl_h, tpl_w = template.shape

# run detection on all images in folder
img_paths = sorted(glob.glob("images/TestPersonImages/*"))
best_general_match = {'dist': np.inf, 'x': 0, 'y': 0}
for p in img_paths:
    current_img = ensure_gray(io.imread(p))
    current_img = normalize(current_img)
    
    # find best match
    best = detect_person_hog(current_img, template, hog_params, step=8)

    if best['dist'] < best_general_match['dist']:
        best_general_match = best
        img_best = img
        best_path = p
        
        # compute HOG visualization for full image
        _, hog_img_full = hog(img, visualize=True, **hog_params)
        hog_img_full = exposure.rescale_intensity(hog_img_full, in_range=(0, hog_img_full.max()))


# plot template, image with bbox, hog image with bbox
fig, axes = plt.subplots(1, 3, figsize=(15, 6))
ax0, ax1, ax2 = axes.ravel()

ax0.imshow(template, cmap='gray')
ax0.set_title("Template")
ax0.axis('off')

ax1.imshow(img, cmap='gray')
rect = patches.Rectangle((best['x'], best['y']), tpl_w, tpl_h,
                             linewidth=2, edgecolor='r', facecolor='none')
ax1.add_patch(rect)
ax1.set_title(f"Image\nbest dist={best['dist']:.2f}\n{os.path.basename(best_path)}")
ax1.axis('off')

ax2.imshow(hog_img_full, cmap='gray')
rect2 = patches.Rectangle((best['x'], best['y']), tpl_w, tpl_h,
                              linewidth=2, edgecolor='r', facecolor='none')
ax2.add_patch(rect2)
ax2.set_title("HOG visualization (full image)")
ax2.axis('off')

plt.tight_layout()
plt.show()
```

