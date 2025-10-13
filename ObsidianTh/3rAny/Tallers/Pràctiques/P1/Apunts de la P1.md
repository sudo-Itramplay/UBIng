
Funcions de Pandas, i com unir-les

## Axis
axis=0 -> Files
axis=1-> Columnes


## Neteja
- Treure NaN[[Panda dropna()|]]
```python
data = data.dropna()
```

- Treure segons una condició 
[[Panda Delete row]], [[Panda fillna()]], [[Panda Clean EmptyCell]]

```python
data = data[ (data["passenger_count"] > 0) ]

#També es pot anidar
data = data[(data["passenger_count"] > 0) & (data["passenger_count"] < 7)]

```

- Eliminar  una columna
```python
data.drop(columns=['fare_amount', 'total_amount', 'payment_type'], axis=1, inplace=True)
```

## Indexació
- `loc`
El mètode `.loc` s'utilitza principalment per a la indexació basada en **etiquetes** (noms de files i columnes). Per agafar una cel·la
#### Selecció per etiquetes
```python
df.loc['Fila2', 'ColumnaA']
```
- Retorna el valor en la fila amb l'etiqueta 'Fila2' i la columna 'ColumnaA'.
#### Selecció d'interval de files
```python
df.loc['Fila2':'Fila5']
```
- Selecciona les files amb etiquetes 'Fila2', 'Fila3', 'Fila4' i 'Fila5' (el final s'inclou).
	- 
#### Selecció Condicional
```python
df.loc > 100, 'Producte']
```
Selecciona les files on el valor de 'Sales' és superior a 100 i mostra la columna 'Producte'.


- `iloc`
El mètode `.iloc` s'utilitza exclusivament per a la indexació basada en la **posició sencera** (índex numèric). Aquesta posició comença a 0.

```python
df.iloc[posicio_files, posicio_columnes]
```
### Selecció per posició
`df.iloc`
Retorna el valor a la primera fila (posició 0) i la tercera columna (posició 2).
### Selecció d'interval de files
`df.iloc[2:5]`
Selecciona les files amb posicions 2, 3 i 4 (la posició 5 s'exclou).
### Selecció de files i columnes
`df.iloc[:, ]`
Selecciona totes les files (`:`) i només les columnes a les posicions 0 i 3.

>[!tip] Slicing
>Quan s'utilitza el _slicing_ (intervals com `[i:j]`), `.iloc` **exclou** la posició final, seguint la lògica estàndard de Python.


## Transformar

- Calculs
Els calculs aritmètics afectaràn a tot un dataframe, o a tots els elements d'una columna
[[Operacions a Series|]]

```python
data["v_mean"] = data["trip_distance"]/((data["tpep_dropoff_datetime"] - data["tpep_pickup_datetime"]).dt.total_seconds() / 3600)
```

- Funcions
[[Panda Functions|]]
```python
# adding 5 to each value 
#-> num representa una cel·la 
new = df.apply(lambda num : num + 5)`

```

```python
#Aqui s'aplica una funció, i al resultat se'l filtra segons una condició
    data = data[
            data.apply(
                lambda x: velocitat_mitja(
                    x["tpep_pickup_datetime"],
                    x["tpep_dropoff_datetime"],
                    x["trip_distance"]) < 66, axis = 1)]
```

[[Plotting]]

## Groupby

```python
df.groupby(['year', 'carrier'])['passenger_count'].mean()
```
Executant surt:
```
year carrier  mean
2020 AA      160.3 
     DL      155.1 
     UA      148.9 
2021 
     AA      180.7 
     DL      172.4 
     UA      174.5 
Name: passenger_count, dtype: float64
```