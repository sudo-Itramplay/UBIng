una unió de punts d'un model -> Topologia

En cada punt d'un model hi ha dos rays (vertex)

Cordenades homogenies, definim (xyz, w) on aquest últim defineix punt/vector


Per cada punt d'un objecte volem saber la seva normal

Al modelar un objecte, a cada punt sabre la normal per poder matitzar COM arriba la llum per calcular el comportament

## Com es modelen els objectes?

Sgons objectes paramètrics


segons Malles poligonals

Intersecció de plans on formen un conjunt tancat de poligons


Els triangles també tenen intersecció








---


El que estigui més aprop de znear no fare x

més lluny de zfar no ho processare


El con aquest estara definit per vfov




frame buffer vs vviewport
	Veure definició



Integradors, 
	Formules per modular els rebots i coses de la llum? o és el que arriba a la llum

Raycasting és nomes simular el primer raig de llum

Raytracing és fer x numero de rebots (crec)

i hi ha una 3ra tecnologia


Per cada pixel x,y calculo el raig (noraml) amb la eq parametrica po+tv
observador + t(punt corresponent del pixel - obs)

la t és de intersecció

Aquesta eq dona el raig,

Si intercepta en negatiu (fora d'on està l observador, no ho volem)