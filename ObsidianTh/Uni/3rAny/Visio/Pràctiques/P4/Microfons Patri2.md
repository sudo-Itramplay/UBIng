

## 1. Marques de Referència

- **Rode** 

- **Sennheiser** 

- **Audio-Technica** 

- **Focusrite** 


---

## 2. Directrius 

### Protocol de Connexió

> [!WARNING] Evitar Bluetooth
> 
> Tot i la comoditat del format sense fils, s'ha d'evitar el protocol Bluetooth estàndard per a l'enregistrament de veu principal.
> 
> - **Motiu:** Introdueix latència variable i aplica una compressió de dades destructiva que degrada significativament la qualitat de l'àudio.
>     
> - **Excepció:** Sistemes de transmissió propietària (com els de Rode o DJI) que utilitzen la banda de 2.4GHz amb latència baixa, tot i que el cable sempre oferirà la màxima fidelitat.
>     

### Configuració de l'Espai

- Recomano **un micròfon per interlocutor** (Cardioide). Això evita problemes de fase i ecos indesitjats.

- **Gestió de l'acústica:**
    
    - Micròfons amb captació anterior i posterior (bidireccionals) poden oferir qualitat d'estudi a baix preu, però són **crítics amb l'entorn**.
    
    - Si l'habitació té reverberació ("eco"), aquests micròfons captaran el reflex de les parets, fent l'àudio inusable. En entorns no tractats, prioritza patrons que rebutgin el so ambiental.
    

---

## 3. Teoria de Captació: Patrons Polars

El patró polar defineix l'espai tridimensional on el micròfon és sensible al so.

### A. Omnidireccional (360°)

- **Comportament:** Esfèric. Sensibilitat idèntica des de qualsevol angle.
    
- **Cas d'ús:** Enregistrament d'ambients, taules rodones o instruments on es busca naturalitat.
    
- **Contraindicació:** Capta tot el soroll mecànic de l'habitació (teclats, ventiladors de PC, trànsit).
    

### B. Cardioide (Unidireccional)

- **Comportament:** Forma de cor. Màxima sensibilitat frontal, rebuig total posterior (180°).
    
- **Cas d'ús:** L'estàndard per a _podcasting_ i _streaming_. Aïlla la veu de l'usuari i ignora el so que prové de darrere (ex: altaveus o soroll de teclat mecànic).
    
- **Efecte de Proximitat:** Accentua les freqüències greus a mesura que la font s'apropa a la càpsula (veu de ràdio).
    

### C. Supercardioide / Hipercardioide

- **Comportament:** Més direccional que el cardioide, estrenyent el focus frontal.
    
- **Peculiaritat:** Presenta un petit lòbul de sensibilitat a la part **posterior**.
    
- **Precaució:** No s'ha de col·locar el monitor/altaveu just al darrere (180°), sinó en angles diagonals (120°-150°) per evitar retroalimentació (_feedback_).
    

### D. Bidireccional (Figura de 8)

- **Comportament:** Capta davant i darrere; rebuig absolut als laterals (90°).
    
- **Cas d'ús:** Entrevistes "cara a cara" amb un sol dispositiu o tècniques estèreo avançades (Blumlein).
    

---

## 4. Teoria de Transducció: Mecanisme

Classificació segons com es converteix l'ona sonora en senyal elèctric.

|**Tipus**|**Funcionament**|**Característiques**|**Entorn Ideal**|
|---|---|---|---|
|**Dinàmic**|Inducció (Bobina mòbil)|Robust, suporta alta pressió sonora (SPL). Menys sensible a aguts i soroll de fons llunyà.|Habitacions sense tractament acústic, Ràdio.|
|**Condensador**|Capacitat elèctrica|Molt sensible, gran detall en altes freqüències i resposta ràpida a transitoris. Requereix **+48V (Phantom Power)**.|Estudis professionals, veus delicades.|
|**Lavalier**|Condensador Electret (solapa)|Miniatura. Sol ser **Omnidireccional** per garantir captació constant encara que l'orador mogui el cap.|Video, presentacions dempeus.|

>[!NOTE] Apunt
>El de condensador realment millora moltissim la qualitatat, i en part és per això que una placa de só compensa, evita haver de comprar la font d'alimentació phantom

Al principi pot funcionar tot correctament amb un Microfon dinàmic, que també veurà millora si tens la placa de só, ja que té altres funcions apart d'alimentar, i et donarà la possibilitat més endavant de poder millorar equipament 

---

## 5. Anàlisi Tècnica de Maquinari

Aplicació de la teoria als models seleccionats.

### Scarlett 2i2

- **Especificacions:** Placa de So
    
- **Diagnòstic:** Estandard en plaques de só d'entrada, dona moltes opcions i la possibilitat de colocar dos microfons. Té sortides per altaveus i auriculars i permeten gestionar cada audio de manera independent. Fan de DAC, amplificador i pots configurar-hi bauds, freqüències, etc. Al ser ja una interfície sòlida, permet una posterior millora sense necessitat de fer grans inversions cada cop
    
### Rode NT-1 (Broadcast)

- **Especificacions:** condensador | Cardioide.
    
- **Diagnòstic:** Estàndard actual per a _Home Studio_. Al ser dinàmic i cardioide, actua com un filtre físic contra el soroll de l'habitació
    
- **Requisit:** Baixa sensibilitat. Requereix una interfície amb preamplificadors potents (més de 50dB de guany) o un activador de línia (ex: FetHead).
    
### Rode PodMic (Broadcast)

- **Especificacions:** Dinàmic | Cardioide.
    
- **Diagnòstic:** Opció econòmica i de qualitat a un microfon de condensador
    
- **Requisit:** Baixa sensibilitat. Requereix una interfície amb preamplificadors potents (més de 50dB de guany) o un activador de línia (ex: FetHead).
    

### Rode Lavalier GO (Portàtil)

- **Especificacions:** Lavalier | Omnidireccional.
    
- **Diagnòstic:** Dissenyat per a sistemes sense fils (Rode Wireless) o gravadores amb entrada TRS 3.5mm.
    
- **Avantatge:** La omnidireccionalitat permet moure el cap sense que el volum fluctuï, ideal per a presentacions dinàmiques.
    
Aquest és un tipus de microfon que NO necessita placa de só, perquè xoca en concepte
### Focusrite Vocaster Two (Bundle)

- **Components:** Interfície Vocaster + Micròfon Dinàmic (DM14v).
    
- **Diagnòstic:**
    
    - **Micròfon:** Dinàmic cardioide (equivalent funcional al PodMic).
    - **Interfície:** Dissenyada específicament per a veu. Aporta suficient guany per moure micròfons dinàmics sense generar soroll de fons (_hiss_), un problema comú en interfícies musicals barates. Inclou funcionalitats de _loopback_ (vital per a streaming).
        
