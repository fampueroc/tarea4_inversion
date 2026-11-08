# Ejecución integrada, intento 1 (6-nov-2026)

*Exportado de Claude Code. Datos personales reemplazados por [correo] y [usuario]; recordatorios internos del sistema y razonamiento interno omitidos; resultados largos de herramientas recortados.*

## 👤 Usuaria · 2026-11-06 07:46 UTC

<pasted_content id="73f9">
Pregunta de investigación: entre 2020 y 2024, ¿la inversión pública se repartió entre los departamentos del Perú en proporción a dónde vive la población pobre?

1. Antes de empezar, escribe un plan de análisis breve.
2. Consulta los datos del BCRP con el servidor MCP bcrp: la inversión de los tres niveles de gobierno 2020-2024 y las exportaciones mineras 2018-2022 por departamento (guárdalas para el análisis), y describe la evolución de la inversión del gobierno nacional 2020-2024 con la herramienta resumen.
3. Procesa la ENAHO 2024 y analiza el cruce con las skills del proyecto: limpieza y validación, gráfico de pobreza por departamento, mapa y análisis del reparto.
4. Escribe informes/informe_final.md con: pregunta y delimitación, fuentes y metodología, al menos tres hallazgos con cifras, visualizaciones (un gráfico del BCRP, uno de la ENAHO y el mapa), interpretación, limitaciones y reproducibilidad. Cada cifra debe citar su fuente (código de serie o archivo). No afirmes relaciones causales.
5. Si una herramienta falla o no encuentra datos, dilo en el informe; no inventes cifras.
</pasted_content id="73f9">

### 🤖 Claude · 2026-11-06 07:46 UTC

**Plan de análisis (breve)**
1. **Delimitación:** 25 departamentos, inversión pública 2020–2024 (nacional, regional, local; BCRP) frente a la población pobre 2024 (ENAHO, INEI).
2. **Datos BCRP:** usar `cuadre_territorial` para la inversión de los 3 niveles y las exportaciones mineras 2018–2022, guardarlas en CSV, y `resumen` para la inversión nacional 2020–2024.
3. **ENAHO:** limpiar y validar contra la cifra oficial del INEI; luego el gráfico por departamento y el mapa.
4. **Cruce:** usar la skill `analizando-reparto`, que calcula la proporción de la inversión frente a la de pobres, la curva de concentración, la densidad y la minería, más un recuadro de Lima.
5. **Informe:** cifras con su fuente, sin afirmaciones causales, y registro de cualquier falla.

Empiezo revisando el proyecto.

> 🔧 **Bash** `{"command": "cd \"C:/Users/[usuario]/Documents/GitHub/Python_Interm/Tareas/Tarea_4\"; ls -la; ls analisis informes datos .claude .claude/skills 2>/dev/null; cat CLAUDE.md 2>/dev/null | head -80", "description": "List project structure"}`

> 🔧 **ToolSearch** `{"query": "select:mcp__bcrp__buscar_series,mcp__bcrp__cuadre_territorial,mcp__bcrp__resumen,mcp__bcrp__serie", "max_results": 4}`

<details><summary>Resultado de la herramienta</summary>

```text
[imagen omitida]
[imagen omitida]
[imagen omitida]
[imagen omitida]
```
</details>

<details><summary>Resultado de la herramienta</summary>

```text
total 345
drwxr-xr-x 1 [usuario] 197121      0 Nov  5 07:34 .
drwxr-xr-x 1 [usuario] 197121      0 Nov  5 05:46 ..
drwxr-xr-x 1 [usuario] 197121      0 Nov  6 00:40 .claude
drwxr-xr-x 1 [usuario] 197121      0 Nov  6 00:42 .git
-rw-r--r-- 1 [usuario] 197121    222 Nov  5 06:23 .gitignore
-rw-r--r-- 1 [usuario] 197121    148 Nov  5 06:23 .mcp.json
drwxr-xr-x 1 [usuario] 197121      0 Nov  5 06:25 .pytest_cache
-rw-r--r-- 1 [usuario] 197121      5 Nov  5 06:23 .python-version
drwxr-xr-x 1 [usuario] 197121      0 Nov  5 06:24 .venv
drwxr-xr-x 1 [usuario] 197121      0 Nov  5 07:24 analisis
drwxr-xr-x 1 [usuario] 197121      0 Nov  5 06:23 datos
drwxr-xr-x 1 [usuario] 197121      0 Nov  6 00:33 evaluacion
drwxr-xr-x 1 [usuario] 197121      0 Nov  6 00:42 figuras
drwxr-xr-x 1 [usuario] 197121      0 Nov  6 00:42 mapas
drwxr-xr-x 1 [usuario] 197121      0 Nov  5 07:26 mcp
-rw-r--r-- 1 [usuario] 197121    503 Nov  5 06:23 pyproject.toml
-rw-r--r-- 1 [usuario] 197121    321 Nov  5 06:23 README.md
drwxr-xr-x 1 [usuario] 197121      0 Nov  6 00:42 salidas
-rw-r--r-- 1 [usuario] 197121 311285 Nov  5 06:23 uv.lock
.claude:
settings.local.json
skills

.claude/skills:
analizando-reparto
graficando-enaho
limpiando-enaho
mapeando-enaho

analisis:
explorar_densidad.py
explorar_primeros_numeros.py
validar_ic.py

datos:
966-Modulo02.zip
966-Modulo34.zip
catalogo_bcrp.csv
peru_departamental_simple.geojson
```
</details>

> 🔧 **mcp__bcrp__cuadre_territorial** `{"indicador": "inversion_gobierno_nacional", "desde": "2020", "hasta": "2024", "guardar": true}`

> 🔧 **mcp__bcrp__cuadre_territorial** `{"indicador": "inversion_gobiernos_regionales", "desde": "2020", "hasta": "2024", "guardar": true}`

> 🔧 **mcp__bcrp__cuadre_territorial** `{"indicador": "inversion_gobiernos_locales", "desde": "2020", "hasta": "2024", "guardar": true}`

> 🔧 **mcp__bcrp__cuadre_territorial** `{"indicador": "exportaciones_mineras", "desde": "2018", "hasta": "2022", "guardar": true}`

> 🔧 **mcp__bcrp__buscar_series** `{"texto": "inversión gobierno nacional", "frecuencia": "Anual"}`

<details><summary>Resultado de la herramienta</summary>

```text
{"indicador":"inversion_gobierno_nacional","unidad":"millones S/","desde":"2020","hasta":"2024","archivo":"salidas/bcrp_inversion_gobierno_nacional_2020_2024.csv","departamentos":[{"ubigeo":"01","departamento":"Amazonas","codigo":"RD16657DA","valores":{"2020":276.5268,"2021":366.4044,"2022":378.3099,"2023":319.7982,"2024":366.6491}},{"ubigeo":"02","departamento":"Ancash","codigo":"RD16658DA","valores":{"2020":363.1984,"2021":1183.6009,"2022":1446.7381,"2023":1969.5186,"2024":2170.7433}},{"ubigeo":"03","departamento":"Apurímac","codigo":"RD16659DA","valores":{"2020":206.7772,"2021":285.4108,"2022":220.8129,"2023":243.328,"2024":429.8691}},{"ubigeo":"04","departamento":"Arequipa","codigo":"RD16660DA","valores":{"2020":242.6842,"2021":227.6677,"2022":205.2631,"2023":374.6803,"2024":402.7613}},{"ubigeo":"05","departamento":"Ayacucho","codigo":"RD16661DA","valores":{"2020":164.1632,"2021":210.311,"2022":232.9678,"2023":278.5359,"2024":343.3457}},{"ubigeo":"06","departamento":"Cajamarca","codigo":"RD16662DA","valores":{"2020":438.0903,"2021":389.8662,"2022":373.7625,"2023":548.1467,"2024":710.2005}},{"ubigeo":"07","departamento":"Callao","codigo":"RD16663DA","valores":{"2020":442.4354,"2021":397.5813,"2022":420.2008,"2023":1999.8987,"2024":1123.651}},{"ubigeo":"08","departamento":"Cusco","codigo":"RD16664DA","valores":{"2020":525.9976,"2021":1249.2247,"2022":1335.0485,"2023":1043.4348,"2024":1092.8273}},{"ubigeo":"09","departamento":"Huancavelica","codigo":"RD16665DA","valores":{"2020":164.8894,"2021":190.2178,"2022":202.9339,"2023":276.9674,"2024":289.9444}},{"ubigeo":"10","departamento":"Huánuco","codigo":"RD16666DA","valores":{"2020":335.1137,"2021":445.7,"2022":449.9449,"2023":584.2856,"2024":431.8695}},{"ubigeo":"11","departamento":"Ica","codigo":"RD16667DA","valores":{"2020":259.9606,"2021":218.5873,"2022":300.8419,"2023":509.4954,"2024":933.2119}},{"ubigeo":"12","departamento":"Junín","codigo":"RD16668DA","valores":{"2020":154.139,"2021":311.402,"2022":273.2518,"2023":431.3811,"2024":768.5602}},{"ubigeo":"13","departamento":"La Libertad","codigo":"RD16669DA","valores":{"2020":443.8449,"2021":718.013,"2022":603.9134,"2023":1217.222,"2024":1784.7457}},{"ubigeo":"14","departamento":"Lambayeque","codigo":"RD16670DA","valores":{"2020":407.7408,"2021":600.6063,"2022":487.9084,"2023":355.1256,"2024":540.317}},{"ubigeo":"15","departamento":"Lima","codigo":"RD16671DA","valores":{"2020":5419.8918,"2021":6436.8653,"2022":5588.7663,"2023":8054.5637,"2024":9694.1867}}
… [4636 caracteres más omitidos]
```
</details>

