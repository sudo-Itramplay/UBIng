---
tags:
  - vim
  - lazyvim
  - keybinds
  - reference
aliases:
  - lazyvim
  - keybinds
  - shortcuts
---
# LazyVim Keybinds

> Leader: `<Space>` | Colorscheme: **Kanagawa Dragon**

## General (`<leader>c`)

| Key | Acció |
|-----|-------|
| `<leader>cl` | Lazy (plugins) |
| `<leader>cm` | Mason (LSP/formatters) |
| `<leader>cd` | Diagnòstic línia |
| `<leader>cc` | Toggle diagnòstics |
| `<leader>cR` | Rename (LSP) |
| `<leader>ca` | Code action |
| `<leader>cf` | Format |
| `<leader>cr` | Canviar directori arrel |
| `<leader>ci` | Inspect highlight |
| `<leader>cA` | Source action |

## Toggles (`<leader>u`)

| Key | Acció |
|-----|-------|
| `<leader>uh` | Inlay hints |
| `<leader>uw` | Wrap |
| `<leader>us` | Spellcheck |
| `<leader>ul` | Line numbers |
| `<leader>ud` | Diagnostics |
| `<leader>uc` | Conceal |
| `<leader>uf` | Format on save |
| `<leader>ug` | Signcolumn |
| `<leader>uL` | Statusline |
| `<leader>uT` | Tabline |

## Buffers (`<leader>b`)

| Key | Acció |
|-----|-------|
| `<leader>bd` | Tancar buffer |
| `<leader>bD` | Tancar (forçat) |
| `<leader>bb` | Seleccionar buffer |
| `<leader>bp` | Pin buffer |
| `<leader>bP` | Tancar no-pinnejats |
| `H` / `L` | Buffer anterior / següent |
| `[b` / `]b` | Buffer anterior / següent |

## Fitxers (`<leader>f`)

| Key | Acció |
|-----|-------|
| `<leader>ff` | Cercar fitxers |
| `<leader>fR` | Fitxers recents |
| `<leader>fb` | Cercar entre buffers |
| `<leader>fg` | Grep (text) |
| `<leader>fG` | Grep (cwd) |
| `<leader>fw` | Paraula (live grep) |
| `<leader>fd` | Dotfiles |
| `<leader>ft` | Colorschemes |
| `<leader>fh` | Help |
| `<leader>fe` | Explorer (root) |
| `<leader>fE` | Explorer (cwd) |
| `<leader>e` | Toggle explorer |

## Cerca (`<leader>s`)

| Key | Acció |
|-----|-------|
| `<leader>sg` | Grep |
| `<leader>sG` | Grep (cwd) |
| `<leader>sw` | Paraula sota cursor |
| `<leader>sW` | Paraula (cwd) |
| `<leader>ss` | Goto symbol (document) |
| `<leader>sS` | Goto symbol (workspace) |
| `<leader>sb` | Cerca al buffer |
| `<leader>sc` | Comandes |
| `<leader>sC` | Historial comandes |
| `<leader>sh` | Help |
| `<leader>sm` | Man pages |
| `<leader>sk` | Keymaps |
| `<leader>sf` | Fitxers |
| `<leader>sr` | Reprendre cerca |
| `<leader>sd` | Diagnòstics |
| `<leader>so` | Opcions |
| `<leader>sp` | Projectes |
| `<leader>s.` | Fitxers recents |
| `<leader>s/` | Buffer (fuzzy) |

## Git (`<leader>g`)

| Key | Acció |
|-----|-------|
| `<leader>gg` | LazyGit |
| `<leader>gG` | LazyGit (cwd) |
| `<leader>gb` | Git blame |
| `<leader>gB` | Git browse (GitHub) |
| `<leader>gf` | File history |
| `<leader>gL` | Git log |
| `<leader>gl` | Git log (fitxer) |
| `<leader>gs` | Git status |
| `<leader>gd` | Git diff |
| `]h` / `[h` | Següent / Anterior hunk |

## LSP

| Key | Acció |
|-----|-------|
| `gd` | Goto definition |
| `gr` | References |
| `gI` | Implementation |
| `gy` | Type definition |
| `gD` | Goto declaration |
| `K` | Hover documentation |
| `]d` / `[d` | Diagnòstic següent / anterior |
| `]e` / `[e` | Error següent / anterior |
| `<C-w><C-d>` | Float diagnòstic |

## Obsidian (`<leader>o`)

| Key | Acció |
|-----|-------|
| `<leader>on` | New note |
| `<leader>oo` | Open in Obsidian app |
| `<leader>os` | Search notes |
| `<leader>ov` | Vault (Uni) |
| `<leader>or` | Rename note |
| `<leader>of` | Follow link |
| `<leader>ol` | List links |
| `<leader>ob` | Backlinks |
| `<leader>ot` | Search tags |
| `<leader>od` | Daily note (today) |
| `<leader>oy` | Yesterday's note |
| `<leader>oc` | Checkbox toggle |
| `<leader>op` | Paste image |

## Run / Build (`<leader>r`)

| Key | Acció |
|-----|-------|
| `<leader>rr` | Run current file |
| `<leader>rb` | LaTeX build |
| `<leader>rv` | LaTeX view PDF |
| `<leader>rs` | LaTeX stop |
| `<leader>rc` | LaTeX clean |
| `<leader>re` | LaTeX errors |

## Misc

| Key | Acció |
|-----|-------|
| `<leader>?` | Keymaps picker |
| `<leader>qq` | Sortir de tot |
| `<leader>q` | Tancar finestra |
| `<leader>mp` | Markdown preview |

## Plugins actius

LazyVim, blink.cmp, bufferline, conform, flash, gitsigns, grug-far, harpoon2, kanagawa, lazy.nvim, lualine, markdown-preview, mason, mini.ai, mini.diff, mini.pairs, neo-tree, neotest, noice, nvim-lint, nvim-lspconfig, nvim-treesitter, obsidian.nvim, persistence, project.nvim, render-markdown, snacks, telescope, todo-comments, trouble, vimtex, which-key, yanky
