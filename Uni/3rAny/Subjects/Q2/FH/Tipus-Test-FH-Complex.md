# Tipus Test - Factors Humans (Preguntes Complexes)

---

## PART I: Preguntes Tipus Test (20 preguntes)

### Pregunta 1
Una empresa de comerç electrònic vol redissenyar la seva pàgina de checkout perquè ha detectat una taxa d'abandonament del 78%. L'equip de disseny proposa dues solucions:
- **Solució A**: Simplificar el procés de 5 passos a 2 passos, concentrant tota la informació en menys pantalles
- **Solució B**: Mantenir els 5 passos (wizard) però afegir un indicador de progrés visual i missatges de confiança a cada pas

Analitzant des de la perspectiva de la **Llei de Hick-Hyman** i els **principis de Norman**, quina afirmació és **MÉS CORRECTA**?

a) La Solució A és superior perquè menys passos vol dir menys interaccions totals, i per tant menys temps acumulat per completar el procés.

b) La Solució A és superior perquè redueix el nombre total de decisions que l'usuari ha de prendre, disminuint la càrrega cognitiva global del procés.

c) La Solució B és superior perquè el wizard divideix el procés en passos amb poques opcions cadascun, reduint el temps de decisió per pas segons Hick-Hyman ($RT = a + b \cdot \log_2(n)$ on $n$ és el nombre d'opcions per pas, no el nombre de passos). A més, l'indicador de progrés proporciona feedback i visibilitat de l'estat del sistema (principi de Norman), atacant tant el golf d'execució com el d'avaluació.

d) La Solució A va en contra de Hick-Hyman perquè concentrar més informació en menys pantalles augmenta el nombre d'opcions per pas ($n$), incrementant el temps de decisió a cada pas. Però la Solució B també és problemàtica perquè més passos vol dir més temps total acumulat. Per tant, cap de les dues solucions és adequada.

**Resposta correcta: c**

> **Explicació**: La Llei de Hick-Hyman mesura el temps per prendre UNA decisió en funció del nombre d'opcions disponibles en aquell moment ($n$). Els wizards aprofiten això: dividir un procés complex en passos amb poques opcions redueix la càrrega cognitiva per pas, encara que augmenti el nombre total de passos. La Solució A fa el contrari: concentra més opcions per pantalla, augmentant $n$ i per tant el temps de decisió a cada pas. La Solució B manté el wizard (poc $n$ per pas) i afegeix feedback (principi de Norman) per reduir l'ansietat i l'abandonament.

---

### Pregunta 2
Estàs realitzant una investigació contextual amb un usuari que treballa com a controlador aeri. Durant l'observació amb la tècnica **Master-Apprentice**, notes que l'usuari realitza una seqüència de 12 accions per gestionar un conflicte d'espai aeri, però quan li preguntes per què ho fa així, respon: "Sempre ho he fet així, no sé explicar-ho".

Aquesta situació il·lustra quin problema fonamental de les tècniques d'investigació?

a) El biaix de confirmació (Confirmation Bias), on l'investigador busca confirmar les seves hipòtesis prèvies sobre el comportament de l'usuari.

b) L'error d'autoinforme (Self-reporting error), on l'usuari no pot articular coneixement tàcit que ha automatitzat amb l'experiència, fent que les entrevistes siguin insuficients per capturar el procés real.

c) L'efecte Hawthorne, on l'usuari modifica el seu comportament perquè sap que està sent observat.

d) El biaix d'ancoratge (Anchoring Bias), on l'usuari es fixa en la primera experiència que recorda i no pot descriure variacions.

**Resposta correcta: b**

---

### Pregunta 3
Una aplicació de banca mòbil ha de dissenyar la funcionalitat de transferència internacional. L'equip identifica tres perfils d'usuari:
- **Perfil X**: Executiu de 45 anys, expert en tecnologia, necessita eficiència màxima
- **Perfil Y**: Jubilada de 72 anys, usuària novella, amb lleugera pèrdua de visió i inseguretat tecnològica
- **Perfil Z**: Estudiant de 20 anys, usuari intermedi, preocupat per la seguretat

Segons els principis de **disseny inclusiu** i la **Llei de Miller**, quina estratègia de disseny és **MÉS ADEQUADA**?

a) Dissenyar tres interfícies diferents, una per a cada perfil, perquè cada una optimitzi els trade-offs específics (eficiència per X, facilitat d'aprenentatge per Y, control d'errors per Z).

b) Dissenyar per al Perfil Y (el més limitat) aplicant el principi de "resoldre per als extrems beneficia a tothom": botons grans, confirmacions clares, i chunking de la informació en grups de 7±2 elements, perquè els altres perfils també es beneficiaran d'aquestes millores.

c) Dissenyar per al Perfil X (el més exigent) perquè si l'expert pot usar el sistema eficientment, els altres usuaris podran adaptar-se amb formació addicional.

d) Dissenyar per al Perfil Z (l'intermedi) com a compromís, i oferir opcions de personalització perquè els altres perfils puguin ajustar la interfície.

**Resposta correcta: b**

---

### Pregunta 4
En un test d'usabilitat amb **between-subjects design**, assignes 30 participants a tres grups (10 per grup) per provar tres versions d'una app de fitness. Després de l'anàlisi, detectes que el Grup 2 (versió B) té una taxa d'èxit significativament més alta.

Quina de les següents interpretacions és **MÉS PROBLEMÀTICA** des del punt de vista metodològic?

a) La versió B és objectivament superior perquè ha obtingut millors resultats en condicions controlades.

