"""Servidor MCP del BCRP. Empiecen aquí: buscar_series ya funciona; completen los TODO hasta que pasen las pruebas.

    uv run pytest                                           # el contrato: las 8 pruebas deben pasar
    uv run mcp/server.py                                    # el servidor, por stdio (desde la raíz de Tarea_4)
    .mcp.json                                               # ya lo conecta a Claude Code

Las cuentas las hace Python, no el modelo: así cada cifra sale de una llamada que se puede repetir.
"""
import re
import time
import unicodedata
from functools import cache
from pathlib import Path

import httpx
import pandas as pd
from fastmcp import FastMCP
from fastmcp.exceptions import ToolError

AQUI = Path(__file__).parent
CATALOGO = AQUI.parent / "datos" / "catalogo_bcrp.csv"   # datos/ en la raíz de Tarea_4
URL_CATALOGO = "https://estadisticas.bcrp.gob.pe/estadisticas/series/metadata"
API = "https://estadisticas.bcrp.gob.pe/estadisticas/series/api"
SOLO_LECTURA = {"readOnlyHint": True, "openWorldHint": True}

mcp = FastMCP("bcrp", instructions=(
    "Series oficiales del Banco Central de Reserva del Perú (BCRP). Primero busca el código con buscar_series; "
    "luego usa resumen para variaciones, promedios y extremos, y serie para los datos. Para datos por departamento "
    "(inversión pública, crédito, depósitos, exportaciones mineras) usa cuadre_territorial: trae los 25 departamentos "
    "con su ubigeo y verifica que sumen el total oficial. No calcules a mano: "
    "cita siempre el código de la serie y el periodo."))


def _sin_tildes(s):
    return unicodedata.normalize("NFD", str(s).lower()).encode("ascii", "ignore").decode()


@cache
def catalogo():
    """El catálogo oficial: 17 mil series en unos 7 MB. Se baja una vez y queda en datos/."""
    if not CATALOGO.exists():
        CATALOGO.parent.mkdir(exist_ok=True)
        r = httpx.get(URL_CATALOGO, timeout=120)
        r.raise_for_status()
        CATALOGO.write_text(r.content.decode("latin-1"), encoding="utf-8")
    df = pd.read_csv(CATALOGO, sep=";", dtype=str).fillna("")
    df = df.rename(columns={"Código de serie": "codigo", "Categoría de serie": "categoria", "Grupo de serie": "grupo",
                            "Nombre de serie": "nombre", "Frecuencia": "frecuencia",
                            "Fecha de actualización": "actualizada", "Fecha de inicio": "inicio"})
    df["texto"] = (df.categoria + " " + df.grupo + " " + df.nombre).map(_sin_tildes)
    return df


def _ficha(codigo):
    fila = catalogo().query("codigo == @codigo")
    if fila.empty:
        raise ToolError(f"No existe el código de serie {codigo!r}. Búsquenlo con buscar_series.")
    f = fila.iloc[0]
    return {"codigo": f.codigo, "nombre": f"{f.grupo} - {f.nombre}", "categoria": f.categoria,
            "frecuencia": f.frecuencia, "inicio": f.inicio, "actualizada": f.actualizada}


@mcp.tool(annotations=SOLO_LECTURA)
def buscar_series(texto: str, frecuencia: str | None = None, limite: int = 10) -> list[dict]:
    """Busca series del BCRP por palabras: todas deben aparecer en la categoría, el grupo o el nombre.

    Ejemplos: "ipc 12 meses", "tipo de cambio interbancario venta", "reservas internacionales netas",
    "tasa de referencia", "cobre precio". frecuencia: "Diaria", "Mensual", "Trimestral" o "Anual".
    Devuelve el código, el nombre completo, la frecuencia y desde cuándo hay datos. Si no hay resultados,
    prueben con menos palabras.
    """
    df = catalogo()
    m = pd.Series(True, index=df.index)
    for palabra in _sin_tildes(texto).split():
        m &= df.texto.str.contains(re.escape(palabra))
    if frecuencia:
        m &= df.frecuencia.str.lower() == frecuencia.lower()
    # primero las series vigentes y, entre ellas, las de nombre más corto (las más generales)
    sel = df[m]
    orden = sel.assign(vieja=sel.actualizada < "2025", largo=(sel.grupo + sel.nombre).str.len())
    return [_ficha(c) for c in orden.sort_values(["vieja", "largo"]).head(limite).codigo]


