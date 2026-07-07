# AGENTS.md — Carnet de Conduir B

## Què és aquest directori

Vault d'Obsidian amb apunts atòmics per a la preparació de l'examen teòric del **Permís B** (carnet de conduir). Cada apunt parteix d'una errada real dels tests de l'autoescola i es desenvolupa en format pregunta-resposta-explicació.

## Idioma

- **Tots els apunts han d'estar en castellà.** L'examen es fa en castellà.
- Els títols dels fitxers han d'estar en castellà (p.ex: `Senales-de-Peligro.md`, NO `Senyes-de-Percat.md`).
- Aquest fitxer (AGENTS.md) i `.carnet-preferences.md` poden ser en català.

## Estructura del vault

```
Cotxe/
├── _MOC.md                           # Resum Central (índex d'errors)
├── Adelantamiento/
├── Autobus/
├── Carriles/
├── Estacionamiento/
├── ITV/
├── Licencias/
├── Maniobras/
├── Motocicleta/
├── Preferencia/
├── Seguridad/
├── Semaforos/
├── Senales/
├── Tasas-Alcoholemia/
├── Tecnica/
├── Teoria/
└── Vehiculo/
```

## Estructura d'un apunt atòmic

Cada fitxer `.md` ha de seguir aquest patró:

```markdown
# Títol en castellà

## Pregunta de examen (errada)

> Text literal de la pregunta o errada

## Respuesta correcta

**VERDAD/FALSO.** Explicació breu de la resposta correcta.

## Explicacion detallada

### Subtema
- Punts clau
- Regles
- Diferències

### Quadre comparatiu (si escau)
| Concepte | Descripció |

### Errores habituales
| Error | Perill |

## Recordatorio

**Frase curta mnemotècnica.**

---

*Apunte relacionado: [[_MOC]]*
```

## Normativa de referència

- **DGT — Reglament General de Circulació (RGC)** vigent.
- **Reforma 23/06/2026:** Títol VI (zones urbanes), VMP, riders, motoristes (guants i calçat tancat obligatori a totes les vies).
- **Criteri:** si un test o app d'autoescola diu alguna cosa diferent de la DGT, preval la DGT.

## Regles de treball

1. **No barrejar català i castellà** en els apunts. Si un fitxer conté paraules catalanes (`senyalitzada`, `calçada`, `contínua`, `reprenre`, `camions petits`…), corregir-les.
2. **Mantenir tot en castellà** llevat d'aquest AGENTS.md i `.carnet-preferences.md`.
3. **Crear nous apunts** dins de la carpeta temàtica corresponent. Si no existeix la carpeta, preguntar abans de crear-la.
4. **Actualitzar `_MOC.md`** cada vegada que s'afegeixi o modifiqui un apunt:
   - Afegir el punt d'error amb format: `### N. Títol`, error, correcció, enllaç.
   - Afegir l'enllaç a l'índex de categories.
5. **No generar ni modificar PDFs** (es fan servir com a referència fora del vault).
6. **No crear codi o scripts** dins del vault; el codi va en repos separats.
7. **Enllaços wiki:** utilitzar `[[Nom-del-Fitxer]]` (Obsidian wiki-links). No renombrar fitxers sense actualitzar els enllaços.

## Formats especials

- **Pregunta errada:** bloque `> ` amb el text literal del test.
- **Resposta:** en negreta `**VERDAD/FALSO.**` seguida d'explicació.
- **Errores habituales:** taula amb dues columnes (`Error | Perill`).
- **Recordatorio:** frase curta en negreta per a memorització ràpida.

## Tags (opcionals)

Si es volen usar tags en els apunts, preferir el castellà:
- `#permiso-B`, `#teoria`, `#senalizacion`, `#normativa-2026`

## Git

- Els canvis es fan dins del vault `UBIng/` (repo de git).
- Cometre amb missatges curts en català (estil del repo): `Apunts carnet`, `Correccions errades`, etc.
- No cometre secrets ni dades personals.

---

*Última actualització: 25/06/2026*