b) La diferència pot ser deguda a variabilitat entre grups (per exemple, el Grup 2 podria tenir més usuaris experts per atzar), ja que el between-subjects design no controla les diferències individuals entre participants.

c) Caldria haver utilitzat un within-subjects design per eliminar la variabilitat inter-grup, tot i que això hauria introduït efectes d'aprenentatge.

d) La mida mostral de 10 per grup és insuficient per fer generalitzacions estadístiques, independentment del disseny experimental utilitzat.

**Resposta correcta: b**

---

### Pregunta 5
Una startup vol crear una **Persona** per al seu producte de meditació. L'equip disposa de:
- 20 entrevistes amb usuaris potencials
- Dades demogràfiques de 500 enquestats
- Anàlisi de la competència (benchmarking)

Quina de les següents aproximacions a la creació de la Persona és **MÈTODOLÒGICAMENT CORRECTA**?

a) Crear una Persona basada exclusivament en les entrevistes qualitatives, ja que aquestes proporcionen la profunditat necessària per capturar motivacions i frustracions reals.

b) Crear una Persona combinant dades qualitatives (entrevistes) i quantitatives (enquestes) mitjançant triangulació, assegurant que l'arquetip representi patrons reals i no només anècdotes individuals.

c) Crear múltiples Persones (una per cada segment demogràfic identificat a les enquestes) perquè una sola Persona no pot capturar tota la diversitat d'usuaris.

d) Crear una proto-persona inicial basada en hipòtesis de l'equip, validar-la amb les entrevistes, i després refinar-la amb les dades quantitatives de les enquestes.

**Resposta correcta: b**

> **Explicació**: La **b** és la resposta més adequada perquè amb dades ja recollides, la triangulació directa (combinar qualitatives + quantitatives) és el procés més eficient i el que els apunts recomanen: "mai confiem en una sola tècnica" per compensar errors d'autoinforme. L'opció **d** descriu un procés vàlid (hipòtesi → validació → refinament) però és menys òptim en aquest context, ja que les proto-persones es defineixen com a representacions "abans de tenir dades empíriques reals". L'opció **a** és incorrecta perquè viola la triangulació. L'opció **c** confon Persones amb segments demogràfics.

---

### Pregunta 6
Un sistema de gestió hospitalària ha de mostrar informació crítica d'un pacient a la pantalla d'urgències: al·lèrgies, medicació actual, constants vitals i historial recent. La pantalla actual mostra tot en una sola vista sense jerarquia visual.

Aplicant la **teoria de la Gestalt** i els principis de **jerarquia visual**, quina reorganització seria **MÉS EFECTIVA**?

a) Agrupar la informació per proximitat (principi de Gestalt) segons la seva naturalesa: al·lèrgies i medicació en un bloc (informació farmacològica), constants vitals en un altre (informació fisiològica), i historial en un tercer (informació contextual), usant espai en blanc per separar els grups.

b) Utilitzar el principi de semblança de Gestalt assignant el mateix color a tota la informació mèdica per crear unitat visual, i destacar només les al·lèrgies en vermell per la seva criticitat.

c) Aplicar el patró de lectura en Z per posicionar la informació més crítica (al·lèrgies) a la cantonada superior esquerra, les constants vitals al centre, i la medicació a la cantonada inferior dreta.

d) Implementar un sistema de pestanyes (tabs) per permetre a l'usuari accedir a cada tipus d'informació de manera seqüencial, reduint la càrrega cognitiva segons la Llei de Miller.

**Resposta correcta: a**

---

### Pregunta 7
En una avaluació heurística d'una plataforma educativa, tres experts independents identifiquen problemes d'usabilitat. L'Expert A troba 15 problemes, l'Expert B en troba 12, i l'Expert C en troba 18. Només 8 problemes són identificats pels tres experts.

Quina conclusió és **MÉS VÀLIDA** sobre aquest resultat?

a) L'Expert C és el més rigorós perquè ha detectat més problemes, i per tant la seva avaluació hauria de tenir més pes en l'informe final.

b) La baixa superposició (8/18 = 44%) demostra que les avaluacions heurístiques són subjectives i poc fiables, i que caldria haver fet tests amb usuaris reals des del principi.

c) La variabilitat entre experts és esperada en avaluacions heurístiques; per això es recomana que múltiples experts facin avaluacions independents i després posin en comú els resultats per obtenir una visió més completa (com indica Nielsen, 3-5 experts detecten ~75% dels problemes).

d) Els 8 problemes comuns són els únics que s'han de solucionar, ja que són els únics validats per consens d'experts; els altres són falsos positius.

**Resposta correcta: c**

---

### Pregunta 8
Una aplicació de navegació GPS per a conductors ha de decidir com presentar les indicacions de gir. Les opcions són:
- **Opció 1**: Text ("Giri a la dreta en 200 metres")
- **Opció 2**: Veu sintètica que llegeix el text
- **Opció 3**: Icona visual amb fletxa i distància

