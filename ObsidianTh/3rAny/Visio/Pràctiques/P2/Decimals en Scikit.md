Quan fem servir [[Scikit-image]] és possible que ens sorgeixi el problema deque ens surtin divisions, i amb això decimals

**Imatge més Fosca (Divisió):** Es divideix la imatge per 2 (`cat/2`).

>[!warning] **Problema:**
> La divisió amb `uint8` produeix un _array_ de **`float64`**.

>[!tip] **Solució (Visualització):**
> Per a visualitzar-lo correctament, s'ha de **convertir a `int`** (`.astype(int)`) o a un altre tipus enter, ja que les funcions de visualització (`imshow`) sovint esperen enters o _floats_ escalats. L'exemple mostra la **pèrdua de precisió** en fer el _cast_ a `int`


```
# Imatge Brillant (visualització forçada)


ax = axs[1,0]
ax.imshow(cat*2, vmin=0, vmax=255) 



# NOTA: Amb dtype uint8, l'operació *2 pot patir wrapping. L'efecte real depèn de la implementació.

# Imatge Fosca (canvi de dtype i pèrdua de precisió)

cat4 = cat/2 # Converteix a float

print(cat4.dtype, cat4.min(), cat4.max()) 
# Sortida esperada: float64 0.0 127.5

ax = axs[1,1]
ax.imshow(cat4.astype(int), vmin=0, vmax=255) # Cast a int per visualitzar
```
