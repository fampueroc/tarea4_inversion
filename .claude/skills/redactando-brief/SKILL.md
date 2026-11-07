---
name: redactando-brief
description: Convierte los resultados validados del análisis de inversión pública y pobreza en un policy brief de una página (PNG y PDF) para quien toma decisiones, con tres cifras clave, un gráfico, el límite del análisis y preguntas para la decisión. Úsala cuando pidan un policy brief, una lámina, un resumen ejecutivo de una página o una versión para decisores de los hallazgos.
---
# Redactar el policy brief

Corre los comandos desde la raíz de Tarea_4. Adapta el método de la skill `canvas-design` de Anthropic: primero una filosofía de diseño escrita (`filosofia.md`), luego una sola página y al final se pule sin agregar.

1. Si faltan `salidas/indicadores.csv`, `salidas/recuadro_lima.csv` o `salidas/analisis.txt`, usa primero la skill `analizando-reparto`.
2. Lee `${CLAUDE_SKILL_DIR}/filosofia.md` antes de cambiar cualquier elemento del diseño.
3. Corre exactamente: `uv run "${CLAUDE_SKILL_DIR}/scripts/brief.py"`
4. Abre `informes/policy_brief.png` y revisa que nada se superponga ni se salga del borde. Si algo falla, corrige posiciones o cortes de línea; no agregues elementos.
5. Responde con las rutas del PNG y del PDF y con las tres cifras que imprimió el script.

## Reglas

- **Ninguna cifra se escribe a mano:** todas se leen de las salidas de `analizando-reparto`, que ya están validadas contra el INEI y el BCRP.
- **El título afirma el hallazgo** y el cuerpo lo acota: es descriptivo, no mide efectos ni juzga eficiencia.
- **Preguntas, no recomendaciones:** los datos describen un reparto; no sostienen una receta de política.
- Un solo gráfico con la paleta validada (naranja = pobres, azul = inversión, en ese orden), con leyenda y valores escritos.
- Fuentes, autora y la aclaración «proyecto académico personal; no representa a ninguna institución» al pie.
