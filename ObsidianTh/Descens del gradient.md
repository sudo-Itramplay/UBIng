És un **[[Algorisme d'optimització]]**

La regla d'actualització dels paràmetres del model (representats per θ) és:

$θnou​=θantic​−α⋅∇J(θantic​)$

On:

- **$θnou$​:** Els nous valors dels paràmetres (pesos i biaixos).
    
- $θantic​:$ Els valors actuals dels paràmetres.
    
- $α (Taxa d'Aprenentatge)$: És un **hiperparàmetre** (un valor que es defineix abans de l'entrenament) que controla la **mida del pas** que es fa en la direcció del descens.
    
    - Si α és massa petit, la convergència serà molt lenta.
        
    - Si α és massa gran, l'algorisme pot sobrepassar el mínim i no convergir (divergència).
        
- $∇J(θantic​)$: El [[Gradient]] de la funció de cost en el punt actual, que indica la direcció a moure.