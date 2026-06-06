
## 1. Fonaments de la Lògica de Predicats

Avui el mètode de resolució es generalitza per a llenguatges de predicats. És crucial distingir tres tipus de fórmules segons la seva interpretació:

* **Tautologia**: Una fórmula que resulta certa en **totes** les interpretacions possibles.


* **Satisfactible**: Aquella que és certa en, almenys, **una** interpretació.


* **Contradicció**: La fórmula que és falsa en **totes** les interpretacions.


>[!tip] *Relació clau**: 
>Una fórmula $\varphi$ és una tautologia si i només si la seva negació $\neg\varphi$ és una contradicció.



## **Conseqüència lògica** ($\models$) 
La consequencia logica és el que ens permet validar raonaments. Diem que $\varphi$ és conseqüència lògica de un conjunt de premisses $\{\varphi_1, ..., \varphi_n\}$ si la implicació conjunta $(\varphi_1 \wedge ... \wedge \varphi_n) \rightarrow \varphi$ és una tautologia. 

Aquesta base teòrica permet el disseny de **demostradors** (com OTTER o PROVER9 en matemàtiques o Prolog a informatica)

---

## 2. Formes Clausals i Algoritme de Transformació

Per aplicar el mètode de resolució, primer hem de transformar les fórmules a una estructura estàndard anomenada **forma clausal**. 

>[!info] Formalitzacio
>Una fórmula està en forma clausal si té l'aspecte $\forall x_1 ... \forall x_n (\psi_1 \wedge ... \wedge \psi_m)$, on cada $\psi_i$ és una **clàusula** (una disjunció de literals). El nucli és la part sense els quantificadors universals.


# Mecanitzacio

L'algoritme per obtenir-la consta de 7 passos crítics per a l'examen:

1. **Eliminar implicacions i co-implicacions**: Substituir $\varphi \rightarrow \psi$ per $\neg\varphi \vee \psi$.


2. **Interioritzar negacions**: Aplicar lleis de De Morgan i les equivalències de negació de quantificadors ($\neg\exists x \varphi \equiv \forall x \neg \varphi$).


3. **Normalitzar variables**: Moure quantificadors si la variable no apareix lliure en l'altra part de la fórmula.


4. **Skolemització**: Eliminar quantificadors existencials ($\exists z$). Si $z$ no està sota un $\forall$, es canvia per una constant nova ($c$). Si està sota l'àmbit de variables $x_1, ..., x_n$ quantificades universalment, es substitueix per una funció $f(x_1, ..., x_n)$.


5. **Renombrar variables**: Evitar conflictes de noms entre variables lligades.


6. **Extracció de quantificadors**: Moure tots els $\forall$ cap a l'exterior.


7. **Distributivitat**: Aplicar regles distributives per obtenir una conjunció de clàusules al nucli.


És vital recordar el **Teorema de la forma clausal**: 
>[!info] **Teorema de la forma clausal**:
>una fórmula $\varphi$ és una contradicció si i només si la seva forma clausal $\varphi'$ també ho és, encara que **no són necessàriament equivalents** de forma general.

---

## 3. Unificació d'Expressions

La unificació és el procés de fer que dues expressions (termes o fórmules atòmiques) siguin idèntiques mitjançant una **substitució**. Una substitució $\lambda$ és un conjunt de parells $\{x_i = t_i\}$ on es reemplacen variables per termes.

L'algoritme de unificació utilitza una pila d'igualtats ($P$) i segueix aquestes regles:

* Si traiem una igualtat de variables o constants idèntiques, continuem.


* Si tenim una variable $e$ i un terme $e'$, i $e$ no apareix dins de $e'$, apliquem la substitució a tota la pila i la guardem al resultat.


* Si tenim funcions o predicats iguals $f(s_1, ..., s_n) = f(t_1, ..., t_n)$, descomposem i posem a la pila les igualtats dels seus arguments $s_i = t_i$.


* Si hi ha un conflicte de símbols (ex: $f(a) = g(x)$), l'algoritme retorna **"fallo"**.



Aquest procés és el "motor" que permet emparellar literals durant la resolució, trobant el **unificador** necessari per cancel·lar termes oposats.

---

## 4. El Mètode de Resolució en Predicats

El **resolvent** és la clàusula resultant de combinar-ne dues de preexistents que contenen literals oposats unificables. El procediment és:

1. **Renombrar variables**: Les dues clàusules no poden compartir noms de variables.


2. **Identificar literals**: Buscar un literal $\psi_1$ en $\varphi_1$ i un $\neg\psi_2$ en $\varphi_2$.


3. **Unificar**: Trobar el unificador $\lambda$ tal que $\psi_1\lambda = \psi_2\lambda$.


4. **Combinar**: El resolvent és $(\varphi_1' \vee \varphi_2')\lambda$, on $\varphi_i'$ són les clàusules originals sense els literals oposats.



Per demostrar que un conjunt de clàusules és inconsistent (i per tant, validar un raonament), apliquem la regla de resolució successivament fins a arribar a la **clàusula buida** ($\square$). Si arribem a la clàusula buida, hem demostrat que el conjunt original era una contradicció. L'exemple final de les transparències mostra com, a partir de 4 premisses (input), s'unifiquen termes com $\{x=a, y=b\}$ i $\{z=f(a)\}$ per anar derivant noves clàusules fins a la contradicció final .
