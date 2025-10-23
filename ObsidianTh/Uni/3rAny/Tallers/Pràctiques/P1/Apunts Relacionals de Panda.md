Basat en els [[Apunts de la P1]]
### Visió General de Pandas

**Pandas** és una llibreria de Python fonamental per a la manipulació i anàlisi de dades. Les seves dues estructures principals són:

- **[[Create Panda|DataFrame]]**: Una estructura bidimensional, semblant a una taula o matriu, que organitza les dades en files i columnes.
    
- **[[Panda serie|Sèrie]]**: Una estructura unidimensional, com una columna de dades o una llista amb índex.
    

L'àlies més comú per importar la llibreria és `pd`.

---

### Creació i Càrrega de Dades

Per començar a treballar, necessitem carregar dades en un [[Create Panda|DataFrame]].

- **Creació Manual**: Es pot generar un [[Create Panda|DataFrame]] a partir d'estructures de Python com un diccionari de llistes o a partir de dues o més [[Panda serie]].
    
- **Càrrega des de Fitxer**: La manera més comuna és carregar dades des d'un fitxer extern amb funcions com `pd.read_csv()`.
    ```python
    import pandas as pd
    df = pd.read_csv('data.csv') # [[Load csv]]
    ```
    

---

### Inspecció i Visualització de Dades

Un cop tenim el [[Create Panda|DataFrame]], el primer pas és entendre les seves dades. Les funcions més útils es troben a [[Panda Functions]].

- **`[[Panda Head and tail|head()]]` i `[[Panda Head and tail|tail()]]`**: Mostren les primeres i les últimes files, respectivament, per a una vista ràpida del contingut.
    
- **`[[Panda Info|info()]]`**: Proporciona un resum tècnic del [[Create Panda|DataFrame]], incloent el nombre de files, columnes, tipus de dades i valors no nuls.
    
- **`[[Panda to_string()]]`**: Converteix tot el DataFrame a una cadena de text, útil per visualitzar totes les files sense truncament.
    
- **`[[Panda Max rows]]`**: Permet configurar el nombre màxim de files que Pandas mostra per pantalla.
    

---

### Neteja de Dades ([[Panda Clean EmptyCell]])

La qualitat de les dades és essencial. La neteja se centra principalment en la gestió de valors nuls (`NaN`).

- **Eliminar Valors Nuls**: El mètode **[[Panda dropna()]]** s'utilitza per eliminar les files (o columnes) que contenen valors `NaN`. Per modificar el DataFrame original directament, s'usa l'argument `inplace=True`.
    
- **Omplir Valors Nuls**: El mètode **[[Panda fillna()]]** substitueix els valors `NaN` per un valor especificat. Aquest valor pot ser un número constant o un de calculat, com la mitjana (`mean`), mediana (`median`) o moda (`mode`) d'una columna.
    
- **Eliminar Files o Columnes**:
    
    - **Condicionalment**: Es poden eliminar files que no compleixen una certa condició booleana.
       
        ```python
        # Manté només les files on el nombre de passatgers és més gran que 0
        data = data[ (data["passenger_count"] > 0) ]
        ```
        
    - **Manualment**: El mètode `drop()` pot eliminar tant files ([[Panda Delete row]]) com columnes ([[Panda Delete column]]). Per a columnes, és crucial especificar `axis=1`.
        

---

### Selecció i Indexació (Slicing)

Per accedir a subconjunts específics de dades dins d'un [[Create Panda|DataFrame]], s'utilitzen principalment dos mètodes d'indexació.

- **[[Panda loc|loc]] (Basat en Etiquetes)**: Selecciona dades utilitzant els noms (etiquetes) de les files i columnes. És inclusiu en els rangs.
    
- **[[iloc]] (Basat en Posició)**: Selecciona dades utilitzant la seva posició numèrica (índex enter). És exclusiu en el límit superior dels rangs, seguint la convenció de Python.
    

---

### Transformació i Operacions

Pandas permet realitzar càlculs i aplicar funcions a les dades de manera eficient.

- **[[Operacions a Series|Operacions Vectoritzades]]**: Les operacions aritmètiques (`+`, `*`, `<`, `>`) s'apliquen element a element sobre una [[Panda serie|Sèrie]], evitant la necessitat d'iterar.
    
- **[[Panda apply()]]**: Aplica una funció personalitzada a cada element d'una columna (o fila). És extremadament potent quan es combina amb funcions `lambda`.
```python
 # Crea una nova columna aplicant una funció lambda a 'ColumnaOriginal'
    df['ColumnaResultat'] = df['ColumnaOriginal'].apply(lambda x: x * 2)
```
- **[[Panda normalització|Normalització]]**: És una tècnica de transformació comú per escalar les dades, per exemple, restant la mitjana i dividint per la desviació estàndard (`std()`).
    
- **`groupby`**: Agrupa les dades basant-se en els valors d'una o més columnes i permet realitzar càlculs agregats (com mitjanes, sumes, etc.) per a cada grup.