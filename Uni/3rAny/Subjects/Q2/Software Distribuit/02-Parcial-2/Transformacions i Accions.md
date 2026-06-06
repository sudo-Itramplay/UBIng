Els dos tipus d'operacions sobre [[RDD|RDDs]] a [[Spark]].

**Transformacions** — creen un nou RDD a partir d'un altre. **Avaluació mandrosa (lazy):** no es computen fins que cal; Spark guarda el **graf** de transformacions (una "recepta") per optimitzar i recuperar-se de fallades.
- `map(func)`, `filter(func)`, `distinct()`, `flatMap(func)`.

**Accions** — forcen l'execució del graf i extreuen resultats fora del framework.
- `reduce(func)` (func commutativa i associativa), `take(n)`, `collect()` (⚠️ tot el dataset al driver — ha de cabre en memòria!), `takeOrdered(n)`.

**Cicle de vida:** Creació → Transformació → Persistència (opcional) → **Execució** (acció).

Relacionat: [[RDD]] · [[Variables Compartides]] · [[Spark]]

#assignatura/SD #tipus/teoria
