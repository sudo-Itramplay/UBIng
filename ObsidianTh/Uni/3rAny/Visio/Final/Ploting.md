Aquí tens uns apunts detallats sobre plotting basats en els exemples dels teus fitxers (`face_detection_and_recognition.ipynb` i `P3-Video.ipynb`) i l'estil que has demanat.

---

# Apunts de Plotting (Matplotlib)

## Histogrames

Representació gràfica de la distribució de dades numèriques. Molt utilitzat per analitzar errors (com l'MSE en reconstrucció de cares) o distribucions de píxels.

```python
plt.figure(figsize=(10, 5))
plt.hist(errors, bins=30, color='salmon', edgecolor='black', alpha=0.7)
plt.title('Distribució de l\'Error')
plt.xlabel('Valor')
plt.ylabel('Freqüència')
plt.show()
```

### Paràmetres Clau

- `x` (array): Les dades d'entrada (ex: llista d'errors).
    
- `bins `(int):
    
    Nombre de barres de l'histograma.
    
    - **Com s'utilitza:** Un valor **més gran** dona més detall (més sorollós). Un valor **més petit** agrupa més les dades (més suau).
        
- `color` (string):
    
    Color de farciment de les barres (ex: 'salmon', 'blue').
    
- `edgecolor` (string):
    
    Color de la línia que envolta cada barra.
    
    - **Com s'utilitza:** Essencial per **separar visualment** les barres, especialment si tenen el mateix color. `'black'` és l'estàndard per claredat.
        
- `alpha` (float, 0-1):
    
    Nivell de transparència.
    
    - **Com s'utilitza:** Útil quan superposes dos histogrames per veure on s'intersecten. `1` és opac, `0` és invisible.
        

**Quan s'utilitza?** Per entendre com estan distribuïdes les teves dades (ex: si els errors de reconstrucció segueixen una distribució normal o tenen _outliers_).

---

## Línies de Referència (Horitzontals i Verticals)

S'utilitzen per marcar llindars, mitjanes o límits específics sobre un gràfic existent.

```python
# Línia Vertical (ex: marcar la mitjana)
plt.axvline(x=mitjana, color='red', linestyle='--', label='Mitjana')

# Línia Horitzontal (ex: marcar un llindar màxim)
plt.axhline(y=llindar, color='green', linestyle='-', linewidth=2)
```

### Paràmetres

- `x` / `y` (float): La posició on es dibuixa la línia.
    
- `color` (string): Color de la línia per destacar-la (ex: `'red'` per alertes).
    
- `linestyle` (string):
    
    Estil del traç.
    
    - **Com s'utilitza:** `'-'` (sòlid), `'--'` (discontinu/dashed), `':'` (puntejat). Les línies discontínues s'usen sovint per referències teòriques o mitjanes.
        
- `label` (string):
    
    Etiqueta per a la llegenda (plt.legend()).
    

**Quan s'utilitza?** Per comparar les dades amb un valor de referència estàtic (ex: "La mitjana d'error és aquí" o "Aquest és el límit de detecció").

---

## Punts (Scatter Plots)

Visualització de dades com a punts individuals en un espai 2D (o 3D).

```python
# Opció 1: Scatter (més control sobre mida/color individual)
plt.scatter(x_coords, y_coords, c='blue', s=10, marker='o')

# Opció 2: Plot (més ràpid per a punts simples)
plt.plot(x_coords, y_coords, 'r.', markersize=5) 
```

### Paràmetres

- `c` / `color` (string/array): Color dels punts. Pot ser una llista per assignar un color diferent a cada punt (clústering).
    
- `s` / `markersize` (float): Mida del punt.
    
- `marker` (string):
    
    Forma del punt.
    
    - **Com s'utilitza:** `'o'` (cercle), `'.'` (punt petit), `'x'` (creu), `'+'` (més). Útil per diferenciar classes en classificació.
        

**Quan s'utilitza?** Per veure la relació entre dues variables, visualitzar núvols de punts (features), o mostrar resultats de classificació (ex: cares vs no-cares en un espai de característiques).

---

## Imatges i Vídeos (Frames)

Visualització de matrius de dades com a imatges. Fonamental en Visió per Computador.

```python
# Mostrar una imatge estàtica
plt.imshow(imatge_rgb)
plt.axis('off') # Amagar eixos si no són rellevants
plt.show()

# Mostrar en escala de grisos
plt.imshow(imatge_gray, cmap='gray')
```

### Visualització de "Vídeo" (Seqüència d'imatges)

