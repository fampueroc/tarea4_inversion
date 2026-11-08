"""Convierte las conversaciones de Claude Code (.jsonl) a Markdown legible, ocultando datos personales.

    uv run evidencias_ia/exportar_conversaciones.py

Qué oculta:
- Cualquier correo electrónico y el usuario de Windows de quien lo ejecuta, en rutas (C:\\Users\\<usuario>, C--Users-<usuario>-...).
- Los recordatorios internos del sistema (<system-reminder>): traen notas de memoria y del entorno, no forman parte
  del diálogo. Se reemplazan por una marca.
- El razonamiento interno del modelo (bloques de «thinking»), que no se muestra en la conversación.
- Las lecturas y ediciones de las notas de memoria de Claude (perfil, horarios y preferencias de la autora) y su
  resultado, y el nombre de su lugar de trabajo.
Qué recorta: los resultados de herramientas muy largos (se indica cuántos caracteres se omitieron).
Al final verifica que no quede ningún dato personal en los archivos generados; si queda, se detiene.

También limpia en su lugar los registros de la evaluación (evaluacion/logs/*.jsonl).
"""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
RAIZ = Path(__file__).resolve().parent.parent
PROYECTOS = Path.home() / ".claude" / "projects"
CORREO = re.compile(r"[\w.+\\-]+@[\w\\-]+\\?\.[\w.\\-]+")   # cualquier correo, también escrito con «\.» (no se escribe el de la autora)
USUARIO = re.compile(r"(?<![A-Za-z])" + re.escape(Path.home().name) + r"(?![A-Za-z])", re.I)   # usuario de Windows, leído del sistema
RESTO_CORREO = re.compile(r"[\w.+\-]*\[correo\](?:@[\w.\-\\]*|[\w.+\-]+)?")
PROMPT_MCP = re.compile(r"<command-name>(?P<nombre>/mcp__[\w-]+)</command-name>\s*<command-args>(?P<args>.*?)</command-args>", re.S)
RECORDATORIO = re.compile(r"<system-reminder>.*?</system-reminder>", re.S)
ORGANIZACION = re.compile(r"[organización]|\bIPA\b|[organización]")   # «[organización]» solo como sigla
MEMORIA = re.compile(r"[\\/]memory[\\/]|MEMORY\.md|originSessionId|node_type: memory|[nota omitida]|[nota omitida]|Diplomado PUCP\. Trab", re.I)   # notas de memoria de Claude
LIMITE = 2500
OMITIDOS = set()   # ids de llamadas que tocan la memoria, para omitir también su resultado

SESIONES = [  # (carpeta del proyecto, id de sesión, archivo de salida, título)
    ("C--Users-{u}-Documents-GitHub-Data-Science-Python", "05211c51-4bd6-4700-b1c0-95eadba03178",
     "mcp/01_desarrollo_mcp_bcrp_sesion04.md", "Desarrollo del servidor MCP del BCRP (ejercicio de la sesión 04, 28-oct-2026)"),
    ("C--Users-{u}-Documents-GitHub-mcp-bcrp", "44379eac-435e-4c70-a879-a922770b1268",
     "mcp/02_prueba_mcp_en_claude_code.md", "Prueba del MCP desde Claude Code (28-oct-2026)"),
    ("C--Users-{u}-Documents-GitHub-Python-Interm-Tareas-Tarea-4", "288b6482-a668-4558-85d4-ed6833fd096e",
     "mcp/03_prompt_y_recurso.md", "Prompt informe y recurso bcrp://serie/RD16682DA del MCP desde Claude Code (8-nov-2026)"),
    ("C--Users-{u}-Documents-GitHub-Data-Science-Python", "b521c8f1-adac-42bd-8d75-9d9720577812",
     "skills/01_desarrollo_skills_enaho_sesion16.md", "Desarrollo de las skills de la ENAHO (ejercicio de la sesión 16, 31-oct-2026)"),
    ("C--Users-{u}-Documents-GitHub-Python-Interm-Tareas-Tarea-4", "1bb110e2-4f4e-4827-909e-21b1901164f9",
     "integracion/intento1_conversacion.md", "Ejecución integrada, intento 1 (6-nov-2026)"),
    ("C--Users-{u}-Documents-GitHub-Python-Interm-Tareas-Tarea-4", "ff4b3efb-1caf-4214-8fff-c882108a2032",
     "integracion/intento2_conversacion.md", "Ejecución integrada, intento 2 (6/7-nov-2026)"),
    ("C--Users-{u}-Documents-GitHub-Data-Science-Python", "731e3686-e8f6-4969-a16d-1b34e470beee",
     "00_conversacion_principal_tarea4.md", "Conversación principal de la Tarea 4: plan, MCP, skills, análisis, evaluación e informe (3 al 7-nov-2026)"),
]


