# Problemes Fonamentals i Seguretat en la Concurrència

En l'àmbit de la programació multithread, ens enfrontem a tres tipus de problemes crítics que afecten la integritat del sistema:

### Problemes

1. **Problemes de seguretat**: Hem de garantir que l'accés simultani a zones de memòria no corrompi les dades. La solució principal són les **regions d'exclusió mútua**, que eviten que diversos fils executin simultàniament instruccions que comprometin la integritat de la informació.

2. **Problemes d'esperes**: Es defineixen tres estats patològics:
    
    - **Deadlock**: Bloqueig mutu entre dos o més processos que s'esperen l'un a l'altre.
        
    - **Starvation**: Un procés no pot avançar mai perquè els recursos s'assignen de forma injusta a daltres.
        
    - **Livelock**: Els processos estan actius i realitzen còmput, però no són capaços de progressar cap als seus objectius.
        
3. **Problemes d'eficiència**: Cal maximitzar el còmput simultani real per aprofitar el maquinari.
    
4. **Condició de carrera (Race Condition)**: Passa quan el resultat final depèn de l'ordre d'execució dels fils. Un exemple típic és un comptador compartit:
    
    - Si dos fils llegeixen el valor "0" alhora , ambdós l'incrementen a "1" i el tornen a guardar , el resultat final serà "1" en lloc de "2".
	
    - Això demostra que la modificació de dades compartides, com un `count++`, ha de ser operació **sincronitzada**.

# 2. Sincronització en Java: Locks i Regions Crítiques

Java proporciona mecanismes natius per gestionar l'accés concurrent mitjançant el concepte de bloqueig o "lock":

 >[!info] **El concepte de Lock**: 
 >Cada objecte a Java té associat un lock únic que pot ser reclamat per qualsevol fil. Si un fil $t_1$ té el lock, qualsevol altre fil $t_2$ que el reclami quedarà bloquejat fins que $t_1$ el retorni.

- **Tipus de sincronització**:
    
    - **Implícita**: Es defineix un mètode amb la paraula clau `synchronized`. El fil obté el lock de l'objecte (`this`) automàticament abans d'executar el mètode.
	
    - **Explícita**: Es defineix un bloc `synchronized(objecte)` dins d'un mètode. Això permet bloquejar només una part específica del codi o bloquejar un objecte diferent a `this`.
![[Pasted image 20260225092218.png]]
- **Estratègies per sincronitzar un comptador (Exemple Servlet)**:
    
    - **Alternativa 1 (Mètode complet)**: Sincronitzar tot el mètode `doGet`. És segur però poc eficient, ja que bloqueja tot el servei per a cada petició.
    ![[Pasted image 20260225092239.png]]
    - **Alternativa 2 (Bloc synchronized)**: Sincronitzar només el bloc que incrementa i imprimeix. Millora lleugerament el control però encara manté el lock durant l'E/S (PrintWriter).
    ![[Pasted image 20260225092255.png]]
    - **Alternativa 3 (Secció crítica mínima)**: Sincronitzar només l'increment de la variable compartida i guardar-lo en una variable local (`local_count`). És la més eficient perquè el lock s'allibera immediatament després de la modificació, permetent que altres fils continuïn mentre s'imprimeix la resposta.
    ![[Pasted image 20260225092309.png]]

### 3. Gestió del Deadlock i Cicle de Vida del Thread

Un dels errors més comuns i difícils de depurar és el bloqueig mutu o Deadlock:

- **Definició de Deadlock**: Situació on un conjunt de fils estan esperant esdeveniments (alliberament de recursos) que només poden ser causats per altres fils del mateix conjunt, generant una espera infinita.
    
- **Prevenció de Deadlocks**: Una estratègia clàssica és l'**ordenació de recursos**. Si tots els fils sol·liciten els recursos (locks) exactament en el mateix ordre, és impossible que es produeixi una espera circular.
![[Pasted image 20260225092500.png]]
- **Exemple de risc**: Si el fil $T_1$ agafa el lock de l'objecte 1 i després de l'objecte 2 , mentre que el fil $T_2$ agafa primer el de l'objecte 2 i després el de l'objecte 1, es pot produir un Deadlock si ambdós agafen el seu primer lock simultàniament.

- **Finalització de Threads**:
    
    - Els fils s'han d'acabar de manera **natural**, retornant del mètode `run()`.
        
    - **Regla d'or**: Un fil no pot finalitzar-ne un altre de manera forçada.
        
    - Per aturar un fil, se li ha d'enviar una **senyal d'interrupció**, i és el propi fil receptor qui ha de gestionar aquesta senyal i decidir acabar la seva execució.

# Coordinació de Threads: Wait, Notify i Join

Més enllà de l'exclusió mútua, els fils necessiten coordinar-se per col·laborar en tasques complexes:

- **Mecanisme wait/notify**: És un sistema d'esperes i notificacions vinculat a cada objecte.
    
    - **`wait()`**: Bloqueja el fil actual, allibera el lock i l'envia a una llista d'espera de l'objecte fins que algú el desperti o s'esgoti un timeout.
	![[Pasted image 20260225092644.png]]
    - **`notify()` / `notifyAll()`**: Desperta un (aleatori) o tots els fils que estan esperant en la llista de notificació d'aquell objecte.
	
    - **Condició d'ús**: Per fer un `wait` o `notify`, el fil **ha de tenir el lock** de l'objecte per evitar condicions de carrera en la pròpia llista de notificació.
        
    - **Aplicacions**: Útil per a cues bloquejants (esperar si la cua és buida), protocols productor-consumidor i per eliminar les costoses "esperes actives" (bucles que consumeixen CPU sense fer res).
        
- **Mètode `join()`**: S'utilitza quan un fil (per exemple, el pare) ha d'esperar que un altre fil acabi la seva feina abans de continuar. És comú en estructures on es llancen diversos "fills" i el pare recull els resultats al final.

- **API `java.util.concurrent`**: Java ofereix una biblioteca completa amb col·leccions concurrents i mecanismes avançats de planificació de tasques que faciliten la programació multithread moderna.

### Exemple wait i notify
![[Pasted image 20260225092731.png]]

### Exemple de join:
![[Pasted image 20260225092749.png]]