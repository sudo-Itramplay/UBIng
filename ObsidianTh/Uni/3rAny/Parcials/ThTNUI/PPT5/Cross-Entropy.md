---
aliases:
  - Entropia creuada
---
L'Entropia Creuada és una [[Uni/3rAny/Tallers/1rParcial/PPT2/Funció de Pèrdua]] per a problemes de [[Uni/3rAny/Parcials/ThTNUI/PPT5/Classificació]]

### Binari
>[!example] Binari (amb dos classes)
>Donat un dataset $(x_i, y_i)$ amb $n$ exemples de 



$$
CE = - \frac{1}{n} \sum_{i=1}^n (y_i \log(\hat y_i) + (1-y_i) \log(1- \hat y_i))
$$

on:
- $\hat y_i$ is the predicted probability for class `1` 
- $1-\hat y_i$is the predicted probability for class `0`.

### Multiclasse

>[!example] Multiclasse
>Donat un dataset $(x_i, y_i)$ amb $n$ exemples de 

$$
CE = - \frac{1}{n} \sum_{i=1}^n \sum_{j=1}^K y^j_i \log(\hat y^j_i)
$$

on:
- $y^j$ és 0 o 1 indicant si j és la classificació correcta per x 
- $\hat y^j$ is the predicted probability for class j for x.

```python
from math import log2

def cross_entropy(p, q):

	return -sum([p[i]*log2(q[i]) for i in range(len(p))])

p = [0.10, 0.40, 0.50]
q = [0.80, 0.15, 0.05]

ce_pp = cross_entropy(p, p)
ce_qq = cross_entropy(q, q)

> ce_pp: 1.361 bits
> ce_qq: 0.884 bits
```

## Funció

El que fem amb això és mesurar la diferència o "distància" entre dues distribucions de probabilitat:

1. La distribució de probabilitat **predita pel model** (ex: la sortida d'una funció Softmax).

2. La distribució de probabilitat **real** (la veritat o _ground truth_, generalment representada com un vector _one-hot_).


>[!tip] **Objectiu**
>**Minimitzar l'entropia creuada**, la qual cosa equival a fer que la distribució de probabilitat predita pel model sigui el més semblant possible a la distribució real.


>[!example] Codi
>```python
>import numpy as np
>def b_cross_entropy_loss(yHat, y):
>    if y == 1:      
> 	   return -np.log(yHat)    
>    else:
> 	 return -np.log(1 - yHat) 
> 	 

 ```
 b_cross_entropy_loss(0.99, 1) 
 >>>	0.01005033585350145
 b_cross_entropy_loss(0.01, 1)
 >>> 	4.605170185988091
 ```


# Representació

# ![](https://hackmd.io/_uploads/BkzKKUSkkg.png)