<details><summary>Resultado de la herramienta</summary>

```text
{"indicador":"inversion_gobiernos_regionales","unidad":"millones S/","desde":"2020","hasta":"2024","archivo":"salidas/bcrp_inversion_gobiernos_regionales_2020_2024.csv","departamentos":[{"ubigeo":"01","departamento":"Amazonas","codigo":"RD16709DA","valores":{"2020":289.522,"2021":292.73,"2022":291.7447,"2023":473.486,"2024":364.0841}},{"ubigeo":"02","departamento":"Ancash","codigo":"RD16710DA","valores":{"2020":212.3136,"2021":261.229,"2022":423.6643,"2023":234.027,"2024":278.5222}},{"ubigeo":"03","departamento":"Apurímac","codigo":"RD16711DA","valores":{"2020":224.2683,"2021":246.5242,"2022":425.3323,"2023":325.2981,"2024":341.176}},{"ubigeo":"04","departamento":"Arequipa","codigo":"RD16712DA","valores":{"2020":416.9177,"2021":537.9782,"2022":689.568,"2023":622.8628,"2024":595.8618}},{"ubigeo":"05","departamento":"Ayacucho","codigo":"RD16713DA","valores":{"2020":306.2334,"2021":405.4897,"2022":490.4018,"2023":621.365,"2024":806.2272}},{"ubigeo":"06","departamento":"Cajamarca","codigo":"RD16714DA","valores":{"2020":149.8543,"2021":282.2339,"2022":393.0704,"2023":711.1384,"2024":838.2726}},{"ubigeo":"07","departamento":"Callao","codigo":"RD16733DA","valores":{"2020":85.3209,"2021":111.2235,"2022":257.8998,"2023":114.0023,"2024":186.0276}},{"ubigeo":"08","departamento":"Cusco","codigo":"RD16715DA","valores":{"2020":380.1556,"2021":584.5557,"2022":703.7477,"2023":807.3798,"2024":1061.2261}},{"ubigeo":"09","departamento":"Huancavelica","codigo":"RD16716DA","valores":{"2020":160.7869,"2021":244.0931,"2022":236.7543,"2023":230.7723,"2024":328.072}},{"ubigeo":"10","departamento":"Huánuco","codigo":"RD16717DA","valores":{"2020":249.2156,"2021":264.0245,"2022":182.0313,"2023":357.8534,"2024":411.7711}},{"ubigeo":"11","departamento":"Ica","codigo":"RD16718DA","valores":{"2020":98.3234,"2021":176.1698,"2022":260.5054,"2023":462.3627,"2024":505.3839}},{"ubigeo":"12","departamento":"Junín","codigo":"RD16719DA","valores":{"2020":260.5474,"2021":326.8678,"2022":640.3225,"2023":834.7508,"2024":874.4867}},{"ubigeo":"13","departamento":"La Libertad","codigo":"RD16720DA","valores":{"2020":182.0383,"2021":233.5886,"2022":274.9431,"2023":428.7023,"2024":645.9916}},{"ubigeo":"14","departamento":"Lambayeque","codigo":"RD16721DA","valores":{"2020":267.836,"2021":340.0859,"2022":370.5433,"2023":475.6086,"2024":622.2822}},{"ubigeo":"15","departamento":"Lima","codigo":"RD16732DA","valores":{"2020":352.7798,"2021":199.7024,"2022":275.0213,"2023":275.8836,"2024":412.5831}},{"ubigeo":"
… [5154 caracteres más omitidos]
```
</details>

<details><summary>Resultado de la herramienta</summary>

```text
{"indicador":"inversion_gobiernos_locales","unidad":"millones S/","desde":"2020","hasta":"2024","archivo":"salidas/bcrp_inversion_gobiernos_locales_2020_2024.csv","departamentos":[{"ubigeo":"01","departamento":"Amazonas","codigo":"RD16683DA","valores":{"2020":212.9361,"2021":259.3993,"2022":284.3952,"2023":345.5537,"2024":404.4019}},{"ubigeo":"02","departamento":"Ancash","codigo":"RD16684DA","valores":{"2020":788.4295,"2021":1263.7621,"2022":1939.3126,"2023":1519.7483,"2024":1864.0848}},{"ubigeo":"03","departamento":"Apurímac","codigo":"RD16685DA","valores":{"2020":390.2361,"2021":553.6334,"2022":826.1609,"2023":567.5236,"2024":640.6735}},{"ubigeo":"04","departamento":"Arequipa","codigo":"RD16686DA","valores":{"2020":737.4188,"2021":985.6287,"2022":1503.1077,"2023":1403.5973,"2024":1374.2756}},{"ubigeo":"05","departamento":"Ayacucho","codigo":"RD16687DA","valores":{"2020":665.0274,"2021":795.3103,"2022":769.0524,"2023":673.5344,"2024":584.7176}},{"ubigeo":"06","departamento":"Cajamarca","codigo":"RD16688DA","valores":{"2020":754.8104,"2021":1152.4099,"2022":1291.3988,"2023":1051.7156,"2024":877.2526}},{"ubigeo":"07","departamento":"Callao","codigo":"RD16689DA","valores":{"2020":75.809,"2021":96.1228,"2022":222.8493,"2023":155.5414,"2024":155.0198}},{"ubigeo":"08","departamento":"Cusco","codigo":"RD16690DA","valores":{"2020":1297.0543,"2021":1680.7832,"2022":2912.3834,"2023":3373.2175,"2024":3316.2012}},{"ubigeo":"09","departamento":"Huancavelica","codigo":"RD16691DA","valores":{"2020":319.6446,"2021":437.3948,"2022":434.0298,"2023":379.5637,"2024":332.6106}},{"ubigeo":"10","departamento":"Huánuco","codigo":"RD16692DA","valores":{"2020":349.4145,"2021":430.0008,"2022":506.3246,"2023":380.6272,"2024":405.7314}},{"ubigeo":"11","departamento":"Ica","codigo":"RD16693DA","valores":{"2020":204.0836,"2021":326.9064,"2022":749.6894,"2023":666.2185,"2024":780.7741}},{"ubigeo":"12","departamento":"Junín","codigo":"RD16694DA","valores":{"2020":407.3985,"2021":506.2862,"2022":667.5723,"2023":604.0011,"2024":522.3914}},{"ubigeo":"13","departamento":"La Libertad","codigo":"RD16695DA","valores":{"2020":841.4976,"2021":1199.1659,"2022":1147.9535,"2023":860.0325,"2024":776.6026}},{"ubigeo":"14","departamento":"Lambayeque","codigo":"RD16696DA","valores":{"2020":240.6767,"2021":434.4398,"2022":449.9012,"2023":357.9779,"2024":257.1951}},{"ubigeo":"15","departamento":"Lima","codigo":"RD16697DA","valores":{"2020":1181.804,"2021":1745.0561,"2022":1732.68,"2023":1259.0215,"2024":1
… [4643 caracteres más omitidos]
```
</details>

<details><summary>Resultado de la herramienta</summary>

