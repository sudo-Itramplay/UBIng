Com es transmeten les dades pels [[Sockets]] ([[IPC i Protocols|marshalling]]).

**Endianness** (ordre dels bytes d'una dada multi-byte, p. ex. un int de 32 bits):
- **Big-Endian (BE):** el byte més significatiu primer. És l'estàndard de xarxa (_Network Byte Order_); `(number >> 24) & 0xFF` al `bytes[0]`.
- **Little-Endian (LE):** el byte menys significatiu primer (processadors Intel x86).

**Recepcions parcials:** `read` retorna el nombre de bytes realment llegits → cal un bucle `do-while` acumulant fins al total esperat.

**Cadenes:**
- **Mida fixa:** omplir el sobrant amb espais.
- **Mida variable:** enviar primer una **capçalera** de mida coneguda amb la longitud, després la càrrega.

> Java: `DataInputStream`/`DataOutputStream`.

Relacionat: [[Sockets]] · [[TCP Stream-mode]] · [[IPC i Protocols]]

#assignatura/SD #tipus/teoria
