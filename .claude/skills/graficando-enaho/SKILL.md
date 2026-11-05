---
name: graficando-enaho
description: Hace gráficos de barras de la pobreza con la ENAHO 2024 del INEI por área urbana y rural, sexo o grupo de edad, siempre ponderados y con las mismas reglas. Úsala cuando pidan graficar, comparar o visualizar la pobreza de la ENAHO por área, sexo o edad.
---
# Graficar la ENAHO

Corre los comandos desde la raíz del repositorio.

1. Si no existe `salidas/personas_2024.parquet`, usa primero la skill `limpiando-enaho`.
2. Elige el corte según el pedido y corre exactamente: `uv run "${CLAUDE_SKILL_DIR}/scripts/graficar.py" --por <area|sexo|edad>`
3. Abre la figura y comprueba que no haya etiquetas cortadas ni superpuestas.
4. Responde con la ruta de la figura y los valores que imprimió el script, sin redondear distinto. Si la diferencia entre grupos es pequeña, aclara que son estimaciones sin intervalo de confianza y no afirmes que los grupos difieren.

## Reglas que cumple el script

No las cambies aunque edites el gráfico.

- Siempre ponderado: área con hogares únicos y `factor07 × mieperho`; sexo y edad con `facpob07`.
- Barras que empiezan en cero, ordenadas de mayor a menor. La edad conserva su orden natural.
- Un solo color y el valor escrito en cada barra.
- El título dice qué y cuándo.
- Nota al pie con la fuente: «Fuente: INEI, ENAHO 2024».
- PNG a 200 dpi en `figuras/`.

Si piden un corte que el script no tiene, avisa y escríbelo aparte con estas mismas reglas. Por departamento, usa la skill `mapeando-enaho`.
