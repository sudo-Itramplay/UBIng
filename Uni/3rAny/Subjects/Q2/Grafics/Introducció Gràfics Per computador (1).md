>[!Info] Def.
>Crear una imatge d'una escena virtual 3D d'objectes gràfics des d'un punt de vista específic en un dispositiu gràfic

Elements a definir:
- Càmera
- Textura
- Model 3D
- Llums

#### Objectiu:
El principal objectiu és visualitzar (de forma realista) volums,
superfícies, (amb fonts de llum) i, segons el cas, la seva evolució
temporal.
![[Pasted image 20260214101705.png]]



>[!Info] Def.
>Visualització 3D interactiva
> Qualsevol ús de computadors per crear/interaccionar amb imatges a partir d'un món virtual

## Mesures d'eficiència
- Big O
- Nº triangles/seg
- nº/texels/seg
- FPS

## Gràfics en Computador
>[!info] Def.
>Disciplina que estudia els models i els algorismes implicats en la construci ó d'informació

#### Teoria

• Representacions bàsiques 
	(Com codificar digitalment els objectes?)
• Mostreig (sampling) i aliasing 
	(Com adquirir les dades i reproduir un senyal?)
• Mètodes numèrics 
	( Com es manipulen els senyals numèricament?)
• Radiometria i transport de la llum 
	(Com es comporta la llum?)
• Percepció 
	(Com es capta tot això pels humans?)

#### Sistemes

- Programació paral·lela, processat heterogèni
- llenguatges específics de gràfics

### Elements gràfics

● Input: 
Objectes, Llum, Càmera i mida del viewport
	● Objectes: 
		representacions 3D de geometria o volums (+Materials+Textures)
	● LLum: 
		objecte que emet fotons (una bombeta:1019 fotons/segon)
	● Càmera: 
		posició de l’observador i frustum de visió (part visible de l’escena)
	● Viewport: 
		Part de la finestra o conjunt de píxels on es formarà la imatge
		final amb Colors/Intensitats (ex. 24-bit RGB a cada píxel

● Output: Frame buffer
Buffer on es guarda la/les imatge/s finals

## Pipeline de visualització

Modelatge -> Animació -> Visualització
![[Pasted image 20260214104336.png]]

### Elements geomètrics:
#### Objectes
- **Superficials**: Nomes representen la frontera del objecte amb l'exterior
- **Volumètrics**: Es representa el volum intern dels objectes o característiques de l'espai, com la temperatura o densitat, ...

### Propietats òptiques
#### Materials:
Modelen el comportament dels objectes amb la llum:
- emissió
- absorció 
- scattering

#### Textures:
Modelen realisme adicional al comportament dels objectes, normalment amb la llum, per detallar petites característiques

### Visualització
#### Rendering:
Procés de càlcul del color al pixel final, associat normalment al càlcul de la il·luminació

**Raytracing** i **RayCasting**
![[Pasted image 20260214111235.png]]

#### Mètode Projectiu: Zbuffer
![[Pasted image 20260214111356.png]]


## Visual Mapping
![[Pasted image 20260214111434.png]]

Defineix funcó de sortida per la visualització


