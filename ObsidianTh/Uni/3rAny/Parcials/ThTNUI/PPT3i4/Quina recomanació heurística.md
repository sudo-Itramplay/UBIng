Donada una definició de distància entre usuaris, podriem pensar en una proposta inicial (molt simple) de recomanació a un usuari $A$:
- Podem buscar un usuari semblant ($A'$) i recomanar una pelicula que hagi agradat a $A'$ a $A$

>[!warning] Compte!
>Aquesta estratègia no és perfecte, atès que podríem recomanar pel·lícules que tothom a puntuat malament excepte

Una possible solució a aquest problema és fer una ponderació de les puntuacions amb tots els usuaris. Aquesta serà la nostra primera proposta de recomanador, que és **heurística**!