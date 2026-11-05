"""¿La inversión pública 2020–2024 se reparte entre departamentos según dónde vive la población pobre?

Cruza la inversión del BCRP (archivos que guarda la herramienta MCP cuadre_territorial) con la pobreza de la
ENAHO 2024 (base de limpiando-enaho). Todo es descriptivo: compara repartos, no mide efectos.

Uso (desde la raíz de Tarea_4):
    uv run .claude/skills/analizando-reparto/scripts/analizar.py

Entra:  salidas/personas_2024.parquet
        salidas/bcrp_inversion_gobierno_nacional_2020_2024.csv  (y _gobiernos_regionales_, _gobiernos_locales_)
        salidas/bcrp_exportaciones_mineras_2018_2022.csv
        datos/peru_departamental_simple.geojson
Sale:   salidas/indicadores.csv, salidas/recuadro_lima.csv, salidas/analisis.txt
        figuras/bcrp_inversion_anual.png, figuras/inversion_vs_pobres.png,
        figuras/curva_concentracion.png, figuras/densidad_inversion.png
Si una validación falla, se detiene sin guardar resultados.
"""
import sys
import textwrap
from pathlib import Path

import geopandas as gpd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sys.stdout.reconfigure(encoding="utf-8")
AQUI = Path(__file__).resolve().parent
REF_INEI = AQUI.parent / "referencias" / "inei_pobreza_2024.csv"
LLAVES = ["conglome", "vivienda", "hogar"]
NIVELES = {"inversion_gobierno_nacional": "Gobierno nacional",
           "inversion_gobiernos_regionales": "Gobiernos regionales",
           "inversion_gobiernos_locales": "Gobiernos locales"}
ANIOS = ("2020", "2024")
DEPARTAMENTOS = {
    "01": "Amazonas", "02": "Áncash", "03": "Apurímac", "04": "Arequipa", "05": "Ayacucho",
    "06": "Cajamarca", "07": "Callao", "08": "Cusco", "09": "Huancavelica", "10": "Huánuco",
    "11": "Ica", "12": "Junín", "13": "La Libertad", "14": "Lambayeque", "15": "Lima",
    "16": "Loreto", "17": "Madre de Dios", "18": "Moquegua", "19": "Pasco", "20": "Piura",
    "21": "Puno", "22": "San Martín", "23": "Tacna", "24": "Tumbes", "25": "Ucayali",
}
# Paleta validada (skill dataviz): una serie en azul; categorías en orden fijo azul, naranja, aguamarina
AZUL, NARANJA, AGUA = "#2a78d6", "#eb6834", "#1baf7a"
TINTA, TINTA_SUAVE, GRIS = "#0b0b0b", "#52514e", "#c3c2b7"
FUENTE_BCRP = "BCRP, inversión bruta fija por departamentos (series RD, anuales)"
FUENTE_ENAHO = "INEI, ENAHO 2024 (sumaria y módulo 02), ponderado con factor07 × mieperho"
lineas = []


def informar(texto=""):
    print(texto)
    lineas.append(texto)


def detener(msg):
    sys.exit(f"ERROR: {msg}\nNo se guardaron resultados.")


# ---------------------------------------------------------------- estimación con el diseño de la ENAHO
def _varianza(z, h):
    """Varianza de un total linealizado: conglomerados con reemplazo dentro de estratos (departamento × estrato)."""
    g = pd.DataFrame({"z": z, "s": h.estrato_diseno, "c": h.conglome}).groupby(["s", "c"]).z.sum().reset_index()
    return sum(len(t) / (len(t) - 1) * ((t.z - t.z.mean()) ** 2).sum() for _, t in g.groupby("s") if len(t) > 1)


def tasa(h, en):
    """Tasa de pobreza (%) de un dominio y su error estándar."""
    W = h.w[en].sum()
    p = h.w[en & h.pobre].sum() / W
    return 100 * p, 100 * np.sqrt(_varianza(np.where(en, h.w * (h.pobre - p) / W, 0.0), h))


def participacion(h, en, de=None):
    """Parte (%) de la población pobre (o de `de`) que vive en un dominio, y su error estándar."""
    y = h.w * (h.pobre if de is None else de)
    R = y[en].sum() / y.sum()
    return 100 * R, 100 * np.sqrt(_varianza((y * en - R * y) / y.sum(), h))