Considerant els **perfils d'accessibilitat** (visual, auditiu, cognitiu) i el **context d'ús** (conductor distret), quina combinació és **MÉS INCLUSIVA**?

a) Utilitzar només l'Opció 2 (veu) perquè el conductor no ha de desviar la mirada de la carretera, i els usuaris amb discapacitat visual poden rebre la informació.

b) Combinar les Opcions 1 i 3 (text + icona) perquè els usuaris amb discapacitat auditiva puguin veure la informació, i afegir l'Opció 2 (veu) com a complement per a situacions on la mirada està ocupada.

c) Utilitzar només l'Opció 3 (icona) perquè és la més ràpida de processar visualment i redueix la càrrega cognitiva segons la Llei de Hick-Hyman.

d) Oferir les tres opcions simultàniament i permetre a l'usuari configurar quines vol activar, seguint el principi de flexibilitat i eficiència d'ús (Heurística H7 de Nielsen).

**Resposta correcta: d**

---

### Pregunta 9
Un equip de disseny està creant un **User Journey Map** per a un servei de subscripció de cafè. Han identificat les següents etapes: Descobriment → Registre → Personalització → Primera comanda → Entrega → Re-comanda.

A l'etapa de "Personalització", detecten que els usuaris abandonen el procés en un 45% dels casos. Segons els principis de **gamificació** i **disseny persuasiu**, quina intervenció seria **MÉS EFECTIVA** per reduir l'abandonament?

a) Simplificar el procés de personalització a només 2 preguntes clau, aplicant la Llei de Hick-Hyman per reduir el nombre de decisions.

b) Implementar una barra de progrés visual i missatges de retroalimentació positiva ("Ja tens el 60% completat!") per generar sensació d'avenç i compromís (patró persuasiu de feedback).

c) Oferir una recomanació per defecte basada en les preferències més populars, permetent a l'usuari modificar-la si vol, aplicant el principi de "reconeixement per sobre del record" (Llei de Miller).

d) Totes les anteriors són vàlides i complementàries: simplificar (A), motivar amb feedback (B), i facilitar amb valors per defecte (C).

**Resposta correcta: d**

---

### Pregunta 10
En un **test A/B** per a una landing page, la Versió A té una taxa de conversió del 12% (n=500) i la Versió B té una taxa del 15% (n=500). La diferència és estadísticament significativa (p < 0.05).

Quina de les següents interpretacions és **MÉS CORRECTA** des de la perspectiva de l'avaluació d'usabilitat?

a) La Versió B és definitivament superior i s'hauria d'implementar immediatament, ja que la significació estadística demostra que és objectivament millor.

b) La significació estadística indica que la diferència probablement no és deguda a l'atzar, però no ens diu per què la Versió B funciona millor; caldria complementar amb tests d'usabilitat qualitatius per entendre els motius subjacents.

c) El test A/B és una mètrica sumativa que mesura el "què" però no el "per què"; per tant, els resultats són menys valuosos que una avaluació formativa amb pocs usuaris que identifiqui problemes específics.

d) La mida mostral de 500 per variant és excessiva per a un test A/B; amb 50 usuaris per variant s'hauria obtingut la mateixa informació amb menys cost.

**Resposta correcta: b**

---

### Pregunta 11
Una empresa vol implementar **intel·ligència artificial generativa (IAG)** en el seu procés de disseny UX. Proposen tres usos:
1. Generar Persones sintètiques basades en dades de clients
2. Analitzar transcripcions de 100 entrevistes per identificar temes emergents
3. Simular tests d'usabilitat amb "usuaris sintètics" abans de fer tests reals

Segons les directrius sobre **IAG en investigació d'usuaris**, quina combinació d'usos és **ÈTICAMENT I METODOLÒGICAMENT ACCEPTABLE**?

a) Només l'ús 2 (anàlisi de transcripcions), perquè la IAG és adequada per processar grans volums de dades qualitatives i identificar patrons, però no per substituir usuaris reals (usos 1 i 3).

b) Els usos 1 i 2 són acceptables, però no el 3, perquè les Persones sintètiques poden ser útils com a hipòtesis inicials, però els tests d'usabilitat requereixen usuaris reals per capturar emocions i comportaments autèntics.

c) Tots tres usos són acceptables si es validen posteriorment amb usuaris reals, ja que la IAG pot accelerar el procés de disseny sempre que no substitueixi completament la recerca amb humans.

d) Només l'ús 1 és acceptable, perquè les Persones sintètiques són hipòtesis que es poden validar, però l'anàlisi automàtica de dades (ús 2) pot introduir biaixos algorítmics, i els tests sintètics (ús 3) són èticament problemàtics.

**Resposta correcta: a**

---

### Pregunta 12
Un dissenyador proposa aplicar el **patró de disseny "Infinite Scroll"** en una aplicació de notícies. Un company argumenta que això pot ser un **patró fosc (Deceptive Pattern)** perquè:

a) Viola el principi de visibilitat de l'estat del sistema (Heurística H1 de Nielsen), ja que l'usuari no sap quanta informació hi ha ni on es troba dins del contingut.

b) Pot generar addicció i consum excessiu de contingut, aprofitant-se de biaixos cognitius com la "por a perdre's alguna cosa" (FOMO), sense que l'usuari en sigui conscient.

