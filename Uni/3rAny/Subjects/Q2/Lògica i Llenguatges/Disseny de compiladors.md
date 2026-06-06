## 1. El Concepte de $\lambda$-tancament (Lambda-cierre)

Abans de transformar un autòmata, hem d'entendre com es mou la informació sense consumir entrada. Aquest és el nucli dels autòmates indeterministes (NFA).

- **Definició formal**: Si tenim un estat $p$, el seu $\lambda$-tancament, denotat com $\Lambda(p)$, és el conjunt d'estats als quals es pot arribar des de $p$ seguint només transicions buides ($\lambda$), sense llegir cap símbol de l'alfabet.
    
- **Propietat reflexiva**: Per definició, tot estat pertany al seu propi $\lambda$-tancament ($p \in \Lambda(p)$).
    
- **Simplificació de notació**: Per facilitar el treball algorítmic, un conjunt d'estats $\{A, B, C\}$ se sol representar simplement com la seqüència $ABCD$.
    
- **Exemple pràctic**: 
	- ![[Pasted image 20260418121417.png]]
	- ![[Pasted image 20260418121433.png]]
	- 
    

## 2. Algoritme de Transformació de NFA a DFA

Aquest procés és vital per a l'eficiència, ja que un autòmata determinista (DFA) és molt més senzill d'implementar en programari. L'algoritme es basa en la "construcció de subconjunts".

- **Estat inicial**: El nou estat inicial $q'_0$ del DFA és el $\lambda$-tancament de l'estat inicial original ($q'_0 = \Lambda(q_0)$).
    
- **Funció de transició ($\delta'$)**: Per a un conjunt d'estats $X$ i un símbol $a$, la transició es calcula buscant tots els estats $q$ assolibles des de qualsevol $p \in X$ amb el símbol $a$, i després aplicant el $\lambda$-tancament a cadascun d'ells.
    
- **Procés iteratiu**: Es calculen les transicions per als nous estats que van apareixent fins que no en surti cap de nou.
    
- **Estats d'acceptació**: Un estat del DFA és acceptador si conté, almenys, un estat que era acceptador en l'autòmata original ($X \cap F \neq \emptyset$).
    
- **Estat d'error**: En el DFA resultant, les transicions no definides (conjunt buit $\emptyset$) es dirigeixen a un "estat d'error" no acceptador del qual no se surt mai.

#### Exemple
![[screenshot-2026-04-18_12-16-51.png]]
![[screenshot-2026-04-18_12-17-02.png]]
![[screenshot-2026-04-18_12-17-14.png]]


## 3. Fases en el Disseny d'un Compilador

El disseny de compiladors és l'aplicació pràctica més important de la teoria d'autòmates. Un compilador tradueix llenguatge d'alt nivell a codi màquina executable.


Està format per 3 fases:
- **Anàlisi Lèxic**: És la primera fase. Llegeix el fitxer de caràcters i els agrupa en categories sintàctiques anomenades **tokens**.
    
    - **Exemples de tokens**: Identificadors (noms de variables), paraules reservades, operadors, símbols de puntuació, etc..
![[Pasted image 20260418122101.png]]
![[Pasted image 20260418122111.png]]


- **Anàlisi Sintàctic**: Determina si l'estructura del programa segueix les regles gramaticals del llenguatge. Treballa amb els tokens subministrats per l'analitzador lèxic per simplificar el disseny.
    
- **Anàlisi Semàntic**: Controla la coherència del significat, com ara la correspondència de tipus en assignacions o paràmetres de funcions.



## 4. Disseny d'Analitzadors Lèxics mitjançant Autòmates

**Referència: Diapositives 14-24**

Per construir un analitzador lèxic, definim autòmates que reconeixen cada categoria sintàctica.

- **Identificadors (ex: en C)**: Comencen per lletra o subratllat, seguits de lletres, dígits o subratllats.
    
- **Nombres enters**: Reconeguts mitjançant transicions de dígits, permetent opcionalment signes '+' o '-' al principi.
    
- **Operadors i Comentaris**:
    
    - L'analitzador ha de distingir entre operadors simples (+, -) i compostos (++, +=, --, -=).
	![[Pasted image 20260418122226.png]]
	
    - **Gestió de comentaris**: L'analitzador ha de "saltar" o ignorar els comentaris (com `/* ... */`), ja que no aporten informació a l'anàlisi sintàctic.
        
- **Integració**: Es crea un gran autòmata que aglutina totes les categories. Es transforma en determinista i s'afegeix un estat d'error per a símbols no permesos.
    

## 5. Implementació i Estats Avançats

Quan passem l'autòmata a codi, ens trobem amb un fenomen tècnic important: l'avanç de caràcter.

- **Estats amb un caràcter d'avanç**: Hi ha categories (com identificadors o enters) que només sabem que han acabat quan llegim el següent símbol (un espai, un punt i coma, etc.).
    
- **Regla de programació**: En arribar a un estat d'acceptació d'aquest tipus, **no s'ha de llegir** el següent caràcter de l'entrada en la següent iteració, perquè ja s'ha llegit per poder tancar el token actual.
    
- **Paraules reservades**: Els identificadors es comparen amb una taula de paraules reservades. Si el token hi és, es retorna la paraula específica; si no, es retorna com a "identificador" genèric.
    
