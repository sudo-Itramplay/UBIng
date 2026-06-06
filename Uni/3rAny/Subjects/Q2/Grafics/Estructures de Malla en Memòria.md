Triar l'estructura de dades per a una [[Malles Poligonals|malla]] depèn de l'operació a optimitzar (intersecció, memòria, navegació).

| Estructura | Millor per a... | Memòria |
| --- | --- | --- |
| **Explícita (STL)** | Impressió 3D simple; llista de vèrtexs per triangle, sense connectivitat | Molt redundant |
| **Vèrtexs Indexats (OBJ/OFF)** | **[[Ray Tracing]]** (interseccions): evita redundància, accés ràpid | Eficient |
| **Adjacència de Cares** | Trobar veïns / topologia (saltar d'un triangle a un altre) | Equilibrada |
| **Winged-Edge** | **Edició** geomètrica; element central = l'**aresta** | Cara (molts punters) |

Relacionat: [[Malles Poligonals]] · [[Malla de Triangles]] · [[Ray Tracing]]

#assignatura/Grafics #tipus/teoria