c) Ambdues afirmacions (a i b) són correctes i complementàries: el patró viola principis d'usabilitat (H1) i pot ser manipulador si no ofereix controls clars per aturar-se.

d) Cap de les anteriors; l'infinite scroll és un patró legítim que millora l'experiència en dispositius mòbils i no és inherentment manipulador si s'implementa correctament.

**Resposta correcta: c**

---

### Pregunta 13
En dissenyar un formulari de registre per a una aplicació de salut mental, has de decidir entre:
- **Format 1**: Totes les preguntes en una sola pàgina amb scroll
- **Format 2**: Wizard de 5 passos amb una pregunta per pas

Considerant la **Llei de Miller**, els **trade-offs de disseny**, i que l'usuari objectiu pot estar en un estat emocional vulnerable, quina opció és **MÉS ADEQUADA**?

a) Format 1 (una pàgina) perquè permet a l'usuari veure tot el que se li demana d'un cop, reduint la incertesa i donant-li control total sobre el procés (principi de control i llibertat de l'usuari, H3 de Nielsen).

b) Format 2 (wizard) perquè redueix la càrrega cognitiva presentant només una pregunta a la vegada (respectant els 7±2 elements de Miller), i proporciona una sensació de progrés que pot ser motivadora per a usuaris vulnerables.

c) Format 1 amb una barra de progrés a la part superior per combinar els beneficis de veure tot el contingut (control) amb la retroalimentació de progrés (feedback).

d) Format 2 amb l'opció de saltar passos no obligatoris, per equilibrar la reducció de càrrega cognitiva amb la flexibilitat i control de l'usuari.

**Resposta correcta: d**

---

### Pregunta 14
Una empresa tecnològica vol avaluar l'accessibilitat de la seva web corporativa. Han contractat un auditor que utilitza les **WCAG 2.1** com a referència. L'auditor identifica que la web no compleix amb el principi **"Robust"** de POUR.

Quina de les següents deficiències és **MÉS PROBABLE** que hagi detectat?

a) Les imatges no tenen text alternatiu (alt text), fent que els lectors de pantalla no puguin descriure-les a usuaris amb discapacitat visual.

b) Els colors utilitzats no tenen suficient contrast, dificultant la lectura per a usuaris amb baixa visió o daltonisme.

c) El codi HTML no segueix els estàndards del W3C, amb etiquetes mal tancades i estructura semànticament incorrecta, fent que algunes tecnologies d'ajuda no puguin interpretar correctament el contingut.

d) Els formularis no tenen etiquetes clares ni missatges d'error descriptius, dificultant la comprensió per a usuaris amb discapacitat cognitiva.

**Resposta correcta: c**

---

### Pregunta 15
En un projecte de disseny d'una app de transport públic, l'equip ha creat un **Mapa d'Empatia** per a la Persona "Maria, 35 anys, mare treballadora". A la secció "THINKS" (Pensa), han escrit: "Espero que l'app sigui fiable perquè no puc permetre'm arribar tard a recollir els nens".

Aquesta entrada il·lustra quin concepte fonamental del disseny centrat en l'usuari?

a) Una **frustració** (Pain) relacionada amb la por a la impuntualitat del servei.

b) Una **motivació** subjacent (necessitat de fiabilitat) que va més enllà del desig superficial (arribar a temps).

c) Un **biaix cognitiu** de l'equip de disseny, que està projectant les seves pròpies pors en la Persona.

d) Un **requeriment funcional** que s'hauria de traduir en una funcionalitat específica de l'app (notificacions en temps real).

**Resposta correcta: b**

---

### Pregunta 16
Un equip de disseny està aplicant el **Design Thinking** per resoldre el problema de la solitud en persones grans. A la fase de **Definició**, han generat la següent pregunta HMW (How Might We):

"Com podríem nosaltres crear oportunitats de connexió social significativa per a persones grans que viuen soles?"

Quina de les següents crítiques a aquesta pregunta HMW és **MÉS VÀLIDA**?

a) La pregunta és massa àmplia i no especifica el canal de connexió (digital, presencial, telefònic), fent que la fase d'Ideació serà poc focalitzada.

b) La pregunta assumeix que les persones grans volen "connexió social", sense haver validat que aquesta sigui realment la seva necessitat principal (podria ser autonomia, seguretat, etc.).

c) La pregunta està ben formulada perquè és oberta, centrada en l'usuari, i invita a múltiples solucions sense presuposar la tecnologia com a única via.

d) La pregunta hauria d'haver-se formulat a la fase d'Empatia, no a la fase de Definició, perquè requereix una comprensió profunda de l'usuari.

**Resposta correcta: c**

---

### Pregunta 17
En avaluar la **usabilitat** d'una aplicació de comerç electrònic, has mesurat les següents mètriques amb 10 usuaris:
- Taxa d'èxit: 85%
- Temps mitjà per completar compra: 4.2 minuts
- Errors per usuari: 1.3
- Puntuació SUS: 72

Segons els **estàndards de la indústria** i les **5Es de la usabilitat**, quina interpretació és **MÉS ACURADA**?

a) L'aplicació és usable perquè la puntuació SUS (72) està per sobre del llindar d'acceptabilitat (68-70), i la taxa d'èxit (85%) indica bona eficàcia.

