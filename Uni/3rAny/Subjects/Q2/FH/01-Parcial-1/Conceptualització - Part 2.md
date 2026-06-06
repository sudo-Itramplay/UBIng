# 1. Models, Artefactes i Grups d'Usuaris 
Un cop hem dut a terme la recerca d'usuaris (User Research), hem de materialitzar tota aquesta informació. La recerca ens permet crear models que representen la realitat dels usuaris. Aquests models es concreten en "artefactes" tangibles.

- **Finalitat dels artefactes:**
    
    - Serveixen per empatitzar amb l'usuari de manera profunda.
    - Ajuden a definir o redefinir el problema exacte que volem resoldre.
    - Són essencials per comunicar idees dins de l'equip de desenvolupament i amb els _stakeholders_.
    - Permeten generar i orientar noves idees de disseny.
    
- **Aproximacions de creació:** Es poden elaborar basant-nos en dades reals recollides o bé mitjançant assumpcions inicials d'experts que posteriorment haurem de reajustar.

> [!info] Concepte de classificació d'usuaris 
> Per dissenyar correctament, hem de segmentar els nostres usuaris segons la seva relació amb el producte: 
> - **Usuaris primaris:** Utilitzen el producte directament; són el públic objectiu de les funcionalitats principals. 
> - **Usuaris secundaris:** No són el públic principal, però es veuen afectats pel producte d'alguna manera. 
> - **Usuaris extrems:** Són casos límit que amplifiquen certes necessitats (ex: experts en tecnologia o usuaris amb diversitat funcional).
> 


- **Importància dels usuaris extrems:** Tot i la regla de Pareto (on dissenyem sovint per a la majoria), tenir en compte els extrems beneficia a tothom i fomenta la innovació.

- També podem classificar els usuaris per variables demogràfiques, nivell d'expertesa, variables conductuals i necessitats d'accessibilitat.


---

# 2. Personas i Arquetips 

Un dels artefactes més icònics en la conceptualització és la "Persona".

- **Definició de Persona:** És la creació d'un personatge fictici o arquetipus que representa els usuaris reals per donar suport al procés de disseny. Es basa exclusivament en la informació recollida mitjançant entrevistes, qüestionaris, etc..

- **Components:** Cada Persona inclou dades demogràfiques, objectius, motivacions, frustracions i hàbits relacionats amb el projecte.
    
- **Beneficis:**
    
    - Faciliten una comprensió compartida dins l'equip de disseny.
        
    - Donen context a les dades amb històries fàcils de recordar.
        
    - Guien les decisions i ajuden a prioritzar funcionalitats.
        
