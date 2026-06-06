Problemes crítics de la programació multithread ([[Threads]]):

- **Seguretat:** l'accés simultani a memòria pot corrompre dades → cal **exclusió mútua** ([[Sincronització en Java]]).
- **Esperes patològiques:**
	- **Deadlock:** bloqueig mutu (dos fils s'esperen l'un a l'altre).
	- **Starvation:** un procés no avança mai (recursos injustos).
	- **Livelock:** processos actius però sense progressar.
- **Race Condition (condició de carrera):** el resultat depèn de l'ordre d'execució. Ex: dos fils llegeixen `count=0`, l'incrementen i el guarden → resultat 1 en lloc de 2. Cal sincronitzar `count++`.
- **Eficiència:** maximitzar el còmput simultani real.

> **Prevenció de deadlock:** ordenació de recursos (tots demanen els locks en el mateix ordre → impossible espera circular).

Relacionat: [[Sincronització en Java]] · [[Coordinació de Threads]] · [[Sincronització]]

#assignatura/SD #tipus/teoria
