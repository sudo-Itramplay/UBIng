Concepte similar a l'**herència** de la programació orientada a objectes. Permet jerarquies on una entitat superior (**superclasse**) comparteix atributs comuns amb entitats inferiors (**subclasses**).

**Exemple (FC Barcelona):**
- L'entitat **Persona** és la base amb atributs generals (DNI, nom, cognoms, data de naixement).
- Se'n deriven **Jugador**, **Treballador** i **Entrenador**, que hereten els atributs de Persona i en tenen de propis ("anys d'experiència", "demarcació"…).

![[Pasted image 20260217170237.png]]

> En convertir a taules: una taula per al pare i una per cada filla, compartint l'identificador del pare com a [[Clau Primària]] → [[Transformació ER a Taules]].

Relacionat: [[Entitat]] · [[Model Entitat-Relació]] · [[Transformació ER a Taules]]

#assignatura/BD #tipus/teoria
