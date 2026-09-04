#!/usr/bin/env python3
"""
carnet_oracle.py — Predictor d'errors d'examen del carnet de conduir B.

Llegeix _MOC.md, classifica errors per tema específic (mínim 3 paraules
significatives), calcula la probabilitat d'error per tema, i genera
recomanacions personalitzades.

Ús:
    python3 carnet_oracle.py [--moc PATH] [--top N] [--json]
"""

import re
import sys
import argparse
import json as json_mod
from collections import Counter, defaultdict
from pathlib import Path

# ── Taxonomia de temes específics ──
# Cada tema té 3+ paraules clau que l'identifiquen.
# Format: (id_tema, paraules_clau)

TOPICS = [
    # SEÑALIZACIÓN
    ("señales prohibido estacionar R-308 días", ["estacionamiento", "prohibido", "r-308", "días", "romanos", "quincena"]),
    ("señales prohibido circular entrada", ["circulación", "prohibida", "r-100", "r-101", "entrada"]),
    ("señales peligro niebla precipitaciones", ["niebla", "precipitaciones", "viento", "p-15", "p-16", "p-17", "visibilidad"]),
    ("señales indicación área descanso servicio", ["descanso", "servicio", "merendero", "s-123", "s-127"]),
    ("señales paso nivel barreras aspa", ["paso", "nivel", "barreras", "aspa", "p-8a", "p-8b", "ferrocarril"]),
    ("señales ciclomotor motocicleta confusión", ["ciclomotor", "motocicleta", "confusión", "triángulo", "círculo"]),
    ("señales cruz fondo azul farmacia hospital", ["cruz", "fondo", "azul", "farmacia", "hospital", "roja"]),
    ("señales panel complementario flecha distancia", ["panel", "complementario", "flecha", "distancia", "metros"]),
    ("señales velocidad aconsejada panel azul", ["velocidad", "aconsejada", "panel", "azul", "cuadrado"]),
    ("señales vado R-3h R-3g parada estacionamiento", ["vado", "r-3h", "r-3g", "diagonal", "cruces"]),
    ("señales verticales derecha izquierda frente", ["verticales", "derecha", "izquierda", "frente", "carril"]),
    ("señales aplicación calzada no segregada", ["calzada", "aplicación", "segregada", "no"]),
    ("señales carril bici motos bicicletas", ["carril", "bici", "motos", "bicicletas"]),
    ("señales prioridad derecha cruces intersecciones", ["prioridad", "derecha", "cruces", "intersecciones"]),
    ("señales R-302 R-303 cambio sentido giros", ["r-302", "r-303", "cambio", "sentido", "giro"]),

    # ADELANTAMIENTO
    ("adelantamiento espacio prohibido no dejar", ["adelantamiento", "espacio", "prohibido", "dejar", "espacio"]),
    ("adelantamiento vehículos dos ruedas distancia", ["vehículos", "dos", "ruedas", "distancia", "1,5", "lateral"]),
    ("adelantamiento autobuses facilitar maniobra", ["autobuses", "facilitar", "maniobra", "paradas"]),
    ("adelantamiento túnel varios carriles permitido", ["túnel", "carriles", "varios", "permitido", "sentido"]),
    ("adelantamiento pasos peatones velocidad", ["pasos", "peatones", "velocidad", "reducida", "frenada"]),

    # LUCES DEL VEHÍCULO
    ("luces antiniebla niebla lluvia estrechas", ["antiniebla", "niebla", "lluvia", "estrechas", "curvas"]),
    ("luces posición estacionamiento travesía", ["posición", "estacionamiento", "travesía", "iluminada", "insuficientemente"]),
    ("luces rojas intermitentes cinco situaciones", ["rojas", "intermitentes", "bomberos", "puente", "aeronave"]),
    ("luces cruce carretera niebla uso", ["cruce", "carretera", "niebla", "uso", "prohibido"]),
    ("luces emergencia peligro señalización", ["emergencia", "peligro", "señalización", "v-16"]),

    # CAMBIO DE SENTIDO
    ("cambio sentido glorieta siempre permitido", ["glorieta", "cambio", "sentido", "vuelta", "completa"]),
    ("cambio sentido marcha atrás prohibida", ["marcha", "atrás", "prohibida", "reiniciar", "maniobra"]),
    ("cambio sentido cerca paso peatones prohibido", ["cambio", "sentido", "peatones", "próximidades", "prohibido"]),
    ("cambio sentido doble sentido borde izquierdo", ["doble", "sentido", "borde", "izquierdo", "ceñirse", "central"]),

    # VELOCIDADES
    ("velocidades máximas autopista autovía convencional", ["autopista", "autovía", "convencional", "urbana", "120", "100", "90", "50"]),
    ("velocidades remolque turismo autovía 90", ["remolque", "turismo", "autovía", "90", "ligero"]),
    ("velocidades carriles adicionales arcén 80", ["carril", "adicional", "arcén", "80", "60", "circunstancial"]),

    # CARRILES
    ("carriles reservados VAO no circulación", ["reservados", "vao", "circulación", "normal", "efectos"]),
    ("carriles sentido contrario obras fluidez", ["sentido", "contrario", "obras", "fluidez", "turismos", "motos"]),
    ("carriles velocidad obligatoria derecha", ["velocidad", "obligatoria", "derecha", "adelantar", "carril"]),
    ("carriles múltiples sentido único dirección", ["múltiples", "sentido", "único", "dirección", "adelantar"]),
    ("carriles autobús línea discontinua", ["autobús", "línea", "discontinua", "carril"]),

    # NEUMÁTICOS
    ("neumáticos mínimo legal 1.6 mm cambio", ["mínimo", "legal", "1,6", "mm", "cambio", "desgaste"]),
    ("neumáticos periodicidad 5 años goma endurecida", ["periodicidad", "5", "años", "goma", "endurecida", "10"]),
    ("neumáticos presión inflado fabricante recomendada", ["presión", "inflado", "fabricante", "recomendada", "máxima"]),
    ("neumáticos nieve adherencia marcas compactada", ["nieve", "adherencia", "marcas", "compactada", "virgen"]),

    # ITV
    ("ITV periodicidad primera segunda inspección", ["primera", "segunda", "inspección", "periodicidad", "4", "2", "anual"]),
    ("ITV distintivo posición ángulo superior", ["distintivo", "posición", "ángulo", "superior", "derecho"]),
    ("ITV remolques tarjeta inspección todos", ["remolques", "tarjeta", "inspección", "todos", "ligeros"]),

    # CARGA Y VEHÍCULO
    ("carga motocicleta lateral anchura sobresalencia", ["motocicleta", "lateral", "anchura", "sobresalencia", "0,25", "0,50"]),
    ("carga sobresaliente turismo detrás delante", ["sobresaliente", "turismo", "detrás", "delante", "10", "15"]),
    ("carga camión paneles esquinas detrás", ["camión", "paneles", "esquinas", "detrás", "amarillos", "rojas"]),
    ("carga motocicleta frontal trasera 0.50", ["motocicleta", "frontal", "trasera", "0,50", "metros"]),

    # SEGURIDAD
    ("seguridad cinturón exenciones distribuidores", ["cinturón", "exenciones", "distribuidores", "mercancías", "poblado"]),
    ("seguridad fumar vehículo privado permitido", ["fumar", "vehículo", "privado", "prohibido", "público", "distracción", "ley 28"]),
    ("seguridad auriculares inalámbricos moto prohibidos", ["auriculares", "inalámbricos", "prohibidos", "moto"]),
    ("seguridad movilidad reducida prohibido parar", ["movilidad", "reducida", "prohibido", "parar", "zonas"]),
    ("seguridad arcén prohibido siempre", ["arcén", "adelantar", "prohibido", "siempre", "nunca", "circular"]),

    # PREFERENCIA Y PASO
    ("preferencia estrechamientos prioridad orden", ["estrechamientos", "prioridad", "orden", "más", "largo", "subida"]),
    ("preferencia tracción animal vehículos estrechamientos", ["tracción", "animal", "vehículos", "estrechamientos", "preferencia"]),
    ("preferencia peatones fuera poblado izquierda", ["peatones", "fuera", "poblado", "izquierda", "sentido", "contrario"]),
    ("preferencia autobús incorporación facilitar", ["autobús", "incorporación", "facilitar", "prioridad", "maniobra"]),
    ("preferencia animales calzada maniobra giro", ["animales", "calzada", "maniobra", "giro", "dirección", "prioridad", "paso"]),

    # ALCOHOLEMIA Y DROGAS
    ("alcoholimia tasas sangre aire expirado", ["alcoholimia", "tasas", "sangre", "aire", "0,5", "0,25"]),
    ("alcoholimia novelas profesionales 0.15", ["novelas", "profesionales", "0,15", "0,3", "primer", "permiso"]),
    ("drogas presencia intoxicación tolerancia cero", ["drogas", "presencia", "intoxicación", "tolerancia", "cero"]),

    # PERMISOS Y LICENCIAS
    ("permisos B camiones furgonetas plazas", ["permiso", "b", "camiones", "furgonetas", "9", "plazas"]),
    ("permisos noviciado puntos pérdida máxima", ["noviciado", "puntos", "pérdida", "máxima", "8", "2", "años"]),
    ("permisos conductor habitual responsable titular", ["conductor", "habitual", "responsable", "titular", "notificaciones"]),

    # MOTOCICLETA
    ("moto carga lateral anchura menor 1 metro", ["moto", "carga", "lateral", "anchura", "menor", "1", "metro"]),
    ("moto remolque solo día visibilidad", ["remolque", "solo", "día", "visibilidad", "50", "masa"]),
    ("moto sidecar señales R-103 R-104", ["sidecar", "r-103", "r-104", "prohibido", "excepción"]),
    ("moto casco guantes calzado reforma 2026", ["casco", "guantes", "calzado", "reforma", "2026", "obligatorio"]),
    ("moto autoprotección espejo retrovisor 100", ["autoprotección", "espejo", "retrovisor", "100", "izquierdo", "exterior"]),

    # TÉCNICA Y MECÁNICA
    ("técnica revoluciones cambio marcha gasolina diésel", ["revoluciones", "cambio", "marcha", "gasolina", "diésel", "rpm"]),
    ("técnica humo motor negro azul blanco", ["humo", "motor", "negro", "azul", "blanco", "aceite", "agua"]),
    ("técnica servofreno asistencia freno", ["servofreno", "asistencia", "freno", "multiplica", "fuerza"]),

    # CONDICIONES ADVERSES
    ("condiciones niebla lluvia nieve sol viento", ["niebla", "lluvia", "nieve", "sol", "viento", "adversas"]),
    ("condiciones aquaplaning frenado emergencia", ["aquaplaning", "frenado", "emergencia", "soltar", "acelerador"]),
    ("condiciones túnel distancia seguridad 100m", ["túnel", "distancia", "seguridad", "100", "metros"]),

    # SEGURO Y DOCUMENTACIÓN
    ("seguro obligatorio exclusiones alcohol robo drogas", ["seguro", "obligatorio", "exclusiones", "alcohol", "robo", "drogas"]),
    ("seguro obligatorio daños terceros póliza", ["seguro", "daños", "terceros", "póliza", "cubre"]),

    # NORMATIVA 2026
    ("normativa reforma RGC zonas urbanas VMP", ["reforma", "rgc", "zonas", "urbanas", "vmp", "2026"]),
    ("normativa adelantamiento ciclistas 5 metros", ["adelantamiento", "ciclistas", "5", "metros", "1,5"]),

    # ESTACIONAMIENTO
    ("estacionamiento sentido único derecha izquierda", ["sentido", "único", "derecha", "izquierda", "urbana"]),
    ("estacionamiento prohibido parada diferencia", ["estacionamiento", "parada", "diferencia", "3", "minutos", "conductor"]),
    ("estacionamiento vado R-3h R-3g diagonal", ["vado", "r-3h", "r-3g", "diagonal", "cruces"]),

    # PARTES DE LA VÍA
    ("partes vía calzada arcén acera elementales", ["calzada", "arcén", "acera", "elementales", "partes"]),
    ("partes vía líneas amarillas continuas discontinuas", ["líneas", "amarillas", "continuas", "discontinuas", "parar", "estacionar"]),

    # PERSONAS Y VEHÍCULOS
    ("personas vehículos art 4 ciclomotor motor", ["vehículos", "motor", "ciclomotor", "art", "4", "personas"]),
    ("personas vehículos camión furgoneta diferencia", ["camión", "furgoneta", "diferencia", "chasis", "personas", "mercancía"]),

    # HERIDO Y ACCIDENTE
    ("herido accidente abrigar shock quemaduras", ["herido", "abrigar", "shock", "quemaduras", "golpe", "calor"]),
    ("herido accidente movilidad salir vía móvil", ["movilidad", "salir", "vía", "móvil", "accidente", "frecuente"]),

    # RECOLZAMENT I NETEJA
    ("neumáticos repuesto presión fabricante", ["repuesto", "presión", "fabricante", "máxima", "hinchar"]),
    ("neumáticos repuesto remolque obligatoria", ["repuesto", "remolque", "obligatoria", "ligero"]),

    # CARGA ESPECÍFICA
    ("carga sobresaliente delantera prohibida turismo", ["delantera", "delante", "prohibida", "turismo", "nunca", "0"]),
    ("carga motocicleta estrecha lateral 0.50", ["estrecha", "lateral", "0,50", "0,50", "anchura", "eje"]),

    # ADELANTAMIENTO ESPECÍFIC
    ("adelantar arcén prohibido siempre nunca", ["arcén", "adelantar", "prohibido", "siempre", "nunca"]),
    ("adelantamiento animales paso maniobra giro", ["animales", "maniobra", "giro", "dirección", "paso", "prioridad"]),

    # SEMÁFOROS ESPECÍFICS
    ("semáforo prioridad señales verticales manda", ["semáforo", "señales", "verticales", "prioridad", "manda", "funcionamiento"]),
    ("semáforo carril propio lado derecho obeceer", ["carril", "propio", "lado", "derecho", "obedecer", "dos", "colores"]),
    ("semáforo ceda paso prioridad verde manda", ["ceda", "paso", "verde", "prioridad", "manda", "señal"]),

    # SEÑALS ESPECÍFIQUES
    ("señal U-turn prohíbe giro izquierda no", ["u-turn", "giro", "izquierda", "prohíbe", "media", "volta"]),
    ("señal carril bici motos obligados dos ruedas", ["carril", "bici", "motos", "obligados", "dos", "ruedas"]),
    ("señal prohibido parar zonas movilidad reducida", ["parar", "prohibido", "movilidad", "reducida", "zonas", "exclusivo"]),
    ("señal velocidad intersección zona peligro aplica", ["velocidad", "intersección", "peligro", "aplica", "zona", "solo"]),

    # VEHÍCULES ESPECÍFICS
    ("vehículos movilidad reducida exentos prohibiciones", ["movilidad", "reducida", "exentos", "prohibiciones", "afectan"]),
    ("vehículos semáforos detienen cada obedece suyo", ["semáforos", "detienen", "cada", "obedece", "suyo", "intersección"]),

    # CARRIL ESPECÍFIC
    ("carril bici motos bicicletas obligados", ["carril", "bici", "motos", "bicicletas", "obligados"]),
    ("carril contradictorio obras fluidez permitidos", ["contradictorio", "obras", "fluidez", "permitidos", "vehículos"]),
]


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


