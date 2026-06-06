# Concepte i Utilitat de les Ombres

Com a concepte fonamental, cal entendre què representa una ombra en el context de la generació d'imatges.

 >[!info] Defincio
 >Les ombres es defineixen formalment com aquelles regions de l'escena que no són visibles des de les fonts de llum.
 >
    
- La seva utilitat pràctica és doble i crucial per al realisme: 
	- d'una banda, ens donen una major sensació de tridimensionalitat (3D) en la imatge generada.
	
	- D'altra banda, proporcionen a l'observador pistes visuals indispensables sobre les formes geomètriques i el posicionament relatiu dels objectes en l'espai 3D.


>[!warning] Compren la diferencia
> Assegureu-vos de comprendre que l'ombra no és un objecte geomètric per si mateix, sinó l'absència d'il·luminació directa a causa d'una oclusió.

# Integració d'Ombres en Ray Tracing i Blinn-Phong

Aquesta secció és vital per a l'examen, ja que detalla el nucli algorísmic. L'algorisme llança un raig per cada píxel i avalua la intersecció amb els objectes.

- La integració en l'algorisme de Ray Tracing es fa mitjançant els anomenats "rajos d'ombres", que són rajos que es tracen des del punt d'intersecció trobat cap a les llums de l'escena.

![[Pasted image 20260303085652.png]]


- Si el raig intersecta un objecte (`hit(ray)`), es crida a la funció `computeLocalLighting()` per calcular la il·luminació local en aquell punt de contacte.

![[Pasted image 20260303085736.png]]



- Per fer aquest càlcul matemàtic, s'utilitza una versió modificada del model d'il·luminació de Blinn-Phong.

- Aquest model modificat afegeix un factor d'ombra a la fórmula de la intensitat total: $$I~total=Ia\_global*Ka+\sum_{i=1}^{numLLums}factor\_Ombra_{i}\cdot atemacio_{i}[difusa_{i}+especular_{i}]+ambient_{i}$$

- El comportament d'aquest paràmetre és binari en llums puntuals: el factor d'ombra és 0.0 si la llum està totalment ocluïda per un objecte opac.
    
- Per contra, el factor d'ombra adquireix el valor 1.0 si no hi ha cap objecte opac que s'interposi entre la font de llum i el punt d'intersecció avaluat.

### Per si ajuda a la pràctica
![[Pasted image 20260303085759.png]]
![[Pasted image 20260303090022.png]]

# El Problema de l'Auto-intersecció ("Shadow Acne")

Aquest és un dels errors gràfics més freqüents a l'hora d'implementar un Ray Tracer, i és una pregunta clàssica d'examen.

- En calcular les ombres, sovint spareix el problema de les auto-interseccions, un fenomen també conegut amb el nom tècnic de "shadow acne".
    
- Aquest artefacte visual és, en essència, un problema de precisió matemàtica dels nombres en coma flotant, on un objecte s'intersecta erròniament a si mateix enfosquint la seva pròpia superfície.
    
- La definició matemàtica del raig cap a la llum s'expressa com $p=p0+iambda^{*}L$, on l'origen és el punt d'intersecció.
    
- Per solucionar de forma elegant aquest problema, la tècnica consisteix a desplaçar lleugerament el punt d'origen del raig d'ombra en la direcció del vector de la llum.
    
- A la pràctica, el punt d'intersecció inicial es canvia aplicant la fórmula $p0=p0+\epsilon^{*}L$, sent $L$ el vector que va des de la superfície a la posició de la llum.
    
- Típicament, s'assigna a $\epsilon$ un valor molt petit per evitar pertorbar el càlcul, utilitzant freqüentment $\epsilon=0.01$ com a estàndard.

# Ombres i penombres

### Soft Shadows (ombres i penombres):

- Un dels inconvenients d'utilitzar fonts de llum puntuals és que produeixen ombres amb vores extremadament dures, poc naturals.

- Per aconseguir un major realisme, es considera que les llums tenen una àrea determinada i no són simples punts; això és el que produeix les penombres o "soft shadows".

![[Pasted image 20260303090215.png]]

>[!info] Penombra
> Visualment queda representat per aquesta difuminacio de les ombres, ja que son punts els quals no queden totalment visibles pel focus de llum, però algun raig hi rebota, produint difuminat

>[!done] Umbra vs Penumbra
>- L'umbra és la regió de l'espai completament ombrejada on no arriba cap fracció de la llum (fully shadowed region).
>
>- La penumbra, en canvi, és la regió parcialment ombrejada, on arriba només una part de l'energia lluminosa (partially shadowed region).

Les llums amb àrea fan ombres suaus per què:
- alguns punts “veuen” tota la llum - totalment il·luminats
- alguns punts no “veuen” res de la llum - ombra
- alguns punts veuen part de la llum - penombra


![[Pasted image 20260303090309.png]]

### Com es calcula?
Algorísmicament, això se simula llançant diversos rajos d'ombra dispersos des d'un mateix punt de la superfície cap a diferents parts de la llum d'àrea.

- Finalment, es pondera el factor d'ombra d'aquell punt calculant la proporció de rajos llençats que efectivament assoleixen veure la font de llum lliure d'obstacles.

## Ombres amb Objectes Transparents

La complexitat algorísmica augmenta quan els oclusors no són totalment opacs, sinó que permeten el pas parcial de la llum.

> [!warning] Calcul de transparencia
> Quan cal calcular un raig d'ombra que travessa objectes transparents, la geometria es tracta com si fos transparent, però amb una simplificació: 
> - Es calcula sense tenir en compte la refracció del raig de la llum per estalviar cost computacional.

### Com és el calcul de Transparencia?

- El procediment comença calculant matemàticament el gruix exacte de l'objecte transparent que travessa el raig d'ombra.
	- Aquest gruix, denominat amb la variable $d'$, s'obté avaluant la distància entre les dues interseccions (d'entrada i sortida) del raig amb la geometria de l'objecte.

- Seguidament, es defineix un factor d'atenuació intrínsec al material transparent en qüestió, el qual es formula com $fah=1.0 / dmax$.
	- El paràmetre dmax representa el gruix límit teòric de l'objecte que provocaria que la llum no pogués passar en absolut.

- Un cop obtinguts aquests paràmetres, es procedeix a calcular el factor d'ombra definitiu mitjançant l'equació: factor d'ombra = $(1.0-fah^{*}d^{\prime})$.

- Aquest nou factor calculat és el que s'aplicarà de manera directa a la component difusa directa i a la component especular directa dins de la fórmula general d'il·luminació de Blinn-Phong per atenuar la llum.