```text
{"indicador":"exportaciones_mineras","unidad":"millones US$ FOB","desde":"2018","hasta":"2022","archivo":"salidas/bcrp_exportaciones_mineras_2018_2022.csv","departamentos":[{"ubigeo":"01","departamento":"Amazonas","codigo":"RD40961BA","valores":{"2018":0,"2019":0,"2020":0,"2021":0,"2022":0}},{"ubigeo":"02","departamento":"Ancash","codigo":"RD40978BA","valores":{"2018":3687.3858,"2019":3088.8018,"2020":3179.6942,"2021":5512.9923,"2022":4692.9137}},{"ubigeo":"03","departamento":"Apurimac","codigo":"RD40995BA","valores":{"2018":2578.2819,"2019":1931.9264,"2020":2047.6875,"2021":3038.2292,"2022":2050.7672}},{"ubigeo":"04","departamento":"Arequipa","codigo":"RD41012BA","valores":{"2018":4702.4477,"2019":4184.4259,"2020":3416.2094,"2021":4981.9356,"2022":5377.8924}},{"ubigeo":"05","departamento":"Ayacucho","codigo":"RD41029BA","valores":{"2018":326.974,"2019":300.4223,"2020":680.987,"2021":763.0469,"2022":740.8272}},{"ubigeo":"06","departamento":"Cajamarca","codigo":"RD41046BA","valores":{"2018":2445.0967,"2019":2929.7,"2020":1322.223,"2021":1411.4314,"2022":1340.9095}},{"ubigeo":"07","departamento":"Callao","codigo":"RD41063BA","valores":{"2018":2966.7408,"2019":1929.3094,"2020":613.1232,"2021":1502.8063,"2022":1481.2403}},{"ubigeo":"08","departamento":"Cusco","codigo":"RD41080BA","valores":{"2018":2140.6496,"2019":1843.5193,"2020":1768.9058,"2021":2358.7336,"2022":2146.7231}},{"ubigeo":"09","departamento":"Huancavelica","codigo":"RD41097BA","valores":{"2018":18.094,"2019":14.1609,"2020":29.5243,"2021":64.0281,"2022":55.7271}},{"ubigeo":"10","departamento":"Huanuco","codigo":"RD41114BA","valores":{"2018":15.1497,"2019":23.5245,"2020":2.1247,"2021":0,"2022":1.9485}},{"ubigeo":"11","departamento":"Ica","codigo":"RD41131BA","valores":{"2018":943.9206,"2019":1325.4048,"2020":1627.2768,"2021":3901.621,"2022":3540.0866}},{"ubigeo":"12","departamento":"Junín","codigo":"RD41148BA","valores":{"2018":813.1907,"2019":788.2056,"2020":964.7675,"2021":1343.7726,"2022":1540.5113}},{"ubigeo":"13","departamento":"La Libertad","codigo":"RD41165BA","valores":{"2018":1215.6722,"2019":999.5984,"2020":1335.6036,"2021":1773.8677,"2022":2063.7328}},{"ubigeo":"14","departamento":"Lambayeque","codigo":"RD41182BA","valores":{"2018":0,"2019":0,"2020":0,"2021":0,"2022":0}},{"ubigeo":"15","departamento":"Lima","codigo":"RD41199BA","valores":{"2018":3506.2417,"2019":5227.9226,"2020":3412.3977,"2021":4522.7727,"2022":4099.4711}},{"ubigeo":"16","departamento":"Loreto","codigo":"RD41216BA","val
… [4915 caracteres más omitidos]
```
</details>

<details><summary>Resultado de la herramienta</summary>

```text
{"result":[{"codigo":"RD16667DA","nombre":"Inversión bruta fija del gobierno nacional por departamentos (millones S/) - Ica (millones de soles)","categoria":"Sector público","frecuencia":"Anual","inicio":"2008","actualizada":"2026-04-30"},{"codigo":"RD16671DA","nombre":"Inversión bruta fija del gobierno nacional por departamentos (millones S/) - Lima (millones de soles)","categoria":"Sector público","frecuencia":"Anual","inicio":"2008","actualizada":"2026-04-30"},{"codigo":"RD16677DA","nombre":"Inversión bruta fija del gobierno nacional por departamentos (millones S/) - Puno (millones de soles)","categoria":"Sector público","frecuencia":"Anual","inicio":"2008","actualizada":"2026-04-30"},{"codigo":"RD16664DA","nombre":"Inversión bruta fija del gobierno nacional por departamentos (millones S/) - Cusco (millones de soles)","categoria":"Sector público","frecuencia":"Anual","inicio":"2008","actualizada":"2026-04-30"},{"codigo":"RD16668DA","nombre":"Inversión bruta fija del gobierno nacional por departamentos (millones S/) - Junín (millones de soles)","categoria":"Sector público","frecuencia":"Anual","inicio":"2008","actualizada":"2026-04-30"},{"codigo":"RD16675DA","nombre":"Inversión bruta fija del gobierno nacional por departamentos (millones S/) - Pasco (millones de soles)","categoria":"Sector público","frecuencia":"Anual","inicio":"2008","actualizada":"2026-04-30"},{"codigo":"RD16676DA","nombre":"Inversión bruta fija del gobierno nacional por departamentos (millones S/) - Piura (millones de soles)","categoria":"Sector público","frecuencia":"Anual","inicio":"2008","actualizada":"2026-04-30"},{"codigo":"RD16679DA","nombre":"Inversión bruta fija del gobierno nacional por departamentos (millones S/) - Tacna (millones de soles)","categoria":"Sector público","frecuencia":"Anual","inicio":"2008","actualizada":"2026-04-30"},{"codigo":"RD16682DA","nombre":"Inversión bruta fija del gobierno nacional por departamentos (millones S/) - Total (millones de soles)","categoria":"Sector público","frecuencia":"Anual","inicio":"2008","actualizada":"2026-04-30"},{"codigo":"RD16658DA","nombre":"Inversión bruta fija del gobierno nacional por departamentos (millones S/) - Ancash (millones de soles)","categoria":"Sector público","frecuencia":"Anual","inicio":"2008","actualizada":"2026-04-30"}]}
```
</details>

> 🔧 **mcp__bcrp__resumen** `{"codigo": "RD16682DA", "desde": "2020", "hasta": "2024"}`

> 🔧 **Bash** `{"command": "cd \"C:/Users/[usuario]/Documents/GitHub/Python_Interm/Tareas/Tarea_4\"; for s in limpiando-enaho graficando-enaho mapeando-enaho analizando-reparto; do echo \"=== $s\"; ls -R .claude/skills/$s; cat .claude/skills/$s/SKILL.md; done; cat README.md", "description": "Read project skills"}`

<details><summary>Resultado de la herramienta</summary>

```text
{"codigo":"RD16682DA","nombre":"Inversión bruta fija del gobierno nacional por departamentos (millones S/) - Total (millones de soles)","frecuencia":"Anual","n":5,"primero":{"periodo":"2020","valor":12545.73358},"ultimo":{"periodo":"2024","valor":25109.329324},"cambio":12563.5957,"variacion_pct":100.14,"promedio":18753.1496,"maximo":{"periodo":"2024","valor":25109.329324},"minimo":{"periodo":"2020","valor":12545.73358},"fuente":"https://estadisticas.bcrp.gob.pe/estadisticas/series/api/RD16682DA/json/2020/2024"}
```
</details>

<details><summary>Resultado de la herramienta</summary>

```text
=== limpiando-enaho
.claude/skills/limpiando-enaho:
reference.md
scripts
SKILL.md

.claude/skills/limpiando-enaho/scripts:
limpiar.py
resumen.py
---
name: limpiando-enaho
description: Limpia los módulos 34 (sumaria) y 02 (miembros) de la ENAHO 2024 del INEI, arma una base de personas con pobreza y factor de expansión, y la valida contra la cifra oficial. Úsala cuando pidan limpiar, unir o analizar la ENAHO, o cuando pregunten cuál fue la pobreza en el Perú, en un departamento, por área, sexo o edad.
---
# Limpiar la ENAHO

Corre los comandos desde la raíz del repositorio.

1. Si existen `salidas/personas_2024.parquet` y `salidas/validacion.txt`, y este dice `RESULTADO: APROBADO`, pasa al paso 4.
2. Si faltan `datos/966-Modulo34.zip` o `datos/966-Modulo02.zip`, pide al usuario bajarlos del INEI como indica `README.md`. No uses otra fuente.
3. Corre exactamente: `uv run "${CLAUDE_SKILL_DIR}/scripts/limpiar.py" --anio 2024`
4. Lee `salidas/validacion.txt`. Si no dice `RESULTADO: APROBADO`, detente y muestra qué prueba falló. No des ninguna cifra.
5. Para responder una pregunta de pobreza, corre: `uv run "${CLAUDE_SKILL_DIR}/scripts/resumen.py" --por <nacional|departamento|area|lima_metropolitana|sexo|edad>`. No calcules esas cifras de otra forma.
6. Responde con la cifra, el peso usado y la fuente: INEI, ENAHO 2024. Toda cifra va ponderada.
7. Antes de usar una variable que no está en la base, o si dudas sobre un código o un peso, lee [reference.md](reference.md).

Solo 2024 tiene cifras de referencia para validar. Si piden otro año, dilo y no lo limpies con este script.
=== graficando-enaho
.claude/skills/graficando-enaho:
scripts
SKILL.md

.claude/skills/graficando-enaho/scripts:
graficar.py
---
name: graficando-enaho
description: Hace gráficos de barras de la pobreza con la ENAHO 2024 del INEI por área urbana y rural, sexo, grupo de edad o departamento, siempre ponderados y con las mismas reglas. Úsala cuando pidan graficar, comparar o visualizar la pobreza de la ENAHO por área, sexo, edad o departamento (ranking o comparación entre departamentos).
---
# Graficar la ENAHO

Corre los comandos desde la raíz del repositorio.

1. Si no existe `salidas/personas_2024.parquet`, usa primero la skill `limpiando-enaho`.
2. Elige el corte según el pedido y corre exactamente: `uv run "${CLAUDE_SKILL_DIR}/scripts/graficar.py" --por <area|sexo|edad|departamento>`
3. Abre la figura y comprueba que no haya etiquetas cortadas ni superpuestas.
4. Responde con la 
… [6897 caracteres más omitidos]
```
</details>

