Mecanismes per gestionar l'accés concurrent ([[Problemes de Concurrència]]).

> **Lock:** cada objecte Java té un lock únic. Si un fil $t_1$ el té, qualsevol $t_2$ que el reclami queda bloquejat fins que $t_1$ el retorni.

**Tipus:**
- **Implícita:** mètode `synchronized` → obté el lock de `this` automàticament.
- **Explícita:** bloc `synchronized(objecte)` → bloqueja només una part del codi o un objecte concret.

**Estratègies (exemple comptador):** sincronitzar tot el mètode (segur però lent), un bloc, o només la **secció crítica mínima** (incrementar i guardar en variable local) → la més eficient, allibera el lock de seguida.

> Els fils s'acaben de forma **natural** (retornant de `run()`); un fil no en pot matar un altre, només **interrompre'l**.

Relacionat: [[Problemes de Concurrència]] · [[Coordinació de Threads]] · [[Threads a Java]]

#assignatura/SD #tipus/teoria
