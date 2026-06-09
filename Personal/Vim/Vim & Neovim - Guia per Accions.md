---
tags:
  - vim
  - nvim
  - lazyvim
  - reference
---
# Vim & Neovim - Guia per Accions

> Guia organitzada per **accions**: busca què vols fer i troba com fer-ho.
> Leader: `<Space>` | Colorscheme: **Kanagawa Dragon**

---

## Què vols fer?

| Vull... | Nota | Exemple ràpid |
|---------|------|---------------|
| Cercar text al fitxer | [[Cercar]] | `/patró`, `n`, `N`, `*`, `#` |
| Cercar fitxers, funcions o variables | [[Cercar#Cercar fitxers i símbols (LazyVim)]] | `<leader>ff`, `<leader>fg`, `<leader>ss` |
| Substituir / Reemplaçar text | [[Substituir]] | `:s/vell/nou/g`, `:%s/patró/canvi/gc` |
| Moure'm pel fitxer | [[Navegar]] | `w`, `b`, `f{x}`, `gg`, `G`, `%` |
| Saltar a definicions / referències | [[LSP i Codi]] | `gd`, `gr`, `gI`, `K` |
| Esborrar text | [[Editar#Esborrar]] | `dw`, `dd`, `diw`, `di(`, `D` |
| Copiar i enganxar | [[Editar#Copiar i Enganxar (Yank)]] | `yy`, `yw`, `p`, `P`, `<leader>p` |
| Seleccionar text | [[Editar#Visual Mode]] | `v`, `V`, `<C-v>` |
| Desfer / Refer | [[Editar#Desfer i Refer]] | `u`, `<C-r>` |
| Canviar entre buffers / finestres | [[Buffers i Finestres]] | `H`/`L`, `<C-h/j/k/l>`, `<leader>-` |
| Toggles (wrap, spell, números...) | [[Toggles]] | `<leader>ul`, `<leader>us`, `<leader>uw` |
| Git (diff, blame, log...) | [[Git]] | `<leader>gg`, `<leader>gb`, `]h` |
| Executar / Compilar | [[Executar]] | `<leader>rr`, `<leader>rb` |
| Gestionar fitxers múltiples | [[Substituir#Multi-fitxer]] | `:cfdo %s/vell/nou/g \| update` |
| Macros i repetició | [[Macros]] | `qa`, `@a`, `99@a` |
| Comandes Ex / Global | [[Comandes-Ex]] | `:g/patró/d`, `:sort`, `:argdo` |

---

## Gramàtica Vim (la regla d'or)

```
verb + noun  →  operador + moviment
```

| Verbs (operadors) | Nouns (moviments / objectes) |
|---|---|
| `d` esborrar | `w` paraula, `$` final línia, `i(` dins parèntesi |
| `y` copiar | `j` avall, `G` final fitxer, `iw` paraula interior |
| `c` canviar | `f{x}` fins a x, `}` paràgraf, `i"` dins cometes |
| `gU` majúscules | `nG` línia n, `/patró` cerca |
| `gu` minúscules | `^` principi línia, `i{` dins bloc |

Exemples: `dw` = esborrar fins a paraula, `yi(` = copiar dins parèntesi, `gU$` = majúsques fins al final.

---

## Subnotes

- [[Cercar]]
- [[Substituir]]
- [[Navegar]]
- [[Editar]]
- [[LSP i Codi]]
- [[Buffers i Finestres]]
- [[Toggles]]
- [[Git]]
- [[Executar]]
- [[Macros]]
- [[Comandes-Ex]]
- [[LazyVim Keybinds]]
- [[La Meva Config Nvim]]
