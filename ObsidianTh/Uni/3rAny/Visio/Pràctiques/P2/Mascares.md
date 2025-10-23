Despres de carregar les imatges, es comença a fer la mascara:
```python
mask = img_coat[:,:,:3] > 0
```
## Separació de la imatge a mascarar del fono
Màscara 3D inicial.
	- Es compara cada píxel dels **tres primers canals** (RGB) de la jaqueta amb 0. 
	- Si el píxel (en algun dels canals) **no és negre** (és a dir, el seu valor >0), el resultat és `True`. (en aquest cas fondo negre)
	- Això crea un array booleà **3D** (`mask`) amb la mateixa mida que la imatge (Alçada, Amplada, 3).

## Creació de la imatge amb mascara
S'aplica la funció `np.max` al llarg de l'**eix dels canals** (`axis=2`). Si _qualsevol_ dels tres canals d'un píxel tenia un `True` (és a dir, el píxel no era negre), el resultat en 2D serà `True`. Això produeix la **màscara final 2D** (Alçada, Amplada) que aïlla la forma de la jaqueta.
```python
mask = np.max(mask, axis=2)
```
Aka, treiem una dimensió

Això el que farà serà donarte una serie de punts (vector) tancats, per aplicarli la mascara a algun element fer:

img[mask] = lo k sea

Posali la imatge i es reemplaçarà nomes en aquests punts