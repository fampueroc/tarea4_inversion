"""Hace el mapa de la pobreza 2024 por departamento, uniendo por código y nunca por nombre.

Uso (desde la raíz del repositorio):
    uv run .claude/skills/mapeando-enaho/scripts/mapear.py

Sale: mapas/pobreza_departamento.png. Si la unión o la validación fallan, no guarda el mapa.
"""

import argparse
import sys
from pathlib import Path

import geopandas as gpd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

LLAVES_HOGAR = ["conglome", "vivienda", "hogar"]
TOLERANCIA = 0.1  # puntos porcentuales frente a la referencia de la clase
REFERENCIA = Path(__file__).resolve().parent.parent / "referencias" / "pobreza_departamento_2024.csv"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", type=Path, default=Path("salidas/personas_2024.parquet"))
    parser.add_argument("--limites", type=Path, default=Path("datos/peru_departamental_simple.geojson"))
    parser.add_argument("--destino", type=Path, default=Path("mapas/pobreza_departamento.png"))
    args = parser.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    if not args.base.exists():
        sys.exit(f"Falta {args.base}. Usa primero la skill limpiando-enaho.")
    if not args.limites.exists():
        sys.exit(f"Falta {args.limites}. Bájalo como indica README.md.")

    # Pobreza por departamento: hogares únicos con factor07 x mieperho, como la sumaria
    hogares = pd.read_parquet(args.base).drop_duplicates(LLAVES_HOGAR).copy()
    hogares["peso"] = hogares.factor07.astype("float64") * hogares.mieperho
    pobreza = hogares.groupby("departamento").apply(
        lambda g: 100 * g.loc[g.pobre, "peso"].sum() / g["peso"].sum(), include_groups=False
    ).rename("pobreza_pct").reset_index()

    # Unir por código, como texto y sin perder el cero: ubigeo[:2] con FIRST_IDDP
    limites = gpd.read_file(args.limites)
    limites["FIRST_IDDP"] = limites.FIRST_IDDP.astype("string")
    mapa = limites.merge(pobreza, left_on="FIRST_IDDP", right_on="departamento", how="outer", validate="1:1")
    if len(mapa) != 25 or mapa.pobreza_pct.isna().any() or mapa.geometry.isna().any():
        sys.exit(f"La unión no dio 25 departamentos con dato:\n{mapa[['FIRST_IDDP', 'departamento', 'pobreza_pct']]}")

    # Validar contra la pobreza de referencia
    referencia = pd.read_csv(REFERENCIA, dtype={"ccdd": str}).set_index("ccdd").pobreza_pct
    diferencia = (mapa.set_index("departamento").pobreza_pct - referencia).abs()
    if diferencia.isna().any() or (diferencia >= TOLERANCIA).any():
        sys.exit(f"Departamentos lejos de la referencia:\n{diferencia[~(diferencia < TOLERANCIA)]}")

    # Dibujar: un color de claro a oscuro, desde cero. Lima (15) y Callao (07) van separados.
    fig, ax = plt.subplots(figsize=(7, 9))
    mapa.plot(
        column="pobreza_pct", cmap="Blues", vmin=0, vmax=50, ax=ax,
        edgecolor="white", linewidth=0.6, legend=True,
        legend_kwds={"label": "Pobreza monetaria (% de personas)", "shrink": 0.5},
    )
    ax.set_axis_off()
    ax.set_title("Pobreza monetaria por departamento, Perú 2024", fontsize=14, fontweight="bold", color="#0b0b0b")
    fig.text(
        0.03, 0.03,
        "Fuente: INEI, ENAHO 2024. Ponderado con factor07 × mieperho. Lima y Callao se muestran por separado.",
        fontsize=8, color="#52514e",
    )
    args.destino.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.destino, dpi=200, facecolor="white", bbox_inches="tight")
    plt.close(fig)

    orden = mapa.set_index("NOMBDEP").pobreza_pct.sort_values(ascending=False).round(1)
    print(f"25 departamentos con dato. Diferencia máxima con la referencia: {diferencia.max():.2f} puntos.")
    print(orden.to_string(header=False))
    print(f"Mapa: {args.destino}")


if __name__ == "__main__":
    main()