def classify_error(error: dict) -> str:
    """Assigna un error al tema més específic de la taxonomia."""
    combined = f"{error['title']} {error['error']} {error['correction']}".lower()
    combined = re.sub(r"[^\w\s]", " ", combined)
    combined_words = set(combined.split())

    best_topic = "altres errors diversos"
    best_score = 0

    for topic_id, keywords in TOPICS:
        # Comptem matches: keyword completa o substring significatiu
        score = 0
        for kw in keywords:
            if kw in combined_words or kw in combined:
                # Keywords més llargues pesen més (són més específiques)
                weight = 2 if len(kw) >= 5 else 1
                score += weight
        if score > best_score:
            best_score = score
            best_topic = topic_id

    # Threshold: necessitem mínim 2 punts per classificar
    if best_score < 2:
        return "altres errors diversos"

    return best_topic


def compute_topic_scores(errors: list[dict]) -> dict:
    """Calcula puntuació per tema."""
    topic_counts = Counter()
    topic_errors = defaultdict(list)

    for error in errors:
        topic = classify_error(error)
        topic_counts[topic] += 1
        topic_errors[topic].append(error["num"])

    total = len(errors)
    scores = {}
    for topic, count in topic_counts.most_common():
        scores[topic] = {
            "count": count,
            "pct": round(count / total * 100, 1),
            "error_nums": topic_errors[topic],
        }
    return scores


