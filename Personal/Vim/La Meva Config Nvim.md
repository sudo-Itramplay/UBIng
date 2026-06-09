---
tags:
  - vim
  - nvim
  - config
  - reference
aliases:
  - config
  - nvim config
  - lazyvim config
---
# La Meva Config Nvim

## Estructura

```
~/.config/nvim/
├── init.lua
├── lazyvim.json          → Extras activats
└── lua/
    ├── config/
    │   ├── autocmds.lua
    │   ├── keymaps.lua   → Keymaps personalitzats
    │   ├── lazy.lua      → Bootstrap lazy.nvim
    │   └── options.lua   → Opcions (relativenumber)
    └── plugins/
        ├── all-themes.lua
        ├── disable-news-alert.lua
        ├── latex.lua
        ├── notes.lua              → Obsidian + img-clip + render-markdown
        ├── omarchy-theme-hotreload.lua
        ├── opencode.lua
        ├── project.lua            → project.nvim + dashboard
        ├── snacks-animated-scrolling-off.lua
        └── plugin/after/
            └── transparency.lua
```

## Extras activats (lazyvim.json)

- `neo-tree` — Explorador de fitxers
- `lang.typescript` — TypeScript/JavaScript
- `lang.python` — Python
- `lang.json` / `lang.yaml` / `lang.docker` — Config files
- `lang.markdown` — Markdown support
- `ui.treesitter-context` — Context del codi
- `coding.yanky` — Portapapers avançat
- `editor.illuminate` — Highlight same word
- `formatting.prettier` / `formatting.black` — Formatters
- `linting.eslint` — Linter JS
- `test.core` — Neotest
- `editor.mini-diff` — Mini diff

## Keymaps personalitzats (keymaps.lua)

### Obsidian (`<leader>o`)

| Key | Acció |
|-----|-------|
| `<leader>on` | New note (`ObsidianNew`) |
| `<leader>oo` | Open in Obsidian app |
| `<leader>os` | Search notes |
| `<leader>ov` | Obrir vault Uni (`~/Uni/2nquadri`) |
| `<leader>or` | Rename note |
| `<leader>of` | Follow link |
| `<leader>ol` | List links |
| `<leader>ob` | Backlinks |
| `<leader>ot` | Search tags |
| `<leader>od` | Daily note (today) |
| `<leader>oy` | Yesterday's note |
| `<leader>oc` | Toggle checkbox |
| `<leader>op` | Paste image from clipboard |

### Run / Build (`<leader>r`)

| Key | Acció |
|-----|-------|
| `<leader>rr` | Run current file (snacks terminal) |
| `<leader>rb` | LaTeX compile |
| `<leader>rv` | LaTeX view PDF |
| `<leader>rs` | LaTeX stop |
| `<leader>rc` | LaTeX clean |
| `<leader>re` | LaTeX errors |

### Misc

| Key | Acció |
|-----|-------|
| `<leader>?` | Keymaps picker (snacks) |

## Obsidian workspace

```lua
workspaces = {
  { name = "uni", path = "~/Uni/2nquadri" }
}
```

- Notes: wiki links `[[link]]`
- Templates: `Templates/`
- Dailies: `Dailies/`
- Imatges: `Images/`

## Plugins addicionals

| Plugin | Què fa |
|--------|--------|
| `obsidian.nvim` | Integració Obsidian (links, cerca, backlinks) |
| `img-clip.nvim` | Enganxar imatges del clipboard |
| `render-markdown.nvim` | Renderitzar markdown inline |
| `project.nvim` | Gestió de projectes (LSP + patterns) |
| `snacks.nvim` | Dashboard + terminal + picker |

## Themes disponibles

bamboo, aether, ethereal, hackerman, catppuccin, everforest, flexoki, gruvbox, matteblack, monokai-pro, nord, rose-pine, tokyonight, kanagawa (actiu)
