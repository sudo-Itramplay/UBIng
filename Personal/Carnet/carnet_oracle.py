#!/usr/bin/env python3
"""
carnet_oracle.py — Predictor d'errors d'examen del carnet de conduir B.

Llegeix _MOC.md i els apunts atòmics, extreu paraules clau de cada pregunta,
agrupa errors per similitud de paraules clau, i genera recomanacions.

Ús:
    python3 carnet_oracle.py [--moc PATH] [--top N] [--json]
"""

import re
import sys
import argparse
import json as json_mod
from collections import Counter, defaultdict
from pathlib import Path

# ── Stop words (paraules buides que no aporten significat) ──

STOP_WORDS = {
    "el", "la", "los", "las", "un", "una", "unos", "unas", "de", "del", "al",
    "en", "por", "para", "con", "sin", "sobre", "entre", "hasta", "desde",
    "es", "son", "está", "están", "hay", "no", "sí", "se", "que", "como",
    "cuál", "qué", "dónde", "cuándo", "cuánto", "quién",
    "y", "o", "pero", "sino", "ni", "aunque", "si", "cuando", "donde",
    "puede", "debe", "deben", "tener", "hacer", "ir", "ver", "saber",
    "ser", "estar", "haber", "poder", "querer",
    "circula", "circular", "circulará", "pueden", "prohibido",
    "permitido", "obligatorio", "obligatoria",
    "señal", "señales", "vehículo", "vehículos", "vía", "vías",
    "tipo", "tipos", "caso", "casos", "forma", "parte",
    "según", "respecto", "acerca", "mediante",
    "dónde", "cuáles", "cómo", "cuándo", "cuántos",
    "esta", "este", "esto", "estos", "estas", "ese", "esa", "eso",
    "así", "tan", "solo", "solamente", "además", "también",
    "meter", "metros", "kilómetros", "km", "m",
    "uno", "dos", "tres", "cuatro", "cinco",
    "verdadero", "falso", "cierto", "incorrecto", "correcto",
    "cual", "maxima", "tengo", "usan", "cambia", "equivocado",
    "tienes", "girar", "aproximarse", "ademas", "tecnica", "anos",
    "hinchar", "introduce", "novedades", "identificar", "diferencia",
    "número", "números", "círculo", "llevar", "porque", "queda",
    "turismo", "turismos", "permiso", "mma",
}

# ── Diccionari mínim de sinònims ──

SYNONYMS = {
    # Convencions generals
    "vs": "diferencias",
    "diferencia": "diferencias",
    "diferència": "diferencias",

    # Velocitat
    "máxima": "velocidad",
    "máximas": "velocidad",
    "màxima": "velocidad",
    "màximes": "velocidad",
    "límite": "velocidad",
    "límits": "velocidad",
    "velocidades": "velocidad",

    # Aparcar / parar
    "estacionar": "estacionamiento",
    "estacionamiento": "estacionamiento",
    "aparcar": "estacionamiento",
    "parada": "parar",
    "parar": "parar",

    # Frenada
    "frenada": "frenada",
    "frenar": "frenada",
    "detención": "frenada",
    "detenció": "frenada",

    # Giros / sentit
    "glorieta": "rotonda",
    "rotonda": "glorieta",
    "giro": "sentido",
    "girar": "sentido",
    "dirección": "sentido",
    "direcció": "sentido",

    # Carretera
    "carretera": "vía",
    "via": "vía",
    "vies": "vía",

    # Prohibicions
    "prohibido": "prohibición",
    "prohibición": "prohibición",
    "prohibit": "prohibición",

    # Obligacions
    "obligatorio": "obligación",
    "obligació": "obligación",
    "obligatoria": "obligación",
}


def normalize(word: str) -> str:
    """Normalitza una paraula amb sinònims i accents."""
    # Primero sinónimos
    word = SYNONYMS.get(word, word)
    # Luego normalizar accents variants comuns
    accent_map = {
        "autovia": "autovía",
        "autopista": "autopista",
        "via": "vía",
        "unico": "único",
        "continua": "continúa",
    }
    return accent_map.get(word, word)


