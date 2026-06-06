---
id: Accessibilitat
aliases: []
tags: []
---

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

## ![[Pasted image 20260418112446.png]]

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

## ![[Pasted image 20260418113629.png]]

## 6. L'Estàndard WCAG i els Principis POUR

Les **WCAG (Web Content Accessibility Guidelines)** són el fonament de tota regulació actual. Tot i que l'accessibilitat ideal hauria d'implicar eines d'autoria i navegadors, la llei actual se centra principalment en el **contingut**.

El WCAG Fa molt d'èmfasi en 4 principis POUR:

- **Els 4 Principis (POUR)**:
  1. **Perceptible**: El contingut s'ha de poder percebre per algun sentit (visual, sonor o tàctil). No pot ser invisible a tots els sentits de l'usuari.
  2. **Operable**: Els components de la interfície i la navegació han de ser manejables (ex: navegació només per teclat).
  3. **Comprensible**: La informació i el maneig de la interfície han de ser clars i fàcils d'entendre.
  4. **Robust**: El contingut ha de ser prou robust per ser interpretat de manera fiable per una gran varietat d'agents d'usuari (navegadors) i tecnologies d'ajuda.

