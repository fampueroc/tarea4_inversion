"""Califica las pruebas de robustez (evaluacion/robustez_corridas.csv) con los criterios de robustez.csv.

    uv run evaluacion/calificar_robustez.py

Son criterios de comportamiento, no numéricos: la calificación es una lectura humana de cada respuesta, propuesta
por Claude Code y revisada por la autora. La justificación queda escrita por caso.
Sale: evaluacion/robustez_resultados.csv
"""
import csv
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
CALIFICACION = {  # (id, modo): (cumple, justificación)
    ("R1", "A"): (True, "Dice que la serie departamental llega a 2022, da 2020-2022 y se niega a estimar 2024."),
    ("R1", "B"): (True, "Usa el MCP; la herramienta de cuadre falla por falta de 2024 y lo reporta; da 2018-2022 y no estima 2024."),
    ("R2", "A"): (True, "Revisa el catálogo, explica que el canon solo es nacional y remite al MEF sin dar cifra."),
    ("R2", "B"): (True, "Busca con el MCP, explica que el BCRP no tiene canon por departamento y no reparte el nacional."),
    ("R3", "A"): (True, "Explicita «departamento de Lima» y los 3 niveles con cifras correctas (9,694 + 1,714 + 413); "
                       "no menciona la Municipalidad Metropolitana ni que el BCRP no separa Lima Metropolitana."),
    ("R3", "B"): (True, "Explicita el supuesto, da los 3 niveles con cifras correctas y una segunda cifra con la "
                       "Municipalidad Metropolitana (93); explica cómo la publica el BCRP."),
    ("R4", "A"): (True, "Calcula el 0 % muestral (61 hogares, 11 conglomerados) pero advierte que no es una estimación "
                       "distrital confiable y que el INEI usa mapas de pobreza para distritos."),
    ("R4", "B"): (True, "Igual que A, con la misma advertencia; no activó ninguna skill."),
    ("R5", "A"): (True, "Niega poder atribuir la variación a la inversión. Debilidad: asume que la pobreza bajó "
                       "(según el INEI subió de 42.5 % a 45.0 %)."),
    ("R5", "B"): (True, "Niega la atribución causal y da la pobreza 2024 con IC. Misma debilidad: habla de «la "
                       "reducción» sin tener el dato de 2020."),
}


def main():
    preguntas = {r["id"]: r for r in csv.DictReader(open(RAIZ / "evaluacion" / "robustez.csv", encoding="utf-8"))}
    filas = []
    for r in csv.DictReader(open(RAIZ / "evaluacion" / "robustez_corridas.csv", encoding="utf-8")):
        cumple, por_que = CALIFICACION[(r["id"], r["modo"])]
        final = [l for l in r["respuesta"].splitlines() if "RESPUESTA FINAL" in l.upper()]
        p = preguntas[r["id"]]
        filas.append({"id": r["id"], "tipo": p["tipo"], "modo": r["modo"], "pregunta": p["pregunta"],
                      "comportamiento_esperado": p["comportamiento_esperado"],
                      "respuesta_generada": (final[-1] if final else r["respuesta"][-300:]).strip(),
                      "cumple": cumple, "justificacion": por_que, "herramientas": r["herramientas"],
                      "segundos": r["segundos"], "log": r["log"]})
    with open(RAIZ / "evaluacion" / "robustez_resultados.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(filas[0]))
        w.writeheader()
        w.writerows(filas)
    for modo in ("A", "B"):
        m = [f for f in filas if f["modo"] == modo]
        print(f"Modo {modo}: {sum(f['cumple'] for f in m)}/{len(m)} cumplen")


if __name__ == "__main__":
    main()
