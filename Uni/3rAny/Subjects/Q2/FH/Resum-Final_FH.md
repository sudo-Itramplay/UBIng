---
id: Resum-Final_FH
aliases: []
tags:
  - tipus/parcial
  - assignatura/FH
assignatura: FH
data: "2026-05-27"
parcial: Final (2n Parcial)
---

# Resum Final — Factors Humans (2n Parcial)

> Contingut complet posterior al Parcial 1: [[Disseny]], [[Accessibilitat]], [[Accessibilitat VUE]], [[Avaluació del Disseny]].

---

# 1. Disseny

### 1. Fonaments i Introducció als Principis de Disseny

L'objectiu principal d'aquesta fase és guiar el procés de creació de productes centrats en l'usuari mitjançant directrius clares. Com a enginyers, hem d'entendre que el disseny no és una capa estètica final, sinó una part integral de la conceptualització i construcció que desemboca en un prototip funcional. Els principis treballen sobre dos eixos:

- **Les 5Es de la Usabilitat:**
  - Eficiència (_Efficiency_),
  - Eficàcia (_Efficacy_),
  - Facilitat d'aprenentatge (_Easy to Learn_),
  - Tolerància a l'error (_Error tolerance_)
  - Atractiu (_Engaging_).
- **Experiència d'Usuari (UX):** Inclou aspectes més profunds com la part emocional, la credibilitat, la identitat i el significat que l'usuari dona a la interacció. La usabilitat és només una part continguda dins de l'ampli espectre de la UX.

### 2. Lleis de la Interacció Humà-Computador (HCI)

Les lleis de HCI són models empírics basats en la psicologia cognitiva que prediuen el comportament humà davant la tecnologia.

Hi ha 3:

- **Llei de Fitts (Efficiency):**
  - El temps per assolir un objectiu depèn de la distància fins a ell i de la seva grandària ($MT=a+b \cdot \log_2(D/W+1)$).
  - Implica dissenyar botons grans i propers a l'àrea d'atenció ("prime pixel") i aprofitar els "màgic píxels" de les cantonades del sistema operatiu.
  - ![[Pasted image 20260502114259.png]]
  - ![[Pasted image 20260502114312.png]]
  - ![[Pasted image 20260502114322.png]]
- **Llei de Hick-Hyman:**
  - El temps per prendre una decisió augmenta logàrticament amb el nombre d'opcions ($RT=a+b \cdot \log_2(n)$).
  - Per tant, la simplicitat és clau per reduir el temps de reacció.
- **Llei de Miller:**
  - La memòria a curt termini humana només pot retenir **$7 \pm 2$ elements**.
  - ![[Pasted image 20260502114448.png]]
  - El disseny ha de prioritzar el **reconeixement per sobre del record**:
    - utilitzant tècniques com el _chunking_ (dividir informació en unitats petites)
    - ajuda contextual (_tooltips_)
    - els _wish lists_.
    - Mostrar gestural signifiers

### 3. Principis de Disseny d'Interacció de Don Norman

Basats en l'obra de referència _The Design of Everyday Things_, aquests principis són vitals per reduir el "golf d'execució" i el "golf d'avaluació".

![[Pasted image 20260502114620.png]]

- **Visibilitat i Feedback:** Les funcions han de ser visibles i el sistema ha d'informar immediatament del resultat de cada acció (visual, àudio o tàctil).
  - Visibilitat:
    ![[Pasted image 20260502114702.png]]
    ![[Pasted image 20260502114748.png]]
  - Feedback
    - Una bona interfaç promou la discoverability (Permet ubicar millor al user)
      - Això es pot fer amb l'ús de microinteraccions (com animacions) per tal de resoldre més fàcilment les respostes de:
      - ![[Pasted image 20260502114937.png]]

- **Affordances i Signifiers:** L'atribute de l'objecte ha d'indicar com s'ha d'usar (affordance), i els senyals visuals (signifiers) han de marcar on interactuar, com els botons de "Call to action".
  - ![[Pasted image 20260502115029.png]]
- **Restriccions (Constraints) i :** Limitar les accions possibles per evitar errors
  - ![[Pasted image 20260502115056.png]]

- **Mapeig (Mapping)**: Assegurar una relació natural entre els controls i els seus efectes (ex: botons de fogons alineats amb el cremador).
  - ![[Pasted image 20260502115224.png]]
  - Això té relació amb el gulf d'execució

- **Consistència i Simplicitat:** Dissenyar elements similars per a tasques similars i minimitzar els elements per facilitar la UX (estil Google).
  - Relacionat amb Easy to Learn, Efficiency, i Error prevention

### 4. Heurístiques de Nielsen

Són 10 regles generals per al disseny d'interfícies que tot examinant ha de conèixer. Destaquen:

