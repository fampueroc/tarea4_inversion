# Prompt informe y recurso bcrp://serie/RD16682DA del MCP desde Claude Code (8-nov-2026)

*Exportado de Claude Code. Datos personales reemplazados por [correo] y [usuario]; recordatorios internos del sistema y razonamiento interno omitidos; resultados largos de herramientas recortados.*

## 👤 Usuaria · 2026-11-08 18:17 UTC

/mcp__bcrp__informe inversión pública por departamento

<details open><summary>Texto que devuelve el prompt del servidor MCP</summary>

```text
Escribe un informe de cinco viñetas sobre «inversión» en el Perú con datos del BCRP. Busca las series con buscar_series y usa resumen o serie para las cifras; no calcules a mano. Cada viñeta debe citar el código de la serie y el periodo, y al final lista las URLs de las fuentes.
```
</details>

> 🔧 **ToolSearch** `{"query": "bcrp buscar_series resumen serie", "max_results": 10}`

<details><summary>Resultado de la herramienta</summary>

```text
[imagen omitida]
[imagen omitida]
[imagen omitida]
[imagen omitida]
[imagen omitida]
```
</details>

> 🔧 **mcp__bcrp__buscar_series** `{"texto": "inversión", "limite": 25}`

> 🔧 **mcp__bcrp__buscar_series** `{"texto": "inversión pública", "limite": 25}`

<details><summary>Resultado de la herramienta</summary>

```text
{"result":[{"codigo":"PM10075FA","nombre":"Operaciones del sector público no financiero - Inversión Pública (millones S/)","categoria":"Resultado económico","frecuencia":"Anual","inicio":"1970","actualizada":"2026-08-20"},{"codigo":"PM10081FA","nombre":"Operaciones del sector público no financiero (porcentaje del PBI) - Inversión Pública","categoria":"Resultado económico","frecuencia":"Anual","inicio":"1970","actualizada":"2026-08-20"},{"codigo":"PN03049FQ","nombre":"Ahorro en cuenta corriente del sector público no financiero (millones S/) - Gastos de Capital - Inversión Pública","categoria":"Resultado económico","frecuencia":"Trimestral","inicio":"T1-1990","actualizada":"2026-08-20"},{"codigo":"PN02458FQ","nombre":"Flujos macroeconómicos (porcentaje del PBI) - Sector Público No Financiero - Gastos de Capital - Inversión Pública","categoria":"Otros no categorizados","frecuencia":"Trimestral","inicio":"T1-2012","actualizada":"2026-08-20"},{"codigo":"PN03105FQ","nombre":"Ahorro en cuenta corriente del sector público no financiero (porcentaje del PBI) - Gastos de Capital - Inversión Pública","categoria":"Resultado económico","frecuencia":"Trimestral","inicio":"T1-1990","actualizada":"2026-08-20"},{"codigo":"PN02546AQ","nombre":"Producto bruto interno por tipo de gasto (millones S/) - Demanda Interna - Inversión Bruta Interna - Inversión Bruta Fija - Pública","categoria":"PBI gasto","frecuencia":"Trimestral","inicio":"T1-1980","actualizada":"2026-08-20"},{"codigo":"PM04942AA","nombre":"Producto bruto interno por tipo de gasto (millones S/) - Demanda Interna - Inversión Bruta Interna - Inversión Bruta Fija - Pública","categoria":"PBI gasto","frecuencia":"Anual","inicio":"1950","actualizada":"2026-08-20"},{"codigo":"PN02534AQ","nombre":"Producto bruto interno por tipo de gasto (millones S/ 2007) - Demanda Interna - Inversión Bruta Interna - Inversión Bruta Fija - Pública","categoria":"PBI gasto","frecuencia":"Trimestral","inicio":"T1-1979","actualizada":"2026-08-20"},{"codigo":"PM04931AA","nombre":"Producto bruto interno por tipo de gasto (millones S/ 2007) - Demanda Interna - Inversión Bruta Interna - Inversión Bruta Fija - Pública","categoria":"PBI gasto","frecuencia":"Anual","inicio":"1950","actualizada":"2026-08-20"},{"codigo":"PN02557AQ","nombre":"Producto bruto interno por tipo de gasto (porcentaje del PBI nominal) - Demanda Interna - Inversión Bruta Interna - Inversión Bruta Fija - Pública","categoria":"PBI gasto","frecuencia":"Trimestral","inicio":"T1-19
… [2067 caracteres más omitidos]
```
</details>

