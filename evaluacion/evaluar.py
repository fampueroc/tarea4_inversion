"""Corre las 10 preguntas de evaluacion/preguntas.csv en dos modos y guarda el registro de cada sesión.

    uv run evaluacion/evaluar.py                      # modos A y B, Sonnet, 4 sesiones a la vez
    uv run evaluacion/evaluar.py --ids B1 E2 --modos B
    uv run evaluacion/evaluar.py --preguntas robustez.csv --salida robustez_corridas.csv

Modo A: Claude Code sin el MCP ni las skills del proyecto (copia sin .claude/ ni .mcp.json, y Skill bloqueada).
Modo B: Claude Code con el servidor MCP bcrp y las skills de .claude/skills/.
Modo M (extra): solo memoria, sin ninguna herramienta, para ver la escalera completa.
En los dos: la misma instrucción, el mismo modelo, los mismos datos crudos (datos/), herramientas generales
(Bash, PowerShell, Read, Write, Edit, Glob, Grep), el mismo entorno de Python y SIN web (WebSearch y WebFetch bloqueadas). Cada pregunta corre
en su propia sesión (claude -p, sin persistencia) dentro de una copia limpia fuera del repositorio, que no lleva
salidas/, informes/ ni evaluacion/: nadie puede leer respuestas ya calculadas.

Sale: evaluacion/logs/<id>_<modo>.jsonl (registro completo) y evaluacion/corridas.csv (respuesta, herramientas,
tiempo). La corrección contra la respuesta esperada la hace evaluacion/calificar.py.
"""
import argparse
import csv
import json
import os
import shutil
import subprocess
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
LOGS = RAIZ / "evaluacion" / "logs"
GENERALES = ["Bash", "PowerShell", "Read", "Write", "Edit", "Glob", "Grep"]
INSTRUCCION = ("Responde en español a la siguiente pregunta sobre el Perú. Si necesitas datos, búscalos y calcula con "
               "las herramientas que tengas disponibles en esta carpeta; no inventes cifras. Si no puedes obtener un "
               "dato con certeza, dilo. Termina tu respuesta con una última línea que empiece con «RESPUESTA FINAL:» "
               "y contenga las cifras pedidas.\n\nPregunta: ")
# Las copias usan el entorno de Python ya instalado del proyecto (en los dos modos), para que el servidor MCP no
# tenga que instalar dependencias al arrancar; y Claude Code espera hasta 60 s a que el MCP conecte.
ENTORNO = {**os.environ, "UV_PROJECT_ENVIRONMENT": str(RAIZ / ".venv"), "MCP_TIMEOUT": "60000"}
COMUNES = ["datos", "pyproject.toml", "uv.lock", ".python-version"]
MODOS = {
    "A": {"copiar": COMUNES, "permitidas": GENERALES, "bloqueadas": ["Skill", "WebSearch", "WebFetch"], "mcp": False},
    "B": {"copiar": COMUNES + [".claude", "mcp", ".mcp.json"], "permitidas": GENERALES + ["Skill", "mcp__bcrp"],
          "bloqueadas": ["WebSearch", "WebFetch"], "mcp": True},
    # Modo M (extra): solo memoria. Sin ninguna herramienta (--tools "") y en una carpeta vacía.
    "M": {"copiar": [], "permitidas": [], "bloqueadas": [], "mcp": False},
}


def preparar_copia(modo):
    copia = Path(tempfile.mkdtemp(prefix=f"tarea4_modo{modo}_"))
    for nombre in MODOS[modo]["copiar"]:
        origen = RAIZ / nombre
        if origen.is_dir():
            shutil.copytree(origen, copia / nombre, ignore=shutil.ignore_patterns("__pycache__", ".pytest_cache", "test_*.py"))
        else:
            shutil.copy2(origen, copia / nombre)
    return copia


