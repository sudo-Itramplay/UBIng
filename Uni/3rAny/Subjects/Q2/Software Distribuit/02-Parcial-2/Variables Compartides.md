Gestió de variables globals a [[Spark]]. En enviar funcions als workers ([[Transformacions i Accions|closures]]), els canvis a variables globals són **locals** i **no es propaguen** al driver ni a altres workers (no hi ha comunicació directa entre workers).

**Dues solucions:**
- **Broadcast Variables:** dades de **només lectura** enviades eficientment del driver a tots els workers (es guarden en memòria local per reutilitzar-les).
- **Accumulators:** agregació **associativa i commutativa** de valors numèrics dels workers cap al driver. **Només el driver pot llegir-los**; per als workers són de **només escriptura**. ⚠️ Només les **accions** garanteixen el processament correcte (el comportament lazy d'una transformació pot no incrementar-los).

Relacionat: [[RDD]] · [[Transformacions i Accions]] · [[Spark]]

#assignatura/SD #tipus/teoria
