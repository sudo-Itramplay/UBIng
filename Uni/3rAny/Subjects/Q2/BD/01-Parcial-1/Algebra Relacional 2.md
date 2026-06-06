# Resum Detallat: Àlgebra Relacional II

## 1. Fonaments i Tipus de Join 

>[!info] Definició: Join
>És, en essència, una selecció aplicada sobre un producte cartesià.
> - És l'eina principal per combinar informació de diferents relacions. 
>

Hi ha 4 tipus:

* **Theta Join ($\gg_F$):** Defineix una relació amb les files que satisfan un predicat genèric $F$ dins del producte cartesià de $R$ i $S$.
* **Equi Join:** És una variant del Theta Join on el predicat $F$ conté exclusivament l'operador d'igualtat ($=$).
![[Pasted image 20260321104409.png]]
* **Procediment algebraic:** Per calcular-lo, primer es realitza el producte cartesià $R \times S$ i després s'aplica l'operació de selecció $\sigma_F$.
* **Ordre de la relació:** L'ordre del resultat és la suma dels ordres de les relacions originals $R$ i $S$.

>[!quote] **Exemple pràctic:** 
>Si volem casar clients amb les seves visites, utilitzem el `client_id` com a nexe d'unió entre les taules `CLIENT` i `VIEWING`.
>![[Pasted image 20260321104458.png]]
>![[Pasted image 20260321104507.png]]
>![[Pasted image 20260321104522.png]]


>[!quote] Exemple 2
>![[Pasted image 20260321104556.png]]


---

## 2. Natural Join 

>[!info] Definició: **Natural Join** 
>És una evolució de l'Equijoin que simplifica la combinació de taules basant-se en atributs comuns.
>![[Pasted image 20260321104658.png]]
>* Es realitza sobre tots els atributs que tenen el mateix nom en ambdues relacions.


>[!warning] Compte : **Eliminació de duplicats** 
>A diferència del Theta Join, el Natural Join elimina automàticament les columnes duplicades del resultat; no tindrem dos camps amb el mateix nom.


* **Algorisme en tres passos:**
	1. Producte cartesià $R \times S$.
    2. Selecció basada en la igualtat dels atributs comuns.
    3. Projecció per descartar els atributs repetits.
* **Càlcul de l'ordre:** L'ordre final és la suma dels ordres de $R$ i $S$ menys el nombre d'atributs comuns.
* **Context d'ús:** S'utilitza quan no s'especifica un predicat $F$ explícit i es volen aprofitar les claus foranes amb el mateix nom.



>[!quote] Exemple:
>![[Pasted image 20260321104925.png]]
>![[Pasted image 20260321104942.png]]
>![[Pasted image 20260321104958.png]]



>[!quote] Exemple 2
>![[Pasted image 20260321105018.png]]
>![[Pasted image 20260321105028.png]]
>![[Pasted image 20260321105144.png]]
>![[Pasted image 20260321105154.png]]




---

## 3. Outer Join 

Sovint, en realitzar un Join, perdem files que no tenen correspondència a l'altra taula. 
>[!done] L'**Outer Join** soluciona aquesta pèrdua d'informació.


* **Objectiu:** Mostrar les files que no tenen parella (unpaired rows) en l'altra relació.

* **Gestió de buits:** Els valors que manquen a la relació oposada s'omplen amb valors **NULL**.
* **Tipus d'Outer Join:**
    * **Left Outer Join:** Es mostren totes les files de la relació de l'esquerra ($R$), encara que no tinguin correspondència en $S$.
    * **Right Outer Join:** Es mantenen totes les files de la dreta ($S$).
    * **Full Outer Join:** Es mantenen totes les files d'ambdues relacions.

* **Aplicació real:** És vital per a informes on volem veure, per exemple, "totes les propietats, tinguin o no visites registrades".

>[!quote] Exemple:
>![[Pasted image 20260321105623.png]]
>![[Pasted image 20260321105637.png]]
>



