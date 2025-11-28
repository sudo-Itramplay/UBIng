## Aprenentatge supervisat
	Tens exemples dels quals pots apendre

Classificador, entra una (exemple) imatge i retorna etiquetes

## Aprenentatge per reforç
	aniràs intentant i repetint fins obtindré què et dona la recompensa i com
Intentem jugar a un joc de taula sense regles
Pren decisions de manera no informada, arriscant-se, per poder apendre



Si estic a estat s, i dsps al a, arribo a s'

Es fa servit $T$ per referirse a la transició


L'objectiu d'un problema per reforç és la recompensa, la base, el que importa
	objectiu: trobar camí per obtenir recompensa max
Per reinforcement

necessitem formula de transició i recompensa



# AL principi
No coneixem T
no coneixem R

ens donen una Politica fixa (P)

objectiu: Apendre els valors dels diferents estats
Calen 4 coses
s són els estats
a són les accions ---> definim accions: moures direcció :a=(Nord, south, east, west)
funció transició
funció recompensa

Aquestes últimes no les sé

En cas que sempre pugui arribar sens probabilitats és determinista i la matriu transició és diagonal

Funció Recompensa no la tenim al principi: 
	Cal que per cada decisió s'obtingui una recomepensa negativa, volem obtenir la decisió menys negativa

La gràcia del reforç és que no és força bruta, no passarem per tots els estats
V = el valor que 
V és el que volem acabar suposant

V serà un vector per tots els estats que tenim inicialitzats tots amb el mateix valor(molt petit, xom 0,01) 

començarem triant estats de manera aleatoria
Es valorarà en funció al que nosaltres hem triat com estat
Al principi, com no sabem res, anirem cap a qualsevol cantó

Un copens hem mogut, sabrem quina recompensa té moure's, que hi ha associat moures a aquella casella

la estimació de recompensa d'aquell punt:
gamma és descompte temporal
$$
\hat r = \gamma v(s_i)-v_{i+1}
$$

i amb això podrem fer $S= r_{real} - \hat r$

I amb algo de RPE obtindrem V restantlo a no se que beta i actualitzarem el valor de la taula (llista) de V


Temporal diference TD

Policy implementa la decisió, la lògica, i afavorir les accions que donguin més recompensa

Policy és una matriu estat i acció

Si algo em retorna més valor del que esperava, puc anar a policy i afegir-hi preferència



V aprens a com està distribuida la recompensa

$\Pi$ aprens com triar 



La funció de politica 

Iteració de valor: fem servir V, que no depen de les funcions

No optimitza la suma de recompenses, sinó la suma de recompenses en mitja


V no dona cap criteri per triar