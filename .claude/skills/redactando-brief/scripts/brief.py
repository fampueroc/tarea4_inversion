"""Policy brief de una página (PNG y PDF) con los hallazgos validados de analizando-reparto.

Uso (desde la raíz de Tarea_4):
    uv run .claude/skills/redactando-brief/scripts/brief.py

Entra:  salidas/indicadores.csv, salidas/recuadro_lima.csv, salidas/analisis.txt (de analizando-reparto)
Sale:   informes/policy_brief.png, informes/policy_brief.pdf
Todas las cifras se leen de esos archivos; ninguna se escribe a mano. Sigue filosofia.md.
"""
import re
import sys
import textwrap
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sys.stdout.reconfigure(encoding="utf-8")
AZUL, NARANJA = "#2a78d6", "#eb6834"          # paleta validada (skill dataviz), orden fijo
TINTA, SUAVE, GRIS, FONDO = "#0b0b0b", "#52514e", "#c3c2b7", "#fcfcfb"
ANCHO, ALTO = 8.27, 11.69                       # A4 vertical, en pulgadas
MARGEN = 0.6 / ANCHO


def detener(msg):
    sys.exit(f"ERROR: {msg}")


def coma(x, d=1):
    """Número con coma decimal, como se escribe en el Perú."""
    return f"{x:.{d}f}".replace(".", ",")


def leer():
    s = Path("salidas")
    faltan = [str(s / f) for f in ("indicadores.csv", "recuadro_lima.csv", "analisis.txt") if not (s / f).exists()]
    if faltan:
        detener("faltan " + ", ".join(faltan) + ". Usa primero la skill analizando-reparto.")
    t = pd.read_csv(s / "indicadores.csv", dtype={"ubigeo": str}).set_index("ubigeo")
    lima = pd.read_csv(s / "recuadro_lima.csv")
    txt = (s / "analisis.txt").read_text(encoding="utf-8")
    m = re.search(r"Población pobre: ([+-]\d\.\d+) \| Inversión total: ([+-]\d\.\d+)", txt)
    tot = re.search(r"Total 2020–2024: ([\d,]+) millones", txt)
    if not m or not tot or len(t) != 25:
        detener("salidas de analizando-reparto incompletas: vuelve a correr esa skill.")
    return t, lima, float(m.group(1)), float(m.group(2)), int(tot.group(1).replace(",", ""))


def texto(fig, x, y, s, size, peso="normal", color=TINTA, ancho=None, **kw):
    s = s.replace(" %", " %")   # el % nunca queda solo al inicio de una línea
    if ancho:
        s = textwrap.fill(s, ancho)
    return fig.text(x, y, s, fontsize=size, fontweight=peso, color=color, va="top", ha="left", **kw)