def indice_concentracion(orden, x, y):
    """Índice de concentración de y, con unidades ordenadas de mayor a menor pobreza y pesadas por x (población).
    Negativo: y se concentra en los departamentos más pobres; positivo: en los menos pobres."""
    cx = np.r_[0, (x[orden] / x.sum()).cumsum().values]
    cy = np.r_[0, (y[orden] / y.sum()).cumsum().values]
    return 1 - np.sum(np.diff(cx) * (cy[1:] + cy[:-1])), cx, cy


# ---------------------------------------------------------------- figuras
def _estilo(ax):
    for lado in ("top", "right"):
        ax.spines[lado].set_visible(False)
    for lado in ("left", "bottom"):
        ax.spines[lado].set_color(GRIS)
    ax.tick_params(colors=TINTA_SUAVE, length=0)


def _guardar(fig, destino, titulo, subtitulo, pie):
    """Título, subtítulo y fuente a distancias fijas en pulgadas, con el texto partido para que nunca se corte."""
    ancho, alto = fig.get_size_inches()
    cols = int(ancho * 11.5)
    titulo = textwrap.fill(titulo, int(ancho * 8.2))
    subtitulo, pie = textwrap.fill(subtitulo, cols), textwrap.fill(pie, int(ancho * 14))
    n_tit, n_sub, n_pie = (len(s.splitlines()) for s in (titulo, subtitulo, pie))
    fig.text(0.02, 1 - 0.15 / alto, titulo, ha="left", va="top", fontsize=13, fontweight="bold", color=TINTA)
    y_sub = 1 - (0.25 + 0.24 * n_tit) / alto
    fig.text(0.02, y_sub, subtitulo, ha="left", va="top", fontsize=9.5, color=TINTA_SUAVE)
    arriba = y_sub - (0.2 * n_sub + 0.15) / alto
    fig.text(0.02, 0.1 / alto, pie, ha="left", va="bottom", fontsize=7.5, color=TINTA_SUAVE)
    fig.tight_layout(rect=(0, (0.2 + 0.14 * n_pie) / alto, 1, arriba))
    destino.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(destino, dpi=200, facecolor="white")
    plt.close(fig)


def fig_bcrp_anual(inv_anual, destino):
    fig, ax = plt.subplots(figsize=(8, 5))
    base = np.zeros(len(inv_anual))
    anios = inv_anual.index.tolist()
    for (nivel, nombre), color in zip(NIVELES.items(), (AZUL, NARANJA, AGUA)):
        v = inv_anual[nivel].values / 1000
        ax.bar(anios, v, bottom=base, color=color, width=0.62, label=nombre, edgecolor="white", linewidth=2)
        base += v
    for x, tot in zip(anios, base):
        ax.text(x, tot + 0.8, f"{tot:,.1f}".replace(",", "X").replace(".", ",").replace("X", "."),
                ha="center", color=TINTA, fontsize=10)
    ax.set_ylabel("Miles de millones de soles corrientes", color=TINTA_SUAVE)
    ax.set_ylim(0, base.max() * 1.15)
    ax.grid(axis="y", color=GRIS, linewidth=0.5, alpha=0.6)
    ax.set_axisbelow(True)
    _estilo(ax)
    ax.legend(frameon=False, loc="upper left", fontsize=9, labelcolor=TINTA)
    _guardar(fig, destino, "La inversión pública pasó de 30,4 a 57,9 mil millones de soles entre 2020 y 2024",
             "Inversión bruta fija por nivel de gobierno, Perú (miles de millones de soles corrientes)",
             f"Fuente: {FUENTE_BCRP}. Incluye la Municipalidad Metropolitana de Lima en gobiernos regionales.")


