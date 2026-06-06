---
id: Disseny
aliases: []
tags: []
---

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
> - Crea connexió amb l’usuari.
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
