
- $C$ [[Uni/3rAny/Tallers/1rParcial/PPT3/Recomanador/Conjunt de tots els usuaris]]
- $S$ [[Uni/3rAny/Tallers/1rParcial/PPT3/Recomanador/Conjunt de tots els items recomanables]]
Aquests espais poden tenir una cardinalitat molt gran (que coincideixin en molts punts)

$$u: CxS \to \mathbb{R}$$
és funció desconeguda de la que tenim una mostra
$u$ assigna el grau d'utilitat o interes que té un determinat item per una determinada persona

 >[!Warning]  Problema
 >Com que $U$ No té tots els elements, sinó una mostra
 >hem d'[[Uni/3rAny/Tallers/1rParcial/PPT3/Inferir|inferir]] en els seus valors
 
En la Pràctica es sol retornar una llista ordenada dels elements seleccionants segons $u(c,s)$

>[!Danger] hem d'anar amb compte
>Les [[Uni/3rAny/Tallers/1rParcial/PPT3/Inferir|inferencies]] es poden fer de diverses maneres
>	El més important és estimant $u$ de manera que [[Uni/3rAny/Parcials/ThTNUI/PPT1i2/Optimització|optimitzi]] algun criteri
>	relacionat amb l'[[Uni/3rAny/Tallers/1rParcial/PPT2/Funció de Pèrdua|error]].
>	A aquest Error se li diu [[Error Empíric]]


>[!info] Representació
>Es sol representar en forma de matriu U
>	Les files representen $c_i$
>	Les columnes representen $s_i$
>$$
\mathbf{U} = 
\begin{pmatrix}
u(c_1, s_1) & u(c_1, s_2) & \cdots & u(c_1, s_k) \\
u(c_2, s_1) & u(c_2, s_2) & \cdots & u(c_2, s_k) \\
\vdots & \vdots & \ddots & \vdots \\
u(c_m, s_1) & u(c_m, s_2) & \cdots & u(c_m, s_k)
\end{pmatrix}
$$