MESES = {"ene": 1, "feb": 2, "mar": 3, "abr": 4, "may": 5, "jun": 6,
         "jul": 7, "ago": 8, "set": 9, "sep": 9, "oct": 10, "nov": 11, "dic": 12}


def _fecha_api(fecha, frecuencia, fin):
    """Pasa "2025-01", "2025-01-15", "2025-T1" o "2025" al formato que pide la API según la frecuencia."""
    partes = str(fecha).replace("T", "").split("-")
    anio = partes[0]
    if frecuencia == "Anual":
        return anio
    if frecuencia == "Diaria":
        if len(partes) == 3:
            return str(fecha)
        mes = partes[1] if len(partes) > 1 else ("12" if fin else "01")
        dia = str(pd.Period(f"{anio}-{mes}", "M").days_in_month) if fin else "01"
        return f"{anio}-{mes}-{dia}"
    tope = "4" if frecuencia == "Trimestral" else "12"
    return f"{anio}-{int(partes[1]) if len(partes) > 1 else (tope if fin else 1)}"


def _periodo(nombre, frecuencia):
    """Pasa "Ene.2025", "01.Oct.26", "T1.25" o "2025" a "2025-01", "2026-10-01", "2025-T1" o "2025"."""
    if frecuencia == "Anual":
        return nombre
    if frecuencia == "Trimestral":
        t, anio = nombre.split(".")
        return f"20{anio[-2:]}-{t}"
    if frecuencia == "Diaria":
        dia, mes, anio = nombre.split(".")
        return f"20{anio[-2:]}-{MESES[mes.lower()[:3]]:02d}-{int(dia):02d}"
    mes, anio = nombre.split(".")
    return f"{anio}-{MESES[mes.lower()[:3]]:02d}"


@cache
def _descargar(url):
    """Pide la URL a la API; si responde HTML (demasiados pedidos seguidos), espera y reintenta. Queda en caché."""
    for intento in range(4):
        try:
            r = httpx.get(url, timeout=30)
            return tuple(r.json()["periods"])
        except (ValueError, KeyError, httpx.HTTPError):
            time.sleep(2 * (intento + 1))
    raise ToolError(f"El BCRP no respondió con datos para {url}. Esperen unos segundos y reintenten.")


def _serie(codigo, desde, hasta):
    ficha = _ficha(codigo)
    frec = ficha["frecuencia"]
    url = f"{API}/{codigo}/json/{_fecha_api(desde, frec, False)}/{_fecha_api(hasta, frec, True)}"
    datos = [{"periodo": _periodo(p["name"], frec), "valor": float(p["values"][0])}
             for p in _descargar(url) if p["values"][0] not in ("n.d.", "")]
    if not datos:
        raise ToolError(f"La serie {codigo} no tiene datos entre {desde} y {hasta}. Hay datos desde {ficha['inicio']}.")
    return {"codigo": codigo, "nombre": ficha["nombre"], "frecuencia": frec, "datos": datos, "fuente": url}


@mcp.tool(annotations=SOLO_LECTURA)
def serie(codigo: str, desde: str, hasta: str) -> dict:
    """Datos de una serie del BCRP entre dos fechas, ambas incluidas, con la URL de la fuente.

    Fechas: "2025-01" (mensual), "2026-10-01" (diaria), "2025-T1" (trimestral), "2025" (anual).
    Ejemplo: serie("PN01271PM", "2025-01", "2025-12"). Si no saben el código, usen antes buscar_series.
    Para variaciones, promedios o extremos usen resumen en vez de calcular a mano.
    """
    return _serie(codigo, desde, hasta)


@mcp.tool(annotations=SOLO_LECTURA)
def resumen(codigo: str, desde: str, hasta: str) -> dict:
    """Resumen de una serie del BCRP entre dos fechas: primero, último, cambio, variación %, promedio,
    máximo y mínimo (con su periodo), y la URL de la fuente.

    Úsenla para cualquier pregunta de «cuánto subió», «cuál fue el máximo» o «el valor en tal mes», en vez de
    calcular a mano. Mismas fechas que serie. Ejemplo: resumen("PN01273PM", "2025-12", "2026-09").
    """
    s = _serie(codigo, desde, hasta)
    df = pd.DataFrame(s["datos"])
    primero, ultimo = s["datos"][0], s["datos"][-1]
    cambio = ultimo["valor"] - primero["valor"]
    return {"codigo": codigo, "nombre": s["nombre"], "frecuencia": s["frecuencia"], "n": len(df),
            "primero": primero, "ultimo": ultimo, "cambio": round(cambio, 4),
            "variacion_pct": round(100 * cambio / primero["valor"], 2) if primero["valor"] else None,
            "promedio": round(df.valor.mean(), 4),
            "maximo": df.loc[df.valor.idxmax()].to_dict(), "minimo": df.loc[df.valor.idxmin()].to_dict(),
            "fuente": s["fuente"]}

