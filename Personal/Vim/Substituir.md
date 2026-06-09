---
tags:
  - vim
  - substitute
  - replace
  - reference
aliases:
  - reemplaçar
  - find and replace
  - sed
---
# Substituir

## Bàsic

| Vull... | Comando | Exemple |
|---------|---------|---------|
| Substituir a la línia actual | `:s/vell/nou/` | `:s/good/awesome/` |
| Substituir a tot el fitxer | `:%s/vell/nou/` | `:%s/let/const/` |
| Substituir totes les ocurrències (línia) | `:s/vell/nou/g` | flag `g` = global |
| Substituir amb confirmació | `:s/vell/nou/gc` | flag `c` = confirm |
| Substituir case-insensitive | `:s/vell/nou/gi` | flag `i` |
| Repetir última substitució | `&` o `:s` | |
| Repetir amb flags | `:&&` | |
| Usar últim patró de cerca | `:s//nou/` | Si `/vell` era l'última cerca |

## Rang

| Vull... | Comando |
|---------|---------|
| Línies 3 a 5 | `:3,5s/vell/nou/` |
| Des de línia actual fins a 10 | `:,10s/vell/nou/` |
| Des de línia 1 fins a actual | `:1,s/vell/nou/` |
| Tot el fitxer | `:%s/vell/nou/` |
| Selecció visual | Seleccionar + `:s/vell/nou/` |

## Grups de captura

Amb `\v` (magic mode) per no haver d'escapar:

| Vull... | Comando |
|---------|---------|
| Intercanviar dues paraules | `:%s/\v(\w+) (\w+)/\2 \1/` |
| Embolcallar amb cometes | `:%s/\d/"\0"/` o `:%s/\d/"&"/` |
| Majúscules al match | `:s/patró/\U&/g` |
| Majúscules al grup 2 | `:s/\v(\w+) (\w+)/\1 \U\2/` |
| Capitalitzar primera lletra | `:s/\<./\U&/g` |

| Símbol | Significat |
|--------|------------|
| `\0` o `&` | Tot el match |
| `\1`, `\2`, `\3` | Grup de captura 1, 2, 3 |
| `\U` | Majúscules el següent |
| `\L` | Minúscules el següent |
| `\E` | Final de `\U` o `\L` |

## Delimitadors alternatius

Quan el patró conté `/`, canvia el delimitador:

```
:s+https://exemple.com+hello+
:s#path/to/file#new/path#
```

## Patrons avançats

| Vull... | Patró |
|---------|-------|
| Match entre cometes | `/"[^"]\+"/` |
| Match entre cometes simples | `/'[^']\+'/` |
| "hello" o "hola" | `/\v(hello\|hola)/` |
| Només "cake" dins "hotcake" | `/hot\zscake/` |
| 3r match de "Mississippi" | `/\v(.{-}\zsMississippi){3}/` |
| Greedy (match llarg) | `a.*1` |
| Non-greedy (match curt) | `a.\{-}1` |

## Multi-fitxer

### Mètode 1: grep + cfdo (tots els fitxers amb match)

```vim
:grep "pizza"
:cfdo %s/pizza/donut/g | update
```

### Mètode 2: bufdo (fitxers seleccionats)

```vim
" Seleccionar fitxers amb Telescope (multi-select amb <Tab>)
:bufdo %s/pizza/donut/g | update
```

### Mètode 3: argdo (llista d'arguments)

```vim
:args *.txt
:argdo %s/dog/chicken/g | update
```

### Mètode 4: Macros + multi-fitxer

```vim
:args *.txt
qq
:%s/dog/chicken/g
:wnext
q
99@q
```

---

## Grug-far (LazyVim plugin)

LazyVim inclou **grug-far.nvim** per fer Find & Replace visual. Buscar-lo amb:
```
<leader>sc → "grug" o "replace"
```
