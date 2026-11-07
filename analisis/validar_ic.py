"""Valida el método de errores estándar contra los intervalos oficiales del INEI (pobreza 2024 por departamento).
Fuente: INEI, «Perú: Evolución de la Pobreza Monetaria, 2015-2024», anexo, p. 220 (intervalo de confianza al 95 %).
    uv run analisis/validar_ic.py
"""
import sys
import numpy as np
import pandas as pd

sys.stdout.reconfigure(encoding="utf-8")
INEI = {  # departamento: (pobreza, IC inferior, IC superior), 2024
    "01": (25.7, 20.9, 30.6), "02": (22.8, 19.1, 26.4), "03": (24.0, 19.3, 28.6), "04": (15.8, 12.6, 19.0),
    "05": (32.8, 28.3, 37.3), "06": (45.0, 40.7, 49.3), "08": (18.5, 14.7, 22.4), "09": (33.4, 29.1, 37.7),
    "10": (39.0, 33.9, 44.0), "11": (6.0, 4.2, 7.9), "12": (18.5, 14.9, 22.1), "13": (30.2, 26.6, 33.8),
    "14": (14.0, 10.3, 17.8), "LM": (27.6, 25.0, 30.1), "07": (33.9, 29.1, 38.6), "LP": (21.7, 18.3, 25.1),
    "16": (43.0, 38.8, 47.2), "17": (11.1, 6.8, 15.5), "18": (11.0, 7.5, 14.5), "19": (39.0, 34.0, 44.0),
    "20": (31.9, 28.6, 35.1), "21": (39.9, 35.4, 44.5), "22": (22.0, 18.1, 25.9), "23": (24.0, 18.3, 29.6),
    "24": (26.9, 22.1, 31.7), "25": (27.1, 22.7, 31.4)}

h = pd.read_parquet("salidas/personas_2024.parquet").drop_duplicates(["conglome", "vivienda", "hogar"]).copy()
h["w"] = h.factor07.astype("float64") * h.mieperho
h["ambito"] = h.departamento.where(h.departamento != "15",
                                   np.where(h.ubigeo.str[:4] == "1501", "LM", "LP"))


def tasa_ee(h, en, estratos):
    """Tasa de pobreza de un dominio y su error estándar (linealización; conglomerados con reemplazo en estratos)."""
    W = h.w[en].sum(); p = h.w[en & h.pobre].sum() / W
    z = np.where(en, h.w * (h.pobre - p) / W, 0.0)
    g = pd.DataFrame({"z": z, "s": estratos, "c": h.conglome}).groupby(["s", "c"]).z.sum().reset_index()
    v = sum(len(t) / (len(t) - 1) * ((t.z - t.z.mean()) ** 2).sum() for _, t in g.groupby("s") if len(t) > 1)
    return 100 * p, 100 * np.sqrt(v)


disenos = {"estrato": h.estrato.astype(str),
           "departamento × estrato": h.departamento + "-" + h.estrato.astype(str)}
filas = []
for a, (p_inei, li, ls) in INEI.items():
    f = {"ambito": a, "inei_pobreza": p_inei, "inei_semiancho": (ls - li) / 2}
    for nombre, s in disenos.items():
        p, ee = tasa_ee(h, h.ambito == a, s)
        f["pobreza"] = round(p, 1); f[f"semiancho_{nombre}"] = 1.96 * ee
    filas.append(f)
t = pd.DataFrame(filas)
print(t.round(2).to_string(index=False))
print("\nPobreza: máxima diferencia con el INEI:", (t.pobreza - t.inei_pobreza).abs().max().round(2), "puntos")
for nombre in disenos:
    r = t[f"semiancho_{nombre}"] / t.inei_semiancho
    print(f"Diseño {nombre}: semiancho propio / INEI → mediana {r.median():.2f}, rango {r.min():.2f}–{r.max():.2f}")
p, ee = tasa_ee(h, pd.Series(True, index=h.index), disenos["departamento × estrato"])
print(f"Nacional: {p:.1f} % [{p - 1.96 * ee:.1f}–{p + 1.96 * ee:.1f}]  (INEI: 27,6 [26,6–28,6])")