REFERENCIA, INFLACION = "PD04722MM", "PN01273PM"   # tasa de referencia y var% 12 meses del IPC de Lima


@mcp.tool(annotations=SOLO_LECTURA)
def tasa_real(desde: str, hasta: str, neutral: float = 2.0) -> dict:
    """Tasa de interés real del BCRP mes a mes y la postura de la política monetaria: restrictiva, neutral o expansiva.

    Úsenla para preguntas como «¿la política del BCRP fue restrictiva en 2023?», «¿cuándo la tasa real fue
    negativa?» o «¿cuál es la tasa real hoy?». Cruza la tasa de referencia (PD04722MM) con la inflación a
    12 meses de Lima (PN01273PM): tasa real = referencia − inflación (ex post). La postura compara la tasa real
    con una tasa neutral (por defecto 2 %): más de 0.5 puntos por encima es restrictiva, más de 0.5 por debajo
    es expansiva. Fechas mensuales: tasa_real("2021-01", "2026-09").
    """
    ref, inf = _serie(REFERENCIA, desde, hasta), _serie(INFLACION, desde, hasta)
    df = pd.DataFrame(ref["datos"]).merge(pd.DataFrame(inf["datos"]), on="periodo", suffixes=("_ref", "_inf"))
    if df.empty:
        raise ToolError(f"No hay meses con tasa de referencia e inflación a la vez entre {desde} y {hasta}.")
    df = df.rename(columns={"valor_ref": "referencia", "valor_inf": "inflacion"})
    df["tasa_real"] = (df.referencia - df.inflacion).round(2)
    df["postura"] = pd.cut(df.tasa_real - neutral, [-float("inf"), -0.5, 0.5, float("inf")],
                           labels=["expansiva", "neutral", "restrictiva"]).astype(str)
    df["inflacion"] = df.inflacion.round(2)
    # rachas: tramos seguidos con la misma postura
    tramo = (df.postura != df.postura.shift()).cumsum()
    rachas = [{"postura": g.postura.iloc[0], "desde": g.periodo.iloc[0], "hasta": g.periodo.iloc[-1], "meses": len(g)}
              for _, g in df.groupby(tramo)]
    return {"desde": df.periodo.iloc[0], "hasta": df.periodo.iloc[-1], "neutral": neutral,
            "ultimo": df.iloc[-1].to_dict(),
            "meses_por_postura": df.postura.value_counts().to_dict(),
            "meses_con_tasa_real_negativa": int((df.tasa_real < 0).sum()),
            "tasa_real_minima": df.loc[df.tasa_real.idxmin(), ["periodo", "tasa_real"]].to_dict(),
            "tasa_real_maxima": df.loc[df.tasa_real.idxmax(), ["periodo", "tasa_real"]].to_dict(),
            "rachas": rachas, "meses": df.to_dict("records"),
            "fuentes": [ref["fuente"], inf["fuente"]]}


# Códigos de departamento del INEI (los dos primeros dígitos del ubigeo), con Lima y Callao separados.
UBIGEO = {"amazonas": "01", "ancash": "02", "apurimac": "03", "arequipa": "04", "ayacucho": "05", "cajamarca": "06",
          "callao": "07", "cusco": "08", "huancavelica": "09", "huanuco": "10", "ica": "11", "junin": "12",
          "la libertad": "13", "lambayeque": "14", "lima": "15", "loreto": "16", "madre de dios": "17",
          "moquegua": "18", "pasco": "19", "piura": "20", "puno": "21", "san martin": "22", "tacna": "23",
          "tumbes": "24", "ucayali": "25"}

# Cada indicador: dónde están sus series anuales en el catálogo y cuál es el total oficial con el que cuadrar.
INDICADORES = {
    "inversion_gobierno_nacional": {
        "grupo": "Inversión bruta fija del gobierno nacional por departamentos (millones S/)", "unidad": "millones S/"},
    "inversion_gobiernos_regionales": {
        "grupo": "Inversión bruta fija de los gobiernos regionales (millones S/)", "unidad": "millones S/"},
    "inversion_gobiernos_locales": {
        "grupo": "Inversión bruta fija de gobiernos locales por departamentos (millones S/)", "unidad": "millones S/"},
    "credito": {"grupo": "Crédito directo del sistema financiero al sector privado por departamentos - fin de periodo "
                         "(millones S/)", "solo": "(total)", "unidad": "millones S/, fin de periodo"},
    "depositos": {"grupo": "Depósitos en el sistema financiero por departamentos - fin de periodo (millones S/)",
                  "solo": "(total)", "unidad": "millones S/, fin de periodo"},
    "exportaciones_mineras": {"grupo_empieza": "Exportaciones por grupo de productos ",   # «de X» y «sin ubigeo»
                              "nombre": "Productos tradicionales - Mineros", "total": "PM40047BA",
                              "unidad": "millones US$ FOB"},
}


