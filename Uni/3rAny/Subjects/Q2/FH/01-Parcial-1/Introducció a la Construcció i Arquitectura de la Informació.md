Aquí suposem que hem fet la part de conceptualització, i sabem què volem resoldre i com.

# 1. Introducció a la Construcció i l'AI

L'etapa de **Construcció** és el pont entre la conceptualització i el producte final. Partim de resultats reals per resoldre problemes reals. Dins d'aquesta, l'**Arquitectura de la Informació (AI)** es defineix com la disciplina que fa que la informació sigui fàcil de trobar i entendre.

>[!tip] AI
>Serveix per organitzar (estructurar, etiquetar) bé la informació per ser ràpidament trobada


- **L'Ecosistema de l'AI:** No es tracta només de contingut; l'AI neix de la intersecció dinàmica de tres àrees:
    
    - **Usuaris:** Qui són, què necessiten i com busquen la informació.
        
    - **Contingut:** Tipus de dades, volum i estructures existents.
        
    - **Context:** Objectius de negoci, cultura organitzativa, tecnologia i recursos.

![[Pasted image 20260312151729.png]]
- Tot i ser els dos robots, i resoldre coses semblants, estàn ideats ddiferents i amb conceptes diferents, el primer reemplaça, el segon es va fer ràpid per ajudar

>[!warning] **Objectiu fonamental:** 
>L'arquitecte de la informació ha d'ajudar l'usuari a respondre preguntes crítiques com: 
>- "On sóc?"
>- "Què puc trobar aquí?" 
>- "On puc anar des d'aquí?".
>
>És a dir, són els responsables de fer una webintuitiva




![[Pasted image 20260312152033.png]]


#### Flux de la informació (amb inputs i outputs)

1. 
![[Pasted image 20260312152140.png]]

2. 
![[Pasted image 20260312152158.png]]

3. 
![[Pasted image 20260312152327.png]]


# 2. Necessitats i Comportaments de l'Usuari

Com a enginyers, hem de modelar com els usuaris interactuen amb el sistema per optimitzar la recuperació de dades.

>[!info] Definició: AI
>L'arquitectura de la informació (AI) és una disciplina de
disseny centrada en fer que la informació sigui fàcil de **trobar**
i **entendre**.

>[!quote] els 4 grans components
> 1. Sistemes d'organització
> 2. Sistemes d'etiquetatge
> 3. Sistemes de navegació
> 4. Sistemes de cerca


![[Pasted image 20260312152906.png]]

- Ens volem centrar en què mostrar, amb una estratègia comú, per poder-se traslladar a les diferents coses ( Android, TV, Mòbil )

>[!warning] Molt Important
>AI no nomes és contingut, són 3 coses dependents entre si de manera ***dinàmica***
>
>![[Pasted image 20260312153050.png]]

El context d'abaix és la cultura de la empresa, el context del user està dins de propi user, A context definim les politiques les la empresa

>[!tip] Concepte important
>Són àmbits dinàmics:
>- el contingut i esl usuaris poden canviar en qualitat, demogràfia, tendències,.... VAN CANVIANT

>[!quote] Exemple
>![[Pasted image 20260312153913.png]]




### **Necessitats d'informació comunes:**
![[Pasted image 20260312154042.png]]

- **The right thing:** Cerca d'un element conegut.
	
- **A few good things:** Cerca exploratòria.
	
- **Everything:** Recerca exhaustiva.
	
- **Need it again:** Recuperació d'informació ja vista (refinding).

>[!tip] Exemple del Pescador
> - **Pesca amb canya — _The right thing_ (conegut):** L'usuari sap exactament què busca i on trobar-ho; llança l'ham per treure una peça específica.
    >
>- **Pesca d'arrossegament — _Everything_ (exhaustiva):** L'usuari necessita recollir absolutament tota la informació disponible sobre un tema per no deixar-se cap dada rellevant.
    >
>- **Tornar a pescar al mateix calador — _Need it again_ (refinding):** L'usuari intenta recuperar una informació que ja havia trobat anteriorment i que necessita consultar de nou.
  >  
>- **Pesca amb trampes o nanses — _A few good things_ (exploratòria):** L'usuari no necessita tot el contingut, sinó només uns quants exemplars de qualitat que li serveixin per satisfer la seva curiositat inicial o resoldre un dubte general.

![[Pasted image 20260312155400.png]]

és el needit again

- Pq pot ser que l'user trobi algo i ho vulgui guardar per tornar-ho a trobar
### Models de comportament (cerca)

- **Berry-picking:** Un procés iteratiu on l'usuari va recollint "baies" (fragments d'informació) i modificant la seva consulta a mesura que aprèn del sistema.
	
- **Pearl-growing:** L'usuari parteix d'un document rellevant i busca elements similars per expandir la seva cerca. Busca coses similars

>[!tip] Pearl-growing - Google Scholar
>Va bé buscar informació, sobretot per TFG



![[Pasted image 20260312154520.png]]
![[Pasted image 20260312154622.png]]
- El "citat per" és la *perla* que diem

Si volguéssim saber més del comportament:
![[Pasted image 20260312154921.png]]

Aquí tenim fonts d'informació, o mètodes, per saber què fa la gent
-  El user research sonn les tècniques que ja hem fet


