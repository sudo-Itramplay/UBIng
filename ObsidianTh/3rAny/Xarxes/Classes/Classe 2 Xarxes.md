La torre OSI
7 capesPDU enviem a capa homonima 
	App-PDU
	Pres-PDU



Gran Capa 
NIC
	Network Interface

V de dades en medi inalàmbric
	V propagació $3 *10⁸$

EN cable V ona electro magnètica

Protocols: 4G, 5G, ...

PAN < LAN < WAN < DWDM (Distància connexió)


La majoria de protocols treballen en MAC

Entre Enllaç i física van per la IEEE

4, 5 i 6G NO ÉS IEEE, 3GPP


MAC (Control acces al medi? Rollo, el que controla)




TCP/IP vs Model OSI --> EN capes i tal (Mirar)

Cada capa de les OSI són independents, pq els punts de interconnexió de capes es mantenen, igualment si vaig amb wifi, ethernet o lo que sea

Nomes importa punt d'acces i primitives d'accès


Tipos enlllàços
Indirecte, emisor receptor i algú per enmig
Directe emisor i receptor


Una ona continua és com la veu, discreta és binari 

La connexió pot ser periòdica i aperiòdica



Ample de banda
- rang de freq on esrà compresa major part d'energia d'un senyal
- El max i min de freq que pot agafar. 

Ample banda = $W=max-min$
	P.ex
	si min 300Hz
	si max 3'6KHz
	$W=3.3KHz$

Un senyal quadrat té rang infinit pq 1/0 = infinit i ns què pollades ha dit

TRX es refereix a transmissió

$log_2N_{iv}$ Si treus la n (nbits) passa a ser baud rate 
$f_{Mostreig} \ge 2*f_{MAX}$
	i estàs en oversampling i no perds info
	SI la vull codifficar en simbols miltiplica $n_{bits}$
Velocitat = 2 * BW (Band width) = Kb/s

VMax és important


Per l'exemple 1 -> $10log_{10} \cdot S/N = SNR$

Ns què ha fet, peròno eren càlculs raros

Hem de decidir si jugar amb decibels o l'altre
M=num nivells si N_bits = 4 -> M=16

Ha de donar 8Mb/s

EX2
	Temperatura en Kelvins
	K és cte de bolsman
		és en decibles o J/K
		

Formules aleatories de la pissarra
$$
\frac{E_b}{n_0} = 115dB = \frac{P \cdot t_{bit}}{K_b \cdot T^º}
$$

$$
115=10 \cdot log_{10}
(\frac{P}{V_{TX} \cdot K \cdot T})$$

* Mira a la tablet exc
* 