def _depto(texto):
    """'Huánuco (millones de soles)' o 'Exportaciones por grupo de productos de Huanuco (...)' -> 'huanuco'."""
    t = _sin_tildes(re.sub(r"\(.*?\)", "", texto))
    return re.sub(r"^exportaciones por grupo de productos (de )?", "", t.strip()).strip()


def _series_del_indicador(indicador):
    """Las series anuales del indicador, cada una marcada como departamento, total u otra (p. ej., Lima Metropolitana)."""
    if indicador not in INDICADORES:
        raise ToolError(f"Indicador {indicador!r} no disponible. Usen uno de: {', '.join(INDICADORES)}.")
    cfg, df = INDICADORES[indicador], catalogo()
    df = df[df.frecuencia == "Anual"]
    if "grupo" in cfg:
        sel = df[df.grupo == cfg["grupo"]]
        if "solo" in cfg:
            sel = sel[sel.nombre.str.strip().str.endswith(cfg["solo"])]
        etiqueta = sel.nombre
    else:
        sel = df[df.grupo.str.startswith(cfg["grupo_empieza"]) & (df.nombre == cfg["nombre"])]
        etiqueta = sel.grupo
    filas = []
    for codigo, texto in zip(sel.codigo, etiqueta):
        d = _depto(texto)
        tipo = "total" if d == "total" else ("departamento" if d in UBIGEO else "otra")
        nombre = re.sub(r"\s*\(.*?\)\s*", " ", texto).strip()
        nombre = re.sub(r"^Exportaciones por grupo de productos (de )?", "", nombre)
        filas.append({"codigo": codigo, "nombre": nombre, "tipo": tipo, "ubigeo": UBIGEO.get(d)})
    if "total" in cfg:
        filas.append({"codigo": cfg["total"], "nombre": "Total nacional", "tipo": "total", "ubigeo": None})
    return cfg, filas


