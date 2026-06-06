
>[!tip] Concepte extra: co-creació i co-disseny
>
>Dissenyar amb la consultoria d'usuaris externs(que no formmin part de la empresa, com als users que hem entrevsitat)
Bon dia. Com a professor vostre, és un plaer acompanyar-vos en la preparació d'aquesta assignatura. El prototipatge no és només una etapa tècnica, sinó l'essència del disseny iteratiu: "sketchejar" és explorar idees, no només documentar-les.

# 3 Prototipatge: Fonaments i Cicle de Disseny

El prototipatge se situa dins de la fase de **Construcció**, actuant com a pont entre la Conceptualització i l'Avaluació.

- **Definició:** És el procés de crear versions preliminars d'un producte per obtenir feedback ràpid i aprendre.
    
- **Pensament Divergent i Convergent:** El disseny requereix primer **divergir** (crear moltes opcions) i després **convergir** (prendre decisions i seleccionar les millors).
    
- **Ideació vs. Prototipatge:** 
	* La **Ideació** parteix de les necessitats de l'usuari (_User Research_) i preguntes tipus "How Might We" (HMW) per generar el màxim nombre d'idees.
		-  El **HMW** és el final de la etapa de Ideació 
		
		
	- El **Prototipatge** fa tangibles aquestes idees, començant per versions de baixa fidelitat (_lo-fi_) per testejar solucions conceptuals amb els usuaris.
	    - El prototip ha de ser fàcil i ràpid, no ha de tenir vincle emocional perquè laintenció és fer-ne molts de manera ràpida per fer tangibles les idees
	    
    
- **Objectius del feedback:** L'examen podria preguntar què busquem validar. Principalment: si l'usuari entén el model conceptual, si la interfície permet assolir objectius, si el vocabulari és adequat i si es troba el camí per realitzar les tasques (escenaris d'ús).
    
- **Iteració:** La qualitat del disseny augmenta a mesura que experimentem amb més alternatives i iterem basant-nos en el feedback rebut.
    ![[Pasted image 20260319154214.png]]

## Tècnica d'Ideació: Crazy 8s

Aquesta és una tècnica de generació ràpida d'idees molt comuna en entorns de _Design Sprint_.

- **Mètode:** Consisteix a generar **8 idees en 8 minuts** (1 minut per esbós).
    
- **Principis:** Es prioritza la **quantitat sobre la qualitat**. No es tracta de detalls de la UI, sinó de visualitzar solucions ràpides.
    
- **Dinàmica:** Es pot fer individualment o en equip, utilitzant un paper Din-A4 doblegat en vuit parts o _post-its_. Les idees més "boges" sovint serveixen de llavor per a solucions innovadores.

![[Pasted image 20260319154233.png]]


## El Model Conceptual (MC)

El Model Conceptual és una peça teòrica fonamental que descriu de manera abstracta què pot fer l'usuari amb el sistema.

>[!note] Idea general
>La intenció és intentar definir quins són els objectes principals de la nostre aplicació, quins conceptes han i necessitem que apareguin + les operacions que podem  fer amb cada un


- **Anàlisi Objecte/Operació:** És el component essencial del MC. Consisteix a enumerar els objectes visibles, els seus atributs i les operacions que l'usuari pot realitzar (ex: en un calendari, l'objecte és "Esdeveniment", els atributs "data/hora" i les operacions "crear/editar").
    
- **Desenvolupament:** Per crear-lo cal definir objectes segons el _user research_, utilitzar **metàfores** que l'usuari ja entengui i decidir el paradigma (Desktop, Mobile, VR, etc.).
    
- **Metàfores:** Permeten presentar interfícies familiars (ex: la metàfora de la "paperera" o de la "targeta"). Faciliten l'aprenentatge (_easy to learn_), però poden ser restrictives o enganyoses si es "trenquen".
	- SUPER IMPORTANT
