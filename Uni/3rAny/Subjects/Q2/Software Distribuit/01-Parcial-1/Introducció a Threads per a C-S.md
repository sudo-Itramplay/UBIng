### Introducció: Els Fils en l'Arquitectura Client-Servidor amb Sockets

En una arquitectura client-servidor basada en sockets, el servidor sol tenir un bucle principal on espera connexions entrants mitjançant el mètode `accept()`. El problema sorgeix perquè les operacions de xarxa (lectura i escriptura en el socket) són, per naturalesa, **bloquejants**.

- **El coll d'ampolla del fil únic:** Si el teu servidor només té un fil d'execució, un cop accepta un client i comença a processar la seva petició, queda "segrestat". Si aquest client té una connexió lenta o envia moltes dades, cap altre client podrà connectar-se fins que el primer hagi acabat.
    
- **On necessitem els fils?:** Just en el moment en què el servidor accepta una nova connexió. L'estratègia clàssica consisteix a tenir un **Fil Principal** (o _Listener_) que només s'encarregui d'escoltar i acceptar connexions.
    
- **Creació de Fils de Servei:** Per a cada nova connexió acceptada, el servidor "delega" la comunicació a un nou fil (sovint anomenat _Worker_). Aquest nou fil s'encarrega de la lògica del socket específic d'aquell client, permetent que el fil principal torni immediatament a l'estat d'escolta per atendre nous clients de manera concurrent.
    
- **Escalabilitat:** Gràcies a aquesta estructura, el teu sistema pot donar servei a múltiples usuaris simultàniament, aprofitant la capacitat de la CPU per alternar entre tasques o executar-les en paral·lel si el hardware ho permet.
    

---

### Resum de Conceptes de Fils a Java

- **Sistemes Multitasca i CPU:** Els sistemes operatius moderns simulen l'execució concurrent de múltiples processos en una sola CPU mitjançant la tècnica de **temps compartit**.
    
    - - **Definició de Processos:** Un procés és una instància d'un programa en execució que té el seu propi espai de memòria. Un procés pare pot generar processos fills, però aquests solen estar aïllats entre si.
            
- **Concurrència interna (Fils):** Un fil d'execució o _thread_ és una unitat de processament dins d'un procés. A diferència dels processos, tots els fils d'un mateix procés **comparteixen els mateixos recursos** i espai de memòria.
    
- **Utilitat dels fils en l'enginyeria de programari:**
    
    - **Aprofitament de hardware:** Permeten utilitzar de manera eficient els sistemes amb múltiples processadors o nuclis.
        
    - **Simplificació del modelat:** És més natural programar tasques independents com a fils separats que com un únic flux complex.
        
    - **Events asíncrons:** Faciliten la gestió de tasques que no ocorren en un ordre predictible, com les peticions de xarxa en el teu cas dels sockets.
        
    - **Responsivitat:** Són essencials per mantenir les interfícies d'usuari (UI) actives mentre es realitzen càlculs pesats en segon pla.
        
- **Jerarquia:** Dins d'un procés, sempre hi ha un fil principal (_main thread_) que pot generar fils fills (_child threads_) per realitzar processament concurrent.