- **H1:** Visibilitat de l'estat del sistema (indicadors de càrrega).
- **H3:** Control i llibertat de l'usuari (opció "Desfer").
- **H5:** Prevenció d'errors (validacions en temps real).
- **H10:** Ajuda i documentació (FAQs i tutorials).

> [!tip] Segurament al examen necessitarem les 10

### 5. Disseny Visual i Teoria de la Percepció

**Referència: Diapositives 31-41**

Hi ha directrius **Generals** i directrius **Específiques** per tal d'ajudar al developer a desenvolupar les diferents pantalles

El disseny visual utilitza teories com la **Gestalt** per crear composicions efectives sota el lema "el tot és més que la suma de les parts".

- **Variables Visuals:** Posició, mida, forma, valor, color, orientació i textura s'usen per organitzar la informació i guiar l'atenció.
  - ![[Pasted image 20260502115639.png]]
- **Jerarquia Visual:** Organització per ordre d'importància (patrons F i Z). El "Squint test" (entretancar els ulls) ens ajuda a avaluar-la ràpidament.
  - ![[Pasted image 20260502115707.png]]
  - ![[Pasted image 20260502115716.png]]
- **Elements clau:** L'espai en blanc (aporta elegància i ordre), la psicologia del color (evoca emocions), la tipografia (imatge de marca) i la proporció àuria ($\Phi \approx 1.618$).
- ![[Pasted image 20260502115832.png]]

![[Pasted image 20260502115809.png]]

### 6. La Guia d'Estil: Normativa i Coherència en el Desenvolupament

La Guia d'Estil no és un simple manual d'estètica; és un document tècnic normatiu que estableix les regles del joc per garantir la consistència visual i funcional d'un sistema durant tot el seu cicle de vida.

