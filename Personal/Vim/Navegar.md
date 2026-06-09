---
tags:
  - vim
  - navigation
  - motions
  - reference
aliases:
  - moure
  - navegar
  - motions
---
# Navegar

## Caràcter a caràcter

| Key | Acció |
|-----|-------|
| `h` | Esquerra |
| `j` | Avall |
| `k` | Amunt |
| `l` | Dreta |
| `gj` / `gk` | Avall/Amunt en línia wrapped |

> Tip: `[count] + motion` → `12j` = 12 línies avall

## Paraules

| Key | Acció |
|-----|-------|
| `w` | Endavant al principi de la paraula |
| `W` | Endavant al principi del WORD |
| `e` | Endavant al final de la paraula |
| `E` | Endavant al final del WORD |
| `b` | Enrere al principi de la paraula |
| `B` | Enrere al principi del WORD |
| `ge` | Enrere al final de la paraula |
| `gE` | Enrere al final del WORD |

> `word` = `[a-zA-Z0-9_]` | `WORD` = tot excepte espais

## Línia actual

| Key | Acció |
|-----|-------|
| `0` | Primer caràcter de la línia |
| `^` | Primer caràcter no-blanc |
| `$` | Últim caràcter de la línia |
| `g_` | Últim caràcter no-blanc |
| `n\|` | Columna n |
| `f{x}` | Endavant fins a {x} (inclòs) |
| `t{x}` | Endavant fins a {x} (abans) |
| `F{x}` / `T{x}` | Enrere |
| `;` | Repetir cerca (mateixa dir) |
| `,` | Repetir cerca (dir oposada) |

> Tip: busca lletres poc comunes (`j`, `x`, `z`) amb `f` per arribar ràpid

## Frases i paràgrafs

| Key | Acció |
|-----|-------|
| `(` | Frase anterior |
| `)` | Frase següent |
| `{` | Paràgraf anterior |
| `}` | Paràgraf següent |

## Números de línia

| Key | Acció |
|-----|-------|
| `gg` / `1G` | Primera línia |
| `G` | Última línia |
| `nG` | Línia n |
| `n%` | n% del fitxer |

## Finestra (viewport)

| Key | Acció |
|-----|-------|
| `H` | Top de la pantalla |
| `M` | Mig de la pantalla |
| `L` | Bottom de la pantalla |
| `nH` | n línies des del top |
| `nL` | n línies des del bottom |

## Scroll

| Key | Acció |
|-----|-------|
| `<C-e>` | Scroll avall 1 línia |
| `<C-d>` | Scroll avall mitja pantalla |
| `<C-f>` | Scroll avall pantalla sencera |
| `<C-y>` | Scroll amunt 1 línia |
| `<C-u>` | Scroll amunt mitja pantalla |
| `<C-b>` | Scroll amunt pantalla sencera |
| `zt` | Cursor a dalt de pantalla |
| `zz` | Cursor al mig de pantalla |
| `zb` | Cursor a baix de pantalla |

## Match de parèntesis

| Key | Acció |
|-----|-------|
| `%` | Saltar al parell de `()`, `[]`, `{}` |

## Flash (navegació ràpida - LazyVim)

| Key | Mode | Acció |
|-----|------|-------|
| `s` | n | Flash jump (escrius 1-2 lletres i saltes) |
| `S` | n | Flash treesitter select |
| `r` | o | Flash remote |
| `R` | n/x | Flash treesitter (visual) |
| `<C-s>` | c | Toggle flash al search |

## Harpoon2 (navegació ràpida entre fitxers)

| Key | Acció |
|-----|-------|
| `<leader>a` | Afegir fitxer a harpoon |
| `<C-e>` | Toggle menú harpoon |
| `<leader>1-4` | Anar a fitxer harpoon 1-4 |

## Jump List

| Key | Acció |
|-----|-------|
| `<C-o>` | Enrere al jump list |
| `<C-i>` | Endavant al jump list |
| `:jumps` | Veure historial de salts |
