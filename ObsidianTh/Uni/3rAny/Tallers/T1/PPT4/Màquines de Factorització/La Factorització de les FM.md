L'únic problema de les [[Màquines de Factorització|FM]] és la seva dimensinalitat, ja que al sumar [[Features]] es va ampliant i cada cop costa més fer els calculs

**Solució**
Factoritzar també les features tal que:

$$
W_{ij} ≈ (v_i,v_j) = v_i^Tv_j
$$ 

Deixant la fòrmula tal que:

$$
\hat y(x)=w_0 + \sum_{i=1}^{d}w_ix_i+\sum_{i=1}^{d}\sum_{j=i+1}^{d}(v_i^T v_j)x_ix_j
$$

### Perquè?
**Escenari:** Un sistema amb $10^6$ usuaris i $10^5$ ítems. El nombre total de característiques (d) és la suma: d=1,100,000.
	El nombre de paràmetres a la matriu W seria de l'ordre de $d^2≈(10^6)^2=10^{12}$ (un bilió). 

>[!warning] Si fem Factorització
>Si triem una dimensió de factors latents petita, per exemple k=10:

1,100,000 característiques×10 dimensions= $1.1 \cdot 10^7$
	(11 milions de paràmetres).

És a dir, passem de $O(d^2)$ a $O(d \cdot k)$
