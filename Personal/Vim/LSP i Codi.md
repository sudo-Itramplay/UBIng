---
tags:
  - vim
  - lsp
  - code
  - reference
aliases:
  - goto definition
  - references
  - code action
  - rename
---
# LSP i Codi

## Navegació de codi

| Vull... | Key | Mode |
|---------|-----|------|
| Anar a definició | `gd` | n |
| Veure referències | `gr` | n |
| Anar a implementació | `gI` | n |
| Anar a definició de tipus | `gy` | n |
| Anar a declaració | `gD` | n |
| Hover (documentació) | `K` | n |

## Diagnòstics

| Vull... | Key | Mode |
|---------|-----|------|
| Diagnòstic de la línia | `<leader>cd` | n |
| Toggle diagnòstics | `<leader>cc` | n |
| Següent diagnòstic | `]d` | n |
| Anterior diagnòstic | `[d` | n |
| Següent error | `]e` | n |
| Anterior error | `[e` | n |
| Float diagnòstic | `<C-w><C-d>` | n |
| Llistar diagnòstics | `<leader>sd` | n |

## Accions de codi

| Vull... | Key | Mode |
|---------|-----|------|
| Code action | `<leader>ca` | n |
| Rename (LSP) | `<leader>cR` | n |
| Format | `<leader>cf` | n |
| Source action | `<leader>cA` | n |
| Inspect highlight | `<leader>ci` | n |

## Tests (Neotest)

| Vull... | Key | Mode |
|---------|-----|------|
| Run test més proper | `<leader>tt` | n |
| Run tests del fitxer | `<leader>tT` | n |
| Test summary | `<leader>ts` | n |
| Test output | `<leader>to` | n |
| Test output panel | `<leader>tO` | n |
| Stop tests | `<leader>tS` | n |
| Debug test | `<leader>td` | n |

## Comandes LSP útils

| Comanda | Què fa |
|---------|--------|
| `:LspInfo` | Info del LSP actiu |
| `:LspRestart` | Reiniciar LSP |
| `:ConformInfo` | Info del formatter |
| `:Mason` | Instal·lar LSP/formatters |