def main():
    t, lima, ic_pobres, ic_inv, inv_total = leer()
    orden = t.sort_values("pobreza_pct", ascending=False)
    top5 = orden.head(5)
    debajo = t[t.ratio_ic_sup < 1].sort_values("inversion_vs_pobres")
    lm = lima.iloc[0]
    caj = t.loc["06"]

    fig = plt.figure(figsize=(ANCHO, ALTO), facecolor=FONDO)
    x0 = MARGEN

    # Encabezado: la respuesta va en el título
    texto(fig, x0, 0.965, "POLICY BRIEF · INVERSIÓN PÚBLICA Y POBREZA · PERÚ 2020–2024", 8, "bold", SUAVE)
    texto(fig, x0, 0.945, "La inversión pública no se reparte según dónde viven los pobres", 19, "bold", ancho=44)
    total = f"{inv_total:,}".replace(",", " ")
    n_bajo = int((orden.head(10).ratio_ic_sup < 1).sum())
    texto(fig, x0, 0.868, f"Entre 2020 y 2024 el Estado invirtió S/ {total} millones (corrientes) en los 25 departamentos. "
          "Su reparto se parece al de la población total, no al de la población pobre: "
          f"{n_bajo} de los 10 departamentos más pobres reciben, con 95 % de confianza, menos de lo que les tocaría "
          "por su número de pobres.", 10.5, color=SUAVE, ancho=88)

    # Tres cifras grandes
    cifras = [
        (f"{coma(top5.pct_pobres_pais.sum())} %", f"{coma(top5.pct_inversion.sum())} %",
         f"de los pobres del país viven en los 5 departamentos más pobres ({', '.join(top5.nombre)}), "
         f"que recibieron el {coma(top5.pct_inversion.sum())} % de la inversión."),
        (f"{len(debajo)} de 25", None,
         f"departamentos reciben, con 95 % de confianza, menos inversión que su parte de pobres. "
         f"Cajamarca: {coma(caj.inversion_vs_pobres, 2)} por cada 1 que le correspondería."),
        (f"{coma(lm.pct_pobres_pais)} %", None,
         f"de los pobres del país vive en Lima Metropolitana (pobreza {coma(lm.pobreza_pct)} %). "
         f"El BCRP no separa su inversión nacional ni local del resto de Lima."),
    ]
    y = 0.785
    col = (1 - 2 * MARGEN) / 3
    for i, (grande, _, desc) in enumerate(cifras):
        xi = x0 + i * col
        fig.add_artist(plt.Line2D([xi, xi + col - 0.03], [y + 0.008, y + 0.008], transform=fig.transFigure,
                                  color=TINTA, linewidth=1.2))
        texto(fig, xi, y, grande, 26, "bold", NARANJA if i == 0 else TINTA)
        texto(fig, xi, y - 0.045, desc, 8.6, color=SUAVE, ancho=31)

    # Un solo gráfico: parte de pobres vs parte de inversión, 10 departamentos más pobres
    diez = orden.head(10).iloc[::-1]
    ax = fig.add_axes([x0 + 0.17, 0.295, 1 - 2 * MARGEN - 0.2, 0.275], facecolor=FONDO)
    yy = np.arange(len(diez))
    h = 0.38
    ax.barh(yy + h / 2, diez.pct_pobres_pais, h, color=NARANJA, label="% de los pobres del país (ENAHO 2024)")
    ax.barh(yy - h / 2, diez.pct_inversion, h, color=AZUL, label="% de la inversión pública 2020–2024 (BCRP)")
    for yi, (p, v) in enumerate(zip(diez.pct_pobres_pais, diez.pct_inversion)):
        ax.text(p + 0.1, yi + h / 2, coma(p), va="center", fontsize=7.5, color=TINTA)
        ax.text(v + 0.1, yi - h / 2, coma(v), va="center", fontsize=7.5, color=TINTA)
    ax.set_yticks(yy, [f"{n}  ({coma(p)} %)" for n, p in zip(diez.nombre, diez.pobreza_pct)], fontsize=8.5, color=TINTA)
    ax.set_xlim(0, max(diez.pct_pobres_pais.max(), diez.pct_inversion.max()) * 1.18)
    ax.xaxis.set_visible(False)
    for lado in ("top", "right", "bottom"):
        ax.spines[lado].set_visible(False)
    ax.spines["left"].set_color(GRIS)
    ax.tick_params(axis="y", length=0)
    fig.legend(*ax.get_legend_handles_labels(), frameon=False, fontsize=8, ncol=2, labelcolor=TINTA,
               loc="upper left", bbox_to_anchor=(x0 - 0.008, 0.598))
    texto(fig, x0, 0.655, "Los 10 departamentos más pobres: parte de pobres y parte de inversión", 11, "bold")
    li = t.loc["15"]
    texto(fig, x0, 0.632, f"Entre paréntesis, la tasa de pobreza 2024. Lima (pobreza {coma(li.pobreza_pct)} %) no está entre "
          f"los 10: reúne el {coma(li.pct_pobres_pais)} % de los pobres y recibió el {coma(li.pct_inversion)} % de la "
          "inversión.", 8.5, color=SUAVE, ancho=100)

    # Lectura y límite
    y2 = 0.255
    texto(fig, x0, y2, "Cómo leerlo", 11, "bold")
    texto(fig, x0, y2 - 0.022,
          f"Si la inversión siguiera a la pobreza, la barra azul igualaría a la naranja. El índice de concentración de "
          f"la inversión es {coma(ic_inv, 3)} (cercano a 0: reparto como la población); el de los pobres, "
          f"{coma(ic_pobres, 3).replace('-', '−')} (concentrados en los departamentos más pobres). Es una comparación descriptiva: "
          "no mide si la inversión reduce la pobreza ni juzga la eficiencia de ningún gobierno. El reparto puede "
          "responder a costos, obras de alcance nacional o reglas como el canon.", 9, color=SUAVE, ancho=100)

    texto(fig, x0, 0.135, "Preguntas para quien decide", 11, "bold")
    preguntas = ["¿Los criterios de asignación de la inversión consideran cuántos pobres hay en cada departamento, "
                 "además de cuánta población?",
                 "¿Conviene reportar la inversión por persona pobre en el seguimiento presupuestal?"]
    for i, p in enumerate(preguntas):
        texto(fig, x0, 0.112 - i * 0.03, "→  " + p, 9, color=TINTA, ancho=98)

    texto(fig, x0, 0.04, "Fuentes: BCRP, inversión bruta fija por departamentos (series RD, 2020–2024), vía servidor MCP; "
          "INEI, ENAHO 2024, ponderada y validada contra «Perú: Evolución de la Pobreza Monetaria 2015-2024». "
          "Intervalos al 95 % por el diseño muestral. Fiorella Ampuero, Tarea 4 (Python Intermedio). "
          "Proyecto académico personal; no representa a ninguna institución.", 7, color=SUAVE, ancho=150)

    destino = Path("informes")
    destino.mkdir(exist_ok=True)
    for ext in ("png", "pdf"):
        fig.savefig(destino / f"policy_brief.{ext}", dpi=200, facecolor=FONDO)
    plt.close(fig)
    print(f"5 más pobres: {top5.pct_pobres_pais.sum():.1f} % de los pobres y {top5.pct_inversion.sum():.1f} % de la "
          f"inversión; {len(debajo)} departamentos con IC < 1; Lima Metropolitana {lm.pct_pobres_pais:.1f} % de los pobres.")
    print("Guardado: informes/policy_brief.png y informes/policy_brief.pdf")


if __name__ == "__main__":
    main()