b) L'aplicació té problemes d'eficiència perquè 4.2 minuts per completar una compra és excessiu comparat amb l'estàndard de la indústria (2-3 minuts), tot i que l'eficàcia és acceptable.

c) Cal analitzar les mètriques en conjunt: l'eficàcia és bona (85%), l'eficiència és millorable (4.2 min), la tolerància a l'error és acceptable (1.3 errors/usuari), i la satisfacció és acceptable (SUS 72); per tant, l'aplicació és usable però amb marge de millora en eficiència.

d) Les mètriques són contradictòries: un SUS de 72 suggereix bona usabilitat, però 1.3 errors per usuari indica problemes de tolerància a l'error que haurien de baixar el SUS; per tant, alguna de les mètriques no és fiable.

**Resposta correcta: c**

---

### Pregunta 18
Una empresa vol implementar **gamificació** en la seva app de fitness per augmentar la retenció d'usuaris. Segons el **Gamification Model Canvas** i els **tipus de jugador de Bartle**, han identificat que la majoria dels seus usuaris són "Socialitzadors" (Socializers).

Quina mecànica de joc seria **MÉS EFECTIVA** per a aquest perfil?

a) Rànquings individuals i competicions per demostrar superioritat sobre altres usuaris (motivació per l'èxit i el reconeixement).

b) Reptes col·laboratius on els usuaris puguin formar equips, compartir progressos i animar-se mútuament (motivació per la connexió social).

c) Sistemes de punts i insígnies per desbloquejar contingut exclusiu (motivació per la col·lecció i l'exploració).

d) Narratives immersives on l'usuari sigui el protagonista d'una història d'aventura (motivació per la fantasia i l'evasió).

**Resposta correcta: b**

---

### Pregunta 19
En un **passeig cognitiu (Cognitive Walkthrough)** d'una app de banca, l'expert avalua la tasca "Fer una transferència". Al pas 3 ("Seleccionar el beneficiari"), es pregunta: "Entendrà l'usuari que ha de fer aquesta acció?"

Quina de les següents condicions faria que la resposta fos **NEGATIVA**?

a) El botó "Afegir beneficiari" és petit i està situat a la part inferior de la pantalla, fora de l'àrea d'atenció visual (violant la Llei de Fitts).

b) L'usuari no sap que necessita tenir el beneficiari registrat prèviament abans de fer la transferència, perquè el sistema no ho indica clarament (problema de visibilitat de l'estat del sistema).

c) Ambdues condicions (a i b) poden fer que l'usuari no entengui que ha de fer aquesta acció: la primera per problemes de visibilitat (Llei de Fitts), la segona per manca de feedback i affordances (principis de Norman).

d) Cap de les anteriors; el passeig cognitiu només avalua si l'usuari sap què fer, no si la interfície és eficient o usable.

**Resposta correcta: c**

---

### Pregunta 20
Una startup de salut digital ha de decidir entre dues estratègies per validar el seu MVP (Minimum Viable Product):
- **Estratègia A**: Fer un test d'usabilitat amb 5 usuaris per identificar problemes abans del llançament
- **Estratègia B**: Llançar el producte i monitorar mètriques d'ús durant 3 mesos per detectar problemes

Segons els principis d'**avaluació formativa vs. sumativa** i la **ISO 9241-210**, quina recomanació és **MÉS ADEQUADA**?

a) Estratègia A perquè l'avaluació formativa (durant el disseny) permet identificar i corregir problemes abans que afectin usuaris reals, seguint el principi de "disseny impulsat per l'avaluació" de la ISO 9241-210.

b) Estratègia B perquè l'avaluació sumativa (després del llançament) proporciona dades reals d'ús en context, i amb 5 usuaris (Estratègia A) no es poden detectar tots els problemes.

c) Combinar ambdues estratègies: fer un test formatiu amb 5 usuaris (Estratègia A) per detectar el 80% dels problemes, llançar el producte, i després fer monitoratge sumatiu (Estratègia B) per detectar problemes a llarg termini i validar en context real.

d) Cap de les dues; la ISO 9241-210 requereix avaluació contínua durant tot el cicle de vida del producte, no només en moments específics.

**Resposta correcta: c**

---

## PART II: Preguntes de Desenvolupament (4 preguntes)

### Pregunta 21
**Cas pràctic**: Una empresa de streaming musical vol redissenyar la seva funció de "descobriment de música". Han detectat que els usuaris escolten sempre els mateixos artistes i no exploren noves recomanacions.

**Tasca**: Aplicant els conceptes de **Llei de Hick-Hyman**, **principis de Norman**, **disseny emocional** i **gamificació**, proposa una solució de disseny que:
1. Redueixi la càrrega cognitiva de triar entre milers de cançons
2. Motivi l'usuari a explorar nou contingut
3. Generi una experiència emocional positiva

**Resposta model**:

La solució hauria d'integrar múltiples principis:

**1. Reducció de càrrega cognitiva (Llei de Hick-Hyman + Llei de Miller)**:
- Implementar un sistema de "recomanacions curades" que presenti només 5-7 opcions per categoria (respectant els 7±2 de Miller)
- Organitzar les recomanacions per estats d'ànim o activitats ("Per entrenar", "Per relaxar-te", "Per concentrar-te") en lloc de gèneres genèrics
- Usar el principi de "reconeixement per sobre del record": mostrar portades d'àlbums i fragments de 30 segons perquè l'usuari pugui decidir sense haver de recordar

