# AGENTS.md

This file provides guidance when working with code in this repository.

## What this directory is

A personal university workspace, not a software project — course notes (Catalan) and lecture-slide PDFs. The active workspace is the **`UBIng/` Obsidian vault**, the unified **3rd-year mind vault** holding both quadrimesters. The other folders are leftover/reference material.

## Top-level layout

- `UBIng/` — the **canonical Obsidian vault / git repo** (see below). All current note-taking happens here.
- `2nquadri/` — **superseded.** Its Q2 notes were imported into `UBIng`. Kept only as a backup; don't add new notes here. (Old repo: `2n-quadri-Th`.)
- `PDFs/` — second-quadrimester lecture-slide PDFs mirrored by subject (`BD`, `FH`, `Gràfics`, `LL`, `SD`). Read-only reference outside the vault; do not generate or modify PDFs.
- `AGENTS.md` — this file. There is no git repo at this top level — only inside `UBIng/` (and the dormant `2nquadri/`).

## The `UBIng` Obsidian vault

The vault root **is** the repo root (`UBIng/`). Treat it as an Obsidian vault, not a generic markdown tree:

- **The repo is PUBLIC** (`origin → github.com/sudo-Itramplay/UBIng.git`). **Never commit secrets, passwords, or private data.** Commits in `git log` use short Catalan messages (`Apunts SD`, `Resums Parcials`) — match that style if asked to commit.
- `.obsidian/` config (community plugins: dataview, tasks, code-styler, toc, todoist-text). Do not disable plugins or rewrite config without being asked.
- Subjects live under `Uni/3rAny/Subjects/`, grouped by quadrimester:
  - `Q1/` — `IA`, `TNUI` (contains `Tallers/` + `ThTNUI/`), `Visio` (contains `TH/` + `ThVA/`), `Xarxes`
  - `Q2/` — `BD`, `FH`, `Grafics`, `Lògica i Llenguatges`, `Software Distribuit`
  - Each subject has (or should get) a curated `_MOC.md` index. Q2 uses per-exam subfolders `01-Parcial-1`, `02-Parcial-2`. Future years slot in as `Uni/4tAny/...` with the same `Subjects/Q1`+`Q2` shape.
- `Home.md` is the vault entry point; `Tuto.md` documents structure, tag convention, and the git workflow. Read `Tuto.md` before making structural changes.
- `Templates/` holds note templates wired via `.obsidian/templates.json`: `Apunt-Classe.md`, `Resum-Parcial.md`, `Practica.md`, `Projecte.md`, `Daily.md`. Create new notes from these so tags are preserved.
- `Images/` holds pasted screenshots (`Pasted image YYYYMMDDHHMMSS.png`), referenced via wiki-links — don't rename/move them, links break silently.
- `Dailies/` is the daily-notes folder (`.obsidian/daily-notes.json`, format `YYYY-MM-DD`, template `Templates/Daily`).
- `Altres/` — transversal reference (Python, Numpy, Pandas, Scikit-image, Mates, Obsidian), outside `Subjects/`.
- `Personal/` — non-academic personal notes, outside `Subjects/`.

### Note conventions

- **All notes are written in Catalan.** Write in Catalan unless asked otherwise. Match the tone: short headings, bullet lists, bold key terms, `**Referència: Diapositives X-Y**` lines pointing back to slides.
- Use Obsidian wiki-links (`[[Note Name]]`, `![[Pasted image ....png]]`) rather than markdown links. Prefer name-only links; many notes also use full-path links (`[[Uni/3rAny/Subjects/...]]`) — those break on move, so update them if you relocate files.
- Tag convention (Catalan): `#assignatura/<IA|TNUI|Visio|Xarxes|BD|FH|Grafics|LL|SD>` + `#tipus/<teoria|parcial|practica|projecte|daily|moc>`. Apply when editing untagged notes during normal work — don't do a mass-retag sweep (most imported Q1 notes are untagged).
- When you create a note, add it to the relevant `Uni/3rAny/Subjects/Q<n>/<assignatura>/_MOC.md`. An unlinked note is effectively invisible.
- File names often contain spaces, accents, and Catalan characters. Quote paths in shell commands; disable git path-quoting (`git -c core.quotepath=false`) when counting/parsing.

## Code lives outside the vault

Practice/exercise code is kept in its own GitHub repos, not in the vault — e.g. the IA Q-learning practice at `github.com/sudo-Itramplay/P3IA`. Don't re-add code or virtualenvs to the vault; link to the repo from a note instead.

## Working on this tree

- Default when asked about a topic: search `UBIng/Uni/3rAny/Subjects/Q<n>/<subject>/` first. Notes are the user's own synthesis; the `PDFs/` folder is raw source.
- When summarising or extending notes, preserve the existing structure rather than imposing a new format.
- **Git workflow**: everything on `main` (no per-quadrimester branches); commit often + per-quadrimester tags (`3r-Q1`, `3r-Q2`). See `UBIng/Tuto.md` → "Git / sync". Run `git` only inside `UBIng/` (or `2nquadri/`), not from `PDFs/` or this top level.
