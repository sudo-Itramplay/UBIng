---
aliases:
  - index DataFrame
---
Per agafar una o mes files/columnes fem servir el mètode `loc`


```
data = {  
  "calories": [420, 380, 390],  
  "duration": [50, 40, 45]  
}  
  
#load data into a DataFrame object:  
df = pd.DataFrame(data)


print(df.loc[[0,1]])

>	0    420    50
>	1    380    40
```

>[!info] Important
>quan fem servir [] el resultat és un DataFrame

>[!tip] Per df amb index
>per fer el `loc` refereixte al index
>`print(df.loc["day2"])`

