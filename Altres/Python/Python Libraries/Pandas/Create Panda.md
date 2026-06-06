---
aliases:
  - Panda DataFrames
---
És una matriu de dades

```
mydataset = {  
  'cars': ["BMW", "Volvo", "Ford"],  
  'passings': [3, 7, 2]  
}

myvar = pd.Dataframe(mydataset)
```

Es pot crear un DataFrame a partir de dos [[Panda serie]]

```
data = {  
  "calories": [420, 380, 390],  
  "duration": [50, 40, 45]  
}  
  
myvar = pd.DataFrame(data)  
  
```

>[!tip] Carregar Dades
>Carrega dades des de un csv amb
>`pd.read_csv('data.csv`)

