Per fer print d'una imatge amb [[Scikit-image]] i [[Matplotlib]] he de:
```
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
```
Compte amb els `vmin` i `vmax` per que no [[Excedir valor del uint8|excedeixin els limit ]]o [[Decimals en Scikit|canviin de tipus]]
