
## 1. Introducció a l'Avaluació

L'avaluació és l'etapa del disseny centrat en l'humà (HCD) que permet validar si les solucions proposades realment funcionen per a les persones. 
	Segons la normativa **ISO 9241-210**, el disseny ha d'estar impulsat i refinat per una avaluació centrada en l'usuari.

- **Propòsits clau**: 
	- Obtenir feedback,
	- identificar punts forts i febles per millorar el disseny,
	- confirmar el compliment de requisits 
	- establir comparatives o _baselines_.
    
- **Perspectiva**: L'avaluació s'ha de fer **SEMPRE** des de la perspectiva de l'usuari/a.
    
- **Eficiència**: Amb només **5 usuaris** es poden detectar aproximadament el **80% dels problemes d'usabilitat**.


- **Tipus Avaluaicio**:
    
    - **Avaluació amb Usuaris reals**
        
    - **Avaluació amb Experts**
    
	- **Monitoratge a llarg termini** 




## 2. Avaluació amb Usuaris: Fonaments i Ètica

Aquest mètode és el més fonamental perquè proporciona informació directa sobre com la gent real utilitza els ordinadors.


- **Avaluacio amb usuaris**:
    
    - **Avaluació Formativa**: Es realitza durant el procés iteratiu (etapes inicials i mitjanes) per millorar el producte.
        
    - **Avaluació Sumativa**: Es realitza al final o durant l'ús operatiu per confirmar que s'han complert els objectius i detectar problemes a llarg termini.
![[Pasted image 20260518174247.png]]

>[!warning] Monitoreig a llarg tremini
>També continua aquest procès via insights, aquests poden tant denotar un problema (molt rebots) com ajudar a solucionar errors



- **Estratègies d'èxit**: 
	- [ ] **Temporització òptima:** Fer els tests prou tard per tenir un disseny concret, però prou aviat per poder-lo ajustar.
	
	- [ ] **Definició de tasques:** Dissenyar tasques rellevants en funció dels objectius del test i del producte o servei.
	
	- [ ] **Reclutament precís:** Seleccionar usuaris del públic objectiu basant-se en l'artefacte _persona_.
	
	- [ ] **Pensament en veu alta (_Thinking Aloud_):** Demanar als usuaris que expressin el que pensen mentre executen les tasques.
	
	- [ ] **Prototips simples:** Utilitzar prototips de baixa o mitjana fidelitat per no desviar l'atenció del flux bàsic.
	
	- [ ] **Moderació activa:** Detectar problemes d'ús i trobar-ne les causes subjacents durant la sessió.
	
	- [ ] **Evitació de biaixos:** Utilitzar, si és possible, un moderador extern al projecte per mantenir l'objectivitat.
	
	- [ ] **Focus en l'usuari:** Centrar-se estrictament en els comportaments observats i en els seus motius.
	
	- [ ] **Fase post-test:** Realitzar una revisió conjunta amb els observadors i una petita conversa de tancament amb els usuaris.
	
	- [ ] **Implicació del disseny:** Involucrar els dissenyadors durant tot el procés per facilitar la posterior iteració.


#### Classificació de Mètodes

Els mètodes de test d'usabilitat es poden categoritzar en funció de **quatre variables principals** (representades en els dos eixos del gràfic) i una tècnica comparativa addicional:

### Eixos de Classificació

- **Segons la interacció:**
    
    - **Moderat:** Hi ha un facilitador que guia la sessió i interactua amb l'usuari.
        
    - **No moderat:** L'usuari realitza les tasques de manera autònoma sense intervenció directa.
        
- **Segons la ubicació:**
    
    - **Remot:** El test es realitza a distància (online).
        
    - **En persona:** El test es fa compartint espai físic amb l'usuari.
        

### Quadrants i Exemples 

- **Remot + Moderat:** _Phone/Video Interview_ (Entrevistes per videotrucada).
    
- **Remot + No moderat:** _Session Recordings_ (Enregistraments de sessions).
    
- **En persona + Moderat:** _Lab Usability Testing_ (Tests de laboratori — **Pràctica 3**) i _Guerrilla Testing_.
    
- **En persona + No moderat:** _Observation "in-the-wild"_ (Observació en entorns reals o de camp).
    