FRAGMENTO = re.compile(r"\w*ampuero\d+\w*", re.I)   # parte del correo antes de la @, sin escribir sus dígitos


def limpiar(s):
    s = RECORDATORIO.sub("[recordatorio interno del sistema omitido]", s)
    s = CORREO.sub("[correo]", s)          # primero el correo completo
    s = FRAGMENTO.sub("[correo]", s)       # luego, fragmentos sueltos
    s = RESTO_CORREO.sub("[correo]", s)    # y lo que quede pegado a un reemplazo (inicial, dominio)
    s = ORGANIZACION.sub("[organización]", s)
    return USUARIO.sub("[usuario]", s)


def recortar(s):
    return s if len(s) <= LIMITE else s[:LIMITE] + f"\n… [{len(s) - LIMITE} caracteres más omitidos]"


def texto_de(contenido):
    """Une los bloques de texto de un mensaje; devuelve (texto, herramientas usadas, resultados)."""
    if isinstance(contenido, str):
        return contenido, [], []
    textos, usos, resultados = [], [], []
    for b in contenido:
        tipo = b.get("type")
        if tipo == "text":
            textos.append(b["text"])
        elif tipo == "tool_use":
            entrada = json.dumps(b.get("input", {}), ensure_ascii=False)
            if MEMORIA.search(entrada):            # lectura o edición de la memoria de Claude: se omite
                OMITIDOS.add(b.get("id"))
                usos.append((b["name"], "[acceso a las notas de memoria de Claude omitido]"))
            else:
                usos.append((b["name"], entrada))
        elif tipo == "tool_result":
            if b.get("tool_use_id") in OMITIDOS or MEMORIA.search(json.dumps(b.get("content"), ensure_ascii=False)):
                resultados.append("[resultado omitido: notas de memoria de Claude]")
                continue
            c = b.get("content")
            if isinstance(c, list):
                c = "\n".join(x.get("text", "[imagen omitida]") if isinstance(x, dict) else str(x) for x in c)
            resultados.append(str(c or ""))
    return "\n".join(textos), usos, resultados


