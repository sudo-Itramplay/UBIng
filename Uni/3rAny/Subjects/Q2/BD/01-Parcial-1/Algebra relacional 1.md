# Introducció a l'Àlgebra Relacional

Aquest primer bloc estableix el propòsit teòric i la motivació d'estudiar aquesta eina matemàtica abans de tocar la sintaxi informàtica.

> [!info] Què és l'Àlgebra Relacional? 
> L'àlgebra relacional és un llenguatge teòric compost per operacions que treballen sobre una o diverses relacions per definir una altra relació resultant. 
> 
 
> [!abstract] Perquè ens interessa?
> El seu gran valor és que ens permet manipular conjunts de dades de manera completament fonamentada sense arribar mai a canviar o modificar les relacions base sobre les quals s'apliquen les operacions.

Per entendre bé SQL primer hem d'aconseguir entendre què fa SQL de fons, amb aquesta base teòrica

>[!warning] És necessari saber això per fer us de SQL?
>No necessariament, però ajuda, SQL és la versió amigable d'aquesta àlgebra

- SQL (Structured Query Language) incorpora nativament l'àlgebra relacional en la seva arquitectura.

- **Propietat Fonamental d'Encadenament**: Tota operació de l'àlgebra relacional dóna com a resultat una relació, la qual cosa equival a una taula.
    
	- Aquesta característica estructural obre la porta a que el resultat d'una operació serveixi automàticament com a dada d'entrada per a una altra de nova.


- Per tant, a l'hora d'enfrontar-nos a problemes d'examen complexos, hem de tenir clar que les operacions es poden **encadenar** de manera seqüencial.

>[!tip] Encadenació
>Com a pandas, les operacions son encadenables, i la sortida d'una pot ser l'entrada de l'altre

## **Classificació General**: 
Aquest model teòric es basa principalment en cinc operacions fonamentals.

- Aquestes es divideixen en dos grans grups: 
	- les operacions que operen exclusivament sobre una *sola relació*, que són la **Selecció** i la **Projecció**.
    
	- I les operacions que requereixen treballar amb *dues taules alhora* (operacions binàries), que són el **Producte Cartesià**, la **Unió** i la **Diferència**.

# Operacions Unàries: Selecció i Projecció

Aquestes dues operacions operen de manera independent sobre una sola relació per alterar-ne les files o les columnes resultants. Formen la base de **filtratge** més elemental.

### **L'Operació de Selecció ($\sigma$)**: 
Treballa directament sobre una relació $R$ creant i definint una nova relació que reté exclusivament aquelles files de $R$ que aconsegueixen satisfer la condició d'un predicat. 
	- En essència, selecciona files específiques d'una relació.

>[!quote] Sintaxi:
>- La sintaxi acadèmica que et demanaran utilitzar és $\sigma_{predicate}(R)$.


#### Exemple 

A tall d'exemple d'examen, per recuperar pel·lícules amb una durada superior als 150 minuts s'empraria el predicat pertinent sobre la relació `MOVIES`: $\sigma_{length>150}(MOVIES)$.

>[!tip] Predicats compostos 
>- L'operació permet crear predicats compostos utilitzant connectors estructurals com ara AND o bé OR (també escrits amb la notació matemàtica V per a OR).

   
### **L'Operació de Projecció ($\pi$)**: 

Actua sobre una relació $R$ per proporcionar-nos una relació que conté exclusivament un subconjunt vertical de l'estructura original de $R$. Serveix per seleccionar columnes o atributs específics d'una relació.

 >[!info] És a dir
 >Extreu només els valors dels atributs o columnes que s'hagin especificat explícitament en els paràmetres de l'operació, eliminant qualsevol duplicat resultant en la vista final.

>[!quote] Sintaxi matemàtica
>- Es formula matemàticament amb la notació $\pi_{c_{1},c_{2},...,c_{n}}(R)$.
   

> [!warning] Composició i Ordre d'Aplicació (Molt Important!) 
> En els exercicis on se'ns demana combinar múltiples filtres i mostrar certs atributs, necessitarem utilitzar ambdues tècniques: selecció i projecció. 
> - La regla d'or aquí és que l'ordre importa radicalment. 
> 	1. S'aplica sempre primer la **Selecció** sobre la relació base, generant una relació intermèdia
> 	2. sobre la qual posteriorment s'executarà la **Projecció**.
> 
> Un exemple clar d'això seria demanar projectar només el nom i el cognom després d'haver filtrat per salari: $\pi_{fname,lname}(\sigma_{salary\ge10000}(STAFF))$.