def extract_keywords(text: str, max_keywords: int = 5) -> list[str]:
    """Extreu paraules clau significatives d'un text."""
    text = text.lower()
    text = re.sub(r"[^\w\sáéíóúñü]", " ", text)
    words = text.split()
    keywords = []
    seen = set()
    for w in words:
        w = normalize(w)
        if w not in STOP_WORDS and len(w) >= 3 and w not in seen:
            keywords.append(w)
            seen.add(w)
        if len(keywords) >= max_keywords:
            break
    return keywords


def keyword_overlap(kw1: list[str], kw2: list[str]) -> float:
    """Calcula la similitud entre dues llistes de paraules clau."""
    s1, s2 = set(kw1), set(kw2)
    if not s1 or not s2:
        return 0.0
    intersection = s1 & s2
    # Pes per paraules més llargues (més especifiques)
    weight = sum(2 if len(w) >= 5 else 1 for w in intersection)
    max_possible = min(len(s1), len(s2)) * 2
    return weight / max_possible if max_possible > 0 else 0.0


def parse_moc(moc_path: Path) -> list[dict]:
    """Extreu cada entrada d'error del _MOC.md."""
    text = moc_path.read_text(encoding="utf-8")
    errors = []
    pattern = r"### (\d+)\.\s+(.+?)\n(.*?)(?=### \d+\.|---|\Z)"
    matches = re.findall(pattern, text, re.DOTALL)

    for num_str, title, body in matches:
        num = int(num_str)
        error_match = re.search(r"\*\*Error:\*\*\s*(.+)", body)
        correccion_match = re.search(r"\*\*Correcci[oó]n:\*\*\s*(.+)", body)
        error_text = error_match.group(1).strip() if error_match else ""
        correccion_text = correccion_match.group(1).strip() if correccion_match else ""
        link_match = re.search(r"\[\[([^\]]+)\]\]", body)
        link = link_match.group(1) if link_match else ""

        errors.append({
            "num": num,
            "title": title.strip(),
            "error": error_text,
            "correction": correccion_text,
            "link": link,
        })

    return errors


def load_keywords_from_notes(base_path: Path, errors: list[dict]) -> dict[int, list[str]]:
    """Llegeix els apunts atòmics i extreu paraules clau de cada pregunta."""
    keywords_map = {}

    for err in errors:
        if not err["link"]:
            continue

        # Busca el fitxer atòmic
        note_path = None
        for p in base_path.rglob(f"{err['link']}.md"):
            note_path = p
            break

        if not note_path:
            continue

        note_text = note_path.read_text(encoding="utf-8")

        # Extreu text de la pregunta
        question_match = re.search(
            r"## Pregunta de examen.*?\n\n> (.+?)(?:\n\n|\n\*\*)",
            note_text,
            re.DOTALL,
        )
        question = question_match.group(1).strip() if question_match else ""

        # Extreu correcció
        correction_match = re.search(r"\*\*Correcci[oó]n:\*\*\s*(.+)", note_text)
        correction = correction_match.group(1).strip() if correction_match else ""

        # Combina títol + pregunta + correcció per extreure paraules clau
        combined = f"{err['title']} {question} {correction}"
        keywords = extract_keywords(combined)
        keywords_map[err["num"]] = keywords

    return keywords_map


def group_errors_by_keywords(
    errors: list[dict],
    keywords_map: dict[int, list[str]],
    threshold: float = 0.4,
) -> list[list[dict]]:
    """Agrupa errors per similitud de paraules clau."""
    assigned = set()
    groups = []

    for err in sorted(errors, key=lambda e: e["num"]):
        num = err["num"]
        if num in assigned:
            continue

        group = [err]
        assigned.add(num)
        kw1 = keywords_map.get(num, [])

        for other in errors:
            other_num = other["num"]
            if other_num in assigned or other_num == num:
                continue
            kw2 = keywords_map.get(other_num, [])
            overlap = keyword_overlap(kw1, kw2)
            if overlap >= threshold:
                group.append(other)
                assigned.add(other_num)

        groups.append(group)

    return groups


