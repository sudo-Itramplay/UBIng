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


La majoria de protocols treballen en [[MAC]]

Entre Enllaç i física van per la IEEE

4, 5 i 6G NO ÉS IEEE, 3GPP


[[MAC]] (Control acces al medi? Rollo, el que controla)




TCP/IP vs Model OSI --> EN capes i tal (Mirar)

Cada capa de les OSI són independents, pq els punts de interconnexió de capes es mantenen, igualment si vaig amb wifi, ethernet o lo que sea

Nomes importa punt d'acces i primitives d'accès


Tipos enlllàços
Indirecte, emisor receptor i algú per enmig
Directe emisor i receptor


Una ona continua és com la veu, discreta és binari 

La connexió pot ser periòdica i aperiòdica



[[Ample de Banda]]
- rang de freq on esrà compresa major part d'energia d'un senyal
- El max i min de freq que pot agafar. 

Ample banda = $W=max-min$
	P.ex
	si min 300Hz
	si max 3'6KHz
	$W=3.3KHz$

Un senyal quadrat té rang infinit pq 1/0 = infinit i ns què pollades ha dit

TRX es refereix a transmissió

$log_2N_{iv}$ Si treus la n (nbits) passa a ser [[Simbols per Segon|baud rate]] 
$f_{Mostreig} \ge 2*f_{MAX}$
	i estàs en oversampling i no perds info
	SI la vull codifficar en simbols miltiplica $n_{bits}$
Velocitat = 2 * BW (Band width) = Kb/s

VMax és important

x/y[db] = [[SNR]]

Per l'exemple 1 -> $10log_{10} \cdot S/N = [[SNR]]$
	S potència senyal i N potència del [[Soroll]]
	
----->>>Propietats logaritmes $log_{10} 10^{1000} = 1000 \cdot log_{10} 10$
----->>>Propietats logaritmes $log_{10} 1+ 10 = log_{10} 10$

Ns què ha fet, peròno eren càlculs raros

Hem de decidir si jugar amb decibels o l'altre
M=num nivells si N_bits = 4 -> M=16

Ha de donar 8Mb/s

EX2
	Temperatura en Kelvins
	K és cte de bolsman (Kb $K_b$)
		és en decibles o J/K
		

Formules aleatories de la pissarra
$$
\frac{E_b}{n_0} = 115dB = \frac{P \cdot t_{bit}}{K_b \cdot T^º}
$$

$$
115=10 \cdot log_{10}
(\frac{P}{V_{TX} \cdot K \cdot T})$$

* Mira a la tablet exc


Exc tablet
	Necessito introduir bits o simbol
	

$log_{10} 10^{1000} = 1000 \cdot log_{10} 10 = 332,19 Mb/s$
$$
V_{TRX[bps]} = 2 \cdot BW \cdot n_{bits}  
$$
Has d'arrodonir a la baixa per no incomplir llei de Shanon (?)
	En aquest cas 16 -> 16,61 i l has de deixar en 16


Potencia total = 100mW
[[Energia per Bit|Eb]] = 1db mJ
T=20
$V_{TX}$


La majoria de fòrmules tenen algun logaritme, vigilar pq moltes vegades pots aplicar-hi propietats d'aquests

db - db És equivalent a dividir (elimines unitats) donada les propietats dels logaritmes (db es calcula amb logaritmes)

invers de temps de bit és la V de transmissió
	E=P * t
	E= $\frac{P}{V_{TX}}$
	Com les ddades es donen en unitats naturals i en decibels, primer has d'escollir amb què jugues
	$$
	db = 10 \cdot log_{10}X(X \space és \space Unitat \space Natural)
	$$
$E_b = db = 10 \cdot log_{10}E_b = 10 \cdot log_{10} \frac{P}{V_{TX}}$

100bps és la velocitat solució, crec


Ample banda mini, és com Vmax per aquest ample
	Apliquem Shannon

$100bp/s = BW \cdot log_2 (1+ \frac{S}{N})$
	S és potencia senyal
	N és noise (P del [[Soroll]])

$$
\frac{S}{N} = \frac{E_b}{K \cdot T}
$$


$1db mJ = 1,26mJ$
La unitat, ns pq, es manté

