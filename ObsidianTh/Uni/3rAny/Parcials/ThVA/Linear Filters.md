# Intro
Les imatges són, en essència, matrius

Les matrius quantifiquen informació rebuda en cada graella, en la que es representa lluminositat o nivell de color

En GrayScale es fa ús de matrius amb 2 dimensions, on trobem un valor del $[0,1]$ quantificant el nivell de blanc de la cel·la

En RGB tenim 3 canals, 3 matrius sobreposades, on en cada una s'hi quantifica el nivell de color (ja sigui R, G o B) de cada cel·la


# Com mesurem qualitat d'imatge?

## Resolució espacial
### Resolució del sensor
La mida d'un element d'una escena del mon real que va a cada pixel 
(quanta info "es mneja" el pixel

### Resolució d'imatge
número de pixels (8x8, 256x512)

## Photometric Resolution
Indica quants nivells de gris pot tenir una imatge
![[2025-11-01_13-40.png]]

# Image Filtering

### Filtering :
Aplicar una funció del veí a cada pixel de la imatge
	Una funció especifica com combinar veins

##### Usos
- Millorar imatge (Denoise)
- Obtenir informació (edges)
- Detectar patrons (template matching)

## Millorar Imatge

#### Tipus de sorolls
![[2025-10-18_17-44 1.png]]

##### S&P
Punts amb el valor maximitzat o minimitzar (Blancs i negre)

>[!tip]
>s'utilitza el [[Filtre de la Mediana]] per minimitzar-lo

##### Impulse
Aparició de punts blancs en una imatge

>[!tip]
>s'utilitza el [[Filtre de la Mediana]] per minimitzar-lo

##### Gaussià
Variacions d'intesnitat dibuixats en una gaussiana

>[!tip]
>S'utilitza un Low-pass filter per minimitzar-lo

>[!note]
>En la seva fòrmula, la $\sigma$ indica que tant ample és aquest soroll (més o menys difuminat)


## Kernel : Box Filtering

Per fer els càlculs, tant per fer denoise com per aplicar-lo, apliquem màscqueres (kernels) que ens diuen com combinar els veins

-> Si tenim una mascara [1,1,1] combinarem els veins dels dos cantons, aplicant als dos el mateix pes

##### **Definició "Box Filter":** 
El "box filter" (o filtre de caixa) és el kernel més simple per fer una mitjana. També s'anomena "Mean filter" (filtre de mitjana) o "rectangular filter"

Exemple, estem fent un filtre de mitjana, si apliquem aquest box filter:

$$
H = \pmatrix{
1 & 1 & 1 \\ 1&1&1 \\ 1&1&1
}
$$
##### Apliquem una convolució:
$$
G=H*F
$$
F és la imatge

**Definició Formal:** La convolució reemplaça cada píxel per una **combinació lineal** dels seus veïns. Els "pesos" d'aquesta combinació són els valors del kernel.

##### Què fa?
Multiplica cada pes del kernel pel valor del píxel de la imatge que té a sota. Suma tots els resultats
**Normalitza:** Divideix el resultat total per la suma de tots els pesos del kernel.

##### Per Què Normalitzar? (La Divisió)
Per mantenir la brillantor de la imatge original


## Convolució
- Shift invariant : Fa shift sense alterar la imatge en resolució o proporcions
- Super posició


### Diferentes mascares, diferents resultats
imatge 1
![[Pasted image 20251101141800.png]]

#### Mascara H
$$
H = \pmatrix{
1 & 1 & 1 
}
$$
![[Pasted image 20251101141854.png]]

#### Mascara V

$$
H = \pmatrix{
1 \\ 1 \\ 1
}
$$

![[Pasted image 20251101141909.png]]

# Mascara asimetrica
![[Pasted image 20251101142001.png]]

![[Pasted image 20251101142009.png]]
Passa a 
![[Pasted image 20251101142033.png]]

(Hi ha menys pixels lo juro)