### 🤖 Claude · 2026-11-06 07:47 UTC

Los cuatro archivos del BCRP están guardados. Paso a la limpieza de la ENAHO.

> 🔧 **Bash** `{"command": "cd \"C:/Users/[usuario]/Documents/GitHub/Python_Interm/Tareas/Tarea_4\"; ls salidas; S=.claude/skills/limpiando-enaho; uv run \"$S/scripts/limpiar.py\" --anio 2024 2>&1 | tail -30; cat salidas/validacion.txt", "description": "Clean ENAHO 2024 and validate", "timeout": 600000}`

<details><summary>Resultado de la herramienta</summary>

```text
bcrp_exportaciones_mineras_2018_2022.csv
bcrp_inversion_gobierno_nacional_2020_2024.csv
bcrp_inversion_gobiernos_locales_2020_2024.csv
bcrp_inversion_gobiernos_regionales_2020_2024.csv
VALIDACIÓN ENAHO 2024

Pobreza monetaria, sumaria (factor07 x mieperho): 27.58 %
Pobreza monetaria, personas (facpob07):           27.53 %
Pobreza extrema, sumaria:                         5.50 %
Pobreza extrema, personas:                        5.50 %
Referencia:                                       27.6 % y 5.5 %

Hogares en la sumaria:   33,691
Filas del módulo 02:     117,721
Residentes habituales:   108,664
Filas de la base final:  108,664

[OK] Llaves de hogar únicas en la sumaria
[OK] Llaves de persona únicas en el módulo 02
[OK] Hogares en la sumaria = 33,691
[OK] Filas del módulo 02 = 117,721
[OK] Residentes habituales = 108,664
[OK] La unión no perdió ni duplicó filas
[OK] Toda persona encontró su hogar
[OK] Ninguna persona sin facpob07
[OK] 25 departamentos en la base
[OK] Pobreza con sumaria a 0.1 de 27.6 %
[OK] Pobreza con personas a 0.1 de 27.6 %
[OK] Pobreza extrema con sumaria a 0.1 de 5.5 %

RESULTADO: APROBADO

Base guardada en salidas\personas_2024.parquet
VALIDACIÓN ENAHO 2024

Pobreza monetaria, sumaria (factor07 x mieperho): 27.58 %
Pobreza monetaria, personas (facpob07):           27.53 %
Pobreza extrema, sumaria:                         5.50 %
Pobreza extrema, personas:                        5.50 %
Referencia:                                       27.6 % y 5.5 %

Hogares en la sumaria:   33,691
Filas del módulo 02:     117,721
Residentes habituales:   108,664
Filas de la base final:  108,664

[OK] Llaves de hogar únicas en la sumaria
[OK] Llaves de persona únicas en el módulo 02
[OK] Hogares en la sumaria = 33,691
[OK] Filas del módulo 02 = 117,721
[OK] Residentes habituales = 108,664
[OK] La unión no perdió ni duplicó filas
[OK] Toda persona encontró su hogar
[OK] Ninguna persona sin facpob07
[OK] 25 departamentos en la base
[OK] Pobreza con sumaria a 0.1 de 27.6 %
[OK] Pobreza con personas a 0.1 de 27.6 %
[OK] Pobreza extrema con sumaria a 0.1 de 5.5 %

RESULTADO: APROBADO
```
</details>

### 🤖 Claude · 2026-11-06 07:47 UTC

Validación aprobada. Corro el gráfico, el mapa y el análisis del reparto.

> 🔧 **Bash** `{"command": "cd \"C:/Users/[usuario]/Documents/GitHub/Python_Interm/Tareas/Tarea_4\"; echo \"=== GRAFICO\"; uv run .claude/skills/graficando-enaho/scripts/graficar.py --por departamento 2>&1 | tail -40; echo \"=== MAPA\"; uv run .claude/skills/mapeando-enaho/scripts/mapear.py 2>&1 | tail -40; echo \"=== REPARTO\"; uv run .claude/skills/analizando-reparto/scripts/analizar.py 2>&1 | tail -20", "description": "Run chart, map and allocation analysis", "timeout": 600000}`

<details><summary>Resultado de la herramienta</summary>

```text
=== GRAFICO
Cajamarca        45.0
Loreto           43.0
Puno             39.9
Pasco            39.0
Huánuco          39.0
Callao           33.9
Huancavelica     33.4
Ayacucho         32.8
Piura            31.9
La Libertad      30.2
Ucayali          27.1
Lima             27.1
Tumbes           26.9
Amazonas         25.7
Tacna            24.0
Apurímac         24.0
Áncash           22.8
San Martín       22.0
Cusco            18.5
Junín            18.5
Arequipa         15.8
Lambayeque       14.0
Madre de Dios    11.1
Moquegua         11.0
Ica               6.0
Peso: factor07 × mieperho
Figura: figuras\pobreza_departamento.png
=== MAPA
25 departamentos con dato. Diferencia máxima con la referencia: 0.05 puntos.
CAJAMARCA        45.0
LORETO           43.0
PUNO             39.9
PASCO            39.0
HUANUCO          39.0
CALLAO           33.9
HUANCAVELICA     33.4
AYACUCHO         32.8
PIURA            31.9
LA LIBERTAD      30.2
UCAYALI          27.1
LIMA             27.1
TUMBES           26.9
AMAZONAS         25.7
TACNA            24.0
APURIMAC         24.0
ANCASH           22.8
SAN MARTIN       22.0
CUSCO            18.5
JUNIN            18.5
AREQUIPA         15.8
LAMBAYEQUE       14.0
MADRE DE DIOS    11.1
MOQUEGUA         11.0
ICA               6.0
Mapa: mapas\pobreza_departamento.png
Comparación con la sesión 16: salidas\mapa_vs_referencia.csv
=== REPARTO

== Hallazgo 2: índices de concentración (orden: de mayor a menor pobreza; negativo = favorece a los más pobres)
  Población pobre: -0.169 | Inversión total: +0.062
  Gobierno nacional: +0.027
  Gobiernos regionales: +0.026
  Gobiernos locales: +0.120

== Hallazgo 3: inversión por habitante según pobreza y densidad (25 departamentos, descriptivo)
  pobreza (por punto): -0.0118 (EE robusto 0.0066; IC 95 % -0.0247 a +0.0012)
  log(densidad): -0.1118 (EE robusto 0.0414; IC 95 % -0.1929 a -0.0307)
  R² = 0.31. Lectura: con igual densidad, +1 punto de pobreza ≈ -1.2 % de inversión por habitante; duplicar la densidad ≈ -7.5 %.

== Complemento: correlación de Spearman entre (inversión / pobres) y % de exportaciones mineras 2018–2022: 0.20 (25 departamentos)

== Recuadro: Lima Metropolitana y Lima provincias
  Lima Metropolitana (provincia de Lima): pobreza 27.6 % [25.0–30.1], 29.8 % de los pobres del país, inversión regional 2020–2024 455 millones S/
  Lima provincias (región Lima): pobreza 21.7 % [18.3–25.1], 2.3 % de los pobres del país, inver
… [254 caracteres más omitidos]
```
</details>

> 🔧 **Bash** `{"command": "cd \"C:/Users/[usuario]/Documents/GitHub/Python_Interm/Tareas/Tarea_4\"; cat salidas/analisis.txt; echo; head -3 salidas/indicadores.csv; uv run python -c \"\nimport pandas as pd; d=pd.read_csv('salidas/indicadores.csv'); pd.set_option('display.width',250); pd.set_option('display.max_columns',40); print(d.columns.tolist()); print(d.to_string())\"; cat salidas/recuadro_lima.csv; head -3 salidas/bcrp_inversion_gobierno_nacional_2020_2024.csv; ls informes 2>/dev/null; ls figuras mapas", "description": "Read analysis outputs"}`

<details><summary>Resultado de la herramienta</summary>