En els notebooks (Jupyter), els vídeos es tracten sovint com una seqüència de frames o utilitzant `matplotlib.animation`.

```python
import matplotlib.animation as animation

fig = plt.figure()
ims = []

# Bucle per processar cada frame
for frame in video_frames:
    # Processament del frame...
    im = plt.imshow(frame, animated=True)
    ims.append([im])

ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True)
plt.show()
```

### Paràmetres (`imshow`)

- `X` (array): La imatge (H, W, 3) per RGB o (H, W) per grisos.
    
- `cmap` (string):
    
    Mapa de colors.
    
    - **Com s'utilitza:** `cmap='gray'` és obligatori per veure imatges en blanc i negre correctament (si no, Matplotlib els posa colors falsos verdosos/liles).
        
- `vmin`, `vmax` (float):
    
    Fixen el rang de valors per al color.
    
    - **Com s'utilitza:** Útil per augmentar el contrast o quan les dades no estan normalitzades entre 0-255 o 0-1.
        

**Quan s'utilitza?** Sempre que treballis amb píxels, matrius de característiques visuals o resultats de segmentació.


## Visualització de Múltiples Imatges (Subplots)

Quan necessites mostrar una graella d'imatges (ex: eigenfaces, frames d'un vídeo, resultats de cerca).

### Mètode `plt.subplots`

És la forma més neta de crear una graella.

```python
# Creem una graella de 2 files x 5 columnes
fig, axes = plt.subplots(2, 5, figsize=(15, 6))

# 'axes' és una matriu (array) d'eixos. L'aplanem (flatten) per iterar fàcilment
for i, ax in enumerate(axes.flat):
    # Suposem que 'images' és una llista d'imatges
    if i < len(images):
        ax.imshow(images[i], cmap='gray')
        ax.set_title(f"Imatge {i}")
        ax.axis('off') # Important: Treure els eixos (números) per neteja
```

### Paràmetres Clau

- **`figsize=(ample, alt)`**: Controla la mida total de la figura. Si les imatges es veuen aixafades, ajusta això.
    
- **`axes.flat`**: Converteix la matriu 2D d'eixos en una llista 1D, fent molt fàcil fer un bucle `for`.
    

---

## Problemes i Formats d'Imatge (Critical)

Matplotlib és flexible, però si no li dones el format esperat, la imatge pot sortir negra, blanca o amb colors psicodèlics.

### A. Escala de Grisos vs RGB (Dimensions)

- **El problema:** Una imatge en escala de grisos té forma `(H, W)`. Si la plotejes directament, Matplotlib li aplica un mapa de colors per defecte ("Viridis", verdós/lila).
    
- **La solució:** Sempre especificar `cmap='gray'`.
    

```python
# Imatge (H, W) -> Necessita cmap='gray'
plt.imshow(img_gray, cmap='gray') 

# Imatge (H, W, 3) -> NO necessita cmap (Matplotlib detecta RGB automàticament)
plt.imshow(img_rgb) 
```

### B. Tipus de Dades (Float vs Int) i Rangs

Matplotlib interpreta els valors segons el tipus de dada:

1. **`uint8` (Enter 0-255):** Matplotlib espera valors entre 0 i 255.
    
2. **`float` (Decimal 0.0-1.0):** Matplotlib espera valors entre 0 i 1.
    

- **Error Comú 1 (Imatge Blanca):** Tens una imatge en `float` però amb valors de 0 a 255 (ex: `200.5`). Matplotlib veu valors > 1 i els pinta tots com a blanc màxim (clipping).
    
    - _Solució:_ Normalitza (`img / 255.0`) o converteix a int (`img.astype('uint8')`).
        
- **Error Comú 2 (Imatge Negra):** Tens una imatge `uint8` però amb valors molt baixos (0 o 1).
    
    - _Solució:_ Escala els valors (`img * 255`).
        

### C. Contrast i Normalització Visual

De vegades la imatge té el format correcte però poc contrast. Pots forçar els límits de visualització sense canviar les dades:

```python
# vmin i vmax forcen que el color negre comenci a 0 i el blanc a 255
# Útil si la teva imatge té un rang estrany (ex: de 50 a 100)
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
```

### Resum Ràpid de comprovació

Abans de fer `plt.imshow()`, fes un print:

1. `print(img.shape)`: És 2D o 3D?
    
2. `print(img.dtype)`: És `float` o `uint8`?
    
3. `print(img.max())`: És > 1? Si és float i > 1, es veurà blanca.