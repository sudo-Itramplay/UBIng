---
id: User Story
aliases: []
tags:
  - assignatura/ES
  - tipus/teoria
---

# User Story

**Referència: [[UserStories]] Diapositives 4-6, 15-17**

**Requisit d'usuari** que s'ha d'implementar al sistema lliurat, escrit per **iniciar la conversa** — no és una especificació final.

Format de la card:

```
As a <role>
I want <goal>
So that <benefit>
Acceptance criteria:
...
```

- **"So that <benefit>"** és el **valor**: sense aquesta clàusula no saps per què existeix la story.
- La finalitat és **començar la conversa** sobre què necessita el negoci i com es pot satisfer amb programari.
- **No és** una especificació final lliurada per implementar; els detalls surten a la [[Three C's|Conversation]] amb el PO.
- **Qui l'escríu**: el **client**, no el desenvolupador.

No tot és una story — **no encaixis al format**:

- **Change requests**, **constraints** (rendiment requerit, stack, base de dades) i **requisits tècnics** (protocol, estàndards de seguretat) → **text pla**.
- Stories de **backend** són habitualment un tema **difícil**.

Exemples **dolents** del PDF:

- "Auto-save every few minutes" → *"As a player, I want auto-save the current game after key events, so that one does not have to repeat the whole stage."*
- "Add tips and reminders of user interface functionality" → *"As a novice player, I want UI tips so that I can get familiar with controls and icons"*
- "Fix bug #127" / "Decrease loading time" → sense rol ni benefici.

> [!warning] Regla mnemotècnica: **write stories, not tasks**. "Fix bug #127" i "Decrease loading time" són tasques/objectius, no stories.

Vegeu també: [[INVEST]] · [[Piràmide de requisits]] · [[Product Backlog]]