>[!tip] La metàfora de la paperera
> És que tu per borrar arxius pots fer click dret borrar, apretar a delete o, i la important, una metàfora on hi ha un icona al exscriptori on tenim una paperera que borra arxius també

   
- **Models Mentals:** Representen el que l'usuari creu que passarà. Es formen per la realitat i nous factors d'influència, creant expectatives i decisions.

![[Pasted image 20260319154202.png]]

>[!tip] Web Util
>https://uxdesign.cc/the-secret-of-good-metaphors-85842f35d973



## Modes i Estils d'Interacció

Defineixen com es produeix la comunicació entre humà i màquina.

>[!info] Modes interacció
>WIMP:
>- Windows
>- Icons
>- nsk
>- Pointers

Quan fem una app de calendari, agafarem de base un calendari fisic, per tant està basat en objectes



 
- **Basats en Activitats:**
    
    1. _Instructing_ (donar ordres).
        
    2. _Conversing_ (diàleg, com en els xats d'IA).
        
    3. _Manipulating_ (arrossegar objectes).
        
    4. _Exploring_ (navegar per l'espai).
	    
    5. Responding 

![[Pasted image 20260319160522.png]]

>[!info] Tipus de activitat
>Del 1 al 4 l'usuari té iniciativa, el 5 és al revés

- **Basats en Objectes:** El sistema s'organitza al voltant d'entitats.
    
- **Estils d'interacció:** Són les instanciacions dels modes (GUI, llenguatge natural, manipulació directa, gestos, BCI, etc.). En l'era de l'IA, apareix el mode _Responding_, on el sistema (ex: Google Lens) pot prendre la iniciativa.


Si Es crea una bona metàsfora, aquesta funciona sense Res fisic o visual, vull dir, no va lligada a la arquitectura
## Fidelitat dels Prototips

La fidelitat indica el grau de proximitat del prototip amb el producte final.

- **Baixa Fidelitat (Lo-fi):** Omet detalls, és ràpid i econòmic. Ideal per a feedback primerenc i prototips conceptuals.
    
- **Alta Fidelitat (Hi-fi):** Producte més acabat, funcional i amb aspecte real.

La dimensió de la fidelitat quantifica d'alguna manera què tant HIFI o LOFI és el prototip
	Què tant espai conceptual deixem per afegir coses  noves
- **Dimensions de la fidelitat:**
    
    - **Amplitud:** Percentatge de funcionalitats cobertes.
	    - Numero de funcionalitats
        
    - **Profunditat:** Grau d'implementació de cada funció. Què tant complet estarà la app
	    - Què tant implementada està cada funcionalitat
	    - Fa servir back end? Tens feta una base de dades? O la estàs simulant? Què agafes i què no del backend?
        
    - **Look & Feel:** Aparença i interacció física.
        
- **Tipus segons dimensió:**
    
    - **Prototip Vertical:** Molt detall en poques funcions.
        
    - **Prototip Horitzontal:** Moltes funcions però amb poc detall (només superfície).
        

>[!warning] Què s'avalua a la pràctica
>Què tant interacitu està el look and feel


## Tècniques de Prototipatge: Storyboarding


Un prototip pot ser des d'un tros de fusta o cartró fins a un programari limitat. 

- **Sketch i Wireframe:** Esbossos fets a mà o amb ordinador.
    
- **Storyboard:** Història visual d'un escenari d'ús (flux d'interacció).
    
- **Elements clau d'un Storyboard:** Scenario (context), Persona (usuari), Títol, Panells (seqüència), Visuals i Captions (text explicatiu).

>[!tip] Els 4 nivells del sketching
>- User journey
>- User Flows
>- Layouts
>- UI Elements
>

- **Consells professionals (_Pro Tips_):**
    
    - Representar l'experiència (pensaments, emocions, motivacions).
        
    - Mantenir-ho simple i deixar fora detalls innecessaris.
        
    - Utilitzar dades de recerca i validar amb participants.
        
    - Ajustar la fidelitat segons l'audiència: començar lo-fi i refinar a hi-fi.
        
    - No excedir els 18 panells; si és més llarg, dividir-ho.
        
![[Pasted image 20260319165130.png]]

![[Pasted image 20260319165144.png]]

