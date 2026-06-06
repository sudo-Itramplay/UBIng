Un **socket** és el **punt final d'un enllaç de comunicació** entre dos processos en màquines (possiblement) diferents. L'API encapsula els detalls del SO i és coherent amb l'ús de fitxers en Unix.

**Tres tipus segons el protocol de transport:**
- **Stream (SOCK_STREAM) — TCP:** flux **bidireccional, fiable, seqüencial i sense duplicats**. Model de **flux de bytes** (no manté límits de missatge). Java: `ServerSocket` + `Socket` → [[TCP Stream-mode]].
- **Datagram (SOCK_DGRAM) — UDP:** flux de **missatges** sense garantia d'ordre ni arribada; manté límits (1 `send` = 1 `recv`). Més ràpid → [[UDP Datagram-mode]].
- **Raw (SOCK_RAW) — ICMP:** només root, per desenvolupar protocols.

Relacionat: [[TCP Stream-mode]] · [[UDP Datagram-mode]] · [[Endianness i Marshalling]] · [[Model Client-Servidor]]

#assignatura/SD #tipus/teoria
