> [!note] Teoria: [[Equivalència Lògica]] · [[Equivalències en Predicats]] · [[Forma Normal Conjuntiva]]

## 1. Regles de la Implicació i Doble Implicació

- **Implicació:** 
$$\varphi\rightarrow\psi\equiv\neg\varphi\vee\psi$$ Transforma una condicional en una disjunció; és el primer pas clau per eliminar fletxes en les transformacions a FNC.

- **Contrapositiva:** $$\varphi\rightarrow\psi\equiv\neg\psi\rightarrow\neg\varphi$$ Inverteix el sentit de l'implicació negant tant l'antecedent com el conseqüent per mantenir l'equivalència.

- **Doble Implicació:** $$\varphi\leftrightarrow\psi\equiv(\varphi\rightarrow\psi)\wedge(\psi\rightarrow\varphi)$$ Descompon l'equivalència en la conjunció de dues implicacions mútues.

## 2. Regles de la Negació

- **Doble Negació:** $$\neg(\neg\varphi)\equiv\varphi$$ Dues negacions consecutives s'anul·len i restitueixen el valor original de la proposició.

- **De Morgan (Disjunció):** $$\neg(\varphi\vee\psi)\equiv\neg\varphi\wedge\neg\psi$$ La negació d'un operador "O" es converteix en un "I" de les proposicions negades individualment.

- **De Morgan (Conjunció):** $$\neg(\varphi\wedge\psi)\equiv\neg\varphi\vee\neg\psi$$ La negació d'un operador "I" es converteix en un "O" de les proposicions negades individualment.

- **Negació de la Implicació:** $$\neg(\varphi\rightarrow\psi)\equiv\varphi\wedge\neg\psi$$ Una implicació només és falsa quan el seu antecedent és cert i el seu conseqüent és fals.


## 3. Lleis de l'Àlgebra Proposicional

- **Llei Commutativa:** $$\varphi\vee\psi\equiv\psi\vee\varphi$$ i $$\varphi\wedge\psi\equiv\psi\wedge\varphi$$ L'ordre dels operands no altera el resultat en disjuncions ni en conjuncions.

- **Llei Associativa:** $$(\varphi\vee\psi)\vee\chi\equiv\varphi\vee(\psi\vee\chi)$$ i $$(\varphi\wedge\psi)\wedge\chi\equiv\varphi\wedge(\psi\wedge\chi)$$ Permet agrupar lliurement les proposicions quan s'encadenen els mateixos operadors.

- **Llei Distributiva:** $$\varphi\vee(\psi\wedge\chi)\equiv(\varphi\vee\psi)\wedge(\varphi\vee\chi)$$ i $$\varphi\wedge(\psi\vee\chi)\equiv(\varphi\wedge\psi)\vee(\varphi\wedge\chi)$$ Distribueix un operador respecte a l'altre, pas final fonamental per obtenir la Forma Normal Conjuntiva.

- **Llei d'Absorció:** $$(\varphi\vee\psi)\wedge\varphi\equiv\varphi$$ i $$(\varphi\wedge\psi)\vee\varphi\equiv\varphi$$ Simplifica l'expressió quan una proposició absorbeix un terme redundant que la conté.

- **Regles de Simplificació:** $$\varphi\vee V\equiv V$$ $$\varphi\vee F\equiv\varphi$$ $$\varphi\wedge V\equiv\varphi$$$$\varphi\wedge F\equiv F$$
- Redueix la fórmula resolent l'operació quan una de les constants lògiques (Cert/V o Fals/F) hi està implicada.
