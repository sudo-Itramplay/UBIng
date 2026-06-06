## 1. Introducció als Demostradors i les seves Aplicacions

- Els demostradors són programes dissenyats per determinar si una fórmula és conseqüència lògica d'un conjunt de premisses determinat.

Aquests sistemes tenen una importància cabdal en la **programació declarativa**; per exemple, els intèrprets de llenguatges com **Prolog** funcionen intrínsecament com a demostradors de teoremes.

- En l'àmbit de l'enginyeria informàtica, s'utilitzen per a la **verificació de sistemes**, permetent demostrar que tant el programari com el maquinari (com els circuits d'una CPU) estan lliures d'errors de disseny.
   
- El mètode central que estudiarem per dissenyar aquests demostradors és el denominat **mètode de resolució**, una eina sintàctica molt més eficient que les taules de veritat tradicionals.


- La necessitat d'aquests mètodes sorgeix perquè el nombre d'interpretacions creix de manera exponencial, fent inviable comprovar tautologies mitjançant mètodes semàntics manuals en sistemes complexos.
	- Per tant, el demostrador actua com un mecanisme de validació de raonaments automatitzable en un ordinador.

>[!tip] Recorda
> demostrador ens permet saber si $\{\varphi_{1},...,\varphi_{n}\}\models\varphi$ és cert.

- Aquesta capacitat és el que ens permet passar d'una col·lecció de fets a una conclusió validada formalment.

- L'objectiu final és trobar un mètode algorítmic que un computador pugui executar sense ambigüitat.


---

## 2. La Forma Normal Conjuntiva (FNC)

- Per utilitzar el mètode de resolució, és imprescindible que les fórmules estiguin en **Forma Normal Conjuntiva (FNC)**.
	
	- Un **literal** es defineix com un àtom (variable proposicional) o la seva negació.
	
	- Una **clàusula** és una disjunció de literals (per exemple, $P \vee \neg Q$).
    
- Una fórmula es troba en FNC si és una conjunció de clàusules de la forma $\phi_{1}\wedge...\wedge\phi_{n}$.

### Tipus de Clausules

- La **clàusula buida** ($\square$) representa una contradicció, ja que no existeix cap interpretació que pugui satisfer una disjunció buida de literals.

- Per transformar qualsevol fórmula a FNC, seguim un algorisme de tres passos basat en equivalències lògiques:
    
    1. Eliminar implicacions ($\rightarrow$) i coimplicacions ($\leftrightarrow$) usant les definicions clàssiques ($\neg\varphi\vee\psi$).
        
    2. Introduir les negacions cap a l'interior dels parèntesis aplicant les **Lleis de De Morgan** i eliminant la doble negació.
        
    3. Aplicar la **propietat distributiva** de la disjunció respecte a la conjunció ($\vee$ sobre $\wedge$).

- Un exemple clar és la fórmula $(P\vee\neg Q)\rightarrow R$, que es transforma en $(\neg P\vee R)\wedge(Q\vee R)$ després d'aplicar aquests passos.
    
- L'aprenentatge d'aquesta transformació és vital, ja que és el pas previ obligatori per a qualsevol procés de resolució.
    
- Sense una FNC correcta, el demostrador no podrà aplicar la regla d'inferència de manera sistemàtica.
    

---

## 3. Conseqüència Lògica i la Regla de Resolució

- Diem que una fórmula $\varphi$ és **conseqüència lògica** d'un conjunt de premisses si la implicació formada per la conjunció de les premisses cap a la conclusió és una tautologia.
	- S'utilitza la notació $\{\varphi_{1},...,\varphi_{n}\}\models\varphi$ per expressar aquesta relació.


- El **mètode de resolució** és un procediment sintàctic que busca validar aquesta relació de manera eficient.
    
- La **regla de resolució** funciona amb dues clàusules (anomenades pares) que contenen un literal complementari (per exemple, $P$ i $\neg P$).
	
	- El resultat de l'operació és una nova clàusula anomenada **resolvent**, que consisteix en la disjunció de tots els literals de les clàusules pare excepte els literals complementaris que s'han suprimit.

>[!quote] Per Exemple
 Si tenim $\neg P\vee Q\vee S$ i $\neg Q\vee T$, el resolvent és $\neg P\vee S\vee T$ (suprimint $Q$ i $\neg Q$).
>   
>- Si tenim dos literals directament oposats com $P$ i $\neg P$, el seu resolvent és la clàusula buida ($\square$).
>    
>- Utilitzem el símbol $\vdash_{R}$ per indicar que una clàusula es pot derivar d'un conjunt d'entrada mitjançant la regla de resolució.
  
- Aquest mètode evita l'explosió exponencial de les interpretacions centrant-se només en les combinacions de literals que poden generar contradiccions.

- És la base de la demostració automàtica de teoremes moderna.


---

## 4. El Teorema de Resolució i l'Algorisme Pràctic


- El **Teorema de Resolució** estableix el lligam definitiu: $\{\varphi_{1},...,\varphi_{n}\}\models\varphi$ si i només si de la FNC de $(\varphi_{1}\wedge...\wedge\varphi_{n}\wedge\neg\varphi)$ es pot deduir la clàusula buida ($\square$).

- Això es basa en el mètode de **reducció a l'absurd**: si la negació de la conclusió juntament amb les premisses ens porta a una contradicció, aleshores el raonament original és vàlid.

- L'algorisme de resolució segueix aquests passos:
    
    1. Negar la conclusió ($\neg\varphi$).
        
    2. Calcular la FNC de les premisses i la conclusió negada.
        
    3. Aplicar la regla de resolució de manera iterativa fins a obtenir $\square$ ("èxit") o fins que no es puguin generar més resolvents ("fallo").
        
- En els exemples pràctics, veiem com un conjunt de clàusules aparentment inconnexes pot derivar en $\square$ mitjançant combinacions successives.

- Un cas d'aplicació real és el raonament sobre bancs i interessos: transformem el llenguatge natural a àtoms ($P, Q, R$), formalitzem les premisses, neguem la conclusió i resolem.

- Si s'arriba a la clàusula buida, podem afirmar amb total seguretat que el raonament és correcte.

- Aquest procés mecanitzable és el que permet que un ordinador "raoni" sobre problemes complexos de manera purament simbòlica.