- **Riscos a evitar (Pregunta típica d'examen):**
    
    - Una sola Persona no pot descriure totes les característiques d'ús.
        
    - Una Persona mai és un usuari real.
        
    - Existeix el risc de centrar el disseny només en la Persona definida, obviant altres casos.
        

> [!tip] Variants del concepte Persona:
> - **Proto-persona:** 
> És una representació provisional creada a partir d'hipòtesis i assumpcions de l'equip, abans de tenir dades empíriques reals. 
> - **Anti-persona:** Representa el perfil d'usuari per al qual expressament NO dissenyem el producte. 
> - **Data-driven Personas (DDP):** Utilitzen Intel·ligència Artificial i grans volums de dades per crear perfils dinàmics i predictius que s'actualitzen en temps real.
> 


---

# 3. Mapes d'Empatia 
Per entendre profundament la "Persona", utilitzem el Mapa d'Empatia (Empathy Map). Es recomana crear un mapa per cada Persona o segment de client.


- **Definició:** És una eina visual dissenyada per representar què pensa, fa, sent, escolta i veu l'usuari en un context específic.
    
- **Estructura clàssica:**
    
    - **SAYS (Diu):** Cites literals i opinions extretes de les dades d'investigació.

    - **THINKS (Pensa):** Conflictes interns, creences i el que realment importa a l'usuari.

    - **DOES (Fa):** Comportament, accions realitzades i com actua l'usuari.

    - **FEELS (Sent):** Emocions de l'usuari, les seves pors i les seves esperances.

- **Vocabulari associat:** L'equip ha de destriar quins són:
	- els **Pains** (frustracions, obstacles, problemes) 
	- els **Gains** (èxits, necessitats satisfetes, objectius a assolir).

- **Utilitat estratègica:** Ajuden l'equip a sintetitzar la recerca i a visualitzar les necessitats abans de definir els requeriments tècnics del producte.


---

# 4. Escenaris d'Ús i User Journey Map 

Quan ja tenim definit _qui_ és l'usuari, necessitem modelar _com_ interactua en el temps. Aquí utilitzem dos artefactes narratius i visuals.

### Escenaris d'ús

- **Concepte:** És una narració (una petita història) que descriu l'usuari interactuant amb el sistema per aconseguir un objectiu concret. Estan protagonitzats per les nostres "Persones".

- **Estructura:** Tenen un fil conductor o _plot_ amb inici, desenvolupament i final. S'hi descriu el context (quan, on, sota quines condicions de llum o estrès), les motivacions de l'usuari i com el producte l'ajuda.

- **Punt clau:** Poden descriure situacions errònies on el sistema falla o confon l'usuari, però la història sempre ha d'acabar bé (amb l'objectiu assolit). S'enfoquen en l'experiència i no pas en els menús o els clics exactes del programari.

### User Journey Map

- **Definició:** És una representació gràfica que mapifica cronològicament l'experiència d'usuari a mesura que utilitza el producte o servei.

- **Components fonamentals:**
    
    - Es divideix en etapes (Stages) que l'usuari travessa.
    
    - Descriu les **Accions** pas a pas.
    
    - Identifica els **Touchpoints**, que són els punts de contacte físics o digitals entre l'usuari i el producte (web, app, botiga física).
    
    - Assenyala els **Pain Points** (frustracions i dificultats detectades en cada pas).
       
    - Grafica la corba d'**Emocions** o experiència al llarg del viatge.
	
    - Mostra **Oportunitats** de millora i innovació per a l'equip de disseny.
	

---

# 5. Investigació d'Usuaris en Productes amb IA i IAG 

El paradigma del disseny canvia completament quan integrem Intel·ligència Artificial (IA). 
	No només estem posant IA a la interfície, hem de validar si l'ús de la IA resol un problema real i aprendre a dissenyar amb un alt grau d'incertesa.

- **Recerca en IA:** 
	- Els productes amb IA fallen estrepitosament quan no responen a necessitats humanes reals. La recerca serveix per identificar moments estratègics on aplicar-la: 
		- moments de càrrega cognitiva alta
		- preses de decisió complexes 
		- processos repetitius.
	També ajuda a avaluar la confiança i expectatives de l'usuari envers la màquina.
   
- **Designerly Understanding:** 
	- Els dissenyadors no necessiten saber programar l'IA, però requereixen una "comprensió de disseny" sobre les seves capacitats, limitacions i riscos per utilitzar-la com a material efectiu i anticipar problemes per a l'usuari.


> [!warning] Norma Infrangible sobre l'ús d'IA Generativa (IAG)
> 
> **La IA Generativa MAI ha de substituir els usuaris reals!**. Encara que l'IA pugui simular "usuaris sintètics", aquests comporten riscos de biaixos, comportaments excessivament previsibles i pateixen d'una manca total d'imprevisibilitat i emocions humanes autèntiques.
> 


- **Com i Quan utilitzar la IAG:**
    
    - **Abans de la recerca:** Utilitzem el _Prompt Engineering_ per planificar entrevistes, generar hipòtesis inicials i estructurar qüestionaris.
	
    - **Després de la recerca:** És extremadament útil per analitzar grans volums de dades, extraient _insights_ o ajudant a agrupar informació temàtica, sempre que anonimitzem dades privades de clients reals.
	
    - **Límits de la IAG:** Cal evitar utilitzar l'IA si manca coneixement de context, si hi ha riscos greus d'al·lucinació de dades o si vulnerem qüestions ètiques.