**2. Motivació per explorar (Gamificació + Disseny persuasiu)**:
- Sistema de "descobertes" amb insígnies per escoltar artistes nous (patró de col·lecció)
- Reptes setmanals: "Descobreix 3 artistes nous aquesta setmana i guanya punts"
- Barra de progrés que mostri "Has descobert X% de la música del teu gènere preferit"
- Element social: compartir descobertes amb amics (motivació per als socialitzadors)

**3. Experiència emocional (Disseny emocional de Norman)**:
- **Nivell visceral**: Disseny visual atractiu amb animacions suaus quan es descobreix un nou artista
- **Nivell conductual**: Feedback immediat ("Bona elecció! Aquest artista s'assembla a X que t'agrada") i facilitat per tornar a escoltes anteriors
- **Nivell reflexiu**: Missatges que reforcin la identitat de l'usuari com a "explorador musical" ("Ets dels primers a descobrir aquest artista!")

**Implementació concreta**: Una pantalla "Descobreix avui" amb 6 targetes grans (3 artistes nous + 3 cançons recomanades), amb botons de "M'agrada" i "No m'agrada" per refinar l'algoritme, i un comptador de descobertes setmanals.

---

### Pregunta 22
**Cas pràctic**: Estàs dissenyant un sistema de check-in online per a una aerolínia. Has de crear un **User Journey Map** complet i identificar **3 pain points crítics** amb les seves corresponents **oportunitats de millora**.

**Tasca**:
1. Defineix les etapes del viatge de l'usuari (mínim 5 etapes)
2. Per a cada etapa, identifica accions, touchpoints, emocions i pain points
3. Proposa 3 oportunitats de millora concretes amb els principis de disseny que les justifiquen

**Resposta model**:

**User Journey Map - Check-in online**

**Etapa 1: Preparació (24h abans del vol)**
- **Accions**: Rebre email de recordatori, obrir app/web de l'aerolínia
- **Touchpoints**: Email, app mòbil, web
- **Emocions**: Expectativa, lleugera ansietat
- **Pain points**: No recordar on està el localitzador, no saber quins documents calen

**Etapa 2: Inici del check-in**
- **Accions**: Introduir localitzador i cognom, validar identitat
- **Touchpoints**: Formulari web/app
- **Emocions**: Frustració si no troba el localitzador, alleujament si funciona
- **Pain points**: Formulari confús, errors de validació poc clars

**Etapa 3: Selecció de seient**
- **Accions**: Veure mapa d'avion, triar seient, confirmar
- **Touchpoints**: Mapa interactiu
- **Emocions**: Estrès si els seients preferits estan ocupats, satisfacció si troba un de bo
- **Pain points**: Mapa difícil de navegar, preus dels seients no clars

**Etapa 4: Serveis addicionals**
- **Accions**: Afegir equipatge, menjar especial, assegurança
- **Touchpoints**: Formularis de selecció
- **Emocions**: Confusió per l'excés d'opcions, frustració pels costos addicionals
- **Pain points**: Upselling agressiu, informació poc clara sobre equipatge

**Etapa 5: Confirmació i targeta d'embarcament**
- **Accions**: Revisar dades, confirmar, descarregar targeta
- **Touchpoints**: Pantalla de confirmació, email, wallet del mòbil
- **Emocions**: Alleujament, satisfacció si tot va bé
- **Pain points**: No saber on es desa la targeta, por de perdre-la

**3 Oportunitats de millora**:

**1. Oportunitat: Sistema de recuperació de localitzador**
- **Principi**: Visibilitat de l'estat del sistema (H1 de Nielsen) + Disseny inclusiu
- **Solució**: En l'email de recordatori, incloure un botó directe "Fer check-in ara" que ja porti les credencials pre-omplertes. Si l'usuari accedeix manualment, oferir recuperar el localitzador via email/SMS amb un sol clic.
- **Justificació**: Redueix la fricció inicial i ajuda a usuaris amb problemes de memòria (Llei de Miller: reconeixement per sobre del record).

**2. Oportunitat: Mapa d'assentaments simplificat**
- **Principi**: Llei de Fitts (botons grans i propers) + Jerarquia visual + Disseny emocional (nivell conductual)
- **Solució**: Mapa amb només 3 categories de seients (finestra, passadís, central) amb colors clars, botons grans per seleccionar, i indicador de "seients lliures" en temps real. Afegir recomanació "Et recomanem el seient 14A perquè t'agrada la finestra".
- **Justificació**: Redueix la càrrega cognitiva (Hick-Hyman: menys opcions = decisió més ràpida) i genera confiança (disseny emocional).

**3. Oportunitat: Confirmació amb accions clares**
- **Principi**: Feedback immediat + Control i llibertat de l'usuari (H3 de Nielsen) + Disseny inclusiu
- **Solució**: Pantalla de confirmació amb checklist visual de "Fet!" per a cada pas completat, botó gran "Descarregar targeta d'embarcament" i opció "Enviar al meu wallet". Missatge clar: "La teva targeta també està al teu email i la pots recuperar des de 'Els meus viatges'".
- **Justificació**: Proporciona feedback (principi de Norman), dóna control (l'usuari sap on trobar la targeta si la perd), i és inclusiu (múltiples vies d'accés).

