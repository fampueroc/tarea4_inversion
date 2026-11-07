"""Exploración: ¿la inversión pública 2020–2024 se reparte como la población pobre de 2024?

Borrador para revisar el enfoque antes de escribir la versión final. Correr desde la raíz de Tarea_4:
    uv run analisis/explorar_primeros_numeros.py
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "mcp"))
from server import cuadre_territorial  # la misma herramienta que usa Claude por MCP

sys.stdout.reconfigure(encoding="utf-8")
LLAVES = ["conglome", "vivienda", "hogar"]
NIVELES = ["inversion_gobierno_nacional", "inversion_gobiernos_regionales", "inversion_gobiernos_locales"]

# 1. BCRP: inversión 2020–2024 por departamento y nivel de gobierno (millones S/ corrientes)
filas = []
for nivel in NIVELES:
    r = cuadre_territorial(nivel, "2020", "2024")
    assert r["cuadra_todo"], nivel
    for d in r["departamentos"]:
        for anio, v in d["valores"].items():
            filas.append({"ubigeo": d["ubigeo"], "departamento": d["departamento"], "nivel": nivel, "anio": anio, "valor": v})
    # Municipalidad Metropolitana de Lima: el BCRP la publica aparte en la inversión regional; va a Lima (15)
    for c in r["cuadre"]:
        for o in c["otras_series"]:
            filas.append({"ubigeo": "15", "departamento": "Lima", "nivel": nivel, "anio": c["periodo"], "valor": o["valor"]})
inv = pd.DataFrame(filas)
inv_depto = inv.groupby("ubigeo").valor.sum()
print(f"Inversión pública 2020–2024 (3 niveles): {inv.valor.sum():,.0f} millones S/")
print(inv.groupby("anio").valor.sum().round(0).to_string(), "\n")

# 2. BCRP: exportaciones mineras, promedio 2018–2022 (último año publicado por departamento)
mina = cuadre_territorial("exportaciones_mineras", "2018", "2022")
exp_min = pd.Series({d["ubigeo"]: np.mean(list(d["valores"].values())) for d in mina["departamentos"]})

# 3. ENAHO 2024: población pobre por departamento (hogares únicos, factor07 × mieperho)
h = pd.read_parquet("salidas/personas_2024.parquet").drop_duplicates(LLAVES).copy()
h["w"] = h.factor07.astype("float64") * h.mieperho
h["ubigeo"] = h.departamento
pobres = h[h.pobre].groupby("ubigeo").w.sum()
poblacion = h.groupby("ubigeo").w.sum()


# Error estándar de la participación de cada departamento en los pobres del país (linealización de un cociente,
# conglomerados dentro de estratos; estrato de diseño = departamento × estrato geográfico)
def ee_participacion(h, d):
    Y = (h.w * h.pobre).sum()
    yd = h.w * h.pobre * (h.ubigeo == d)
    R = yd.sum() / Y
    z = (yd - R * h.w * h.pobre) / Y
    g = pd.DataFrame({"z": z, "estr": h.ubigeo + "-" + h.estrato.astype(str), "c": h.conglome})
    tot = g.groupby(["estr", "c"]).z.sum().reset_index()
    var = 0.0
    for _, t in tot.groupby("estr"):
        n = len(t)
        if n > 1:
            var += n / (n - 1) * ((t.z - t.z.mean()) ** 2).sum()
    return np.sqrt(var)


nombres = pd.Series({d["ubigeo"]: d["departamento"] for d in mina["departamentos"]})
t = pd.DataFrame({
    "departamento": nombres,
    "pobreza_pct": 100 * pobres / poblacion,
    "pct_pobres_pais": 100 * pobres / pobres.sum(),
    "pct_inversion": 100 * inv_depto / inv_depto.sum(),
    "pct_exp_mineras": 100 * exp_min / exp_min.sum(),
})
t["ee_pct_pobres"] = [100 * ee_participacion(h, d) for d in t.index]
t["ic95_pobres"] = [f"{a - 1.96 * e:.1f}–{a + 1.96 * e:.1f}" for a, e in zip(t.pct_pobres_pais, t.ee_pct_pobres)]
t["inversion_vs_pobres"] = t.pct_inversion / t.pct_pobres_pais   # >1: recibe más inversión que su parte de pobres
t = t.sort_values("pobreza_pct", ascending=False)

# Curva e índice de concentración: departamentos de más pobre a menos pobre
cum_pob = np.r_[0, (poblacion[t.index] / poblacion.sum()).cumsum().values]
cum_inv = np.r_[0, (inv_depto[t.index] / inv_depto.sum()).cumsum().values]
cum_pobres = np.r_[0, (pobres[t.index] / pobres.sum()).cumsum().values]
ic = lambda cum: 1 - np.sum(np.diff(cum_pob) * (cum[1:] + cum[:-1]))   # >0 se concentra en los menos pobres

pd.set_option("display.width", 200)
print(t[["departamento", "pobreza_pct", "pct_pobres_pais", "ic95_pobres", "pct_inversion", "inversion_vs_pobres",
         "pct_exp_mineras"]].round(2).to_string())
print(f"\nPobres en el país: {pobres.sum():,.0f} de {poblacion.sum():,.0f} personas ({100 * pobres.sum() / poblacion.sum():.2f} %)")
print(f"Índice de concentración (orden: de mayor a menor pobreza; negativo = favorece a los más pobres)")
print(f"  inversión pública 2020–2024: {ic(cum_inv):+.3f}")
print(f"  población pobre (referencia): {ic(cum_pobres):+.3f}")
print(f"Correlación entre % de inversión y % de pobres: {t.pct_inversion.corr(t.pct_pobres_pais):.2f}; "
      f"con % de exportaciones mineras: {t.pct_inversion.corr(t.pct_exp_mineras):.2f}")

# --- Revisión adicional: tamaño de la población y niveles de gobierno
t["pct_poblacion"] = 100 * poblacion[t.index] / poblacion.sum()
t["inversion_vs_poblacion"] = t.pct_inversion / t.pct_poblacion
print("\nInversión frente a población total (no solo pobres), 6 primeros y 6 últimos por pobreza:")
print(t[["departamento", "pct_poblacion", "pct_inversion", "inversion_vs_poblacion"]].round(2).iloc[np.r_[0:6, -6:0]].to_string())
for nivel in NIVELES:
    s = inv[inv.nivel == nivel].groupby("ubigeo").valor.sum()
    c = np.r_[0, (s[t.index] / s.sum()).cumsum().values]
    print(f"Índice de concentración, {nivel}: {ic(c):+.3f}")
sub = inv[inv.nivel != NIVELES[0]].groupby("ubigeo").valor.sum()
t["sub_vs_pobres"] = (100 * sub / sub.sum())[t.index] / t.pct_pobres_pais
print(f"Correlación de Spearman entre (inversión subnacional / pobres) y % exportaciones mineras: "
      f"{t.sub_vs_pobres.rank().corr(t.pct_exp_mineras.rank()):.2f}")
