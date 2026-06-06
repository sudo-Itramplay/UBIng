
## 1. Fonaments de les Reflexions i l'Algorisme Recursiu

El Ray Tracing és, per definició, un algorisme recursiu que busca simular el comportament de la llum en interactuar amb superfícies. En lloc de quedar-nos amb un color estàtic ( o amb un sol raig), refinem el càlcul del píxel sumant contribucions de diferents rajos secundaris.

- **L'Equació de Color:** El color final d'un punt es determina per la suma del color local (llum ambient, difusa i especular) més les contribucions de la reflexió i la transparència, atenuades per coeficients propis del material.
$$color = colorLocal(point, normal, material) + K \cdot colorReflexió + K' \cdot colorTransparència$$

- **Jerarquia de Rajos:** Distingim clarament entre el **Raig Primari** (que surt de l'observador cap a l'escena) i els **Rajos Secundaris** (reflectits i transmesos) que es generen en cada punt d'intersecció.
    
- **Gestió de la Recursivitat:** Com que no podem llançar rajos infinitament, hem de definir **casos base** per aturar l'algorisme:
    
    - **Profunditat màxima:** Arribar a un nombre límit de rebots (paràmetre _depth_).
        
    - **Acabament adaptatiu:** Aturar la recursió quan la contribució del raig a la il·luminació total és gairebé insignificant (molt petita).
        
- **Fórmula Recursiva General:** La intensitat total es pot veure com una suma en cadena on cada terme nou està multiplicat pel coeficient d'atenuació del material anterior: $I = I_{local} + K_r(I'_{local} + K'_r(I''_{local} + ...))$.
    

---

## 2. Tipus de Reflexions: Especular, Difusa i "Fuzzy"

**Referència: Diapositives 8-12 (Reflexions)**

No totes les superfícies reflecteixen la llum de la mateixa manera. Com a enginyers, hem de modelar aquestes diferències segons les propietats del material.

- **Reflexions Especulars (Metalls):** Són reflexions perfectes on l'angle d'incidència és igual al de reflexió.
    
    - La direcció del raig reflectit ($r_{out}$) es calcula mitjançant:
        
        $$r_{out} = r_{in} - 2(r_{in} \cdot N) \cdot N$$
        
    - On $r_{in}$ és el raig incident i $N$ és la normal al punt d'intersecció.
        
- **El problema del "Surface Acne":** Degut a la precisió numèrica dels ordinadors, un raig reflectit pot intersectar amb la mateixa superfície on s'ha generat, creant taques negres lletges.
    
    - **Solució:** Desplaçar lleugerament el punt d'inici del raig reflectit en la direcció de la normal o del mateix raig de sortida, o utilitzar un valor $t_{min}$ petit per evitar auto-interseccions immediates.
        
- **Reflexions "Fuzzy" (Especularitat rugosa):** Per simular materials que no són miralls perfectes, afegim una petita aleatorietat al raig reflectit.
    
    - S'utilitza un paràmetre **fuzzy** (entre 0 i 1) que multiplica un vector aleatori dins d'una esfera:
        
        $$v = r + fuzzy \cdot randomInSphere()$$
        
        .
        
- **Reflexions Difuses:** La llum rebota en qualsevol direcció. Es modela fent que el raig de sortida vagi cap a un punt aleatori dins d'una esfera tangent a la normal del punt d'impacte.
    

---

## 3. La Física de les Transparències i la Llei de Snell

**Referència: Diapositives 4-10 (Transparències)**

Les transparències afegeixen una capa extra de realisme en simular com la llum travessa objectes com el vidre o l'aigua, desviant-se segons el medi.

- **Raig Transmès (Refracció):** La direcció del raig depèn de l'índex de refracció ($\mu$) dels dos medis.
    
- **Índex de Refracció (IOR):** És una mesura de la densitat òptica del material (ex: Aire $\approx$ 1.0, Aigua = 1.33, Vidre = 1.66, Diamant = 2.42).
    
- **Llei de Snell:** Regeix el canvi de direcció de la llum. La relació és:
    
    $$\frac{\sin \theta_t}{\sin \theta_i} = \frac{\mu_i}{\mu_t} = \mu_{it}$$
    
    .
    
- **Càlcul del vector de transmissió ($\vec{t}$):** Es fa servir la funció `glm::refract` basada en la fórmula vectorial que considera la normal ($\vec{n}$) i el vector incident ($\vec{i}$).
    
- **Reflexió Total Interna:** Quan la llum intenta passar d'un medi més dens a un de menys dens amb un angle d'incidència molt elevat, el raig no pot sortir i es reflecteix internament al 100%.
    
    - Matemàticament, això passa quan el terme de l'arrel quadrada en la fórmula de refracció és negatiu ($1 - \mu_{it}^2(1 - \cos^2 \theta_i) < 0$).
        
    - En aquest cas, només es té en compte el raig reflectit (`glm::reflect`).
        

---

## 4. Implementació Pràctica i Simplificacions

**Referència: Diapositives 11-23 (Transparències)**

En l'entorn de programació d'una pràctica base, sovint fem certes simplificacions per mantenir l'eficiència, encara que es poden ampliar opcionalment per a major realisme.

- **Orientació de la Normal:** És vital saber si el raig entra o surt de l'objecte. Si el producte escalar entre el raig incident i la normal és positiu ($\vec{i} \cdot \vec{n} > 0$), vol dir que estem a l'interior i hem de girar la normal ($\vec{n} = -\vec{n}$) per fer els càlculs correctament.
    
- **Atenuació de la Transparència ($K_t$):** Nou atribut del material (RGB) que indica quins colors deixa passar l'objecte. Sovint es defineix com $1 - K_s$.
    
- **Simplificacions comunes en pràctiques:**
    
    - No calcular el canvi de direcció en els rajos d'ombra que travessen objectes transparents.
        
    - No tenyir l'ombra amb el color del material transparent (les ombres es mantenen grises/negres).
        
    - No considerar objectes transparents niats (un dins de l'altre).
        
- **Millores Avançades:**
    
    - **Bombolles:** Es poden simular usant esferes amb radi negatiu dins d'esferes de vidre.
        
    - **Blinn-Phong Ponderat:** Perquè les transparències no semblin massa opaques o "brutes", podem graduar l'efecte de la il·luminació local usant $K_t$:
        
        $$color = ((1 - K_t) \cdot ColorBlinnPhong) + K_{transmès} \cdot colorRayPixel$$
        
        .
        
