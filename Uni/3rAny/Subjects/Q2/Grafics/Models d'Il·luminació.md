Determinen el color d'un punt un cop trobada la [[Intersecció Raig-Objecte|intersecció]] ([[Rendering]]). Depenen de:

- Mecanismes de comportament de la llum ([[Materials]]): absorció, emissió, reflexió (scatter), transmissió.
- Tipus de [[Reflexions]]: difuses / especulars.
- Llum directa / indirecta; càlculs **locals** o **globals**.

> La intensitat total en un punt = contribució de **totes les llums** de l'escena + la intensitat **ambient** global.

**Atenuació:** la llum decau amb la distància al quadrat ($1/d^2$); sovint $1/(a + bd + cd^2)$ per a control artístic.

El model estàndard de classe és [[Blinn-Phong]].

Relacionat: [[Blinn-Phong]] · [[Ombres]] · [[Reflexions]] · [[Textures]]

#assignatura/Grafics #tipus/teoria
