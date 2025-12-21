## 1. La Imatge Digital

Una **[[Imatge|imatge]]** és una font d'energia lumínica que transporta informació codificada del món. La seva versió digital es crea quan una càmera substitueix la pel·lícula analògica per una **[[Matriu de sensors]]**. Cada sensor emmagatzema valors enters, formant una matriu de dades.

El procés de digitalització implica dos passos fonamentals:

- **[[Sampling|Mostreig]]**: Converteix l'espai 2D continu capturat per la càmera en una matriu discreta de píxels.
    
- **[[Quantificació]]**: Arrodoneix el valor de cada mostra a l'enter més proper per assignar-li un nivell d'intensitat.
    

### 1.1. Representació i Qualitat

Les imatges digitals es poden representar de diverses maneres, principalment:

- **[[imatges de nivell de gris]]**: Una matriu de 3 dimensions `[y, x, nivell_de_gris]`, on la intensitat del negre es representa com un `float64`.
    
- **[[imatges RGB]]**: Una matriu de 3 dimensions `[y, x, [R,G,B]]`, on cada canal de color (Vermell, Verd, Blau) es representa amb un valor `uint8` (fins a 255).
    

La qualitat d'una imatge es defineix per la seva **[[Resolució]]**, que té dues components:

- **[[Resolució Espaial]]**: El nombre de píxels en els eixos X i Y (p. ex., 1920x1080).
    
- **[[Resolució Fotomètrica]]**: El nombre de colors que es poden representar, determinat pel nombre de bits per píxel (p. ex., 1 bit permet 2 colors).
    

L'**[[Histograma]]** és una eina gràfica que mostra la distribució dels nivells d'intensitat dels píxels i s'utilitza principalment per a la millora del contrast.

## 2. Processament amb Filtres

El **[[Filtratge]]** consisteix a aplicar una funció sobre el veïnatge de cada píxel. Aquesta operació es defineix mitjançant un **filtre** o **màscara (kernel)**. El procés d'aplicar el filtre a la imatge s'anomena **[[Convolució]]**.

### 2.1. Usos del Filtratge

El filtratge té diverses aplicacions clau:

- Millora d'imatges, com la reducció de soroll ([[Smoothing|allisament]]).
    
- Extracció d'informació, com la detecció de **[[Vora|vores]]**, que són canvis ràpids en la intensitat.
    
- Detecció de patrons.
    

## 3. Reducció de Soroll (Smoothing)

L'**[[Smoothing|allisament]]** és una tècnica de filtratge utilitzada per reduir el soroll en una imatge. Existeixen diferents **[[Uni/3rAny/Visio/TH/ppt2 i 3/Filtres Lineals/Processament amb filtres/Filtres/Tipus de soroll|tipus de soroll]]**, i cada un es tracta de manera més efectiva amb filtres específics.

- **[[Soroll d'impuls]]**: Aparició de píxels blancs aïllats.
    
- **[[Soroll Salt&Pepper]]**: Píxels que prenen valors extrems (blanc o negre).
    
- **[[Soroll Gaussià]]**: Soroll més general i distribuït.
    

### 3.2. Tipus de Filtres

Els filtres s'escullen segons l'objectiu i el tipus de soroll a tractar.

- **[[Filtre de la Mitjana]]**: És un filtre lineal que substitueix cada píxel pel valor mitjà del seu veïnat. Es realitza mitjançant una convolució amb un nucli on tots els pesos són uniformes (com un "box filter").
    
- **[[Filtre de la Mediana]]**: Calcula la mediana dels valors del veïnat per assignar-la al píxel central. És especialment efectiu per eliminar **[[Soroll d'impuls]]** i **[[Soroll Salt&Pepper]]**.
    
    - **Propietats clau**: Preserva les vores (`Edge Preserving`) i no introdueix valors de píxel nous a la imatge.
        
- **[[Filtre Gaussià]]**: És un filtre lineal de suavització que utilitza pesos no uniformes basats en una funció Gaussiana 2D. Els píxels més propers tenen més influència.
    
    - **Objectiu**: Elimina components d'alta freqüència, actuant com un filtre "passa-baix" (`low-pass filter`), i és útil per reduir el soroll en general. El paràmetre $\sigma$ controla el grau de suavització.