"""Limpia los módulos 34 (sumaria) y 02 (miembros) de la ENAHO y valida contra el INEI.

Uso (desde la raíz del repositorio):
    uv run .claude/skills/limpiando-enaho/scripts/limpiar.py --anio 2024

Sale: salidas/personas_2024.parquet y salidas/validacion.txt.
Si una validación falla, escribe validacion.txt, no guarda la base y termina con código 1.
"""

import argparse
import sys
import zipfile
from pathlib import Path

import pandas as pd

# Por ahora solo 2024 tiene cifras de referencia para validar.
ANIOS = {
    2024: {
        "codigo": 966,
        "sumaria": "966-Modulo34/sumaria-2024.dta",
        "miembros": "966-Modulo02/enaho01-2024-200.dta",
        "pobreza": 27.6,
        "extrema": 5.5,
        "hogares": 33_691,
        "filas_miembros": 117_721,
        "residentes": 108_664,
    }
}
TOLERANCIA = 0.1  # puntos porcentuales

LLAVES_HOGAR = ["conglome", "vivienda", "hogar"]
LLAVES_PERSONA = LLAVES_HOGAR + ["codperso"]
COLUMNAS_HOGAR = LLAVES_HOGAR + ["ubigeo", "dominio", "estrato", "pobreza", "factor07", "mieperho"]
COLUMNAS_PERSONA = LLAVES_PERSONA + ["p203", "p204", "p205", "p206", "p207", "p208a", "facpob07"]


def leer(zip_path: Path, interno: str, llaves: list[str]) -> pd.DataFrame:
    """Lee un .dta del zip, con los códigos sin etiquetar y los nombres en minúscula."""
    if not zip_path.exists():
        sys.exit(f"Falta {zip_path}. Bájalo del portal de microdatos del INEI (ver README.md).")
    with zipfile.ZipFile(zip_path) as z, z.open(interno) as f:
        df = pd.read_stata(f, convert_categoricals=False)
    df.columns = df.columns.str.lower()  # la columna del año llega como «aÑo»
    for llave in llaves + ["ubigeo"]:
        if llave in df.columns:
            if not pd.api.types.is_string_dtype(df[llave]):
                sys.exit(f"La llave {llave} no llegó como texto: perdería los ceros a la izquierda.")
    return df


def ponderada(condicion: pd.Series, peso: pd.Series) -> float:
    return float(100 * peso[condicion].sum() / peso.sum())


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--anio", type=int, default=2024)
    parser.add_argument("--datos", type=Path, default=Path("datos"))
    parser.add_argument("--salidas", type=Path, default=Path("salidas"))
    args = parser.parse_args()

    if args.anio not in ANIOS:
        sys.exit(f"Solo hay cifras de referencia para validar {sorted(ANIOS)}; no se limpia {args.anio} sin validar.")
    ref = ANIOS[args.anio]
    codigo = ref["codigo"]

    # 1 y 2. Leer y normalizar
    hogares = leer(args.datos / f"{codigo}-Modulo34.zip", ref["sumaria"], LLAVES_HOGAR)
    miembros = leer(args.datos / f"{codigo}-Modulo02.zip", ref["miembros"], LLAVES_PERSONA)
    filas_miembros = len(miembros)

    # 3. Residentes habituales: miembro presente, o no miembro que vive hace 30 días o más
    es_residente = ((miembros.p204 == 1) & (miembros.p205 == 2)) | ((miembros.p204 == 2) & (miembros.p206 == 1))
    personas = miembros.loc[es_residente, COLUMNAS_PERSONA]

    # 4. Unir personas y hogares. ubigeo, dominio y estrato se toman de la sumaria.
    base = personas.merge(
        hogares[COLUMNAS_HOGAR], on=LLAVES_HOGAR, how="left", validate="m:1", indicator=True
    )

    # 5. Construir
    base["departamento"] = base.ubigeo.str[:2]
    base["urbano"] = base.estrato <= 5
    base["pobre"] = base.pobreza <= 2  # pobreza es un código (1, 2, 3), nunca un promedio
    base["pobre_extremo"] = base.pobreza == 1
    base["anio"] = args.anio

    # 6. Validar
    peso_hogar = hogares.factor07 * hogares.mieperho
    pob_sumaria = ponderada(hogares.pobreza <= 2, peso_hogar)
    ext_sumaria = ponderada(hogares.pobreza == 1, peso_hogar)
    pob_personas = ponderada(base.pobre, base.facpob07)
    ext_personas = ponderada(base.pobre_extremo, base.facpob07)

    pruebas = [
        ("Llaves de hogar únicas en la sumaria", not hogares.duplicated(LLAVES_HOGAR).any()),
        ("Llaves de persona únicas en el módulo 02", not miembros.duplicated(LLAVES_PERSONA).any()),
        (f"Hogares en la sumaria = {ref['hogares']:,}", len(hogares) == ref["hogares"]),
        (f"Filas del módulo 02 = {ref['filas_miembros']:,}", filas_miembros == ref["filas_miembros"]),
        (f"Residentes habituales = {ref['residentes']:,}", len(personas) == ref["residentes"]),
        ("La unión no perdió ni duplicó filas", len(base) == len(personas)),
        ("Toda persona encontró su hogar", (base._merge == "both").all()),
        ("Ninguna persona sin facpob07", base.facpob07.notna().all()),
        ("25 departamentos en la base", base.departamento.nunique() == 25),
        (f"Pobreza con sumaria a {TOLERANCIA} de {ref['pobreza']} %", abs(pob_sumaria - ref["pobreza"]) < TOLERANCIA),
        (f"Pobreza con personas a {TOLERANCIA} de {ref['pobreza']} %", abs(pob_personas - ref["pobreza"]) < TOLERANCIA),
        (f"Pobreza extrema con sumaria a {TOLERANCIA} de {ref['extrema']} %", abs(ext_sumaria - ref["extrema"]) < TOLERANCIA),
    ]
    aprobado = all(ok for _, ok in pruebas)

    lineas = [
        f"VALIDACIÓN ENAHO {args.anio}",
        "",
        f"Pobreza monetaria, sumaria (factor07 x mieperho): {pob_sumaria:.2f} %",
        f"Pobreza monetaria, personas (facpob07):           {pob_personas:.2f} %",
        f"Pobreza extrema, sumaria:                         {ext_sumaria:.2f} %",
        f"Pobreza extrema, personas:                        {ext_personas:.2f} %",
        f"Referencia:                                       {ref['pobreza']} % y {ref['extrema']} %",
        "",
        f"Hogares en la sumaria:   {len(hogares):,}",
        f"Filas del módulo 02:     {filas_miembros:,}",
        f"Residentes habituales:   {len(personas):,}",
        f"Filas de la base final:  {len(base):,}",
        "",
    ]
    lineas += [f"[{'OK' if ok else 'FALLA'}] {texto}" for texto, ok in pruebas]
    lineas += ["", f"RESULTADO: {'APROBADO' if aprobado else 'NO APROBADO'}"]
    texto = "\n".join(lineas) + "\n"

    # 7. Guardar
    args.salidas.mkdir(parents=True, exist_ok=True)
    (args.salidas / "validacion.txt").write_text(texto, encoding="utf-8")
    sys.stdout.reconfigure(encoding="utf-8")
    print(texto)
    destino = args.salidas / f"personas_{args.anio}.parquet"
    if not aprobado:
        destino.unlink(missing_ok=True)  # no dejar una base anterior que parezca validada
        sys.exit(1)
    base.drop(columns="_merge").to_parquet(destino, index=False)
    print(f"Base guardada en {destino}")


if __name__ == "__main__":
    main()
