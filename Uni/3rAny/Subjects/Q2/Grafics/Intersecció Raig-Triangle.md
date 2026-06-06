Cas concret d'[[Intersecció Raig-Objecte]] (vegeu també la pràctica [[Intersecció d'un Triangle]]).

1. **Calcular la [[Normal]]** del triangle: $\vec{N} = (V_1-V_0)\times(V_2-V_0)$, normalitzada.
2. **Intersecció raig-pla:** $t = \frac{(V_0 - A)\cdot \vec{N}}{\vec{B}\cdot \vec{N}}$. Si el denominador ≈ 0 (paral·lel) o $t<0$ (darrere), descartar.
3. **Test d'interior — coordenades baricèntriques** $(u,v,w)$: $P = u V_0 + v V_1 + w V_2$. El punt és **dins** si $u,v,w \ge 0$ i $u+v+w=1$.
4. **Validar rang** $[t_{min}, t_{max}]$ i omplir la info d'impacte.

Les baricèntriques també serveixen per **interpolar** normals o coordenades de [[Textures|textura]].

Relacionat: [[Intersecció Raig-Objecte]] · [[Malla de Triangles]] · [[Normal]] · [[Intersecció d'un Triangle]]

#assignatura/Grafics #tipus/teoria
