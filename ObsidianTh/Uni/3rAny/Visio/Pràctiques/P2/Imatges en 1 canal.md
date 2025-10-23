Amb [[Scikit-image]] les imatges poden tenir 3 canals, RGB o 1 canal, gray scale

Quan tenim un canal treballarem amb float64 en comptes de uint8
I el float representarà el nivell de lluminositat

La conversió no és simplement una mitjana:
Conversió RGB a GrayScale
$$
L=0.2126⋅R+0.7152⋅G+0.0722⋅B
$$
>[!tip]
>La funció `rgb2gray` s'encarrega automàticament de l'algorisme de ponderació.

>[!bug] Important
>Hauràs d'importar: `from skimage.color import rgb2gray`


```python
# Conversió de RGB a escala de grisos
from skimage.color import rgb2gray
# ...

ax = axs[0,1]
ax.imshow(rgb2gray(cat), cmap='gray') # Aplica la conversió i visualitza
```