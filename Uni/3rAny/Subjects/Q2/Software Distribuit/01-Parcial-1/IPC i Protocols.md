El SO ofereix eines de **comunicació entre processos (IPC)**: [[Sockets]], cues de missatges, semàfors, memòria compartida. Les APIs usen `Connect`, `Disconnect`, `Send`, `Receive`.

**Protocol:** cal per sincronitzar emissor i receptor. L'especificació inclou:
1. la **seqüència** d'intercanvi (diagrama d'esdeveniments).
2. el **format** de les dades a cada pas.

**Representació de dades:**
- **Data Marshalling:** convertir estructures de dades en una seqüència binària apta per a la xarxa (representació externa per evitar incompatibilitats → [[Endianness i Marshalling]]).
- **Framing (separar missatges):** longitud fixa · finalitzadors · longitud codificada al principi. Els protocols de text (HTTP, SMTP) són populars per la seva llegibilitat.

Relacionat: [[Procés i Thread]] · [[Sincronització]] · [[Endianness i Marshalling]] · [[Sockets]]

#assignatura/SD #tipus/teoria
