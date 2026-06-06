Xarxa - permet lainterconnexió entre diferents xarcxes


LAN
La lan permet intercanviar (puc saber la ip de destí però no la mac, no podre empaquetar en trames coses) 


Els routers incorporen un protocol de control per poder saber què passa sense estar-hi

Dona protocol MAC plana (és important)

és dificil fer una jerarquia
	 si tinc 3 switchos, a cada aula fent coses

La capa IP  és que jerarquitza la xarxa (32 o 128 bits)


Encaminament (routing)

Per N nodes tenim $N* \frac{(N-1)}{2}$ enllaços
això és dificil de gestiona rperò molt rapid i segurt


Xarxes de Difusió
Ethernet



Xarxes de Commutació
Tenim diferents nodes (transit i perifèric)
perifèric és qui dona servei
Eñ transit és el de les companyies

Els nodes no nomes reenvien, també fan controls de flux i altres

Té tipus aquesta xarxa
circuits, missatges i paquets

La de missatges és teorica i no s'ha aplicat mai

A la fase 2 de circuits, no hi ha retard un cop establert el camí, ja que cada node nomes té la instrucció de reenviar

Exemple d'aplicaicó és trucada


missatge crec, no ho se

Si es satura alguna xarxa, com que hi ha diferents nodes, podem redirigir entrades



EL VIRTUAL
Evita diferents encaminaments, per a que tot arribi en ordre


HI ha una merda que é sun graf de retransmiccio de dades d'encaminament en que es fa una taoula entre tots els routers i es van apuntant els routers als que pots anar, i des de quin (M ha arribat un missatge de 7 desde 3.. Llavors si vull enviar a 7 he d'enviar a 3)



hi ha un router master, en el que si no saps anar a algun lloc, ell envia


