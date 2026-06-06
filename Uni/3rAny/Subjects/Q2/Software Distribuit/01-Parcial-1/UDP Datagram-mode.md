Comunicació **no orientada a la connexió** amb [[Sockets]] **Datagram (UDP)**. No hi ha `accept()`. Java: `DatagramSocket` (port) + `DatagramPacket` (dades + IP + port).

- **Servidor:** crea `DatagramSocket`, prepara un `DatagramPacket` buffer, crida `receive()` (bloquejant).
- **Client:** crea `DatagramSocket`, prepara el paquet amb IP/port destí, crida `send()`.

> [!warning] Comportament crític
> Diversos processos poden enviar al mateix socket → **ordre d'arribada impredictible**. Si el datagrama s'envia **abans** que el receptor faci `receive`, les dades **es perden**.

Relacionat: [[TCP Stream-mode]] · [[Sockets]] · [[Multicast]]

#assignatura/SD #tipus/teoria
