---
name: mapeando-enaho
description: Hace un mapa coroplético del Perú con la pobreza por departamento de la ENAHO 2024 del INEI, uniendo por código de ubigeo y validando los 25 departamentos. Úsala cuando pidan un mapa de la pobreza, un mapa por departamento o por región, o ver la pobreza de la ENAHO en el territorio.
---
# Mapear la ENAHO

Corre los comandos desde la raíz del repositorio.

1. Si no existe `salidas/personas_2024.parquet`, usa primero la skill `limpiando-enaho`.
2. Si falta `datos/peru_departamental_simple.geojson`, pide al usuario bajarlo como indica `README.md`.
3. Corre exactamente: `uv run "${CLAUDE_SKILL_DIR}/scripts/mapear.py"`
4. Si el script se detiene, muestra el error y no entregues ningún mapa. No lo arregles uniendo por nombre.
5. Abre el mapa y comprueba que ningún departamento esté en blanco.
6. Responde con la ruta del mapa, y los departamentos con mayor y menor pobreza según lo que imprimió el script.

## Reglas que cumple el script

No las cambies aunque edites el mapa.

- Une por código y como texto: `ubigeo[:2]` con `FIRST_IDDP`. Nunca por nombre: «APURIMAC» no es «Apurímac».
- Exige 25 departamentos y ninguno sin dato.
- Valida cada departamento contra `referencias/pobreza_departamento_2024.csv` (copia idéntica del archivo de la sesión 16 del curso) y guarda la comparación en `salidas/mapa_vs_referencia.csv`.
- Pondera con hogares únicos y `factor07 × mieperho`, como la referencia.
- Un color de claro a oscuro, desde 0. Nunca arcoíris.
- Leyenda con la unidad: % de personas.
- Lima (15) y Callao (07) van separados.