```text
== Datos del BCRP (guardados por la herramienta MCP cuadre_territorial)
  Gobierno nacional: cuadra con el total oficial todos los años; series 26
  Gobiernos regionales: cuadra con el total oficial todos los años; series 27; Municipalidad Metropolitana de Lima asignada a Lima
  Gobiernos locales: cuadra con el total oficial todos los años; series 26
  Total 2020–2024: 226,627 millones S/ corrientes (30,402 en 2020 y 57,945 en 2024)

== ENAHO 2024: validación contra el INEI (Evolución de la Pobreza Monetaria 2015-2024, p. 220)
  27 ámbitos (25 departamentos con Lima dividida en 2, y el nacional): diferencia máxima 0.05 puntos; semiancho del IC 95 % entre 0.95 y 1.01 veces el del INEI

== Hallazgo 1: parte de la inversión frente a parte de los pobres y de la población
  Cajamarca      pobreza 45.0 % | pobres del país  7.36 % [6.50–8.22] | inversión  4.40 % | inv/pobres 0.60 [0.54–0.68] | inv/población 0.98
  Loreto         pobreza 43.0 % | pobres del país  5.10 % [4.48–5.73] | inversión  3.18 % | inv/pobres 0.62 [0.56–0.71] | inv/población 0.97
  Puno           pobreza 39.9 % | pobres del país  6.66 % [5.67–7.66] | inversión  4.36 % | inv/pobres 0.65 [0.57–0.77] | inv/población 0.95
  Pasco          pobreza 39.0 % | pobres del país  1.34 % [1.08–1.61] | inversión  1.21 % | inv/pobres 0.90 [0.75–1.12] | inv/población 1.27
  Huánuco        pobreza 39.0 % | pobres del país  3.80 % [3.21–4.38] | inversión  2.55 % | inv/pobres 0.67 [0.58–0.79] | inv/población 0.95
  Callao         pobreza 33.9 % | pobres del país  4.07 % [3.32–4.82] | inversión  2.58 % | inv/pobres 0.63 [0.53–0.78] | inv/población 0.78
  Huancavelica   pobreza 33.4 % | pobres del país  1.91 % [1.62–2.20] | inversión  1.87 % | inv/pobres 0.98 [0.85–1.15] | inv/población 1.18
  Ayacucho       pobreza 32.8 % | pobres del país  2.67 % [2.24–3.10] | inversión  3.24 % | inv/pobres 1.21 [1.04–1.45] | inv/población 1.44
  Piura          pobreza 31.9 % | pobres del país  6.66 % [5.87–7.45] | inversión  7.15 % | inv/pobres 1.07 [0.96–1.22] | inv/población 1.24
  La Libertad    pobreza 30.2 % | pobres del país  6.61 % [5.72–7.49] | inversión  5.01 % | inv/pobres 0.76 [0.67–0.88] | inv/población 0.83
  Ucayali        pobreza 27.1 % | pobres del país  1.59 % [1.27–1.91] | inversión  1.60 % | inv/pobres 1.00 [0.84–1.26] | inv/población 0.99
  Lima           pobreza 27.1 % | pobres del país 32.11 % [29.54–34.67] | inversión 19.77 % | inv/pobres 0.62 [0.57–0.67] | inv/población 0.60
  Tumb
… [18722 caracteres más omitidos]
```
</details>

### 🤖 Claude · 2026-11-06 07:48 UTC

Las skills piden revisar las figuras, así que las abro.

> 🔧 **Read** `{"file_path": "C:\\Users\\[usuario]\\Documents\\GitHub\\Python_Interm\\Tareas\\Tarea_4\\figuras\\bcrp_inversion_anual.png"}`

<details><summary>Resultado de la herramienta</summary>

```text
[imagen omitida]
```
</details>

> 🔧 **Read** `{"file_path": "C:\\Users\\[usuario]\\Documents\\GitHub\\Python_Interm\\Tareas\\Tarea_4\\figuras\\pobreza_departamento.png"}`

<details><summary>Resultado de la herramienta</summary>

```text
[imagen omitida]
```
</details>

> 🔧 **Read** `{"file_path": "C:\\Users\\[usuario]\\Documents\\GitHub\\Python_Interm\\Tareas\\Tarea_4\\mapas\\pobreza_departamento.png"}`

<details><summary>Resultado de la herramienta</summary>

```text
[imagen omitida]
```
</details>

> 🔧 **Read** `{"file_path": "C:\\Users\\[usuario]\\Documents\\GitHub\\Python_Interm\\Tareas\\Tarea_4\\figuras\\inversion_vs_pobres.png"}`

<details><summary>Resultado de la herramienta</summary>

```text
[imagen omitida]
```
</details>

### 🤖 Claude · 2026-11-06 07:48 UTC

Las cuatro figuras se ven bien: no hay etiquetas cortadas y los 25 departamentos del mapa tienen color. Escribo el informe.

> 🔧 **Write** `{"file_path": "C:\\Users\\[usuario]\\Documents\\GitHub\\Python_Interm\\Tareas\\Tarea_4\\informes\\informe_final.md", "content": "# ¿La inversión pública se reparte donde vive la población pobre? Perú, 2020–2024\n\n*Informe final, Tarea 4. Fiorella Ampuero, con Claude Code. Fecha: 6 de noviembre de 2026.*\n\n## 1. Pregunta y delimitación\n\n**Pregunta.** Entre 2020 y 2024, ¿la inversión pública se repartió entre los departamentos del Perú en proporción a dónde vive la población pobre?\n\n**Delimitación.**\n\n- **Unidad:** los 25 departamentos que publica el BCRP, con Lima y Callao por separado. Lima se trata como un solo departamento, como lo publica el BCRP. Un recuadro separa Lima Metropolitana y Lima provincias solo donde la fuente lo permite.\n- **Inversión:** inversión bruta fija del gobierno nacional, los gobiernos regionales y los gobiernos locales, acumulada 2020–2024, en millones de soles corrientes (BCRP).\n- **Pobreza:** pobreza monetaria 2024 y participación de cada departamento en el total de pobres del país (INEI, ENAHO 2024).\n- **Comparación:** se compara la *parte* de la inversión de cada departamento con su *parte* de los pobres. Un cociente de 1 significa que recibe la misma parte de inversión que su parte de pobres.\n- **Alcance:** el estudio es descriptivo. Compara dos repartos y no afirma que la inversión cause ni reduzca la pobreza, ni que un gobierno sea eficiente o ineficiente.\n\n## 2. Fuentes y metodología\n\n### Fuentes\n\n| Fuente | Contenido | Archivo guardado |\n|---|---|---|\n| BCRP, inversión bruta fija del gobierno nacional por departamentos (series ʼRD16657DAʼ–ʼRD16681DAʼ; total ʼRD16682DAʼ) | 2020–2024, millones S/ | ʼsalidas/bcrp_inversion_gobierno_nacional_2020_2024.csvʼ |\n| BCRP, inversión de los gobiernos regionales por departamentos (series ʼRD16709DAʼ–ʼRD16733DAʼ; Municipalidad Metropolitana de Lima ʼRD16734DAʼ) | 2020–2024, millones S/ | ʼsalidas/bcrp_inversion_gobiernos_regionales_2020_2024.csvʼ |\n| BCRP, inversión de los gobiernos locales por departamentos (series ʼRD16683DAʼ–ʼRD16707DAʼ) | 2020–2024, millones S/ | ʼsalidas/bcrp_inversion_gobiernos_locales_2020_2024.csvʼ |\n| BCRP, exportaciones mineras por departamento (series ʼRD40961BAʼ–ʼRD41369BAʼ; «sin ubigeo» ʼRD41386BAʼ; total ʼPM40047BAʼ) | 2018–2022, millones US$ FOB | ʼsalidas/bcrp_exportaciones_mineras_2018_2022.csvʼ |\n| INEI, ENAHO 2024, módulos 34 (sumaria) y 02 (miembros del hogar) | Pobreza monetaria | ʼdatos/966-Modulo34.zipʼ, ʼdatos/966-Modulo
… [14977 caracteres más omitidos]`

<details><summary>Resultado de la herramienta</summary>

```text
File created successfully at: C:\Users\[usuario]\Documents\GitHub\Python_Interm\Tareas\Tarea_4\informes\informe_final.md (file state is current in your context — no need to Read it back)
```
</details>

### 🤖 Claude · 2026-11-06 07:49 UTC

Compruebo que `PM40047BA` sea de verdad el total de exportaciones mineras que cité.

> 🔧 **mcp__bcrp__serie** `{"codigo": "PM40047BA", "desde": "2018", "hasta": "2018"}`

<details><summary>Resultado de la herramienta</summary>

```text
{"codigo":"PM40047BA","nombre":"Exportaciones por Grupo de Productos (valores FOB millones US$) - Productos Tradicionales - Mineros","frecuencia":"Anual","datos":[{"periodo":"2018","valor":28904.4160093611}],"fuente":"https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PM40047BA/json/2018/2018"}
```
</details>

