---
tags:
  - vim
  - macros
  - automation
  - reference
aliases:
  - macro
  - automatitzar
  - repetir
---
# Macros

## Enregistrar i executar

| Vull... | Comando |
|---------|---------|
| Enregistrar macro al register `a` | `qa` ... accions ... `q` |
| Executar macro del register `a` | `@a` |
| Executar macro n vegades | `n@a` (ex: `99@a`) |
| Repetir última macro | `@@` |
| Afegir a macro existent | `qA` ... accions ... `q` (majúscula = append) |

## Exemples pràctics

### Afegir `;` al final de cada línia

```
qa    → enregistrar a register a
A;    → append ; al final de línia
<Esc> → tornar a normal
j     → baixar una línia
q     → parar enregistrament
99@a  → executar 99 vegades
```

### Numerar línies

```
qa     → enregistrar
I      → insert al principi
<C-a>  → incrementar número
<Esc>  → sortir
j      → baixar
q      → parar
```

### Substituir amb macro + multi-fitxer

```
:args *.txt
qq
:%s/dog/chicken/g
:wnext
q
99@q
```

## Dot command (`.`)

| Vull... | Key |
|---------|-----|
| Repetir últim canvi | `.` |

El dot command repeteix l'últim canvi (insert, delete, change, etc.). És la "macro" més simple i més usada.

## Registers i macros

Les macros es guarden als registers `a-z`. Pots veure-les amb `:reg` i editar-les amb:

```
:let @a = 'contingut_de_la_macro'
```

Per enganxar una macro al register i editar-la:
```
"ap     → enganxa el contingut del register a
```
