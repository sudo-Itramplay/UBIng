---
tags:
  - vim
  - ex-commands
  - global
  - reference
aliases:
  - comandes
  - global command
  - ex commands
---
# Comandes Ex

## Global Command (`:g`)

Executa un comando a totes les línies que matchin el patró.

```
:g/patró/comando
```

| Vull... | Comando |
|---------|---------|
| Esborrar línies amb "console" | `:g/console/d` |
| Esborrar línies SENSE "console" | `:v/console/d` o `:g!/console/d` |
| Esborrar línies amb "one" o "two" | `:g/one\|two/d` |
| Esborrar línies amb dígit | `:g/\d/d` |
| Rang (línies 1-5) | `:1,5g/console/d` |
| Copiar TODOs al final | `:g/TODO/t $` |
| Moure TODOs al final | `:g/TODO/m $` |
| Invertir tot el fitxer | `:g/^/m 0` |
| Reduir línies buides a 1 | `:g/^$/,/./-1j` |
| Afegir `;` a cada línia no-buida | `:g/./normal A;` |
| Executar macro a línies match | `:g/const/normal @a` |
| Sense guardar al register | `:g/console/d_` |

### Global recursiu

```
:g/console/g/two/d     → de les línies amb "console", esborra les que tenen "two"
:g/console/v/two/d     → de les línies amb "console", esborra les que NO tenen "two"
```

## Sort

| Vull... | Comando |
|---------|---------|
| Ordenar tot el fitxer | `:sort` |
| Ordenar rang | `:3,5sort` |
| Ordenar dins d'arrays | `:g/\[/+1,/\]/-1sort` |

## Argdo / Cfdo / Bufdo

| Vull... | Comando |
|---------|---------|
| Substituir a tots els fitxers amb match | `:grep "patró"` → `:cfdo %s/patró/nou/g \| update` |
| Substituir a buffers seleccionats | `:bufdo %s/vell/nou/g \| update` |
| Substituir a llista d'arguments | `:args *.txt` → `:argdo %s/vell/nou/g \| update` |

## Altres comandes útils

| Comanda | Què fa |
|---------|--------|
| `:Lazy` | Gestor de plugins |
| `:Mason` | Instal·lar LSP/formatters/linters |
| `:LazyHealth` | Comprovar salut |
| `:checkhealth` | Diagnòstics generals |
| `:Telescope projects` | Llistar projectes |
| `:Lazy reload` | Recarregar plugin |
| `:NeotestRun` | Executar test |
| `:w` | Guardar |
| `:q` | Tancar |
| `:wq` / `:x` | Guardar i tancar |
| `:q!` | Tancar sense guardar |
| `:e {fitxer}` | Obrir fitxer |
| `:find {fitxer}` | Buscar fitxer al path |
| `:sp` / `:vsp` | Split horitzontal / vertical |
| `:bn` / `:bp` | Buffer next / previous |
| `:bd` | Buffer delete |
| `:%bd \| e#` | Tancar tots excepte actual |
| `:noh` | Treure highlight de cerca |
| `:set {opció}?` | Veure valor d'opció |
