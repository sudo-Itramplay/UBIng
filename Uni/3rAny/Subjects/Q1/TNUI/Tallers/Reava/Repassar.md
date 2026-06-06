
# Apunts Preguntes a revisar


### 1. Bayes - Exercici Medicina

Al document `9 El Teorema de Bayes - HackMD.pdf` s'explica molt bé la teoria i es posen exemples d'assignatures (Algorísmica), però **no apareix el text de l'exercici de medicina** que menciones.

* **Què hauries de buscar:** Probablement és l'exemple clàssic del "Test de diagnòstic" (ex: Càncer o VIH). Repassa com es calcula la probabilitat de tenir la malaltia si el test és positiu, tenint en compte la **prevalença** (probabilitat a priori), la **sensibilitat** (True Positive Rate) i la **especificitat** (True Negative Rate). És un exercici típic on el resultat sol ser contraintuïtiu.

### 2. Recomanadors - Per què Factorization Machine és un model lineal

El document `Recomanadors (Part II) - HackMD.pdf` se centra més en *Next Event Prediction* i *Softmax*. L'explicació de per què les FM són lineals és una qüestió teòrica important:

* **Què hauries de mirar:** Comprova si a les teves notes tens la fòrmula. Les FM són lineals perquè modelen la interacció de variables mitjançant el producte escalar de vectors latents, però la predicció final és una **suma ponderada** d'aquests components. S'anomenen lineals perquè són lineals respecte als seus paràmetres un cop definits els productes creuats.

### 3. El Problema de les "Pomes" i la Cervesa

Als documents apareix el model de la "Bossa de la compra" i l'exemple típic de **Bolquers i Cervesa** (diapers and beer).

* **Nota:** Si el professor va parlar de "pomes", és una variant. Assegura't de saber aplicar els conceptes de **Suport, Confiança i Interès** a qualsevol parell de productes. El concepte d'**Interès** (la diferència entre la confiança i la probabilitat basal) és el que sol ser la clau de la "heurística" que es demana.

### 4. Perceptró i limitacions - notebook1

La pregunta menciona específicament un "notebook1". Com que només disposem dels PDF de teoria (`FC and CNN MNIST.pdf`), no veig el codi ni els experiments concrets d'aquell fitxer .ipynb.

* **Què hauries de mirar:** Obre el notebook i fixa't en el moment on el perceptró simple (o la xarxa totalment connectada) comença a fallar quan la imatge es mou o té soroll. Això il·lustra la falta d'**invariància a la translació**, que és la limitació principal que solucionen les CNN.

### 5. Ética - Independència i Separació (Exemple Universitats)

El document `Algorimes i Dades Aspectes ètics.pdf` menciona el teorema d'incompatibilitat, però l'exemple de les universitats sol ser un cas pràctic per explicar que si intentes ser "just" per a un grup (mateixa taxa d'admissió), pots acabar sent "injust" en la precisió de les teves prediccions per a l'altre.

* **Consell:** Tenir clar que no es poden satisfer totes les mètriques d'equitat alhora.

La resta de preguntes (Bootstrapping, Thompson Sampling, LLMs i Optimització) estan molt ben cobertes als documents i amb el que t'he posat a la resposta anterior hauries de tenir-ne prou.
