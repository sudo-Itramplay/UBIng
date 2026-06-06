
# 📂 Pandas: Manipulació Avançada de Dades

Tags: #python #datascience #pandas #data-engineering

Data: 2025-12-15

## 1. Merge (Combinació de DataFrames)

> **Concepte:** `merge` és l'equivalent als **JOINs** de SQL. Combina dos DataFrames basant-se en una o més claus (columnes) comunes.

### Sintaxi Bàsica


```python
pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None)
```

### Paràmetres Clau

- **`left`, `right`**: Els dos objectes DataFrame a combinar.
    
- **`on`**: Nom de la columna clau (ha d'existir a tots dos).
    
- **`how`**: Tipus de join:
    
    - `'inner'` (per defecte): Intersecció. Només claus presents a tots dos.
        
    - `'outer'`: Unió. Totes les claus; omple amb `NaN` on faltin dades.
        
    - `'left'`: Totes les claus de l'esquerra.
        
    - `'right'`: Totes les claus de la dreta.
        
- **`suffixes`**: Tupla per afegir sufixos a columnes amb el mateix nom (ex: `('_x', '_y')`).
    

### 💻 Codi d'Exemple: Merge

Python

```python
import pandas as pd

# 1. Definició de Dades
df_usuaris = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'nom': ['Anna', 'Bernat', 'Carla', 'David']
})

df_comandes = pd.DataFrame({
    'comanda_id': [101, 102, 103],
    'usuari_id': [1, 2, 5],  # L'usuari 5 no existeix a df_usuaris
    'import': [250, 150, 300]
})

# 2. Operació: LEFT JOIN
# Volem tots els usuaris, tinguin comandes o no.
resultat = pd.merge(
    left=df_usuaris,
    right=df_comandes,
    left_on='id',       # Clau taula esquerra
    right_on='usuari_id', # Clau taula dreta
    how='left'
)

print(resultat)
```

Resultat esperat:

Observa com en David té NaN perquè no té comandes, i l'usuari 5 desapareix (perquè és un left join sobre usuaris).

---

## 2. GroupBy (Estratègia Split-Apply-Combine)

> **Concepte:** Divideix les dades en grups basats en alguna criteri (**Split**), aplica una funció a cada grup (**Apply**), i combina els resultats en una nova estructura (**Combine**).

### Sintaxi Bàsica

Python

```python
df.groupby(by)[columna_objectiu].funcio_agregacio()
```

### Operacions Comunes

1. **Agregació simple:** `sum()`, `mean()`, `max()`, `count()`.
    
2. **Agregació múltiple (`agg`):** Aplicar diferents funcions a diferents columnes.
    
3. **Filtrat (`filter`):** Eliminar grups que no compleixen una condició.
    

### 💻 Codi d'Exemple: GroupBy

Python

```python
# 1. Dades
df_vendes = pd.DataFrame({
    'departament': ['IT', 'IT', 'RH', 'RH', 'Vendes', 'Vendes'],
    'empleat': ['A', 'B', 'C', 'D', 'E', 'F'],
    'salari': [3000, 3200, 2500, 2600, 4000, 4200],
    'bonus': [100, 100, 50, 50, 200, 300]
})

# 2. Operació: Agregació Múltiple
# Volem el salari mitjà i el bonus total per departament.
informe = df_vendes.groupby('departament').agg({
    'salari': 'mean',  # Mitjana del salari
    'bonus': 'sum'     # Suma del bonus
})

# Renombrar columnes per claredat (opcional però recomanat)
informe.columns = ['salari_mitja', 'bonus_total']

print(informe)
```

> [!TIP] Professor Note
> 
> El resultat d'un groupby converteix la columna agrupada ('departament') en l'Índex del nou DataFrame. Si vols que segueixi sent una columna normal, utilitza as_index=False dins del groupby.

---

## 3. Pivot Table (Taules Dinàmiques)

> **Concepte:** Permet reestructurar i resumir dades, convertint valors d'una columna en noves columnes (capçaleres). És una generalització del `groupby` però multidimensional. Ideal per a informes matricials.

### Sintaxi Bàsica


```python
pd.pivot_table(data, values=None, index=None, columns=None, aggfunc='mean', fill_value=None)
```

### Paràmetres Clau

- **`index`**: La clau que es quedarà com a files.
    
- **`columns`**: La clau els valors únics de la qual es convertiran en noves columnes.
    
- **`values`**: La columna numèrica que volem analitzar/agregar.
    
- **`aggfunc`**: Funció a aplicar (per defecte és la mitjana `mean`, però sovint voldràs `sum` o `count`).
    
- **`fill_value`**: Valor per substituir els `NaN` resultants (ex: 0).
    

### 💻 Codi d'Exemple: Pivot Table


```python
# 1. Dades
df_metriques = pd.DataFrame({
    'data': ['2023-01', '2023-01', '2023-01', '2023-02', '2023-02'],
    'ciutat': ['BCN', 'MAD', 'VLC', 'BCN', 'MAD'],
    'categoria': ['Electrònica', 'Roba', 'Electrònica', 'Roba', 'Electrònica'],
    'vendes': [1000, 500, 800, 600, 1200]
})

# 2. Operació: Matriu Ciutat vs Categoria
# Volem veure quant s'ha venut de cada categoria a cada ciutat.
taula_dinamica = pd.pivot_table(
    df_metriques,
    values='vendes',
    index='ciutat',           # Files: Ciutats
    columns='categoria',      # Columnes: Categories de producte
    aggfunc='sum',            # Suma total de vendes
    fill_value=0              # Si no hi ha vendes, posar 0
)

print(taula_dinamica)
```

---

## Resum Comparatiu

|**Mètode**|**Propòsit Principal**|**Dimensionalitat del Resultat**|
|---|---|---|
|**Merge**|Enllaçar dades de diferents fonts (SQL Join).|Horitzontal (més columnes).|
|**GroupBy**|Reduir dades mitjançant càlculs (Agregació).|Vertical (menys files, mateixa estructura).|
|**Pivot**|Reorganitzar dades per anàlisi visual/matricial.|Matriu 2D (canvi d'estructura dràstic).|

---

### Següent pas

Vols que et prepari un **exercici integrat** on carreguem un dataset "brut" fictici i hàgim de netejar-lo utilitzant les tres tècniques en cadena per obtenir un informe final?