def format_groups(
    groups: list[list[dict]],
    keywords_map: dict[int, list[str]],
    top_n: int = 10,
) -> str:
    """Formateja els grups per a la sortida."""
    # Ordena grups per mida (descendent) i després per número d'error mínim
    groups_sorted = sorted(groups, key=lambda g: (-len(g), g[0]["num"]))

    lines = []
    lines.append("=" * 65)
    lines.append("  ORACLE DEL CARNET DE CONDUIR B")
    lines.append(f"  {sum(len(g) for g in groups)} errors registrats")
    lines.append("=" * 65)
    lines.append("")

    for i, group in enumerate(groups_sorted[:top_n]):
        if len(group) < 2:
            # Error individual
            err = group[0]
            kws = keywords_map.get(err["num"], [])
            lines.append(f"  # {i+1:2d}  {err['title']}")
            lines.append(f"        1 error (error aïllat)")
            lines.append(f"       error: {err['num']}")
            lines.append(f"       keywords: {kws}")
            lines.append("")
        else:
            # Grup d'errors
            group_title = " + ".join(e["title"][:35] for e in group[:3])
            if len(group) > 3:
                group_title += f" + {len(group)-3} més"

            # Troba paraules clau compartides
            all_kws = [set(keywords_map.get(e["num"], [])) for e in group]
            if all_kws:
                shared = set.intersection(*all_kws) if all_kws else set()
            else:
                shared = set()

            lines.append(f"  # {i+1:2d}  {group_title}")
            lines.append(
                f"        {len(group)} errors ({len(group)*100//sum(len(g) for g in groups)}% del total)"
            )
            lines.append(f"       errors: {', '.join(str(e['num']) for e in group)}")
            lines.append(f"       keywords compartides: {sorted(shared) if shared else 'cap'}")
            lines.append("")

    # Recomanació pre-test
    lines.append("=" * 65)
    lines.append("  RECOMANACIÓ PRE-TEST")
    lines.append("  " + "─" * 45)
    lines.append("")

    # Top 3 grups més grans (només grups, no individuals)
    big_groups = [g for g in groups_sorted if len(g) >= 2][:3]
    if big_groups:
        for i, group in enumerate(big_groups):
            group_title = " + ".join(e["title"][:30] for e in group[:2])
            lines.append(f"  {i+1}. {group_title} ({len(group)} errors)")
        lines.append("")
        total_in_top = sum(len(g) for g in big_groups)
        total_errors = sum(len(g) for g in groups)
        pct = total_in_top * 100 // total_errors if total_errors else 0
        lines.append(
            f"  Si dominés aquests 3 grups, reduiries errors ~{pct}%."
        )
    else:
        lines.append("  No hi ha grups significatius de repetició.")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Oracle del carnet de conduir B")
    parser.add_argument(
        "--moc",
        default=str(Path(__file__).parent / "Cotxe" / "_MOC.md"),
        help="Path al fitxer _MOC.md",
    )
    parser.add_argument("--top", type=int, default=10, help="Número de grups a mostrar")
    parser.add_argument("--json", action="store_true", help="Sortida en format JSON")
    args = parser.parse_args()

    moc_path = Path(args.moc)
    base_path = moc_path.parent

    # Parseja el MOC
    errors = parse_moc(moc_path)

    # Carrega paraules clau dels apunts atòmics
    keywords_map = load_keywords_from_notes(base_path, errors)

    # Agrupa errors per similitud
    groups = group_errors_by_keywords(errors, keywords_map)

    if args.json:
        # Sortida JSON
        result = []
        for group in sorted(groups, key=lambda g: (-len(g), g[0]["num"])):
            shared = set.intersection(
                *[set(keywords_map.get(e["num"], [])) for e in group]
            ) if group else set()
            result.append({
                "size": len(group),
                "errors": [e["num"] for e in group],
                "titles": [e["title"] for e in group],
                "shared_keywords": sorted(shared),
            })
        print(json_mod.dumps(result, ensure_ascii=False, indent=2))
    else:
        # Sortida formatejada
        output = format_groups(groups, keywords_map, top_n=args.top)
        print(output)


if __name__ == "__main__":
    main()
