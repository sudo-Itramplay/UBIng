Comunicació orientada a la connexió amb [[Sockets]] **Stream (TCP)**. El servidor sempre ha d'estar preparat abans que el client actuï.

**Cicle del servidor:** crear `ServerSocket` → escoltar (`listen`) → **`accept()`** (bloquejant; crea un nou socket de **dades** per client) → I/O (`InputStream`/`OutputStream`) → tancar. El servidor usa dos sockets: un de connexió (escolta) i un de dades per client.

**Cicle del client:** crear `Socket(IP, port)` → obtenir streams → protocol → tancar.

- **`setSoTimeout()`** llança `InterruptedIOException` si expira.
- ⚠️ Gestionar **recepcions parcials:** `read` no garanteix llegir tots els bytes de cop → bucle fins a completar.
- Tancar sempre amb `finally`.

Relacionat: [[Sockets]] · [[UDP Datagram-mode]] · [[Endianness i Marshalling]] · [[Tipus de Servidors]]

#assignatura/SD #tipus/teoria