![[Pasted image 20260312163056.png]]

- No he escoltat
![[Pasted image 20260312163115.png]]
- Exacte

# 3. Components de l'AI: Organització i Etiquetatge

Aquests són els sistemes que donen estructura al "caos".
![[Pasted image 20260312155602.png]]

- Hem de pensar en aquests 4 sistemes

### **Sistemes d'Organització:** 
Abans d'organitzar res, hem de saber què organitzar. Hem d'intentar llistar d'alguna manera els continguts.


>[!warning] Primer pas
>Abans d'organitzar, cal fer un **inventari de contingut** (llistat de pàgines, recursos o pantalles).

![[Pasted image 20260312155841.png]]
- Pensa que és un exemple incomplet, falta dir què hi ha a cada part
	- En una web l'inventari és:
	![[Pasted image 20260312160114.png]]
	

- **Esquemes Exactes:** Criteris objectius:
	- com l'ordre alfabètic
	- cronològic 
	- geogràfic.
	
- **Esquemes Ambigus:** Criteris subjectius però molt útils
	- per temes
	- per tasca
	- per audiència o per metàfora.
        
### **Sistemes d'Etiquetatge (Labelling):** 
Serveixen per representar conjunts d'informació de forma eficient.

>[!example] Exemple
>L'etiqueta "Contact us" -> nom de contacte, direcció, tel., correu



- Poden ser **textuals** (enllaços, capçaleres) o **icònics**.
	▪ Textuals (links, headings, opcions de navegació, tags,...)
	▪ Icons (menu, cerca, carret compra, ....)

- **Consell d'examen:** Les etiquetes han de ser coherents i representatives per evitar l'ambigüitat.

#### Testing
- **Card Sorting:** Tècnica clau per testejar l'etiquetatge, on els usuaris agrupen etiquetes en categories 
	- Exemple
		- obert: Li dono totes les etiquetes i que ell faci
		- tancat: Dono categories al user i que ells coloquin 
		- híbrid: Li deixo opcio a, que si hi ha un grup no creat, que el crei
        

- Anàlisi de competència
- analítica de cerques
- Thesaurus: Quan tenim una etiqueta que no estem convençuts
### Sistemes de Navegació

La navegació permet el moviment per la interfície. Es divideix en tres grans blocs:

- **Principals:**
    
    - **Global:** Present a tot el lloc (ex: menú superior, "fat footers").
	    - Mega menú, per webs bastant amplies, en una secció apareixen subseccions
	    - ![[Pasted image 20260312164317.png]]
	    - El tipic index d'abaix de tot amb informació variada (Sol estar el side map i info de la empresa)
	    - ![[Pasted image 20260312164407.png]]
        
    - **Local:** Permet explorar àrees específiques ("Què hi ha a prop?").
	    - Un submenú sempre visible
	    - ![[Pasted image 20260312164424.png]]
	    - 
        
    - **Contextual:** Enllaços "vegeu també" o productes relacionats.
	    - Quin tipus de navegació és? Contextual (la imatge seguent)
	    - ![[Pasted image 20260312164459.png]]
    
	![[Pasted image 20260312164055.png]]
- **Complementaris:** Sitemaps, índexs i assistents (wizards).
	- Ja no es fa servir tant, són sistemes que t'ajuden en la cerca i/o et donen info adicioal
	- Aqui destaca la cerca
	- ![[Pasted image 20260312164531.png]]
	- Ens ajuden a configurar coses, ens seccionen un msteix pas
	
    
- **Avançats:** Personalització mitjançant IA i visualitzacions complexes.
    
- **Avaluació:** Utilitzem el **Tree Test** per validar la jerarquia i el **Stress Test** per verificar si l'usuari se sap ubicar en una pàgina interna aleatòria.
![[Pasted image 20260312164611.png]]


### Sistemes de Cerca

**Referència: Diapositives 60-80**

Un sistema de cerca no és només una caixa de text; és un motor complex.

- **Anatomia:** Inclou la interfície (com es presenta), el motor (algorismes i tecnologia) i el contingut (què s'indexa).
    
- **Mètriques de qualitat:**
    
    - **Precision:** Quants dels resultats recuperats són realment rellevants.
        
    - **Recall:** Quina part dels documents rellevants totals del sistema hem estat capaços de trobar.
        
- **Disseny de la interfície:** Cal decidir com llistar els resultats (alfabèticament per a accions clares, o per rànquing/rellevància per a l'aprenentatge) i oferir filtres per donar control a l'usuari.
    
- **Suport a la revisió:** Implementar autocompletat (per a tasques simples) o autosuggestió (per a cerques exploratòries).
    

# Transició al Prototipat

**Referència: Diapositives 85-88**

L'AI és un procés viu i iteratiu. Un cop definit l'inventari, l'organització, l'etiquetatge, la navegació i la cerca, es genera el **Sitemap**. Aquest document guiarà la següent fase: el **Prototipat Conceptual (Lo-fi)** o Wireframes, on començarem a visualitzar el model conceptual sense detalls visuals.

Estudia amb confiança; l'arquitectura ben feta és la que fa que l'usuari no hagi de pensar massa. Molts ànims!