### 🤖 Claude · 2026-11-06 07:49 UTC

Escribí `informes/informe_final.md`. La respuesta corta es **no**: entre 2020 y 2024 la inversión pública se repartió más según dónde vive la población que según dónde viven los pobres. Todas las validaciones pasaron y ninguna herramienta falló.

**Hallazgos principales**
1. **Los departamentos más pobres reciben menos de lo que les tocaría.** Cajamarca, Loreto, Puno, Pasco y Huánuco tienen el 24.3 % de los pobres del país, pero recibieron el 15.7 % de la inversión, casi lo mismo que su parte de la población (16.0 %). En 7 departamentos la inversión queda claramente por debajo de su parte de pobres: el intervalo de confianza del 95 % del cociente queda entero por debajo de 1. Entre ellos está Lima, con el 32.1 % de los pobres y el 19.8 % de la inversión. En el otro extremo, Moquegua recibió 7.5 veces su parte de pobres e Ica 5.3 veces.
2. **La inversión se inclina levemente hacia los departamentos menos pobres.** Su índice de concentración es +0.062, frente a −0.169 de la población pobre (un valor negativo indica que se concentra en los más pobres). Ningún nivel de gobierno da negativo, y los gobiernos locales son los que más se alejan (+0.120).
3. **La densidad pesa más que la pobreza en la inversión por habitante.** Duplicar la densidad va con unos 7.5 % menos de inversión por habitante. El efecto de la pobreza no se distingue de cero (intervalo de −0.0247 a +0.0012).

**Contexto y validaciones**
- La inversión del gobierno nacional (serie `RD16682DA`, herramienta `resumen`) pasó de 12,545.7 a 25,109.3 millones de soles, un +100.14 % en soles sin ajustar por inflación.
- La ENAHO dio 27.58 % de pobreza nacional, frente a 27.6 % oficial. Por departamento, la diferencia máxima con el INEI es de 0.05 puntos.
- La inversión de los tres niveles de gobierno cuadra con el total oficial del BCRP en todos los años.

**Problema de datos:** la herramienta del BCRP avisó que las exportaciones mineras por departamento no suman el total oficial en 2018, 2019, 2020 y 2022; la mayor diferencia sin explicar es de 101.95 millones de dólares en 2022. Lo dejé tal cual y lo puse en las limitaciones, sin corregir ni rellenar cifras. Por eso el dato de minería, una relación débil de 0.20 con el reparto, es solo aproximado.

**Archivos regenerados:** los que `git status` mostraba como borrados en `figuras/`, `mapas/` y `salidas/` volvieron a crearse al correr las skills. No hice commit.

El informe incluye el gráfico del BCRP, el de la ENAHO y el mapa, más otras tres figuras del análisis. No hay afirmaciones causales y cada cifra cita su código de serie o archivo.

## 👤 Usuaria · 2026-11-06 08:09 UTC

quiero tomarle captura 9. 📸 Captura: las skills
Cuando aparezcan líneas como Skill(limpiando-enaho) o Skill(analizando-reparto).

### 🤖 Claude · 2026-11-06 08:09 UTC

No hubo líneas `Skill(...)` porque corrí los scripts de las skills directamente con Bash, sin usar la herramienta Skill. Las invoco ahora para que aparezcan en pantalla y puedas tomar la captura. Los resultados serán los mismos.

> 🔧 **Skill** `{"skill": "limpiando-enaho"}`

<details><summary>Resultado de la herramienta</summary>

```text
Launching skill: limpiando-enaho
```
</details>

> 🔧 **Skill** `{"skill": "graficando-enaho", "args": "--por departamento"}`

<details><summary>Resultado de la herramienta</summary>

```text
Launching skill: graficando-enaho
```
</details>

> 🔧 **Skill** `{"skill": "mapeando-enaho"}`

<details><summary>Resultado de la herramienta</summary>

```text
Launching skill: mapeando-enaho
```
</details>

> 🔧 **Skill** `{"skill": "analizando-reparto"}`

<details><summary>Resultado de la herramienta</summary>

```text
Launching skill: analizando-reparto
```
</details>

### 🤖 Claude · 2026-11-06 08:09 UTC

Sigo los pasos de cada skill: la limpieza ya está aprobada, así que paso al paso 4, y luego corro el gráfico, el mapa y el análisis.

> 🔧 **Bash** `{"command": "cd \"C:/Users/[usuario]/Documents/GitHub/Python_Interm/Tareas/Tarea_4\"; grep \"RESULTADO\" salidas/validacion.txt; echo \"=== GRAFICO\"; uv run \"C:/Users/[usuario]/Documents/GitHub/Python_Interm/Tareas/Tarea_4/.claude/skills/graficando-enaho/scripts/graficar.py\" --por departamento 2>&1 | tail -3; echo \"=== MAPA\"; uv run \"C:/Users/[usuario]/Documents/GitHub/Python_Interm/Tareas/Tarea_4/.claude/skills/mapeando-enaho/scripts/mapear.py\" 2>&1 | sed -n '1p;$p'; echo \"=== REPARTO\"; uv run \"C:/Users/[usuario]/Documents/GitHub/Python_Interm/Tareas/Tarea_4/.claude/skills/analizando-reparto/scripts/analizar.py\" 2>&1 | tail -1", "description": "Run skill steps: validation, chart, map, analysis", "timeout": 600000}`

<details><summary>Resultado de la herramienta</summary>

```text
RESULTADO: APROBADO
=== GRAFICO
Ica               6.0
Peso: factor07 × mieperho
Figura: figuras\pobreza_departamento.png
=== MAPA
25 departamentos con dato. Diferencia máxima con la referencia: 0.05 puntos.
Comparación con la sesión 16: salidas\mapa_vs_referencia.csv
=== REPARTO
Guardado: salidas/indicadores.csv, salidas/recuadro_lima.csv, salidas/analisis.txt y 4 figuras en figuras/
```
</details>

### 🤖 Claude · 2026-11-06 08:09 UTC

Ya aparecen en la terminal las cuatro líneas `Skill(...)` justo encima de este mensaje: `limpiando-enaho`, `graficando-enaho`, `mapeando-enaho` y `analizando-reparto`. Puedes tomar la captura 9 ahora.

En la primera corrida usé los scripts de las skills directamente con Bash, sin la herramienta Skill. Por eso esas líneas no salieron antes. Ahora las invoqué y seguí sus pasos:

- **Limpieza:** `salidas/validacion.txt` dice `RESULTADO: APROBADO`, así que no hizo falta volver a limpiar la ENAHO.
- **Gráfico:** se regeneró `figuras/pobreza_departamento.png`.
- **Mapa:** se regeneró `mapas/pobreza_departamento.png` con los 25 departamentos. La diferencia máxima con la referencia es de 0.05 puntos.
- **Reparto:** se regeneraron `salidas/analisis.txt`, los otros archivos de `salidas/` y las 4 figuras en `figuras/`.

Las cifras son las mismas de antes, así que `informes/informe_final.md` no cambia.

## 👤 Usuaria · 2026-11-06 08:12 UTC

11. 📸 Captura 4: el final
Cuando Claude diga que terminó y escribió informes/informe_final.md.

### 🤖 Claude · 2026-11-06 08:13 UTC

Terminé: el informe está escrito en **`informes/informe_final.md`**. Cumple los cinco puntos del pedido:

1. **Plan de análisis:** lo escribí antes de empezar.
2. **Datos del BCRP:**
   - Bajé con `cuadre_territorial` la inversión de los tres niveles de gobierno (2020–2024) y las exportaciones mineras (2018–2022). Están guardadas en `salidas/bcrp_*.csv`.
   - Con `resumen` sobre la serie `RD16682DA`, la inversión del gobierno nacional pasó de 12,545.7 a 25,109.3 millones de soles, un +100.14 %.
3. **ENAHO 2024:** corrí las skills `limpiando-enaho`, `graficando-enaho`, `mapeando-enaho` y `analizando-reparto`. La validación salió `APROBADO`: 27.58 % de pobreza, frente a 27.6 % del INEI.
4. **Contenido del informe:**
   - pregunta y delimitación, fuentes y metodología;
   - tres hallazgos con cifras, más un complemento de minería y un recuadro de Lima;
   - 6 figuras, entre ellas el gráfico del BCRP, el de la ENAHO y el mapa;
   - interpretación, limitaciones y reproducibilidad.

   Cada cifra cita su código de serie o su archivo, y no hay afirmaciones causales.
5. **Fallas:** ninguna herramienta falló. El único problema fue que las exportaciones mineras por departamento no suman el total oficial en 2018, 2019, 2020 y 2022. Lo dejé tal cual y lo explico en las limitaciones, sin corregir ni rellenar cifras.

