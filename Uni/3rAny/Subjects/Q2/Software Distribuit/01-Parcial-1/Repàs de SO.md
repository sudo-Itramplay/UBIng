# Programes i Processos

- **Procés**: és un programa en execució, amb els valors actuals, les
seves variables d’estat, i tots els recursos usats pel S.O. per
gestionar la seva execució. 
	És una entitat dinàmica que només existeix quan el programa està executant-se.

- **Programa**: És el conjunt d’ordres per resoldre un problema o
funció especı́fica, basades en un llenguatge de programació.


- Un procés no és estàtic, sinó que transita per diferents estats segons el diagrama de vida:

![[Pasted image 20260219084504.png]]

Actualment els SO permeten la **concurrència**
	Il·lusió de l'execució simultània de múltiples processos en una sola CPU

>[!important] Thread
> Dins d'un mateix procés, podem trobar **fils d'execució (threads)**.
> 
> Aquests threads són unitats paral·leles que comparteixen els mateixos recursos del procés pare, permetent una gestió més eficient de les tasques internes


# Comunicació intra-processos(IPC) i protocols

El SO ofereix eines de IPC com els sockets, cues de missatges, semàfors i memòria compartida. 

Les aplicacions utilitzen APIs amb funcions bàsiques: `Connect`, `Disconnect` per a TCP i `Send`, `Recieve` per al intercanvi de dades.

- Per poder efectuar la comunicació, cal que els dos processos sincronitzin les seves operacions (Quan un envia l'altre ha de rebre)
Caldrà d'un protocol per garantir la correcta sincronització
#### Protocol
L’especificació d’un protocol ha d’incloure:

1.- la seqüència d’intercanvi de dades
	que pot ser descrita mitjançant un diagrama d’esdeveniments.

2.- l’especificació del format de les dades intercanviades en cada
pas.

### Representació de dades
El **Data Marshalling** és el procés de convertir estructures de dades en una seqüència binària apta per a la xarxa
- sovint usant una representació externa per evitar problemes d'incompatibilitat entre equips. 
- També cal definir com se separen els missatges (trames) mitjançant:
	- **Missatges de Longitud fixa**: Sempre la mateixa mida.
    
	- **Missatges amb Finalitzadors**: Un caràcter especial que marca el final.
    
	- **Missatges que Codifiquen la seva longitud**: El missatge indica al principi quants bytes té. Els protocols basats en text (com HTTP o SMTP) són populars per la seva facilitat d'anàlisi i lectura humana.


# Sincronització

La sincronització determina com es comporta un procés mentre espera que una operació de comunicació s'acabi.


- Les operacions **síncrones (bloquejants)** aturen l'execució del procés fins que la tasca es completa. Això simplifica la programació, però pot deixar el sistema inactiu durant massa temps.

- Les operacions **asíncrones (no bloquejants)** permeten que el procés continuï treballant i sigui notificat més tard, maximitzant l'ús de la CPU tot i que augmenta la complexitat de control per no ignorar missatges.

Es presenten diversos escenaris d'interacció:

1. **Enviament i Recepció síncrona**: Tots dos es bloquegen fins que la dada es transmet i es confirma.

2. **Enviament Asíncron i Recepció Síncrona**: L'emissor continua immediatament, però el receptor espera la dada.

3. **Enviament Síncron i Recepció Asíncrona**: L'emissor pot quedar bloquejat indefinidament si el receptor no demana la dada correctament. 
	- Una tècnica comuna és utilitzar **Threads** per simular asincronia: un fil nou fa una crida bloquejant mentre el fil principal del programa continua la seva execució sense aturar-se.

## Problemes d'accions bloquejants
L'ús incorrecte d'operacions bloquejants pot portar a fallades crítiques de disseny. 

El problema més greu és el **Deadlock (interbloqueig)**

>[!tip] Quan passa el deadlock?
>Quan dos processos es queden esperant dades l'un de l'altre indefinidament: 
>- el Procés 1 espera al Procés 2, 
>- el Procés 2 espera al Procés 1. 
>Aquesta situació atura completament l'aplicació i s'ha d'evitar mitjançant un disseny de protocol acurat.


D'altra banda, factors externs com talls a la xarxa poden fer que una operació `receive` es pengi per sempre si la dada mai arriba. 

- Com que és inacceptable que un procés es quedi bloquejat de forma indefinida en sistemes reals, s'utilitzen els **Timeouts**.