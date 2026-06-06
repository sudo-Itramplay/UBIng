Generalització de la [[Regla de Resolució]] al [[Llenguatge de Predicats]], que necessita [[Unificació]].

**Procediment del resolvent:**
1. **Renombrar variables:** les dues clàusules no poden compartir noms.
2. **Identificar literals:** un $\psi_1$ en $\varphi_1$ i un $\neg\psi_2$ en $\varphi_2$.
3. **Unificar:** trobar $\lambda$ tal que $\psi_1\lambda = \psi_2\lambda$ ([[Unificació]]).
4. **Combinar:** el resolvent és $(\varphi_1'\vee\varphi_2')\lambda$ (sense els literals oposats).

Per validar un raonament, s'aplica fins a arribar a la **[[Forma Normal Conjuntiva|clàusula buida]] ($\square$)** → el conjunt és una contradicció.

Relacionat: [[Regla de Resolució]] · [[Unificació]] · [[Forma Clausal]]

#assignatura/LL #tipus/teoria
