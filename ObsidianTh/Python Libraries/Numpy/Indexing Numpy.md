
```
arr = np.array([[1,2,3], 
				[4,5,6],
				[7,8,9]])

print(arr)
> [[1 2 3]
  [4 5 6]
  [7 8 9]]


# Accedir columna fila
arr[0,0] #row column

> 1


# Obtenir elements més grans a 
arr[arr > 5]

> [6 7 8 9]


# Assignació condicional
	# assignem als parells el valor 10
arr[arr%2 == 0] = 10
> [[1 10 3]
   [10 5 10]
   [7 10 9]]
   
```