---

### Pregunta 23
**Cas pràctic**: Una universitat vol millorar l'accessibilitat de la seva plataforma d'e-learning. Has de fer una **auditoria d'accessibilitat** basada en les **WCAG 2.1** i els **principis POUR**.

**Tasca**:
1. Explica què avalua cadascun dels 4 principis POUR
2. Identifica 4 problemes d'accessibilitat comuns (un per cada principi) en plataformes d'e-learning
3. Proposa solucions tècniques concretes per a cada problema

**Resposta model**:

**1. Els 4 principis POUR**:

**Perceptible**: El contingut ha de ser presentat de manera que l'usuari pugui percebre'l amb almenys un dels seus sentits (vista, oïda, tacte). No pot ser invisible a tots els sentits.

**Operable**: Els components de la interfície i la navegació han de ser manejables. L'usuari ha de poder interactuar amb tots els elements (teclat, ratolí, dispositius d'ajuda).

**Comprensible**: La informació i el funcionament de la interfície han de ser clars i fàcils d'entendre. L'usuari ha de poder comprendre tant el contingut com com utilitzar el sistema.

**Robust**: El contingut ha de ser prou robust per ser interpretat de manera fiable per una gran varietat d'agents d'usuari, incloent tecnologies d'ajuda (lectors de pantalla, magnificadors, etc.).

**2. Problemes comuns i solucions**:

**Problema 1 (Perceptible)**: Els vídeos de les classes no tenen subtítols ni transcripció.
- **Impacte**: Usuaris amb discapacitat auditiva no poden accedir al contingut. Usuaris en entorns sorollosos o sense auriculars també es veuen afectats (discapacitat situacional).
- **Solució tècnica**: Implementar subtítols automàtics amb revisió manual per garantir precisió. Oferir transcripció completa en text descarregable. Usar el tag `<track>` en HTML5 per als subtítols.
- **WCAG**: Compleix el criteri 1.2.2 (Subtítols per a contingut pregravat).

**Problema 2 (Operable)**: Els qüestionaris interactius només es poden completar amb ratolí; no funcionen amb teclat.
- **Impacte**: Usuaris amb discapacitat motora que depenen del teclat o dispositius d'ajuda no poden completar les activitats.
- **Solució tècnica**: Assegurar que tots els elements interactius (botons, checkboxes, drag-and-drop) tinguin l'atribut `tabindex` correcte i es puguin activar amb Enter/Space. Per a drag-and-drop, oferir una alternativa amb selecció per teclat. Afegir `aria-labels` per descriure l'acció.
- **WCAG**: Compleix el criteri 2.1.1 (Teclat).

**Problema 3 (Comprensible)**: Els missatges d'error en els formularis d'entrega de treballs són genèrics ("Error en l'enviament") i no indiquen com solucionar-los.
- **Impacte**: Usuaris amb discapacitat cognitiva (o qualsevol usuari estressat) no entenen què han de fer per corregir l'error.
- **Solució tècnica**: Missatges d'error específics i constructius: "El fitxer supera els 10MB permesos. Comprimeix-lo o selecciona un fitxer més petit". Usar `aria-live="polite"` perquè els lectors de pantalla anunciïn l'error. Posicionar el focus automàticament al camp amb error.
- **WCAG**: Compleix el criteri 3.3.1 (Identificació d'errors) i 3.3.3 (Suggeriments en cas d'error).

**Problema 4 (Robust)**: El contingut està construït amb HTML semànticament incorrecte: `<div>` per a capçaleres en lloc de `<h1>`, `<h2>`, etc., i taules per a layout en lloc de CSS.
- **Impacte**: Els lectors de pantalla no poden interpretar correctament l'estructura del document, fent que la navegació per capçaleres sigui impossible per a usuaris amb discapacitat visual.
- **Solució tècnica**: Reescriure el codi usant HTML5 semàntic: `<header>`, `<nav>`, `<main>`, `<article>`, `<aside>`, `<footer>`. Usar capçaleres jeràrquiques correctament (`<h1>` per al títol principal, `<h2>` per a seccions, etc.). Validar el codi amb el W3C Validator.
- **WCAG**: Compleix el criteri 4.1.1 (Parsing) i 1.3.1 (Informació i relacions).

---

### Pregunta 24
**Cas pràctic**: Una empresa de videojocs vol avaluar la usabilitat del seu nou joc mòbil abans del llançament. Disposen d'un pressupost limitat i han de triar entre tres mètodes d'avaluació:
- **Mètode A**: Test d'usabilitat en laboratori amb 8 usuaris (cost: 5.000€)
- **Mètode B**: Avaluació heurística amb 3 experts (cost: 2.000€)
- **Mètode C**: Test A/B amb 1.000 usuaris beta (cost: 3.000€)

**Tasca**:
1. Compara els tres mètodes segons: tipus d'avaluació (formativa/sumativa), dades que proporcionen (qualitatives/quantitatives), i limitacions
2. Recomana una combinació òptima dels tres mètodes (o un subconjunt) justificada amb els principis d'avaluació
3. Explica com aplicaries el concepte de **triangulació** en la teva recomanació