<details><summary>Resultado de la herramienta</summary>

```text
{"result":[{"codigo":"PD37982GM","nombre":"Indicadores de coyuntura - Inversión minera (var% real 12 meses)","categoria":"Indicadores de coyuntura","frecuencia":"Mensual","inicio":"Ene-2001","actualizada":"2026-09-02"},{"codigo":"PN01183MM","nombre":"Sistema privado de pensiones - Cartera de Inversiones (millones S/)","categoria":"Mercado de capitales","frecuencia":"Mensual","inicio":"Ene-2002","actualizada":"2026-10-23"},{"codigo":"RD14153DM","nombre":"Inversión bruta fija de los gobiernos regionales (millones S/) - Ica","categoria":"Sector público","frecuencia":"Mensual","inicio":"Ene-2008","actualizada":"2026-09-16"},{"codigo":"RD14162DM","nombre":"Inversión bruta fija de los gobiernos regionales (millones S/) - Puno","categoria":"Sector público","frecuencia":"Mensual","inicio":"Ene-2008","actualizada":"2026-09-16"},{"codigo":"RD14167DM","nombre":"Inversión bruta fija de los gobiernos regionales (millones S/) - Lima","categoria":"Sector público","frecuencia":"Mensual","inicio":"Ene-2008","actualizada":"2026-09-16"},{"codigo":"RD14150DM","nombre":"Inversión bruta fija de los gobiernos regionales (millones S/) - Cusco","categoria":"Sector público","frecuencia":"Mensual","inicio":"Ene-2008","actualizada":"2026-09-16"},{"codigo":"RD14154DM","nombre":"Inversión bruta fija de los gobiernos regionales (millones S/) - Junín","categoria":"Sector público","frecuencia":"Mensual","inicio":"Ene-2008","actualizada":"2026-09-16"},{"codigo":"RD14160DM","nombre":"Inversión bruta fija de los gobiernos regionales (millones S/) - Pasco","categoria":"Sector público","frecuencia":"Mensual","inicio":"Ene-2008","actualizada":"2026-09-16"},{"codigo":"RD14161DM","nombre":"Inversión bruta fija de los gobiernos regionales (millones S/) - Piura","categoria":"Sector público","frecuencia":"Mensual","inicio":"Ene-2008","actualizada":"2026-09-16"},{"codigo":"RD14164DM","nombre":"Inversión bruta fija de los gobiernos regionales (millones S/) - Tacna","categoria":"Sector público","frecuencia":"Mensual","inicio":"Ene-2008","actualizada":"2026-09-16"},{"codigo":"RD14170DM","nombre":"Inversión bruta fija de los gobiernos regionales (millones S/) - Total","categoria":"Sector público","frecuencia":"Mensual","inicio":"Ene-2008","actualizada":"2026-09-16"},{"codigo":"RD14145DM","nombre":"Inversión bruta fija de los gobiernos regionales (millones S/) - Ancash","categoria":"Sector público","frecuencia":"Mensual","inicio":"Ene-2008","actualizada":"2026-09-16"},{"codigo":"RD14157DM","nombre":"Inver
… [2661 caracteres más omitidos]
```
</details>

> 🔧 **mcp__bcrp__buscar_series** `{"texto": "inversión bruta fija gobiernos locales total"}`

> 🔧 **mcp__bcrp__resumen** `{"codigo": "PM10075FA", "desde": "2020", "hasta": "2025"}`