def exportar(origen, destino, titulo):
    lineas = [f"# {titulo}", "",
              "*Exportado de Claude Code. Datos personales reemplazados por [correo] y [usuario]; recordatorios internos "
              "del sistema y razonamiento interno omitidos; resultados largos de herramientas recortados.*", ""]
    n_usuaria = n_claude = n_herr = 0
    prompt_mcp_pendiente = False
    for linea in origen.read_text(encoding="utf-8").splitlines():
        try:
            e = json.loads(linea)
        except json.JSONDecodeError:
            continue
        hora = (e.get("timestamp") or "")[:16].replace("T", " ")
        contenido = e.get("message", {}).get("content", "")
        # Prompt de un servidor MCP invocado con «/mcp__servidor__prompt»: se muestra el comando y el texto que
        # devuelve el servidor (Claude Code lo guarda como mensaje interno justo después del comando).
        comando = PROMPT_MCP.search(contenido) if isinstance(contenido, str) else None
        if e.get("type") == "user" and comando:
            n_usuaria += 1
            lineas += [f"## 👤 Usuaria · {hora} UTC", "", limpiar(f"{comando['nombre']} {comando['args']}").strip(), ""]
            prompt_mcp_pendiente = True
            continue
        if e.get("isMeta") and e.get("type") == "user" and prompt_mcp_pendiente:
            prompt_mcp_pendiente = False
            texto = texto_de(contenido)[0]
            lineas += ["<details open><summary>Texto que devuelve el prompt del servidor MCP</summary>", "",
                       "```text", limpiar(texto).strip().replace("```", "ʼʼʼ"), "```", "</details>", ""]
            continue
        prompt_mcp_pendiente = False if e.get("type") == "assistant" else prompt_mcp_pendiente
        if e.get("type") not in ("user", "assistant") or e.get("isMeta"):
            continue
        if e.get("isCompactSummary"):  # resumen automático al compactar el contexto: repite notas internas
            lineas += [f"*[{(e.get('timestamp') or '')[:16].replace('T', ' ')}] Resumen automático del contexto "
                       "(compactación de Claude Code) omitido; la conversación sigue a continuación.*", ""]
            continue
        texto, usos, resultados = texto_de(e.get("message", {}).get("content", ""))
        hora = (e.get("timestamp") or "")[:16].replace("T", " ")
        if e["type"] == "user":
            for r in resultados:
                lineas += ["<details><summary>Resultado de la herramienta</summary>", "", "```text",
                           recortar(limpiar(r)).replace("```", "ʼʼʼ"), "```", "</details>", ""]
            if texto.strip() and not texto.startswith("<command-") and not texto.startswith("<local-command"):
                t = limpiar(texto).strip()
                if t and t != "[recordatorio interno del sistema omitido]":
                    n_usuaria += 1
                    lineas += [f"## 👤 Usuaria · {hora} UTC", "", t, ""]
        else:
            if texto.strip():
                n_claude += 1
                lineas += [f"### 🤖 Claude · {hora} UTC", "", limpiar(texto).strip(), ""]
            for nombre, entrada in usos:
                n_herr += 1
                lineas += [f"> 🔧 **{nombre}** `{recortar(limpiar(entrada)).replace('`', 'ʼ')}`", ""]
    escribir_en_partes(destino, lineas)
    return n_usuaria, n_claude, n_herr


def escribir_en_partes(destino, lineas, maximo=400_000):
    """Escribe el Markdown; si pasa de ~400 KB lo divide en partes que empiezan en un mensaje de la usuaria."""
    destino.parent.mkdir(parents=True, exist_ok=True)
    for viejo in destino.parent.glob(destino.stem + "_parte*.md"):
        viejo.unlink()
    texto = "\n".join(lineas) + "\n"
    if len(texto.encode("utf-8")) <= maximo:
        destino.write_text(texto, encoding="utf-8")
        return
    partes, actual, tam = [], [], 0
    for l in lineas:
        if l.startswith("## 👤") and tam > maximo * 0.9:
            partes.append(actual)
            actual, tam = [], 0
        actual.append(l)
        tam += len(l.encode("utf-8")) + 1
    partes.append(actual)
    n = len(partes)
    for i, parte in enumerate(partes, 1):
        cab = [] if i == 1 else [f"{lineas[0]} (parte {i} de {n})", ""]
        pie = ["", f"*Continúa en [{destino.stem}_parte{i + 1}.md]({destino.stem}_parte{i + 1}.md).*"] if i < n else []
        (destino.parent / f"{destino.stem}_parte{i}.md").write_text("\n".join(cab + parte + pie) + "\n", encoding="utf-8")
    indice = [lineas[0], "", f"La conversación es larga y está dividida en {n} partes:", ""]
    indice += [f"- [Parte {i}]({destino.stem}_parte{i}.md)" for i in range(1, n + 1)]
    destino.write_text("\n".join(indice) + "\n", encoding="utf-8")


