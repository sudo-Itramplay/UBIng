---
tags:
  - vim
  - editing
  - reference
aliases:
  - editar
  - delete
  - copy
  - paste
  - yank
  - visual
  - undo
---
# Editar

## Esborrar

| Vull... | Comando | Mode |
|---------|---------|------|
| Caràcter sota cursor | `x` | n |
| Caràcter abans del cursor | `X` | n |
| Fins a final de línia | `D` | n |
| Línia sencera | `dd` | n |
| Fins a paraula següent | `dw` | n |
| Paraula actual | `diw` | n |
| Dins de parèntesi | `di(` | n |
| Parèntesi inclòs | `da(` | n |
| Dins de `{}` | `di{` | n |
| Dins de cometes `"` | `di"` | n |
| Dins de tag HTML | `dit` | n |
| Tag HTML inclòs | `dat` | n |
| Fins al final del fitxer | `dG` | n |
| Fins al principi | `dgg` | n |
| n línies | `{n}dd` | n |
| Sense guardar al register | `"_d` + motion | n |

## Copiar i Enganxar (Yank)

| Vull... | Comando | Mode |
|---------|---------|------|
| Copiar línia | `yy` | n |
| Copiar paraula | `yw` | n |
| Copiar fins a final de línia | `y$` | n |
| Copiar paraula actual | `yiw` | n |
| Copiar dins parèntesi | `yi(` | n |
| Copiar dins cometes | `yi"` | n |
| Copiar tot el fitxer | `:%y` | cmd |
| Enganxar després | `p` | n |
| Enganxar abans | `P` | n |
| Enganxar de l'historial (Yanky) | `<leader>p` | n |
| Cicle yanky següent | `]y` | n |
| Cicle yanky anterior | `[y` | n |

### Registers

| Register | Què conté |
|----------|-----------|
| `"` | Últim yank/delete (default) |
| `0` | Últim yank |
| `1-9` | Últims deletes (1 = més recent) |
| `a-z` | Registers amb nom (`"ayy` = copiar a register a) |
| `"_` | Black hole (descarta) |
| `"+` | Clipboard del sistema |
| `"*` | Selection clipboard |
| `:reg` | Veure tots els registers |

Exemple: `"ayy` copia línia al register a, `"ap` enganxa des de register a.

## Canviar (delete + insert)

| Vull... | Comando |
|---------|---------|
| Canviar paraula | `cw` |
| Canviar fins a final de línia | `C` |
| Canviar línia sencera | `cc` o `S` |
| Canviar dins parèntesi | `ci(` |
| Canviar paraula actual | `ciw` |

## Insert Mode

| Vull... | Key |
|---------|-----|
| Inserir després del cursor | `a` |
| Inserir abans del cursor | `i` |
| Afegir al final de línia | `A` |
| Inserir al principi de línia | `I` |
| Nova línia a sota | `o` |
| Nova línia a sobre | `O` |
| Sortir d'insert mode | `<Esc>` |
| Executar 1 comando normal | `<C-o>` + cmd |
| Acceptar suggeriment (Copilot/CMP) | `<C-s>` |
| Següent suggeriment | `<Tab>` |
| Anterior suggeriment | `<S-Tab>` |

## Visual Mode

| Vull... | Key | Mode |
|---------|-----|------|
| Selecció per caràcters | `v` | n |
| Selecció per línies | `V` | n |
| Selecció per blocs (columna) | `<C-v>` | n |
| Tornar a última selecció | `gv` | n |
| Canviar extrem de selecció | `o` / `O` | v |
| Sortir de visual | `<Esc>` o mateixa tecla | v |

### Operacions en Visual Mode

| Vull... | Comando en visual |
|---------|-------------------|
| Esborrar selecció | `d` o `x` |
| Copiar selecció | `y` |
| Canviar a majúscules | `U` o `gU` |
| Canviar a minúscules | `u` o `gu` |
| Substituir a selecció | `:s/vell/nou/g` |
| Indentar | `>` |
| Desindentar | `<` |
| Moure línies amunt/avall | `J` / `K` |
| Substituir caràcters | `r{x}` |
| Afegir a múltiples línies (bloc) | `<C-v>` → seleccionar → `A` o `I` → text → `<Esc>` |
| Incrementar números (bloc) | `<C-v>` → seleccionar → `g<C-a>` |

## Desfer i Refer

| Vull... | Key |
|---------|-----|
| Desfer | `u` |
| Refer | `<C-r>` |
| Desfer tota la línia | `U` |
| Veure historial d'undo | `:undolist` o `g+` / `g-` |

## Comentaris

| Vull... | Key | Mode |
|---------|-----|------|
| Comentar línia (toggle) | `gcc` | n |
| Comentar selecció | `gc` | v |
| Comentar bloc | `gb` | n |

## Edició ràpida

| Vull... | Key | Mode |
|---------|-----|------|
| Moure línia avall | `<A-j>` | n/i |
| Moure línia amunt | `<A-k>` | n/i |
| Moure selecció amunt/avall | `J` / `K` | v |
| Indentar (manté selecció) | `>` / `<` | v |
| Join línies | `J` | n |
| Repetir últim canvi | `.` | n |
| Reemplaçar caràcter | `r{x}` | n |
