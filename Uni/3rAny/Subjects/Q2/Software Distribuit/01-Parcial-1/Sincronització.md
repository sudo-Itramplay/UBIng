Determina com es comporta un procés mentre espera que una operació de comunicació acabi ([[IPC i Protocols]]).

- **Síncrones (bloquejants):** aturen l'execució fins que la tasca es completa. Simples, però poden deixar el sistema inactiu.
- **Asíncrones (no bloquejants):** el procés continua i és notificat més tard; maximitzen l'ús de CPU però són més complexes. Sovint es simula asincronia amb [[Threads]].

**Problemes de les accions bloquejants:**
- **Deadlock (interbloqueig):** dos processos s'esperen mútuament indefinidament → s'evita amb un disseny acurat del protocol.
- **Timeouts:** cal limitar l'espera perquè un `receive` no es pengi per sempre si la dada no arriba.

Relacionat: [[IPC i Protocols]] · [[Problemes de Concurrència]] · [[Threads]]

#assignatura/SD #tipus/teoria
