### Visió General de l'Arquitectura de Xarxes

La comunicació en xarxes d'ordinadors s'estructura mitjançant models per garantir la compatibilitat i la interoperabilitat. El model de referència fonamental és l'**[[OSI]]** (Open Systems Interconnection), un marc conceptual de set capes desenvolupat per estandarditzar les comunicacions. Tot i que serveix com a base teòrica, la seva implementació pràctica és el **[[model TCPIP]]**, que simplifica l'arquitectura en menys capes, agrupant funcionalitats.

El model OSI distingeix tres entorns:

1. **[[Entorn de sistemes reals]]**: On s'executen les aplicacions de l'usuari.
    
2. **[[Entorn OSI]]**: Afegeix protocols per a la comunicació entre aplicacions.
    
3. **[[Entorn de Xarxa]]**: Defineix els protocols específics d'una tecnologia de xarxa, com Ethernet.
    

### El Procés d'Encapsulació i les Unitats de Dades

La comunicació entre un sistema origen i un destí es basa en un procés d'**[[Encapsulació]]**, on cada [[Capa]] afegeix la seva pròpia informació de control a les dades que rep de la capa superior. Aquesta comunicació horitzontal entre capes homòlogues es coneix com a **[[Peer-to-Peer]]**.

Les estructures de dades principals en aquest procés són:

- **[[N-SDU]] (Unitat de Dades de Servei)**: És la "càrrega útil" que una capa N rep de la capa superior (N+1).
    
- **[[N-PCI]] (Informació de Control del Protocol)**: És la capçalera (i/o cua) que la capa N afegeix a la SDU per gestionar la comunicació.
    
- **[[N-PDU]] (Unitat de Dades del Protocol)**: És el resultat de combinar la N-PCI i la N-SDU. Aquesta és la unitat d'informació que s'intercanvia entre capes iguals de sistemes diferents. La N-PDU d'una capa es converteix en la (N-1)-SDU de la capa inferior, continuant el cicle d'encapsulació.
    

Per a la comunicació vertical dins d'un mateix sistema (entre capes adjacents), s'utilitza la **[[N-IDU]]** (Unitat de Dades de la Interfície), composta per la N-SDU i la **[[N-ICI]]** (Informació de Control de la Interfície), que conté paràmetres del servei sol·licitat.

### Un Viatge a través de les Capes OSI

1. **[[Capa Aplicació]], [[Capa Presentació]] i [[Capa de Sessió]]**: Aquestes tres capes superiors gestionen la interacció amb l'usuari, la representació de les dades (codificació, format) i el control del diàleg entre aplicacions, respectivament. En el model TCP/IP, totes tres es consoliden en una única **Capa d'Aplicació**.
    
2. **[[Capa Transport]]**: Ofereix una transferència de dades transparent amb control d'errors i de flux **extrem a extrem** (origen a destí). La seva unitat d'informació (PDU) és el **segment**.
    
3. **[[Capa Xarxa]]**: S'encarrega de l'adreçament lògic (p. ex., [[Classes IP]]) i de trobar la millor ruta (encaminament) a través de la xarxa. La seva PDU és el **paquet**. Els **routers** operen en aquesta capa.
    
4. **[[Capa Enllaç de Dades]]**: Gestiona el control d'errors i de flux **punt a punt** (entre nodes adjacents) i organitza els bits en trames. Inclou la subcapa **[[MAC]]** (Control d'Accés al Medi), que gestiona l'adreçament físic (adreça MAC). Els **switches** operen aquí.
    
5. **[[Capa Física]]**: Transmet el flux de bits no estructurats a través del medi físic, definint les especificacions elèctriques i mecàniques.
    

### Transmissió Física de Dades

Per transmetre informació, les dades han de ser adaptades al medi mitjançant la **[[Modulació]]** (modificar una ona portadora) i la **[[Codificació]]**.

El **[[Medi de Transmissió de la informació]]** és el canal físic pel qual viatja el senyal. Aquests es classifiquen en:

- **[[Medis Guiats]]**: Com el **[[Parell trenat]]** (**[[STP]]** o **[[UTP]]**), el cable **[[Coaxial]]** i la **[[Fibra Optica]]**.
    
- **[[Medis No guiats]]**: Com les **[[Ones de Ràdio]]**, **[[Microones terrestre]]** i **[[Microones Via Satèl·lit]]**.
    

Els **[[Tipus Enllaç/Classificació del Enllaços|enllaços]]** poden ser **[[Enllaç Punt a Punt]]** o **[[Enllaç Multipunt]]**, i segons el sentit de la transmissió, **[[Simplex]]** (unidireccional), **[[Half Duplex]]** (bidireccional no simultani) o **[[Duplex]]** (bidireccional simultani). L'abast geogràfic defineix els tipus de xarxes com **[[PAN]]**, **[[LAN]]** i **[[WAN]]**.

### Reptes i Límits de la Transmissió

La transmissió de dades s'enfronta a dos reptes principals:

1. **[[Atenuació]]**: La pèrdua de potència del senyal amb la distància, que pot requerir l'ús d'**[[Amplificadors]]**.
    
2. **[[Soroll]]**: Senyals indesitjats que es barregen amb el senyal original. Pot ser **[[Soroll Tèrmic]]** (la potència del qual es calcula amb la **[[Fòrmula de Johnson]]**), **[[Diafonia]]**, **[[Intermodulació]]** o **[[Soroll Impulsiu]]**.
    

La **[[Velocitat de Transmissió]]** (mesurada en **[[Bits per Segon|bps]]** o **[[Simbols per Segon|bauds]]**) està limitada per l'**[[Ample de Banda]]** (BW) del canal i la relació senyal-soroll (**[[SNR]]**). Aquests límits teòrics es descriuen mitjançant:

- La **[[Llei de Hartley]]**, que defineix la capacitat en un canal ideal sense soroll.
    
- El **[[Teorema de Shannon-Hartley]]**, que estableix la capacitat màxima teòrica en un canal amb soroll, demostrant que el soroll imposa un límit fonamental que Hartley ignora.