Més enllà de l'exclusió mútua ([[Sincronització en Java]]), els [[Threads]] es coordinen per col·laborar.

**Mecanisme wait/notify** (vinculat a cada objecte):
- **`wait()`:** bloqueja el fil, **allibera el lock** i l'envia a la llista d'espera fins que el despertin o expiri un timeout.
- **`notify()` / `notifyAll()`:** desperta un (aleatori) o tots els fils en espera.
- Per fer `wait`/`notify` el fil **ha de tenir el lock** de l'objecte.
- Aplicacions: cues bloquejants, productor-consumidor, eliminar esperes actives.

**`join()`:** un fil (pare) espera que un altre acabi abans de continuar.

> Llibreria `java.util.concurrent`: col·leccions concurrents i planificació avançada.

Relacionat: [[Sincronització en Java]] · [[Problemes de Concurrència]] · [[Threads a Java]]

#assignatura/SD #tipus/teoria
