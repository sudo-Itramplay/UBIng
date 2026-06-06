## P1
![[WhatsApp Image 2025-10-21 at 14.57.09 (1).jpeg]]

Es crida despres de configurar eel dispositiu amb Serial begin amb els bauds corresponents i el posem en mode buscar wifi:
  // Configura l'ESP8266 en mode "Station" (WIFI_STA), que significa que es connectarà a un router existent.
  WiFi.mode(WIFI_STA);

Posteriorment cridarem a wifiNetworkSelection(); Per introduir les credencials per saber a quin wifi ens volem conectar i ens hi conectarem amb aquest mètode

S'ha de cridar quan busques 

Falta posar de str a char (no ho vam fer nosaltres)




## P2

![[acipy.jpeg]]

#### ⚙️ **Com es fa l'ajust?**

L'objectiu de l'ajust de corbes és trobar els paràmetres d'una funció matemàtica (un model) que facin que aquesta funció s'assembli el màxim possible a les teves dades experimentals. El procés general és:

1. **Definir el model teòric**: Primer, has de definir una funció que representi el fenomen que estudies. Per al RSSI, un model comú és el **model de pèrdua de senyal logarítmic**:
    
    $RSSI(d)=A−10⋅n⋅log10​(d)$
    
    
    On:
    
    - `d` és la distància.
        
    - `A` és el valor de RSSI a 1 metre de distància (potència de referència).
        
    - `n` és l'exponent de pèrdua de senyal (Path Loss Exponent), que depèn de l'entorn.
        
2. **Preparar les dades**: Necessites les teves dades experimentals: un conjunt de distàncies (`x_data`) i els valors de RSSI mesurats a cada distància (`y_data`).
    
3. **Executar l'ajust**: Utilitzes una funció com `curve_fit` passant-li el model, les dades `x` i les dades `y`. La funció et retornarà els valors òptims per als paràmetres del teu model (en aquest cas, `A` i `n`).
    

#### 🔬 **Per què cal fer aquest ajust?**

El model teòric pur (la fórmula) és una idealització. El món real té obstacles, interferències i reflexions (efecte multicamí) que el model teòric no contempla.

L'ajust és necessari per **calibrar el model teòric a les condicions del teu entorn real**. En trobar els valors de `A` i `n` que millor s'ajusten a les _teves_ mesures, crees un model matemàtic personalitzat que descriu amb molta més precisió com es comporta el senyal WiFi _en aquell espai concret_. Aquest model calibrat és molt més útil per a tasques com, per exemple, estimar la distància a partir d'una nova mesura de RSSI.


# P3

![[WhatsApp Image 2025-10-21 at 14.57.jpeg]]


## P4
![[wasa.jpeg]]

