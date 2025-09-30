La utilitat de $u'(c,s)$ de l'ítem $S$ per l'user $C$
1. u(c,s) si l'ha valorat
2. Sinó: estimació construida a partir de les utilitat $u(c_i,s)$ 
	Es a dir, determinarem u(s) per $c_1$ (a qui li volem recomanar) segons la persona $c_i$


>[!warning] Limitacions
> 1. Cold Start: Els nous usuaris no tindràn amb què compararse
>2. Nou ítem: Ningú l'haurà valorat, i per tant no es recomanarà
>3. ítem poc freqüent: L'item que no tingui masses valoracions, es recomanarà malament

>[!tip] Els ítems poc freqüents importen
> - El número de ítems poc freqüents és més alt que de freqüents
> - Els items freqüents es vendran igualment que no es recomanin

## Exemple
Si la nostra [[Heurística]] consta de fer una [[suma ponderada]] tal que:
$$
\sum_{j=1}^{m}{ \alpha_{c_q c_j} \cdot u(c_j, s_p)} 
$$
donada la matriu de la [[Funció d'utilitat]]
>$$
\mathbf{U} = 
\begin{pmatrix}
? & \cdots & u_{1p} & \cdots & ? && \\
\vdots & \vdots &\vdots & \vdots & \vdots\\
? & \cdots & ?_p  & \cdots& u_{2n} \\
\vdots & \vdots &\vdots & \vdots & \vdots\\
u(c_m, s_1) & \cdots & u(c_m, s_k)& \cdots& ?
\end{pmatrix}
$$

És a dir: comparem un usuari amb UN altre usuari, agafant els valors del usuari que aquest hagi donat valoració

Quan un dels dos usuaris no hagi valorat, no farem ús d'aquella cel·la

## Anexe
[[Conjunt de tots els usuaris]]
[[Conjunt de tots els items recomanables]]