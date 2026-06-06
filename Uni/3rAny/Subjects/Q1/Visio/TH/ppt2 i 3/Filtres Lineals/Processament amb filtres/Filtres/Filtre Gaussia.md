El filtre Gaussià és un altre tipus de filtre lineal de suavització

• **Mecanisme:** Utilitza pesos no uniformes, on els píxels veïns més propers tenen la major influència sobre el valor de sortida

>[!tip] base
>El nucli del filtre és una aproximació d'una funció Gaussiana 2D

• **Objectiu:** Aquest filtre **elimina components d'alta freqüència** de la imatge, per la qual cosa se l'anomena filtre "passa-baix" (_low-pass filter_)

- La suavització és útil per reduir el soroll en general



• **Control de suavització:** El paràmetre σ (variància) de la Gaussiana controla l'extensió de la suavització