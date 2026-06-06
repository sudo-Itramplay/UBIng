Exemple canònic de [[P2P]] optimitzat per a la **distribució massiva de fitxers grans** (eficiència de descàrrega).

- **Quid Pro Quo:** "comparteixo si tu comparteixes" → evita els _free riders_.
- **Protocol:** fitxer `.torrent` (hash, nom, URL del **tracker**) → petició al **tracker** → llista de peers: **Seeds** (fitxer complet) i **Leechers** (incomplets).
- **Gestió de peces (256 KB):**
	- Descàrrega en **paral·lel** de múltiples peers.
	- **Rarest First:** prioritzar les peces menys freqüents.
	- **Choking:** seleccionar periòdicament els 4 peers amb millor taxa.
	- **Optimistic Upload:** cada 30 s enviar a un peer aleatori per descobrir nous nodes.

Relacionat: [[DHT i Overlay Network]] · [[P2P]] · [[Blockchain]]

#assignatura/SD #tipus/teoria
