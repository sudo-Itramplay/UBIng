# Interacció Persona-Ordinador (HCI)

- L'HCI (Human Computer Interaction) és un camp interdisciplinari que se centra exclusivament en el disseny de sistemes interactius per a l'ús humà. 
	- La premissa fonamental és que l'única via per a un bon disseny és començar per les persones.

- Es defineix com un sistema sòcio-tecnològic on una persona (o grup de persones) interactua amb un ordinador per intentar aconseguir un objectiu concret.

## Components

### H
**El component "Human":**
A l'hora d'avaluar l'usuari, hem de considerar factors crítics com:
- l'atenció, la confiança, la memòria, la diversitat, el context d'ús i el comportament d'aprenentatge. 
A més, hem de tenir en compte l'ètica, la privacitat, els biaixos i evitar danys no intencionats.

>[!tip] Ojo
>No dissenyem només per a qui fa el clic. Hi ha altres actors clau: 
>- els _stakeholders_ o parts interessades (com el CEO, màrqueting o enginyeria, cadascú amb les seves preocupacions de mercat o implementació) 
>- els _bystanders_ o persones afectades indirectament pel sistema.

### C
- **El component "Computer":** És la màquina qui executa els programes, respon i ens estableix els límits tècnics; sovint potenciat per sistemes d'Intel·ligència Artificial.

### I
- **La Interacció:** És el cicle on la persona expressa les seves intencions al computador i aquest hi respon. 

>[!info] Tipus de sistemes
>El sistema pot ser:
>-  reactiu (reacciona a l'acció de l'usuari) 
>- proactiu (sistemes amb IA que s'avancen a les demandes, com els recomanadors).


---

### Secció 2: Disseny Centrat en l'Usuari (UCD) i Metodologies

_(Referència: Diapositives 11-24 i els teus apunts personals)_

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

# Model Teòric d'Interacció i el Factor Humà

- A nivell cognitiu, la interacció no es redueix a l'acte mecànic de "fer clic". És un cicle continu de pensament, acció i interpretació que transcorre entre l'usuari i el sistema.

- Per entendre què passa realment durant la interacció, s'utilitza un model teòric que divideix el procés en dos grans "golfs" o bretxes entre el que vol la persona i l'estat del món físic o digital.

- **El Golf d'Execució (Bridge of Execution):** Representa el salt des de l'usuari cap al sistema.
	
    - _Goal:_ L'usuari estableix un objectiu (p. ex., tinc calor a l'aula).
        
    - _Plan:_ Formula un pla per assolir-lo (pensar en encendre l'aire).
        
    - _Specify:_ Especifica l'acció concreta necessària.
        
    - _Perform:_ Executa físicament l'acció (demanar-ho o prémer el botó).
        
- **El Golf d'Avaluació (Bridge of Evaluation):** Representa el salt des del sistema de tornada cap a l'usuari.
	
    - _World:_ El món realitza un canvi d'estat.
        
    - _Perceive:_ L'usuari percep de manera sensorial el que ha passat.
        
    - _Interpret:_ L'usuari processa i interpreta aquesta informació.
        
    - _Compare:_ Finalment, compara el nou estat amb l'objectiu inicial per saber si s'ha complert.
        
- **El Factor Humà:** Tota aquesta teoria es fonamenta en entendre el factor humà, que engloba les capacitats, característiques i limitacions que influeixen en l'ús d'un sistema.

- Dissenyar tenint present aquest factor és el que garanteix que els sistemes acabin sent eficients, inclusius, confiables i agradables. S'hi arriba a través del UCD i analitzant el processament cognitiu, la percepció i el sistema motor humà.


---

### Usabilitat vs. Experiència d'Usuari (UX)

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