def exportar_evaluacion():
    """Los registros de evaluacion/logs/ como Markdown legible, un archivo por modo, en evidencias_ia/evaluacion/."""
    import csv
    global PREGUNTAS
    PREGUNTAS = {}
    for archivo in ("preguntas.csv", "robustez.csv"):
        with open(RAIZ / "evaluacion" / archivo, encoding="utf-8") as f:
            PREGUNTAS.update({r["id"]: r["pregunta"] for r in csv.DictReader(f)})
    logs_dir = RAIZ / "evaluacion" / "logs"
    grupos = {"A": "modo_A_sin_mcp_ni_skills", "B": "modo_B_con_mcp_y_skills",
              "M": "modo_M_solo_memoria_intento_fallido"}
    for modo, nombre in grupos.items():
        lineas = [f"# Sesiones de evaluación: {nombre.replace('_', ' ')}", "",
                  "*Cada sección es una sesión independiente de `claude -p` (`evaluacion/evaluar.py`), con las mismas "
                  "reglas de privacidad que el resto de las evidencias. Registro original en `evaluacion/logs/`.*", ""]
        for log in sorted(logs_dir.glob(f"*_{modo}.jsonl")):
            tmp = RAIZ / "evidencias_ia" / "evaluacion" / "_tmp.md"
            exportar(log, tmp, "")
            cuerpo = tmp.read_text(encoding="utf-8").splitlines()[4:]
            tmp.unlink()
            pid = log.stem.split("_")[0]
            texto_p = PREGUNTAS.get(pid, "")
            lineas += ["---", "", f"## Pregunta {pid} · modo {modo}", "", f"> **Pregunta:** {texto_p}", ""]
            lineas += [l.replace("## 👤 Usuaria", "### 👤 Pregunta enviada").replace("### 🤖 Claude", "#### 🤖 Claude")
                       for l in cuerpo]
        escribir_en_partes(RAIZ / "evidencias_ia" / "evaluacion" / f"{nombre}.md", lineas)
        print(f"evaluacion/{nombre}.md")


def main():
    usuario = Path.home().name
    for carpeta, sesion, salida, titulo in SESIONES:
        origen = PROYECTOS / carpeta.format(u=usuario) / f"{sesion}.jsonl"
        if not origen.exists():
            print(f"FALTA {origen.name}: no se exporta {salida}")
            continue
        n = exportar(origen, RAIZ / "evidencias_ia" / salida, titulo)
        print(f"{salida}: {n[0]} mensajes de la usuaria, {n[1]} de Claude, {n[2]} usos de herramientas")
    # Registros de la evaluación: misma limpieza, en su lugar
    for log in sorted((RAIZ / "evaluacion" / "logs").glob("*.jsonl")):
        log.write_text(limpiar(log.read_text(encoding="utf-8")), encoding="utf-8")
    exportar_evaluacion()
    # Verificación final: ningún dato personal en lo que se va a publicar
    # En los registros de la evaluación la ruta «...\memory\» es la carpeta vacía de cada copia temporal: ahí se
    # buscan solo datos personales; en las conversaciones exportadas, además, cualquier rastro de las notas de memoria.
    PEGADO = re.compile(r"[\w.+\-]\[correo\]|\[correo\][@\w]")  # restos de correo junto a un reemplazo
    md = list((RAIZ / "evidencias_ia").rglob("*.md"))
    logs = list((RAIZ / "evaluacion").rglob("*.jsonl"))
    revisar = md + logs
    malos = [str(p.relative_to(RAIZ)) for p in revisar
             if any(rx.search(p.read_text(encoding="utf-8"))
                    for rx in ((CORREO, FRAGMENTO, USUARIO, ORGANIZACION, MEMORIA, PEGADO) if p in md
                               else (CORREO, FRAGMENTO, USUARIO, ORGANIZACION, PEGADO)))]
    if malos:
        sys.exit("ERROR: quedan datos personales en " + ", ".join(malos))
    print(f"Verificado: sin correo, usuario de Windows, organización ni notas de memoria en {len(revisar)} archivos.")


if __name__ == "__main__":
    main()
