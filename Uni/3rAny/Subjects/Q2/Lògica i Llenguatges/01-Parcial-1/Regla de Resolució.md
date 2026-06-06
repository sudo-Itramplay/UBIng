Procediment **sintàctic** del [[Demostrador]] que valida la [[Conseqüència Lògica]] de manera eficient. Opera sobre clàusules en [[Forma Normal Conjuntiva|FNC]].

- La regla pren dues clàusules (pares) amb un **literal complementari** ($P$ i $\neg P$). El **resolvent** és la disjunció de tots els literals excepte el parell complementari.
	- Ex: $\neg P\vee Q\vee S$ i $\neg Q\vee T$ → resolvent $\neg P\vee S\vee T$.
	- $P$ i $\neg P$ → clàusula buida ($\square$). Notació: $\vdash_R$.

> [!info] Teorema de Resolució
> $\{\varphi_1,...,\varphi_n\}\models\varphi$ ⟺ de la FNC de $(\varphi_1\wedge\dots\wedge\varphi_n\wedge\neg\varphi)$ es pot deduir $\square$ (reducció a l'absurd).

**Algorisme:** negar la conclusió → calcular FNC → aplicar resolució fins a $\square$ (èxit) o esgotar resolvents (fallo).

Per a predicats cal [[Unificació]] → [[Resolució en Predicats]].

Relacionat: [[Forma Normal Conjuntiva]] · [[Conseqüència Lògica]] · [[Resolució en Predicats]]

#assignatura/LL #tipus/teoria
