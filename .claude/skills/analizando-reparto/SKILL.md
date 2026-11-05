---
name: analizando-reparto
description: Compara cómo se reparte la inversión pública del BCRP entre departamentos (2020–2024, gobiernos nacional, regionales y locales) con dónde vive la población pobre según la ENAHO 2024, con intervalos de confianza validados contra el INEI, curva de concentración, densidad poblacional, minería y un recuadro de Lima. Úsala cuando pidan cruzar inversión pública o datos del BCRP por departamento con la pobreza de la ENAHO, o preguntar si la inversión llega a los departamentos pobres.
---
# Analizar el reparto de la inversión frente a la pobreza

Corre los comandos desde la raíz de Tarea_4.

1. Si no existe `salidas/personas_2024.parquet`, usa primero la skill `limpiando-enaho`.
2. Si faltan los archivos `salidas/bcrp_*.csv`, pídelos al servidor MCP `bcrp` con la herramienta `cuadre_territorial` y `guardar=True`:
   - `inversion_gobierno_nacional`, `inversion_gobiernos_regionales` e `inversion_gobiernos_locales`, de `2020` a `2024`;
   - `exportaciones_mineras`, de `2018` a `2022` (por departamento, el BCRP publica solo hasta 2022).
   No escribas esos archivos a mano ni copies cifras: deben salir de la herramienta.
3. Corre exactamente: `uv run "${CLAUDE_SKILL_DIR}/scripts/analizar.py"`
4. Si el script se detiene, muestra el error y no reportes resultados. No relajes las validaciones.
5. Responde con las cifras de `salidas/analisis.txt`, sin redondear distinto, y las rutas de las figuras.

## Reglas que cumple el script

No las cambies aunque edites el análisis.

- **Verifica el cuadre** de cada archivo del BCRP: los departamentos (y la Municipalidad Metropolitana de Lima, asignada a Lima) deben sumar el total oficial cada año.
- **Valida la ENAHO contra el INEI** (`referencias/inei_pobreza_2024.csv`, del informe «Perú: Evolución de la Pobreza Monetaria, 2015-2024», anexo p. 220): 27 ámbitos a 0.1 puntos como máximo, y el ancho de los intervalos entre 0.85 y 1.15 veces el oficial.
- **Diseño muestral**: conglomerados (`conglome`) dentro de estratos `departamento × estrato`, linealización; hogares únicos con `factor07 × mieperho`.
- **Participaciones, no conteos**: el INEI ajusta los conteos absolutos a proyecciones de población (9 395 mil pobres) y la base pública da otro total; las tasas y las partes sí coinciden.
- **Lima es un departamento** (como lo publica el BCRP); el recuadro separa Lima Metropolitana y Lima provincias solo donde la fuente lo permite (pobreza e inversión regional).
- **Descriptivo**: compara repartos. No escribas que la inversión causa o reduce la pobreza, ni que un gobierno es eficiente o ineficiente.
- Figuras con la paleta validada de la skill dataviz, título que dice el hallazgo, unidades y fuente.

## Lo que sale

| Archivo | Contenido |
|---|---|
| `salidas/indicadores.csv` | 25 departamentos: pobreza e IC, % de pobres del país e IC, % de población, % de inversión (total y por nivel), inversión/pobres e IC, densidad, inversión por habitante, % de exportaciones mineras |
| `salidas/recuadro_lima.csv` | Lima Metropolitana y Lima provincias |
| `salidas/analisis.txt` | Validaciones y los tres hallazgos con sus cifras |
| `figuras/bcrp_inversion_anual.png` | Inversión por nivel de gobierno, 2020–2024 (gráfico del BCRP) |
| `figuras/inversion_vs_pobres.png` | Inversión/pobres por departamento, con IC 95 % |
| `figuras/curva_concentracion.png` | Curvas de concentración de la inversión y de la población pobre |
| `figuras/densidad_inversion.png` | Inversión por habitante según densidad y pobreza |
