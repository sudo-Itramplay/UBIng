
## Reescale

Reescala en base la imatge:
un 15% més, per exemple:
```python
rom skimage.transform import rescale


img_panda_black = rescale(img_panda, 1.15, channel_axis=-1)

```


>[!note] Chanel axis
> És bona pràctica indicar `channel_axis=-1` (o `channel_axis=2`) si la imatge és en color (RGB), per assegurar que l'escalat no s'aplica a l'eix dels canals de color.



## Resize
Agafa la imatge i li assigna la mida que li demanis:
Agafa la imatge i l'ajusta (força) a la mida exacta en píxels que li demanis. **No** manté la relació d'aspecte per defecte.

```python
from skimage.transform import resize


# 800 píxels d'alt per 600 píxels d'ample
nova_mida = (800, 600)

img_panda_resized = resize(img_panda, nova_mida)
```