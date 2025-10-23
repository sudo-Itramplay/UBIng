Per modificar una imatge amb [[Scikit-image]] i [[Numpy]] Haurem de treballar amb la imatge com si fos una matriu

Donada una `img` de 100x100 de color negre
```python
#Farem 3 alteracions, per tant

img1 = img.copy()

img1[:,50:] = 255

  

img2 = img.copy()

img2[50:,:] = 255

  

img3 = img.copy()

img3[:50,:50] = 255
```
El negre és 0, 255 és blanc


Per visualitzar les 3 dades juntes farem:

### Creem espai de visualització
`fig, axes = plt.subplots(1, 3)`
Amb això fem un espai d'una fila i 3 columnes (3 subplots, un en cada columna)

`fig` és:
`axes` són els 3 subplots:

```
for ax in axes:
```

[[Matplotlib Amagar eixos|Amaguem els eixos]] dels 3 subplots:
```python
for ax in axes:
	ax.get_xaxis().set_visible(False)
	ax.get_yaxis().set_visible(False)
```

Especifiquem el canal:
en aquest cas [[Imatges en 1 canal| agafem un canal]]
```python
axes[0].imshow(img1, cmap='gray')

axes[1].imshow(img2, cmap='gray')

axes[2].imshow(img3, cmap='gray')
```