def correr(fila, modo, modelo, limite):
    copia = preparar_copia(modo)
    cfg = MODOS[modo]
    cmd = ["claude", "-p", INSTRUCCION + fila["pregunta"], "--model", modelo, "--output-format", "stream-json",
           "--verbose", "--no-session-persistence", "--strict-mcp-config"]
    if modo == "M":
        cmd += ["--tools", ""]
    else:
        cmd += ["--allowedTools", *cfg["permitidas"], "--disallowedTools", *cfg["bloqueadas"]]
    if cfg["mcp"]:
        cmd += ["--mcp-config", str(copia / ".mcp.json")]
    log = LOGS / f"{fila['id']}_{modo}.jsonl"
    inicio = time.time()
    try:
        with open(log, "w", encoding="utf-8") as f:
            proc = subprocess.run(cmd, cwd=copia, stdout=f, stderr=subprocess.PIPE, text=True, encoding="utf-8",
                                  timeout=limite, env=ENTORNO)
        error = proc.stderr.strip()[-300:] if proc.returncode else ""
    except subprocess.TimeoutExpired:
        error = f"tiempo agotado ({limite} s)"
    segundos = round(time.time() - inicio, 1)
    shutil.rmtree(copia, ignore_errors=True)
    return resumir(fila, modo, log, segundos, error)


def resumir(fila, modo, log, segundos, error):
    herramientas, respuesta, costo, turnos = [], "", None, None
    for linea in log.read_text(encoding="utf-8").splitlines():
        try:
            ev = json.loads(linea)
        except json.JSONDecodeError:
            continue
        if ev.get("type") == "assistant":
            for b in ev.get("message", {}).get("content", []):
                if b.get("type") == "tool_use":
                    nombre = b["name"]
                    if nombre == "Skill":
                        nombre += ":" + str(b.get("input", {}).get("skill", b.get("input", {}).get("command", "")))
                    herramientas.append(nombre)
        elif ev.get("type") == "result":
            respuesta = ev.get("result", "") or ""
            costo, turnos = ev.get("total_cost_usd"), ev.get("num_turns")
            if ev.get("is_error") and not error:
                error = str(ev.get("subtype", "error"))
    return {"id": fila["id"], "tipo": fila["tipo"], "modo": modo, "segundos": segundos, "turnos": turnos,
            "costo_usd": costo, "herramientas": " | ".join(herramientas),
            "uso_mcp": any(h.startswith("mcp__bcrp") for h in herramientas),
            "uso_skills": any(h.startswith("Skill:") for h in herramientas),
            "error": error, "respuesta": respuesta.strip(), "log": str(log.relative_to(RAIZ)).replace("\\", "/")}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--modos", nargs="+", default=["A", "B"], choices=list(MODOS))
    p.add_argument("--ids", nargs="*")
    p.add_argument("--modelo", default="sonnet")
    p.add_argument("--paralelo", type=int, default=4)
    p.add_argument("--limite", type=int, default=900, help="segundos máximos por sesión")
    p.add_argument("--preguntas", default="preguntas.csv", help="archivo dentro de evaluacion/ (p. ej. robustez.csv)")
    p.add_argument("--salida", default="corridas.csv", help="archivo de salida dentro de evaluacion/")
    a = p.parse_args()
    LOGS.mkdir(parents=True, exist_ok=True)
    with open(RAIZ / "evaluacion" / a.preguntas, encoding="utf-8") as f:
        preguntas = [r for r in csv.DictReader(f) if not a.ids or r["id"] in a.ids]
    casos = [(r, m) for m in a.modos for r in preguntas]
    print(f"{len(casos)} sesiones con {a.modelo}, {a.paralelo} a la vez...", flush=True)
    with ThreadPoolExecutor(a.paralelo) as ex:
        filas = list(ex.map(lambda c: correr(c[0], c[1], a.modelo, a.limite), casos))
    for r in filas:
        print(f"{r['id']} {r['modo']}: {r['segundos']} s, MCP={r['uso_mcp']}, skills={r['uso_skills']} {r['error']}")
    salida = RAIZ / "evaluacion" / a.salida
    previas = []
    if salida.exists():   # conserva corridas de otros ids/modos
        with open(salida, encoding="utf-8") as f:
            previas = [r for r in csv.DictReader(f) if (r["id"], r["modo"]) not in {(x["id"], x["modo"]) for x in filas}]
    with open(salida, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(filas[0]))
        w.writeheader()
        w.writerows(sorted(previas + filas, key=lambda r: (r["modo"], r["id"])))
    print(f"Guardado: {salida.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()