- **Híbrid / Transversal:** _User Testing Platforms_ (Plataformes de test que cobreixen l'espectre remot).

![[Pasted image 20260518174750.png]]

#####  Mètode Comparatiu Addicional

- **A/B testing:** Experimentació quantitativa on es comparen dues versions d'una mateixa interfície (A i B) per veure quina funciona millor.


- **Consideracions Ètiques (Molt important)**:
    
    - **Abans**: Cal obtenir un **consentiment informat**. S'ha d'emfatitzar que es prova el sistema, **no l'usuari**. L'usuari pot aturar-se quan vulgui.
        
    - **Durant**: Cal crear una atmosfera relaxada i evitar que el cap de l'usuari observi la prova per no generar pressió. Mai s'ha d'indicar que l'usuari comet errors.
        
    - **Després**: S'ha de garantir la confidencialitat absoluta. Els resultats no han de permetre identificar individus.
        

## 3. Procediment i Disseny de l'Estudi

Tot test d'usabilitat requereix una preparació rigorosa que inclou la definició d'objectius i un **test pilot** (provar el test abans de fer-lo amb els usuaris reals per validar instruccions i durada).

### Procediment
#### 1. Preparacio
- **Definició de l'objectiu:** L'objectiu clar i els recursos disponibles determinen directament:
    
    - Els mètodes a aplicar.
		![[Pasted image 20260518175920.png]]
    - Els materials i instruments a utilitzar.
        
    - La selecció i perfil dels participants.
	    ![[Pasted image 20260518175958.png]]


- **Consideracions ètiques:** Cal planificar i tenir en compte els aspectes ètics i de privacitat (per exemple, consentiments informats).
    
- **Test pilot:** Realitzar una prova prèvia interna per validar que tot funciona correctament abans de registrar els usuaris reals. 
	- **Valorem el test, no el producte**
    
### **Arquitectura de l'estudi**:

- **Between-subjects design**: Diferents grups d'usuaris fan diferents tasques o proven diferents versions. Evita l'efecte d'aprenentatge, però requereix més participants.
	
- **Within-subjects design**: Cada usuari realitza totes les tasques o prova totes les versions. És més eficient en nombre d'usuaris, però cal balancejar l'ordre de les tasques per evitar el _transfer effect_ (aprenentatge).

![[Pasted image 20260518180150.png]]

- **Exemples d'objectius**: Si l'objectiu és l'accessibilitat, calen usuaris amb diversitat funcional; si és la "primera impressió", calen usuaris novells.

![[Pasted image 20260518180220.png]]


#### 2. Realització

- **Estructura de la sessió:** Totes les sessions han de mantenir la mateixa estructura per a tots els participants:
    
    1. **Introducció i tasques:** Benvinguda, contextualització i lliurament de les tasques.
        
    2. **Execució:** L'usuari realitza les tasques de manera autònoma.
        
    3. **Tancament:** Emissió de qüestionaris i/o realització d'una entrevista final.
        
- **Rol del moderador:** Intervé de manera totalment passiva; **només actua si l'usuari es bloqueja** i no pot continuar.
    

#### 3. Anàlisi dels resultats

- **Reportar i iterar:** Analitzar les dades recollides durant les sessions i generar un informe de resultats que inclogui propostes de millora concretes per al disseny.


    

### 4. Mètriques d'Usabilitat i UX

Les mètriques ens permeten quantificar l'experiència. Se solen dividir en tres categories principals:

- **Eficàcia**: Taxa d'èxit (completion rate) i taxa d'errors.
    
- **Eficiència**: Temps per completar la tasca, nombre de clics i "lostness".
    
- **Satisfacció (Actitudinals)**: Percepció de facilitat, confiança i càrrega de treball.
    
- **Mètriques fisiològiques**: _Eye tracking_ (fixacions), dilatació de la pupil·la, ritme cardíac o conductància de la pell per mesurar emocions i atenció.
####  Exemples d'Objectius i Mètriques Associades

A la pràctica, triem les mètriques segons les preguntes de recerca que volem respondre:

<summary> <b>Objectiu 1: Comprovar si els usuaris poden completar una tasca concreta sense errors</b></summary>

* **Taxa d'èxit (*Completion rate*):** Percentatge d'usuaris que aconsegueixen completar la tasca amb èxit. *(Eficàcia)*
* **Taxa d'errors:** Percentatge d'usuaris que cometen almenys un error durant l'execució de la tasca. *(Eficàcia)*
* **Temps de compleció:** Temps mitjà requerit per un usuari per completar la tasca de principi a fi. *(Eficiència)*



<summary> <b>Objectiu 2: Avaluar si l'usuari entén el significat d'una icona o etiqueta</b></summary>

* **Percentatge de comprensió correcta:** Resposta numèrica i quantificable a la pregunta directa: *"Què creus que fa aquest botó?"* o *"Què significa aquesta etiqueta?"*
* **Comentaris qualitatius:** Recull de confusions, dubtes o interpretacions errònies expressades per l'usuari en veu alta.



<summary> <b>Objectiu 3: Mesurar la càrrega cognitiva durant una tasca complexa</b></summary>

* **NASA-TLX (*Task Load Index*):** Qüestionari estandarditzat post-tasca que s'utilitza per mesurar l'esforç mental i físic percebut per l'usuari. *(Satisfacció / Càrrega de treball)*
* **Temps de reflexió abans d'actuar:** El temps de latència o pausa que fa l'usuari abans d'interactuar amb un element de la interfície.



<summary><b>Objectiu 4: Avaluar la satisfacció general amb el sistema</b></summary>

* **SUS (*System Usability Scale*):** Qüestionari ràpid i estandarditzat de 10 ítems per avaluar la usabilitat percebuda d'un sistema.
* **NPS (*Net Promoter Score*):** Mètrica d'una sola pregunta per mesurar la lleialtat i la probabilitat de recomanació del producte.
* **Comentaris oberts:** Feedback qualitatiu de tancament sobre què els ha agradat més i què menys del sistema.


---

### 5. Qüestionaris Estandarditzats

Són eines ja validades que no s'han de modificar. S'utilitzen post-tasca o post-estudi.

- **SEQ (Single Ease Question)**: Una sola pregunta d'1 a 7 sobre la dificultat d'una tasca.
    
- **SUS (System Usability Scale)**: 10 preguntes (positives i negatives intercalades). Una puntuació per sobre de 68-70 es considera "acceptable".
    
- **UEQ (User eXperience Questionnaire)**: Mesura dimensions com l'atractiu, la claredat, l'eficiència, la seguretat, l'estimulació i la novetat.
    
- **NPS (Net Promoter Score)**: Mesura la lleialtat. Es calcula com:
    
    $$NPS = \% \text{Promoters (9-10)} - \% \text{Detractors (0-6)}$$
    
    Els usuaris amb puntuacions 7-8 es consideren "Passius" i no compten per a la fórmula.
    
#### 5.1 Anàlisi de Resultats en l'Avaluació amb Usuaris

Un cop finalitzades les proves amb usuaris, s'han d'analitzar tant les dades quantitatives com les qualitatives per extreure propostes de millora reals:

- **Dades Quantitatives:** S'utilitzen eines estadístiques estructurades en dos nivells:
    
    - _Anàlisi Descriptiu:_ Permet una primera comprensió de les dades mitjançant mètriques com la mitjana, la mitjana, la moda i el rang interquartílic. Es recolza en visualitzacions com histogrames, _box plots_ o _scatterplots_.
        
    - _Anàlisi Inferencial:_ Aplica mètodes paramètrics i no paramètrics per fer generalitzacions sobre la població a partir de la mostra estudiada , visualitzant els grups mitjançant gràfics de barres o relacions de variables.
        
- **Dades Qualitatives (Anàlisi Temàtica):** S'utilitza el mètode de Clarke & Braun (2017) per identificar patrons o "temes" dins de les transcripcions d'àudio o notes de text. El procés segueix 6 passos estructurats:
    
    1. Reclutar i recollir les dades (_Gather_).
        
    2. Llegir detalladament el contingut (_Read_).
        
    3. Codificar les dades segons el seu significat primari (_Code_).
        
    4. Crear nous codis per encapsular temes emergents (_Create themes_).
        
    5. Prendre un descans d'un dia per guanyar perspectiva (_Take a break_).


## 6. Avaluació per Experts (Inspection Methods)

Aquestes avaluacions no requereixen usuaris reals, el que les fa més ràpides i barates, però no capturen emocions reals.

- Perque?
	- D'aquesta manera veiem problemes d'usabilitat abans de fer un primer test amb usuaris
	- Permet una avaluacio mes amplia
	- Mes simple i rapid que amb usuaris
	- O per quan no es poden usuaris ja sigui per posibilitat o temps
- Desvantatges
	- S'han de complementar amb usuaris reals
	- hi ha risc de biaix/subjectivitat
	- abast limitat, ens regim a coses que no capturen emocions
	- Es dificil tenir en compte context real
	- No es recullen dades d'interaccio

- **Avaluació Heurística**: L'expert jutja la interfície basant-se en principis (ex: les 10 heurístiques de Nielsen com "Visibilitat de l'estat del sistema" o "Prevenció d'errors"). 
	- Els experts faran varies passades
	- Es recomana que diversos experts ho facin de forma independent i després posin en comú els resultats.
	- Finalment redacten un informe que inclou els problemes i las seva gravetat

    
- **Passeig Cognitiu (Cognitive Walkthrough)**: L'expert simula ser un usuari novell intentant completar una tasca específica. Per a cada pas es pregunta:
    
    1. Entendrà l'usuari que ha de fer aquesta acció?
        
    2. Veurà l'usuari l'element per fer-la?
        
    3. Entendrà el feedback que rep?
    
	Es fa sobretot per intentar fer mes accesibles les aplicacions
        

## 7. IA Generativa (IAG) en l'Avaluació

**Referència: Diapositives 60-64**

L'ús d'eines com ChatGPT està transformant com treballem en IPO.

- **Aplicacions**: Generació d' _screeners_ (qüestionaris de selecció), creació de plantilles Excel amb fórmules per al SUS, i suport en l'**anàlisi temàtic** (anàlisi qualitatiu de transcripcions d'entrevistes).
    
- **Anàlisi Temàtic**: Procés de 6 passos (Recollir dades -> Llegir -> Codificar -> Crear temes -> Pausa -> Avaluar _fit_ dels temes). La IAG ajuda a identificar patrons i codis en grans volums de text.
