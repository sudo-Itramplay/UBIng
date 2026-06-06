
Humà és molt bó reconeixent textures
	Som bons pq contenen patrons

S'han de fer assumpcions

Textura és propietat de regions i no pixels
Tipos txtura 1-stochastic 2-structural

Sorra es stochastic
pared pedra o maons és estructural

LEs texxtures depenen de distància pots identificar més coses si estàs més aprop

La textura representa que no hauries de poder contar les textures:
	Si en una cistella de mimbre pots contar cada linia, però no és viable


Amb les textures, els filtres, no ens acbaen d'ajudar
amb 2 o 3 filtres no aconseguim res

Així que es fan servvir filterbanks
	és a dir, fem ús de un porronal de filtres per tenir informació poc a poc
es fa un filtre per a cada una de les 8 direccions, amb diferents mesures i amb diferrents mascares (verticlal, horitzontal, punt)

Visualment es representen com una especie de mapa de calor


El match texxture to the quadradets, el blan és el més activat

La proporcio dels pixels veins si canviem contrast i/o ___ es manté

LBP 
si passa d'un threshhold i es considera diferent es posa un 0, i sinó un 1

Aquesta mascara binaria la passen a decimal
- Són descriptors
per el LBP ( num veins, distància dels veins)

si distància és 1 treballes amb els immediatament al cantó
si fessis (exemple) (16,1) hi hauria punts que caurien a mid pixel i es fa ns que coi pq caigui en pixel sencer


LBP es diu uniforme
	Se li mira num de transicions
	ells van decidir que si mires num de transicions <=2 estarà bé
	(Això defineix si és patró uniforme o no)


LBP és una manera simple i menys precisa de gauss


Es pot arribar a agafar un objecte per la textura


