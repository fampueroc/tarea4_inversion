"""Grafica la pobreza 2024 de la ENAHO por área, sexo o edad.

Uso (desde la raíz del repositorio):
    uv run .claude/skills/graficando-enaho/scripts/graficar.py --por area

Sale: figuras/pobreza_<area|sexo|edad>.png e imprime los valores.
"""

import argparse
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

LLAVES_HOGAR = ["conglome", "vivienda", "hogar"]
EDADES = [0, 15, 30, 45, 60, 200]
NOMBRES_EDAD = ["0 a 14", "15 a 29", "30 a 44", "45 a 59", "60 o más"]
TITULOS = {
    "area": "Pobreza monetaria por área de residencia, Perú 2024",
    "sexo": "Pobreza monetaria por sexo, Perú 2024",
    "edad": "Pobreza monetaria por grupo de edad, Perú 2024",
}
COLOR = "#2a78d6"
TINTA = "#0b0b0b"
TINTA_SUAVE = "#52514e"


def calcular(base: pd.DataFrame, por: str) -> tuple[pd.Series, str]:
    """Devuelve la pobreza por grupo y una nota sobre el peso usado."""
    if por == "area":
        # El área es del hogar: hogares únicos con factor07 x mieperho, como la sumaria.
        datos = base.drop_duplicates(LLAVES_HOGAR).copy()
        datos["peso"] = datos.factor07.astype("float64") * datos.mieperho
        clave = datos.urbano.map({True: "Urbana", False: "Rural"})
        nota = "factor07 × mieperho"
    else:
        datos = base.copy()
        datos["peso"] = datos.facpob07.astype("float64")
        nota = "facpob07"
        if por == "sexo":
            clave = datos.p207.map({1: "Hombres", 2: "Mujeres"})
        else:
            clave = pd.cut(datos.p208a, EDADES, right=False, labels=NOMBRES_EDAD)
    tasas = datos.groupby(clave, observed=True).apply(
        lambda g: 100 * g.loc[g.pobre, "peso"].sum() / g["peso"].sum(), include_groups=False
    )
    # La edad conserva su orden natural; lo demás se ordena de mayor a menor.
    return (tasas if por == "edad" else tasas.sort_values(ascending=False)), nota


def dibujar(tasas: pd.Series, por: str, nota: str, destino: Path) -> None:
    alto = 1.7 + 0.5 * len(tasas)
    fig, ax = plt.subplots(figsize=(7.5, alto))
    posiciones = range(len(tasas))
    ax.barh(posiciones, tasas.values, color=COLOR, height=0.62)
    ax.set_yticks(list(posiciones), [str(i) for i in tasas.index], color=TINTA, fontsize=11)
    ax.invert_yaxis()
    ax.set_xlim(0, max(50, tasas.max() * 1.15))  # empieza en cero, con la misma escala en todas
    for y, valor in zip(posiciones, tasas.values):
        ax.text(valor + 0.6, y, f"{valor:.1f} %", va="center", color=TINTA, fontsize=11)
    ax.xaxis.set_visible(False)
    for lado in ("top", "right", "bottom"):
        ax.spines[lado].set_visible(False)
    ax.spines["left"].set_color("#c3c2b7")
    ax.tick_params(axis="y", length=0)
    fig.suptitle(TITULOS[por], x=0.02, ha="left", fontsize=13, fontweight="bold", color=TINTA)
    pie = f"% de personas en pobreza monetaria. Fuente: INEI, ENAHO 2024. Ponderado con {nota}."
    fig.text(0.02, 0.02, pie, fontsize=8, color=TINTA_SUAVE)
    fig.tight_layout(rect=(0, 0.07, 1, 0.93))
    destino.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(destino, dpi=200, facecolor="white")
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--por", required=True, choices=list(TITULOS))
    parser.add_argument("--base", type=Path, default=Path("salidas/personas_2024.parquet"))
    parser.add_argument("--figuras", type=Path, default=Path("figuras"))
    args = parser.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    if not args.base.exists():
        sys.exit(f"Falta {args.base}. Usa primero la skill limpiando-enaho.")
    tasas, nota = calcular(pd.read_parquet(args.base), args.por)
    destino = args.figuras / f"pobreza_{args.por}.png"
    dibujar(tasas, args.por, nota, destino)
    print(tasas.round(1).to_string(header=False))
    print(f"Peso: {nota}\nFigura: {destino}")


if __name__ == "__main__":
    main()