![[Pasted image 20260310160909.png]]

![[Pasted image 20260310160851.png]]



#### Altre Exemple

![[Pasted image 20260310161506.png]]

![[Pasted image 20260310161446.png]]


# Operacions Binàries de Conjunts: Unió i Diferència


> [!info] Requisit Previ: Taules Compatibles 
> L'estàndard acadèmic exigeix que tant per fer una Unió com per fer una Diferència, les relacions $R$ i $S$ han de ser estrictament compatibles. 
> - Es considera que dos esquemes són compatibles quan el seu nombre d'atributs és exactament el mateix
> - el domini o tipus de dades d'aquests atributs coincideix. 
> 
> Recorda que aquestes relacions poden ser fruit directe d'altres operacions algebraiques anteriors.


## **La Unió de Conjunts ($\cup$)**: 
L'operació d'unió entre les relacions $R$ i $S$ s'encarrega de definir una relació integral que alberga les files pertanyents a $R$, o aquelles pertanyents a $S$, o fins i tot aquelles presents de forma simultània en ambdues taules. 
	- Així, afegeix o suma relacions compatibles, eliminant immediatament les files duplicades.

>[!quote] Sintaxi
>- El seu símbol d'operació i notació lògica és $R\cup S$.

>[!tip] Enunciat lògic
>Dins d'un enunciat lògic, el terme o connector "o" (per exemple: buscar oficines en lloguer A "o" B) és l'indicatiu lingüístic fonamental que requereix emprar la unió.


#### Exemple
![[Pasted image 20260310161622.png]]
![[Pasted image 20260310161638.png]]

![[Pasted image 20260310161654.png]]


# **La Diferència de Conjunts ($-$)**: 

L'operació de diferència executada entre les relacions $R$ i $S$ dóna lloc a una relació que només conté aquelles files que es troben a $R$, però que es caracteritzen per estar absents de $S$. 
- Resta així les files comunes compartides per dues relacions.

>[!quote] Sintaxi
>- La seva formulació visual i estructural és $R-S$.
    
- És de vital importància tenir present que $R-S$ no produirà en cap cas el mateix resultat que l'operació matemàtica inversa $S-R$.

>[!tip] Enunciat lògic
>- L'anàlisi lingüística per a un examen indica l'ús d'aquesta operació en casos com: ciutats presents a A, però que no estan a B 
> 
>(fet que determina la Diferència envers la Unió).


#### Exemple
![[Pasted image 20260310161744.png]]
![[Pasted image 20260310161759.png]]


![[Pasted image 20260310161808.png]]

# El Producte Cartesià i Conceptes Complementaris

Per finalitzar el repàs d'aquesta primera part d'àlgebra, abordem l'operació binària encarregada de crear conjunts globals combinant múltiples esquemes estructurals.

## **El Producte Cartesià ($\times$)**: 

Aquesta operació teòrica defineix i estableix una relació generada mitjançant la concatenació total de les files de la relació $R$ juntament amb totes les files corresponents de la relació $S$.

>[!tip] És a dir
>Aquesta operació junta les dues taules en una

![[Pasted image 20260310162156.png]]

- El conjunt o relació final conté de manera exhaustiva tots els parells possibles que es poden conformar creuant $(R, S)$. És l'operació emprada per combinar relacions compatibles directament.

- Des d'una perspectiva d'estructura de dades, l'esquema d'aquesta relació acabada de crear representa la unió absoluta dels esquemes inicials de $R$ i de $S$.

>[!quote] Sintaxi
>- La sintaxi per representar aquesta relació estructural és $R\times S$.
    

![[Pasted image 20260310162223.png]]

### ? Investigar
- Com a tècnica clau en disseny i resolució, quan sorgeixen conflictes perquè ens trobem amb atributs que posseeixen noms completament idèntics en ambdues taules, la norma és clarificar l'origen de la dada utilitzant el prefix complet de la taula: `RELATION_NAME.attribute` 
	- (per exemple: `CLIENT.client_id=VIEWING.client_id`).