**Resposta model**:

**1. Comparació dels mètodes**:

**Mètode A: Test d'usabilitat en laboratori (8 usuaris)**
- **Tipus**: Avaluació formativa (durant el disseny, per millorar)
- **Dades**: Qualitatives (observació de comportaments, pensament en veu alta, problemes identificats) + quantitatives (taxa d'èxit, temps, errors)
- **Limitacions**: Cost elevat, mostra petita (però suficient per detectar ~80% dels problemes), context artificial (laboratori vs. ús real), requereix moderador expert
- **Fortaleses**: Proporciona insights profunds sobre el "per què" dels problemes, permet iterar ràpidament

**Mètode B: Avaluació heurística (3 experts)**
- **Tipus**: Avaluació formativa per inspecció (sense usuaris reals)
- **Dades**: Qualitatives (llista de problemes d'usabilitat amb severitat)
- **Limitacions**: Subjectivitat dels experts, no captura emocions reals ni comportaments inesperats, pot passar per alt problemes específics del context d'ús
- **Fortaleses**: Ràpida i barata, detecta problemes abans de fer tests amb usuaris, àmplia cobertura de principis de disseny

**Mètode C: Test A/B amb 1.000 usuaris beta**
- **Tipus**: Avaluació sumativa (per comparar versions i prendre decisions)
- **Dades**: Quantitatives (mètriques d'ús, taxes de conversió, retenció, etc.)
- **Limitacions**: Mesura el "què" però no el "per què", requereix tenir dues versions implementades, no detecta problemes d'usabilitat específics sinó només diferències globals
- **Fortaleses**: Dades reals en context, mostra gran (estadísticament significativa), permet prendre decisions basades en evidència

**2. Combinació òptima recomanada**:

**Recomanació**: Aplicar els tres mètodes en seqüència, optimitzant el pressupost:

**Fase 1 (Setmana 1-2): Mètode B - Avaluació heurística (2.000€)**
- **Objectiu**: Detectar problemes d'usabilitat evidents abans de fer tests amb usuaris
- **Justificació**: Segons Nielsen, 3-5 experts detecten ~75% dels problemes. Això permetrà corregir errors greus abans d'invertir en tests amb usuaris, estalviant temps i diners.
- **Resultat esperat**: Llista de 20-30 problemes amb severitat, que es corregeixen immediatament.

**Fase 2 (Setmana 3-4): Mètode A - Test d'usabilitat en laboratori (5.000€)**
- **Objectiu**: Validar que els problemes detectats pels experts s'han solucionat i detectar problemes subtils que els experts no van veure
- **Justificació**: Amb 5-8 usuaris es detecta el 80% dels problemes restants (segons Nielsen i Landauer). El context controlat permet observar comportaments i entendre el "per què".
- **Resultat esperat**: Identificació de 5-10 problemes nous, amb insights qualitatius per solucionar-los.

**Fase 3 (Setmana 5-8): Mètode C - Test A/B amb usuaris beta (3.000€)**
- **Objectiu**: Validar que la versió final funciona en context real i comparar amb la versió anterior (si n'hi ha)
- **Justificació**: Les dades quantitatives confirmen que les millores d'usabilitat es tradueixen en millors mètriques de negoci (retenció, temps de joc, compres).
- **Resultat esperat**: Evidència estadística que la versió millorada és superior, amb dades per presentar a stakeholders.

**Cost total**: 10.000€ (pressupost complet utilitzat de manera òptima)

**3. Triangulació aplicada**:

La **triangulació** és el principi de combinar múltiples mètodes o fonts de dades per validar els resultats i obtenir una visió més completa. En aquest cas:

**Triangulació de mètodes**:
- **Experts (Mètode B)** detecten problemes basant-se en principis de disseny
- **Usuaris reals (Mètode A)** validen o refuten aquests problemes amb comportaments observats
- **Dades massives (Mètode C)** confirmen que les solucions implementades funcionen a gran escala

**Triangulació de dades**:
- **Qualitatives dels experts** (llista de problemes) + **Qualitatives dels usuaris** (observacions) + **Quantitatives del test A/B** (mètriques) = Visió completa del "què", "per què" i "quant".

**Triangulació de perspectives**:
- **Perspectiva tècnica** (experts en usabilitat) + **Perspectiva de l'usuari** (comportaments reals) + **Perspectiva de negoci** (mètriques de rendiment) = Decisions de disseny informades i equilibrades.

**Benefici de la triangulació**: Si un problema és identificat pels experts, observat en el test amb usuaris, i es tradueix en una millora mètrica al test A/B, tenim una **validació robusta** que justifica la inversió en solucionar-lo. Si només un mètode el detecta, cal investigar més abans d'actuar.

---

## Notes finals

Aquest tipus test està dissenyat per avaluar:
- **Comprensió profunda** dels conceptes (no només definicions)
- **Aplicació pràctica** dels principis en casos reals
- **Integració** de múltiples conceptes en una sola resposta
- **Pensament crític** per identificar la millor opció entre diverses vàlides

Les preguntes de desenvolupament requereixen:
- **Síntesi** de conceptes de diferents temes
- **Justificació** amb principis teòrics
- **Propostes concretes** i implementables
- **Visió holística** del procés de disseny UX
