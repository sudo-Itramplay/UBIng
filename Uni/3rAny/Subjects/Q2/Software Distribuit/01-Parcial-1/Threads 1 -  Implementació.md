# Threads a Java i JVM
Aquí ens centrem en com la Màquina Virtual de Java (JVM) gestiona aquests fils i quines són les regles del joc dins d'aquest entorn.

- **Suport natiu a la JVM:** Java permet que una aplicació tingui múltiples fils d'execució corrent de manera concurrent directament sobre la seva màquina virtual.
    
- **La classe Thread:** Java encapsula tota la funcionalitat dels fils en la classe `Thread`, la qual hereta d' `Object` i implementa la interfície `Runnable`.
    
- **Cicle de vida i finalització:** Normalment, en engegar la JVM, només existeix un fil. L'execució de l'aplicació continua fins que es compleix una de les següents condicions:
    
    - Es fa una crida explícita al mètode `exit()` de la classe `Runtime`.
        
    - **Tots els fils han acabat** la seva tasca, ja sigui perquè el mètode `run()` ha retornat un valor (ha finalitzat el codi) o perquè s'ha produït una excepció no controlada que ha propagat fora d'aquest mètode.
        
- **Mecanismes de creació:** Java ofereix dues vies principals per definir el comportament d'un nou fil, permetent flexibilitat segons el disseny de la teva aplicació:
    
    1. Crear una classe que **hereti directament de la classe Thread**.
        
    2. Crear una classe que **implementi la interfície Runnable** i passar aquesta instància al constructor d'un objecte `Thread`.

# Opcions d'Implementació
Aquesta part és la més pràctica i la que segurament hauràs d'aplicar directament al teu codi de sockets per a la pràctica.

- **Opció 1: Herència de Thread:**
    
    - Cal declarar una subclasse de `Thread` i sobreescriure obligatòriament el mètode `run()`, que contindrà el codi que volem que s'executi concurrentment.
        
    - **Punt clau d'examen:** Per iniciar el fil, s'instancia la subclasse i es crida al mètode `start()`. Mai s'ha de cridar a `run()` directament, ja que llavors no es crearia un fil nou, sinó que s'executaria com un mètode normal.
        
    - Mètodes útils inclouen `sleep()` per pausar l'execució i `getName()` per identificar el fil.
![[Pasted image 20260225091551.png]]
- **Opció 2: Implementació de Runnable (Recomanat):**
    
    - Aquesta forma és més flexible perquè permet que la teva classe hereti d'una altra classe (com una classe base del teu projecte) mentre implementa el comportament de fil.
        
    - S'ha d'implementar el mètode `run()`.

    - Per engegar-lo, es crea un objecte `Thread` passant-li la teva classe `Runnable` com a argument al constructor: `new Thread(new LaTevaClasse()).start()`.
![[Pasted image 20260225091607.png]]
- **Comportament en execució:** En els exemples proporcionats ("Jamaica" i "Fiji"), es veu com els fils s'intercalen. Com que utilitzen un temps de "dormida" aleatori (`Math.random() * 1000`), l'ordre de sortida pel terminal no és predictible, demostrant la naturalesa no determinista de la concurrència.