> 🔧 **mcp__bcrp__resumen** `{"codigo": "PM10081FA", "desde": "2020", "hasta": "2025"}`

> 🔧 **mcp__bcrp__resumen** `{"codigo": "RD14170DM", "desde": "2025-01", "hasta": "2026-08"}`

<details><summary>Resultado de la herramienta</summary>

```text
{"result":[{"codigo":"RD14143DM","nombre":"Inversión bruta fija de gobiernos locales por departamentos (millones S/) - Total","categoria":"Sector público","frecuencia":"Mensual","inicio":"Ene-2008","actualizada":"2026-09-16"},{"codigo":"RD15454DQ","nombre":"Inversión bruta fija de gobiernos locales por departamentos (millones S/) - Total (millones de soles)","categoria":"Sector público","frecuencia":"Trimestral","inicio":"T1-2008","actualizada":"2026-04-30"},{"codigo":"RD16708DA","nombre":"Inversión bruta fija de gobiernos locales por departamentos (millones S/) - Total (millones de soles)","categoria":"Sector público","frecuencia":"Anual","inicio":"2008","actualizada":"2026-04-30"}]}
```
</details>

<details><summary>Resultado de la herramienta</summary>

```text
{"codigo":"RD14170DM","nombre":"Inversión bruta fija de los gobiernos regionales (millones S/) - Total","frecuencia":"Mensual","n":19,"primero":{"periodo":"2025-01","valor":629.707281},"ultimo":{"periodo":"2026-07","valor":1520.555501},"cambio":890.8482,"variacion_pct":141.47,"promedio":1205.2215,"maximo":{"periodo":"2025-12","valor":2206.19846},"minimo":{"periodo":"2025-01","valor":629.707281},"fuente":"https://estadisticas.bcrp.gob.pe/estadisticas/series/api/RD14170DM/json/2025-1/2026-8"}
```
</details>

<details><summary>Resultado de la herramienta</summary>

```text
{"codigo":"PM10075FA","nombre":"Operaciones del sector público no financiero - Inversión Pública (millones S/)","frecuencia":"Anual","n":6,"primero":{"periodo":"2020","valor":30774.7157220428},"ultimo":{"periodo":"2025","valor":61230.0779172812},"cambio":30455.3622,"variacion_pct":98.96,"promedio":47874.1283,"maximo":{"periodo":"2025","valor":61230.0779172812},"minimo":{"periodo":"2020","valor":30774.7157220428},"fuente":"https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PM10075FA/json/2020/2025"}
```
</details>

<details><summary>Resultado de la herramienta</summary>

```text
{"codigo":"PM10081FA","nombre":"Operaciones del sector público no financiero (porcentaje del PBI) - Inversión Pública","frecuencia":"Anual","n":6,"primero":{"periodo":"2020","valor":4.19284099587751},"ultimo":{"periodo":"2025","valor":5.04406727241006},"cambio":0.8512,"variacion_pct":20.3,"promedio":4.8054,"maximo":{"periodo":"2024","valor":5.20822720648393},"minimo":{"periodo":"2020","valor":4.19284099587751},"fuente":"https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PM10081FA/json/2020/2025"}
```
</details>

> 🔧 **mcp__bcrp__buscar_series** `{"texto": "inversión bruta fija gobiernos regionales total", "frecuencia": "Anual"}`

> 🔧 **mcp__bcrp__resumen** `{"codigo": "RD16708DA", "desde": "2020", "hasta": "2025"}`

> 🔧 **mcp__bcrp__cuadre_territorial** `{"indicador": "inversion_gobiernos_regionales", "desde": "2024", "hasta": "2025"}`

<details><summary>Resultado de la herramienta</summary>

```text
{"result":[{"codigo":"RD16735DA","nombre":"Inversión bruta fija de los gobiernos regionales (millones S/) - Total (millones de soles)","categoria":"Sector público","frecuencia":"Anual","inicio":"2008","actualizada":"2026-04-30"}]}
```
</details>

<details><summary>Resultado de la herramienta</summary>

