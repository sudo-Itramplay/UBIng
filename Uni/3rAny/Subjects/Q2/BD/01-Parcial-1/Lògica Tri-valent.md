La presència de [[NULL]] obliga a abandonar la lògica binària i adoptar tres valors: **Cert, Fals i Desconegut (Unknown)**. Qualsevol comparació amb un NULL dona `unknown`.

**Taules de veritat:**
- **OR:** `unknown OR true = true` · `unknown OR false = unknown` · `unknown OR unknown = unknown`
- **AND:** `unknown AND true = unknown` · `unknown AND false = false` · `unknown AND unknown = unknown`
- **NOT:** `NOT unknown = unknown`

**Impacte en les operacions:**
- **[[Selecció]]:** només es mantenen les files on el predicat és estrictament `true` (es descarten `false` i `unknown`).
- **[[Join]]:** si un dels atributs del join és NULL, la fila no s'afegeix.
- **[[Projecció]] / conjunts:** els NULLs es tracten com valors normals per detectar duplicats.

Relacionat: [[NULL]] · [[Selecció]] · [[Restriccions d'Integritat]]

#assignatura/BD #tipus/teoria
