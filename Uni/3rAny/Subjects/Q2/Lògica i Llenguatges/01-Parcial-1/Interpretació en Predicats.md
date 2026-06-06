Una **interpretació ($I$)** és l'estructura que defineix el context on operem en el [[Llenguatge de Predicats]].

- **Domini ($D$):** conjunt no buit d'elements (els enters, els humans…). $D^n$ és el producte cartesià.
- **Assignacions:**
	- a cada variable $x$ → un element $I(x)\in D$.
	- a cada constant $c$ → un element fix $I(c)\in D$.
	- a cada funció $f$ d'$n$ args → una funció $I(f):D^n\rightarrow D$.
	- a cada predicat $R$ → una relació $I(R)\subseteq D^n$.

**Avaluació de [[Terme|termes]]:** se substitueixen pels seus valors (ex: $I(f(a,v_2))=2+6=8$). El resultat és sempre un element de $D$.

Relacionat: [[Avaluació de Fórmules]] · [[Terme]] · [[Llenguatge de Predicats]]

#assignatura/LL #tipus/teoria