- **Identitat de Marca (El "Core"):** Tot projecte neix d'una identitat. La guia ha de recollir l'ús correcte del logotip, definint els marges de seguretat i les variants permeses.
  - És crucial la definició de la paleta de colors, distingint entre colors primaris (d'acció), secundaris (de suport) i neutres (per a fons i estructures), incloent-hi sempre els seus valors hexadecimals o RGBA per a una implementació precisa.
- **Tipografia i To de Veu:** Aquí establim la jerarquia de lectura (H1, H2, H3, cos de text). No només triem la font per la seva llegibilitat (com Roboto o Google Sans), sinó que definim el "To de Veu".
  - Hem de decidir si el sistema parla a l'usuari de manera formal, propera o tècnica, ja que això impacta directament en el disseny emocional.
- **Elements de Disseny i Iconografia:** Es normalitza l'estil de les imatges i el set d'icones (que han de ser semànticament coherents). S'especifiquen les regles d'espaiat (_spacing_) i marges, sovint basades en una retícula o _grid_ (com el sistema d'espaiat de 8px), garantint que el _layout_ sigui equilibrat i harmoniós.
- **Components d'Interfície (UI):** Aquesta és la part més operativa per a la vostra pràctica. Heu de definir l'aspecte de tots els elements interactius: estils de botons (primaris, secundaris, deshabilitats), el disseny dels formularis (estats d'error, focus i validació) i els mecanismes de navegació (menús, _breadcrumbs_, pestanyes).

### 7. Disseny Emocional

L'enginyeria informàtica moderna ha d'apuntar al cim de la piràmide d'Aaron Walter: el producte ha de ser funcional, fiable, usable i, finalment, **plaent**. Don Norman defineix 3 nivells de reacció emocional:

1. **Visceral:** Reaccions ràpides i judicis immediats sobre l'estètica.
2. **Conductual (Behavioral):** Controlat per l'ús i l'experiència de la interacció.
3. **Reflexiu:** El nivell més alt, on l'usuari analitza el significat i l'impacte personal del producte.

![[Pasted image 20260502120438.png]]

> [!info] Com afecta el disseny emocional (positivament) a la UX?
>
> - Crea connexió amb l'usuari.
> - Millora de la usabilitat i satisfacció.
> - Impuls de la motivació i el compromís (veure diapositives de Gamificació).
> - Contribució al benestar de l'usuari.
> - Millora imatge de la marca.

### 8. Patrons de Disseny: Solucions Tècniques a Problemes Recurrents

Dins de la vostra guia d'estil i posterior construcció, aplicareu "Patrons de Disseny". Un patró és una solució que ja ha estat validada per la indústria per resoldre un problema comú de la interfície. L'ús de patrons estandarditzats facilita el "Recognition rather than Recall" de l'usuari (Llei de Miller), ja que aquest ja sap com interactuar amb elements que ha vist en altres sistemes d'èxit.

- **Patrons Generals i de Navegació:** Inclouen solucions per a controls d'entrada de dades (com els _wizards_ per a processos complexos), disseny de menús, cercadors i gestió d'errors. Per exemple, un formulari de registre no s'ha d'inventar de zero; ha de seguir el patró de _Structured Format_ per minimitzar la càrrega cognitiva.
- **Patrons Persuasius:** Són aquells que, basant-se en la psicologia del comportament, busquen guiar l'usuari cap a accions beneficioses d'una manera ètica. Inclouen mecàniques de joc (_gamificació_) i mecanismes de retroalimentació (_feedback_) que reforcen el compromís de l'usuari amb la plataforma.
- **Patrons Foscos (Deceptive Patterns):** Com a acadèmic, és el meu deure advertir-vos contra aquestes pràctiques. Són dissenys manipuladors que enganyen l'usuari (ex: subscripcions difícils de cancel·lar o costos ocults). En els vostres projectes, la transparència i l'ètica han de prevaldre; el mal disseny pot donar beneficis a curt termini, però destrueix la credibilitat de la marca a llarg termini.
- **Documentació del Patró:** Cada patró s'ha de documentar amb el resum del problema, l'exemple visual i el seu ús correcte. Això és el que eleva el vostre treball de "fer dibuixos" a fer "enginyeria d'interfícies". Consulteu recursos com _ui-patterns.com_ o les guies de _Nielsen Norman Group_ per fonamentar les vostres eleccions en la pràctica.

Finalment, la **Intel·ligència Artificial Generativa (IAG)** s'ha d'integrar com una eina per generar ràpidament arquitectures d'informació i prototips de baixa fidelitat (com amb Figma AI o Uizard), però sempre validant el feedback amb usuaris reals.

### 8. Fonts d'Inspiració i Benchmarking en el Disseny Visual

El disseny de programari d'alt nivell requereix una fase d'observació activa de les tendències de la indústria per no "reinventar la roda" de manera ineficient. Com a professionals, hem de recórrer a galeries i premis que actuen com a estàndards de qualitat:

- **Webby Awards:** Coneguts com els "Oscars de la Web", aquests premis (com els guanyadors de 2025: Antoine Wodniack o Locomotive) estableixen el límit de la innovació en _Best Home Page_ i desenvolupament creatiu. Analitzar-los permet comprendre la intersecció entre estètica d'avantguarda i funcionalitat complexa.
- **Land-book i Pageflows:** Són repositoris imprescindibles per al _benchmarking_. Mentre Land-book se centra en l'atractiu visual i la curació de galeries per a creatius, Pageflows ens permet estudiar els fluxos d'interacció (_user flows_) reals, crucial per dissenyar experiències d'usuari (UX) consistents.
- **Figma Resource Library:** Un recurs tècnic on els dissenyadors compartim les tendències de disseny web més recents. Com a estudiants, heu d'utilitzar aquestes fonts per validar si les vostres propostes visuals s'alineen amb les expectatives del mercat actual.
- **Importància del Benchmarking:** No es tracta de copiar, sinó de realitzar una recerca formal que ens ajudi a identificar patrons d'èxit en seccions específiques, portafolis o plataformes d'e-commerce, garantint que la nostra arquitectura de la informació sigui familiar i intuïtiva per a l'usuari final.

### 9. Fonaments del Disseny Emocional i Psicologia de l'Usuari

**Referència: Diapositiva 45 (i transició a la 46)**

En aquest punt del temari, fem un salt qualitatiu: passem de la construcció purament funcional a la comprensió de la psique de l'usuari. El disseny emocional és la frontera que separa un producte útil d'un producte indispensable.

- **Més enllà de la Usabilitat:** Una experiència d'usuari superior no s'atura en la facilitat d'ús. Com a enginyers, hem d'integrar el disseny persuasiu i emocional per captivar i influenciar positivament el comportament de l'usuari.
- **Connexió Cognitiva i Afectiva:** El disseny emocional busca crear una resposta psicològica que generi un vincle amb el producte digital. Això s'aconsegueix entenent com les interfícies poden evocar sentiments de seguretat, confiança o plaer.
- **Introducció a la Piràmide de Necessitats d'Aaron Walter:** Aquesta secció ens prepara per entendre que, així com existeix la piràmide de Maslow per a l'ésser humà, en UX hi ha una jerarquia de necessitats: el programari primer ha de ser funcional i fiable, però el seu èxit definitiu resideix en la seva capacitat de ser plaent (_pleasurable_).
- **Rol de l'Enginyer Informàtic:** Hem de ser capaços de traduir aquests conceptes abstractes en elements de disseny concrets: microinteraccions, tons de veu en els missatges i paletes de colors que ressonin amb el model mental de la nostra audiència objectiu.

---

# 2. Accessibilitat

## 1. Conceptes Fonamentals i Motivació

L'accessibilitat web busca que els productes digitals puguin ser utilitzats pel màxim nombre de persones, independentment de les seves capacitats.

Actualment, existeix una forta demanda de professionals formats, ja que les empreses tenen dificultats per complir els requeriments vigents.

- **Conseqüències del no-compliment**: Casos reals com **Vueling** o **Amazon** demostren que la falta d'accessibilitat pot comportar sancions legals greus i pèrdues de mercat.
- **Beneficis (L'estudi de PwC)**: El disseny inclusiu no és només ètic, sinó rendible. Els productes inclusius tripliquen o quadripliquen la seva audiència original, i el mercat demanda productes accessibles per valor de 40 bilions.
- **Discapacitats Contextuals**: Un concepte clau de l'examen. L'accessibilitat no només afecta persones amb discapacitats permanents. Existeixen situacions temporals (una infecció d'oïda) o situacionals (un conductor distret o un pare amb un nadó en braços) que es beneficien de les mateixes solucions de disseny.

- **Principis del Disseny Inclusiu**:
  1. Reconèixer l'exclusió i els nostres propis biaixos.
  2. Aprendre de la diversitat per trobar solucions creatives.
  3. Resoldre per a casos extrems beneficia a tota la població (efecte "rampa de vorera").

---

## 2. Perfils de Visió i Tecnologies d'Ajuda

La discapacitat visual impedeix percebre colors, text o imatges.

> [!warning] Quan és discapacitat?
> Es considera discapacitat quan no és corregible amb Ulleres.

- **Tipologies**:
  - **Daltonisme**: Confusió de colors (típicament vermell/verd). Perceben diferències per lluminositat.
  - **Baixa visió**: Problemes d'agudesa (text petit) o de camp visual (pèrdua de visió central o perifèrica).De vegades una excessiva lluminositat, així com parpelleigs, flaixos o moviment els poden molestar.
  - **Ceguesa**: Requereix la percepció de contingut de forma no visual.
- **Tecnologies d'ajuda (Assistive Tech)**:
  - **Magnificadors**: Com _ZoomText_, per ampliar zones de la pantalla.
  - **Lectors de pantalla**: Com _JAWS_ o _NVDA_, que transformen el text en veu.
  - **Dispositius Braille**: Línies Braille per a lectura tàctil i impressores específiques.
- **Requisits de disseny**: Ús de text real (no imatges de text), contrastos adequats, navegació completa per teclat i indicació correcta de l'idioma per als lectors de pantalla.

![[Pasted image 20260418112446.png]]

## 3. Perfils d'Audició (Oïda)

Dificulta la percepció o distinció de sons. És un col·lectiu ampli (430 milions de persones al món).

- **Conceptes clau**:
  - **Sordesa prelocutiva vs postlocutiva**:
    - **Prelocutiva**: Passa abans d'aprendre a parlar.
      - Pot afectar molt el desenvolupament del llenguatge.
  - **Oralistes vs. Signistes**: Els primers llegeixen llavis i parlen; els segons usen llengües de signes (que no són universals, ex: LSC, LSE).

![[Pasted image 20260418112705.png]]

- **Ajudes Tècniques**:
  - **Audiòfons i Implants Coclears**: Dispositius per processar el so.
  - **Bucle magnètic**: Transmet el so de la sala directament a la pròtesi de l'usuari, eliminant el soroll ambiental.
- **Requisits de disseny**: Vídeos amb subtítols, avisos visuals per a alertes sonores i oferir alternatives al contacte telefònic (xat, email).

![[Pasted image 20260418112748.png]]

---

## 4. Perfils Motors i Cognitius

Són col·lectius molt heterogenis que requereixen adaptacions físiques o de simplificació de continguts.

- **Discapacitat Motora**: Afecta l'ús del teclat, ratolí i la precisió de moviments.

      - **Ajudes**: _Eye-tracking_ (control amb la mirada), _joysticks_, sistemes de bufat o polsadors grans.

      - **Disseny**: Vincles grans i separats, evitar passos innecessaris i permetre més temps per completar tasques.

  ![[Pasted image 20260418113301.png]]

- **Discapacitat Cognitiva**: Inclou trastorns com l'autisme, dislèxia o TDAH.
  - **Dificultats**: Comprensió del llenguatge, memòria i complexitat.
  - **Estratègia COGA**: Ús de llenguatge simple, evitar textos llargs, reduir la càrrega de memòria i utilitzar mapes conceptuals.
  - **Eines**: Correctors d'estil (ex: _ClaroRead_) i lectors de text a veu per a reforç auditiu.

![[Pasted image 20260418113530.png]]

---

## 5. Persones Grans (Silver Economy)

L'envelliment de la població fa que aquest grup sigui crític. El 2050, el 30% de la població a Europa serà major de 60 anys.

- **Pluridiscapacitat lleu**: No solen tenir una discapacitat severa, sinó una suma de pèrdues lleus de visió (contrast), oïda (freqüències altes), motor (psicomotricitat fina) i cognitiu (memòria episòdica).
- **Barrera tecnològica**: Solen actuar amb menys confiança davant la tecnologia.
- **Bones pràctiques**: Facilitar l'ampliació de text, donar indicacions pas a pas molt clares i mantenir rutines de disseny conegudes.

![[Pasted image 20260418113629.png]]

## 6. L'Estàndard WCAG i els Principis POUR

Les **WCAG (Web Content Accessibility Guidelines)** són el fonament de tota regulació actual. Tot i que l'accessibilitat ideal hauria d'implicar eines d'autoria i navegadors, la llei actual se centra principalment en el **contingut**.

El WCAG Fa molt d'èmfasi en 4 principis POUR:

- **Els 4 Principis (POUR)**:
  1. **Perceptible**: El contingut s'ha de poder percebre per algun sentit (visual, sonor o tàctil). No pot ser invisible a tots els sentits de l'usuari.
  2. **Operable**: Els components de la interfície i la navegació han de ser manejables (ex: navegació només per teclat).
  3. **Comprensible**: La informació i el maneig de la interfície han de ser clars i fàcils d'entendre.
  4. **Robust**: El contingut ha de ser prou robust per ser interpretat de manera fiable per una gran varietat d'agents d'usuari (navegadors) i tecnologies d'ajuda.

---

# 3. Accessibilitat en Vue.js

## 1. Recursos i Llibreries de Suport

Per no haver de reinventar la roda, és fonamental conèixer l'ecosistema de recursos disponibles per a Vue:

- **Documentació Oficial**: La guia de bones pràctiques de Vue.
- **Vuetify**: Una llibreria basada en _Material Design_ de Google que destaca per mantenir els seus components altament actualitzats i accessibles.
- **AccessiVue**: Un recurs molt interessant creat per una ex-alumna de la facultat com a TFG. Inclou 5 components funcionals (CRUD, Cercador, Drag and Drop, Formularis i Biblioteca de recursos) amb accessibilitat nativa integrada.
- **Vue-a11y**: Comunitat amb receptes i eines específiques per a l'accessibilitat.

## 2. Navegació: Skip Links i Focus

Un dels errors més comuns en les Single Page Applications (SPA) és obligar l'usuari de teclat a tabular per tots els menús cada vegada que canvia de vista.

- **Solució**: Implementar un "Skip to main content". És un vincle directe al contingut principal que apareix al principi del document.
- **Comportament visual**: Es pot ocultar visualment i fer que només sigui visible quan rep el focus del teclat.

---

# 4. Avaluació del Disseny

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

> [!warning] Monitoreig a llarg tremini
> També continua aquest procès via insights, aquests poden tant denotar un problema (molt rebots) com ajudar a solucionar errors

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

##### Mètode Comparatiu Addicional

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

#### Exemples d'Objectius i Mètriques Associades

A la pràctica, triem les mètriques segons les preguntes de recerca que volem respondre:

**Objectiu 1: Comprovar si els usuaris poden completar una tasca concreta sense errors**

- **Taxa d'èxit (_Completion rate_):** Percentatge d'usuaris que aconsegueixen completar la tasca amb èxit. _(Eficàcia)_
- **Taxa d'errors:** Percentatge d'usuaris que cometen almenys un error durant l'execució de la tasca. _(Eficàcia)_
- **Temps de compleció:** Temps mitjà requerit per un usuari per completar la tasca de principi a fi. _(Eficiència)_

**Objectiu 2: Avaluar si l'usuari entén el significat d'una icona o etiqueta**

- **Percentatge de comprensió correcta:** Resposta numèrica i quantificable a la pregunta directa: _"Què creus que fa aquest botó?"_ o _"Què significa aquesta etiqueta?"_
- **Comentaris qualitatius:** Recull de confusions, dubtes o interpretacions errònies expressades per l'usuari en veu alta.

**Objectiu 3: Mesurar la càrrega cognitiva durant una tasca complexa**

- **NASA-TLX (_Task Load Index_):** Qüestionari estandarditzat post-tasca que s'utilitza per mesurar l'esforç mental i físic percebut per l'usuari. _(Satisfacció / Càrrega de treball)_
- **Temps de reflexió abans d'actuar:** El temps de latència o pausa que fa l'usuari abans d'interactuar amb un element de la interfície.

**Objectiu 4: Avaluar la satisfacció general amb el sistema**

- **SUS (_System Usability Scale_):** Qüestionari ràpid i estandarditzat de 10 ítems per avaluar la usabilitat percebuda d'un sistema.
- **NPS (_Net Promoter Score_):** Mètrica d'una sola pregunta per mesurar la lleialtat i la probabilitat de recomanació del producte.
- **Comentaris oberts:** Feedback qualitatiu de tancament sobre què els ha agradat més i què menys del sistema.

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
  - _Anàlisi Inferencial:_ Aplica mètodes paramètrics i no paramètrics per fer generalitzacions sobre la població a partir de la mostra estudiada, visualitzant els grups mitjançant gràfics de barres o relacions de variables.
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

L'ús d'eines com ChatGPT està transformant com treballem en IPO.

- **Aplicacions**: Generació d' _screeners_ (qüestionaris de selecció), creació de plantilles Excel amb fórmules per al SUS, i suport en l'**anàlisi temàtic** (anàlisi qualitatiu de transcripcions d'entrevistes).
- **Anàlisi Temàtic**: Procés de 6 passos (Recollir dades -> Llegir -> Codificar -> Crear temes -> Pausa -> Avaluar _fit_ dels temes). La IAG ajuda a identificar patrons i codis en grans volums de text.

# 5: Disseny Responsable i Sostenible

## 1. Introducció al Disseny Responsable

### Definició: Disseny UX Ètic

El disseny UX ètic busca crear experiències digitals segures, transparentes, inclusives i centrades en les persones. Implica prendre decisions responsables sobre l'impacte del producte en els individus, avaluant críticament aspectes com la manipulació mitjançant patrons foscos (_dark patterns_) o el respecte escrupolós a la privacitat. Un exemple clar d'UX ètica és no ocultar o dificultar deliberadament l'opció per cancel·lar una subscripció.

### El paper dels valors humans en UX

Els valors humans en UX fan referència a dissenyar sistemes interactius fonamentant-se en principis consolidats com l'accessibilitat, l'equitat, el benestar o la inclusió. Aquests valors varien i s'han d'adaptar segons el context d'ús i el col·lectiu d'usuaris final. Per exemple, el desenvolupament d'una aplicació accessible neix del valor de la inclusió de persones amb discapacitats.

### Impactes de les decisions de disseny

Com a enginyers de programari, hem de ser conscients que les nostres decisions tècniques i de disseny afecten diferents dimensions crítiques:

- **Interacció social**: Modifiquen com les persones interactuen amb la tecnologia i com es relacionen entre elles.

- **Drets individuals**: Influeixen directament en la privacitat i la llibertat individual de l'usuari.

- **Equitat social**: Poden reproduir biaixos socials subjacents o, en el pior dels casos, excloure deliberadament o accidental col·lectius sencers.

- **Sostenibilitat**: Determinen el consum energètic de la infraestructura i el programari, afectant directament el medi ambient.

### Beneficis dels "bons" dissenys

L'adopció d'un enfocament responsable en el cicle de vida del programari permet assolir solucions d'enginyeria que aporten beneficis clars:

- **Mitigació de l'estrès digital**: Dissenyar interfícies que evitin la sobrecàrrega cognitiva o la fatiga de l'usuari.

- **Foment de l'autonomia**: Permetre que l'usuari mantingui el control conscient de les seves accions i decisions dins del sistema.

- **Generació de confiança**: Construir relacions sòlides mitjançant el programari gràcies a la transparència i l'equitat en el tractament de dades.

- **Promoció de la inclusió**: Garantir l'accessibilitat universal per a qualsevol perfil d'usuari.

Per canalitzar aquests objectius d'una manera estructurada i holística, el temari presenta dos grans enfocaments metodològics: el _Privacy by Design_ (PbD) i el _Value Sensitive Design_ (VSD).

---

## 2. Principis de Privacy by Design (PbD)

El marc del _Privacy by Design_ (PbD) estableix que la privacitat s'ha d'integrar en el programari per defecte i des de les fases més primerenques. Aquest enfocament és clau per garantir el compliment de normatives legals com el GDPR (_General Data Protection Regulation_), reduir riscos de seguretat i generar confiança.

S'estructura en **7 principis fonamentals**:

### 1. Proactive not Reactive; Preventative not Remedial

- **Concepte**: Anticipar-se i prevenir esdeveniments abans que infringeixin la privacitat de les persones o organitzacions, en lloc d'esperar que el problema passi i aplicar remeis posteriors.

- **Exemple**: Abans de desplegar una aplicació o base de dades, realitzar auditories per comprovar possibles vectors de fuites de dades o accessos no autoritzats.

### 2. Privacy as the Default Setting

- **Concepte**: Les dades personals de l'usuari han d'estar protegides de manera automàtica per la mateixa configuració de fàbrica del sistema, sense requerir cap acció o activació manual per part de l'individu.

- **Exemple**: Una aplicació mòbil manté la compartició de la ubicació completament desactivada per defecte fins que l'usuari decideix activar-la explícitament.

### 3. Privacy Embedded into Design

- **Concepte**: La privacitat no és un mòdul addicional o un pegat que s'afegeix al final del desenvolupament; s'ha d'integrar com un element central de l'arquitectura del sistema des de la seva concepció inicial.

- **Exemple**: Dissenyar un formulari de registre sol·licitant de manera estricta el mínim de dades possibles per al seu funcionament (minimització de dades).

### 4. Full Functionality - Positive-Sum, not Zero-Sum

- **Concepte**: Evitar el fals dilema entre seguretat i funcionalitat. El disseny ha d'assolir un escenari on "tots guanyen" (suma positiva), demostrant que és viable protegir la privacitat sense degradar l'experiència ni les funcions de l'aplicació.

- **Exemple**: Desenvolupar una aplicació que ofereix recomanacions personalitzades de qualitat a l'usuari sense necessitat d'emmagatzemar cap mena d'historial sensible als servidors.

### 5. End-to-End Security - Lifecycle Protection

- **Concepte**: Garantir la seguretat i integritat de la informació durant absolutament tot el cicle de vida de les dades, cobrint des de la captura inicial i el trànsit, fins a l'emmagatzematge i la seva destrucció definitiva i segura.

- **Exemple**: Un servei de missatgeria xifra les dades extrem a extrem (_end-to-end_) i programa la destrucció automatitzada dels missatges un cop l'usuari es dóna de baixa o passats $X$ dies.

### 6. Visibility and Transparency - Keep it Open

- **Concepte**: Mantenir el sistema obert i transparent per assegurar que els usuaris coneguin amb certesa quines dades es recullen, per a quin propòsit s'utilitzen i amb quins tercers es comparteixen, facilitant mecanismes de verificació, monitoratge i queixa.

- **Exemple**: La implementació de les etiquetes de privacitat (_privacy labels_) que s'utilitzen a l'App Store d'Apple per a iOS i macOS.

### 7. Respect for User Privacy - Keep it User-Centric

- **Concepte**: El disseny de la interfície ha de prioritzar els interessos de l'usuari, oferint opcions clares, nets de manipulacions, que li facilitin prendre decisions informades i mantenir el control de la seva privacitat.

### Patrons de disseny associats a la privacitat en formularis

L'aplicació pràctica del PbD en el disseny de formularis web i aplicacions exigeix seguir certs patrons de disseny concrets:

- **Explain Why You Need A User's Data**: Explicar a l'usuari de forma clara el motiu de la recol·lecció de dades directament en el context on es demanen.

- **Always Provide A Way Out**: Atès que la realitat rarament és binària, s'ha d'oferir flexibilitat i opcions d'escapament. Per exemple, en demanar el gènere en un formulari, cal incloure opcions inclusives com "Other" o "Prefer not to say".

- **Always Ask For Exactly What You Need, Never More**: Limitar les peticions estrictament al necessari. Un cas d'estudi és el formulari de verificació d'edat històric de Carlsberg, on inicialment només es demanava l'any de naixement i exclusivament se sol·licitava el mes o el dia si l'any no era suficient per validar la majoria d'edat (+18).

- **When Asking For Sensitive Details, Prepare Customers Ahead Of Time**: Quan es demanen dades d'alta sensibilitat (com ara targetes de crèdit, signatures o documents oficials), els usuaris experimenten més inseguretat. El sistema ha d'utilitzar un to professional i seriós, transmetre senyals visuals de seguretat, indicar prèviament quins documents caldran, i permetre desar el formulari per continuar-lo més tard.

- **Don't Expect Accurate Data For Temporary Accounts**: En la creació de comptes temporals (com l'accés a xarxes Wi-Fi públiques), els usuaris tendeixen a introduir correus falsos o secundaris per por al _spam_ o al rastreig. Les organitzacions han d'assumir que no rebran dades precises i han d'oferir mètodes de registre simples i un valor clar a canvi.

- **Don't Store Private Data By Default**: L'emmagatzematge automatitzat d'informació sensible (com mètodes de pagament o passaports) genera rebuig. Es recomana requerir un consentiment explícit abans de desar-los, detallant clarament com es protegiran.

---

## 3. Metodologies de Value Sensitive Design (VSD) i UX Sostenible

El _Value Sensitive Design_ (VSD) és una aproximació metodològica que situa els valors humans al centre del procés de disseny de la tecnologia.

### El trípode metodològic del VSD

**tres tipus de recerques**:

1. **Recerca Conceptual**: Se centra en la identificació i definició dels valors humans que són rellevants per al projecte (ex: privacitat, autonomia, justícia). Així mateix, exigeix realitzar una anàlisi exhaustiva tant dels grups d'interès directes (els usuaris del sistema) com dels indirectes (aquells afectats pel desplegament de la tecnologia).

2. **Recerca Empírica**: Consisteix a avaluar i estudiar de quina manera els usuaris del món real perceben, Prioritzen i viuen aquests valors en el seu dia a dia. S'executa mitjançant tècniques qualitatives i quantitatives de recerca com entrevistes, enquestes o observació de camp.

3. **Recerca Tècnica**: Analitza com les propietats de les tecnologies existents suporten o, al contrari, comprometen i posen en risc els valors identificats. A partir d'aquí, es focalitza en el desenvolupament de noves solucions tècniques que incorporin de forma nativa aquests valors humans.

Els valors habituals i recurrents en l'aplicació del VSD inclouen la privacitat, l'autonomia, la justícia, el benestar, la inclusió, la dignitat humana i la sostenibilitat.

### Els principis de la UX Sostenible

La incorporació del valor de la sostenibilitat en el disseny d'interfícies i sistemes (UX Sostenible) persegueix reduir l'impacte ambiental, energètic i social dels productes digitals. D'acord amb la literatura del sector, s'estructuren els següents **11 principis fonamentals**:

1. **Design for ecosystems instead of users**: Estendre el focus del disseny més enllà de l'usuari individual per considerar l'impacte en la totalitat de persones, sistemes i elements de l'ecosistema afectats pel producte.

2. **Understand the negative impacts**: Analitzar de manera crítica les externalitats negatives derivades del programari, incloent-hi el consum elèctric, les emissions de carboni indirectes o l'impacte social.

3. **Design for all aspects of Sustainability**: Abordar la sostenibilitat des d'una perspectiva global i no només verda, integrant el medi ambient, l'equitat social, la salut i el benestar humà.

4. **Design Carbon Friendly**: Optimitzar el codi, l'arquitectura i el disseny visual per reduir dràsticament la transferència de dades i el processament del processador, generant un programari molt més lleuger i eficient. Una solució pràctica és la implementació del _mode fosc_ per estalviar energia en dispositius amb pantalles OLED.

5. **Design for Equality**: Assegurar la creació de productes digitals altament accessibles i inclusius, evitant que el disseny accentuï o creï noves bretxes digitals o desigualtats.

6. **Design for Wellbeing and Fairness**: Dissenyar solucions digitals que posin per davant la salut mental i el benestar de l'usuari, descartant de manera absoluta mètodes persuasius opacs o patrons manipulatius.

7. **Design for sustainable Users**: Ajudar els usuaris a prendre decisions més ecològiques i responsables a través d'opcions sostenibles configurades per defecte o informant-los directament de la petjada de les seves accions.

8. **Solve the right Problems**: Validar que el sistema de programari resol un problema real, significatiu i viable a llarg termini, evitant el desenvolupament de solucions cosmètiques o innecessàries.

9. **Design for less**: Aplicar el minimalisme digital eliminant contingut superflu, animacions innecessàries i complexitat de dades per minimitzar el còmput en el servidor i el client. _Nota d'examen_: Els carrusels d'imatges s'identifiquen com un component poc sostenible a causa de les animacions, càrrega de múltiples imatges pesades i processament addicional que requereixen.

10. **Make Sustainability Default**: Integrar els requisits de sostenibilitat de manera nativa en el flux de treball d'enginyeria, no com una llista de verificació opcional al final del projecte.

11. **Design new Narratives**: Comunicar la sostenibilitat de forma atractiva i positiva, convertint-la en un factor de valor afegit i d'innovació tant per a l'empresa com per als usuaris.

> **Exemple de conscienciació (Sustainable UX)**: El disseny sostenible va més enllà de l'eficiència energètica bruta; té una component educadora. Un cas paradigmàtic és un lloc web de comerç electrònic que, en detectar que el seu centre de dades no es pot abastir temporalment d'energia 100% renovable, mostra un avís contextual informatiu a l'usuari (permetent-li, no obstant això, finalitzar la seva compra si ho desitja).

#### Conclusions i Respostes a les Preguntes de Recerca (RQ)

- **RQ1 (Etapes del viatge de l'usuari)**: S'identifiquen **quatre estadis principals i seqüencials**: descobriment de l'app (_app discovery_), exploració i selecció, instal·lació, i finalment, la concessió de permisos (_permission granting_).

- **RQ2 (Variacions segons el tipus d'aplicació)**: Aquestes etapes no són rígidament lineals, sinó que estan connectades de forma inherent. Estan estretament influenciades per factors com el tipus d'aplicació, recomanacions socials, la reputació de la marca, l'utilitat percebuda i les expectatives del context.

- **RQ3 (Estratègies de privacitat aplicades)**: Al llarg del camí, els usuaris executen mètodes actius de protecció com la verificació prèvia a través de les seccions de seguretat de les botigues (ex: la _Data Safety Section_ o DSS de Google Play), la revisió activa de comentaris (_reviews_), l'acceptació altament selectiva de permisos o, en contraposició, la conformitat rutinària per tedi.