```text
{"codigo":"RD16708DA","nombre":"Inversión bruta fija de gobiernos locales por departamentos (millones S/) - Total (millones de soles)","frecuencia":"Anual","n":6,"primero":{"periodo":"2020","valor":11489.492179},"ultimo":{"periodo":"2025","valor":22390.530665},"cambio":10901.0385,"variacion_pct":94.88,"promedio":17923.9137,"maximo":{"periodo":"2025","valor":22390.530665},"minimo":{"periodo":"2020","valor":11489.492179},"fuente":"https://estadisticas.bcrp.gob.pe/estadisticas/series/api/RD16708DA/json/2020/2025"}
```
</details>

<details><summary>Resultado de la herramienta</summary>

```text
{"indicador":"inversion_gobiernos_regionales","unidad":"millones S/","desde":"2024","hasta":"2025","archivo":null,"departamentos":[{"ubigeo":"01","departamento":"Amazonas","codigo":"RD16709DA","valores":{"2024":364.0841,"2025":461.5112}},{"ubigeo":"02","departamento":"Ancash","codigo":"RD16710DA","valores":{"2024":278.5222,"2025":400.7096}},{"ubigeo":"03","departamento":"Apurímac","codigo":"RD16711DA","valores":{"2024":341.176,"2025":494.0952}},{"ubigeo":"04","departamento":"Arequipa","codigo":"RD16712DA","valores":{"2024":595.8618,"2025":695.9291}},{"ubigeo":"05","departamento":"Ayacucho","codigo":"RD16713DA","valores":{"2024":806.2272,"2025":921.2691}},{"ubigeo":"06","departamento":"Cajamarca","codigo":"RD16714DA","valores":{"2024":838.2726,"2025":903.1921}},{"ubigeo":"07","departamento":"Callao","codigo":"RD16733DA","valores":{"2024":186.0276,"2025":192.8128}},{"ubigeo":"08","departamento":"Cusco","codigo":"RD16715DA","valores":{"2024":1061.2261,"2025":959.8789}},{"ubigeo":"09","departamento":"Huancavelica","codigo":"RD16716DA","valores":{"2024":328.072,"2025":307.9736}},{"ubigeo":"10","departamento":"Huánuco","codigo":"RD16717DA","valores":{"2024":411.7711,"2025":404.5923}},{"ubigeo":"11","departamento":"Ica","codigo":"RD16718DA","valores":{"2024":505.3839,"2025":382.0985}},{"ubigeo":"12","departamento":"Junín","codigo":"RD16719DA","valores":{"2024":874.4867,"2025":983.0636}},{"ubigeo":"13","departamento":"La Libertad","codigo":"RD16720DA","valores":{"2024":645.9916,"2025":752.7001}},{"ubigeo":"14","departamento":"Lambayeque","codigo":"RD16721DA","valores":{"2024":622.2822,"2025":655.9396}},{"ubigeo":"15","departamento":"Lima","codigo":"RD16732DA","valores":{"2024":412.5831,"2025":519.5489}},{"ubigeo":"16","departamento":"Loreto","codigo":"RD16722DA","valores":{"2024":969.2213,"2025":999.504}},{"ubigeo":"17","departamento":"Madre de Dios","codigo":"RD16723DA","valores":{"2024":214.7211,"2025":211.6048}},{"ubigeo":"18","departamento":"Moquegua","codigo":"RD16724DA","valores":{"2024":276.7286,"2025":289.9162}},{"ubigeo":"19","departamento":"Pasco","codigo":"RD16725DA","valores":{"2024":306.8796,"2025":434.4102}},{"ubigeo":"20","departamento":"Piura","codigo":"RD16726DA","valores":{"2024":1183.1659,"2025":1101.5796}},{"ubigeo":"21","departamento":"Puno","codigo":"RD16727DA","valores":{"2024":760.01,"2025":870.6663}},{"ubigeo":"22","departamento":"San Martín","codigo":"RD16728DA","valores":{"2024":544.5609,"2025":638.0513}},{"ubigeo":"23","departamento":"T
… [3186 caracteres más omitidos]
```
</details>