**Conclusión:** entre 2020 y 2024 la inversión pública no se repartió en proporción a dónde vive la población pobre. Los cinco departamentos más pobres tienen el 24.3 % de los pobres del país y recibieron el 15.7 % de la inversión.

## 👤 Usuaria · 2026-11-06 08:15 UTC

8. 📸 Captura 2: el MCP
Cuando aparezcan líneas con bcrp - cuadre_territorial o bcrp - resumen.

### 🤖 Claude · 2026-11-06 08:15 UTC

Esas líneas salieron al principio de la sesión, pero ya quedaron muy arriba en la terminal. Vuelvo a hacer las mismas consultas al servidor MCP `bcrp` para que se vean ahora.

> 🔧 **mcp__bcrp__cuadre_territorial** `{"indicador": "inversion_gobierno_nacional", "desde": "2020", "hasta": "2024", "guardar": true}`

> 🔧 **mcp__bcrp__cuadre_territorial** `{"indicador": "inversion_gobiernos_regionales", "desde": "2020", "hasta": "2024", "guardar": true}`

> 🔧 **mcp__bcrp__cuadre_territorial** `{"indicador": "inversion_gobiernos_locales", "desde": "2020", "hasta": "2024", "guardar": true}`

> 🔧 **mcp__bcrp__cuadre_territorial** `{"indicador": "exportaciones_mineras", "desde": "2018", "hasta": "2022", "guardar": true}`

> 🔧 **mcp__bcrp__resumen** `{"codigo": "RD16682DA", "desde": "2020", "hasta": "2024"}`

<details><summary>Resultado de la herramienta</summary>

```text
{"indicador":"inversion_gobierno_nacional","unidad":"millones S/","desde":"2020","hasta":"2024","archivo":"salidas/bcrp_inversion_gobierno_nacional_2020_2024.csv","departamentos":[{"ubigeo":"01","departamento":"Amazonas","codigo":"RD16657DA","valores":{"2020":276.5268,"2021":366.4044,"2022":378.3099,"2023":319.7982,"2024":366.6491}},{"ubigeo":"02","departamento":"Ancash","codigo":"RD16658DA","valores":{"2020":363.1984,"2021":1183.6009,"2022":1446.7381,"2023":1969.5186,"2024":2170.7433}},{"ubigeo":"03","departamento":"Apurímac","codigo":"RD16659DA","valores":{"2020":206.7772,"2021":285.4108,"2022":220.8129,"2023":243.328,"2024":429.8691}},{"ubigeo":"04","departamento":"Arequipa","codigo":"RD16660DA","valores":{"2020":242.6842,"2021":227.6677,"2022":205.2631,"2023":374.6803,"2024":402.7613}},{"ubigeo":"05","departamento":"Ayacucho","codigo":"RD16661DA","valores":{"2020":164.1632,"2021":210.311,"2022":232.9678,"2023":278.5359,"2024":343.3457}},{"ubigeo":"06","departamento":"Cajamarca","codigo":"RD16662DA","valores":{"2020":438.0903,"2021":389.8662,"2022":373.7625,"2023":548.1467,"2024":710.2005}},{"ubigeo":"07","departamento":"Callao","codigo":"RD16663DA","valores":{"2020":442.4354,"2021":397.5813,"2022":420.2008,"2023":1999.8987,"2024":1123.651}},{"ubigeo":"08","departamento":"Cusco","codigo":"RD16664DA","valores":{"2020":525.9976,"2021":1249.2247,"2022":1335.0485,"2023":1043.4348,"2024":1092.8273}},{"ubigeo":"09","departamento":"Huancavelica","codigo":"RD16665DA","valores":{"2020":164.8894,"2021":190.2178,"2022":202.9339,"2023":276.9674,"2024":289.9444}},{"ubigeo":"10","departamento":"Huánuco","codigo":"RD16666DA","valores":{"2020":335.1137,"2021":445.7,"2022":449.9449,"2023":584.2856,"2024":431.8695}},{"ubigeo":"11","departamento":"Ica","codigo":"RD16667DA","valores":{"2020":259.9606,"2021":218.5873,"2022":300.8419,"2023":509.4954,"2024":933.2119}},{"ubigeo":"12","departamento":"Junín","codigo":"RD16668DA","valores":{"2020":154.139,"2021":311.402,"2022":273.2518,"2023":431.3811,"2024":768.5602}},{"ubigeo":"13","departamento":"La Libertad","codigo":"RD16669DA","valores":{"2020":443.8449,"2021":718.013,"2022":603.9134,"2023":1217.222,"2024":1784.7457}},{"ubigeo":"14","departamento":"Lambayeque","codigo":"RD16670DA","valores":{"2020":407.7408,"2021":600.6063,"2022":487.9084,"2023":355.1256,"2024":540.317}},{"ubigeo":"15","departamento":"Lima","codigo":"RD16671DA","valores":{"2020":5419.8918,"2021":6436.8653,"2022":5588.7663,"2023":8054.5637,"2024":9694.1867}}
… [4636 caracteres más omitidos]
```
</details>

<details><summary>Resultado de la herramienta</summary>

```text
{"indicador":"inversion_gobiernos_regionales","unidad":"millones S/","desde":"2020","hasta":"2024","archivo":"salidas/bcrp_inversion_gobiernos_regionales_2020_2024.csv","departamentos":[{"ubigeo":"01","departamento":"Amazonas","codigo":"RD16709DA","valores":{"2020":289.522,"2021":292.73,"2022":291.7447,"2023":473.486,"2024":364.0841}},{"ubigeo":"02","departamento":"Ancash","codigo":"RD16710DA","valores":{"2020":212.3136,"2021":261.229,"2022":423.6643,"2023":234.027,"2024":278.5222}},{"ubigeo":"03","departamento":"Apurímac","codigo":"RD16711DA","valores":{"2020":224.2683,"2021":246.5242,"2022":425.3323,"2023":325.2981,"2024":341.176}},{"ubigeo":"04","departamento":"Arequipa","codigo":"RD16712DA","valores":{"2020":416.9177,"2021":537.9782,"2022":689.568,"2023":622.8628,"2024":595.8618}},{"ubigeo":"05","departamento":"Ayacucho","codigo":"RD16713DA","valores":{"2020":306.2334,"2021":405.4897,"2022":490.4018,"2023":621.365,"2024":806.2272}},{"ubigeo":"06","departamento":"Cajamarca","codigo":"RD16714DA","valores":{"2020":149.8543,"2021":282.2339,"2022":393.0704,"2023":711.1384,"2024":838.2726}},{"ubigeo":"07","departamento":"Callao","codigo":"RD16733DA","valores":{"2020":85.3209,"2021":111.2235,"2022":257.8998,"2023":114.0023,"2024":186.0276}},{"ubigeo":"08","departamento":"Cusco","codigo":"RD16715DA","valores":{"2020":380.1556,"2021":584.5557,"2022":703.7477,"2023":807.3798,"2024":1061.2261}},{"ubigeo":"09","departamento":"Huancavelica","codigo":"RD16716DA","valores":{"2020":160.7869,"2021":244.0931,"2022":236.7543,"2023":230.7723,"2024":328.072}},{"ubigeo":"10","departamento":"Huánuco","codigo":"RD16717DA","valores":{"2020":249.2156,"2021":264.0245,"2022":182.0313,"2023":357.8534,"2024":411.7711}},{"ubigeo":"11","departamento":"Ica","codigo":"RD16718DA","valores":{"2020":98.3234,"2021":176.1698,"2022":260.5054,"2023":462.3627,"2024":505.3839}},{"ubigeo":"12","departamento":"Junín","codigo":"RD16719DA","valores":{"2020":260.5474,"2021":326.8678,"2022":640.3225,"2023":834.7508,"2024":874.4867}},{"ubigeo":"13","departamento":"La Libertad","codigo":"RD16720DA","valores":{"2020":182.0383,"2021":233.5886,"2022":274.9431,"2023":428.7023,"2024":645.9916}},{"ubigeo":"14","departamento":"Lambayeque","codigo":"RD16721DA","valores":{"2020":267.836,"2021":340.0859,"2022":370.5433,"2023":475.6086,"2024":622.2822}},{"ubigeo":"15","departamento":"Lima","codigo":"RD16732DA","valores":{"2020":352.7798,"2021":199.7024,"2022":275.0213,"2023":275.8836,"2024":412.5831}},{"ubigeo":"
… [5154 caracteres más omitidos]
```
</details>

<details><summary>Resultado de la herramienta</summary>

