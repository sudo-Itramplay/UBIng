## Definició
El Descens de Gradient Estocàstic (_Stochastic Gradient Descent_, **SGD**) és una alternativa eficient al Descens de Gradient tradicional (Batch Gradient Descent) quan el **volum de dades és molt gran** i el càlcul del gradient a partir de _totes_ les dades (_costosa i lenta_) no és viable.


>[!NOTE] Breu
>És el [[Uni/3rAny/Parcials/ThTNUI/PPT1i2/Descens del gradient]] agafant una dada aleatoria cada cop.


## Càlcul
L'eficàcia de l'SGD es basa en la propietat **additiva** de la majoria de **funcions d'error (o de cost)** en l'aprenentatge automàtic:

$E(θ)= \sum L(f(x_i​; θ ),y_i​)$


on :
- E és l'error total
- θ són els paràmetres del model
- L és la funció de pèrdua per a cada punt de dada i.

L'SGD aprofita això calculant el gradient (la direcció del màxim pendent) no sobre la suma total, sinó a partir de l'estimació d'una **única dada** o d'un **conjunt petit de dades** anomenat _mini-batch_.

## Algorisme
L'algorisme es repeteix fins a la convergència o un nombre fix d'iteracions:

1. **Selecció Aleatòria:** Tria una **única dada** d'entrenament xi​ (o un _mini-batch_ de dades B) del conjunt total.
    
    - _Condició clau:_ A cada cicle (_epoch_), s'ha de **iterar sobre les dades en ordre aleatori** per garantir la convergència al mínim local.
    
2. **Càlcul del Gradient Estocàstic:**
    
    - Calcula el **[[Uni/3rAny/Parcials/ThTNUI/PPT1i2/Gradient|gradient]] ∇Ei​(θ)** de la funció de cost utilitzant **només** la dada (o _mini-batch_) seleccionada.
    
    - Aquest gradient indica la direcció d'augment del cost _per a aquesta mostra específica_.
    
3. **Actualització de Paràmetres (Pas):**
    
    - Ajusta els paràmetres del model (θ) en la **direcció oposada** al gradient estimat (és a dir, cap al mínim):
        
        θ←θ−η⋅∇Ei​(θ)
	    
    - On η (eta) és la **taxa d'aprenentatge (_learning rate_)**, que controla la mida del pas.

- **Batch GD** - [[Uni/3rAny/Parcials/ThTNUI/PPT1i2/Descens del gradient]]
	- Tot el conjunt de dades (Batch)
	- Molt precisa
	- Molt lenta
- **SGD** 
	- Una sola dada o _mini-batch
	- Sorollosa (Estocàstica)
	- Molt ràpida (més iteracions)