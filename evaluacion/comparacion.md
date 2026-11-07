# Comparación: Claude Code sin y con MCP y Skills

## Diseño

| | |
|---|---|
| Preguntas | 10 (`preguntas.csv`): 4 del BCRP, 4 de la ENAHO y 2 combinadas, con respuesta esperada y tolerancia fijadas **antes** de correr (commit `942ecc1`, 6-nov-2026 00:25) |
| Respuestas esperadas | BCRP: API oficial consultada con `curl`, sin pasar por el MCP. ENAHO: informe del INEI *Perú: Evolución de la Pobreza Monetaria, 2015-2024*. Combinadas: cálculo validado contra el INEI |
| Modelo | Sonnet (`claude -p --model sonnet`), el mismo en los dos modos |
| Sesiones | Una sesión independiente por pregunta y modo (`--no-session-persistence`), 20 en total |
| Aislamiento | Cada sesión corre en una copia limpia fuera del repositorio, **sin** `salidas/`, `informes/` ni `evaluacion/` |
| Instrucción | Idéntica en los dos modos (`evaluar.py`): responder en español, no inventar cifras y cerrar con «RESPUESTA FINAL» |
| Corrección | `calificar.py` aplica las tolerancias de `preguntas.csv`; en C1 y C2 la interpretación (sin afirmar causalidad) se revisa a mano |

### Herramientas habilitadas en cada modo

| | Modo A: sin MCP ni Skills | Modo B: con MCP y Skills |
|---|---|---|
| Herramientas generales | Bash, PowerShell, Read, Write, Edit, Glob, Grep | Las mismas |
| Servidor MCP `bcrp` | No (`--strict-mcp-config`, sin `.mcp.json`) | Sí |
| Skills del proyecto | No (copia sin `.claude/` y `Skill` bloqueada) | Sí (`.claude/skills/`) |
| Web (WebSearch, WebFetch) | Bloqueada | Bloqueada |
| Datos en la copia | `datos/`: zips de la ENAHO, GeoJSON y catálogo del BCRP | Los mismos |
| Entorno de Python | El del proyecto (`UV_PROJECT_ENVIRONMENT`) | El mismo |

El modo A **no** es «Claude sin herramientas»: tiene Bash y los datos crudos, como cualquier usuario de Claude Code. Bash permite usar `curl`, así que el modo A podía consultar la API pública del BCRP. No se bloqueó porque la tarea compara Claude Code con y sin los componentes especializados.

## Resultados

| | Modo A | Modo B |
|---|---|---|
| **Respuestas correctas** | **10/10** | **10/10** |
| Incorrectas o sin respuesta | 0 | 0 |
| Tiempo promedio por pregunta | 29.0 s | 34.7 s |
| Tiempo mediano | 22.1 s | 22.9 s |
| Tiempo promedio en preguntas BCRP / ENAHO / combinadas | 17.1 / 23.6 / 63.8 s | 21.3 / 28.3 / 74.5 s |
| Turnos promedio | 6.5 | 6.7 |
| Costo total (10 preguntas) | US$ 0.76 | US$ 1.00 |

| ID | Pregunta | A | B | Cómo llegó B a la respuesta |
|---|---|---|---|---|
| B1 | Inversión regional, Cusco 2024 | ✅ 15.4 s | ✅ 20.2 s | MCP `cuadre_territorial` |
| B2 | Inversión del gobierno nacional, total 2024 | ✅ 22.3 s | ✅ 22.2 s | MCP `cuadre_territorial` |
| B3 | Año máximo de la inversión local de Cajamarca | ✅ 15.0 s | ✅ 19.6 s | MCP `cuadre_territorial` |
| B4 | Exportaciones mineras de Arequipa, 2022 | ✅ 15.8 s | ✅ 23.2 s | MCP `cuadre_territorial` y `buscar_series` |
| E1 | Pobreza de Cajamarca | ✅ 23.2 s | ✅ 22.6 s | Skill `limpiando-enaho` |
| E2 | Pobreza de Lima Metropolitana | ✅ 21.9 s | ✅ 36.4 s | Leyó la skill de limpieza y corrió sus scripts por Bash, **sin invocar la skill** |
| E3 | Pobreza rural | ✅ 20.3 s | ✅ 21.7 s | Skill `limpiando-enaho` |
| E4 | IC 95 % de la pobreza nacional | ✅ 29.0 s | ✅ 32.5 s | Sin invocar skills; **leyó el archivo de referencia del INEI** de `analizando-reparto` y luego **calculó** el IC por su cuenta (26.59–28.57 %) |
| C1 | Cajamarca: % de inversión y % de pobres | ✅ 29.9 s | ✅ 71.3 s | MCP y skill `analizando-reparto` |
| C2 | Los 5 más pobres: % de pobres y % de inversión | ✅ 97.6 s | ✅ 77.7 s | MCP y skill `analizando-reparto` |

**Preguntas que mejoraron o empeoraron:** ninguna cambió de correcta a incorrecta, ni al revés. En tiempo, B fue más lento en 7 de 10 preguntas (sobre todo en C1, por correr la limpieza y el análisis completos) y más rápido en 3: B2 y E1 por décimas de segundo, y C2 (77.7 s frente a 97.6 s), donde A tuvo que reconstruir todo el cruce a mano.

### Pruebas de robustez (`robustez.csv`, `robustez_resultados.csv`)

Cinco pedidos con una trampa definida de antemano (commit `8eff069`):

| ID | Trampa | A | B |
|---|---|---|---|
| R1 | Exportaciones de 2024 por departamento (el BCRP publica hasta 2022) | ✅ | ✅ |
| R2 | Canon minero por departamento (el BCRP solo tiene el nacional) | ✅ | ✅ |
| R3 | «Lima» ambigua y tres niveles de gobierno | ✅ | ✅ (además da la cifra con y sin la Municipalidad Metropolitana) |
| R4 | Pobreza distrital con la ENAHO (no representativa) | ✅ | ✅ |
| R5 | Pregunta causal | ✅ | ✅ |

