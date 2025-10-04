---
aliases:
  - Panda list
---
Una Panda serie és una llista, com una columna de dades
```
a = [1,7,2]

myvar = pd.Series(a)

# La indexació és igual que en llistes

print(myvar[0])

>1

```


A un Panda Serie se li pot posar un label

``` 
myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar["x"])
```


També es pot fer com

```
calories = {"day1": 420, "day2": 380, "day3": 390}  
  
myvar = pd.Series(calories)  
  
print(myvar)
```
