Primera fase del [[Fases d'un Compilador|compilador]]: llegeix el fitxer de caràcters i els agrupa en **tokens** (identificadors, paraules reservades, operadors, puntuació…). Es construeix amb **autòmates** que reconeixen cada categoria.

- **Identificadors (C):** comencen per lletra o `_`, seguits de lletres/dígits/`_`.
- **Enters:** transicions de dígits, amb signe opcional.
- **Operadors:** distingir simples (`+`) i compostos (`++`, `+=`).
- **Comentaris:** s'han de "saltar" (`/* ... */`).
- **Integració:** un gran autòmata que aglutina les categories, fet determinista ([[Conversió NFA a DFA]]) amb estat d'error.

**Caràcter d'avanç:** algunes categories (identificadors, enters) només acaben en llegir el símbol següent → en l'estat d'acceptació **no** es llegeix el caràcter següent. Les **paraules reservades** es comproven amb una taula.

Relacionat: [[Fases d'un Compilador]] · [[Conversió NFA a DFA]] · [[λ-tancament]]

#assignatura/LL #tipus/teoria