def fig_ratio(t, destino):
    t = t.sort_values("pobreza_pct")
    fig, ax = plt.subplots(figsize=(8, 8.5))
    y = np.arange(len(t))
    ax.axvline(1, color=TINTA_SUAVE, linestyle=(0, (3, 3)), linewidth=1, zorder=1)
    ax.errorbar(t.inversion_vs_pobres, y, xerr=[t.inversion_vs_pobres - t.ratio_ic_inf, t.ratio_ic_sup - t.inversion_vs_pobres],
                fmt="o", color=AZUL, ecolor=AZUL, elinewidth=1.5, markersize=6, capsize=0, zorder=3)
    ax.set_yticks(y, [f"{n} ({p:.1f} %)" for n, p in zip(t.nombre, t.pobreza_pct)], fontsize=9, color=TINTA)
    ax.set_xscale("log", base=2)
    ax.set_xticks([0.5, 1, 2, 4, 8], ["0,5", "1", "2", "4", "8"])
    ax.set_xlabel("% de la inversión 2020–2024 ÷ % de la población pobre 2024 (escala logarítmica)", color=TINTA_SUAVE)
    ax.text(1.04, len(t) - 0.4, "1 = recibe la misma parte de inversión\nque su parte de pobres", fontsize=8,
            color=TINTA_SUAVE, va="top")
    ax.grid(axis="x", color=GRIS, linewidth=0.5, alpha=0.6)
    _estilo(ax)
    _guardar(fig, destino, "5 de los 6 departamentos más pobres reciben una parte de la inversión menor que su parte de pobres",
             "Departamentos ordenados por pobreza 2024 (entre paréntesis), de más pobre (arriba) a menos pobre; IC 95 %",
             f"Fuentes: {FUENTE_BCRP}; {FUENTE_ENAHO}. Intervalos por el error muestral de la ENAHO.")


def fig_concentracion(cx, c_inv, c_pob, ic_inv, ic_pob, destino):
    fig, ax = plt.subplots(figsize=(7, 6.5))
    ax.plot([0, 1], [0, 1], color=GRIS, linewidth=1.5, label="Reparto igual a la población")
    ax.plot(cx, c_pob, color=NARANJA, linewidth=2, marker="o", markersize=4, label=f"Población pobre (índice {ic_pob:+.3f})")
    ax.plot(cx, c_inv, color=AZUL, linewidth=2, marker="o", markersize=4, label=f"Inversión pública (índice {ic_inv:+.3f})")
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    ax.set_xlabel("Población acumulada, de los departamentos más pobres a los menos pobres", color=TINTA_SUAVE)
    ax.set_ylabel("Parte acumulada", color=TINTA_SUAVE)
    ax.xaxis.set_major_formatter(lambda v, _: f"{v:.0%}"); ax.yaxis.set_major_formatter(lambda v, _: f"{v:.0%}")
    ax.grid(color=GRIS, linewidth=0.5, alpha=0.6)
    _estilo(ax)
    ax.legend(frameon=False, loc="upper left", fontsize=9, labelcolor=TINTA)
    _guardar(fig, destino, "La inversión se reparte más como la población que como la pobreza",
             "Curvas de concentración: índice negativo = se concentra en los departamentos más pobres",
             f"Fuentes: {FUENTE_BCRP}, suma 2020–2024; {FUENTE_ENAHO}.")


def fig_densidad(t, b, destino):
    fig, ax = plt.subplots(figsize=(8, 6))
    sc = ax.scatter(t.densidad, t.inversion_por_hab, c=t.pobreza_pct, cmap="Blues", vmin=0, vmax=50, s=70,
                    edgecolor="white", linewidth=1.5, zorder=3)
    ax.set_xscale("log")
    for _, r in t.iterrows():
        if r.densidad < 4 or r.densidad > 300 or r.inversion_por_hab > 2700 or r.pobreza_pct > 39:
            ax.annotate(r.nombre, (r.densidad, r.inversion_por_hab), xytext=(6, 4), textcoords="offset points",
                        fontsize=8, color=TINTA)
    cb = fig.colorbar(sc, ax=ax, shrink=0.7)
    cb.set_label("Pobreza monetaria 2024 (% de personas)", color=TINTA_SUAVE)
    cb.outline.set_visible(False)
    ax.set_xlabel("Densidad: habitantes por km² (escala logarítmica)", color=TINTA_SUAVE)
    ax.set_ylabel("Soles corrientes por habitante al año", color=TINTA_SUAVE)
    ax.grid(color=GRIS, linewidth=0.5, alpha=0.6)
    _estilo(ax)
    _guardar(fig, destino, "La inversión por habitante es mayor donde hay menos densidad, no donde hay más pobreza",
             "Inversión pública por habitante (promedio 2020–2024) según densidad y pobreza de cada departamento",
             f"Fuentes: {FUENTE_BCRP}; {FUENTE_ENAHO}; superficie del GeoJSON departamental del curso.")


