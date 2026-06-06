Resum de com fer gràfics amb [[Matplotlib]]

## Base
- Crear plot
fig, axs = plt.subplots(nrows, ncols , sharex=bool, sharey=bool)

els share és per a que no s'imprimeixin els números del plot per a les dues gràficques

## Estetic

- **Etiquetes i Títols:** Per a l'enfocament orientat a objectes, s'utilitzen els mètodes de l'objecte `Axes`: `ax.set_title()`, `ax.set_xlabel()`, i `ax.set_ylabel()`. Si hi ha múltiples subplots, `fig.suptitle()` pot afegir un títol general a tota la figura.
- **Gestió de Ticks:** Les funcions com `plt.xticks()` o `ax.set_xticks()` permeten als analistes definir la posició i el format de les marques de graduació dels eixos, la qual cosa és crucial per a dades categòriques o per a sèries temporals amb punts de dades dispersos.
- **Transparència (`alpha`):** L'ús del paràmetre `alpha` (transparència) és un element clau per gestionar la densitat de dades. Permet que les formes o línies superposades siguin semi-transparent, assegurant que les distribucions subjacents o altres sèries de dades no quedin completament ocultes per les capes superiors.
- **Ordre de Dibuix (`zorder`):** El paràmetre `zorder` controla l'ordre de dibuix dels elements. Un valor més alt indica que un element (com una línia de tendència agregada o una anotació) s'ha de dibuixar sobre els elements amb un `zorder` inferior. Això és essencial per assegurar que els resultats clau de l'anàlisi de grup siguin visuals prominents i no estiguin enterrats sota les dades brutes.

```
    plt.figure(figsize=(10, 5))
    
    for year, subset in df.groupby('year'):
        plt.hist(subset[column], bins=30, alpha=0.3, label=str(year))
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend(title='Any', loc='upper right')
    plt.xlim(xlim)
    plt.tight_layout()
    plt.show()


visualize_histograms(df, 'trip_distance', title = 'Distància dels viatge per any',
                     xlabel = 'Distància (km)', ylabel = 'Quantitat', xlim = (-5, 80))
```