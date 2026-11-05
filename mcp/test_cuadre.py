"""Dos pruebas propias para cuadre_territorial, la herramienta nueva de esta tarea.

    uv run pytest -q          # 8 originales (test_server.py, sin cambios) + estas 2 = 10 passed

Piden datos reales al BCRP. Los valores esperados se comprobaron en la API del BCRP (series RD16709DA a RD16735DA).
"""
import pytest
from fastmcp.exceptions import ToolError

from test_server import llamar


def test_cuadre_inversion_regional_explica_lima_metropolitana():
    r = llamar("cuadre_territorial", indicador="inversion_gobiernos_regionales", desde="2024", hasta="2024")
    # 25 departamentos con la llave del INEI, Lima (15) y Callao (07) por separado
    assert [d["ubigeo"] for d in r["departamentos"]] == [f"{i:02d}" for i in range(1, 26)]
    assert r["departamentos_faltantes"] == []
    c = r["cuadre"][0]
    assert c["total_oficial"] == pytest.approx(13717.39, abs=0.01)
    assert c["diferencia"] == pytest.approx(92.82, abs=0.01)
    # la diferencia es exactamente la Municipalidad Metropolitana de Lima, que el BCRP publica aparte
    assert [o["nombre"] for o in c["otras_series"]] == ["Municipalidad Metropolitana de Lima"]
    assert c["diferencia_sin_explicar"] == pytest.approx(0, abs=0.05)
    assert c["cuadra"] is True


def test_cuadre_avisa_cuando_no_hay_datos_en_vez_de_inventar():
    # las exportaciones por departamento del BCRP terminan en 2022: pedir 2024 debe fallar con un mensaje útil
    with pytest.raises(ToolError, match="último año publicado es 2022"):
        llamar("cuadre_territorial", indicador="exportaciones_mineras", desde="2024", hasta="2024")
