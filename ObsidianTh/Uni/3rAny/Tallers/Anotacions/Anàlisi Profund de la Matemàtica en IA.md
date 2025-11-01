---
tags:
---
#IA, #matemàtiques, #deep-learning, #àlgebra-lineal, #càlcul-diferencial, #probabilitat, #estadística, #apunts-examen


---

## Introducció: La Trinitat Matemàtica de la IA

La Intel·ligència Artificial moderna, i especialment el _Deep Learning_, es construeix sobre tres pilars matemàtics interconnectats. No són disciplines separades, sinó eines que treballen en conjunt per permetre que les màquines aprenguin.

1. **Àlgebra Lineal:** És el **llenguatge de la representació**. Proporciona les estructures de dades (vectors, matrius) per emmagatzemar i manipular la informació de manera eficient.

2. **Càlcul Diferencial:** És el **motor de l'aprenentatge**. Proporciona el mecanisme d'optimització (descens de gradient) per ajustar els paràmetres d'un model i minimitzar els seus errors.

3. **Probabilitat i Estadística:** És el **marc per a la incertesa i l'avaluació**. Permet modelar la incertesa del món real i mesurar el rendiment i la confiança dels models.


---

## 1. Àlgebra Lineal: L'Estructura de les Dades

L'Àlgebra Lineal és fonamental perquè permet realitzar operacions sobre grans quantitats de dades de forma simultània i eficient. Pensa en ella com la gramàtica que ens permet construir "frases" computacionals.

### 1.1. Escalars, Vectors, Matrius i Tensors

Aquestes són les estructures de dades fonamentals.

- **Escalar:** Un simple número. Ex: x∈R.

- **Vector:** Una llista (array) de nombres. Representa un punt en un espai de múltiples dimensions. La seva dimensionalitat ve donada pel nombre d'elements que conté.
    
    - **Exemple en IA:** Un _word embedding_ és un vector que captura el significat semàntic d'una paraula. La paraula "rei" es pot representar com el vector `[0.9, 0.2, 0.1, ...]`. Un altre exemple és una imatge en escala de grisos de 28x28 píxels, que es pot "aplanar" en un vector de 784 dimensions.
        
    - Notació: v![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAALCAYAAABCm8wlAAAAOUlEQVQYV2NkwA54gcK6QHyMEYcCkLAAEHPgUwBSxEVIAS8hBXyEFAgTUiBKSIEQIQXshBQwEFQAALNkAYpU1hatAAAAAElFTkSuQmCC)=![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAsAAABWCAYAAAAZvGwPAAAAcElEQVRIS2NkwA52A4Vd0KTOMuJQvBMo/guIe5HkP+NSDDL5ARCnIhs2qng0NIAhMJo2kJPBaGiMhsZowThaMI4WjGjtjtGCcbRgHC0YRwvG0YJxpBWMoJ6mLhDfQvL4TVxFQTdQkSlaCOFUjLVrCwBMuauIhaG1OQAAAABJRU5ErkJggg==)​v1​v2​⋮vn​​![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAsAAABWCAYAAAAZvGwPAAAAcElEQVRIS2NkYGC4AMT6QIwMdgA5nmhiDIxAARMg5kGSKAOy/wOxNzbF6GLzgQISuEweVQwLAVA4j4bGaGiM5hRoGhgtN5CLg9HQGA0NUAiMVhPI6WA0NEZDY7R5iZQGRquJ0WpixFQTJHVLie7wAgAk/FpXjw8zkQAAAABJRU5ErkJggg==)​
        
- **Matriu:** Un conjunt de vectors organitzats en una graella rectangular (files i columnes).
    
    - **Exemple en IA:** La matriu de pesos (`W`) d'una capa neuronal. Si una capa té 10 neurones d'entrada i 5 de sortida, la matriu de pesos serà de 5x10. Cada fila representa els pesos de connexió cap a una neurona de sortida. Un _batch_ de dades també és una matriu, on cada fila és una mostra (ex: una imatge) i cada columna una característica (ex: un píxel).
        
    - Notació: A=[a11​a21​​a12​a22​​]
        
