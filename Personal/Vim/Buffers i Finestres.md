---
tags:
  - vim
  - buffers
  - windows
  - splits
  - reference
aliases:
  - buffers
  - finestres
  - splits
---
# Buffers i Finestres

## Buffers

| Vull... | Key | Mode |
|---------|-----|------|
| Buffer següent | `L` o `]b` | n |
| Buffer anterior | `H` o `[b` | n |
| Seleccionar buffer | `<leader>bb` | n |
| Tancar buffer | `<leader>bd` | n |
| Tancar buffer (forçat) | `<leader>bD` | n |
| Pin buffer | `<leader>bp` | n |
| Tancar no-pinnejats | `<leader>bP` | n |
| Tancar finestra | `<leader>q` | n |
| Sortir de tot | `<leader>qq` | n |

## Splits / Finestres

| Vull... | Key | Mode |
|---------|-----|------|
| Split horitzontal | `<leader>-` | n |
| Split vertical | `<leader>\|` | n |
| Anar a finestra esquerra | `<C-h>` | n |
| Anar a finestra avall | `<C-j>` | n |
| Anar a finestra amunt | `<C-k>` | n |
| Anar a finestra dreta | `<C-l>` | n |
| Reduir finestra (vertical) | `<C-Up>` | n |
| Augmentar finestra (vertical) | `<C-Down>` | n |
| Reduir finestra (horitzontal) | `<C-Left>` | n |
| Augmentar finestra (horitzontal) | `<C-Right>` | n |

## Persistence (sessions)

LazyVim inclou **persistence.nvim** per restaurar sessions. Els buffers, finestres i posició del cursor es guarden automàticament.
