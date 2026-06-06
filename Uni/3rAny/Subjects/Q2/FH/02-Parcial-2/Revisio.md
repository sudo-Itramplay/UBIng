---
data: 2026-05-27
assignatura: FH
tags:
  - tipus/parcial
  - assignatura/FH
---

# FH Final — Repassada ràpida

> [!abstract] Notes atòmiques del 2n Parcial
> **Disseny:** [[Disseny]] · [[Lleis de la Interacció]] · [[Principis de Don Norman]] · [[Heurístiques de Nielsen]] · [[Disseny Visual]] · [[Guia d'Estil]] · [[Disseny Emocional]] · [[Patrons de Disseny]]
> **Accessibilitat:** [[Accessibilitat]] · [[Disseny Inclusiu]] · [[Perfils de Visió]] · [[Perfils d'Audició]] · [[Perfils Motors i Cognitius]] · [[Persones Grans]] · [[WCAG i POUR]] · [[Accessibilitat VUE]]
> **Avaluació:** [[Avaluació del Disseny]] · [[Avaluació amb Usuaris]] · [[Avaluació per Experts]] · [[Mètriques d'Usabilitat]] · [[Qüestionaris Estandarditzats]]

---

## 1. Disseny

**5Es de la Usabilitat**: Eficiència, Eficàcia, Easy to Learn, Error tolerance, Engaging. La UX engloba tot això més la part emocional.

**Lleis HCI** (3):
- **Fitts**: el temps per clicar un objecte depèn de la seva distància i mida ($MT=a+b\log_2(D/W+1)$). → botons grans i propers, "màgic píxels" a les cantonades.
- **Hick-Hyman**: més opcions = més temps de decisió ($RT=a+b\log_2(n)$). → simplicitat.
- **Miller**: la memòria a curt termini reté **7 ± 2** elements. → *chunking*, reconeixement per sobre del record.

**Principis de Don Norman** (reducció del "golf d'execució/avaluació"):
- **Visibilitat i Feedback**: les funcions han de ser visibles i el sistema ha de respondre immediatament.
- **Affordances i Signifiers**: l'objecte indica com s'usa; els senyals visuals marquen on interactuar.
- **Constraints**: limitar accions per evitar errors.
- **Mapping**: relació natural entre control i efecte (ex: fogons alineats amb botons).
- **Consistència i Simplicitat**: elements similars per a tasques similars.

**10 Heurístiques de Nielsen** (saber-les totes per l'examen):
- H1: Visibilitat de l'estat del sistema.
- H2: Concordança sistema-món real.
- H3: Control i llibertat de l'usuari (Desfer).
- H4: Consistència i estàndards.
- H5: Prevenció d'errors.
- H6: Reconeixement en lloc de record.
- H7: Flexibilitat i eficiència d'ús.
- H8: Estètica i disseny minimalista.
- H9: Ajuda a reconèixer, diagnosticar i recuperar-se d'errors.
- H10: Ajuda i documentació.

**Disseny Visual (Gestalt)**: "el tot és més que la suma de les parts". Variables visuals: posició, mida, forma, color... Jerarquia visual amb patrons **F i Z**. *Squint test* per avaluar-la ràpidament. Proporció àuria $\Phi \approx 1.618$.

**Guia d'Estil**: identitat de marca (logo, paleta hex/RGBA), tipografia + to de veu (formal/proper/tècnic), iconografia, espaiat (grid de 8px), components UI (botons, formularis, navegació).

**Disseny Emocional** (Aaron Walter → funcional > fiable > usable > **plaent**). Don Norman: 3 nivells:
- **Visceral**: reacció estètica immediata.
- **Conductual**: experiència d'ús.
- **Reflexiu**: significat i impacte personal.

**Patrons de Disseny**:
- **Generals**: wizards, cercadors, gestió d'errors.
- **Persuasius**: gamificació, feedback positiu.
- **Foscos (Deceptive patterns)**: manipulació → cal evitar-los.

---

## 2. Accessibilitat

**Idea clau**: accessibilitat no és només per a discapacitats permanents → també **contextuals** (temporal: infecció d'oïda; situacional: conductor, pare amb nadó).

**Beneficis**: estudi PwC → productes inclusius tripliquen/quadrupliquen audiència. Mercat de 40 bilions. Vueling i Amazon han rebut sancions per no complir.

**Principis del disseny inclusiu**:
1. Reconèixer l'exclusió i els propis biaixos.
2. Aprendre de la diversitat.
3. Resoldre per a extrems beneficia tothom (efecte "rampa de vorera").

**Perfils**:

| Col·lectiu | Tipologies | Tecnologies d'ajuda | Disseny |
|------------|------------|---------------------|---------|
| **Visió** | Daltonisme (vermell/verd, perceben per lluminositat), baixa visió, ceguesa | Magnificadors (ZoomText), lectors pantalla (JAWS, NVDA), Braille | Text real, contrastos, nav. per teclat |
| **Audició** | Prelocutiva (abans de parlar), postlocutiva. Oralistes vs Signistes (LSC/LSE) | Audiòfons, implants coclears, bucle magnètic | Subtítols, avisos visuals, alternativa al telèfon |
| **Motor** | Precisió reduïda, ús limitat de teclat/ratolí | Eye-tracking, joysticks, polsadors | Vincles grans i separats, menys passos |
| **Cognitiu** | Autisme, dislèxia, TDAH | ClaroRead, lectors text-veu | COGA: llenguatge simple, textos curts |
| **Gent gran** | Pluridiscapacitat lleu (visió+oïda+motor+cognitiu) | — | Text gran, instruccions pas a pas, rutines conegudes |

**WCAG + POUR** (fonament de tota regulació):
- **P**erceptible: contingut perceptible per algun sentit.
- **O**perable: navegable per teclat.
- **U**nderstandable (Comprensible): clar i fàcil d'entendre.
- **R**obust: interpretat per navegadors i tecnologies d'ajuda diverses.

**Vue.js**: Vuetify (Material Design), AccessiVue (TFG ex-alumna: 5 components accessibles), Vue-a11y. **Skip link** ("Skip to main content") per no haver de tabular tots els menús en cada canvi de vista → es mostra només quan té el focus.

---

## 3. Avaluació del Disseny

**Idea**: validar si el disseny funciona per a les persones reals. ISO 9241-210. Perspectiva sempre de l'usuari. **5 usuaris → 80% dels problemes**.

**Tipus**:
- **Avaluació Formativa**: durant el procés iteratiu, per millorar.
- **Avaluació Sumativa**: al final, per confirmar objectius.
- **Monitoratge a llarg termini**: insights d'ús real (rebots, errors).

**Classificació de mètodes** (2 eixos):
- Moderat vs No moderat
- Remot vs En persona

| | Moderat | No moderat |
|---|---|---|
| **Remot** | Phone/Video Interview | Session Recordings |
| **En persona** | Lab Testing, Guerrilla Testing | Observation "in-the-wild" |

**A/B testing**: comparar dues versions (A i B) quantitativament.

**Consideracions ètiques**:
- *Abans*: consentiment informat; es prova el **sistema, no l'usuari**; pot aturar-se quan vulgui.
- *Durant*: atmosfera relaxada; mai indicar errors.
- *Després*: confidencialitat absoluta; resultats no han de permetre identificar individus.

**Arquitectura de l'estudi**:
- **Between-subjects**: grups diferents → evita aprenentatge, necessita més participants.
- **Within-subjects**: el mateix usuari fa tot → eficient, però cal balancejar l'ordre (*transfer effect*).

**Procediment**: Preparació (objectiu, ètica, test pilot) → Realització (intro + execució + tancament) → Anàlisi i informe.

**Mètriques**:
- **Eficàcia**: taxa d'èxit (*completion rate*), taxa d'errors.
- **Eficiència**: temps per tasca, nombre de clics, *lostness*.
- **Satisfacció**: percepció, confiança, càrrega de treball. NASA-TLX.
- **Fisiològiques**: eye-tracking, pupil·la, ritme cardíac.

**Qüestionaris estandarditzats** (no modificar!):
- **SEQ**: 1 pregunta (1-7) sobre dificultat d'una tasca.
- **SUS**: 10 preguntes alternades (positiu/negatiu). **> 68-70 = acceptable**.
- **UEQ**: atractiu, claredat, eficiència, estimulació, novetat.
- **NPS**: $\% \text{Promotors (9-10)} - \% \text{Detractors (0-6)}$. Passius (7-8) no compten.

**Anàlisi de resultats**:
- Quantitativa: descriptiva (mitjana, mediana, box plots) + inferencial (paramètric/no paramètric).
- Qualitativa: **Clarke & Braun** (6 passos): Gather → Read → Code → Create themes → Take a break → Avaluar fit.

**Avaluació per Experts** (sense usuaris reals, ràpida i barata però limitada):
- **Avaluació Heurística**: experts jutgen la interfície contra les 10 heurístiques de Nielsen. Diverses passades independents → posada en comú → informe de gravetat.
- **Passeig Cognitiu**: simular usuari novell en una tasca. Per cada pas: (1) sap que ha de fer-ho? (2) veu l'element? (3) entén el feedback?

**IAG en avaluació**: generació de screeners, plantilles SUS, anàlisi temàtic de transcripcions.
