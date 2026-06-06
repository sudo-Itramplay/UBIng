
Ajedrez un rei blanc i un negre, on el negre no es pot moure

## Objectiu
Matar Rey


## Arxius

- chess classe que representa el joc
- board classe que representa el tablero
- Piece classe que representa a una peça
	Aqui no modificar
- aichess és una capsula per a les 3 classes anteriors per fer la P
	Aqui s'ha d'implementar l'algoritme



#### State
del tablero
és una llista de 3 elements
[row, column, piece_type]
rey blanc = 6
rey negre = 12
Torre blanca = 2
Torre negre = 8

- RB [7,5]
- RN[0,5]


### aichess

#### Current State
llista de posions/peces blanques

per exemple, seria 
	current= ([7,5,6] , [7,0,2]) (rey blanc inici) (suposada )
####  List Next States
llista potencials estats del current_state


#### Path to target
Per guardar la seqüència d'estats que ha de passar del inical fins el final

#### changeState

Funcio per simular moviments, el seguent moviment

#### move Pieces
mou totes les peces del start state fins el "to"

#### reconstructState

#### h()
Hem de revisar el mètode Heurístic, pq suposa una condició que no va bé

#### AstarSearch
El mètode Important
Se'ns ha donat el DFS i BFS d'exemple

El cost del Astar és O(g(h) + h())

g() és el cost que portem
h() és el cost que estimem







#### isCheckMate
Per ara hardcoded, més endavant ns'ha de canviar

et dona estat de si s'ha acabt o no










### board

isSameState
	Si dos states del taulell són el mateix

getListNextStateW (o B tmb)

print_board
	Per debug
### chess

bosrd
	taulell real on farem els moviments pels que estem segurs
boardsim
	Per fer suposicions de moviments

move
	Function to move a piece from start state to to position
moveSim
	El mateix però pel simulat

### piece



### PDF

Mirar de començar posició inicial demanada

Fer llista dels visitats fins el final -> Tot el recorregut


3p A*

3p llista retornada amb el path

-->Mirar heuristica i provar amb altres estats inicials si funciona


#### Apunts
##### 1
t is fundamental that you implement the state as a list of elements containing the positions
and types of pieces you move. 

##### 2 Prova final
 For example, the initial position could be: [[7,0,2], [7,4,6]].
 
##### Condicions inicials
starting board configuration (pre-programmed): 
it contains a black king, on position [0,5] and two white pieces, the movement
of which you will have to program: 
a king on position [7,5] 
a rook on position [7,0]. 

Keep
in mind that in this exercise, the black piece do not move, and that **only you can move the
white pieces**. Your goal is to find the configuration state such that it is a check-mate to the
black king.
## P2
Ens donaran codi que simula moviment peces
No tindrem totes les peces
	2 torres i 2 reis
Juguen entre ells

Implementar diferents algoritmes per a cada color per veure efectes dels algoritmes

