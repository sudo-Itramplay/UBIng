Com amagar eixos amb [[Matplotlib]]
**Neteja visual.** Amaga els eixos X i Y de cadascun dels subgràfics. Això és habitual per presentar imatges com a tals, sense marques de píxels ni coordenades.

```python
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
```

o també:
Aquesta instrucció s'utilitza per **netejar** un eix d'una gràfica, eliminant les etiquetes numèriques dels tics sense eliminar els tics ni l'eix en si mateix.
`ax.axes.yaxis.set_ticklabels([])`
