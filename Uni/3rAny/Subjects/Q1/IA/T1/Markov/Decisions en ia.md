Per fer decisions en IA ja no ens serveixen els antic algorismes com A*, Minimax, alfa-beta poda o Expectimax, donat que tenen una base determinista

És a dir, sabem el cost que tindràn els diferents resultats de manera exacta

Al món real aquesta pràctica no és factible, ja que no nomes no sabem els resultats sinó que tampoc sabem si en aquells casos tindrem "soroll"


>[!Example]
>Si anem a la feina podem agafar 3 transports
>- En un model determinista sabriem el temps que tardariem en fer el trajecte, i sempre costaria aquell temps
>
>En el món real, però, tenim altres factors 
>- Si agafem el cotxe tenim una certa probabilitat de que el trànsit sigui mínim, moderat, o greu

Llavors cada estat estaria definit per diferents tipus de probabilitats (decisions de Markov)

## Markov
##### Markov 1r grau
La probabilitat de outcome, nomes depen del estat actual, ja que del estat acutal resumeix tota la informació rellevant del passat
##### Markov de 2n grau
La probabilitat de outcome, nomes depen del estat actual ==**i l'anterior**==, ja que del estat acutal podem suposar el passat,

Cada estat ara representa la decisió PERÒ no l'acció

és a dir, nosaltres tenim cotxe, tren i bici
aquests són 3 estats
Li posem un cost associat al temps que tardem i a cada estat tindrem accions

les accions van associades a unes probabilitats, que defineixen què pot passar en aquell estat

Hi ha estats que són **absorvents** en els que hi hem de passar si o  si, ens ajuda a definir metas o accions necessaries

[[Representació decisions Markov.canvas|Representació decisions Markov]]


## Com es resol un PDM?
#ProcessosDecissióMarkov

En els problemes de cerca determinista en que intervé nomes un agent, l'objectiu és trobar el pla òptim
Volem una **Política Òptima**:
$$
\prod*:S \to A
$$
Política és una funció que assigna probabilitat ad'acció a cada estat
Aquesta maximitza la utilitat si es continua el procès
el resultat és un ==agent reflex==

### PDM Superior/inferior
Quan les recompenses arriben No només al final o no sabem quan acabarà

Hi ha 3 tipus de carta: 2,3,4

Hem de dir si la seguent és superior o inferior
si fallem acaba el joc, sinó sumem punts equivalents al valor

Normalment es fa un descomote temporal, quant més tardem s'ens suma u al descomptador

les recompenses més properes en temps tenen una utilitat major