---
### Intersecció ($\cap$)

La intersecció és una operació de conjunts que ens permet trobar elements comuns entre dues relacions.

>[!info] Definició : Intersecció
>- **Definició**: Genera una relació amb les files que apareixen simultàniament a $R$ i a $S$.


>[!warning] **Condició de compatibilitat**: 
>Per realitzar una intersecció, les relacions $R$ i $S$ han de ser compatibles (mateix esquema o nombre d'atributs amb dominis equivalents).


- **Relació amb la Diferència**: La intersecció es pot expressar derivadament com $R \cap S = R - (R - S)$.
    
- **Exemple d'examen**: Trobar ciutats que tinguin tant oficines (`BRANCH`) com propietats per llogar (`PROPERTY4RENT`).

>[!quote] Exemple:
>![[Pasted image 20260321110011.png]]
>![[Pasted image 20260321110027.png]]
>

---
### Divisió ($\div$)

La divisió és una de les operacions més complexes i es sol identificar amb la paraula clau "tots" en els enunciats.

- **Lògica d'operació**: Donada una relació $R(x, y)$ i $S(y)$, el resultat $R \div S$ són els valors de $x$ que estan relacionats amb tots els valors de $y$ presents a $S$.
    
- **Expressió amb operacions bàsiques**: La divisió es defineix mitjançant la noció de "desqualificació". Un valor $x$ es desqualifica si existeix algun $y$ a $S$ tal que la parella $(x, y)$ no està a $R$.
    
- **Fórmula de desqualificació**: $Desqualificats(x) = \Pi_x ((\Pi_x(A) \times B) - A)$.


>[!quote] Exemple
>![[Pasted image 20260321110742.png]]


---
### Gestió de valors NULL i Lògica Tri-valent

La presència de valors NULL obliga a abandonar la lògica binària tradicional per adoptar una lògica de tres valors: Cert, Fals i Desconegut (Unknown).

- **Comparacions**: Qualsevol comparació amb un NULL resulta en `unknown`.

#### OR
- **Taules de veritat**:
    - `unknown OR true = true`
    - `unknown OR false = unknown`
    - `unknown OR unknown = unknown`

#### AND
- **Taules de veritat**:
    - `unknown AND true = unknown
    - `unknown AND false = false`
    - `unknown AND unknown = unknown`

#### NOT
- `NOT unknown = unknown`


- **Impacte en operacions**:
    
    - **Selecció**: Només es mantenen les files on el predicat és estrictament `true` (es descarten els `false` i els `unknown`).
	
	- **Joins** Si un dels dos atributs en els que li fem el join és NULL, NO s'afegeix la columna 
    
    - **Projecció/Conjunts**: Els NULLs es tracten com valors normals per identificar i eliminar duplicats.


---
### Funcions d'Agregació ($\mathcal{G}$)

Les funcions d'agregació estenen l'àlgebra relacional per realitzar càlculs estadístics i resums de dades.

- **Funcions comunes**: `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`.
    
- **Tractament de NULLs**:
    
    - `COUNT(*)` compta totes les files, incloent NULLs.
    - `COUNT(A)` Compta els valors no-NULLS del atribut A         
    - Les altres funcions (`SUM`, `AVG`, etc.) ignoren els valors NULL en els seus càlculs.

- **Sintaxi de l'agrupament**: $$_{Atributs\_d'agrupament}\mathcal{G}_{Llista\_agregació}(R)$$

- Els atributs d'agrupament són opcionals; si no n'hi ha, l'agregació es fa sobre tota la relació.

![[Pasted image 20260321112720.png]]

- **Filtrat post-agregació**: Per filtrar grups basant-se en el resultat d'una agregació (equivalent al `HAVING` de SQL), s'aplica una selecció $\sigma$ sobre el resultat de l'operació $\mathcal{G}$.

*Hi ha exc en el ppt perpracticar