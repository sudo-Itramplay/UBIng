La JVM dona suport natiu a múltiples [[Threads]] concurrents. La classe `Thread` implementa `Runnable`. L'aplicació acaba quan tots els fils acaben (`run()` retorna) o amb `Runtime.exit()`.

**Dues vies de creació:**
- **Opció 1 — heretar de `Thread`:** sobreescriure `run()`. S'inicia amb **`start()`** (mai `run()` directament, o no es crea fil nou).
- **Opció 2 — implementar `Runnable` (recomanat):** més flexible (permet heretar d'una altra classe). `new Thread(new LaMevaClasse()).start()`.

> Mètodes útils: `sleep()`, `getName()`. Amb temps aleatoris, l'ordre de sortida no és predictible (concurrència no determinista).

Relacionat: [[Threads]] · [[Sincronització en Java]] · [[Coordinació de Threads]]

#assignatura/SD #tipus/teoria
