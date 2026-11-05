"""Imprime la pobreza ponderada a partir de la base limpia.

Uso (desde la raíz del repositorio):
    uv run .claude/skills/limpiando-enaho/scripts/resumen.py --por departamento

--por: nacional, departamento, area, lima_metropolitana, sexo o edad.
"""

import argparse
import sys
from pathlib import Path

import pandas as pd

LLAVES_HOGAR = ["conglome", "vivienda", "hogar"]
EDADES = [0, 15, 30, 45, 60, 200]
NOMBRES_EDAD = ["0-14", "15-29", "30-44", "45-59", "60 o más"]
DEPARTAMENTOS = {
    "01": "Amazonas", "02": "Áncash", "03": "Apurímac", "04": "Arequipa", "05": "Ayacucho",
    "06": "Cajamarca", "07": "Callao", "08": "Cusco", "09": "Huancavelica", "10": "Huánuco",
    "11": "Ica", "12": "Junín", "13": "La Libertad", "14": "Lambayeque", "15": "Lima",
    "16": "Loreto", "17": "Madre de Dios", "18": "Moquegua", "19": "Pasco", "20": "Piura",
    "21": "Puno", "22": "San Martín", "23": "Tacna", "24": "Tumbes", "25": "Ucayali",
}


def tasa(grupo: pd.DataFrame, peso: str) -> float:
    return 100 * grupo.loc[grupo.pobre, peso].sum() / grupo[peso].sum()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--por", default="nacional",
        choices=["nacional", "departamento", "area", "lima_metropolitana", "sexo", "edad"],
    )
    parser.add_argument("--base", type=Path, default=Path("salidas/personas_2024.parquet"))
    args = parser.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    if not args.base.exists():
        sys.exit(f"Falta {args.base}. Corre primero limpiar.py.")
    base = pd.read_parquet(args.base)

    if args.por in ("sexo", "edad"):
        # El sexo y la edad son de cada persona: se pondera con facpob07.
        datos, peso = base, "facpob07"
        if args.por == "sexo":
            clave = datos.p207.map({1: "Hombres", 2: "Mujeres"})
        else:
            clave = pd.cut(datos.p208a, EDADES, right=False, labels=NOMBRES_EDAD)
    else:
        # Área y territorio son del hogar: hogares únicos con factor07 x mieperho, como la sumaria.
        datos = base.drop_duplicates(LLAVES_HOGAR).copy()
        datos["peso_hogar"] = datos.factor07.astype("float64") * datos.mieperho
        peso = "peso_hogar"
        clave = {
            "nacional": pd.Series("Perú", index=datos.index),
            "departamento": datos.departamento.map(DEPARTAMENTOS),
            "area": datos.urbano.map({True: "Urbana", False: "Rural"}),
            "lima_metropolitana": (datos.dominio == 8).map({True: "Lima Metropolitana", False: "Resto del país"}),
        }[args.por]

    resultado = datos.groupby(clave, observed=True).apply(lambda g: tasa(g, peso), include_groups=False)
    print(f"Pobreza monetaria 2024 (% de personas), ponderada con {peso}")
    print(resultado.astype("float64").round(1).to_string(header=False))


if __name__ == "__main__":
    main()
