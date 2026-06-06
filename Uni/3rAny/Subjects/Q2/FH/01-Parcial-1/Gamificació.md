# 1. Introducció a la Gamificació

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


# 2. Principis de Disseny

Quan construïm programari interactiu, el disseny ha de seguir unes pautes arquitectòniques clares. 

- Els principis generals de disseny exigeixen començar sempre analitzant el problema, els objectius, l'usuari i el seu context.

>[!fail] Error Comú
> És un error comú tractar la gamificació com una capa decorativa; s'ha d'integrar profundament en les tasques clau del sistema.

- El disseny ha d'utilitzar mecàniques que s'adaptin als diferents tipus de jugadors que utilitzaran l'aplicació.

- Com en qualsevol cicle de vida de desenvolupament de programari àgil, és necessari iterar amb els usuaris mitjançant la creació de prototips i la realització de tests.
## Principis específics importants
(Nomes hi ha un enumeració)

- Pel que fa als principis específics a implementar, el sistema ha de proporcionar un feedback immediat i visible a l'usuari.

- S'ha de garantir que l'usuari tingui una sensació constant de progrés i d'avanç.

- Un dels reptes més grans en el disseny és mantenir l'equilibri correcte entre el repte proposat i l'habilitat de l'usuari.

- El sistema ha de proporcionar recompenses que siguin significatives per a qui les rep.
   
- S'ha de fomentar l'autonomia per tal d'alimentar la motivació intrínseca de l'individu.

- És altament recomanable incloure un component social en el disseny de l'experiència.
    
- Finalment, les regles del sistema han de brillar per la seva simplicitat i claredat.
    

# 3. Metodologies de Gamificació

Per no dissenyar a cegues, els professionals utilitzen bastides conceptuals. El "Gamification Model Canvas" (GMC) és l'eina estrella d'aquest temari i requereix la vostra màxima atenció per entendre com es relacionen els seus components interns.

- El Gamification Model Canvas (GMC) és una eina visual de disseny que serveix per planificar una estratègia de gamificació de manera estructurada.
    
- Aquest model es compon d'elements clau relacionats entre si per donar sentit a l'estratègia global.

## Elements Principals GMC

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


# 4. Tipus de Jugador

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
>-
>
>Extrinsec
>
>- 


![[Pasted image 20260319170251.png]]

# 5. Com Mesurar l'Impacte i Casos d'Estudi

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
    

# Estudis
- La solidesa d'aquesta teoria es demostra en la indústria a través de casos d'estudi reals en múltiples sectors.
    
- En educació tenim plataformes líders com Duolingo o Khan Academy.
    
- En l'àmbit de l'estil de vida, s'aplica en aplicacions com Nike+, Fitbit o Dacadoo.
    
- Pel que fa al compromís dels empleats corporatius, grans empreses com SAP o McDonalds utilitzen la gamificació per motivar la seva plantilla.
    