- **Tensor:** Una generalització d'aquestes estructures a qualsevol nombre de dimensions. Un escalar és un tensor de rang 0, un vector de rang 1, una matriu de rang 2.
    
    - **Exemple en IA:** Una imatge en color (RGB) és un tensor de rang 3: (alçada, amplada, 3 canals de color). Un vídeo és un tensor de rang 4: (nombre d'imatges, alçada, amplada, canals). Els paràmetres d'una xarxa neuronal convolucional són tensors de rang 4.
        

### 1.2. Operacions Fonamentals i la seva Interpretació

#### Producte Escalar (Dot Product)

El producte escalar entre dos vectors mesura la seva **projecció mútua**. Intuïtivament, ens diu com d'alineats estan.

- **Fórmula:** a![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAALCAYAAABCm8wlAAAAOUlEQVQYV2NkwA54gcK6QHyMEYcCkLAAEHPgUwBSxEVIAS8hBXyEFAgTUiBKSIEQIQXshBQwEFQAALNkAYpU1hatAAAAAElFTkSuQmCC)⋅b![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAALCAYAAABCm8wlAAAAOUlEQVQYV2NkwA54gcK6QHyMEYcCkLAAEHPgUwBSxEVIAS8hBXyEFAgTUiBKSIEQIQXshBQwEFQAALNkAYpU1hatAAAAAElFTkSuQmCC)=∑i=1n​ai​bi​=∥a![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAALCAYAAABCm8wlAAAAOUlEQVQYV2NkwA54gcK6QHyMEYcCkLAAEHPgUwBSxEVIAS8hBXyEFAgTUiBKSIEQIQXshBQwEFQAALNkAYpU1hatAAAAAElFTkSuQmCC)∥∥b![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAALCAYAAABCm8wlAAAAOUlEQVQYV2NkwA54gcK6QHyMEYcCkLAAEHPgUwBSxEVIAS8hBXyEFAgTUiBKSIEQIQXshBQwEFQAALNkAYpU1hatAAAAAElFTkSuQmCC)∥cos(θ)
    
- **Interpretació Geomètrica:**
    
    - Si cos(θ)=1 (vectors apunten a la mateixa direcció), el producte escalar és màxim.
        
    - Si cos(θ)=0 (vectors perpendiculars, ortogonals), el producte escalar és 0.
        
    - Si cos(θ)=−1 (vectors apunten a direccions oposades), el producte escalar és mínim (negatiu).
        
- **Aplicació en IA (Essencial):**
    
    - **Càlcul de la sortida d'una neurona:** La sortida d'una neurona abans de la funció d'activació (z) és el producte escalar entre el vector d'entrades (x![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAALCAYAAABCm8wlAAAAOUlEQVQYV2NkwA54gcK6QHyMEYcCkLAAEHPgUwBSxEVIAS8hBXyEFAgTUiBKSIEQIQXshBQwEFQAALNkAYpU1hatAAAAAElFTkSuQmCC)) i el vector de pesos (w![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAALCAYAAABCm8wlAAAAOUlEQVQYV2NkwA54gcK6QHyMEYcCkLAAEHPgUwBSxEVIAS8hBXyEFAgTUiBKSIEQIQXshBQwEFQAALNkAYpU1hatAAAAAElFTkSuQmCC)), més un biaix (b). z=w![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAALCAYAAABCm8wlAAAAOUlEQVQYV2NkwA54gcK6QHyMEYcCkLAAEHPgUwBSxEVIAS8hBXyEFAgTUiBKSIEQIQXshBQwEFQAALNkAYpU1hatAAAAAElFTkSuQmCC)⋅x![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAALCAYAAABCm8wlAAAAOUlEQVQYV2NkwA54gcK6QHyMEYcCkLAAEHPgUwBSxEVIAS8hBXyEFAgTUiBKSIEQIQXshBQwEFQAALNkAYpU1hatAAAAAElFTkSuQmCC)+b. Això mesura com "coincideix" l'entrada amb el patró que la neurona ha après (emmagatzemat a w![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAALCAYAAABCm8wlAAAAOUlEQVQYV2NkwA54gcK6QHyMEYcCkLAAEHPgUwBSxEVIAS8hBXyEFAgTUiBKSIEQIQXshBQwEFQAALNkAYpU1hatAAAAAElFTkSuQmCC)).
        
    - **Mesura de Similitud:** En el processament de llenguatge natural (NLP), la **similitud cosinus** (una normalització del producte escalar) s'utilitza per mesurar com de similars són dos vectors de paraules (embeddings). Si la similitud és propera a 1, les paraules tenen significats similars.
        

#### Multiplicació de Matrius

Aquesta operació és el cor computacional de les xarxes neuronals. Una multiplicació de matrius és, en essència, una sèrie de productes escalars.

- **Fórmula:** Si C=A⋅B, llavors Cij​=∑k​Aik​Bkj​. L'element a la fila `i`, columna `j` de la matriu resultant és el producte escalar de la fila `i` de la primera matriu amb la columna `j` de la segona.

- **Interpretació Geomètrica:** Una multiplicació matricial és una **transformació lineal** de l'espai. Pot rotar, escalar o deformar un conjunt de vectors.

- Aplicació en IA: El pas d'informació d'una capa a la següent en una xarxa neuronal (forward pass) és una multiplicació matricial. Si X és la matriu d'entrades (un batch de dades) i W és la matriu de pesos de la capa, la sortida Z es calcula com:
    
    Z=X⋅WT+b
    
    Aquesta operació transforma les representacions de les dades de la capa anterior a un nou espai de característiques més abstracte en la capa actual.
    

### 1.3. Normes: Mesurant la Mida d'un Vector

Una norma és una funció que assigna una "longitud" o "mida" a un vector.

- **Norma L2 (Euclidiana):** És la distància física des de l'origen. ∥x![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAALCAYAAABCm8wlAAAAOUlEQVQYV2NkwA54gcK6QHyMEYcCkLAAEHPgUwBSxEVIAS8hBXyEFAgTUiBKSIEQIQXshBQwEFQAALNkAYpU1hatAAAAAElFTkSuQmCC)∥2​=∑i=1n​xi2​![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAmwAAAABCAYAAABjYPKIAAAAKUlEQVRIS2NkgABOIP4OZY9SoyEwGgKjITAaAqMhMBoCoyEwGgKDKAQAuQ0BAr3fYyUAAAAASUVORK5CYII=)​
- **Norma L1 (Manhattan):** És la suma dels valors absoluts dels components. ∥x![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAALCAYAAABCm8wlAAAAOUlEQVQYV2NkwA54gcK6QHyMEYcCkLAAEHPgUwBSxEVIAS8hBXyEFAgTUiBKSIEQIQXshBQwEFQAALNkAYpU1hatAAAAAElFTkSuQmCC)∥1​=∑i=1n​∣xi​∣.

- **Aplicació en IA (Regularització):** Les normes s'utilitzen per prevenir l'_overfitting_. S'afegeix un terme a la funció de pèrdua que penalitza els pesos (`W`) grans.
    
    - **Regularització L2 (Ridge):** Afegeix λ∑wi2​. Afavoreix pesos petits i distribuïts.
        
    - **Regularització L1 (Lasso):** Afegeix λ∑∣wi​∣. Pot forçar alguns pesos a ser exactament zero, realitzant una mena de "selecció de característiques" automàtica.
        

---

## 2. Càlcul Diferencial: El Mecanisme d'Aprenentatge

Si l'àlgebra lineal estructura les dades, el càlcul ens permet **optimitzar** el model per a que aprengui d'aquestes dades. L'aprenentatge és un problema de recerca del mínim d'una funció d'error.

### 2.1. La Funció de Pèrdua (Loss Function)

És una funció que mesura la discrepància entre les prediccions del model (y^​) i els valors reals (y). L'objectiu de l'entrenament és trobar el conjunt de paràmetres (W) que minimitzen aquesta funció.

- **Exemple (Error Quadràtic Mig - MSE):** L(W)=N1​∑i=1N​(y^​i​−yi​)2.

- **El Paisatge de Pèrdua:** Podem imaginar la funció de pèrdua com un paisatge amb valls i muntanyes. Cada punt en el pla horitzontal representa una possible configuració dels pesos del model, i l'alçada en aquell punt és l'error corresponent. L'objectiu és trobar el punt més baix de la vall (el **mínim global**).


### 2.2. Derivades i Gradients: La Brúixola per a la Vall

- **Derivada (dxdf​):** Per a una funció d'una sola variable, la derivada en un punt ens dóna el pendent de la recta tangent en aquell punt.
    
    - Si dxdf​>0, la funció creix.
        
    - Si dxdf​<0, la funció decreix.
        
    - Si dxdf​=0, estem en un punt crític (mínim, màxim o punt de sella).
        
- Gradient (∇L(W)): És la generalització de la derivada per a funcions de múltiples variables (com la nostra funció de pèrdua, que depèn de milions de pesos). El gradient és un vector que conté totes les derivades parcials de la funció respecte a cada un dels seus paràmetres.
    
    ∇L(W)=![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAsAAABWCAYAAAAZvGwPAAAAcElEQVRIS2NkwA52A4Vd0KTOMuJQvBMo/guIe5HkP+NSDDL5ARCnIhs2qng0NIAhMJo2kJPBaGiMhsZowThaMI4WjGjtjtGCcbRgHC0YRwvG0YJxpBWMoJ6mLhDfQvL4TVxFQTdQkSlaCOFUjLVrCwBMuauIhaG1OQAAAABJRU5ErkJggg==)​∂w1​∂L​∂w2​∂L​⋮∂wn​∂L​​![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAsAAABWCAYAAAAZvGwPAAAAcElEQVRIS2NkYGC4AMT6QIwMdgA5nmhiDIxAARMg5kGSKAOy/wOxNzbF6GLzgQISuEweVQwLAVA4j4bGaGiM5hRoGhgtN5CLg9HQGA0NUAiMVhPI6WA0NEZDY7R5iZQGRquJ0WpixFQTJHVLie7wAgAk/FpXjw8zkQAAAABJRU5ErkJggg==)​
    
    > **Intuïció Clau:** El gradient ∇L(W) sempre apunta en la direcció de **màxim increment** de la funció de pèrdua. Per tant, per minimitzar la pèrdua, hem de moure'ns en la direcció **oposada** al gradient.
    

### 2.3. L'Algorisme de Descens de Gradient (Gradient Descent)

És un algorisme iteratiu per trobar el mínim d'una funció.

> **Analogia:** Imagina que estàs en una muntanya en plena boira i vols arribar a la vall. No veus el camí, però pots sentir la inclinació del terra sota els teus peus. Fas un pas en la direcció on el pendent és més pronunciat cap avall. Repeteixes aquest procés fins que el terra sigui pla. Aquesta és l'essència del descens de gradient.

- **Passos de l'Algorisme:**
    
    1. **Inicialització:** Escollir uns pesos inicials aleatoris (W0​).
        
    2. Iteració (època): Repetir fins a la convergència:
        
        a. Calcular el Gradient: Avaluar el gradient de la funció de pèrdua amb els pesos actuals, ∇L(Wt​). Això requereix l'ús de tot el conjunt de dades.
        
        b. Actualitzar els Pesos: Moure els pesos en la direcció oposada al gradient.
        
        Wt+1​=Wt​−η⋅∇L(Wt​)
        
- **El Hiperparàmetre Clau: La Taxa d'Aprenentatge (η, Learning Rate)**
    
    - És la "mida del pas" que fem a cada iteració.
        
    - Si η és **massa petita**, la convergència serà molt lenta.
        
    - Si η és **massa gran**, podem "saltar" per sobre del mínim i divergir. [Image comparing small vs. large learning rate in gradient descent]
        

#### Variants del Descens de Gradient

- **Stochastic Gradient Descent (SGD):** En lloc de calcular el gradient sobre tot el conjunt de dades (molt costós), l'aproxima usant **una sola mostra** a cada pas. És molt més ràpid però més sorollós (la trajectòria és més erràtica).
    
- **Mini-batch Gradient Descent:** És el compromís ideal i el més utilitzat. Calcula el gradient sobre un petit subconjunt de dades (_batch_) a cada pas. És eficient computacionalment i menys sorollós que SGD.
    

### 2.4. Backpropagation: La Màgia del Càlcul de Gradients

Com calculem eficientment el gradient de la pèrdua respecte a milions de pesos en una xarxa neuronal profunda? La resposta és l'algorisme de **backpropagation**, que no és més que una aplicació intel·ligent de la **regla de la cadena** del càlcul.

- **Regla de la Cadena:** Si z=f(y) i y=g(x), llavors la derivada de z respecte a x és: dxdz​=dydz​⋅dxdy​.
    
- **Intuïció del Backpropagation:**
    
    1. **Forward Pass:** Es passen les dades a través de la xarxa, capa per capa, fins a obtenir una predicció i calcular l'error final.
        
    2. **Backward Pass:** Es comença per l'error final i es propaga "cap enrere". A cada capa, la regla de la cadena permet calcular com l'error depèn dels pesos d'aquella capa, reutilitzant els gradients ja calculats de les capes posteriors.
        

> El backpropagation permet calcular totes les derivades parcials (∂wi​∂L​) de manera molt eficient, sense haver de recalcular-ho tot des de zero per a cada pes.

---

## 3. Probabilitat i Estadística: Gestió de la Incertesa

El món real és incert i sorollós. La probabilitat ens ofereix el llenguatge per quantificar aquesta incertesa i l'estadística les eines per inferir conclusions a partir de dades.

### 3.1. Probabilitat per a les Sortides del Model

Molts models de classificació no produeixen una resposta absoluta, sinó una distribució de probabilitat sobre les possibles classes.

- Funció Sigmoid (σ(z)): S'utilitza en la capa de sortida per a classificació binària. Transforma qualsevol número real en un valor entre 0 i 1, interpretable com una probabilitat.
    
    σ(z)=1+e−z1​
    
- Funció Softmax: S'utilitza en la capa de sortida per a classificació multiclase. Agafa un vector de puntuacions (logits) i el transforma en un vector de probabilitats on tots els elements sumen 1.
    
    softmax(zi​)=∑j=1K​ezj​ezi​​
    
    La sortida de Softmax ens diu la probabilitat que l'entrada pertanyi a cada una de les K classes.
    

### 3.2. Funcions de Pèrdua des d'una Perspectiva Probabilística

El principi d'**Estimació de Màxima Versemblança (Maximum Likelihood Estimation - MLE)** és un concepte estadístic fonamental que unifica moltes funcions de pèrdua.

> **Idea de MLE:** Donades unes dades, quins paràmetres del model fan que les dades que hem observat siguin el més probables possible?

Resulta que **minimitzar certes funcions de pèrdua és equivalent a maximitzar la versemblança** de les dades.

- **Error Quadràtic Mig (MSE):** Minimitzar l'MSE és equivalent a fer una estimació de màxima versemblança sota l'supòsit que els errors segueixen una distribució Gaussiana (Normal).
    
- Entropia Creuada (Cross-Entropy): Aquesta és la funció de pèrdua estàndard per a problemes de classificació.
    
    H(p,q)=−i=1∑K​p(xi​)log(q(xi​))
    
    Aquí, p és la distribució de probabilitat real (un vector one-hot, ex: [0, 1, 0] si la classe correcta és la segona) i q és la distribució predita pel model (la sortida de Softmax).
    
    L'entropia creuada mesura la "distància" entre la distribució predita i la real. Minimitzar l'entropia creuada és exactament el mateix que maximitzar la versemblança de les dades de classificació. És l'eina perfecta per entrenar classificadors probabilístics.
    

## Conclusió Final per a l'Examen

La interconnexió és la clau. Un model de _Deep Learning_ és un objecte matemàtic complex on:

1. Les dades i els pesos es representen com a **tensors** (Àlgebra Lineal).
    
2. El processament de la informació es realitza mitjançant operacions matricials, com el **producte escalar** i la **multiplicació de matrius** (Àlgebra Lineal).
    
3. L'objectiu és minimitzar una funció de pèrdua, sovint basada en principis de **probabilitat** com la **Cross-Entropy**.
    
4. Aquesta minimització es fa de forma iterativa amb el **Descens de Gradient** (Càlcul), que requereix calcular el **gradient** de la pèrdua.
    
5. El gradient es calcula eficientment per a totes les capes mitjançant l'algorisme de **Backpropagation**, que és una aplicació recursiva de la **regla de la cadena** (Càlcul).
    

Dominar aquestes tres àrees i la seva sinergia és dominar els fonaments teòrics de la Intel·ligència Artificial moderna.