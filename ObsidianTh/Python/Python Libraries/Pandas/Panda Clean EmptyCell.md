## 1
Eliminar rows amb `EmptyCells`
[[Panda dropna()]]

```
df = pd.read_csv('data.csv')  
  
new_df = df.dropna()  
  
print(new_df.to_string())
```

##  2
Emplenar rows amb `EmptyCells`
[[Panda fillna()]]

```
df.fillna(130, inplace=True)
```


## 3
Reemplaçant columnes en Concret
amb [[Panda fillna()]] també

## 4
Reemplaçar per un valor concret

>[!info]
>Després d'aquestses funcions haurem de fillna tq:
>`df.fillna({"Calories": x}, inplace=True)`
### 1 Mitjana
`x = df["Calories"].mean()`
### 2 Mediana
`x = df["Calories"].median()`
### 3 Moda
`x = df["Calories"].mode()[0]`