# ---------------------------------------------------------------- principal
def main():
    raiz = Path(".")
    base = raiz / "salidas" / "personas_2024.parquet"
    if not base.exists():
        detener(f"falta {base}. Usa primero la skill limpiando-enaho.")
    archivos = {n: raiz / "salidas" / f"bcrp_{n}_{ANIOS[0]}_{ANIOS[1]}.csv" for n in NIVELES}
    archivos["exportaciones_mineras"] = raiz / "salidas" / "bcrp_exportaciones_mineras_2018_2022.csv"
    faltan = [str(p) for p in archivos.values() if not p.exists()]
    if faltan:
        detener("faltan datos del BCRP: " + ", ".join(faltan) + ". Pídelos con la herramienta MCP "
                "cuadre_territorial(indicador, desde, hasta, guardar=True): los 3 niveles de inversión 2020–2024 y "
                "exportaciones_mineras 2018–2022.")

    # --- BCRP: verificar el cuadre de lo que guardó el MCP y armar la inversión por departamento
    informar("== Datos del BCRP (guardados por la herramienta MCP cuadre_territorial)")
    inv = []
    for nivel in NIVELES:
        d = pd.read_csv(archivos[nivel], dtype={"ubigeo": str, "anio": str})
        dep = d[d.tipo == "departamento"]
        if dep.ubigeo.nunique() != 25:
            detener(f"{nivel}: {dep.ubigeo.nunique()} departamentos en vez de 25.")
        for anio, g in d.groupby("anio"):
            total = g[g.tipo == "total"].valor.sum()
            suma = g[g.tipo.isin(["departamento", "otra"])].valor.sum()
            if abs(total - suma) > max(0.05, 1e-4 * total):
                detener(f"{nivel} {anio}: los departamentos suman {suma:,.1f} y el total oficial es {total:,.1f}.")
        otras = d[d.tipo == "otra"].assign(ubigeo="15")   # Municipalidad Metropolitana de Lima -> Lima
        inv.append(pd.concat([dep, otras]))
        informar(f"  {NIVELES[nivel]}: cuadra con el total oficial todos los años; series {d.codigo.nunique()}"
                 + (f"; {otras.nombre.iloc[0]} asignada a Lima" if len(otras) else ""))
    inv = pd.concat(inv)
    inv_anual = inv.groupby(["anio", "indicador"]).valor.sum().unstack()
    inv_depto = inv.groupby("ubigeo").valor.sum()
    informar(f"  Total 2020–2024: {inv_depto.sum():,.0f} millones S/ corrientes "
             f"({inv_anual.sum(axis=1).iloc[0]:,.0f} en 2020 y {inv_anual.sum(axis=1).iloc[-1]:,.0f} en 2024)")
    mina = pd.read_csv(archivos["exportaciones_mineras"], dtype={"ubigeo": str})
    exp_min = mina[mina.tipo == "departamento"].groupby("ubigeo").valor.mean()

    # --- ENAHO: hogares únicos, diseño muestral y validación contra el INEI
    informar("\n== ENAHO 2024: validación contra el INEI (Evolución de la Pobreza Monetaria 2015-2024, p. 220)")
    h = pd.read_parquet(base).drop_duplicates(LLAVES).copy()
    h["w"] = h.factor07.astype("float64") * h.mieperho
    h["estrato_diseno"] = h.departamento + "-" + h.estrato.astype(str)
    h["ambito"] = h.departamento.where(h.departamento != "15", np.where(h.ubigeo.str[:4] == "1501", "LM", "LP"))
    ref = pd.read_csv(REF_INEI, dtype={"ambito": str}).set_index("ambito")
    peor_p, razones = 0.0, []
    for a, r in ref.iterrows():
        en = pd.Series(True, index=h.index) if a == "PE" else h.ambito == a
        p, ee = tasa(h, en)
        peor_p = max(peor_p, abs(p - r.pobreza_pct))
        razones.append(1.96 * ee / ((r.ic95_superior - r.ic95_inferior) / 2))
    if peor_p > 0.1 or not 0.85 <= min(razones) <= max(razones) <= 1.15:
        detener(f"la ENAHO no reproduce al INEI: diferencia máx. {peor_p:.2f} puntos; "
                f"semiancho de los IC entre {min(razones):.2f} y {max(razones):.2f} veces el del INEI.")
    informar(f"  27 ámbitos (25 departamentos con Lima dividida en 2, y el nacional): diferencia máxima "
             f"{peor_p:.2f} puntos; semiancho del IC 95 % entre {min(razones):.2f} y {max(razones):.2f} veces el del INEI")

    # --- Indicadores por departamento
    geo = gpd.read_file(raiz / "datos" / "peru_departamental_simple.geojson")
    km2 = pd.Series((geo.HECTARES / 100).values, index=geo.FIRST_IDDP.astype(str))
    nombres = pd.Series(DEPARTAMENTOS)
    poblacion = h.groupby("departamento").w.sum()
    filas = []
    for u in sorted(inv_depto.index):
        en = h.departamento == u
        p, ee_p = tasa(h, en)
        s, ee_s = participacion(h, en)
        filas.append({"ubigeo": u, "nombre": nombres[u], "pobreza_pct": p, "pobreza_ic_inf": p - 1.96 * ee_p,
                      "pobreza_ic_sup": p + 1.96 * ee_p, "pct_pobres_pais": s, "pct_pobres_ic_inf": s - 1.96 * ee_s,
                      "pct_pobres_ic_sup": s + 1.96 * ee_s, "pct_poblacion": 100 * poblacion[u] / poblacion.sum()})
    t = pd.DataFrame(filas).set_index("ubigeo")
    t["pct_inversion"] = 100 * inv_depto / inv_depto.sum()
    for nivel in NIVELES:
        s = inv[inv.indicador == nivel].groupby("ubigeo").valor.sum()
        t[f"pct_{nivel}"] = 100 * s / s.sum()
    t["inversion_vs_pobres"] = t.pct_inversion / t.pct_pobres_pais
    t["ratio_ic_inf"] = t.pct_inversion / t.pct_pobres_ic_sup   # la inversión es un registro: solo varía el denominador
    t["ratio_ic_sup"] = t.pct_inversion / t.pct_pobres_ic_inf
    t["inversion_vs_poblacion"] = t.pct_inversion / t.pct_poblacion
    t["km2"] = km2
    t["densidad"] = poblacion / km2
    t["inversion_por_hab"] = 1e6 * inv_depto / poblacion / 5   # soles por habitante al año, promedio 2020–2024
    t["pct_exp_mineras_2018_2022"] = 100 * exp_min / exp_min.sum()

    # --- Hallazgo 1: reparto frente a pobres y frente a población
    informar("\n== Hallazgo 1: parte de la inversión frente a parte de los pobres y de la población")
    orden = t.sort_values("pobreza_pct", ascending=False)
    for u, r in orden.iterrows():
        informar(f"  {r.nombre:<14} pobreza {r.pobreza_pct:4.1f} % | pobres del país {r.pct_pobres_pais:5.2f} % "
                 f"[{r.pct_pobres_ic_inf:.2f}–{r.pct_pobres_ic_sup:.2f}] | inversión {r.pct_inversion:5.2f} % | "
                 f"inv/pobres {r.inversion_vs_pobres:4.2f} [{r.ratio_ic_inf:.2f}–{r.ratio_ic_sup:.2f}] | "
                 f"inv/población {r.inversion_vs_poblacion:4.2f}")
    cinco = orden.head(5)
    informar(f"  Los 5 departamentos más pobres ({', '.join(cinco.nombre)}): {cinco.pct_pobres_pais.sum():.1f} % de los "
             f"pobres, {cinco.pct_poblacion.sum():.1f} % de la población y {cinco.pct_inversion.sum():.1f} % de la inversión")
    debajo = t[t.ratio_ic_sup < 1]
    informar(f"  Con el IC 95 % entero por debajo de 1 (reciben menos que su parte de pobres): {len(debajo)} departamentos: "
             + ", ".join(debajo.sort_values("inversion_vs_pobres").nombre))

    # --- Hallazgo 2: índices de concentración
    informar("\n== Hallazgo 2: índices de concentración (orden: de mayor a menor pobreza; negativo = favorece a los más pobres)")
    o = orden.index
    ic_pob, cx, c_pob = indice_concentracion(o, poblacion, h[h.pobre].groupby("departamento").w.sum())
    ic_inv, _, c_inv = indice_concentracion(o, poblacion, inv_depto)
    informar(f"  Población pobre: {ic_pob:+.3f} | Inversión total: {ic_inv:+.3f}")
    for nivel, nombre in NIVELES.items():
        ic_n, _, _ = indice_concentracion(o, poblacion, inv[inv.indicador == nivel].groupby("ubigeo").valor.sum())
        t.loc[:, f"ic_{nivel}"] = ic_n
        informar(f"  {nombre}: {ic_n:+.3f}")

    # --- Hallazgo 3: densidad (regresión descriptiva con errores robustos HC1)
    informar("\n== Hallazgo 3: inversión por habitante según pobreza y densidad (25 departamentos, descriptivo)")
    X = np.column_stack([np.ones(len(t)), t.pobreza_pct, np.log(t.densidad)])
    y = np.log(t.inversion_por_hab.values)
    b = np.linalg.lstsq(X, y, rcond=None)[0]
    e = y - X @ b
    n, k = X.shape
    XtX = np.linalg.inv(X.T @ X)
    ee = np.sqrt(np.diag(n / (n - k) * XtX @ (X.T * e ** 2) @ X @ XtX))
    for nombre, bi, ei in [("pobreza (por punto)", b[1], ee[1]), ("log(densidad)", b[2], ee[2])]:
        informar(f"  {nombre}: {bi:+.4f} (EE robusto {ei:.4f}; IC 95 % {bi - 1.96 * ei:+.4f} a {bi + 1.96 * ei:+.4f})")
    informar(f"  R² = {1 - e.var() / y.var():.2f}. Lectura: con igual densidad, +1 punto de pobreza ≈ "
             f"{100 * (np.exp(b[1]) - 1):+.1f} % de inversión por habitante; duplicar la densidad ≈ "
             f"{100 * (2 ** b[2] - 1):+.1f} %.")

    # --- Complemento: minería (exportaciones 2018–2022, último año publicado por departamento)
    rho = t.inversion_vs_pobres.rank().corr(t.pct_exp_mineras_2018_2022.rank())
    informar(f"\n== Complemento: correlación de Spearman entre (inversión / pobres) y % de exportaciones mineras "
             f"2018–2022: {rho:.2f} (25 departamentos)")

    # --- Recuadro de Lima
    informar("\n== Recuadro: Lima Metropolitana y Lima provincias")
    rec = []
    for a, nombre in [("LM", "Lima Metropolitana (provincia de Lima)"), ("LP", "Lima provincias (región Lima)")]:
        en = h.ambito == a
        p, ee_p = tasa(h, en)
        s, ee_s = participacion(h, en)
        rec.append({"ambito": nombre, "pobreza_pct": p, "pobreza_ic_inf": p - 1.96 * ee_p, "pobreza_ic_sup": p + 1.96 * ee_p,
                    "pct_pobres_pais": s, "pct_pobres_ic_inf": s - 1.96 * ee_s, "pct_pobres_ic_sup": s + 1.96 * ee_s})
    reg = inv[inv.indicador == "inversion_gobiernos_regionales"]
    rec[0]["inversion_regional_2020_2024"] = reg[reg.tipo == "otra"].valor.sum()
    rec[1]["inversion_regional_2020_2024"] = reg[(reg.tipo == "departamento") & (reg.ubigeo == "15")].valor.sum()
    rec = pd.DataFrame(rec)
    for _, r in rec.iterrows():
        informar(f"  {r.ambito}: pobreza {r.pobreza_pct:.1f} % [{r.pobreza_ic_inf:.1f}–{r.pobreza_ic_sup:.1f}], "
                 f"{r.pct_pobres_pais:.1f} % de los pobres del país, inversión regional 2020–2024 "
                 f"{r.inversion_regional_2020_2024:,.0f} millones S/")
    informar("  La inversión del gobierno nacional y de los gobiernos locales en Lima no viene separada en el BCRP.")

    # --- Guardar
    salidas = raiz / "salidas"
    t.round(4).to_csv(salidas / "indicadores.csv", encoding="utf-8")
    rec.round(4).to_csv(salidas / "recuadro_lima.csv", index=False, encoding="utf-8")
    figuras = raiz / "figuras"
    fig_bcrp_anual(inv_anual, figuras / "bcrp_inversion_anual.png")
    fig_ratio(t, figuras / "inversion_vs_pobres.png")
    fig_concentracion(cx, c_inv, c_pob, ic_inv, ic_pob, figuras / "curva_concentracion.png")
    fig_densidad(t, b, figuras / "densidad_inversion.png")
    informar("\nGuardado: salidas/indicadores.csv, salidas/recuadro_lima.csv, salidas/analisis.txt y 4 figuras en figuras/")
    (salidas / "analisis.txt").write_text("\n".join(lineas) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
