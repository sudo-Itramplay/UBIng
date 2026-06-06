#Python

## Per obtenir index i element alhora

Enumerate retorna parells on el primer element és l'index i el segon el value de la seqüència iterable
```
for a,b in enumerate(['a','b','c']):
	print(a,b)


>0 a
>1 b
>2 c
```

## Combinar/unir múltiples iterables
- Retorna una tupla de la combinació dels iterables
- Uneix el primer de la llista 1 amb el primer de la llista 2 i així succesivament.
- En cas de tenir llises de longituds diferents, com que nomes farà parells, farà que:
	`lenfinal = min( len(list1) , len(list2)`

```
for i in zip([1,2,3],[3,4,5,6]):
	print(i)


>(1,3)
>(2,4)
>(3,5)
```