> 🔧 **mcp__bcrp__resumen** `{"codigo": "RD16735DA", "desde": "2020", "hasta": "2025"}`

> 🔧 **mcp__bcrp__resumen** `{"codigo": "RD16726DA", "desde": "2020", "hasta": "2025"}`

> 🔧 **mcp__bcrp__resumen** `{"codigo": "RD16718DA", "desde": "2024", "hasta": "2025"}`

<details><summary>Resultado de la herramienta</summary>

```text
{"codigo":"RD16718DA","nombre":"Inversión bruta fija de los gobiernos regionales (millones S/) - Ica (millones de soles)","frecuencia":"Anual","n":2,"primero":{"periodo":"2024","valor":505.383887},"ultimo":{"periodo":"2025","valor":382.098536},"cambio":-123.2854,"variacion_pct":-24.39,"promedio":443.7412,"maximo":{"periodo":"2024","valor":505.383887},"minimo":{"periodo":"2025","valor":382.098536},"fuente":"https://estadisticas.bcrp.gob.pe/estadisticas/series/api/RD16718DA/json/2024/2025"}
```
</details>

<details><summary>Resultado de la herramienta</summary>

```text
{"codigo":"RD16735DA","nombre":"Inversión bruta fija de los gobiernos regionales (millones S/) - Total (millones de soles)","frecuencia":"Anual","n":6,"primero":{"periodo":"2020","valor":6366.456097},"ultimo":{"periodo":"2025","valor":14622.774015},"cambio":8256.3179,"variacion_pct":129.68,"promedio":10388.4439,"maximo":{"periodo":"2025","valor":14622.774015},"minimo":{"periodo":"2020","valor":6366.456097},"fuente":"https://estadisticas.bcrp.gob.pe/estadisticas/series/api/RD16735DA/json/2020/2025"}
```
</details>

<details><summary>Resultado de la herramienta</summary>

```text
{"codigo":"RD16726DA","nombre":"Inversión bruta fija de los gobiernos regionales (millones S/) - Piura (millones de soles)","frecuencia":"Anual","n":6,"primero":{"periodo":"2020","valor":660.073418},"ultimo":{"periodo":"2025","valor":1101.579588},"cambio":441.5062,"variacion_pct":66.89,"promedio":813.0259,"maximo":{"periodo":"2024","valor":1183.165944},"minimo":{"periodo":"2021","valor":553.113388},"fuente":"https://estadisticas.bcrp.gob.pe/estadisticas/series/api/RD16726DA/json/2020/2025"}
```
</details>

### 🤖 Claude · 2026-11-08 18:17 UTC

**Informe: inversión pública en el Perú, con detalle por departamento (BCRP)**

- **Inversión pública total (SPNF).** Pasó de S/ 30 775 millones en 2020 a S/ 61 230 millones en 2025, un aumento de 98,96 %. El nivel de 2025 es el más alto del periodo, que promedió S/ 47 874 millones al año. *Serie PM10075FA, 2020–2025.*

- **Peso en la economía.** Subió de 4,19 % del PBI en 2020 a 5,04 % en 2025. El máximo fue 5,21 % en 2024, así que en 2025 la inversión creció en soles pero bajó ligeramente como proporción del PBI. *Serie PM10081FA, 2020–2025.*

- **Gobiernos regionales.** Su inversión bruta fija pasó de S/ 6 366 millones en 2020 a S/ 14 623 millones en 2025, un aumento de 129,68 %. Crecieron más rápido que el total. La suma de los 25 departamentos, más la Municipalidad Metropolitana de Lima (S/ 136,8 millones, serie RD16734DA), coincide exactamente con el total oficial en 2024 y en 2025. *Serie RD16735DA, 2020–2025; cuadre con RD16709DA–RD16734DA.*

