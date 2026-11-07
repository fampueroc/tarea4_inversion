"""Exploración 2: Lima Metropolitana frente al resto de Lima, y densidad poblacional. Borrador.
    uv run analisis/explorar_densidad.py
"""
import sys
from pathlib import Path

import geopandas as gpd
import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "mcp"))
from server import cuadre_territorial

sys.stdout.reconfigure(encoding="utf-8")
LLAVES = ["conglome", "vivienda", "hogar"]
h = pd.read_parquet("salidas/personas_2024.parquet").drop_duplicates(LLAVES).copy()
h["w"] = h.factor07.astype("float64") * h.mieperho

# Lima Metropolitana (provincia 1501) frente al resto del departamento de Lima
lima = h[h.departamento == "15"].assign(parte=lambda d: np.where(d.ubigeo.str[:4] == "1501", "Lima Metropolitana", "Lima provincias"))
for parte, g in lima.groupby("parte"):
    print(f"{parte}: pobreza {100 * g.w[g.pobre].sum() / g.w.sum():.1f} %, población {g.w.sum():,.0f}, pobres {g.w[g.pobre].sum():,.0f}")
r = cuadre_territorial("inversion_gobiernos_regionales", "2020", "2024")
gr_lima = sum(d["valores"].values() for d in r["departamentos"] if d["ubigeo"] == "15") if False else \
    sum(next(d for d in r["departamentos"] if d["ubigeo"] == "15")["valores"].values())
mml = sum(o["valor"] for c in r["cuadre"] for o in c["otras_series"])
print(f"Inversión regional 2020–2024: Gobierno Regional de Lima {gr_lima:,.0f} M S/; Municipalidad Metropolitana {mml:,.0f} M S/\n")

# Densidad: superficie del GeoJSON del curso (HECTARES) y población expandida de la ENAHO
geo = gpd.read_file("datos/peru_departamental_simple.geojson")
area_geom = geo.to_crs("ESRI:102033").area / 1e6   # equal-area para Sudamérica, km²
sup = pd.DataFrame({"ubigeo": geo.FIRST_IDDP.astype(str), "km2": geo.HECTARES / 100, "km2_geometria": area_geom}).set_index("ubigeo")
inv = pd.Series(0.0, index=sup.index)
for nivel in ["inversion_gobierno_nacional", "inversion_gobiernos_regionales", "inversion_gobiernos_locales"]:
    r = cuadre_territorial(nivel, "2020", "2024")
    for d in r["departamentos"]:
        inv[d["ubigeo"]] += sum(d["valores"].values())
    inv["15"] += sum(o["valor"] for c in r["cuadre"] for o in c["otras_series"])
pob = h.groupby("departamento").w.sum(); pobre = h[h.pobre].groupby("departamento").w.sum()
t = sup.assign(densidad=pob / sup.km2, pobreza=100 * pobre / pob,
               inv_pc=1e6 * inv / pob / 5)   # soles por habitante por año, promedio 2020–2024
t["nombre"] = geo.set_index(geo.FIRST_IDDP.astype(str)).NOMBDEP
print("Superficie: HECTARES del GeoJSON vs. área calculada de la geometría (diferencia máx. %):",
      round(100 * ((t.km2 - t.km2_geometria) / t.km2).abs().max(), 1))
print(t.sort_values("densidad")[["nombre", "densidad", "pobreza", "inv_pc"]].round(1).to_string())

# Regresión descriptiva: log(inversión por habitante) según pobreza y log(densidad), 25 departamentos
X = np.column_stack([np.ones(len(t)), t.pobreza, np.log(t.densidad)]); y = np.log(t.inv_pc)
b, *_ = np.linalg.lstsq(X, y, rcond=None)
res = y - X @ b; n, k = X.shape
ee = np.sqrt(np.diag(res @ res / (n - k) * np.linalg.inv(X.T @ X)))
print(f"\nlog(inversión por habitante) = {b[0]:.2f} {b[1]:+.4f}·pobreza {b[2]:+.3f}·log(densidad);  "
      f"ee: {ee[1]:.4f}, {ee[2]:.3f};  R² = {1 - res.var() / y.var():.2f}")
print(f"Sin densidad: corr(pobreza, log inversión por hab.) = {np.corrcoef(t.pobreza, y)[0, 1]:.2f}; "
      f"corr(log densidad, log inversión por hab.) = {np.corrcoef(np.log(t.densidad), y)[0, 1]:.2f}")