@mcp.tool(annotations={"readOnlyHint": False, "destructiveHint": False, "openWorldHint": True})
def cuadre_territorial(indicador: str, desde: str, hasta: str, guardar: bool = False) -> dict:
    """Valores anuales por departamento de un indicador del BCRP, con su código de ubigeo, y el cuadre contra el total oficial.

    Úsenla para preguntas como «¿cuánto invirtieron los gobiernos regionales en cada departamento en 2024?» o
    «¿la suma de los departamentos coincide con el total nacional?». Devuelve los 25 departamentos (Lima y Callao
    separados) con la llave ubigeo de dos dígitos del INEI, lista para unir con la ENAHO, y para cada año: suma de
    departamentos, total oficial, diferencia y las series que no son departamentos (como la Municipalidad
    Metropolitana de Lima) que la explican. Si faltan años, lo dice en vez de rellenar.

    Con guardar=True escribe además salidas/bcrp_<indicador>_<desde>_<hasta>.csv (una fila por serie y año, con su
    código y URL de la fuente), que es lo que lee la skill analizando-reparto para cruzar con la ENAHO.

    Indicadores: inversion_gobierno_nacional, inversion_gobiernos_regionales, inversion_gobiernos_locales,
    credito, depositos, exportaciones_mineras. Años: cuadre_territorial("inversion_gobiernos_regionales", "2020", "2024").
    """
    cfg, filas = _series_del_indicador(indicador)
    datos, fuentes = {}, []
    for f in filas:
        try:
            s = _serie(f["codigo"], desde, hasta)
        except ToolError:
            ficha = _ficha(f["codigo"])
            todo = _serie(f["codigo"], ficha["inicio"], hasta)["datos"]
            raise ToolError(f"{indicador}: la serie {f['codigo']} ({f['nombre']}) no tiene datos entre {desde} y "
                            f"{hasta}; su último año publicado es {todo[-1]['periodo']}. Usen años hasta ese.") from None
        datos[f["codigo"]] = {d["periodo"]: d["valor"] for d in s["datos"]}
        fuentes.append(s["fuente"])
        f["fuente"] = s["fuente"]
    periodos = sorted({p for v in datos.values() for p in v})
    deptos = [f for f in filas if f["tipo"] == "departamento"]
    faltan = sorted(set(UBIGEO.values()) - {f["ubigeo"] for f in deptos})
    total = next((f for f in filas if f["tipo"] == "total"), None)
    cuadre = []
    for p in periodos:
        suma = sum(datos[f["codigo"]].get(p, 0.0) for f in deptos)
        otras = [{"codigo": f["codigo"], "nombre": f["nombre"], "valor": round(datos[f["codigo"]].get(p, 0.0), 4)}
                 for f in filas if f["tipo"] == "otra"]
        oficial = datos[total["codigo"]].get(p) if total else None
        dif = None if oficial is None else oficial - suma
        resto = None if dif is None else dif - sum(o["valor"] for o in otras)
        tol = None if oficial is None else max(0.05, abs(oficial) * 1e-4)   # 0.01 % o 0.05: solo redondeo
        cuadre.append({"periodo": p, "suma_departamentos": round(suma, 4), "total_oficial": oficial,
                       "diferencia": None if dif is None else round(dif, 4), "otras_series": otras,
                       "diferencia_sin_explicar": None if resto is None else round(resto, 4),
                       "cuadra": None if resto is None else abs(resto) <= tol})
    archivo = None
    if guardar:
        archivo = AQUI.parent / "salidas" / f"bcrp_{indicador}_{desde}_{hasta}.csv"
        archivo.parent.mkdir(exist_ok=True)
        pd.DataFrame([{"indicador": indicador, "tipo": f["tipo"], "ubigeo": f["ubigeo"], "nombre": f["nombre"],
                       "codigo": f["codigo"], "anio": p, "valor": v, "unidad": cfg["unidad"], "fuente": f["fuente"]}
                      for f in filas for p, v in datos[f["codigo"]].items()]).to_csv(archivo, index=False)
        archivo = str(archivo.relative_to(AQUI.parent)).replace("\\", "/")
    return {"indicador": indicador, "unidad": cfg["unidad"], "desde": periodos[0], "hasta": periodos[-1],
            "archivo": archivo,
            "departamentos": [{"ubigeo": f["ubigeo"], "departamento": f["nombre"], "codigo": f["codigo"],
                               "valores": {p: round(v, 4) for p, v in datos[f["codigo"]].items()}}
                              for f in sorted(deptos, key=lambda f: f["ubigeo"])],
            "departamentos_faltantes": faltan, "cuadre": cuadre,
            "cuadra_todo": all(c["cuadra"] for c in cuadre if c["cuadra"] is not None),
            # si no cuadra, comparar fechas: un total actualizado después que los departamentos puede traer revisiones
            "actualizacion": {"total": _ficha(total["codigo"])["actualizada"] if total else None,
                              "departamentos": sorted({_ficha(f["codigo"])["actualizada"] for f in deptos})},
            "fuentes": fuentes}


@mcp.resource("bcrp://serie/{codigo}")
def ficha(codigo: str) -> dict:
    """Ficha de una serie del BCRP: nombre, categoría, frecuencia, desde cuándo hay datos y última actualización."""
    return _ficha(codigo)


@mcp.prompt
def postura_monetaria(desde: str, hasta: str) -> str:
    """Informe de la postura monetaria del BCRP en un periodo, con la tasa real y cifras verificables."""
    return (f"Usa la herramienta tasa_real del servidor bcrp entre {desde} y {hasta} y escribe un informe breve en "
            "español: (1) la tasa real y la postura del último mes, (2) los tramos restrictivos, neutrales y "
            "expansivos con sus fechas, (3) los meses con tasa real negativa y (4) la tasa real mínima y máxima. "
            "No calcules a mano: cada cifra debe salir de la herramienta y citar el código de la serie "
            "(PD04722MM o PN01273PM) y el periodo. Termina con las URLs de las fuentes.")


@mcp.prompt
def informe(tema: str) -> str:
    """Informe de cinco viñetas sobre un tema con series del BCRP, cada cifra con su código y periodo."""
    return (f"Escribe un informe de cinco viñetas sobre «{tema}» en el Perú con datos del BCRP. Busca las series con "
            "buscar_series y usa resumen o serie para las cifras; no calcules a mano. Cada viñeta debe citar el "
            "código de la serie y el periodo, y al final lista las URLs de las fuentes.")


if __name__ == "__main__":
    mcp.run()
