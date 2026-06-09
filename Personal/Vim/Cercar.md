---
tags:
  - vim
  - search
  - reference
aliases:
  - buscar
  - find
  - grep
  - cercar fitxers
  - cercar funcions
  - cercar variables
---
# Cercar

## Dins del fitxer actual

| Vull... | Comando | Mode |
|---------|---------|------|
| Cercar endavant | `/patró` | n |
| Cercar enrere | `?patró` | n |
| Repetir cerca (mateixa direcció) | `n` | n |
| Repetir cerca (direcció oposada) | `N` | n |
| Cercar paraula sota cursor (endavant) | `*` | n |
| Cercar paraula sota cursor (enrere) | `#` | n |
| Cercar paraula parcial (endavant) | `g*` | n |
| Cercar paraula parcial (enrere) | `g#` | n |
| Repetir última cerca exacta | `//` | n |
| Historial de cerques | `:history /` | cmd |
| Treure highlight de cerca | `:noh` o `<esc><esc>` | n |
| Cercar a la línia actual (endavant) | `f{x}` | n |
| Cercar a la línia (abans de x) | `t{x}` | n |
| Cercar a la línia (enrere) | `F{x}` / `T{x}` | n |
| Repetir cerca a línia | `;` (mateixa) / `,` (oposada) | n |

### Regex útil per cercar

| Patró | Què fa |
|-------|--------|
| `\d` | Qualsevol dígit `[0-9]` |
| `\D` | No-dígit |
| `\w` | Caràcter de paraula `[0-9A-Za-z_]` |
| `\s` / `\S` | Espai / No-espai |
| `\l` / `\u` | Minúscula / Majúscula |
| `^` | Principi de línia |
| `$` | Final de línia |
| `\v` | Magic mode (no cal escapar `(){}|`) |
| `\zs` / `\ze` | Inici / Final del match |
| `[a-z]` | Rang de caràcters |
| `[^x]` | Qualsevol caràcter excepte x |
| `\+` | Un o més (escapat) |
| `*` | Zero o més |
| `\{n,m}` | Entre n i m repeticions |
| `.\{-}` | Non-greedy (match mínim) |
| `\|` | OR (sense `\v`) |

Exemples:
- `/\v\d{3}-\d{4}` → números tipus `123-4567`
- `/^func\s` → línies que comencen amb "func "
- `/".\{-}"` → contingut entre cometes (non-greedy)
- `/\v(hello|hola)` → "hello" o "hola"

### Case sensitivity

| Opció | Efecte |
|-------|--------|
| `set ignorecase` | Totes les cerques case-insensitive |
| `set smartcase` | Case-sensitive si hi ha majúscula al patró |
| `\C` al patró | Força case-sensitive (`/\Chello`) |

---

## Cercar fitxers i símbols (LazyVim)

### Fitxers

| Vull... | Keybind | Què fa |
|---------|---------|--------|
| Cercar fitxers per nom | `<leader>ff` | Telescope find files |
| Fitxers recents | `<leader>fR` o `<leader>s.` | Recent files |
| Cercar entre buffers oberts | `<leader>fb` | Buffer list |
| Explorador de fitxers | `<leader>e` / `<leader>fe` | Neo-tree |
| Colorschemes | `<leader>ft` | Theme picker |

### Text / Contingut

| Vull... | Keybind | Què fa |
|---------|---------|--------|
| Grep al projecte | `<leader>fg` / `<leader>sg` | Live grep |
| Grep al cwd | `<leader>fG` / `<leader>sG` | Grep (cwd) |
| Paraula sota cursor | `<leader>sw` | Search word |
| Paraula (cwd) | `<leader>sW` | Search word cwd |
| Cerca al buffer actual | `<leader>sb` / `<leader>s/` | Buffer fuzzy search |
| Reprendre última cerca | `<leader>sr` | Resume |

### Símbols (funcions, variables, classes)

| Vull... | Keybind | Què fa |
|---------|---------|--------|
| Símbols del document | `<leader>ss` | Goto symbol (document) |
| Símbols del workspace | `<leader>sS` | Goto symbol (workspace) |
| Diagnòstics | `<leader>sd` | Llistar errors/warnings |

### Altres

| Vull... | Keybind | Què fa |
|---------|---------|--------|
| Help de Vim | `<leader>sh` / `<leader>fh` | Help tags |
| Comandes | `<leader>sc` | Command palette |
| Historial de comandes | `<leader>sC` | Command history |
| Keymaps | `<leader>sk` | Keymap picker |
| Man pages | `<leader>sm` | Unix man pages |
| Opcions | `<leader>so` | Vim options |
| Projectes | `<leader>sp` | Telescope projects |

---

## Marks (marcadors de posició)

| Vull... | Comando | Notes |
|---------|---------|-------|
| Marcar posició | `m{x}` | `a-z` = local, `A-Z` = global |
| Saltar a mark (exacte) | `` `x `` | Línia + columna |
| Saltar a mark (línia) | `'x` | Només línia |
| Tornar abans de l'últim salt | `''` o ` `` ` | |
| Inici de l'últim canvi | `` `[ `` | |
| Final de l'últim canvi | `` `] `` | |
| Última selecció visual | `` `< `` / `` `> `` | |
| Veure tots els marks | `:marks` | |

---

## Jump List

| Vull... | Comando |
|---------|---------|
| Enrere al jump list | `<C-o>` |
| Endavant al jump list | `<C-i>` |
| Veure jumps | `:jumps` |

Mots que compten com a "jump": `G`, `/`, `?`, `n`, `N`, `%`, `(`, `)`, `{`, `}`, `H`, `M`, `L`, `[[`, `]]`, `'`, `` ` ``
