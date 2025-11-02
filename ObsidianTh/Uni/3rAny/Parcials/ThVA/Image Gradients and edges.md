# Derivada d'una imatge i cantonades

#### Què identifica a un Edge?
Varies coses:
- Canvia orientació
- Canvia contrast
- casts shadows
- canvis de depth
Tot això és pot definir amb: Canvi brusc en la intesnitat de la imatge
- Imatge:
![[Pasted image 20251101194527.png]]
- Si agafem una fila d'una imatge i la representem:
![[Pasted image 20251101194604.png]]
- On la seva derivada és tal que:
![[Pasted image 20251101194635.png]]

Per fer això hem de veure com abordar les derivades  a una convolució

Sabent que la derivada es pot fer tal que:
$$
lim_{\epsilon \to 0} \frac{f(x+\epsilon, y) - f(x,y)}{\epsilon}
$$

Ens trobem ab el problema de que el  resultat ha de ser dicret, així que aproximarem les dades:
$$
lim_{\epsilon \to 0} \frac{f(x+1, y) - f(x,y)}{1}
$$




##### Com ho computem?
![[Pasted image 20251101195024.png]]
Aquest serà el nostre box filter, per horitzontals:
### Box filters per a derivades

##### H
![[Pasted image 20251101200239.png]]

##### V
![[Pasted image 20251101200256.png]]

>[!error] Soroll
>El problema d'aquest procediment és que si hi ha soroll a la imatge l'escamparem

Un recurs que es fa servir és ferla mitjana de 3 derivades

## Edge filters

![[Pasted image 20251101200435.png]]

>[!note] Què diferència a Sobel de Prewitt
>- Sobel, by using non-uniform weights, gives more importance to the closest neighbors.


## Gradient
Apunta a cal a la direcció de on hi ha el canvi d'intensitat més brusc (extrems de la 2a derivada, o els punts de màxim pendent en una funció normal)


>[!tip] Ojo
>Aquest concepte és el que indica el **edge strenght**