```text
{"indicador":"inversion_gobiernos_locales","unidad":"millones S/","desde":"2020","hasta":"2024","archivo":"salidas/bcrp_inversion_gobiernos_locales_2020_2024.csv","departamentos":[{"ubigeo":"01","departamento":"Amazonas","codigo":"RD16683DA","valores":{"2020":212.9361,"2021":259.3993,"2022":284.3952,"2023":345.5537,"2024":404.4019}},{"ubigeo":"02","departamento":"Ancash","codigo":"RD16684DA","valores":{"2020":788.4295,"2021":1263.7621,"2022":1939.3126,"2023":1519.7483,"2024":1864.0848}},{"ubigeo":"03","departamento":"Apurímac","codigo":"RD16685DA","valores":{"2020":390.2361,"2021":553.6334,"2022":826.1609,"2023":567.5236,"2024":640.6735}},{"ubigeo":"04","departamento":"Arequipa","codigo":"RD16686DA","valores":{"2020":737.4188,"2021":985.6287,"2022":1503.1077,"2023":1403.5973,"2024":1374.2756}},{"ubigeo":"05","departamento":"Ayacucho","codigo":"RD16687DA","valores":{"2020":665.0274,"2021":795.3103,"2022":769.0524,"2023":673.5344,"2024":584.7176}},{"ubigeo":"06","departamento":"Cajamarca","codigo":"RD16688DA","valores":{"2020":754.8104,"2021":1152.4099,"2022":1291.3988,"2023":1051.7156,"2024":877.2526}},{"ubigeo":"07","departamento":"Callao","codigo":"RD16689DA","valores":{"2020":75.809,"2021":96.1228,"2022":222.8493,"2023":155.5414,"2024":155.0198}},{"ubigeo":"08","departamento":"Cusco","codigo":"RD16690DA","valores":{"2020":1297.0543,"2021":1680.7832,"2022":2912.3834,"2023":3373.2175,"2024":3316.2012}},{"ubigeo":"09","departamento":"Huancavelica","codigo":"RD16691DA","valores":{"2020":319.6446,"2021":437.3948,"2022":434.0298,"2023":379.5637,"2024":332.6106}},{"ubigeo":"10","departamento":"Huánuco","codigo":"RD16692DA","valores":{"2020":349.4145,"2021":430.0008,"2022":506.3246,"2023":380.6272,"2024":405.7314}},{"ubigeo":"11","departamento":"Ica","codigo":"RD16693DA","valores":{"2020":204.0836,"2021":326.9064,"2022":749.6894,"2023":666.2185,"2024":780.7741}},{"ubigeo":"12","departamento":"Junín","codigo":"RD16694DA","valores":{"2020":407.3985,"2021":506.2862,"2022":667.5723,"2023":604.0011,"2024":522.3914}},{"ubigeo":"13","departamento":"La Libertad","codigo":"RD16695DA","valores":{"2020":841.4976,"2021":1199.1659,"2022":1147.9535,"2023":860.0325,"2024":776.6026}},{"ubigeo":"14","departamento":"Lambayeque","codigo":"RD16696DA","valores":{"2020":240.6767,"2021":434.4398,"2022":449.9012,"2023":357.9779,"2024":257.1951}},{"ubigeo":"15","departamento":"Lima","codigo":"RD16697DA","valores":{"2020":1181.804,"2021":1745.0561,"2022":1732.68,"2023":1259.0215,"2024":1
… [4643 caracteres más omitidos]
```
</details>

<details><summary>Resultado de la herramienta</summary>

```text
{"indicador":"exportaciones_mineras","unidad":"millones US$ FOB","desde":"2018","hasta":"2022","archivo":"salidas/bcrp_exportaciones_mineras_2018_2022.csv","departamentos":[{"ubigeo":"01","departamento":"Amazonas","codigo":"RD40961BA","valores":{"2018":0,"2019":0,"2020":0,"2021":0,"2022":0}},{"ubigeo":"02","departamento":"Ancash","codigo":"RD40978BA","valores":{"2018":3687.3858,"2019":3088.8018,"2020":3179.6942,"2021":5512.9923,"2022":4692.9137}},{"ubigeo":"03","departamento":"Apurimac","codigo":"RD40995BA","valores":{"2018":2578.2819,"2019":1931.9264,"2020":2047.6875,"2021":3038.2292,"2022":2050.7672}},{"ubigeo":"04","departamento":"Arequipa","codigo":"RD41012BA","valores":{"2018":4702.4477,"2019":4184.4259,"2020":3416.2094,"2021":4981.9356,"2022":5377.8924}},{"ubigeo":"05","departamento":"Ayacucho","codigo":"RD41029BA","valores":{"2018":326.974,"2019":300.4223,"2020":680.987,"2021":763.0469,"2022":740.8272}},{"ubigeo":"06","departamento":"Cajamarca","codigo":"RD41046BA","valores":{"2018":2445.0967,"2019":2929.7,"2020":1322.223,"2021":1411.4314,"2022":1340.9095}},{"ubigeo":"07","departamento":"Callao","codigo":"RD41063BA","valores":{"2018":2966.7408,"2019":1929.3094,"2020":613.1232,"2021":1502.8063,"2022":1481.2403}},{"ubigeo":"08","departamento":"Cusco","codigo":"RD41080BA","valores":{"2018":2140.6496,"2019":1843.5193,"2020":1768.9058,"2021":2358.7336,"2022":2146.7231}},{"ubigeo":"09","departamento":"Huancavelica","codigo":"RD41097BA","valores":{"2018":18.094,"2019":14.1609,"2020":29.5243,"2021":64.0281,"2022":55.7271}},{"ubigeo":"10","departamento":"Huanuco","codigo":"RD41114BA","valores":{"2018":15.1497,"2019":23.5245,"2020":2.1247,"2021":0,"2022":1.9485}},{"ubigeo":"11","departamento":"Ica","codigo":"RD41131BA","valores":{"2018":943.9206,"2019":1325.4048,"2020":1627.2768,"2021":3901.621,"2022":3540.0866}},{"ubigeo":"12","departamento":"Junín","codigo":"RD41148BA","valores":{"2018":813.1907,"2019":788.2056,"2020":964.7675,"2021":1343.7726,"2022":1540.5113}},{"ubigeo":"13","departamento":"La Libertad","codigo":"RD41165BA","valores":{"2018":1215.6722,"2019":999.5984,"2020":1335.6036,"2021":1773.8677,"2022":2063.7328}},{"ubigeo":"14","departamento":"Lambayeque","codigo":"RD41182BA","valores":{"2018":0,"2019":0,"2020":0,"2021":0,"2022":0}},{"ubigeo":"15","departamento":"Lima","codigo":"RD41199BA","valores":{"2018":3506.2417,"2019":5227.9226,"2020":3412.3977,"2021":4522.7727,"2022":4099.4711}},{"ubigeo":"16","departamento":"Loreto","codigo":"RD41216BA","val
… [4915 caracteres más omitidos]
```
</details>

<details><summary>Resultado de la herramienta</summary>

```text
{"codigo":"RD16682DA","nombre":"Inversión bruta fija del gobierno nacional por departamentos (millones S/) - Total (millones de soles)","frecuencia":"Anual","n":5,"primero":{"periodo":"2020","valor":12545.73358},"ultimo":{"periodo":"2024","valor":25109.329324},"cambio":12563.5957,"variacion_pct":100.14,"promedio":18753.1496,"maximo":{"periodo":"2024","valor":25109.329324},"minimo":{"periodo":"2020","valor":12545.73358},"fuente":"https://estadisticas.bcrp.gob.pe/estadisticas/series/api/RD16682DA/json/2020/2024"}
```
</details>

### 🤖 Claude · 2026-11-06 08:15 UTC

Justo encima de este mensaje se ven ahora las cinco llamadas al servidor MCP `bcrp`, listas para la captura 2.

| Llamada | Periodo | Resultado |
|---|---|---|
| `bcrp - cuadre_territorial` · `inversion_gobierno_nacional` | 2020–2024 | Cuadra todos los años |
| `bcrp - cuadre_territorial` · `inversion_gobiernos_regionales` | 2020–2024 | Cuadra todos los años; la diferencia es la Municipalidad Metropolitana de Lima |
| `bcrp - cuadre_territorial` · `inversion_gobiernos_locales` | 2020–2024 | Cuadra todos los años |
| `bcrp - cuadre_territorial` · `exportaciones_mineras` | 2018–2022 | No cuadra en 2018, 2019, 2020 ni 2022, como dice el informe |
| `bcrp - resumen` · `RD16682DA` | 2020–2024 | De 12,545.7 a 25,109.3 millones de soles, +100.14 % |

Las cuatro llamadas de `cuadre_territorial` usaron `guardar=True`, así que volvieron a escribir los CSV de `salidas/`. Los datos son los mismos de la primera vez, así que el análisis y `informes/informe_final.md` no cambian.

