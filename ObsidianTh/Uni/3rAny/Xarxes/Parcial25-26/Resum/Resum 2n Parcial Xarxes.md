Aquest Resum aborda des de:
- Capítol 3: La capa de Xarxa
- Capítol 4: Encapsulació. Nivell d'enllaç
- Capítol 5: Capa Transport (crec)


# Capítol 3. La capa de Xarxa
El seu rol és el d'establir comunicacions i de l'intercanvi de dades entre xarxes, amb l'objectiu principal de **Proporcionar [^1]routing i "[^2]forwarding Instructions"** Permetent que les dades siguin transmeses d'orígen a destí a través de nodes intermedis (routers).

**[[#Tipus de Xarxes]]**:
- [[#Xarxes Dedicades]]
- [[#Xarxes de Difusió]]
- [[#Xarxes de Commutació]]

**[[#Responsabilitats]]**:
- [[#Routing [ 1]]]
- [[#Adreçament Lògic]]
- Packet Forwarding
- Error Handling
- Error Control
- Fragmentació i Reassembling
- Control de la Congestió


## Tipus de Xarxes

### Xarxes Dedicades
On tots els equips es conecten entre si

- **Disseny**: 
	- Si tenim N nodes, calen:
		$\frac{N(N−1)}{2}$ enllaços i $N−1$ interfícies per node.

En una xarxa dedicada, cada node ha de tenir una línia directa amb tota la resta de nodes.

- **Interfícies ($N−1$):** Si tu ets un node en una sala amb N persones, per parlar amb tothom de forma privada (dedicada) necessites N−1 cables sortint del teu ordinador.

- **Enllaços ($\frac{N(N−1)}{2}$):** Si suméssim totes les interfícies de tots els nodes, tindríem N×(N−1). Però com que cada cable connecta **dos** nodes, dividim per dos per no comptar cada cable dues vegades.

> [!EXAMPLE] Exemple pràctic d'escalabilitat Fixa't com canvia la complexitat només afegint uns pocs nodes:
> 
> - **Xarxa de 5 nodes:**
>     
>     - Interfícies per node: 4
>         
>     - Enllaços totals: $\frac{5(4)}{2} = 10$ 
>         
> - **Xarxa de 10 nodes:**
>     
>     - Interfícies per node: 9
>         
>     - Enllaços totals: $\frac{10(9)}{2} = 45$
>         
> - **Xarxa de 100 nodes:**
>     
>     - Interfícies per node: 99
>         
>     - Enllaços totals:  $\frac{100(99)}{2} = 4950$
>

![[Pasted image 20260103102324.png]]

>[!CHECK] Avantatges: Simplicitat Inicial i Rendiment
>- **Planificació trivial:** No calen algorismes de routing complexos ni commutadors (switches) intermedis. Si vols enviar dades al Node B, saps exactament per quin cable han de sortir.    
>- **Retard (Latència) mínim:** La comunicació és directa, sense salts intermedis.
>    
>- **Ample de banda dedicat:** No comparteixes el canal amb ningú; no hi ha col·lisions.

>[!DANGER] Desavantatges: El mur de la realitat (Cost i Espai)
>- **Límit físic:** Arriba un punt on no pots posar 100 targetes de xarxa en un sol servidor.
>    
>- **Manteniment de malson:** Si un cable falla en una xarxa de 1.000 nodes, identificar quin dels 499.500 cables és el culpable és pràcticament impossible sense eines caríssimes.
>    
>- **Cost quadràtic:** El cost no creix de forma lineal amb els usuaris, sinó que creix proporcionalment al quadrat del nombre de nodes ($O(N^2)$).

### Xarxes de Difusió

Tenen un medi de connexió únic compartit per tots els equips de la xarxa.

- **Disseny**:
    
    - Independentment del nombre de nodes (N), la topologia física es simplifica dràsticament:
        
        - **1** únic medi compartit (bus, aire en Wi-Fi, o hub).
            
        - **1** única interfície per node.
            

En una xarxa de difusió, quan un node transmet, el senyal es propaga per tot el medi i **tots** els altres nodes el reben, encara que no siguin el destinatari.

- **Interfícies (1):** Cada node només necessita una targeta de xarxa per connectar-se al medi comú.
    
- **Enllaços (1):** El medi és compartit. No calen cables individuals entre cada parella de nodes.
    

> [!EXAMPLE] Exemple pràctic d'eficiència física Observa com la infraestructura es manté gairebé constant encara que la xarxa creixi:
> 
> - **Xarxa de 5 nodes:**
>     
>     - Interfícies totals: 5 (1 per node)
>         
>     - Medi compartit: 1
>         
>         
> - **Xarxa de 100 nodes:**
>     
>     - Interfícies totals: 100
>         
>     - Medi compartit: 1
>         


![[2026-01-03_10-41.png]]


> [!CHECK] Avantatges: Economia i Flexibilitat
> 
> - **Baix cost:** Estalvi massiu en cablejat i interfícies respecte a la malla completa.
>     
> - **Escalabilitat física simple:** Afegir un node nou és tan fàcil com "enganxar-se" al medi existent.
>     
> - **Difusió natural:** Enviar un missatge a tothom (broadcast) no requereix replicar el paquet; es fa amb una sola transmissió.
>     

> [!Fail] Desavantatges: Gestió del Medi i Seguretat
> 
> - **Col·lisions:** Si dos nodes parlen a la vegada, els senyals xoquen i es corrompen. Calen protocols d'accés al medi (**MAC**) com CSMA/CD o CSMA/CA.
> 
>     
> - **Seguretat/Privacitat:** Com que tothom rep el que s'envia, és més fàcil "escoltar" el trànsit d'altri (sniffing).
> 
> 
> - **Ample de banda compartit:** Els N nodes s'han de repartir la capacitat total del medi. Si molts transmeten a la vegada, el rendiment cau en picat.
>     



>[!info] Canvi de Cost
>En les dedicades el problema era el **Cost de material** (cables/ports), 
>
>En les de difusió el repte és l'**eficiència del protocol**.
>
>Hem passat d'un problema de _hardware_ a un problema de _software/logística_ (gestió de torns i adreçament). 
>
>Per això necessitem les adreces MAC: per saber quin paquet hem de processar i quin hem de descartar.


### Xarxes de Commutació
A diferència de les xarxes dedicades, aquestes fan servir equips intermedis per commutar els paquets i dirigir-los cap al seu destí.

El procés de comunicació en aquestes xarxes implica normalment **3 fases**:

1. **Establiment** de la connexió.
    
2. **Transferència** de la informació.
    
3. **Alliberament** de la connexió.
    

---

#### 1. Commutació de Circuits

És el model clàssic de la telefonia analògica.

- **Funcionament**: S'estableix una ruta fixa entre l'origen i el destí abans de començar la transmissió.
    
- **Reserva de Recursos**: Un cop acceptada la connexió, el canal queda **reservat i és exclusiu**.
    
- **Limitació**: Cap altre dispositiu pot utilitzar aquests recursos fins que la connexió s'allibera, el que pot ser ineficient si no s'envien dades constantment.
    

#### 2. Commutació de Missatges

Una aproximació més teòrica que no s'acostuma a implementar en xarxes de dades modernes.

- **Funcionament**: El node decideix quin és el millor "següent salt" i envia **tota** la informació de cop.
    
- **Sense Fragmentació**: La característica principal és que no es fragmenta el missatge.
    
- **Ineficiència**: És inviable per a missatges molt grans (gigabytes), ja que bloqueja els nodes intermedis i requereix molta memòria.
    

#### 3. Commutació de Paquets

És l'evolució lògica que divideix el missatge en unitats més petites anomenades **paquets**.

La idea central és **dividir** el missatge en fragments per permetre que múltiples usuaris comparteixin els mateixos recursos de transmissió **simultàniament**.

> [!INFO] Modes de Funcionament de Paquets
> Existeixen dues maneres de gestionar aquests fragments:
> - Mode Datagrama
> - Mode Circuit Virtual

##### Mode Datagrama

- En aquest mode, cada paquet es tracta com una entitat independent. 
- L'encaminament es decideix salt a salt en temps real.

>[!example] **Funcionament**: 
>Cada fragment porta una capçalera amb l'adreça completa d'origen i destí. 
>
>Els nodes trien el millor camí disponible en aquell instant de temps per a cada paquet individual.

>[!check] **Aventatges**:
>  
>- **Robustesa**: Si un node falla, els paquets següents poden trobar rutes alternatives automàticament.
>    
>- **Sense retard inicial**: No cal una fase d'establiment de connexió; l'enviament és immediat.
>

>[!fail] **Desaventatges**:
    >
>- **Desordre**: Els paquets poden arribar al destí en un ordre diferent al d'emissió.
>	
>- **Sense QoS**: No hi ha garanties de qualitat de servei (retard, amplada de banda).
   
##### Mode Circuits Virtuals

És un híbrid que intenta combinar l'eficiència dels paquets amb l'ordre dels circuits.

> [!example] Funcionament
> S'escull un camí fix a priori abans d'enviar les dades. 
> 
>Tot i que el camí està definit, el canal no es reserva en exclusiva i pot ser utilitzat per altres commutacions.


>[!check] **Aventatges**:
>  
>- **Ordre garantit**: Els paquets arriben sempre en la seqüència correcta.
>    
>- **Qualitat de Servei (QoS)**: Permet oferir garanties sobre el rendiment de la connexió.
>

>[!fail] **Desaventatges**:
>- **Retard d'establiment**: Requereix temps per configurar la ruta abans de transmetre.
>	
>- **Vulnerabilitat**: Si un node del camí prefixat falla, tota la connexió cau i s'ha de tornar a establir.
   


> [!NOTE] Es poden fer servir alhora?
> 
> Sí, és perfectament possible i, de fet, és molt comú. 
> 
> En el món real de l'enginyeria de xarxes, s'utilitza la jerarquia de protocols. 
> 
> Per exemple:
> 
> Podem tenir una xarxa que:
> -  A nivell de capa de xarxa (IP) funcioni per datagrames (per ser flexible i global)
> - Però que estigui transportant dades sobre una infraestructura de nivell inferior (com MPLS o ATM) que funcioni mitjançant circuits virtuals 
>  
> Per garantir la velocitat i la QoS en el tronc central (backbone) de la xarxa.





## Responsabilitats


### Routing [^1]
És la feina de Determinar el camí més optim per a que les dades hi viatgin

Ha de tenir en compte:
- Topologia de xarxa[^3]
- Congestió[^4]
- Qualitat de servei (QoS)[^5]

#### Conceptes Clau: Protocols d'Encaminament vs. Encaminables

Segons els exàmens de cursos anteriors, és fonamental distingir entre:

- **Protocols d'encaminament (Routing Protocols)**: Són els encarregats de trobar la millor ruta minimitzant la mètrica o cost. S'ocupen de generar i mantenir les **taules d'encaminament**, que indiquen el "següent salt" per arribar al destí.
    
- **Protocols encaminables (Routed Protocols)**: Són els protocols que transporten les dades i proporcionen l'**adreça lògica** (com IP) que els protocols d'encaminament utilitzen per trobar la ruta.
    

#### La Mètrica

La mètrica és el criteri que utilitza el protocol per escollir entre diferents camins possibles.

- **Exemple comú**: El nombre mínim de salts (hops) entre nodes.
    

#### Procés de construcció de la Taula de Routing

Perquè un node sàpiga com arribar a tot arreu, segueix aquests passos:

1. **Enviament de paquets "Hello"**: Tots els nodes s'identifiquen davant els seus veïns per conèixer la seva existència.
    
2. **Intercanvi de taules**: Els veïns intercanvien les seves taules de routing per aprendre rutes cap a nodes que no veuen directament.
    
3. **Convergència**: El procés es repeteix fins que tots els nodes de la xarxa saben com arribar a qualsevol altre punt.


![[2026-01-03_11-19.png]]

---

> [!TIP] Diferència Teòrica
> 
> Recorda que el Routing és un procés global (triar el camí), mentre que el Forwarding és un procés local de cada router (passar el paquet de l'entrada a la sortida segons la taula).


>[!note] Diferència amb el forwarding:
>_forwarding_ (reenviament), és l'acció física de moure el paquet d'una interfície d'entrada a una de sortida.



### Adreçament Lògic
És la feina d'assignar adreces lògiques (IP) Als dispositius connectats. 

- Això permet que aquests siguin identificats i localitzables


Un datagrama IP es divideix fonamentalment en dues parts: 
- la **capçalera** (que conté la informació de control) 
- la **càrrega útil** (_payload_, amb les dades de les capes superiors).

![[2026-01-03_11-38.png]]

La capçalera està estructurada en blocs de 32 bits per optimitzar el processament en els encaminadors2222.

1. **Versió (4 bits):** 
	Indica quina versió del protocol s'està utilitzant; en aquest cas, el valor és 4 per a IPv43333.
    
2. **IHL (Internet Header Length) (4 bits):** 
	Indica la longitud de la capçalera en blocs de 32 bits. El valor mínim és 5 (20 bytes) si no hi ha opcions.
    
3. **Tipus de Servei (ToS) (8 bits):** 
	Permet indicar preferències de qualitat de servei, com ara la prioritat, el retard o la fiabilitat que necessita el paquet5555.
    
4. **Longitud Total (16 bits):** 
	Especifica la mida total del datagrama (capçalera + dades) en bytes6666.
    
5. **Identificació (16 bits):** 
	Un número de seqüència que, juntament amb l'adreça d'origen, identifica unívocament el datagrama. És clau per al procés de reensamblatge si el paquet es fragmenta.
    
6. **Flags (3 bits):** S'utilitzen principalment dos:
    
    - **More (M):** Si està a 1, indica que el datagrama és un fragment i que no és l'últim.
        
    - **Don't Fragment (DF):** Si està a 1, indica que el datagrama no es pot fragmentar; si un router no el pot enviar sencer, l'haurà de descartar.
    
7. **Desplaçament del fragment (13 bits):** Indica la posició de la càrrega útil d'aquest fragment respecte al datagrama original, mesurat en unitats de 64 bits.
    
8. **Temps de Vida (TTL) (8 bits):** Un comptador que evita que els paquets circulin infinitament en cas de bucles d'encaminament. Cada router que travessa el paquet en resta una unitat; si arriba a 0, el paquet es descarta.
    
9. **Protocol (8 bits):** Indica quin protocol de la capa de transport (com TCP o UDP) ha de rebre les dades en el destí.
    
10. **Suma de comprovació (Checksum) (16 bits):** S'utilitza per detectar errors només en la capçalera. Atès que el TTL canvia a cada salt, aquest camp s'ha de recalcular en cada router.
    
11. **Adreces d'Origen i Destí (32 bits cadascuna):** Les adreces lògiques IP del remitent i del destinatari final.



>[!note] Conceptes
>- **Fragmentació:** Es realitza quan un router ha de passar un datagrama per una xarxa amb una MTU (Mida de Transmissió Màxima) inferior a la mida del paquet. El reensamblatge es fa sempre en el destí final.
> - **Regla d'Or:** Les adreces IP (Capa 3) es mantenen constants d'origen a destí (excepte si hi ha NAT), mentre que les adreces MAC (Capa 2) canvien a cada salt.
> - **Diferència amb IPv6:** En IPv6 es simplifica la capçalera, desapareix el _checksum_ (per agilitzar el processament) i no es permet la fragmentació en els encaminadors; aquesta és responsabilitat exclusiva de l'origen.









# Problemes

### Fragmentació IP

Enunciat: Tenim un datagrama IP de longitud total 404 Bytes (inclou capçalera). Hem de fragmentar-lo en 3 datagrames de mides similars.

Objectiu: Calcular la mida de dades, capçalera, offset i flags per a cada fragment.

**1. Anàlisi de les dades inicials:**

- **Longitud Total ($L_T$):** 404 Bytes.
    
- **Capçalera IP ($H$):** 20 Bytes (mida estàndard mínima).
    
- **Dades Útils (Payload, $D$):** $L_T - H = 404 - 20 = 384$ Bytes.
    

2. Càlcul de la divisió:

Ens demanen dividir en 3 fragments similars.

$$\text{Dades per fragment} = \frac{384 \text{ Bytes}}{3} = 128 \text{ Bytes}$$

Comprovem la restricció d'alineació: Per a tots els fragments (excepte l'últim), la mida de les dades ha de ser múltiple de 8 Bytes (64 bits).

$$\frac{128}{8} = 16 \rightarrow \text{Exacte. És vàlid.}$$

**3. Desenvolupament mecànic dels fragments:**

- **Fragment 1:**
    
    - **Dades:** 128 Bytes.
        
    - **Offset:** 0 (Inici).
        
    - **Flag MF (More Fragments):** 1 (Hi ha més fragments).
        
    - **Longitud Total:** $128 (\text{Dades}) + 20 (\text{Capçalera}) = 148$ Bytes.
        
- **Fragment 2:**
    
    - **Dades:** 128 Bytes.
        
    - Offset: L'offset indica el nombre de blocs de 8 bytes enviats anteriorment.
        
        $$\text{Offset} = \frac{\text{Dades acumulades anteriors}}{8} = \frac{128}{8} = 16$$
        
    - **Flag MF:** 1.
        
    - **Longitud Total:** $128 + 20 = 148$ Bytes.
        
- **Fragment 3 (Últim):**
    
    - **Dades:** 128 Bytes.
        
    - Offset:
        
        $$\text{Offset} = \frac{128 + 128}{8} = \frac{256}{8} = 32$$
        
    - **Flag MF:** 0 (És l'últim).
        
    - **Longitud Total:** $128 + 20 = 148$ Bytes.
        

**Resultat final:** 3 fragments idèntics de 148 Bytes (128 de dades) amb offsets 0, 16 i 32.

---

### Subnetting VLSM

Enunciat: Xarxa base 192.168.3.0/24. Crear subxarxes per a: 100, 60, 40, 5 i 5 equips.

Mètode: VLSM (Variable Length Subnet Mask). Ordenem sempre de major a menor requeriment.

**1. Subxarxa A (100 equips):**

- **Bits necessaris ($h$):** $2^h - 2 \geq 100 \rightarrow 2^7 = 128$. Necessitem **7 bits** de host.
    
- **Màscara:** $32 - 7 = /25$ ($255.255.255.128$).
    
- **Adreça Xarxa:** 192.168.3.0/25
    
- **Rang:** 192.168.3.1 a 192.168.3.126
    
- **Broadcast:** 192.168.3.127
    
- **Següent IP lliure:** 192.168.3.128
    

**2. Subxarxa B (60 equips):**

- **Bits necessaris:** $2^h - 2 \geq 60 \rightarrow 2^6 = 64$. Necessitem **6 bits** de host.
    
- **Màscara:** $32 - 6 = /26$ ($255.255.255.192$).
    
- **Adreça Xarxa:** 192.168.3.128/26
    
- **Rang:** 192.168.3.129 a 192.168.3.190
    
- **Broadcast:** 192.168.3.191
    
- **Següent IP lliure:** 192.168.3.192
    

**3. Subxarxa C (40 equips):**

- **Bits necessaris:** $2^h - 2 \geq 40 \rightarrow 2^6 = 64$. Necessitem **6 bits** de host (amb 5 bits tindríem 32, insuficient).
    
- **Màscara:** $32 - 6 = /26$ ($255.255.255.192$).
    
- **Adreça Xarxa:** 192.168.3.192/26
    
- **Rang:** 192.168.3.193 a 192.168.3.254
    
- **Broadcast:** 192.168.3.255
    
- **Següent IP lliure:** Cap. Hem arribat al límit de la xarxa /24 (255).
    

**4. Subxarxes D i E (5 equips):**

- **Problema detectat:** Les subxarxes A, B i C han consumit tot l'espai d'adreçament ($128 + 64 + 64 = 256$ IPs).
    
- **Conclusió mecànica:** No és possible assignar les subxarxes per als grups de 5 equips amb una única xarxa classe C (192.168.3.0/24) sota aquests requeriments.
    

---

### Eficiència en Protocol ARQ

Enunciat: Enllaç punt a punt, RQ-Inactiva (Stop-and-Wait).

- Mida trama ($L$): 1024 Bytes.
    
- Velocitat ($R$): 250 kbps.
    
- Distància ($d$): 10 km.
    
- Velocitat prop ($v$): $3 \cdot 10^8$ m/s (aprox. llum).
    
- Temps procés ($T_{proc}$): 0.1 ms.
    
- Mida ACK ($L_{ack}$): 100 bits.
    

1. Càlcul de Temps de Transmissió ($T_{tx}$):

$$T_{tx} = \frac{\text{Mida (bits)}}{\text{Velocitat (bps)}} = \frac{1024 \cdot 8}{250 \cdot 10^3} = \frac{8192}{250000} = 0,032768 \text{ s} \approx \mathbf{32,77 \text{ ms}}$$

2. Càlcul de Temps de Propagació ($T_{prop}$):

$$T_{prop} = \frac{\text{Distància}}{\text{Velocitat prop.}} = \frac{10 \cdot 10^3}{3 \cdot 10^8} = 3,33 \cdot 10^{-5} \text{ s} \approx \mathbf{0,033 \text{ ms}}$$

3. Càlcul de Temps de Transmissió ACK ($T_{tx\_ack}$):

$$T_{tx\_ack} = \frac{100 \text{ bits}}{250 \cdot 10^3 \text{ bps}} = 0,0004 \text{ s} = \mathbf{0,4 \text{ ms}}$$

4. Càlcul del Cicle Total (RTT + procés):

El temps total per enviar un paquet i rebre la confirmació és:

$$T_{total} = T_{tx} + 2 \cdot T_{prop} + T_{proc} + T_{tx\_ack}$$

$$T_{total} = 32,77 + 2(0,033) + 0,1 + 0,4$$

$$T_{total} = 32,77 + 0,066 + 0,1 + 0,4 = \mathbf{33,336 \text{ ms}}$$

5. Eficiència ($\eta$):

$$\eta = \frac{\text{Temps útil}}{\text{Temps total}} = \frac{T_{tx}}{T_{total}}$$

$$\eta = \frac{32,77}{33,336} = 0,983$$

Resultat: L'eficiència és del 98,3%.

Nota: Com que $T_{prop}$ i $T_{ack}$ són molt petits comparats amb $T_{tx}$, l'eficiència és molt alta.



[^1]: Encaminament

[^2]: Reenviament

[^3]: La disposició física i lògica dels nodes i enllaços.

[^4]: L'estat actual de saturació dels canals.

[^5]: Els requeriments específics de la transmissió (retard, amplada de banda, etc.).
