# Graph Report - .  (2026-07-06)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 13 nodes · 9 edges · 8 communities (3 shown, 5 thin omitted)
- Extraction: 89% EXTRACTED · 11% INFERRED · 0% AMBIGUOUS · INFERRED: 1 edges (avg confidence: 0.8)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `72cc49ee`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]

## God Nodes (most connected - your core abstractions)
1. `Luces con Niebla` - 4 edges
2. `Luces con Lluvia` - 3 edges
3. `Luz Antiniebla Trasera` - 3 edges
4. `Luz de Posición` - 2 edges
5. `Luz de Carretera (Largas)` - 2 edges
6. `Luz de Cruce (Cortas)` - 2 edges
7. `Luz Antiniebla Delantera` - 0 edges
8. `Luz de Estacionamiento` - 0 edges
9. `Luz de Freno` - 0 edges
10. `Luz de Marcha Atrás` - 0 edges

## Surprising Connections (you probably didn't know these)
- `Luz Antiniebla Trasera` --semantically_similar_to--> `Luz de Posición`  [INFERRED] [semantically similar]
  Vehiculo/Luces-Niebla-Lluvia-Intensa.md → Vehiculo/Luces-Vehiculo.md
- `Luces con Niebla` --references--> `Luz de Carretera (Largas)`  [EXTRACTED]
  Vehiculo/Luces-Niebla-Lluvia-Intensa.md → Vehiculo/Luces-Vehiculo.md
- `Luces con Niebla` --references--> `Luz de Cruce (Cortas)`  [EXTRACTED]
  Vehiculo/Luces-Niebla-Lluvia-Intensa.md → Vehiculo/Luces-Vehiculo.md
- `Luces con Lluvia` --references--> `Luz de Carretera (Largas)`  [EXTRACTED]
  Vehiculo/Luces-Niebla-Lluvia-Intensa.md → Vehiculo/Luces-Vehiculo.md
- `Luces con Lluvia` --references--> `Luz de Cruce (Cortas)`  [EXTRACTED]
  Vehiculo/Luces-Niebla-Lluvia-Intensa.md → Vehiculo/Luces-Vehiculo.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Protocolo de Luces en Visibilidad Reducida** — vehiculo_luces_vehiculo_cruce, vehiculo_luces_niebla_lluvia_intensa_antiniebla_trasera, vehiculo_luces_niebla_lluvia_intensa_antiniebla_delantera [EXTRACTED 0.90]
- **Luces de Señalización y Seguridad** — vehiculo_luces_vehiculo_freno, vehiculo_luces_vehiculo_emergencia, vehiculo_luces_vehiculo_marcha_atras [INFERRED 0.85]

## Communities (8 total, 5 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.67
Nodes (4): Luces con Lluvia, Luces con Niebla, Luz de Carretera (Largas), Luz de Cruce (Cortas)

### Community 1 - "Community 1"
Cohesion: 0.67
Nodes (3): Luz Antiniebla Trasera, Luz de Posición, MOC Vehículo

## Knowledge Gaps
- **5 isolated node(s):** `Luz Antiniebla Delantera`, `Luz de Estacionamiento`, `Luz de Freno`, `Luz de Marcha Atrás`, `Luz de Emergencia (Warning)`
  These have ≤1 connection - possible missing edges or undocumented components.
- **5 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Luces con Niebla` connect `Community 0` to `Community 1`?**
  _High betweenness centrality (0.092) - this node is a cross-community bridge._
- **Why does `Luz Antiniebla Trasera` connect `Community 1` to `Community 0`?**
  _High betweenness centrality (0.056) - this node is a cross-community bridge._
- **Why does `Luces con Lluvia` connect `Community 0` to `Community 1`?**
  _High betweenness centrality (0.033) - this node is a cross-community bridge._
- **What connects `Luz Antiniebla Delantera`, `Luz de Estacionamiento`, `Luz de Freno` to the rest of the system?**
  _5 weakly-connected nodes found - possible documentation gaps or missing edges._