def generate_report(errors: list[dict], scores: dict, top_n: int) -> str:
    """Genera l'informe complet."""
    total = len(errors)

    lines = []
    lines.append("=" * 65)
    lines.append("  ORACLE DEL CARNET DE CONDUIR B")
    lines.append(f"  {total} errors registrats")
    lines.append("=" * 65)
    lines.append("")
    lines.append("  RANKING PER TEMA ESPECÍFIC")
    lines.append("  " + "─" * 50)
    lines.append("")

    rank = 0
    for topic, data in scores.items():
        if rank >= top_n:
            break
        rank += 1
        pct = data["pct"]
        barra = "█" * max(1, int(pct))
        lines.append(f"  #{rank:2d}  {topic}")
        lines.append(f"       {data['count']:2d} errors ({pct:4.1f}%)  {barra}")
        lines.append(f"       errors: {', '.join(str(n) for n in data['error_nums'])}")
        lines.append("")

    # Resum ràpid
    lines.append("=" * 65)
    lines.append("  RECOMANACIÓ PRE-TEST")
    lines.append("  " + "─" * 50)
    lines.append("")

    top3 = list(scores.items())[:3]
    if top3:
        lines.append("  Revisa AQUESTS 3 temes abans del proper test:")
        for i, (topic, data) in enumerate(top3, 1):
            lines.append(f"  {i}. {topic.upper()} ({data['count']} errors)")
        lines.append("")
        top3_pct = sum(d["count"] for _, d in top3) / total * 100
        lines.append(f"  Si dominés aquests 3, reduiries errors ~{top3_pct:.0f}%.")

    lines.append("")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Oracle del carnet de conduir B")
    parser.add_argument("--moc", default=None)
    parser.add_argument("--top", type=int, default=20)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    moc_path = Path(args.moc) if args.moc else Path(__file__).parent / "Cotxe" / "_MOC.md"
    if not moc_path.exists():
        print(f"Error: {moc_path} no existeix", file=sys.stderr)
        sys.exit(1)

    errors = parse_moc(moc_path)
    if not errors:
        print("Error: sense errors al MOC", file=sys.stderr)
        sys.exit(1)

    scores = compute_topic_scores(errors)

    if args.json:
        out = {
            "total_errors": len(errors),
            "topics": {k: {"count": v["count"], "pct": v["pct"], "error_nums": v["error_nums"]} for k, v in scores.items()}
        }
        print(json_mod.dumps(out, indent=2, ensure_ascii=False))
    else:
        print(generate_report(errors, scores, args.top))


if __name__ == "__main__":
    main()
