Paradigma del [[Middleware]] que abstrau la xarxa perquè el programador treballi com si els objectes fossin locals, tot i executar-se en màquines remotes.

- **Objecte Remot:** els seus mètodes són invocables des d'altres processos/màquines.
- **Objecte Local:** només accessible pel procés que el conté.
- **Abstracció:** s'orienta a **mètodes** (funcionalitats) en lloc d'intercanvi manual de missatges ([[Sockets]]).

**Invocació (crucial):**
- **Arguments no-remots:** es passen **per còpia** (han de ser `Serializable`).
- **Objectes remots:** es passen **per referència** (via la interfície remota).
- Tota crida ha de gestionar `RemoteException`.

Implementació de referència: [[Java RMI]].

Relacionat: [[Java RMI]] · [[Middleware]] · [[Web Services]]

#assignatura/SD #tipus/teoria
