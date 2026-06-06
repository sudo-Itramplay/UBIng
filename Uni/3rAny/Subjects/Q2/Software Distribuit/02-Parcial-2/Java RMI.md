**Remote Method Invocation:** desenvolupar aplicacions d'[[Objectes Distribuïts]] amb la mateixa sintaxi que les aplicacions Java locals.

**Components:**
- **Interfície Remota:** el contracte; ha d'estendre `java.rmi.Remote` i cada mètode declarar `RemoteException`.
- **Implementació (`Impl`):** el codi real; hereta d'`UnicastRemoteObject` (per ser exportada i escoltar peticions). És **concurrent** (un fil per petició → cal [[Sincronització en Java|sincronitzar]]).
- **RMIRegistry:** servei de noms (port **1099**); el servidor publica amb `bind`/`rebind`, el client cerca amb `lookup` (`rmi://host:port/name`).

**Bootstrap:** una JVM no neix amb referències remotes → usa el registre per localitzar el primer objecte; després pot rebre'n més via **callbacks**.

> [!fail] Error comú
> El client només ha de conèixer la **interfície**; el casting del `lookup` es fa cap a la interfície, mai cap a la classe d'implementació.

**Pas de paràmetres:** per **còpia** (`Serializable`) o per **referència** (objectes `Remote`).

Relacionat: [[Objectes Distribuïts]] · [[Middleware]] · [[Sincronització en Java]]

#assignatura/SD #tipus/teoria
