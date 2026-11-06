"""Califica evaluacion/corridas.csv contra las tolerancias de evaluacion/preguntas.csv (fijadas antes de correr).

    uv run evaluacion/calificar.py

Revisa la línea «RESPUESTA FINAL» de cada sesión (si falta, toda la respuesta). En C1 y C2 la parte numérica es
automática; la interpretación (sin causalidad) se marca para revisión humana en la columna revision_humana.
Sale: evaluacion/resultados.csv
"""
import csv
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
NUM = re.compile(r"\d{1,3}(?:[   ]\d{3})+(?:[.,]\d+)?|\d+(?:[.,]\d+)?")


def numeros(texto):
    """'1 061,2', '25 109,33', '4.40', '7,36 %' -> floats. Interpreta la coma como decimal."""
    out = []
    for m in NUM.findall(texto):
        s = re.sub(r"[   ]", "", m).replace(",", ".")
        try:
            out.append(float(s))
        except ValueError:
            pass
    return out


def hay(texto, lo, hi):
    return any(lo <= x <= hi for x in numeros(texto))


def sin_causalidad(texto):
    """Heurística para la revisión humana: ¿niega causalidad o se declara descriptiva?"""
    t = texto.lower()
    return bool(re.search(r"no (prueba|permite|demuestra|implica|establece|mide)[^.]*causal|descriptiv|no causal", t))


CHEQUEOS = {  # id -> (función sobre el texto final, descripción); rangos de preguntas.csv
    "B1": (lambda t: hay(t, 1050.6, 1071.8), "1050.6–1071.8"),
    "B2": (lambda t: hay(t, 24858.2, 25360.4), "24858.2–25360.4"),
    "B3": (lambda t: "2022" in t and hay(t, 1278.5, 1304.3), "2022 y 1278.5–1304.3"),
    "B4": (lambda t: hay(t, 5324.1, 5431.7), "5324.1–5431.7"),
    "E1": (lambda t: hay(t, 44.9, 45.1), "44.9–45.1"),
    "E2": (lambda t: hay(t, 27.5, 27.7), "27.5–27.7"),
    "E3": (lambda t: hay(t, 39.2, 39.4), "39.2–39.4"),
    "E4": (lambda t: hay(t, 26.5, 26.7) and hay(t, 28.5, 28.7), "26.5–26.7 y 28.5–28.7"),
    "C1": (lambda t: hay(t, 4.30, 4.50) and hay(t, 7.16, 7.56) and "menor" in t.lower(), "4.30–4.50, 7.16–7.56 y «menor»"),
    "C2": (lambda t: all(d in t for d in ["Cajamarca", "Loreto", "Puno", "Pasco", "Huánuco"])
           and hay(t, 24.0, 24.6) and hay(t, 15.4, 16.0), "5 departamentos, 24.0–24.6 y 15.4–16.0"),
}


def fuente(herr):
    f = []
    if "mcp__bcrp" in herr:
        f.append("MCP bcrp (API del BCRP)")
    if "Skill:" in herr:
        f.append("skills: " + ", ".join(sorted({h.split(":")[1] for h in herr.split(" | ") if h.startswith("Skill:")})))
    if not f and "Bash" in herr:
        f.append("Bash: API del BCRP con curl y/o microdatos de la ENAHO procesados por Claude")
    return "; ".join(f) or "sin herramientas"


def main():
    preguntas = {r["id"]: r for r in csv.DictReader(open(RAIZ / "evaluacion" / "preguntas.csv", encoding="utf-8"))}
    filas = []
    for r in csv.DictReader(open(RAIZ / "evaluacion" / "corridas.csv", encoding="utf-8")):
        lineas = [l for l in r["respuesta"].splitlines() if "RESPUESTA FINAL" in l.upper()]
        final = lineas[-1] if lineas else r["respuesta"]
        ok_num = bool(r["respuesta"]) and CHEQUEOS[r["id"]][0](final)
        revision = ""
        correcta = ok_num
        if r["id"] in ("C1", "C2"):
            causal_ok = sin_causalidad(r["respuesta"]) or r["id"] == "C1"
            revision = ("pendiente: confirmar que no afirma causalidad"
                        + ("" if causal_ok else " (la heurística no encontró una negación explícita)"))
            correcta = ok_num and causal_ok
        p = preguntas[r["id"]]
        filas.append({"id": r["id"], "tipo": r["tipo"], "modo": r["modo"], "pregunta": p["pregunta"],
                      "respuesta_esperada": p["respuesta_esperada"], "tolerancia": p["tolerancia"],
                      "respuesta_generada": final.strip(), "fuente_utilizada": fuente(r["herramientas"]),
                      "herramientas": r["herramientas"], "uso_mcp": r["uso_mcp"], "uso_skills": r["uso_skills"],
                      "correcta": correcta, "chequeo_automatico": CHEQUEOS[r["id"]][1], "revision_humana": revision,
                      "segundos": r["segundos"], "turnos": r["turnos"], "costo_usd": r["costo_usd"],
                      "error": r["error"] or ("sin respuesta" if not r["respuesta"] else ""), "log": r["log"]})
    filas.sort(key=lambda f: (f["modo"], list(preguntas).index(f["id"])))
    with open(RAIZ / "evaluacion" / "resultados.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(filas[0]))
        w.writeheader()
        w.writerows(filas)
    for modo in sorted({f["modo"] for f in filas}):
        m = [f for f in filas if f["modo"] == modo]
        seg = sum(float(f["segundos"]) for f in m) / len(m)
        print(f"Modo {modo}: {sum(f['correcta'] for f in m)}/{len(m)} correctas, {seg:.1f} s en promedio; "
              f"incorrectas: {[f['id'] for f in m if not f['correcta']]}")
    print("Guardado: evaluacion/resultados.csv")


if __name__ == "__main__":
    main()