Ningún modo inventó datos. **Debilidad común en R5:** los dos supusieron que la pobreza de Cajamarca bajó, cuando según el INEI subió de 42.5 % (2020) a 45.0 % (2024).

## Principales hallazgos y errores encontrados

1. **El modo A acertó todo.** Con Bash y los datos crudos, Sonnet descargó la API del BCRP con `curl` y procesó los microdatos de la ENAHO con pandas. Revisamos los registros (`logs/*_A.jsonl`) y no leyó archivos del proyecto fuera de su copia. En este experimento, **la exactitud no distingue a los modos**.
2. **Las skills no se activaron en 2 de 6 preguntas de la ENAHO** (E2 y E4). En E2, Claude leyó la skill y corrió sus scripts por Bash; en E4 resolvió con código propio. Sus descripciones no cubren «Lima Metropolitana» ni «intervalo de confianza»: es una mejora pendiente para `limpiando-enaho`.
3. **El modo B tuvo acceso a cifras de referencia.** `analizando-reparto/referencias/inei_pobreza_2024.csv` forma parte de la skill (lo usa para validar) y contiene cifras oficiales. En E4, Claude lo leyó, lo citó y además calculó el intervalo de forma independiente, con el mismo resultado. La respuesta es correcta, pero no puede contarse como un cálculo a ciegas.
4. **Arranque del MCP.** En la prueba previa, el servidor MCP no alcanzó a conectar en la copia limpia porque `uv` instalaba las dependencias desde cero. Se corrigió usando el entorno ya instalado en los dos modos; la prueba fallida no se cuenta.
5. **Dato con cuadre incompleto.** Las exportaciones mineras por departamento no suman el total oficial en 4 de 5 años (hasta 101.95 millones de US$ en 2022). La herramienta `cuadre_territorial` lo reporta en vez de ocultarlo.
6. **Series mensuales frente a anuales.** En C1 y C2, el modo A sumó las series mensuales del BCRP (total 2020–2024: 226 365 millones de soles) y el modo B usó las anuales (226 627 millones). La diferencia es de 0.1 % y no cambia los porcentajes pedidos, pero muestra que el código improvisado puede elegir otra serie sin advertirlo.

## Revisión de la autora: interpretación de C1 y C2

Las cuatro respuestas cumplen el criterio fijado de antemano: cifras dentro de la tolerancia y conclusión descriptiva, sin afirmar causalidad (`REVISION_HUMANA` en `calificar.py`). La calificación no cambia. Pero la lectura completa muestra una diferencia de calidad que la calificación numérica no captura.

La pregunta de investigación es de **focalización territorial**: si el reparto de la inversión pública entre departamentos guarda relación con la distribución de la **necesidad** (la población pobre) o con la de la **población total**, y cómo cambia esa relación al considerar la **densidad poblacional**. La densidad importa porque la provisión de infraestructura en territorios dispersos tiene costos por habitante más altos, de modo que un mismo nivel de inversión por persona no significa lo mismo en Loreto que en Lima. Es, por tanto, una pregunta sobre **asociación y reparto**, no sobre el efecto de la inversión en la pobreza.

- **Modo A, C2:** responde las cifras, pero organiza su conclusión en torno a la causalidad («no se puede decir que la menor inversión cause la pobreza, ni que más inversión la reduciría»), que no era lo preguntado, y **no considera la densidad**. Tampoco calcula intervalos de confianza: reconoce que el orden entre Pasco y Huánuco «no es firme».
- **Modo B, C1 y C2:** sitúa la respuesta en el marco del reparto. Da la razón inversión/pobres con su intervalo de confianza (Cajamarca 0.60 [0.54–0.68]), la compara con la parte de población y advierte que la inversión por habitante **disminuye con la densidad**, lo que es compatible con mayores costos en zonas dispersas.

La diferencia se explica por el diseño: la skill `analizando-reparto` lleva incorporado el marco de la investigación (participaciones, densidad, intervalos validados), mientras que el modo A reconstruye el análisis desde cero en cada sesión y decide por su cuenta qué es relevante. Para una investigación con un enfoque teórico definido, esta es una ventaja de las skills que la exactitud numérica, igual en ambos modos, no refleja.

## Conclusión sobre la utilidad de MCP y Skills

Con preguntas de cifras puntuales y datos crudos a mano, un modelo actual con Bash llega a las mismas respuestas que con MCP y Skills, y algo más rápido y barato (−16 % de tiempo, −24 % de costo). **La ventaja del MCP y las Skills no se vio en la exactitud, sino en cómo se obtiene la respuesta:**

- **Trazabilidad:** el modo B cita la serie, el periodo y el cuadre contra el total oficial; el código del modo A se escribe cada vez y no queda guardado.
- **Pertinencia:** el modo B responde dentro del marco de la investigación (reparto frente a necesidad y densidad); el modo A tiende a desviarse hacia preguntas que no se hicieron (ver la revisión de la autora).
- **Consistencia y validación:** el modo B usa siempre el mismo método, ya validado contra el INEI (27 ámbitos, IC entre 0.95 y 1.01 veces el oficial); el modo A acertó, pero con un procedimiento distinto en cada sesión.
- **Reutilización:** en la ejecución integrada, las mismas skills produjeron el informe completo y regeneraron salidas idénticas byte a byte.

**Alcance de esta conclusión:** una sola corrida por pregunta, un solo modelo y 10 preguntas. Con preguntas más ambiguas, otro modelo o sin acceso a los microdatos, el resultado podría ser distinto.
