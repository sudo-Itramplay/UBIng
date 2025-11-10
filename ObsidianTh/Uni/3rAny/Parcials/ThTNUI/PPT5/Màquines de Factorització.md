---
aliases:
  - FM
  - Factorization Machine
---
Les Màquines de Factorització es van dissenyar per abordar directament les limitacions de les [[Uni/3rAny/Parcials/ThTNUI/PPT5/Màquines de Factorització|MF]]

>[!info] Què les diferència
>- Poden treballar millor amb les dades binaries del feedback implícit
>- Poden ser modelades amb infinites "Condicions"
>- Proporcionen un output en forma de ranking (llista) en comptes de valoració predita

![[2025-10-15_15-58.png]]
## Explicació dels punts
1 . **Generalitzen el Model:** (punt 1 i 2)
A diferència de la [[Uni/3rAny/Parcials/ThTNUI/PPT5/Màquines de Factorització|MF]] que només modela la interacció `usuari-ítem`, les FMs poden incorporar un nombre arbitrari de característiques (context, atributs de l'ítem, dades demogràfiques de l'usuari, etc.) i modelar les seves interaccions. Això les fa extremadament flexibles per a dades disperses i variades com el feedback implícit.

2. **S'adapten a l'Objectiu:** (Punt 3)
El model de les FMs es pot entrenar amb diferents funcions de pèrdua, incloses aquelles dissenyades específicament per a **tasques de rànquing** (com BPR o WARP loss). Això permet optimitzar directament la qualitat de la llista ordenada que es presentarà a l'usuari.


## Equació
La seva equació compren els dos nivells d'interacció d'una feature:
- El pes per a cada base
- la interacció entre altres [[Uni/3rAny/Parcials/ThTNUI/PPT5/Features]] i la seva combinació

- L'objectiu del model és fer una predicció, $ŷ$​, a partir d'un vector de característiques d'entrada $x$ de dimensió $d$. 

- Aquest vector pot contenir qualsevol tipus d'informació: 
	- l'ID de l'usuari, l'ID de l'ítem, el gènere de la pel·lícula, l'hora del dia, etc.

L'equació per a una Màquina de Factorització de grau dos (que modela interaccions de parells de característiques) es defineix com:

$$
\hat y(x)=w_0 + \sum_{i=1}^{d}w_ix_i+\sum_{i=1}^{d}\sum_{j=i+1}^{d} W_{ij}x_ix_j
$$

### Desglosse
##### Part 1: El Biaix Global (w0​)
- **Què és?** 
	- És un terme independent. 
	- Representa la predicció mitjana global del sistema, sense tenir en compte cap característica específica. 
És el punt de partida de la nostra predicció.

##### Part 2: La Part Lineal (Efectes de 1r Ordre)

Primer sumatori

- **Què és?** 
- Aquesta part és **exactament un model de regressió lineal**.
    - $x_i​$ és el valor de la característica i-èssima.
    - $w_i$​ és el pes o la importància que el model aprèn per a aquesta característica.
       
- **Intuïció:** Aquesta suma captura la contribució individual de cada característica a la predicció final. Per exemple, pot aprendre que les pel·lícules del gènere "Comèdia" tendeixen a rebre, de mitjana, 0.2 punts més de valoració.

##### Part 3: La Part d'Interacció (Efectes de 2n Ordre)
Segon sumatori

- **Què és?** 
Modela l'efecte de les **interaccions entre parells de característiques**.

- El doble sumatori recorre cada parell únic de característiques (i,j).

- $x_i$,$x_j$​​ representa la interacció entre la característica $i$ i la $j$.

- $W_{ij}$​ és el pes que el model aprèn per a aquesta interacció específica.


- **Intuïció:** La veritable preferència sovint no és additiva, sinó sinèrgica. Per exemple:
    
    - L'usuari "Anna" pot no tenir una preferència especialment forta per les pel·lícules de "Ciència-Ficció" en general.
    
    - Les pel·lícules del director "Denis Villeneuve" poden agradar-li, però no de manera excepcional.
    
    - No obstant això, la **combinació** d'Anna veient una pel·lícula de Ciència-Ficció **dirigida per** Denis Villeneuve pot generar un efecte molt més positiu que la simple suma de les parts. El pes WAnna, Villeneuve​ capturaria precisament aquesta sinergia.