- **Piura.** Es el departamento con más inversión regional en 2025: S/ 1 101,6 millones. Le siguen Loreto (S/ 999,5 millones, RD16722DA) y Junín (S/ 983,1 millones, RD16719DA). Entre 2020 y 2025 la inversión regional en Piura subió 66,89 %. Su máximo fue S/ 1 183,2 millones en 2024 y su mínimo S/ 553,1 millones en 2021. *Serie RD16726DA, 2020–2025.*

- **No todos los departamentos crecieron en 2025.** En Ica, la inversión del gobierno regional bajó de S/ 505,4 millones en 2024 a S/ 382,1 millones en 2025, una caída de 24,39 %. Mientras tanto, la inversión de los gobiernos locales en todo el país casi se duplicó entre 2020 y 2025: pasó de S/ 11 489 millones a S/ 22 391 millones (+94,88 %). *Series RD16718DA, 2024–2025, y RD16708DA, 2020–2025.*

Todas las cifras son nominales, en millones de soles corrientes, así que una parte del crecimiento es inflación. Los rankings comparan montos absolutos, no montos por habitante. Para cruzar estos datos con la pobreza de la ENAHO está la skill `analizando-reparto`.

**Fuentes**
- https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PM10075FA/json/2020/2025
- https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PM10081FA/json/2020/2025
- https://estadisticas.bcrp.gob.pe/estadisticas/series/api/RD16735DA/json/2020/2025
- https://estadisticas.bcrp.gob.pe/estadisticas/series/api/RD16726DA/json/2020/2025
- https://estadisticas.bcrp.gob.pe/estadisticas/series/api/RD16722DA/json/2024/2025
- https://estadisticas.bcrp.gob.pe/estadisticas/series/api/RD16719DA/json/2024/2025
- https://estadisticas.bcrp.gob.pe/estadisticas/series/api/RD16718DA/json/2024/2025
- https://estadisticas.bcrp.gob.pe/estadisticas/series/api/RD16734DA/json/2024/2025
- https://estadisticas.bcrp.gob.pe/estadisticas/series/api/RD16708DA/json/2020/2025

## 👤 Usuaria · 2026-11-08 20:16 UTC

@bcrp:bcrp://serie/RD16682DA ¿qué mide esta serie y desde cuándo hay datos?

> 🔧 **ToolSearch** `{"query": "select:ReadMcpResourceTool", "max_results": 1}`

<details><summary>Resultado de la herramienta</summary>

```text
[imagen omitida]
```
</details>

> 🔧 **ReadMcpResourceTool** `{"server": "bcrp", "uri": "bcrp://serie/RD16682DA"}`

<details><summary>Resultado de la herramienta</summary>

```text
{"contents":[{"uri":"bcrp://serie/RD16682DA","mimeType":"text/plain","text":"{\"codigo\": \"RD16682DA\", \"nombre\": \"Inversi\\u00f3n bruta fija del gobierno nacional por departamentos (millones S/) - Total (millones de soles)\", \"categoria\": \"Sector p\\u00fablico\", \"frecuencia\": \"Anual\", \"inicio\": \"2008\", \"actualizada\": \"2026-04-30\"}"}]}
```
</details>

### 🤖 Claude · 2026-11-08 20:17 UTC

**RD16682DA** es el **total nacional de la inversión bruta fija del gobierno nacional**, en millones de soles corrientes. Es una serie **anual**, con datos **desde 2008**. El BCRP la actualizó por última vez el 30-04-2026, así que es probable que ya incluya 2025.

Pertenece a la categoría «Inversión bruta fija del gobierno nacional por departamentos», dentro de Sector público. Es el tercer nivel de gobierno, junto a los dos del informe anterior:

| Nivel de gobierno | Serie anual (total) |
|---|---|
| Nacional | **RD16682DA** |
| Regionales | RD16735DA |
| Locales | RD16708DA |

Si quieres, consulto su resumen 2020–2025 o reviso con `cuadre_territorial("inversion_gobierno_nacional", …)` que la suma de los departamentos coincida con el total.

