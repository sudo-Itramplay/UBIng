Paradigma d'enviament de dades a **múltiples receptors simultàniament** (a diferència de l'Unicast 1-a-1), optimitzant el trànsit de xarxa.

- Només via **UDP** ([[UDP Datagram-mode]]): no fiable, sense connexió ni garantia d'ordre.
- **IP Multicast:** enviar un paquet IP a un grup de màquines, construït sobre IP.
- **Grup Multicast:** identificat per una adreça de **Classe D** (224.0.0.0 – 239.255.255.255). Quan una màquina s'afegeix al grup, accepta tots els missatges a aquella adreça. Es pot enviar a un grup **sense ser-ne membre**. Per a proves locals: 224.0.0.1.

Relacionat: [[UDP Datagram-mode]] · [[Tipus de Servidors]] · [[Model Client-Servidor]]

#assignatura/SD #tipus/teoria
