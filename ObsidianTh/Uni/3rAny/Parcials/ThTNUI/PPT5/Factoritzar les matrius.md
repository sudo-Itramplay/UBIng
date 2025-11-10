---
aliases:
  - MF
  - Matrix Factorization
---

Técnica d'aprenentatge automàtic, especialment utilitzada en sistemes recomanadors, per descompondre una matriu d'interaccions usuari-ítem en productes de matrius de factors latents de dimensions inferiors.

![[Pasted image 20251014134409.png]]
## Matriu d'interaccions

- Tenim un conjunt de dades amb les valoracions que diferents usuaris han donat a diferents ítems 
	- (per exemple, usuaris valorant pel·lícules). 
	
- Podem organitzar aquesta informació en una matriu que anomenarem $R$.

### R
- **Files($U$):** Cada fila representa un usuari únic del conjunt U.

-  **Columnes($D$):** Cada columna representa un ítem únic del conjunt D.

 - **Cel·les (Rij​):** El valor a la cel·la (i,j) és la valoració que l'usuari i ha donat a l'ítem j.



Normalment, aquesta matriu és molt **gran** i **esparsa** (plena de valors buits), ja que un usuari mitjà ha valorat només una petita fracció dels ítems disponibles.

## Descompondre per aproximar
L'objectiu de la **factorització de matrius** és trobar dues matrius més petites, anomenades P i Q, el producte de les quals ens doni una bona aproximació de la matriu original R.

$$
P×Q^T=\hat R≈R
$$

Aquestes noves matrius representen **factors latents** ([[Uni/3rAny/Parcials/ThTNUI/PPT5/Features]])(característiques ocultes o abstractes) que expliquen per què un usuari ha donat una certa valoració a un ítem.


### **Matriu d'Usuaris (P)**

- **Dimensions:** 
	$∣U∣×K$.

- **Contingut:** 
	Cada fila d'aquesta matriu és un vector que representa un usuari en un espai de K dimensions. Aquest vector descriu les preferències de l'usuari segons els K factors latents.

- **Exemple:** 
	Si K=2 i els factors latents fossin "afinitat per la ciència-ficció" i "gust per la comèdia", el vector d'un usuari podria ser `[0.9, 0.2]`, indicant una alta preferència per la ciència-ficció i baixa per la comèdia.


### **Matriu d'Ítems (Q)**

- **Dimensions:** 
	∣D∣×K.
    
- **Contingut:** 
	Cada fila és un vector que representa un ítem en el mateix espai de K dimensions. Descriu les característiques de l'ítem segons aquests factors.
    
- **Exemple:** 
	Una pel·lícula de ciència-ficció amb tocs d'humor podria tenir el vector `[0.8, 0.4]`.
    

### **El Nombre de Factors Latents (K)**

- K és un hiperparàmetre que triem nosaltres.
    
- És un nombre significativament més petit que el nombre d'usuaris i d'ítems ($K≪∣U∣$ i $K≪∣D∣$).
    
- Aquesta reducció de dimensionalitat és clau: ens força a capturar els patrons més importants de les dades, ignorant el soroll i ajudant a generalitzar millor.

## Com funciona?
Per calcular la valoració predita, haurem de fer el càlcul d'una de les [[Uni/3rAny/Parcials/ThTNUI/PPT5/Features]]

## [[Uni/3rAny/Parcials/ThTNUI/PPT5/Com Factoritzar Matrius?]]