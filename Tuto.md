---
tags:
  - tipus/moc
---

# Tuto — Com està organitzat aquest vault

Aquest vault (repo **UBIng**) funciona com un **segon cervell**: un sol repositori per a tota la carrera, amb les notes organitzades per curs i quadrimestre. Un conjunt petit de notes índex (MOCs) i de plantilles fan que tot sigui fàcil de trobar i d'ampliar.

Si només recordes una cosa: **obre [[Home]] i des d'allà arribes a tot**.

---

## Estructura de carpetes

```
UBIng/                       ← arrel del vault = repo de tota la carrera
├── Home.md                  ← punt d'entrada
├── Tuto.md                  ← aquest fitxer
├── Uni/
│   └── 3rAny/
│       └── Subjects/
│           ├── Q1/          ← primer quadrimestre
│           │   ├── IA/
│           │   ├── TNUI/    (Tallers + ThTNUI)
│           │   ├── Visio/   (TH + ThVA)
│           │   └── Xarxes/
│           └── Q2/          ← segon quadrimestre
│               ├── BD/      ├── FH/  ├── Grafics/
│               ├── Lògica i Llenguatges/  └── Software Distribuit/
├── Templates/               ← plantilles per crear notes noves
├── Dailies/                 ← notes diàries (YYYY-MM-DD.md)
├── Images/                  ← captures enganxades
├── Altres/                  ← referència transversal (Python, Mates, Obsidian)
├── Personal/                ← notes personals (no acadèmiques)
└── .obsidian/               ← config del vault
```

Cada assignatura té (o tindrà) un `_MOC.md` que n'indexa les notes. Anys futurs s'afegeixen com `Uni/4tAny/...` amb la mateixa estructura `Subjects/Q1` i `Subjects/Q2`.

---

## Convenció de tags

Cada nota nova porta **dos tags**: un d'assignatura i un de tipus.

### Tags d'assignatura

**Q1:** `#assignatura/IA` · `#assignatura/TNUI` · `#assignatura/Visio` · `#assignatura/Xarxes`
**Q2:** `#assignatura/BD` · `#assignatura/FH` · `#assignatura/Grafics` · `#assignatura/LL` · `#assignatura/SD`

### Tags de tipus

`#tipus/teoria` · `#tipus/parcial` · `#tipus/practica` · `#tipus/projecte` · `#tipus/daily` · `#tipus/moc`

> Les notes importades de Q1 encara no tenen tags. No cal tocar-les en bloc: ves afegint-los quan obris una nota per editar-la.

---

## MOCs

Un **MOC** (Map of Content) és una nota índex que enllaça amb d'altres:

- `Home.md` — MOC arrel, enllaça als MOCs d'assignatura.
- `Subjects/Q<n>/<assignatura>/_MOC.md` — MOC d'assignatura.

**Regla d'or**: si una nota no apareix en cap MOC, és invisible. Quan creïs una nota nova, posa-la al MOC.

---

## Git / sync — com treballo el repo

Repo a GitHub (`origin → github.com/sudo-Itramplay/UBIng`).

**Tot viu a `main`.** No faig una branca per quadrimestre: les notes són additives (cada quadrimestre va a la seva carpeta) i les branques amagarien notes entre elles i lluitarien amb la sincronització. El flux és: editar → commit sovint → push.

- **Commits**: estil curt en català — `Apunts BD`, `Resum FH parcial 1`, etc.
- **Tags per quadrimestre**: en acabar un quadrimestre, marco una foto fixa: `git tag 3r-Q1` / `git tag 3r-Q2` + `git push --tags`.
- **Branca d'esborrany (opcional)**: per a una reorganització grossa i arriscada, una branca temporal `scratch` que fusiono o elimino.

> ⚠️ No desis mai contrasenyes ni secrets al vault: el repo és **públic**.
