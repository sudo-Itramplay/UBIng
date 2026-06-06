> [!abstract] Resum complet del 1r Parcial · vegeu les notes atòmiques al [[_MOC|MOC de FH]]
> **Fonaments:** [[HCI]] · [[Disseny Centrat en l'Usuari]] · [[Design Thinking]] · [[Model d'Interacció]] · [[Usabilitat]] · [[UX]] · [[UI vs UX]]
> **Conceptualització:** [[User Research]] · [[Entrevistes]] · [[Qüestionaris]] · [[Biaixos Cognitius]] · [[Persona]] · [[Mapa d'Empatia]] · [[User Journey Map]]
> **Construcció:** [[Arquitectura de la Informació]] · [[Sistemes d'Organització]] · [[Sistemes de Navegació]] · [[Sitemap]]
> **Prototipatge:** [[Prototipatge]] · [[Ideació]] · [[Model Conceptual]] · [[Fidelitat dels Prototips]] · [[Storyboarding]]
> **Gamificació:** [[Gamificació]] · [[Gamification Model Canvas]] · [[Tipus de Jugador]]

# Tema 1
## Interacció Persona-Ordinador (HCI)

- L'HCI (Human Computer Interaction) és un camp interdisciplinari que se centra exclusivament en el disseny de sistemes interactius per a l'ús humà. 
	- La premissa fonamental és que l'única via per a un bon disseny és començar per les persones.

- Es defineix com un sistema sòcio-tecnològic on una persona (o grup de persones) interactua amb un ordinador per intentar aconseguir un objectiu concret.

### Components

#### H
**El component "Human":**
A l'hora d'avaluar l'usuari, hem de considerar factors crítics com:
- l'atenció, la confiança, la memòria, la diversitat, el context d'ús i el comportament d'aprenentatge. 
A més, hem de tenir en compte l'ètica, la privacitat, els biaixos i evitar danys no intencionats.

>[!tip] Ojo
>No dissenyem només per a qui fa el clic. Hi ha altres actors clau: 
>- els _stakeholders_ o parts interessades (com el CEO, màrqueting o enginyeria, cadascú amb les seves preocupacions de mercat o implementació) 
>- els _bystanders_ o persones afectades indirectament pel sistema.

9i0
#### C
- **El component "Computer":** És la màquina qui executa els programes, respon i ens estableix els límits tècnics; sovint potenciat per sistemes d'Intel·ligència Artificial.

#### I
- **La Interacció:** És el cicle on la persona expressa les seves intencions al computador i aquest hi respon. 

>[!info] Tipus de sistemes
>El sistema pot ser:
>-  reactiu (reacciona a l'acció de l'usuari) 
>- proactiu (sistemes amb IA que s'avancen a les demandes, com els recomanadors).


---

#### Disseny Centrat en l'Usuari (UCD) i Metodologies

- El Disseny Centrat en l'Usuari (UCD) és un enfocament fonamentalment iteratiu que posa a l'usuari en el centre absolut de tot el procés.

Aquest enfocament exigeix entendre les necessitats, desitjos, capacitats, limitacions, context dels usuaris per crear productes que siguin realment útils i rellevants per a ells. 

- Es divideix en tres grans fases macro: 
	- Conceptualització
	- Construcció 
	- Avaluació.

- Existeixen diverses metodologies alineades amb el UCD, establint etapes i tècniques clares. 

>[!info] Les més destacades són:
> - el _Design Thinking_, el _Double Diamond_, l'_Agile UX_ i el _Lean UX_.
>  
>  També s'empren conjunts d'eines com el _Design Toolkit_ de la UOC o el de Google.
   
- El model **Double Diamond** del Design Council UK consta de quatre fases dividides en dos diamants (un per al problema i un per a la solució): _Discover_ i _Define_ (on s'aplica el pensament divergent per crear opcions i convergent per prendre decisions), i _Develop_ i _Deliver_.

- La metodologia estrella és el **Design Thinking** (DT), que es divideix en 5 etapes iteratives per fomentar l'empatia, la creativitat i la innovació:

    - 1. Empatia (Conceptualització): L'objectiu és entendre l'usuari i el seu context de manera local i global. S'investiga la realitat, els problemes i les tendències de la competència per obtenir inspiració.
	
    - 2. Definició (Conceptualització): Analitzem la informació prèvia per identificar àrees d'oportunitat clares on fonamentar les solucions. La clau d'aquesta etapa, com indiques als teus apunts, és formular les preguntes "How Might We" (HMW).
	
    - 3. Ideació (Construcció): Es busca generar el major nombre possible d'idees per solucionar els problemes, posant en dubte el _status quo_ i seleccionant les opcions més rellevants.
	
    - 4. Prototipat (Construcció): Fem tangibles les idees generades perquè evolucionin en equip. Es parteix de prototips bàsics que es van millorant successivament basant-nos en els valors dels usuaris.
	
    - 5. Testeig (Avaluació): S'avaluen i es refinen les solucions demanant als usuaris que provin els prototips. Això assegura que aportem el valor detectat a la fase de Definició i minimitza el risc de fracàs del projecte.


---

## Model Teòric d'Interacció i el Factor Humà

- A nivell cognitiu, la interacció no es redueix a l'acte mecànic de "fer clic". És un cicle continu de pensament, acció i interpretació que transcorre entre l'usuari i el sistema.

- Per entendre què passa realment durant la interacció, s'utilitza un model teòric que divideix el procés en dos grans "golfs" o bretxes entre el que vol la persona i l'estat del món físic o digital.

- **Bridge of Execution:** Representa el salt des de l'usuari cap al sistema.
	
    - _Goal:_ L'usuari estableix un objectiu (p. ex., tinc calor a l'aula).
        
    - _Plan:_ Formula un pla per assolir-lo (pensar en encendre l'aire).
        
    - _Specify:_ Especifica l'acció concreta necessària.
        
    - _Perform:_ Executa físicament l'acció (demanar-ho o prémer el botó).
        
- **Bridge of Evaluation:** Representa el salt des del sistema de tornada cap a l'usuari.
	
    - _World:_ El món realitza un canvi d'estat.
        
    - _Perceive:_ L'usuari percep de manera sensorial el que ha passat.
        
    - _Interpret:_ L'usuari processa i interpreta aquesta informació.
        
    - _Compare:_ Finalment, compara el nou estat amb l'objectiu inicial per saber si s'ha complert.
        
- **El Factor Humà:** Tota aquesta teoria es fonamenta en entendre el factor humà, que engloba les capacitats, característiques i limitacions que influeixen en l'ús d'un sistema.

- Dissenyar tenint present aquest factor és el que garanteix que els sistemes acabin sent eficients, inclusius, confiables i agradables. S'hi arriba a través del UCD i analitzant el processament cognitiu, la percepció i el sistema motor humà.


---

#### Usabilitat vs. Experiència d'Usuari (UX)

- En disseny de productes, treballem amb una equació bàsica: La utilitat pràctica (Usefulness) és la suma de la Utilitat funcional (Utility) i la Usabilitat (Usability).
    
- La **Usabilitat** es refereix exclusivament a la facilitat amb la qual els usuaris poden interactuar amb un sistema i aconseguir els seus objectius de manera satisfactòria.

- Un sistema usable ha de complir certs criteris: 
	- ha de ser fàcil d'aprendre
	- eficaç
	- eficient
	- provocar pocs errors
	- permetre recuperar-se fàcilment si n'hi ha
	- fàcil de recordar.

- Com a enginyers, ens enfrontem constantment a compromisos de disseny o **"Trade-offs"**. Aquests compromisos es resolen analitzant qui és el nostre usuari i com és la tasca.
    
    - Si el perfil d'usuari és _expert_, l'element més important a potenciar és l'**eficiència** del sistema.

    - Si l'usuari és _novell_, el disseny ha de primar que sigui **fàcil d'aprendre**.

    - Si ens trobem davant un usuari _desmotivat_, la prioritat és aconseguir una interacció **satisfactòria** per retenir-lo.

    - Si la tasca en si és molt _complexa_, és fonamental assegurar un bon **control d'errors** i que el procés sigui fàcil d'aprendre.

- La **User Experience (UX)** és un concepte molt més ampli i holístic. Si bé un producte ha de ser usable, la UX busca crear experiències que també siguin memorables, emocionals i significatives per a l'usuari.

- Segons el diagrama del rusc (Honeycomb) de Peter Morville, l'experiència d'usuari perfecta assoleix un equilibri on el sistema és: 
	- Accessible
	- Desitjable (Desirable), 
	- Fàcil de trobar (Findable), 
	- Creïble, 
	- Útil (Useful), 
	- Usable 
	En definitiva, Valuós. 

Com anotes encertadament, la interfície (UI) és merament l'eina visual (la capa final) a través de la qual s'executa aquesta interacció profundament analitzada.


# Tema 2

## 1. Introducció a la Conceptualització i l'Empatia

L'etapa de conceptualització d'un disseny serveix per conèixer els nostres usuaris en profunditat
	només així podrem definir correctament el problema a resoldre basant-nos en allò que hem après d'ells. 

Per assolir-ho, és imprescindible empatitzar amb l'usuari i comprendre el seu context, tant físic com social i cultural.

>[!info] Concepte important
>* "Nosaltres no som els usuaris". Dissenyem per satisfer les necessitats d'usuaris reals.


* **Objectiu del disseny**: 
	Volem aconseguir experiències atractives, personalitzades i que s'adaptin completament a les seves necessitats, capacitats i desitjos.


* **Informació a recollir**: 
	Necessitem dades demogràfiques (edat, sexe, cultura), formatives i tècniques (nivell d'educació, experiència amb ordinadors i en el domini de l'aplicació). També hem d'indagar en el seu context d'ús, motivacions i limitacions físiques.
![[Pasted image 20260226154827.png]]

#### Important:
1. la diferència entre un *Perfil d'Usuari* i una *Persona* 
Mentre que un perfil prové de dades directes d'un usuari entrevistat, una *Persona* en UX/UI és un arquetip imaginari creat aglomerant atributs detectats en la investigació. 

2. Desig vs Motivació
També cal distingir el *Desig* (com la gent decideix fer una cosa) de la *Motivació* (els elements que impulsen l'acció).

* Tot això s'aconsegueix aplicant tècniques de *user research* (investigació d'usuaris), el propòsit de les quals és recollir dades per validar hipòtesis i crear models o artefactes útils per al disseny.



---

## 2. Tècniques de Recerca: Entrevistes i Qüestionaris

Sempre hem de partir d'una hipòtesi inicial sobre qui són els nostres usuaris (incloent dades demogràfiques i comportamentals), que posteriorment refinarem amb la investigació. 

Per validar aquestes hipòtesis, les eines més directes són les entrevistes i els qüestionaris:

>[!tip] Concepte Important: **Triangulació**
> Com a mètode fonamental, recorda que els usuaris pateixen errors d'autoinforme (*self-reporting errors*); és a dir, no sempre diuen el que realment pensen o no recorden bé com actuen. 
> - Per això mai confiem en una sola tècnica i fem servir la triangulació.


#### Entrevistes
*  Són tècniques qualitatives d'interacció directa. Requereixen una planificació rigorosa: 
	* definir l'objectiu
	* reclutar
	* preparar guions
	* gestionar el consentiment. 

Existeixen tres modalitats:

* *Estructurades*: Utilitzen un guió fix amb preguntes tancades; es pregunten exactament en el mateix ordre a tothom.

* *No estructurades*: Són converses fluïdes amb preguntes obertes per explorar tòpics lliurement, tot i que l'entrevistador sol tenir un rumb en ment.

* *Semi-estructurades*: Són l'híbrid perfecte. Comencen amb un guió fix i preguntes preparades per garantir consistència, però s'obren posteriorment per indagar en respostes interessants.



##### Bones Pràctiques
* Ambient còmode
* escolta activament
* dóna temps per pensar 

>[!warning] Important
>Evita fer preguntes que indueixin la resposta o demanin prediccions del futur.


#### **Qüestionaris**: 
Aporten volum quantitatiu i assoleixen més públic. 
Estructura'ls lògicament (començant per dades bàsiques abans de les específiques) i cuida el format de resposta (likert, checkboxes). 

Ves amb molt de compte amb els biaixos cognitius, com :
(al glossari al final)
- el [[#**Confirmation Bias (Biaix de confirmació) **]] 
- l'[[#**Anchoring Bias (Biaix d'ancoratge) **]]

>[!tip] Recorda 
>Alternar el format de les preguntes per evitar la fatiga de l'usuari.


---

## 3. Investigació Contextual i Observació Indirecta

Quan necessitem anar més enllà del que l'usuari declara verbalment i veure'l actuar de debò, entren en joc la investigació contextual i l'observació indirecta.

#### **Investigació Contextual**: 
Aquesta tècnica busca l'enteniment profund situant l'investigador directament en el context natural ("el món") on l'usuari treballa.

* *Relació Master-Apprentice*:
	* Aquesta és una dinàmica d'examen clau.
	* L'usuari actua com el mestre que executa la tasca i sap com funciona tot, mentre que l'investigador pren el rol de l'aprenent que observa, coopera i demana aclariments.


* *Principis bàsics*: 
	* S'ha d'avaluar sempre el Context, cercar la Cooperació, fer una Interpretació conjunta d'allò observat i mantenir una Focalització cap als objectius de l'estudi.


* *Thinking Aloud*: 
	* Durant l'observació de les tasques (siguin habituals o predefinides), es demana a l'usuari que pensi en veu alta per entendre el seu procés mental. 
	* Tot i els grans "insights", l'observació directa té riscos: consum d'altos recursos i la possible alteració del comportament de l'usuari pel fet de ser observat.



#### **Observació Indirecta**: 
Consisteix a recollir dades qualitatives de forma sostinguda i passiva.

* *Diaris (Cultural probes)*: 
	* L'usuari ha de registrar (escriure, fer fotos) la seva activitat, dificultats i tasques durant un període (setmanes o mesos). 
	* Requereix una forta disciplina de l'usuari.


* *Interaction logging*: 
	* Usant el software, els patrons d'ús es capturen automàticament; això elimina l'error de record de l'usuari i pot allargar-se substancialment en el temps.

---

## 4. Focus Groups i Benchmarking

Per tancar el ventall de tècniques de descobriment de necessitats qualitatives, recorrem a l'estudi de dinàmiques grupals i a l'observació de l'entorn competitiu del mercat.

### **Focus Groups**: 
Consisteixen en reunions informals i guiades amb grups d'entre 5 i 10 usuaris.


* *Estructura i objectiu*:
	* Un moderador segueix un guió de temes mentre una altra persona s'encarrega exclusivament de prendre notes o gravar.
	* L'objectiu és observar idees i reaccions espontànies, així com la dinàmica de discussió del grup.


* *Avís metodològic*: 
	* Com en les entrevistes, aquí només analitzem "el que els usuaris diuen que fan"; per això, el Focus Group poques vegades hauria de ser la teva única tècnica.


### **Benchmarking**: 
És l'estudi rigorós de la competència directa o indirecta. Ajudarà a identificar bones pràctiques, àrees defectuoses a la indústria i oportunitats d'avantatge competitiu.


* *El procés*: 
	* Escull quins productes vols analitzar, defineix clarament els criteris comparatius, fes una auditoria per producte i resumeix-ho finalment en una Taula d'anàlisi general comparativa.


* *Criteris d'anàlisi comuns*: 
	* Alguns dels paràmetres més recurrents inclouen la usabilitat general, l'eficiència dels fluxos (ex: passos per a fer un pagament), el disseny visual i estètic, l'arquitectura de la informació i l'accessibilitat conforme als estàndards WCAG. 
	* Aquests seran els teus referents per evitar cometre els errors de la competència.

---

## 5. Selecció de Tècniques i Síntesi de Dades

Saber quanta informació has de recollir i com processar-la un cop finalitzat el *user research* és la frontera on el dissenyador novell es separa del professional.

### **Com escollir la tècnica més adequada**: 
Mai hi ha una fórmula màgica única. 
Has d'avaluar:
- els objectius del teu estudi específic (explorar en general o contrastar detalls)
- les condicions dels teus participants (com el seu grau de motivació i temps disponible) 
- els recursos del projecte (pressupost i temps). 

Normalment s'ha d'optar per diverses simultàniament.


## **Anàlisi de les dades (Fase de Definició)**:
El procés arrenca quan cada membre de l'equip fa una revisió individual de tot el material compilat (qüestionaris, vídeos, transcripcions).

### *Tècniques de síntesi*: 
L'equip es reuneix per aplicar tècniques col·laboratives. 

#### **Clustering** o *Diagrama d'afinitat*
Consisteix a agrupar per categories temàtiques o problemes tota la informació rellevant trobada (sovint usant post-its de colors). 
	 Nomes s'usa per grupar temes, no relacions


#### *Mapa Mental*
Tècnica lleugerament més estructurada per generar relacions entre els diferents grups temàtics.

Semblant a abans però relacionant els postits

#### *Generació de solucions*: 
D'aquesta fase analítica en sortiran els patrons de frustracions i desitjos. 

Mitjançant les conegudes preguntes d'ideació tipus 
*"How might we..."* ("Com podríem nosaltres...")

es marca el tret de sortida per deixar de banda la conceptualització del problema i endinsar-nos en la cerca formal de solucions.


# Tema 3
## 1. Models, Artefactes i Grups d'Usuaris 
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

## 2. Personas i Arquetips 

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

## 3. Mapes d'Empatia 
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

## 4. Escenaris d'Ús i User Journey Map 

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

## 5. Investigació d'Usuaris en Productes amb IA i IAG 

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


# Tema 4
Aquí suposem que hem fet la part de conceptualització, i sabem què volem resoldre i com.

## 1. Introducció a la Construcció i l'AI

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


## 2. Necessitats i Comportaments de l'Usuari

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

## 3. Components de l'AI: Organització i Etiquetatge

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


Un sistema de cerca no és només una caixa de text; és un motor complex.

- **Anatomia:** Inclou la interfície (com es presenta), el motor (algorismes i tecnologia) i el contingut (què s'indexa).
    
- **Mètriques de qualitat:**
    
    - **Precision:** Quants dels resultats recuperats són realment rellevants.
        
    - **Recall:** Quina part dels documents rellevants totals del sistema hem estat capaços de trobar.
        
- **Disseny de la interfície:** Cal decidir com llistar els resultats (alfabèticament per a accions clares, o per rànquing/rellevància per a l'aprenentatge) i oferir filtres per donar control a l'usuari.
    
- **Suport a la revisió:** Implementar autocompletat (per a tasques simples) o autosuggestió (per a cerques exploratòries).
    

# Transició al Prototipat


L'AI és un procés viu i iteratiu. Un cop definit l'inventari, l'organització, l'etiquetatge, la navegació i la cerca, es genera el **Sitemap**. Aquest document guiarà la següent fase: el **Prototipat Conceptual (Lo-fi)** o Wireframes, on començarem a visualitzar el model conceptual sense detalls visuals.

Estudia amb confiança; l'arquitectura ben feta és la que fa que l'usuari no hagi de pensar massa. Molts ànims!


# Tema 5

>[!tip] Concepte extra: co-creació i co-disseny
>
>Dissenyar amb la consultoria d'usuaris externs(que no formmin part de la empresa, com als users que hem entrevsitat)
Bon dia. Com a professor vostre, és un plaer acompanyar-vos en la preparació d'aquesta assignatura. El prototipatge no és només una etapa tècnica, sinó l'essència del disseny iteratiu: "sketchejar" és explorar idees, no només documentar-les.

## 3 Prototipatge: Fonaments i Cicle de Disseny

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

### Tècnica d'Ideació: Crazy 8s

Aquesta és una tècnica de generació ràpida d'idees molt comuna en entorns de _Design Sprint_.

- **Mètode:** Consisteix a generar **8 idees en 8 minuts** (1 minut per esbós).
    
- **Principis:** Es prioritza la **quantitat sobre la qualitat**. No es tracta de detalls de la UI, sinó de visualitzar solucions ràpides.
    
- **Dinàmica:** Es pot fer individualment o en equip, utilitzant un paper Din-A4 doblegat en vuit parts o _post-its_. Les idees més "boges" sovint serveixen de llavor per a solucions innovadores.

![[Pasted image 20260319154233.png]]


### El Model Conceptual (MC)

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




# Tema 6
## 1. Introducció a la Gamificació

>[!info] Intenció
>L'essència de gamificar o ludificar consisteix a utilitzar mecàniques de joc en contextos que no són de joc.

   
- Com a definició acadèmica de referència:
>[!info] Definició: Gamificació
>Zichermann estableix que és l'ús de la psicologia del comportament i les mecàniques de joc per influir en els comportaments desitjats o millorar les experiències dels usuaris.

  
- Com que és un procés de disseny, requereix necessàriament l'ús de metodologies i eines de suport.
	- Un sistema gamificat d'èxit ha de combinar obligatòriament la motivació extrínseca i la intrínseca.

>[!example] Recompenses
>
>- Les recompenses extrínseques es materialitzen a través d'elements com les taules de classificació o les barres de progrés.
  >  
>- La motivació intrínseca s'assoleix quan les tasques es perceben com a significatives, agradables o personalment gratificants per a l'usuari.

- L'aplicació d'aquestes tècniques aporta beneficis clars: 
	- en educació genera més participació i motivació.
    
	- En l'àmbit de la salut i el benestar, afavoreix l'adherència als tractaments i la creació d'hàbits saludables.
    
	- A la feina i en la productivitat, permet un millor seguiment d'objectius i ofereix reconeixement visible.
    
	- Finalment, pot fomentar comportaments sostenibles i incentivar la participació ciutadana en processos comunitaris.


>[!warning] Perills
>- Tot i això, com a enginyers hem d'estar alerta als riscos de disseny: pot derivar en manipulació o disseny persuasiu opac, i generar addicció a les recompenses.
>
>- Un mal disseny pot provocar desmotivació a causa dels rànquings, pressió social, penalització pública o sobrecàrrega.


## 2. Principis de Disseny

Quan construïm programari interactiu, el disseny ha de seguir unes pautes arquitectòniques clares. 

- Els principis generals de disseny exigeixen començar sempre analitzant el problema, els objectius, l'usuari i el seu context.

>[!fail] Error Comú
> És un error comú tractar la gamificació com una capa decorativa; s'ha d'integrar profundament en les tasques clau del sistema.

- El disseny ha d'utilitzar mecàniques que s'adaptin als diferents tipus de jugadors que utilitzaran l'aplicació.

- Com en qualsevol cicle de vida de desenvolupament de programari àgil, és necessari iterar amb els usuaris mitjançant la creació de prototips i la realització de tests.
### Principis específics importants
(Nomes hi ha un enumeració)

- Pel que fa als principis específics a implementar, el sistema ha de proporcionar un feedback immediat i visible a l'usuari.

- S'ha de garantir que l'usuari tingui una sensació constant de progrés i d'avanç.

- Un dels reptes més grans en el disseny és mantenir l'equilibri correcte entre el repte proposat i l'habilitat de l'usuari.

- El sistema ha de proporcionar recompenses que siguin significatives per a qui les rep.
   
- S'ha de fomentar l'autonomia per tal d'alimentar la motivació intrínseca de l'individu.

- És altament recomanable incloure un component social en el disseny de l'experiència.
    
- Finalment, les regles del sistema han de brillar per la seva simplicitat i claredat.
    

## 3. Metodologies de Gamificació

Per no dissenyar a cegues, els professionals utilitzen bastides conceptuals. El "Gamification Model Canvas" (GMC) és l'eina estrella d'aquest temari i requereix la vostra màxima atenció per entendre com es relacionen els seus components interns.

- El Gamification Model Canvas (GMC) és una eina visual de disseny que serveix per planificar una estratègia de gamificació de manera estructurada.
    
- Aquest model es compon d'elements clau relacionats entre si per donar sentit a l'estratègia global.

### Elements Principals GMC

- Els _Behaviors_ (Comportaments), que descriuen les accions necessàries que han de desenvolupar els jugadors per tal d'obtenir retorns del projecte, com per exemple mirar un vídeo o respondre una enquesta.
    
- Les _Aesthetics_ (Estètiques) defineixen les respostes emocionals desitjables que s'evoquen en el jugador quan interacciona amb el joc, incloent-hi la narrativa, el repte o la companyonia.
    
- Les _Dynamics_ (Dinàmiques) descriuen el comportament en temps d'execució de les mecàniques actuant sobre el jugador al llarg del temps, utilitzant-se per crear les estètiques del joc (ex: estatus, progressió, recompensa).
    
- Les _Mechanics_ (Mecàniques) estableixen les regles del joc utilitzant components per crear les dinàmiques, com ara la regla de donar 10 punts per veure un vídeo.
    
- Els _Components_ són els elements o característiques específiques del joc que serveixen per crear mecàniques o donar feedback, com els punts, insígnies, nivells, barres de progrés, avatars o béns virtuals.

![[Pasted image 20260314121955.png]]


### Altres estratègies:

- A banda del GMC, el dissenyador té al seu abast altres metodologies formals, com ara el model **Octalysis**.

- També destaca el framework **MDA**, que precisament es basa en la interacció entre Mecàniques, Dinàmiques i Estètiques.

- Finalment, la Teoria de l'Autodeterminació (**Self-Determination Theory**) s'utilitza com a marc fonamental per dissenyar orientant-se a la motivació intrínseca.


## 4. Tipus de Jugador

En enginyeria de programari, no dissenyem per a un "usuari mitjà" inexistent. Hem de modelar perfils d'usuari (persones). L'estudi de les tipologies de jugadors us permetrà personalitzar les dinàmiques perquè l'aplicació sigui efectiva per a diferents perfils d'estudiants, treballadors o clients.

- El disseny gamificat fa ús de tipologies de jugador per entendre què mou a cada individu, basant-se en models com els exposats a Gamified.uk.

![[Pasted image 20260314123422.png]]


- És crucial recordar un principi fonamental: els usuaris no pertanyen a un sol perfil de manera exclusiva, sinó que **tenen un percentatge de cada tipus**.

- El model presentat s'estructura en sis tipologies principals, cadascuna impulsada per una motivació central.

- El perfil _Philanthropist_ (Filantrop) està motivat pel propòsit (_Purpose_) i gaudeix compartint coneixement, regalant o tenint cura d'altres.

- El perfil _Free Spirit_ (Esperit Lliure) es mou per l'autonomia (_Autonomy_); busca l'exploració, l'expressió creativa, la personalització i descobrir contingut ocult o "Easter Eggs".

- El perfil _Achiever_ (Aconseguidor) té com a motor la mestria (_Mastery_); l'atrauen els reptes difícils, aprendre noves habilitats, completar missions i pujar de nivell o superar "Boss Battles".

- El perfil _Player_ (Jugador) està directament focalitzat en la recompensa (_Reward_), buscant punts, premis físics, posicionar-se en taules de classificació i aconseguir insígnies.

- El perfil _Socialiser_ (Sociable) es basa en la relació i connexió amb els altres (_Relatedness_), valorant la xarxa social, la creació d'equips o gremis, i l'estatus social.

- Finalment, el perfil _Disruptor_ (Disruptor) persegueix el canvi (_Change_), gaudint en plataformes d'innovació, utilitzant eines de desenvolupament, exercint el vot i actuant sovint des de l'anonimat.

>[!tip] Tipus de motivació
>
>Intrinsec
>
>- TODO
>
>Extrinsec
>
>- TODO


![[Pasted image 20260319170251.png]]

## 5. Com Mesurar l'Impacte i Casos d'Estudi

El que no es pot mesurar no es pot millorar per això implementem mecanismes de telemetria i validació.

![[Pasted image 20260314123702.png]]

- Per mesurar de manera qualitativa l'impacte d'un sistema gamificat, s'utilitzen eines estandarditzades com els qüestionaris.

- Alguns dels qüestionaris més destacats en l'àmbit acadèmic i professional inclouen:
	- la GAMEX (Gameful Experience Scale).
	-  la _Situational motivation scale_ 
	- la _User engagement scale_ per avaluar la immersió i motivació de l'usuari.
    
- A nivell quantitatiu, és imprescindible mesurar el compromís (engagement) a través de mètriques d'ús directe. Això inclou el monitoratge de:
	- nombre d'usuaris actius, ja sigui a nivell diari o mensual.
    
	- També s'analitzen indicadors analítics com la freqüència i la durada de les sessions de connexió.
    
	- Dins del propi sistema, es quantifiquen les tasques o reptes completats per cada individu.
    
	- Es fa un seguiment exhaustiu de la progressió de l'usuari, avaluant el seu avanç en nivells, acumulació de punts o obtenció d'insígnies (_badges_).
    
	- Finalment, es mesura el volum d'interacció social dins la plataforma i els nivells generals de satisfacció declarada.
    

## Estudis
- La solidesa d'aquesta teoria es demostra en la indústria a través de casos d'estudi reals en múltiples sectors.
    
- En educació tenim plataformes líders com Duolingo o Khan Academy.
    
- En l'àmbit de l'estil de vida, s'aplica en aplicacions com Nike+, Fitbit o Dacadoo.
    
- Pel que fa al compromís dels empleats corporatius, grans empreses com SAP o McDonalds utilitzen la gamificació per motivar la seva plantilla.
    


# Tema 7

## 1. Introducció als Wearables

Els _wearables_ es defineixen fonamentalment com a dispositius informàtics que l'usuari porta posats sobre el cos de manera permanent. A diferència d'altres tecnologies, la seva naturalesa implica que estan **sempre en funcionament** i operant en segon pla.

### Característiques clau:

- **Sensòrica avançada:** Equipats amb diversos tipus de sensors per captar dades biomètriques i ambientals.
    
- **Interaccions efímeres:** Estan dissenyats per a interaccions molt ràpides (micro-interaccions).
    
- **Fonaments teòrics:** Es basen en conceptes clau de la HCI com la **Computació Ubíqua** (tecnologia present a tot arreu), l'**Embodied Interaction** (interacció corporitzada) i la **Humanistic Intelligence**.
    
- **Focus del temari:** Tot i l'existència d'anells o bandes, el contingut acadèmic se centra específicament en els **Smartwatches**.
    

## 2. Humanistic Intelligence (Intel·ligència Humanística)

Aquest concepte, impulsat per pioners com Marvin Minsky i Steve Mann, proposa una simbiosi on l'ordinador i l'humà actuen com un únic sistema enllaçat.

### Els 6 pilars del model:

1. **Unmonopolizing (No monopolitzador):** No ha d'ocupar tota l'atenció de l'usuari ni impedir que realitzi altres tasques.
    
2. **Unrestrictive (No restrictiu):** No ha de limitar les activitats físiques o socials de la persona.
    
3. **Observable:** El dispositiu és conscient de l'usuari i el seu entorn.
    
4. **Controllable (Controlable):** L'usuari sempre ha de tenir el control sobre el dispositiu.
    
5. **Attentive (Atent):** L'ordinador monitoritza constantment l'usuari per transmetre-li informació rellevant en el moment just.
    
6. **Communicative (Comunicatiu):** Actua com una interfície de comunicació fluida.
    

## 3. Wearables vs. Smartphones

Com a enginyers, hem d'entendre que un _smartwatch_ no és un telèfon petit; les regles del joc canvien radicalment segons el context d'ús.

|**Característica**|**Wearable**|**Smartphone**|
|---|---|---|
|**Pantalla**|Molt petita|Gran|
|**Temps d'ús**|Segons (micro-interaccions)|Minuts|
|**Context**|Principalment en moviment|Sovint en repòs/quiet|
|**Input**|Veu, gestos corporals|Touch / Teclat virtual|
|**Atenció**|Ràpida i fragmentada|Focalitzada i sostinguda|

## 4. Reptes i Tipus d'Interacció

El disseny per a _wearables_ s'enfronta a limitacions físiques i situacionals severes, com pantalles minúscules, bateries limitades i la necessitat de gestionar la privacitat en espais públics.

### Modalitats d'interacció (Multimodalitat):

- **Gestos Tàctils:** Taps, swipes en 4 direccions i pressions llargues.
    
- **Gestos de Canell:** _Wrist raise_ (aixecar per activar) i _wrist flick_ (gir ràpid).
    
- **Veu:** Ús d'assistents per obrir aplicacions o dictar missatges.
    
- **Hàptica:** Vibracions subtils per a alertes sense necessitat de mirar la pantalla.
    
- **Elements Físics:** Botons laterals i la **Corona Digital** per fer scroll o zoom sense tapar la pantalla amb els dits.
    

### Categories d'ús segons NN/g:

L'estudi de Nielsen Norman Group identifica accions com **Receiving** (rebre info), **Referencing** (consultar dades ràpides), **Recording** (capturar dades biomètriques), **Controlling** (gestionar altres dispositius), **Communicating** i **Guiding** (navegació pas a pas).

## 5. Principis de Disseny Específics

Per garantir una bona experiència d'usuari (UX), hem de seguir quatre pilars fonamentals:

1. **Glanceability:** L'usuari ha de poder absorbir la informació en 1 o 2 segons. Això s'assoleix amb tipografies grans, icones clares i jerarquies visuals extremadament simples.
    
2. **Simplicitat:** Fluxos de tasques molt curts i reducció dràstica del nombre d'opcions.
    
3. **Context Awareness:** L'aplicació ha de ser "intel·ligent" i adaptar-se segons la ubicació, el ritme cardíac o l'hora del dia (UX adaptativa).
    
4. **Accessibilitat:** Disseny inclusiu mitjançant contrastos alts i mides de text ajustables.
    

## 6. Patrons de Disseny Arquitectònics

En el desenvolupament de programari per a _wearables_, utilitzem patrons específics per organitzar la informació:

- **Notificacions:** El canal principal d'entrada d'informació externa.
    
- **Complications/Widgets:** Petits elements informatius directament a l'esfera del rellotge (ex: bateria, data, BPM).
    
- **Tiles o Cards:** Pantalles d'accés ràpid que es mostren en fer _swipe_ lateral.
    
- **Accions Ràpides:** Botons grans i accessibles per a funcions immediates com "Play" o "Clear all".
    
- **Companion Apps:** Aplicacions que viuen al telèfon i serveixen per configurar o analitzar dades del _wearable_ de forma extensa.
    

>[!tips] Info a teoria:
>- Amb els wearables el més important és el context
>- Mirar els conceptes de disseny
>- Principi vs patro de disseny
>	- Principis són més absractes que serveixen per aplicar-se a un patró
>		- ex. La Gleanceability
>	- El patrons


# Tema 8

### 1. Introducció i Ideació

La premissa fonamental del disseny d'interacció és preguntar-nos: **Estem resolent un problema real de l'usuari amb la IA?**. No es tracta d'aplicar tecnologia perquè sí, sinó de minimitzar riscos mentre maximitzem beneficis. Si la resposta és afirmativa, entrem en la fase d'ideació on disposem de tres eines principals:

- **Storyboarding:** Per visualitzar el context d'ús.
    
- **Models Digitals (Digital Twins):** Per modelar el sistema.
    
- **Frameworks i Patrons:** Com el de Google PAIR, per aplicar bones pràctiques.
    

### 2. Storyboarding en IA

Un storyboard explica visualment una història per validar la viabilitat de la visió d'UX. En IA és vital perquè permet detectar "buits" en la interacció que el text sol ocultar.

**Components clau d'un storyboard:**

- **Escena inicial:** Context i protagonista.
    
- **Coses i Persones:** Objectes de l'entorn i accions dels usuaris.
    
- **Expressions facials:** Indispensables per transmetre l'estat emocional (frustració, satisfacció, pèrdua de confiança).
    
- **Transicions:** Connecten les escenes. Poden ser d'acció a acció, de subjecte a subjecte, de canvi d'escena o, el més important, d'**interacció amb la IA**.
    
- **Conclusió:** Ha de mostrar clarament el benefici o resultat de la solució.
    

> **Nota de l'acadèmic:** Un bon storyboard d'IA ha de mostrar no només quan el sistema funciona, sinó també com reacciona l'usuari quan la IA falla o dóna una resposta inesperada .

### 3. Digital Twins Model (Bessons Digitals)

Un **bessó digital** és un model virtual d'un objecte o procés real. En UX per a IA, l'utilitzem per decidir quines variables del món físic ha de conèixer la IA per ser útil.

**Etapes de creació:**

1. **Entendre les dades:** Què rep la IA del món real?.
    
2. **Representació visual i etiquetatge:** Dibuixar el sistema i posar nom a les dades d'entrada (inputs).
    
3. **Definir el cas d'ús:** Què pot predir o fer el model? (outputs) .
    
4. **Iteració:** Identificar dades que falten i integrar noves fonts (exemple: passar d'un smartwatch que només mesura el pols a un que integra GPS i dades de son per predir l'esperança de vida).
    
5. **Ètica:** Vigilar conclusions que puguin ser problemàtiques.
    

### 4. Mètriques de Rendiment: Confusion vs. Value Matrix

Com a enginyers, no només ens importa si el model és precís, sinó si és rendible i útil.

- **Confusion Matrix (Matriu de Confusió):** Avalua el rendiment tècnic comparant prediccions amb la realitat (True Positives, False Positives, etc.).
    
- **Value Matrix (Matriu de Valor):** Tradueix els resultats de la matriu de confusió en **costos i beneficis del món real** (assignant valors monetaris o de ROI).
    

> **Exemple d'examen:** Un model "Aggressive" pot tenir molts avisos (alta Recall), però si cada False Positive costa molts diners (FP), la matriu de valor ens dirà que potser és millor un model "Balanced" amb menys precisió tècnica però més retorn econòmic.

### 5. Marc de Disseny Google PAIR

El framework **PAIR (People + AI Research)** se centra en tres pilars: **transparència, confiança i control**.

**Els 5 Principis de PAIR:**

1. **User Autonomy:** L'usuari ha de tenir el control.
    
2. **Data & Model Alignment:** Les dades han d'estar alineades amb l'objectiu.
    
3. **Adapt with Feedback:** El sistema ha d'aprendre de l'usuari.
    
4. **Helpful AI:** La IA ha de ser útil, no només tecnològica.
    
5. **Evolving Safety:** Seguretat constant i evolutiva.
    

### 6. Patrons de Disseny d'IA

PAIR proposa patrons pràctics per a situacions comunes:

- **Expectatives:** Explica què pot fer el sistema realment (ex: "identifica 400 plantes" en comptes de "identifica qualsevol planta") .
    
- **Benefici vs. Tecnologia:** Explica què guanya l'usuari, no quins algorismes fas servir (ex: "t'ajuda a aprendre" vs "usa un model de llenguatge natural") .
    
- **Gestió d'errors:** Sigues responsable dels errors i dóna control a l'usuari quan l'automatització falla.
    
- **Privacitat:** Sigues transparent amb les dades que reculls per generar recomanacions.
    
- **Feedback:** Permet que l'usuari corregeixi el sistema (ex: botons de "massa fàcil" o "massa difícil").
    

### 7. Patrons Específics per a LLMs

Pels models de llenguatge (com ChatGPT o Copilots), fem servir patrons d'interacció específics:

- **Restating/Talk-Back:** Confirmar què s'ha entès i guiar l'usuari.
    
- **Suggestions/Next Steps:** Oferir idees per començar o camins a seguir després d'una resposta.
    
- **Auto-Complete:** Completar text en temps real.
    
- **Guardrails:** Filtres per assegurar que les respostes siguin segures i ètiques.
    





# Glossari
### **Confirmation Bias (Biaix de confirmació):** 
És el parany mental més perillós per a un investigador. Consisteix en la tendència a formular preguntes, o interpretar les dades recollides, d'una manera que validi les nostres hipòtesis o creences inicials. Tal com destaquen els apunts, és molt fàcil construir preguntes d'una manera que ens asseguri que les nostres suposicions seran validades.

### **Anchoring Bias (Biaix d'ancoratge):**
Es produeix quan una persona es basa massa en la primera peça d'informació que rep (l'"àncora") a l'hora de prendre una decisió o fer una valoració. Als teus apunts s'adverteix que la seqüència o l'ordre de les opcions en un qüestionari és molt important precisament per aquest efecte.

### **Leading Questions (Preguntes capcioses):** 
Són aquelles preguntes redactades de tal manera que suggereixen directament a l'usuari quina és la resposta que esperem obtenir. D'aquesta manera, estem posant paraules a la boca de l'usuari.

### **Self-reporting Errors (Errors d'autoinforme):**
Més que un biaix cognitiu únic, és una realitat del comportament humà: l'usuari no sempre diu el que pensa de veritat, ni recorda exactament com fa les coses a la realitat. Per això demanem accions passades en lloc de prediccions futures.

### **Social Desirability Bias (Biaix de desitjabilitat social):** 
És la inclinació dels enquestats a respondre d'una manera que serà vista favorablement pels altres. L'usuari tendirà a amagar hàbits o opinions que considera "socialment inacceptables" per projectar una imatge millor de si mateix davant teu.

### **Recency Bias (Biaix de recència):** 
És la tendència a donar molta més importància, o a recordar amb molta més facilitat, els esdeveniments recents en comparació amb els fets més antics.

### **Framing (Efecte d'emmarcament):** 
Aquest efecte demostra que les persones reaccionen de manera diferent a una mateixa elecció depenent de com se'ls presenti o "emmarqui" la informació (per exemple, presentant un resultat com una pèrdua o com un guany).





