La potència de les BD modernes rau en la **multiusuarietat**: executar diverses [[Transacció|transaccions]] alhora. Hi ha dos tipus de processat:

**1. Processament Intercalat (Interleaved):**
- Concurrència clàssica amb **un sol CPU**; la simultaneïtat és una il·lusió per la velocitat de commutació.
- El CPU executa instruccions d'un procés, el suspèn i passa al següent; en reprendre's continua on s'havia quedat.
- Manté el CPU ocupat durant les esperes d'E/S i garanteix **justícia** (fairness).
- La majoria de la teoria de control de concurrència ([[Schedules i Serialitzabilitat|serialitzabilitat]]) es basa en aquest model.

**2. Processament Paral·lel (Parallel):**
- Concurrència **real i física**; exigeix **múltiples CPUs**.
- Els processos s'executen realment al mateix instant, sense intercalar.

Sense control apareixen els [[Problemes de Concurrència]].

Relacionat: [[Transacció]] · [[Problemes de Concurrència]] · [[Schedules i Serialitzabilitat]]

#assignatura/BD #tipus/teoria
