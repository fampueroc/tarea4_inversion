# Sesiones de evaluación: modo A sin mcp ni skills

*Cada sección es una sesión independiente de `claude -p` (`evaluacion/evaluar.py`), con las mismas reglas de privacidad que el resto de las evidencias. Registro original en `evaluacion/logs/`.*

---

## Pregunta B1 · modo A

> **Pregunta:** Según el BCRP, ¿cuánto fue la inversión bruta fija de los gobiernos regionales en el departamento de Cusco en 2024, en millones de soles?

#### 🤖 Claude · 2026-11-06 05:27 UTC

Voy a revisar primero qué hay en la carpeta de trabajo.

> 🔧 **Glob** `{"pattern": "**/*"}`

<details><summary>Resultado de la herramienta</summary>

```text
datos\catalogo_bcrp.csv
datos\966-Modulo02.zip
datos\966-Modulo34.zip
datos\peru_departamental_simple.geojson
.python-version
pyproject.toml
uv.lock
```
</details>

> 🔧 **Bash** `{"command": "cd datos; head -c 1500 catalogo_bcrp.csv; echo; wc -l catalogo_bcrp.csv; unzip -l 966-Modulo02.zip | head -30; unzip -l 966-Modulo34.zip | head -30"}`

<details><summary>Resultado de la herramienta</summary>

```text
Código de serie;Categoría de serie;Grupo de serie;Nombre de serie;Descripción de la serie;Metodología de la serie;Unidad de medida;Escala;Geografía (País, Región de Perú);Fuente;Frecuencia;Fecha de creación;Grupo de publicación;Área que publica;Fecha de actualización;Fecha de inicio;Fecha de fin;Memo;

PN00001MM;Sociedades creadoras de depósito;Cuentas monetarias de las sociedades creadoras de depósito;Activos Externos Netos de Corto Plazo (millones S/);https://estadisticas.bcrp.gob.pe/estadisticas/series/documentos/bcrpdataapi.pdf;https://estadisticas.bcrp.gob.pe/estadisticas/series/documentos/bcrpdataapi.pdf;;;;BCRP;Mensual;2022-03-24;Sistema financiero y empresas bancarias y expectativas sobre condiciones crediticias;Departamento de Estadísticas Monetarias;2026-10-23;Ene-1992;Dic-2025;;

PN00002MM;Sociedades creadoras de depósito;Cuentas monetarias de las sociedades creadoras de depósito;Activos Externos Netos de Corto Plazo (millones US$);;;;;;BCRP;Mensual;2022-03-24;Sistema financiero y empresas bancarias y expectativas sobre condiciones crediticias;Departamento de Estadísticas Monetarias;2026-10-23;Ene-1992;Dic-2025;;

PN00003MM;Sociedades creadoras de depósito;Cuentas monetarias de las sociedades creadoras de depósito;Activos Externos Netos de Corto Plazo - Activos (millones US$);;;;;;BCRP;Mensual;2022-03-24;Sistema financiero y empresas bancarias y expectativas sobre condiciones crediticias;Departamento de Estadísticas Monetarias;2026-10-23;Ene-19
17168 catalogo_bcrp.csv
Archive:  966-Modulo02.zip
  Length      Date    Time    Name
---------  ---------- -----   ----
        0  2025-05-07 14:43   966-Modulo02/
   201079  2024-06-18 10:39   966-Modulo02/CED-01-200-2024.pdf
   395343  2021-05-07 11:05   966-Modulo02/Criterios para codificar Ocupaciones Peligrosas.pdf
  3940690  2025-05-16 14:36   966-Modulo02/Diccionario2024.pdf
 10217755  2025-05-07 14:39   966-Modulo02/enaho01-2024-200.dta
   349153  2020-05-11 21:36   966-Modulo02/enaho_tabla_ciuo_88.dta
    56727  2020-05-11 21:36   966-Modulo02/enaho_tabla_cno_2015.dta
   487444  2024-02-06 18:57   966-Modulo02/FichaTecnica.pdf
---------                     -------
 15648191                     8 files
Archive:  966-Modulo34.zip
  Length      Date    Time    Name
---------  ---------- -----   ----
        0  2026-05-14 09:56   966-Modulo34/
    24486  2025-05-07 19:18   966-Modulo34/ConstVarGasto-Metodologia actualizada.zip
   254671  2025-05-05 19:34   966-Modulo34/DefinicionValoresMonetariosBas
… [616 caracteres más omitidos]
```
</details>

#### 🤖 Claude · 2026-11-06 05:28 UTC

Los zips son de ENAHO; lo relevante es el catálogo. Busco las series.

> 🔧 **Bash** `{"command": "cd datos; grep -i \"inversi\" catalogo_bcrp.csv | grep -i \"cusco\" | cut -d';' -f1,4,7,8,9,11,16,17 | head -40"}`

<details><summary>Resultado de la herramienta</summary>

```text
RD14099DM;Cusco;;;RE;Mensual;Ene-2008;Dic-2025
RD14125DM;Cusco;;;RE;Mensual;Ene-2008;Dic-2025
RD14150DM;Cusco;;;RE;Mensual;Ene-2008;Dic-2025
RD15410DQ;Cusco (millones de soles);;;RE;Trimestral;T1-2008;T4-2025
RD15436DQ;Cusco (millones de soles);;;RE;Trimestral;T1-2008;T4-2025
RD15461DQ;Cusco (millones de soles);;;RE;Trimestral;T1-2008;T4-2025
RD16664DA;Cusco (millones de soles);;;RE;Anual;2008;2025
RD16690DA;Cusco (millones de soles);;;RE;Anual;2008;2025
RD16715DA;Cusco (millones de soles);;;RE;Anual;2008;2025
Shell cwd was reset to C:\Users\[usuario]\AppData\Local\Temp\tarea4_modoA_q_q2pfe9
```
</details>

> 🔧 **Bash** `{"command": "cd datos; grep -E \"^RD16(664|690|715)DA\" catalogo_bcrp.csv | cut -d';' -f1-5,7,8,9"}`

<details><summary>Resultado de la herramienta</summary>

```text
RD16664DA;Sector público;Inversión bruta fija del gobierno nacional por departamentos (millones S/);Cusco (millones de soles);Información estadística regional / Sector público / Inversión bruta fija del gobierno nacional por departamentos (millones S/) / Cusco (millones de soles);;;RE
RD16690DA;Sector público;Inversión bruta fija de gobiernos locales por departamentos (millones S/);Cusco (millones de soles);Información estadística regional / Sector público / Inversión bruta fija de gobiernos locales por departamentos (millones S/) / Cusco (millones de soles);;;RE
RD16715DA;Sector público;Inversión bruta fija de los gobiernos regionales (millones S/);Cusco (millones de soles);Información estadística regional / Sector público / Inversión bruta fija de los gobiernos regionales (millones S/) / Cusco (millones de soles);;;RE
Shell cwd was reset to C:\Users\[usuario]\AppData\Local\Temp\tarea4_modoA_q_q2pfe9
```
</details>

#### 🤖 Claude · 2026-11-06 05:28 UTC

La serie es RD16715DA. El catálogo no trae valores, así que consulto la API del BCRP.

> 🔧 **Bash** `{"command": "curl -s -m 60 \"https://estadisticas.bcrp.gob.pe/estadisticas/series/api/RD16715DA/json/2022/2025\""}`

<details><summary>Resultado de la herramienta</summary>

```text
{
"config":
{
"title":"Inversión bruta fija de los gobiernos regionales (millones S/)",
"series":
[
{
"name":"Inversión bruta fija de los gobiernos regionales (millones S/) - Cusco (millones de soles)",
"dec":"0"
}]
},
"periods":
[
{
"name":"2022",
"values":["703.74766"]
},
{
"name":"2023",
"values":["807.379846"]
},
{
"name":"2024",
"values":["1061.226088"]
},
{
"name":"2025",
"values":["959.878853"]
}
]
}
Shell cwd was reset to C:\Users\[usuario]\AppData\Local\Temp\tarea4_modoA_q_q2pfe9
```
</details>

#### 🤖 Claude · 2026-11-06 05:28 UTC

Según la API del BCRP (serie RD16715DA, «Inversión bruta fija de los gobiernos regionales (millones S/) – Cusco», frecuencia anual), el valor de 2024 es 1 061,226 millones de soles. Eso equivale a unos 1 061,2 millones.

Para comparar, la serie da 703,7 millones en 2022, 807,4 millones en 2023 y 959,9 millones en 2025.

RESPUESTA FINAL: 1 061,2 millones de soles (≈ S/ 1 061,23 millones) en 2024, serie BCRP RD16715DA

---

## Pregunta B2 · modo A

> **Pregunta:** Según el BCRP, ¿cuánto sumó la inversión bruta fija del gobierno nacional en todos los departamentos del Perú en 2024, en millones de soles?

#### 🤖 Claude · 2026-11-06 05:27 UTC

Voy a revisar qué hay en la carpeta.

> 🔧 **Glob** `{"pattern": "**/*"}`

<details><summary>Resultado de la herramienta</summary>

```text
datos\catalogo_bcrp.csv
datos\966-Modulo02.zip
datos\966-Modulo34.zip
datos\peru_departamental_simple.geojson
.python-version
pyproject.toml
uv.lock
```
</details>

> 🔧 **Bash** `{"command": "cd datos; head -c 1500 catalogo_bcrp.csv; echo; wc -l catalogo_bcrp.csv; grep -i -E \"bruta fija\" catalogo_bcrp.csv | head -30; unzip -l 966-Modulo02.zip | head -30; unzip -l 966-Modulo34.zip | head -30"}`

<details><summary>Resultado de la herramienta</summary>

```text
Código de serie;Categoría de serie;Grupo de serie;Nombre de serie;Descripción de la serie;Metodología de la serie;Unidad de medida;Escala;Geografía (País, Región de Perú);Fuente;Frecuencia;Fecha de creación;Grupo de publicación;Área que publica;Fecha de actualización;Fecha de inicio;Fecha de fin;Memo;

PN00001MM;Sociedades creadoras de depósito;Cuentas monetarias de las sociedades creadoras de depósito;Activos Externos Netos de Corto Plazo (millones S/);https://estadisticas.bcrp.gob.pe/estadisticas/series/documentos/bcrpdataapi.pdf;https://estadisticas.bcrp.gob.pe/estadisticas/series/documentos/bcrpdataapi.pdf;;;;BCRP;Mensual;2022-03-24;Sistema financiero y empresas bancarias y expectativas sobre condiciones crediticias;Departamento de Estadísticas Monetarias;2026-10-23;Ene-1992;Dic-2025;;

PN00002MM;Sociedades creadoras de depósito;Cuentas monetarias de las sociedades creadoras de depósito;Activos Externos Netos de Corto Plazo (millones US$);;;;;;BCRP;Mensual;2022-03-24;Sistema financiero y empresas bancarias y expectativas sobre condiciones crediticias;Departamento de Estadísticas Monetarias;2026-10-23;Ene-1992;Dic-2025;;

PN00003MM;Sociedades creadoras de depósito;Cuentas monetarias de las sociedades creadoras de depósito;Activos Externos Netos de Corto Plazo - Activos (millones US$);;;;;;BCRP;Mensual;2022-03-24;Sistema financiero y empresas bancarias y expectativas sobre condiciones crediticias;Departamento de Estadísticas Monetarias;2026-10-23;Ene-19
17168 catalogo_bcrp.csv
PN02521AQ;PBI gasto;Producto bruto interno por tipo de gasto (variaciones porcentuales reales anualizadas);Demanda Interna - Inversión Bruta Interna - Inversión Bruta Fija;;;;;;INEI, BCRP;Trimestral;2022-02-18;Demanda y oferta global, balanza de pagos, sector público y monetario;Departamento de Indicadores de la Actividad Economía;2026-08-20;T1-1980;T4-2025;;
PN02522AQ;PBI gasto;Producto bruto interno por tipo de gasto (variaciones porcentuales reales anualizadas);Demanda Interna - Inversión Bruta Interna - Inversión Bruta Fija - Privada;;;;;;INEI, BCRP;Trimestral;2022-02-18;Demanda y oferta global, balanza de pagos, sector público y monetario;Departamento de Indicadores de la Actividad Economía;2026-08-20;T1-1980;T4-2025;;
PN02523AQ;PBI gasto;Producto bruto interno por tipo de gasto (variaciones porcentuales reales anualizadas);Demanda Interna - Inversión Bruta Interna - Inversión Bruta Fija - Pública;;;;;;INEI, BCRP;Trimestral;2022-02-18;Demanda y oferta global, balanza de pagos,
… [11165 caracteres más omitidos]
```
</details>

> 🔧 **Bash** `{"command": "cd datos; grep -i \"gobierno nacional\" catalogo_bcrp.csv | grep -i -E \"inversi\" | cut -c1-400 | head -40"}`

<details><summary>Resultado de la herramienta</summary>

```text
RD14092DM;Sector público;Inversión bruta fija del gobierno nacional por departamentos (millones S/);Amazonas;Información estadística regional / Sector público / Inversión bruta fija del gobierno nacional por departamentos (millones S/) / Amazonas;;;;RE;Ministerio de Economía y Finanzas;Mensual;2017-05-02;;Departamento de Bases de Datos Macroeconómicas;2026-09-16;Ene-2008;Dic-2025;;
RD14093DM;Sector público;Inversión bruta fija del gobierno nacional por departamentos (millones S/);Ancash;Información estadística regional / Sector público / Inversión bruta fija del gobierno nacional por departamentos (millones S/) / Ancash;;;;RE;Ministerio de Economía y Finanzas;Mensual;2017-05-02;;Departamento de Bases de Datos Macroeconómicas;2026-09-16;Ene-2008;Dic-2025;;
RD14094DM;Sector público;Inversión bruta fija del gobierno nacional por departamentos (millones S/);Apurímac;Información estadística regional / Sector público / Inversión bruta fija del gobierno nacional por departamentos (millones S/) / Apurímac;;;;RE;Ministerio de Economía y Finanzas;Mensual;2017-05-02;;Departamento de Bases de Datos Macroeconómicas;2026-09-16;Ene-2008;Dic-2025;;
RD14095DM;Sector público;Inversión bruta fija del gobierno nacional por departamentos (millones S/);Arequipa;Información estadística regional / Sector público / Inversión bruta fija del gobierno nacional por departamentos (millones S/) / Arequipa;;;;RE;Ministerio de Economía y Finanzas;Mensual;2017-05-02;;Departamento de Bases de Datos Macroeconómicas;2026-09-16;Ene-2008;Dic-2025;;
RD14096DM;Sector público;Inversión bruta fija del gobierno nacional por departamentos (millones S/);Ayacucho;Información estadística regional / Sector público / Inversión bruta fija del gobierno nacional por departamentos (millones S/) / Ayacucho;;;;RE;Ministerio de Economía y Finanzas;Mensual;2017-05-02;;Departamento de Bases de Datos Macroeconómicas;2026-09-16;Ene-2008;Dic-2025;;
RD14097DM;Sector público;Inversión bruta fija del gobierno nacional por departamentos (millones S/);Cajamarca;Información estadística regional / Sector público / Inversión bruta fija del gobierno nacional por departamentos (millones S/) / Cajamarca;;;;RE;Ministerio de Economía y Finanzas;Mensual;2017-05-02;;Departamento de Bases de Datos Macroeconómicas;2026-09-16;Ene-2008;Dic-2025;;
RD14098DM;Sector público;Inversión bruta fija del gobierno nacional por departamentos (millones S/);Callao;Información estadística regional / Sector público / Inversión bruta fija del gobierno
… [13043 caracteres más omitidos]
```
</details>

#### 🤖 Claude · 2026-11-06 05:28 UTC

El catálogo solo lista las series; los valores están en la API del BCRP. Consulto la serie mensual «Total» (RD14117DM) para 2024.

> 🔧 **Bash** `{"command": "curl -s -m 60 \"https://estadisticas.bcrp.gob.pe/estadisticas/series/api/RD14117DM/json/2024-1/2024-12/ing\""}`

<details><summary>Resultado de la herramienta</summary>

```text
{
"config":
{
"title":"Inversión bruta fija del gobierno nacional por departamentos (millones S/)",
"series":
[
{
"name":"Inversión bruta fija del gobierno nacional por departamentos (millones S/) - Total",
"dec":"0"
}]
},
"periods":
[
{
"name":"Jan.2024",
"values":["1422.780074"]
},
{
"name":"Feb.2024",
"values":["1353.600097"]
},
{
"name":"Mar.2024",
"values":["1736.356768"]
},
{
"name":"Apr.2024",
"values":["1455.785758"]
},
{
"name":"May.2024",
"values":["1509.092133"]
},
{
"name":"Jun.2024",
"values":["2120.717935"]
},
{
"name":"Jul.2024",
"values":["1942.9051"]
},
{
"name":"Aug.2024",
"values":["1618.503634"]
},
{
"name":"Sep.2024",
"values":["2361.822946"]
},
{
"name":"Oct.2024",
"values":["2616.459514"]
},
{
"name":"Nov.2024",
"values":["2097.915677"]
},
{
"name":"Dec.2024",
"values":["4873.389688"]
}
]
}
Shell cwd was reset to C:\Users\[usuario]\AppData\Local\Temp\tarea4_modoA_fdmlq5uo
```
</details>

> 🔧 **Bash** `{"command": "python3 -c \"print(sum([1422.780074,1353.600097,1736.356768,1455.785758,1509.092133,2120.717935,1942.9051,1618.503634,2361.822946,2616.459514,2097.915677,4873.389688]))\""}`

<details><summary>Resultado de la herramienta</summary>

```text
Exit code 49
Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.
```
</details>

> 🔧 **Bash** `{"command": "echo \"1422.780074 1353.600097 1736.356768 1455.785758 1509.092133 2120.717935 1942.9051 1618.503634 2361.822946 2616.459514 2097.915677 4873.389688\" | tr ' ' '\\n' | awk '{s+=$1} END{printf \"%.3f\\n\", s}'"}`

<details><summary>Resultado de la herramienta</summary>

```text
25109.329
Shell cwd was reset to C:\Users\[usuario]\AppData\Local\Temp\tarea4_modoA_fdmlq5uo
```
</details>

#### 🤖 Claude · 2026-11-06 05:28 UTC

En 2024, la inversión bruta fija del gobierno nacional en todos los departamentos sumó unos **25 109 millones de soles**.

- **Fuente:** el catálogo de la carpeta (`datos/catalogo_bcrp.csv`) solo lista las series, sin valores. Los datos salieron de la API del BCRP, serie **RD14117DM**, «Inversión bruta fija del gobierno nacional por departamentos (millones S/) – Total». El BCRP indica como fuente primaria al Ministerio de Economía y Finanzas.
- **Cálculo:** sumé los 12 valores mensuales de 2024 (enero a diciembre). Son 25 109,329 millones de soles sin redondear.
- **Mes con más inversión:** diciembre, con 4 873,4 millones.
- **Revisión de las cifras:** la serie se actualizó por última vez el 16/09/2026, así que las cifras del BCRP pueden revisarse.
- **Lo que no hice:** no sumé los departamentos uno por uno. Usé la fila «Total» que publica el BCRP.

RESPUESTA FINAL: ≈ 25 109 millones de soles (25 109,33) de inversión bruta fija del gobierno nacional en 2024.

---

## Pregunta B3 · modo A

> **Pregunta:** Según el BCRP, entre 2020 y 2024, ¿en qué año fue más alta la inversión bruta fija de los gobiernos locales del departamento de Cajamarca y cuánto fue, en millones de soles?

#### 🤖 Claude · 2026-11-06 05:27 UTC

Voy a revisar primero qué datos hay en la carpeta.

> 🔧 **Glob** `{"pattern": "**/*"}`

<details><summary>Resultado de la herramienta</summary>

```text
datos\catalogo_bcrp.csv
datos\966-Modulo02.zip
datos\966-Modulo34.zip
datos\peru_departamental_simple.geojson
.python-version
pyproject.toml
uv.lock
```
</details>

> 🔧 **Bash** `{"command": "cd datos; head -c 1500 catalogo_bcrp.csv; echo; wc -l catalogo_bcrp.csv; grep -i -E \"inversi.n bruta fija|Cajamarca\" catalogo_bcrp.csv | head -30; unzip -l 966-Modulo02.zip | head; unzip -l 966-Modulo34.zip | head"}`

<details><summary>Resultado de la herramienta</summary>

```text
Código de serie;Categoría de serie;Grupo de serie;Nombre de serie;Descripción de la serie;Metodología de la serie;Unidad de medida;Escala;Geografía (País, Región de Perú);Fuente;Frecuencia;Fecha de creación;Grupo de publicación;Área que publica;Fecha de actualización;Fecha de inicio;Fecha de fin;Memo;

PN00001MM;Sociedades creadoras de depósito;Cuentas monetarias de las sociedades creadoras de depósito;Activos Externos Netos de Corto Plazo (millones S/);https://estadisticas.bcrp.gob.pe/estadisticas/series/documentos/bcrpdataapi.pdf;https://estadisticas.bcrp.gob.pe/estadisticas/series/documentos/bcrpdataapi.pdf;;;;BCRP;Mensual;2022-03-24;Sistema financiero y empresas bancarias y expectativas sobre condiciones crediticias;Departamento de Estadísticas Monetarias;2026-10-23;Ene-1992;Dic-2025;;

PN00002MM;Sociedades creadoras de depósito;Cuentas monetarias de las sociedades creadoras de depósito;Activos Externos Netos de Corto Plazo (millones US$);;;;;;BCRP;Mensual;2022-03-24;Sistema financiero y empresas bancarias y expectativas sobre condiciones crediticias;Departamento de Estadísticas Monetarias;2026-10-23;Ene-1992;Dic-2025;;

PN00003MM;Sociedades creadoras de depósito;Cuentas monetarias de las sociedades creadoras de depósito;Activos Externos Netos de Corto Plazo - Activos (millones US$);;;;;;BCRP;Mensual;2022-03-24;Sistema financiero y empresas bancarias y expectativas sobre condiciones crediticias;Departamento de Estadísticas Monetarias;2026-10-23;Ene-19
17168 catalogo_bcrp.csv
PN02521AQ;PBI gasto;Producto bruto interno por tipo de gasto (variaciones porcentuales reales anualizadas);Demanda Interna - Inversión Bruta Interna - Inversión Bruta Fija;;;;;;INEI, BCRP;Trimestral;2022-02-18;Demanda y oferta global, balanza de pagos, sector público y monetario;Departamento de Indicadores de la Actividad Economía;2026-08-20;T1-1980;T4-2025;;
PN02522AQ;PBI gasto;Producto bruto interno por tipo de gasto (variaciones porcentuales reales anualizadas);Demanda Interna - Inversión Bruta Interna - Inversión Bruta Fija - Privada;;;;;;INEI, BCRP;Trimestral;2022-02-18;Demanda y oferta global, balanza de pagos, sector público y monetario;Departamento de Indicadores de la Actividad Economía;2026-08-20;T1-1980;T4-2025;;
PN02523AQ;PBI gasto;Producto bruto interno por tipo de gasto (variaciones porcentuales reales anualizadas);Demanda Interna - Inversión Bruta Interna - Inversión Bruta Fija - Pública;;;;;;INEI, BCRP;Trimestral;2022-02-18;Demanda y oferta global, balanza de pagos,
… [10768 caracteres más omitidos]
```
</details>

#### 🤖 Claude · 2026-11-06 05:28 UTC

Busco la serie de gobiernos locales por departamento en el catálogo.

> 🔧 **Bash** `{"command": "cd datos; grep -i \"Cajamarca\" catalogo_bcrp.csv | grep -i -E \"inversi\" | cut -c1-400"}`

<details><summary>Resultado de la herramienta</summary>

```text
RD14097DM;Sector público;Inversión bruta fija del gobierno nacional por departamentos (millones S/);Cajamarca;Información estadística regional / Sector público / Inversión bruta fija del gobierno nacional por departamentos (millones S/) / Cajamarca;;;;RE;Ministerio de Economía y Finanzas;Mensual;2017-05-02;;Departamento de Bases de Datos Macroeconómicas;2026-09-16;Ene-2008;Dic-2025;;
RD14123DM;Sector público;Inversión bruta fija de gobiernos locales por departamentos (millones S/);Cajamarca;Información estadística regional / Sector público / Inversión bruta fija de gobiernos locales por departamentos (millones S/) / Cajamarca;;;;RE;Ministerio de Economía y Finanzas;Mensual;2017-05-02;;Departamento de Bases de Datos Macroeconómicas;2026-09-16;Ene-2008;Dic-2025;;
RD14149DM;Sector público;Inversión bruta fija de los gobiernos regionales (millones S/);Cajamarca;Información estadística regional / Sector público / Inversión bruta fija de los gobiernos regionales (millones S/) / Cajamarca;;;;RE;Ministerio de Economía y Finanzas;Mensual;2017-05-02;;Departamento de Bases de Datos Macroeconómicas;2026-09-16;Ene-2008;Dic-2025;;
RD15408DQ;Sector público;Inversión bruta fija del gobierno nacional por departamentos (millones S/);Cajamarca (millones de soles);Información estadística regional / Sector público / Inversión bruta fija del gobierno nacional por departamentos (millones S/) / Cajamarca (millones de soles);;;;RE;Ministerio de Economía y Finanzas;Trimestral;2017-12-13;;Departamento de Bases de Datos Macroecon�
RD15434DQ;Sector público;Inversión bruta fija de gobiernos locales por departamentos (millones S/);Cajamarca (millones de soles);Información estadística regional / Sector público / Inversión bruta fija de gobiernos locales por departamentos (millones S/) / Cajamarca (millones de soles);;;;RE;Ministerio de Economía y Finanzas;Trimestral;2017-12-13;;Departamento de Bases de Datos Macroeconóm
RD15460DQ;Sector público;Inversión bruta fija de los gobiernos regionales (millones S/);Cajamarca (millones de soles);Información estadística regional / Sector público / Inversión bruta fija de los gobiernos regionales (millones S/) / Cajamarca (millones de soles);;;;RE;Ministerio de Economía y Finanzas;Trimestral;2017-12-13;;Departamento de Bases de Datos Macroeconómicas;2026-04-30;T1-200
RD16662DA;Sector público;Inversión bruta fija del gobierno nacional por departamentos (millones S/);Cajamarca (millones de soles);Información estadística regional / Sector público / Inv
… [1076 caracteres más omitidos]
```
</details>

#### 🤖 Claude · 2026-11-06 05:28 UTC

La serie anual es RD16688DA. Intento obtener los datos de la API del BCRP.

> 🔧 **Bash** `{"command": "curl -s -m 60 \"https://estadisticas.bcrp.gob.pe/estadisticas/series/api/RD16688DA/json/2020/2024/esp\" | head -c 1500"}`

<details><summary>Resultado de la herramienta</summary>

```text
{
"config":
{
"title":"Inversión bruta fija de gobiernos locales por departamentos (millones S/)",
"series":
[
{
"name":"Inversión bruta fija de gobiernos locales por departamentos (millones S/) - Cajamarca (millones de soles)",
"dec":"0"
}]
},
"periods":
[
{
"name":"2020",
"values":["754.810411"]
},
{
"name":"2021",
"values":["1152.409851"]
},
{
"name":"2022",
"values":["1291.398847"]
},
{
"name":"2023",
"values":["1051.715621"]
},
{
"name":"2024",
"values":["877.252555"]
}
]
}
Shell cwd was reset to C:\Users\[usuario]\AppData\Local\Temp\tarea4_modoA_jyfu0_ud
```
</details>

#### 🤖 Claude · 2026-11-06 05:28 UTC

Según el BCRP, la inversión bruta fija de los gobiernos locales de Cajamarca fue más alta en **2022**, con unos **1 291,4 millones de soles**.

Los datos salen de la serie anual RD16688DA del BCRP, "Inversión bruta fija de gobiernos locales por departamentos (millones S/) – Cajamarca". La fuente primaria es el Ministerio de Economía y Finanzas. Consulté la API del BCRP el 6 de noviembre de 2026.

| Año | Millones de S/ |
|---|---|
| 2020 | 754,8 |
| 2021 | 1 152,4 |
| 2022 | **1 291,4** |
| 2023 | 1 051,7 |
| 2024 | 877,3 |

Los montos están en soles corrientes, tal como los publica la serie.

RESPUESTA FINAL: 2022, con 1 291,4 millones de soles (S/ 1 291,40 millones aprox.)

---

## Pregunta B4 · modo A

> **Pregunta:** Según el BCRP, ¿cuánto fueron las exportaciones de productos tradicionales mineros del departamento de Arequipa en 2022, en millones de dólares FOB?

#### 🤖 Claude · 2026-11-06 05:27 UTC

Reviso primero qué hay en la carpeta.

> 🔧 **Glob** `{"pattern": "**/*"}`

<details><summary>Resultado de la herramienta</summary>

```text
datos\catalogo_bcrp.csv
datos\966-Modulo02.zip
datos\966-Modulo34.zip
datos\peru_departamental_simple.geojson
.python-version
pyproject.toml
uv.lock
```
</details>

> 🔧 **Bash** `{"command": "cd datos; head -c 1500 catalogo_bcrp.csv; echo; wc -l catalogo_bcrp.csv; grep -i -E \"arequipa\" catalogo_bcrp.csv | grep -i -E \"tradicional|miner\" | head -30; unzip -l 966-Modulo02.zip | head -30; unzip -l 966-Modulo34.zip | head -30"}`

<details><summary>Resultado de la herramienta</summary>

```text
Código de serie;Categoría de serie;Grupo de serie;Nombre de serie;Descripción de la serie;Metodología de la serie;Unidad de medida;Escala;Geografía (País, Región de Perú);Fuente;Frecuencia;Fecha de creación;Grupo de publicación;Área que publica;Fecha de actualización;Fecha de inicio;Fecha de fin;Memo;

PN00001MM;Sociedades creadoras de depósito;Cuentas monetarias de las sociedades creadoras de depósito;Activos Externos Netos de Corto Plazo (millones S/);https://estadisticas.bcrp.gob.pe/estadisticas/series/documentos/bcrpdataapi.pdf;https://estadisticas.bcrp.gob.pe/estadisticas/series/documentos/bcrpdataapi.pdf;;;;BCRP;Mensual;2022-03-24;Sistema financiero y empresas bancarias y expectativas sobre condiciones crediticias;Departamento de Estadísticas Monetarias;2026-10-23;Ene-1992;Dic-2025;;

PN00002MM;Sociedades creadoras de depósito;Cuentas monetarias de las sociedades creadoras de depósito;Activos Externos Netos de Corto Plazo (millones US$);;;;;;BCRP;Mensual;2022-03-24;Sistema financiero y empresas bancarias y expectativas sobre condiciones crediticias;Departamento de Estadísticas Monetarias;2026-10-23;Ene-1992;Dic-2025;;

PN00003MM;Sociedades creadoras de depósito;Cuentas monetarias de las sociedades creadoras de depósito;Activos Externos Netos de Corto Plazo - Activos (millones US$);;;;;;BCRP;Mensual;2022-03-24;Sistema financiero y empresas bancarias y expectativas sobre condiciones crediticias;Departamento de Estadísticas Monetarias;2026-10-23;Ene-19
17168 catalogo_bcrp.csv
RD12954DM;Producción;Producción de productos mineros según departamentos;Cobre - Arequipa (tm.f);Información estadística regional / Producción / Producción de productos mineros según departamentos / Cobre - Arequipa (tm.f);;;;RE;Ministerio de Energía y Minas;Mensual;2017-05-02;;Departamento de Bases de Datos Macroeconómicas;2026-09-16;Ene-2001;Dic-2025;;
RD12974DM;Producción;Producción de productos mineros según departamentos;Molibdeno - Arequipa (tm.f);Información estadística regional / Producción / Producción de productos mineros según departamentos / Molibdeno - Arequipa (tm.f);;;;RE;Ministerio de Energía y Minas;Mensual;2017-05-02;;Departamento de Bases de Datos Macroeconómicas;2026-09-16;Ene-2001;Dic-2025;;
RD12981DM;Producción;Producción de productos mineros según departamentos;Oro - Arequipa (grs.f);Información estadística regional / Producción / Producción de productos mineros según departamentos / Oro - Arequipa (grs.f);;;;RE;Ministerio de Energía y Minas;Mensual;2017-05-0
… [12714 caracteres más omitidos]
```
</details>

#### 🤖 Claude · 2026-11-06 05:28 UTC

El catálogo tiene la serie (RD38191BM), pero no sus valores. Intento consultarla en la API del BCRP.

> 🔧 **Bash** `{"command": "curl -s -m 60 \"https://estadisticas.bcrp.gob.pe/estadisticas/series/api/RD38191BM/json/2022-1/2022-12/ing\" | head -c 2000"}`

<details><summary>Resultado de la herramienta</summary>

```text
{
"config":
{
"title":"Exportaciones por grupo de productos de Arequipa (Valores FOB en millones US$)",
"series":
[
{
"name":"Exportaciones por grupo de productos de Arequipa (Valores FOB en millones US$) - Productos tradicionales - Mineros",
"dec":"0"
}]
},
"periods":
[
{
"name":"Jan.2022",
"values":["499.89478773"]
},
{
"name":"Feb.2022",
"values":["436.83405271"]
},
{
"name":"Mar.2022",
"values":["499.58276315"]
},
{
"name":"Apr.2022",
"values":["382.02252833"]
},
{
"name":"May.2022",
"values":["552.62357179"]
},
{
"name":"Jun.2022",
"values":["493.36789117"]
},
{
"name":"Jul.2022",
"values":["397.41613531"]
},
{
"name":"Aug.2022",
"values":["311.83847078"]
},
{
"name":"Sep.2022",
"values":["451.84773624"]
},
{
"name":"Oct.2022",
"values":["467.11979287"]
},
{
"name":"Nov.2022",
"values":["374.20637064"]
},
{
"name":"Dec.2022",
"values":["511.13832521"]
}
]
}
Shell cwd was reset to C:\Users\[usuario]\AppData\Local\Temp\tarea4_modoA_kpo95hhw
```
</details>

> 🔧 **Bash** `{"command": "python -c \"print(sum([499.89478773,436.83405271,499.58276315,382.02252833,552.62357179,493.36789117,397.41613531,311.83847078,451.84773624,467.11979287,374.20637064,511.13832521]))\""}`

<details><summary>Resultado de la herramienta</summary>

```text
5377.89242593
Shell cwd was reset to C:\Users\[usuario]\AppData\Local\Temp\tarea4_modoA_kpo95hhw
```
</details>

#### 🤖 Claude · 2026-11-06 05:28 UTC

Según el BCRP, las exportaciones de productos tradicionales mineros de Arequipa en 2022 sumaron unos 5 378 millones de dólares FOB.

La serie es RD38191BM, «Exportaciones por grupo de productos de Arequipa (Valores FOB en millones US$) – Productos tradicionales – Mineros». La consulté en la API de BCRPData y sumé los 12 valores mensuales de 2022:

| Mes | Millones US$ FOB |
|---|---|
| Ene | 499,89 |
| Feb | 436,83 |
| Mar | 499,58 |
| Abr | 382,02 |
| May | 552,62 |
| Jun | 493,37 |
| Jul | 397,42 |
| Ago | 311,84 |
| Sep | 451,85 |
| Oct | 467,12 |
| Nov | 374,21 |
| Dic | 511,14 |
| **Total** | **5 377,89** |

El BCRP no entrega esta serie con total anual, así que el total sale de mi suma de los valores mensuales.

RESPUESTA FINAL: ≈ 5 378 millones de US$ FOB (5 377,89) en exportaciones tradicionales mineras de Arequipa en 2022.

---

## Pregunta C1 · modo A

> **Pregunta:** Considerando la inversión bruta fija del gobierno nacional, los gobiernos regionales y los gobiernos locales sumada de 2020 a 2024 (BCRP), ¿qué porcentaje de esa inversión se ejecutó en Cajamarca, y qué porcentaje de la población pobre del Perú vivía en Cajamarca en 2024 (ENAHO)? ¿Cajamarca recibe una parte de la inversión mayor o menor que su parte de los pobres?

#### 🤖 Claude · 2026-11-06 05:28 UTC

Voy a revisar primero qué hay en la carpeta.

> 🔧 **Glob** `{"pattern": "**/*"}`

<details><summary>Resultado de la herramienta</summary>

```text
datos\catalogo_bcrp.csv
datos\966-Modulo02.zip
datos\966-Modulo34.zip
datos\peru_departamental_simple.geojson
.python-version
pyproject.toml
uv.lock
```
</details>

> 🔧 **Bash** `{"command": "cd datos; head -c 1500 catalogo_bcrp.csv; echo; wc -l catalogo_bcrp.csv; grep -i -c \"cajamarca\" catalogo_bcrp.csv; unzip -l 966-Modulo02.zip | head -20; unzip -l 966-Modulo34.zip | head -20"}`

<details><summary>Resultado de la herramienta</summary>

```text
Código de serie;Categoría de serie;Grupo de serie;Nombre de serie;Descripción de la serie;Metodología de la serie;Unidad de medida;Escala;Geografía (País, Región de Perú);Fuente;Frecuencia;Fecha de creación;Grupo de publicación;Área que publica;Fecha de actualización;Fecha de inicio;Fecha de fin;Memo;

PN00001MM;Sociedades creadoras de depósito;Cuentas monetarias de las sociedades creadoras de depósito;Activos Externos Netos de Corto Plazo (millones S/);https://estadisticas.bcrp.gob.pe/estadisticas/series/documentos/bcrpdataapi.pdf;https://estadisticas.bcrp.gob.pe/estadisticas/series/documentos/bcrpdataapi.pdf;;;;BCRP;Mensual;2022-03-24;Sistema financiero y empresas bancarias y expectativas sobre condiciones crediticias;Departamento de Estadísticas Monetarias;2026-10-23;Ene-1992;Dic-2025;;

PN00002MM;Sociedades creadoras de depósito;Cuentas monetarias de las sociedades creadoras de depósito;Activos Externos Netos de Corto Plazo (millones US$);;;;;;BCRP;Mensual;2022-03-24;Sistema financiero y empresas bancarias y expectativas sobre condiciones crediticias;Departamento de Estadísticas Monetarias;2026-10-23;Ene-1992;Dic-2025;;

PN00003MM;Sociedades creadoras de depósito;Cuentas monetarias de las sociedades creadoras de depósito;Activos Externos Netos de Corto Plazo - Activos (millones US$);;;;;;BCRP;Mensual;2022-03-24;Sistema financiero y empresas bancarias y expectativas sobre condiciones crediticias;Departamento de Estadísticas Monetarias;2026-10-23;Ene-19
17168 catalogo_bcrp.csv
184
Archive:  966-Modulo02.zip
  Length      Date    Time    Name
---------  ---------- -----   ----
        0  2025-05-07 14:43   966-Modulo02/
   201079  2024-06-18 10:39   966-Modulo02/CED-01-200-2024.pdf
   395343  2021-05-07 11:05   966-Modulo02/Criterios para codificar Ocupaciones Peligrosas.pdf
  3940690  2025-05-16 14:36   966-Modulo02/Diccionario2024.pdf
 10217755  2025-05-07 14:39   966-Modulo02/enaho01-2024-200.dta
   349153  2020-05-11 21:36   966-Modulo02/enaho_tabla_ciuo_88.dta
    56727  2020-05-11 21:36   966-Modulo02/enaho_tabla_cno_2015.dta
   487444  2024-02-06 18:57   966-Modulo02/FichaTecnica.pdf
---------                     -------
 15648191                     8 files
Archive:  966-Modulo34.zip
  Length      Date    Time    Name
---------  ---------- -----   ----
        0  2026-05-14 09:56   966-Modulo34/
    24486  2025-05-07 19:18   966-Modulo34/ConstVarGasto-Metodologia actualizada.zip
   254671  2025-05-05 19:34   966-Modulo34/DefinicionValoresMonetario
… [620 caracteres más omitidos]
```
</details>

> 🔧 **Bash** `{"command": "cd datos; grep -i \"inversi[oó]n bruta fija\" catalogo_bcrp.csv | grep -i -E \"gobierno|regional|local\" | cut -d';' -f1,4,7,9,11,16,17 | head -60"}`

<details><summary>Resultado de la herramienta</summary>

```text
RD14092DM;Amazonas;;RE;Mensual;Ene-2008;Dic-2025
RD14093DM;Ancash;;RE;Mensual;Ene-2008;Dic-2025
RD14094DM;Apurímac;;RE;Mensual;Ene-2008;Dic-2025
RD14095DM;Arequipa;;RE;Mensual;Ene-2008;Dic-2025
RD14096DM;Ayacucho;;RE;Mensual;Ene-2008;Dic-2025
RD14097DM;Cajamarca;;RE;Mensual;Ene-2008;Dic-2025
RD14098DM;Callao;;RE;Mensual;Ene-2008;Dic-2025
RD14099DM;Cusco;;RE;Mensual;Ene-2008;Dic-2025
RD14100DM;Huancavelica;;RE;Mensual;Ene-2008;Dic-2025
RD14101DM;Huánuco;;RE;Mensual;Ene-2008;Dic-2025
RD14102DM;Ica;;RE;Mensual;Ene-2008;Dic-2025
RD14103DM;Junín;;RE;Mensual;Ene-2008;Dic-2025
RD14104DM;La Libertad;;RE;Mensual;Ene-2008;Dic-2025
RD14105DM;Lambayeque;;RE;Mensual;Ene-2008;Dic-2025
RD14106DM;Lima;;RE;Mensual;Ene-2008;Dic-2025
RD14107DM;Loreto;;RE;Mensual;Ene-2008;Dic-2025
RD14108DM;Madre de Dios;;RE;Mensual;Ene-2008;Dic-2025
RD14109DM;Moquegua;;RE;Mensual;Ene-2008;Dic-2025
RD14110DM;Pasco;;RE;Mensual;Ene-2008;Dic-2025
RD14111DM;Piura;;RE;Mensual;Ene-2008;Dic-2025
RD14112DM;Puno;;RE;Mensual;Ene-2008;Dic-2025
RD14113DM;San Martín;;RE;Mensual;Ene-2008;Dic-2025
RD14114DM;Tacna;;RE;Mensual;Ene-2008;Dic-2025
RD14115DM;Tumbes;;RE;Mensual;Ene-2008;Dic-2025
RD14116DM;Ucayali;;RE;Mensual;Ene-2008;Dic-2025
RD14117DM;Total;;RE;Mensual;Ene-2008;Dic-2025
RD14118DM;Amazonas;;RE;Mensual;Ene-2008;Dic-2025
RD14119DM;Ancash;;RE;Mensual;Ene-2008;Dic-2025
RD14120DM;Apurímac;;RE;Mensual;Ene-2008;Dic-2025
RD14121DM;Arequipa;;RE;Mensual;Ene-2008;Dic-2025
RD14122DM;Ayacucho;;RE;Mensual;Ene-2008;Dic-2025
RD14123DM;Cajamarca;;RE;Mensual;Ene-2008;Dic-2025
RD14124DM;Callao;;RE;Mensual;Ene-2008;Dic-2025
RD14125DM;Cusco;;RE;Mensual;Ene-2008;Dic-2025
RD14126DM;Huancavelica;;RE;Mensual;Ene-2008;Dic-2025
RD14127DM;Huánuco;;RE;Mensual;Ene-2008;Dic-2025
RD14128DM;Ica;;RE;Mensual;Ene-2008;Dic-2025
RD14129DM;Junín;;RE;Mensual;Ene-2008;Dic-2025
RD14130DM;La Libertad;;RE;Mensual;Ene-2008;Dic-2025
RD14131DM;Lambayeque;;RE;Mensual;Ene-2008;Dic-2025
RD14132DM;Lima;;RE;Mensual;Ene-2008;Dic-2025
RD14133DM;Loreto;;RE;Mensual;Ene-2008;Dic-2025
RD14134DM;Madre de Dios;;RE;Mensual;Ene-2008;Dic-2025
RD14135DM;Moquegua;;RE;Mensual;Ene-2008;Dic-2025
RD14136DM;Pasco;;RE;Mensual;Ene-2008;Dic-2025
RD14137DM;Piura;;RE;Mensual;Ene-2008;Dic-2025
RD14138DM;Puno;;RE;Mensual;Ene-2008;Dic-2025
RD14139DM;San Martín;;RE;Mensual;Ene-2008;Dic-2025
RD14140DM;Tacna;;RE;Mensual;Ene-2008;Dic-2025
RD14141DM;Tumbes;;RE;Mensual;Ene-2008;Dic-2025
RD14142DM;Ucayali;;RE;Mensual;Ene-2008;Dic-2025
RD14143DM;Total;;RE;Mensual;Ene-2008;Dic-2025

… [474 caracteres más omitidos]
```
</details>

#### 🤖 Claude · 2026-11-06 05:28 UTC

Necesito ver los grupos/categorías de estas series.

> 🔧 **Bash** `{"command": "cd datos; grep -i \"inversi[oó]n bruta fija\" catalogo_bcrp.csv | grep -E \"^RD1(409[2-9]|41[0-9][0-9])\" | awk -F';' '{print $1\";\"$2\";\"$3\";\"$4}' | grep -E \"Cajamarca|Total\""}`

<details><summary>Resultado de la herramienta</summary>

```text
RD14097DM;Sector público;Inversión bruta fija del gobierno nacional por departamentos (millones S/);Cajamarca
RD14117DM;Sector público;Inversión bruta fija del gobierno nacional por departamentos (millones S/);Total
RD14123DM;Sector público;Inversión bruta fija de gobiernos locales por departamentos (millones S/);Cajamarca
RD14143DM;Sector público;Inversión bruta fija de gobiernos locales por departamentos (millones S/);Total
RD14149DM;Sector público;Inversión bruta fija de los gobiernos regionales (millones S/);Cajamarca
RD14170DM;Sector público;Inversión bruta fija de los gobiernos regionales (millones S/);Total
Shell cwd was reset to C:\Users\[usuario]\AppData\Local\Temp\tarea4_modoA_hk61ckqv
```
</details>

> 🔧 **Bash** `{"command": "cd /tmp; curl -s -m 60 \"https://estadisticas.bcrp.gob.pe/estadisticas/series/api/RD14097DM-RD14117DM-RD14123DM-RD14143DM-RD14149DM-RD14170DM/json/2020-1/2024-12\" -o b.json; head -c 800 b.json"}`

<details><summary>Resultado de la herramienta</summary>

```text
{
"config":
{
"title":"Inversión bruta fija del gobierno nacional por departamentos (millones S/)",
"series":
[
{
"name":"Inversión bruta fija del gobierno nacional por departamentos (millones S/) - Cajamarca",
"dec":"0"
},
{
"name":"Inversión bruta fija del gobierno nacional por departamentos (millones S/) - Total",
"dec":"0"
},
{
"name":"Inversión bruta fija de gobiernos locales por departamentos (millones S/) - Cajamarca",
"dec":"0"
},
{
"name":"Inversión bruta fija de gobiernos locales por departamentos (millones S/) - Total",
"dec":"0"
},
{
"name":"Inversión bruta fija de los gobiernos regionales (millones S/) - Cajamarca",
"dec":"0"
},
{
"name":"Inversión bruta fija de los gobiernos regionales (millones S/) - Total",
"dec":"0"
}]
},
"periods":
[
{
"name":"Ene.2020",
"values":[
Shell cwd was reset to C:\Users\[usuario]\AppData\Local\Temp\tarea4_modoA_hk61ckqv
```
</details>

> 🔧 **Bash** `{"command": "cd /tmp; python -c \"\nimport json\nd=json.load(open('b.json',encoding='utf-8'))\np=d['periods'];print(len(p))\ns=[0]*6;bad=0\nfor x in p:\n    for i,v in enumerate(x['values']):\n        try:s[i]+=float(v)\n        except: bad+=1\nprint(s,bad)\nc=s[0]+s[2]+s[4];t=s[1]+s[3]+s[5];print(c,t,c/t*100)\n\"\ncd ~ 2>/dev/null; cd \"C:/Users/[usuario]/AppData/Local/Temp/tarea4_modoA_hk61ckqv\"; cat pyproject.toml"}`

<details><summary>Resultado de la herramienta</summary>

```text
60

[2458.9979359999998, 93553.32018999998, 5127.587285, 85152.95139100001, 2374.302138, 47659.067349000004] 0

9960.887359 226365.33893000003 4.4003589092233995

[project]
name = "tarea-4-agente-inversion-pobreza"
version = "0.1.0"
description = "Agente de investigación: MCP del BCRP y Skills de la ENAHO 2024 para comparar el reparto de la inversión pública con el de la pobreza"
readme = "README.md"
requires-python = ">=3.14"
dependencies = [
    "fastmcp>=4,<5",
    "geopandas>=1.2.0",
    "httpx",
    "matplotlib>=3.11.2",
    "pandas>=3.1.0",
    "pyarrow>=26.0.0",
]

[dependency-groups]
dev = ["pytest"]

[tool.pytest.ini_options]
testpaths = ["mcp"]
Shell cwd was reset to C:\Users\[usuario]\AppData\Local\Temp\tarea4_modoA_hk61ckqv
```
</details>

> 🔧 **Bash** `{"command": "cd /tmp; mkdir -p enh; cd enh; unzip -oq \"C:/Users/[usuario]/AppData/Local/Temp/tarea4_modoA_hk61ckqv/datos/966-Modulo34.zip\" \"966-Modulo34/sumaria-2024.dta\"; cd /tmp; python -c \"\nimport pandas as pd\nd=pd.read_stata('enh/966-Modulo34/sumaria-2024.dta',convert_categoricals=False)\nprint(d.shape);print([c for c in d.columns if c in('pobreza','factor07','mieperho','ubigeo','dominio','estrato')])\nd['dep']=d.ubigeo.astype(str).str.zfill(6).str[:2]\nd['w']=d.factor07*d.mieperho\nprint(d.pobreza.value_counts())\np=d[d.pobreza.isin([1,2])]\ng=p.groupby('dep').w.sum();print(g['06'],g.sum(),g['06']/g.sum()*100)\na=d.groupby('dep').w.sum();print(d.w.sum(), a['06']/d.w.sum()*100, g['06']/a['06']*100)\n\""}`

<details><summary>Resultado de la herramienta</summary>

```text
(33691, 163)

['ubigeo', 'dominio', 'estrato', 'mieperho', 'pobreza', 'factor07']

pobreza

3    26879

2     5224

1     1588

Name: count, dtype: int64

699670.75 9.510145e+06 7.357099

3.44827e+07 4.508306 45.006897
Shell cwd was reset to C:\Users\[usuario]\AppData\Local\Temp\tarea4_modoA_hk61ckqv
```
</details>

#### 🤖 Claude · 2026-11-06 05:28 UTC

Cajamarca recibe una parte de la inversión menor que su parte de los pobres: 4,4 % de la inversión frente a 7,4 % de los pobres.

**Inversión bruta fija, 2020–2024 (BCRP, millones de S/, suma de los 60 meses)**

Descargué las series departamentales del BCRP por su API. Los códigos son RD14097DM/RD14117DM, RD14123DM/RD14143DM y RD14149DM/RD14170DM.

| Nivel de gobierno | Cajamarca | Total nacional |
|---|---|---|
| Gobierno nacional | 2 459,0 | 93 553,3 |
| Gobiernos regionales | 2 374,3 | 47 659,1 |
| Gobiernos locales | 5 127,6 | 85 153,0 |
| **Suma** | **9 960,9** | **226 365,3** |

Cajamarca ejecutó 9 960,9 / 226 365,3 = **4,40 %** de la inversión.

**Pobreza 2024 (ENAHO, Sumaria 2024)**

Conté como pobres a las personas con `pobreza` igual a 1 (pobre extremo) o 2 (pobre no extremo). Ponderé por `factor07 × mieperho` y asigné el departamento con los dos primeros dígitos del ubigeo (06 = Cajamarca). Eso da unos 700 mil pobres en Cajamarca de unos 9,51 millones en todo el país, es decir **7,36 %** de los pobres del Perú. Como referencia, Cajamarca tiene el 4,5 % de la población total y su tasa de pobreza es de 45,0 %.

**Comparación**

La inversión de Cajamarca es unos 2,96 puntos porcentuales menor que su parte de los pobres. La razón entre ambas es 4,40 / 7,36 ≈ 0,60.

**Salvedades**
- La inversión es la ejecutada en el departamento, no la que corresponde a su población. Parte de la inversión del gobierno nacional se registra por departamento según el BCRP, pero no verifiqué cómo se asigna la que sirve a varias regiones.
- Sumé los tres niveles en soles corrientes, sin deflactar. No usé los totales de pobreza oficiales publicados por el INEI. Mi cálculo viene directamente de la base microdatos.

RESPUESTA FINAL: Cajamarca ejecutó ≈4,40 % de la inversión bruta fija (gobierno nacional + regionales + locales, 2020–2024) y concentraba ≈7,36 % de los pobres del Perú en 2024; recibe una parte MENOR que su parte de los pobres.

---

## Pregunta C2 · modo A

> **Pregunta:** Tomando los 5 departamentos con mayor pobreza monetaria en 2024 según la ENAHO, ¿qué porcentaje de la población pobre del país vivía en ellos y qué porcentaje de la inversión bruta fija pública 2020-2024 (gobierno nacional, regionales y locales, BCRP) se ejecutó en ellos? ¿Qué se puede concluir y qué no?

#### 🤖 Claude · 2026-11-06 05:28 UTC

Voy a revisar primero qué hay en la carpeta.

> 🔧 **Glob** `{"pattern": "**/*"}`

<details><summary>Resultado de la herramienta</summary>

```text
datos\catalogo_bcrp.csv
datos\966-Modulo02.zip
datos\966-Modulo34.zip
datos\peru_departamental_simple.geojson
.python-version
pyproject.toml
uv.lock
```
</details>

> 🔧 **Bash** `{"command": "cd datos; head -c 1500 catalogo_bcrp.csv; echo; wc -l catalogo_bcrp.csv; unzip -l 966-Modulo02.zip | head -30; unzip -l 966-Modulo34.zip | head -30; cat ../pyproject.toml"}`

<details><summary>Resultado de la herramienta</summary>

```text
Código de serie;Categoría de serie;Grupo de serie;Nombre de serie;Descripción de la serie;Metodología de la serie;Unidad de medida;Escala;Geografía (País, Región de Perú);Fuente;Frecuencia;Fecha de creación;Grupo de publicación;Área que publica;Fecha de actualización;Fecha de inicio;Fecha de fin;Memo;

PN00001MM;Sociedades creadoras de depósito;Cuentas monetarias de las sociedades creadoras de depósito;Activos Externos Netos de Corto Plazo (millones S/);https://estadisticas.bcrp.gob.pe/estadisticas/series/documentos/bcrpdataapi.pdf;https://estadisticas.bcrp.gob.pe/estadisticas/series/documentos/bcrpdataapi.pdf;;;;BCRP;Mensual;2022-03-24;Sistema financiero y empresas bancarias y expectativas sobre condiciones crediticias;Departamento de Estadísticas Monetarias;2026-10-23;Ene-1992;Dic-2025;;

PN00002MM;Sociedades creadoras de depósito;Cuentas monetarias de las sociedades creadoras de depósito;Activos Externos Netos de Corto Plazo (millones US$);;;;;;BCRP;Mensual;2022-03-24;Sistema financiero y empresas bancarias y expectativas sobre condiciones crediticias;Departamento de Estadísticas Monetarias;2026-10-23;Ene-1992;Dic-2025;;

PN00003MM;Sociedades creadoras de depósito;Cuentas monetarias de las sociedades creadoras de depósito;Activos Externos Netos de Corto Plazo - Activos (millones US$);;;;;;BCRP;Mensual;2022-03-24;Sistema financiero y empresas bancarias y expectativas sobre condiciones crediticias;Departamento de Estadísticas Monetarias;2026-10-23;Ene-19
17168 catalogo_bcrp.csv
Archive:  966-Modulo02.zip
  Length      Date    Time    Name
---------  ---------- -----   ----
        0  2025-05-07 14:43   966-Modulo02/
   201079  2024-06-18 10:39   966-Modulo02/CED-01-200-2024.pdf
   395343  2021-05-07 11:05   966-Modulo02/Criterios para codificar Ocupaciones Peligrosas.pdf
  3940690  2025-05-16 14:36   966-Modulo02/Diccionario2024.pdf
 10217755  2025-05-07 14:39   966-Modulo02/enaho01-2024-200.dta
   349153  2020-05-11 21:36   966-Modulo02/enaho_tabla_ciuo_88.dta
    56727  2020-05-11 21:36   966-Modulo02/enaho_tabla_cno_2015.dta
   487444  2024-02-06 18:57   966-Modulo02/FichaTecnica.pdf
---------                     -------
 15648191                     8 files
Archive:  966-Modulo34.zip
  Length      Date    Time    Name
---------  ---------- -----   ----
        0  2026-05-14 09:56   966-Modulo34/
    24486  2025-05-07 19:18   966-Modulo34/ConstVarGasto-Metodologia actualizada.zip
   254671  2025-05-05 19:34   966-Modulo34/DefinicionValoresMonetariosBas
… [1116 caracteres más omitidos]
```
</details>

> 🔧 **Bash** `{"command": "cd datos; grep -i \"bruta fija\" catalogo_bcrp.csv | grep -i -E \"departamento|región|regional|gobierno\" | cut -c1-400 | head -40; python --version; which uv"}`

<details><summary>Resultado de la herramienta</summary>

```text
PN02521AQ;PBI gasto;Producto bruto interno por tipo de gasto (variaciones porcentuales reales anualizadas);Demanda Interna - Inversión Bruta Interna - Inversión Bruta Fija;;;;;;INEI, BCRP;Trimestral;2022-02-18;Demanda y oferta global, balanza de pagos, sector público y monetario;Departamento de Indicadores de la Actividad Economía;2026-08-20;T1-1980;T4-2025;;
PN02522AQ;PBI gasto;Producto bruto interno por tipo de gasto (variaciones porcentuales reales anualizadas);Demanda Interna - Inversión Bruta Interna - Inversión Bruta Fija - Privada;;;;;;INEI, BCRP;Trimestral;2022-02-18;Demanda y oferta global, balanza de pagos, sector público y monetario;Departamento de Indicadores de la Actividad Economía;2026-08-20;T1-1980;T4-2025;;
PN02523AQ;PBI gasto;Producto bruto interno por tipo de gasto (variaciones porcentuales reales anualizadas);Demanda Interna - Inversión Bruta Interna - Inversión Bruta Fija - Pública;;;;;;INEI, BCRP;Trimestral;2022-02-18;Demanda y oferta global, balanza de pagos, sector público y monetario;Departamento de Indicadores de la Actividad Economía;2026-08-20;T1-1980;T4-2025;;
PN02532AQ;PBI gasto;Producto bruto interno por tipo de gasto (millones S/ 2007);Demanda Interna - Inversión Bruta Interna - Inversión Bruta Fija;;;;;;INEI, BCRP;Trimestral;2022-02-18;Demanda y oferta global, balanza de pagos, sector público y monetario;Departamento de Indicadores de la Actividad Economía;2026-08-20;T1-1979;T4-2025;;
PN02533AQ;PBI gasto;Producto bruto interno por tipo de gasto (millones S/ 2007);Demanda Interna - Inversión Bruta Interna - Inversión Bruta Fija - Privada;;;;;;INEI, BCRP;Trimestral;2022-02-18;Demanda y oferta global, balanza de pagos, sector público y monetario;Departamento de Indicadores de la Actividad Economía;2026-08-20;T1-1979;T4-2025;;
PN02534AQ;PBI gasto;Producto bruto interno por tipo de gasto (millones S/ 2007);Demanda Interna - Inversión Bruta Interna - Inversión Bruta Fija - Pública;;;;;;INEI, BCRP;Trimestral;2022-02-18;Demanda y oferta global, balanza de pagos, sector público y monetario;Departamento de Indicadores de la Actividad Economía;2026-08-20;T1-1979;T4-2025;;
PN02544AQ;PBI gasto;Producto bruto interno por tipo de gasto (millones S/);Demanda Interna - Inversión Bruta Interna - Inversión Bruta Fija;;;;;;INEI, BCRP;Trimestral;2022-02-18;Demanda y oferta global, balanza de pagos, sector público y monetario;Departamento de Indicadores de la Actividad Economía;2026-08-20;T1-1980;T4-2025;;
PN02545AQ;PBI gasto;Producto bruto inte
… [11941 caracteres más omitidos]
```
</details>

#### 🤖 Claude · 2026-11-06 05:28 UTC

Busco series por departamento para inversión pública.

> 🔧 **Bash** `{"command": "cd datos; python - <<'E'\nimport csv\nr=list(csv.reader(open('catalogo_bcrp.csv',encoding='utf-8-sig'),delimiter=';'))\nh=r[0]\nfor x in r[1:]:\n    t=' '.join(x).lower()\n    if ('inversión' in t or 'inversion' in t) and ('gobierno' in t or 'regional' in t or 'local' in t) and ('departament' in t or 'región' in t or 'regional' in t):\n        print(x[0],'|',x[2],'|',x[3],'|',x[8],'|',x[10],x[15],x[16])\nE\nls ~/.claude 2>/dev/null | head; ls .."}`

<details><summary>Resultado de la herramienta</summary>

```text
<persisted-output>
Output too large (33.3KB). Full output saved to: C:\Users\[usuario]\.claude\projects\C--Users-[usuario]-AppData-Local-Temp-tarea4-modoA-hwsvq2qn\ec29da9d-c666-48c4-b90f-8c5a9b091b6f\tool-results\b8uvwzhyo.txt

Preview (first 2KB):
PN01186MM | Sistema privado de pensiones | Cartera de Inversiones - Valores Gubernamentales - gobierno central (composici�n porcentual) |  | Mensual Ene-2002 Dic-2025

PN03049FQ | Ahorro en cuenta corriente del sector p�blico no financiero (millones S/) | Gastos de Capital - Inversi�n P�blica |  | Trimestral T1-1990 T4-2025

PN03105FQ | Ahorro en cuenta corriente del sector p�blico no financiero (porcentaje del PBI) | Gastos de Capital - Inversi�n P�blica |  | Trimestral T1-1990 T4-2025

PM06319MA | Sistema privado de pensiones | Composici�n del Portafolio de Inversiones - Valores gubernamentales - Valores del gobierno central (porcentaje) |  | Anual 2003 2025

PM10075FA | Operaciones del sector p�blico no financiero | Inversi�n P�blica (millones S/) |  | Anual 1970 2025

PM10081FA | Operaciones del sector p�blico no financiero (porcentaje del PBI) | Inversi�n P�blica |  | Anual 1970 2025

RD14092DM | Inversi�n bruta fija del gobierno nacional por departamentos (millones S/) | Amazonas | RE | Mensual Ene-2008 Dic-2025

RD14093DM | Inversi�n bruta fija del gobierno nacional por departamentos (millones S/) | Ancash | RE | Mensual Ene-2008 Dic-2025

RD14094DM | Inversi�n bruta fija del gobierno nacional por departamentos (millones S/) | Apur�mac | RE | Mensual Ene-2008 Dic-2025

RD14095DM | Inversi�n bruta fija del gobierno nacional por departamentos (millones S/) | Arequipa | RE | Mensual Ene-2008 Dic-2025

RD14096DM | Inversi�n bruta fija del gobierno nacional por departamentos (millones S/) | Ayacucho | RE | Mensual Ene-2008 Dic-2025

RD14097DM | Inversi�n bruta fija del gobierno nacional por departamentos (millones S/) | Cajamarca | RE | Mensual Ene-2008 Dic-2025

RD14098DM | Inversi�n bruta fija del gobierno nacional por departamentos (millones S/) | Callao | RE | Mensual Ene-2008 Dic-2025

RD14099DM | Inversi�n bruta fija del gobierno nacional por departamentos (millones S/) | Cusco | RE | Mensual Ene-2008 Dic-2025

...
</persisted-output>
Shell cwd was reset to C:\Users\[usuario]\AppData\Local\Temp\tarea4_modoA_hwsvq2qn
```
</details>

> 🔧 **Bash** `{"command": "cd datos; python - <<'E'\nimport csv,re\nr=list(csv.reader(open('catalogo_bcrp.csv',encoding='utf-8-sig'),delimiter=';'))\ng={}\nfor x in r[1:]:\n    if 'nversi' in x[2] and 'departamentos' in x[2]:\n        g.setdefault(x[2],[]).append((x[0],x[3],x[10],x[15],x[16]))\nfor k,v in g.items(): print(k,len(v),v[0],v[-1])\nE\npython -c \"\nimport urllib.request;print(urllib.request.urlopen('https://estadisticas.bcrp.gob.pe/estadisticas/series/api/RD14092DM/json/2020-1/2024-12',timeout=20).read()[:500])\""}`

<details><summary>Resultado de la herramienta</summary>

```text
Inversi�n bruta fija del gobierno nacional por departamentos (millones S/) 78 ('RD14092DM', 'Amazonas', 'Mensual', 'Ene-2008', 'Dic-2025') ('RD16682DA', 'Total (millones de soles)', 'Anual', '2008', '2025')

Inversi�n bruta fija de gobiernos locales por departamentos (millones S/) 78 ('RD14118DM', 'Amazonas', 'Mensual', 'Ene-2008', 'Dic-2025') ('RD16708DA', 'Total (millones de soles)', 'Anual', '2008', '2025')

b'{\n"config":\n{\n"title":"Inversi\xc3\xb3n bruta fija del gobierno nacional por departamentos (millones S/)",\n"series":\n[\n{\n"name":"Inversi\xc3\xb3n bruta fija del gobierno nacional por departamentos (millones S/) - Amazonas",\n"dec":"0"\n}]\n},\n"periods":\n[\n{\n"name":"Ene.2020",\n"values":["4.015005"]\n},\n{\n"name":"Feb.2020",\n"values":["9.330231"]\n},\n{\n"name":"Mar.2020",\n"values":["5.281877"]\n},\n{\n"name":"Abr.2020",\n"values":["72.022897"]\n},\n{\n"name":"May.2020",\n"values":["3.633596"]\n},\n{\n"name":"Jun.2020",\n"values'
Shell cwd was reset to C:\Users\[usuario]\AppData\Local\Temp\tarea4_modoA_hwsvq2qn
```
</details>

> 🔧 **Bash** `{"command": "cd datos; python - <<'E'\nimport csv\nr=list(csv.reader(open('catalogo_bcrp.csv',encoding='utf-8-sig'),delimiter=';'))\ns=set()\nfor x in r[1:]:\n    if 'nversi' in x[2] and ('departamento' in x[2].lower()) : s.add(x[2])\nprint(s)\nfor x in r[1:]:\n    if 'gobierno nacional por departamentos' in x[2] or 'gobiernos locales por departamentos' in x[2] or 'regionales por departamentos' in x[2]:\n        if x[10]=='Anual': print(x[0],x[2][:45],x[3])\nE"}`

<details><summary>Resultado de la herramienta</summary>

```text
{'Inversi�n bruta fija del gobierno nacional por departamentos (millones S/)', 'Inversi�n bruta fija de gobiernos locales por departamentos (millones S/)'}

RD16551DA Gastos no financieros de gobiernos locales po Amazonas (millones de soles)

RD16552DA Gastos no financieros de gobiernos locales po Ancash (millones de soles)

RD16553DA Gastos no financieros de gobiernos locales po Apur�mac (millones de soles)

RD16554DA Gastos no financieros de gobiernos locales po Arequipa (millones de soles)

RD16555DA Gastos no financieros de gobiernos locales po Ayacucho (millones de soles)

RD16556DA Gastos no financieros de gobiernos locales po Cajamarca (millones de soles)

RD16557DA Gastos no financieros de gobiernos locales po Callao (millones de soles)

RD16558DA Gastos no financieros de gobiernos locales po Cusco (millones de soles)

RD16559DA Gastos no financieros de gobiernos locales po Huancavelica (millones de soles)

RD16560DA Gastos no financieros de gobiernos locales po Hu�nuco (millones de soles)

RD16561DA Gastos no financieros de gobiernos locales po Ica (millones de soles)

RD16562DA Gastos no financieros de gobiernos locales po Jun�n (millones de soles)

RD16563DA Gastos no financieros de gobiernos locales po La Libertad (millones de soles)

RD16564DA Gastos no financieros de gobiernos locales po Lambayeque (millones de soles)

RD16565DA Gastos no financieros de gobiernos locales po Lima (millones de soles)

RD16566DA Gastos no financieros de gobiernos locales po Loreto (millones de soles)

RD16567DA Gastos no financieros de gobiernos locales po Madre de Dios (millones de soles)

RD16568DA Gastos no financieros de gobiernos locales po Moquegua (millones de soles)

RD16569DA Gastos no financieros de gobiernos locales po Pasco (millones de soles)

RD16570DA Gastos no financieros de gobiernos locales po Piura (millones de soles)

RD16571DA Gastos no financieros de gobiernos locales po Puno (millones de soles)

RD16572DA Gastos no financieros de gobiernos locales po San Mart�n (millones de soles)

RD16573DA Gastos no financieros de gobiernos locales po Tacna (millones de soles)

RD16574DA Gastos no financieros de gobiernos locales po Tumbes (millones de soles)

RD16575DA Gastos no financieros de gobiernos locales po Ucayali (millones de soles)

RD16576DA Gastos no financieros de gobiernos locales po Total (millones de soles)

RD16577DA Gastos no financieros de gobiernos locales po Amazonas (var% anual)

RD16578DA Gastos no financieros de gobiernos locales
… [6404 caracteres más omitidos]
```
</details>

#### 🤖 Claude · 2026-11-06 05:28 UTC

Busco ahora gobiernos regionales.

> 🔧 **Bash** `{"command": "cd datos; python - <<'E'\nimport csv\nr=list(csv.reader(open('catalogo_bcrp.csv',encoding='utf-8-sig'),delimiter=';'))\ns={}\nfor x in r[1:]:\n    t=x[2].lower()\n    if 'regional' in t and ('nversi' in t or 'capital' in t or 'formaci' in t):\n        s.setdefault(x[2],[]).append((x[0],x[3],x[10],x[8]))\nfor k,v in s.items(): print(k,len(v),v[:2])\nE"}`

<details><summary>Resultado de la herramienta</summary>

```text
Inversi�n bruta fija de los gobiernos regionales (millones S/) 81 [('RD14144DM', 'Amazonas', 'Mensual', 'RE'), ('RD14145DM', 'Ancash', 'Mensual', 'RE')]
Shell cwd was reset to C:\Users\[usuario]\AppData\Local\Temp\tarea4_modoA_hwsvq2qn
```
</details>

> 🔧 **Bash** `{"command": "mkdir -p /tmp/w && cd /tmp/w && cat > a.py <<'E'\nimport csv,json,urllib.request,time\nr=list(csv.reader(open(r'C:/Users/[usuario]/AppData/Local/Temp/tarea4_modoA_hwsvq2qn/datos/catalogo_bcrp.csv',encoding='utf-8-sig'),delimiter=';'))\nniv={'Inversión bruta fija del gobierno nacional por departamentos (millones S/)':'GN','Inversión bruta fija de gobiernos locales por departamentos (millones S/)':'GL','Inversión bruta fija de los gobiernos regionales (millones S/)':'GR'}\nout={}\nfor x in r[1:]:\n    if x[2] in niv and x[10]=='Mensual' and x[0].endswith('DM'):\n        u=f'https://estadisticas.bcrp.gob.pe/estadisticas/series/api/{x[0]}/json/2020-1/2024-12'\n        for i in range(3):\n            try: d=json.load(urllib.request.urlopen(u,timeout=30));break\n            except Exception as e: time.sleep(1)\n        v=[float(p['values'][0]) for p in d['periods'] if p['values'][0] not in ('n.d.','')]\n        out[(niv[x[2]],x[3])]=(sum(v),len(d['periods']),len(v))\nimport pandas as pd\ndf=pd.Series({k:v[0] for k,v in out.items()}).unstack(0)\nprint(df.round(1).to_string()); print({k:v[1:] for k,v in out.items() if v[1]!=60 or v[2]!=60})\ndf.to_pickle('inv.pkl')\nE\npython a.py"}`

<details><summary>Resultado de la herramienta</summary>

```text
                                          GL       GN       GR

Amazonas                              1506.7   1707.7   1706.9

Ancash                                7375.3   7133.0   1409.7

Apur�mac                              2978.2   1385.0   1555.8

Arequipa                              6004.0   1452.7   2862.7

Ayacucho                              3487.6   1229.1   2627.8

Cajamarca                             5127.6   2459.0   2374.3

Callao                                 705.3   4383.4    754.4

Cusco                                12579.6   5245.8   3536.7

Huancavelica                          1903.2   1123.7   1199.9

Hu�nuco                               2072.1   2246.7   1463.0

Ica                                   2727.7   2221.3   1502.3

Jun�n                                 2707.6   1935.6   2929.7

La Libertad                           4825.3   4766.9   1764.9

Lambayeque                            1740.2   2391.0   2076.3

Lima                                  7632.9  34994.0   1515.7

Loreto                                2060.6   1831.3   3318.1

Madre de Dios                          341.2   1205.9    796.9

Moquegua                              2031.9    840.3   1014.6

Municipalidad Metropolitana de Lima      NaN      NaN    454.5

Pasco                                  798.9    696.5   1235.9

Piura                                 6450.3   5965.9   3776.4

Puno                                  3389.5   4306.5   2169.9

San Mart�n                            2398.9   1413.4   1834.6

Tacna                                 2493.1    670.6   1128.3

Total                                85153.0  93553.3  47659.1

Tumbes                                 680.6   1460.6    657.5

Ucayali                               1134.4    487.3   1992.3

{}
Shell cwd was reset to C:\Users\[usuario]\AppData\Local\Temp\tarea4_modoA_hwsvq2qn
```
</details>

> 🔧 **Bash** `{"command": "cd /tmp/w && mkdir -p z && cd z && unzip -oq \"C:/Users/[usuario]/AppData/Local/Temp/tarea4_modoA_hwsvq2qn/datos/966-Modulo34.zip\" \"966-Modulo34/sumaria-2024.dta\" && cd .. && cat > b.py <<'E'\nimport pandas as pd\nd=pd.read_stata('z/966-Modulo34/sumaria-2024.dta',convert_categoricals=False)\nprint([c for c in d.columns if c.lower() in('ubigeo','pobreza','factor07','mieperho','percepho','linea','dominio','estrato')])\nd.columns=d.columns.str.lower()\nd['dep']=d.ubigeo.astype(str).str.zfill(6).str[:2]\nd['pop']=d.factor07*d.mieperho\nd['pobre']=d.pobreza.isin([1,2])\ng=d.groupby('dep').apply(lambda x: pd.Series({'pob':x['pop'].sum(),'pobres':x.loc[x.pobre,'pop'].sum()}))\ng['tasa']=g.pobres/g.pob*100\ng['share']=g.pobres/g.pobres.sum()*100\nprint(g.sort_values('tasa',ascending=False).round(2).to_string()); print(g.sum(), g.pobres.sum()/g.pob.sum())\ng.to_pickle('pov.pkl')\nE\npython b.py"}`

<details><summary>Resultado de la herramienta</summary>

```text
['ubigeo', 'dominio', 'estrato', 'mieperho', 'percepho', 'linea', 'pobreza', 'factor07']

              pob        pobres       tasa      share

dep                                                  

06   1.554586e+06  6.996708e+05  45.009998   7.360000

16   1.129071e+06  4.851909e+05  42.970001   5.100000

21   1.586886e+06  6.337717e+05  39.939999   6.660000

19   3.277761e+05  1.277409e+05  38.970001   1.340000

10   9.266531e+05  3.610481e+05  38.959999   3.800000

07   1.142618e+06  3.868892e+05  33.860001   4.070000

09   5.431026e+05  1.814145e+05  33.400002   1.910000

05   7.754468e+05  2.540618e+05  32.759998   2.670000

20   1.988570e+06  6.335782e+05  31.860001   6.660000

13   2.080789e+06  6.281966e+05  30.190001   6.610000

25   5.584841e+05  1.511820e+05  27.070000   1.590000

15   1.127991e+07  3.053352e+06  27.070000  32.110001

24   2.619591e+05  7.047007e+04  26.900000   0.740000

01   4.423553e+05  1.139012e+05  25.750000   1.200000

23   3.807547e+05  9.133938e+04  23.990000   0.960000

03   4.941885e+05  1.184013e+05  23.959999   1.240000

02   1.212494e+06  2.761403e+05  22.770000   2.900000

22   9.474458e+05  2.086415e+05  22.020000   2.190000

08   1.409467e+06  2.613340e+05  18.540001   2.750000

12   1.450149e+06  2.682689e+05  18.500000   2.820000

04   1.421684e+06  2.244038e+05  15.780000   2.360000

14   1.349731e+06  1.895108e+05  14.040000   1.990000

17   1.659918e+05  1.850442e+04  11.150000   0.190000

18   1.983858e+05  2.175927e+04  10.970000   0.230000

11   8.542031e+05  5.137343e+04   6.010000   0.540000

pob       3.448270e+07

pobres    9.510145e+06

tasa      6.624587e+02

share     1.000000e+02

dtype: float32 0.27579468
Shell cwd was reset to C:\Users\[usuario]\AppData\Local\Temp\tarea4_modoA_hwsvq2qn
```
</details>

> 🔧 **Bash** `{"command": "cd /tmp/w && python - <<'E'\nimport pandas as pd\ninv=pd.read_pickle('inv.pkl'); pov=pd.read_pickle('pov.pkl')\ninv.index=[i.replace('�','?') for i in inv.index]\ntot=inv.loc['Total']; body=inv.drop('Total')\nprint('suma deptos vs total',body.sum().round(1).to_dict(),tot.round(1).to_dict())\ntop=['Cajamarca','Loreto','Puno','Pasco','Hu?nuco']\nt=body.loc[top]; t['T']=t.sum(axis=1); print(t.round(1))\nT=body.sum(axis=1)\ntt=body.sum().sum(); print('total',tt, 'top',t['T'].sum(), t['T'].sum()/tt*100)\nprint((t.sum()/body.sum()*100).round(2))\nprint('pob share',pov.loc[['06','16','21','19','10'],'pob'].sum()/pov.pob.sum()*100)\nE"}`

<details><summary>Resultado de la herramienta</summary>

```text
Exit code 1
suma deptos vs total {'GL': 85153.0, 'GN': 93553.3, 'GR': 47659.1} {'GL': 85153.0, 'GN': 93553.3, 'GR': 47659.1}

Traceback (most recent call last):

  File "<stdin>", line 7, in <module>

  File "C:\Users\[usuario]\Documents\GitHub\Python_Interm\Tareas\Tarea_4\.venv\Lib\site-packages\pandas\core\indexing.py", line 1342, in __getitem__

    return self._getitem_axis(maybe_callable, axis=axis)

           ~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "C:\Users\[usuario]\Documents\GitHub\Python_Interm\Tareas\Tarea_4\.venv\Lib\site-packages\pandas\core\indexing.py", line 1923, in _getitem_axis

    return self._getitem_iterable(key, axis=axis)

           ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^

  File "C:\Users\[usuario]\Documents\GitHub\Python_Interm\Tareas\Tarea_4\.venv\Lib\site-packages\pandas\core\indexing.py", line 1863, in _getitem_iterable

    keyarr, indexer = self._get_listlike_indexer(key, axis)

                      ~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^

  File "C:\Users\[usuario]\Documents\GitHub\Python_Interm\Tareas\Tarea_4\.venv\Lib\site-packages\pandas\core\indexing.py", line 2093, in _get_listlike_indexer

    keyarr, indexer = ax._get_indexer_strict(key, axis_name)

                      ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^

  File "C:\Users\[usuario]\Documents\GitHub\Python_Interm\Tareas\Tarea_4\.venv\Lib\site-packages\pandas\core\indexes\base.py", line 6557, in _get_indexer_strict

    self._raise_if_missing(keyarr, indexer, axis_name)

    ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "C:\Users\[usuario]\Documents\GitHub\Python_Interm\Tareas\Tarea_4\.venv\Lib\site-packages\pandas\core\indexes\base.py", line 6609, in _raise_if_missing

    raise KeyError(f"{not_found} not in index")

KeyError: "['Hu?nuco'] not in index"
```
</details>

> 🔧 **Bash** `{"command": "cd /tmp/w && python - <<'E'\nimport pandas as pd\ninv=pd.read_pickle('inv.pkl'); pov=pd.read_pickle('pov.pkl')\nbody=inv.drop('Total')\ntop=[i for i in body.index if i[:2] in('Ca','Lo','Pu','Pa','Hu') and not i.startswith('Hua') and not i.startswith('Pi') and i not in('Callao',) ]\ntop=[i for i in top if i!='Pasco' or True]\nprint(top)\ntop=['Cajamarca','Loreto','Puno','Pasco',[i for i in body.index if i.startswith('Hu') and i.endswith('nuco')][0]]\nt=body.loc[top].copy(); t['T']=t.sum(axis=1); print(t.round(1))\ntt=body.sum().sum(); print(t['T'].sum(), tt, t['T'].sum()/tt*100)\nprint((t.sum()/body.sum()*100).round(2))\nprint('pob',pov.loc[['06','16','21','19','10'],'pob'].sum()/pov.pob.sum()*100)\nE"}`

<details><summary>Resultado de la herramienta</summary>

```text
['Cajamarca', 'Hu�nuco', 'Loreto', 'Pasco', 'Puno']

               GL      GN      GR       T

Cajamarca  5127.6  2459.0  2374.3  9960.9

Loreto     2060.6  1831.3  3318.1  7210.0

Puno       3389.5  4306.5  2169.9  9865.9

Pasco       798.9   696.5  1235.9  2731.3

Hu�nuco    2072.1  2246.7  1463.0  5781.9

35549.906034 226365.33893 15.704659645350235

GL    15.79

GN    12.34

GR    22.16

T       NaN

dtype: float64

pob 16.022444
Shell cwd was reset to C:\Users\[usuario]\AppData\Local\Temp\tarea4_modoA_hwsvq2qn
```
</details>

#### 🤖 Claude · 2026-11-06 05:30 UTC

Los 5 departamentos con más pobreza concentraban cerca de una cuarta parte de la población pobre del país, pero recibieron menos de una sexta parte de la inversión bruta fija pública de 2020-2024.

## Datos y método
- **Pobreza:** usé la sumaria ENAHO 2024 (`sumaria-2024.dta`). Conté como pobre a quien tiene `pobreza` igual a 1 o 2, y expandí con `factor07 × mieperho`. El departamento sale de los 2 primeros dígitos del `ubigeo`. La tasa nacional me da 27,6 %, que coincide con la cifra oficial.
- **Inversión:** usé la API del BCRP con las series mensuales de inversión bruta fija por departamento, 2020-01 a 2024-12. Son tres series: gobierno nacional, gobiernos locales y gobiernos regionales. Los 60 meses están completos en todas. La suma de los departamentos coincide con el total de cada serie. El monto es nominal, en millones de S/.
- **Gobierno regional de Lima:** en las series regionales aparece la Municipalidad Metropolitana de Lima como un rubro aparte. Lo dejé en el total nacional, pero no afecta a los 5 departamentos analizados.

## Los 5 departamentos más pobres (ENAHO 2024)

| Departamento | Tasa de pobreza | Población pobre | Inversión 2020-24 (mill. S/) |
|---|---|---|---|
| Cajamarca | 45,0 % | 7,4 % del total nacional | 9 961 |
| Loreto | 43,0 % | 5,1 % | 7 210 |
| Puno | 39,9 % | 6,7 % | 9 866 |
| Pasco | 39,0 % | 1,3 % | 2 731 |
| Huánuco | 39,0 % | 3,8 % | 5 782 |
| **Total de los 5** | | **24,3 %** | **35 550 de 226 365 = 15,7 %** |

Los 5 departamentos concentran el 16,0 % de la población total, así que la brecha entre población pobre e inversión no se explica solo por el tamaño de cada departamento.

Por nivel de gobierno, estos 5 recibieron el 12,3 % de la inversión del gobierno nacional, el 15,8 % de la de los gobiernos locales y el 22,2 % de la de los gobiernos regionales.

## Qué se puede concluir
- La inversión pública está repartida de forma desigual frente a la pobreza. Los 5 departamentos tienen 24,3 % de los pobres y 15,7 % de la inversión, unos 8,6 puntos porcentuales menos.
- La brecha es mayor en el gobierno nacional (12,3 %). Solo los gobiernos regionales (22,2 %) se acercan a la proporción de pobres.
- Por persona, estos departamentos recibieron menos inversión que el promedio nacional. Su 15,7 % de la inversión se reparte entre el 16,0 % de la población.

## Qué no se puede concluir
- **Causalidad:** no se puede decir que la menor inversión cause la pobreza, ni que más inversión la reduciría. La pobreza de 2024 es un resultado de largo plazo. La inversión de 2020-2024 es solo un flujo reciente.
- **Eficiencia o calidad:** el monto no dice si los proyectos sean buenos ni si llegan a los pobres. Tampoco mide el gasto corriente (salud, educación, programas sociales), que puede ser más relevante para la pobreza.
- **Dentro del departamento:** la inversión se registra donde se ejecuta, no donde viven sus beneficiarios. Por ejemplo, una obra nacional en Lima puede servir a todo el país.
- **Ranking:** Pasco (38,97 %) y Huánuco (38,96 %) casi empatan, y la ENAHO es una encuesta con margen de error. No calculé intervalos de confianza, así que el orden entre los departamentos de cola no es firme. Con una muestra pequeña en Pasco, su cifra es la menos precisa.
- **Precios:** los montos son nominales y no están deflactados. Eso no cambia las proporciones de forma importante, pero sí los montos absolutos.
- **Comparación temporal:** comparo la pobreza de un solo año (2024) con la inversión acumulada de cinco años.

RESPUESTA FINAL: Los 5 departamentos más pobres en 2024 (Cajamarca, Loreto, Puno, Pasco y Huánuco) concentraban el 24,3 % de la población pobre del país y recibieron el 15,7 % de la inversión bruta fija pública 2020-2024 (S/ 35 550 millones de S/ 226 365 millones). Esto muestra una brecha de unos 8,6 puntos porcentuales, pero no prueba causalidad ni mide la calidad del gasto.

---

## Pregunta E1 · modo A

> **Pregunta:** Según la ENAHO 2024 del INEI, ¿qué porcentaje de la población del departamento de Cajamarca estaba en pobreza monetaria en 2024?

#### 🤖 Claude · 2026-11-06 05:28 UTC

Voy a revisar la carpeta y buscar el dato.

> 🔧 **Bash** `{"command": "ls -la; curl -sL -m 20 \"https://www.google.com/search?q=pobreza+monetaria+Cajamarca+2024+INEI\" -A \"Mozilla/5.0\" | head -c 500"}`

<details><summary>Resultado de la herramienta</summary>

```text
total 1046
drwxr-xr-x 1 [usuario] 197121      0 Nov  6 00:28 .
drwxr-xr-x 1 [usuario] 197121      0 Nov  6 00:28 ..
-rw-r--r-- 1 [usuario] 197121      5 Nov  5 06:23 .python-version
drwxr-xr-x 1 [usuario] 197121      0 Nov  5 06:23 datos
-rw-r--r-- 1 [usuario] 197121    503 Nov  5 06:23 pyproject.toml
-rw-r--r-- 1 [usuario] 197121 311285 Nov  5 06:23 uv.lock
<!DOCTYPE html><html lang="es-419"><head><title>Google Search</title><style>body{background-color:#fff}</style><script nonce="QYrk1Fr98eRtrbNlCXrDIg">window.google = window.google || {};window.google.c = window.google.c || {cap:0};</script></head><body><noscript><style>table,div,span,p{display:none}</style><meta content="0;url=/httpservice/retry/enablejs?sei=b2XtauvoGYzpmLQPpLGquAY" http-equiv="refresh"><div style="display:block">Haz clic <a href="/httpservice/retry/enablejs?sei=b2XtauvoGYzpmLQP
Shell cwd was reset to C:\Users\[usuario]\AppData\Local\Temp\tarea4_modoA_sxunivd2
```
</details>

> 🔧 **Bash** `{"command": "ls -laR datos | head -50; cat pyproject.toml"}`

<details><summary>Resultado de la herramienta</summary>

```text
datos:
total 28216
drwxr-xr-x 1 [usuario] 197121        0 Nov  5 06:23 .
drwxr-xr-x 1 [usuario] 197121        0 Nov  6 00:28 ..
-rw-r--r-- 1 [usuario] 197121  5793097 Nov  5 06:23 966-Modulo02.zip
-rw-r--r-- 1 [usuario] 197121 15935617 Nov  5 06:23 966-Modulo34.zip
-rw-r--r-- 1 [usuario] 197121  7005225 Nov  5 06:23 catalogo_bcrp.csv
-rw-r--r-- 1 [usuario] 197121   139681 Nov  5 06:23 peru_departamental_simple.geojson
[project]
name = "tarea-4-agente-inversion-pobreza"
version = "0.1.0"
description = "Agente de investigación: MCP del BCRP y Skills de la ENAHO 2024 para comparar el reparto de la inversión pública con el de la pobreza"
readme = "README.md"
requires-python = ">=3.14"
dependencies = [
    "fastmcp>=4,<5",
    "geopandas>=1.2.0",
    "httpx",
    "matplotlib>=3.11.2",
    "pandas>=3.1.0",
    "pyarrow>=26.0.0",
]

[dependency-groups]
dev = ["pytest"]

[tool.pytest.ini_options]
testpaths = ["mcp"]
Shell cwd was reset to C:\Users\[usuario]\AppData\Local\Temp\tarea4_modoA_sxunivd2
```
</details>

> 🔧 **Bash** `{"command": "mkdir -p /tmp/m34 && cd /tmp/m34 && unzip -oq \"C:/Users/[usuario]/AppData/Local/Temp/tarea4_modoA_sxunivd2/datos/966-Modulo34.zip\" && find . -type f | head -30"}`

<details><summary>Resultado de la herramienta</summary>

```text
./966-Modulo34/ConstVarGasto-Metodologia actualizada.zip
./966-Modulo34/DefinicionValoresMonetariosBasedeDatos.pdf
./966-Modulo34/Diccionario2024.pdf
./966-Modulo34/Estratificacion del Marco.pdf
./966-Modulo34/FichaTecnica.pdf
./966-Modulo34/sumaria-2024-12g.dta
./966-Modulo34/Sumaria-2024-12g.pdf
./966-Modulo34/sumaria-2024.dta
./966-Modulo34/Sumaria-2024.pdf
Shell cwd was reset to C:\Users\[usuario]\AppData\Local\Temp\tarea4_modoA_sxunivd2
```
</details>

> 🔧 **Bash** `{"command": "cd /tmp && cat > s.py <<'E'\nimport pandas as pd\nd=pd.read_stata('/tmp/m34/966-Modulo34/sumaria-2024.dta',convert_categoricals=False)\nprint(d.shape); print([c for c in d.columns if c in('pobreza','factor07','mieperho','ubigeo','dominio','estrato','conglome','vivienda','hogar')])\nd['dep']=d['ubigeo'].astype(str).str.zfill(6).str[:2]\nc=d[d.dep=='06'].copy()\nc['w']=c.factor07*c.mieperho\nprint(len(c))\nprint(c.groupby('pobreza').w.sum()/c.w.sum())\nprint(c.w.sum(), c.w[c.pobreza.isin([1,2])].sum()/c.w.sum()*100)\nE\npython -I s.py"}`

<details><summary>Resultado de la herramienta</summary>

```text
Exit code 1
Traceback (most recent call last):

  File "C:\Users\[usuario]\AppData\Local\Temp\s.py", line 2, in <module>

    d=pd.read_stata('/tmp/m34/966-Modulo34/sumaria-2024.dta',convert_categoricals=False)

  File "C:\Users\[usuario]\Documents\GitHub\Python_Interm\Tareas\Tarea_4\.venv\Lib\site-packages\pandas\io\stata.py", line 2305, in read_stata

    return reader.read()

           ~~~~~~~~~~~^^

  File "C:\Users\[usuario]\Documents\GitHub\Python_Interm\Tareas\Tarea_4\.venv\Lib\site-packages\pandas\io\stata.py", line 1705, in read

    self._ensure_open()

    ~~~~~~~~~~~~~~~~~^^

  File "C:\Users\[usuario]\Documents\GitHub\Python_Interm\Tareas\Tarea_4\.venv\Lib\site-packages\pandas\io\stata.py", line 1152, in _ensure_open

    self._open_file()

    ~~~~~~~~~~~~~~~^^

  File "C:\Users\[usuario]\Documents\GitHub\Python_Interm\Tareas\Tarea_4\.venv\Lib\site-packages\pandas\io\stata.py", line 1165, in _open_file

    handles = get_handle(

        self._original_path_or_buf,

    ...<3 lines>...

        compression=self._compression,

    )

  File "C:\Users\[usuario]\Documents\GitHub\Python_Interm\Tareas\Tarea_4\.venv\Lib\site-packages\pandas\io\common.py", line 954, in get_handle

    handle = open(handle, ioargs.mode)

FileNotFoundError: [Errno 2] No such file or directory: '/tmp/m34/966-Modulo34/sumaria-2024.dta'
```
</details>

#### 🤖 Claude · 2026-11-06 05:28 UTC

Python de Windows no entiende la ruta /tmp; uso ruta Windows.

> 🔧 **Bash** `{"command": "cd /tmp && W=$(cygpath -m /tmp/m34/966-Modulo34/sumaria-2024.dta) && sed -i \"s#/tmp/m34/966-Modulo34/sumaria-2024.dta#$W#\" s.py && python -I s.py"}`

<details><summary>Resultado de la herramienta</summary>

```text
(33691, 163)

['conglome', 'vivienda', 'hogar', 'ubigeo', 'dominio', 'estrato', 'mieperho', 'pobreza', 'factor07']

1469

pobreza

1    0.197154

2    0.252915

3    0.549931

Name: w, dtype: float32

1.5545858e+06 45.006893
Shell cwd was reset to C:\Users\[usuario]\AppData\Local\Temp\tarea4_modoA_sxunivd2
```
</details>

#### 🤖 Claude · 2026-11-06 05:28 UTC

En 2024, el **45,0 %** de la población de Cajamarca estaba en pobreza monetaria.

Lo calculé con la base Sumaria 2024 de la ENAHO, que está en `datos/966-Modulo34.zip`. Filtré los hogares con ubigeo que empieza en 06, que es Cajamarca: son 1 469 hogares en la muestra. Ponderé cada hogar por `factor07 × mieperho` (factor de expansión por número de miembros), para contar personas y no hogares. Sumé las categorías «pobre extremo» y «pobre no extremo» de la variable `pobreza`.

| Condición | % de la población |
|---|---|
| Pobre extremo | 19,7 % |
| Pobre no extremo | 25,3 % |
| **Pobreza monetaria total** | **45,0 %** |
| No pobre | 55,0 % |

No pude verificar la cifra contra la publicación oficial del INEI, porque no logré buscar en la web desde aquí. Es una estimación muestral, así que lleva un margen de error que no calculé. Cualquier diferencia con la cifra publicada, de décimas de punto, vendría del redondeo o de la forma de ponderar.

RESPUESTA FINAL: 45,0 % de la población de Cajamarca en pobreza monetaria en 2024 (19,7 % pobre extremo + 25,3 % pobre no extremo)

---

## Pregunta E2 · modo A

> **Pregunta:** Según la ENAHO 2024 del INEI, ¿cuál fue la tasa de pobreza monetaria en Lima Metropolitana (los 43 distritos de la provincia de Lima, sin el Callao) en 2024?

#### 🤖 Claude · 2026-11-06 05:28 UTC

Primero reviso si hay datos en la carpeta.

> 🔧 **Glob** `{"pattern": "**/*"}`

<details><summary>Resultado de la herramienta</summary>

```text
datos\catalogo_bcrp.csv
datos\966-Modulo02.zip
datos\966-Modulo34.zip
datos\peru_departamental_simple.geojson
.python-version
pyproject.toml
uv.lock
```
</details>

> 🔧 **Bash** `{"command": "cd C:/Users/[usuario]/AppData/Local/Temp/tarea4_modoA_fx3l7ulv && mkdir -p ../enaho_m34 && cd ../enaho_m34 && unzip -o -q ../tarea4_modoA_fx3l7ulv/datos/966-Modulo34.zip && find . -type f | head -30"}`

<details><summary>Resultado de la herramienta</summary>

```text
./966-Modulo34/ConstVarGasto-Metodologia actualizada.zip
./966-Modulo34/DefinicionValoresMonetariosBasedeDatos.pdf
./966-Modulo34/Diccionario2024.pdf
./966-Modulo34/Estratificacion del Marco.pdf
./966-Modulo34/FichaTecnica.pdf
./966-Modulo34/sumaria-2024-12g.dta
./966-Modulo34/Sumaria-2024-12g.pdf
./966-Modulo34/sumaria-2024.dta
./966-Modulo34/Sumaria-2024.pdf
Shell cwd was reset to C:\Users\[usuario]\AppData\Local\Temp\tarea4_modoA_fx3l7ulv
```
</details>

> 🔧 **Bash** `{"command": "cd C:/Users/[usuario]/AppData/Local/Temp/tarea4_modoA_fx3l7ulv && uv run --with pandas python -I -c \"\nimport pandas as pd\nd=pd.read_stata('../enaho_m34/966-Modulo34/sumaria-2024.dta',convert_categoricals=False)\nprint(d.shape);print([c for c in d.columns if c.lower() in('ubigeo','dominio','estrato','pobreza','factor07','mieperho','percepho','departamento','conglome','vivienda','hogar','linea','linpe')])\nprint(d.dominio.value_counts())\nprint(d.ubigeo.head())\n\""}`

<details><summary>Resultado de la herramienta</summary>

```text
(33691, 163)

['conglome', 'vivienda', 'hogar', 'ubigeo', 'dominio', 'estrato', 'mieperho', 'percepho', 'linpe', 'linea', 'pobreza', 'factor07']

dominio

7    7211

5    5531

1    4751

6    4523

8    4090

2    3287

3    2283

4    2015

Name: count, dtype: int64

0    010101

1    010101

2    010101

3    010101

4    010101

Name: ubigeo, dtype: str
Shell cwd was reset to C:\Users\[usuario]\AppData\Local\Temp\tarea4_modoA_fx3l7ulv
```
</details>

> 🔧 **Bash** `{"command": "cd C:/Users/[usuario]/AppData/Local/Temp/tarea4_modoA_fx3l7ulv && uv run --with pandas python -I -c \"\nimport pandas as pd\nd=pd.read_stata('../enaho_m34/966-Modulo34/sumaria-2024.dta',convert_categoricals=False)\nd['w']=d.factor07*d.mieperho\nd['p']=d.pobreza.isin([1,2])\nl=d[d.dominio==8]\nprint(l.ubigeo.str[:4].value_counts())\ndef r(x):print(len(x),(x.w*x.p).sum()/x.w.sum()*100)\nr(l)\nr(l[l.ubigeo.str[:4]=='1501'])\nr(l[l.ubigeo.str[:4]=='0701'])\nprint(d.groupby('dominio').apply(lambda x:(x.w*x.p).sum()/x.w.sum()*100))\n\""}`

<details><summary>Resultado de la herramienta</summary>

```text
ubigeo

1501    3063

0701    1027

Name: count, dtype: int64

4090 28.211704

3063 27.584463

1027 33.85989

dominio

1    24.282572

2    14.005232

3    20.148096

4    45.697422

5    30.096807

6    25.599789

7    30.024269

8    28.211704

dtype: float32
Shell cwd was reset to C:\Users\[usuario]\AppData\Local\Temp\tarea4_modoA_fx3l7ulv
```
</details>

#### 🤖 Claude · 2026-11-06 05:28 UTC

Según mi cálculo con la ENAHO 2024 (módulo 34, base Sumaria), la tasa de pobreza monetaria en los 43 distritos de la provincia de Lima, sin el Callao, fue de **27,6 %**.

**Método:**
- Usé el archivo `sumaria-2024.dta`, que está en la carpeta de datos.
- Dejé solo los hogares con ubigeo que empieza en 1501, es decir, la provincia de Lima: 3 063 hogares de la muestra.
- Conté como pobres a quienes tienen `pobreza` = 1 (pobre extremo) o 2 (pobre no extremo).
- Ponderé por `factor07 × mieperho`, para medir la pobreza como proporción de personas.

**Contraste con el dominio «Lima Metropolitana»:** el dominio 8 de la ENAHO incluye también la Provincia Constitucional del Callao (ubigeo 0701). Con ambas áreas la tasa sube a 28,2 %. Solo en el Callao sale 33,9 %, pero con 1 027 hogares de muestra.

**Limitación:** no calculé intervalos de confianza. La cifra es una estimación muestral y no la contrasté con una publicación oficial del INEI.

RESPUESTA FINAL: 27,6 % de pobreza monetaria en Lima Metropolitana (provincia de Lima, 43 distritos, sin Callao) en 2024; con Callao (dominio 8 de la ENAHO) sería 28,2 %.

---

## Pregunta E3 · modo A

> **Pregunta:** Según la ENAHO 2024 del INEI, ¿qué porcentaje de la población del área rural del Perú estaba en pobreza monetaria en 2024?

> 🔧 **Glob** `{"pattern": "*"}`

<details><summary>Resultado de la herramienta</summary>

```text
datos\catalogo_bcrp.csv
datos\966-Modulo02.zip
datos\966-Modulo34.zip
datos\peru_departamental_simple.geojson
.python-version
pyproject.toml
uv.lock
```
</details>

> 🔧 **Bash** `{"command": "cd datos; mkdir -p /tmp/m34; unzip -o -q 966-Modulo34.zip -d /tmp/m34; find /tmp/m34 | head -30; unzip -l 966-Modulo02.zip | head"}`

<details><summary>Resultado de la herramienta</summary>

```text
/tmp/m34
/tmp/m34/966-Modulo34
/tmp/m34/966-Modulo34/ConstVarGasto-Metodologia actualizada.zip
/tmp/m34/966-Modulo34/DefinicionValoresMonetariosBasedeDatos.pdf
/tmp/m34/966-Modulo34/Diccionario2024.pdf
/tmp/m34/966-Modulo34/Estratificacion del Marco.pdf
/tmp/m34/966-Modulo34/FichaTecnica.pdf
/tmp/m34/966-Modulo34/sumaria-2024-12g.dta
/tmp/m34/966-Modulo34/Sumaria-2024-12g.pdf
/tmp/m34/966-Modulo34/sumaria-2024.dta
/tmp/m34/966-Modulo34/Sumaria-2024.pdf
Archive:  966-Modulo02.zip
  Length      Date    Time    Name
---------  ---------- -----   ----
        0  2025-05-07 14:43   966-Modulo02/
   201079  2024-06-18 10:39   966-Modulo02/CED-01-200-2024.pdf
   395343  2021-05-07 11:05   966-Modulo02/Criterios para codificar Ocupaciones Peligrosas.pdf
  3940690  2025-05-16 14:36   966-Modulo02/Diccionario2024.pdf
 10217755  2025-05-07 14:39   966-Modulo02/enaho01-2024-200.dta
   349153  2020-05-11 21:36   966-Modulo02/enaho_tabla_ciuo_88.dta
    56727  2020-05-11 21:36   966-Modulo02/enaho_tabla_cno_2015.dta
Shell cwd was reset to C:\Users\[usuario]\AppData\Local\Temp\tarea4_modoA_xsp0m0gz
```
</details>

> 🔧 **Bash** `{"command": "cd /tmp/m34/966-Modulo34; python -I -c \"\nimport pandas as pd\nd=pd.read_stata('sumaria-2024.dta',convert_categoricals=False)\nprint(d.shape)\nd['pob']=d.mieperho*d.factor07\nd['rural']=d.estrato>5\nprint(d.estrato.value_counts().sort_index())\nprint(d.area.value_counts() if 'area' in d else '')\nprint(d.pobreza.value_counts())\nfor k,g in d.groupby('area' if 'area' in d else 'rural'):\n    print(k,(g.pob*g.pobreza.isin([1,2])).sum()/g.pob.sum(), (g.pob*(g.pobreza==1)).sum()/g.pob.sum())\n\" 2>&1 | tail -30"}`

<details><summary>Resultado de la herramienta</summary>

```text
(33691, 163)

estrato

1    5963

2    6349

3    2738

4    2584

5    4397

6    2039

7    6797

8    2824

Name: count, dtype: int64



pobreza

3    26879

2     5224

1     1588

Name: count, dtype: int64

False 0.24806988 0.031363122

True 0.39302793 0.15518467
Shell cwd was reset to C:\Users\[usuario]\AppData\Local\Temp\tarea4_modoA_xsp0m0gz
```
</details>

> 🔧 **Bash** `{"command": "cd /tmp/m34/966-Modulo34; python -I -c \"\nimport pandas as pd\nd=pd.read_stata('sumaria-2024.dta',convert_categoricals=False)\nd['pob']=d.mieperho*d.factor07\nprint((d.pob*d.pobreza.isin([1,2])).sum()/d.pob.sum())\nprint(d.columns[:40].tolist())\n\""}`

<details><summary>Resultado de la herramienta</summary>

```text
0.27579468

['a�o', 'mes', 'conglome', 'vivienda', 'hogar', 'ubigeo', 'dominio', 'estrato', 'mieperho', 'totmieho', 'percepho', 'ia01hd', 'ia02hd', 'ig03hd1', 'ig03hd2', 'ig03hd3', 'ig03hd4', 'ga03hd', 'ga04hd', 'sg23', 'sig24', 'sg25', 'sig26', 'sg27', 'sig28', 'sg42', 'sg421', 'sg422', 'sg423', 'sg42d', 'sg42d1', 'sg42d2', 'sg42d3', 'ingbruhd', 'ingnethd', 'pagesphd', 'ingindhd', 'ingauthd', 'insedthd', 'insedlhd']
Shell cwd was reset to C:\Users\[usuario]\AppData\Local\Temp\tarea4_modoA_xsp0m0gz
```
</details>

#### 🤖 Claude · 2026-11-06 05:28 UTC

En 2024, el 39,3 % de la población del área rural del Perú estaba en pobreza monetaria.

Lo calculé con la base Sumaria 2024 de la ENAHO (`sumaria-2024.dta`, módulo 34 del archivo `966-Modulo34.zip`). Estos son los pasos:

- **Población:** ponderé cada hogar por el número de miembros (`mieperho`) por el factor de expansión (`factor07`).
- **Pobreza monetaria:** conté como pobres a los hogares con `pobreza` igual a 1 (pobre extremo) o 2 (pobre no extremo).
- **Área rural:** la definí como los estratos 6 a 8. Esta división no la verifiqué con el diccionario, y el archivo no trae una variable de área ya construida.

Para comprobar el método calculé también el total nacional y me dio 27,6 %, que coincide con la cifra oficial del INEI que recuerdo.

Otras cifras que salieron del mismo cálculo:

| Medida | Rural | Urbano |
|---|---|---|
| Pobreza monetaria total | 39,3 % | 24,8 % |
| Pobreza extrema | 15,5 % | 3,1 % |

No tuve acceso al boletín oficial del INEI para contrastar la cifra rural, así que el 39,3 % es mi cálculo propio con los microdatos.

RESPUESTA FINAL: 39,3 % de la población rural estaba en pobreza monetaria en 2024 (cálculo propio con la Sumaria ENAHO 2024; pobreza extrema rural: 15,5 %).

---

## Pregunta E4 · modo A

> **Pregunta:** Según la ENAHO 2024 del INEI, ¿cuál es el intervalo de confianza al 95 % de la tasa de pobreza monetaria nacional de 2024?

> 🔧 **Glob** `{"pattern": "**/*"}`

<details><summary>Resultado de la herramienta</summary>

```text
datos\catalogo_bcrp.csv
datos\966-Modulo02.zip
datos\966-Modulo34.zip
datos\peru_departamental_simple.geojson
.python-version
pyproject.toml
uv.lock
```
</details>

> 🔧 **Bash** `{"command": "cd datos; mkdir -p /tmp/m34 /tmp/m02; unzip -o -q 966-Modulo34.zip -d /tmp/m34; unzip -o -q 966-Modulo02.zip -d /tmp/m02; find /tmp/m34 /tmp/m02 | head -50"}`

<details><summary>Resultado de la herramienta</summary>

```text
/tmp/m34
/tmp/m34/966-Modulo34
/tmp/m34/966-Modulo34/ConstVarGasto-Metodologia actualizada.zip
/tmp/m34/966-Modulo34/DefinicionValoresMonetariosBasedeDatos.pdf
/tmp/m34/966-Modulo34/Diccionario2024.pdf
/tmp/m34/966-Modulo34/Estratificacion del Marco.pdf
/tmp/m34/966-Modulo34/FichaTecnica.pdf
/tmp/m34/966-Modulo34/sumaria-2024-12g.dta
/tmp/m34/966-Modulo34/Sumaria-2024-12g.pdf
/tmp/m34/966-Modulo34/sumaria-2024.dta
/tmp/m34/966-Modulo34/Sumaria-2024.pdf
/tmp/m02
/tmp/m02/966-Modulo02
/tmp/m02/966-Modulo02/CED-01-200-2024.pdf
/tmp/m02/966-Modulo02/Criterios para codificar Ocupaciones Peligrosas.pdf
/tmp/m02/966-Modulo02/Diccionario2024.pdf
/tmp/m02/966-Modulo02/enaho01-2024-200.dta
/tmp/m02/966-Modulo02/enaho_tabla_ciuo_88.dta
/tmp/m02/966-Modulo02/enaho_tabla_cno_2015.dta
/tmp/m02/966-Modulo02/FichaTecnica.pdf
Shell cwd was reset to C:\Users\[usuario]\AppData\Local\Temp\tarea4_modoA_39vrng16
```
</details>

> 🔧 **Bash** `{"command": "cd /tmp/m34/966-Modulo34; cat > /tmp/a.py <<'E'\nimport pandas as pd\nd=pd.read_stata('sumaria-2024.dta',convert_categoricals=False)\nprint(d.shape);print([c for c in d.columns if c.lower() in('pobreza','factor07','mieperho','conglome','estrato','vivienda','hogar','ubigeo','dominio','estrsocial')])\nprint(d.pobreza.value_counts())\nE\nuv run --project \"C:/Users/[usuario]/AppData/Local/Temp/tarea4_modoA_39vrng16\" python -I /tmp/a.py 2>&1 | tail -20"}`

<details><summary>Resultado de la herramienta</summary>

```text
(33691, 163)

['conglome', 'vivienda', 'hogar', 'ubigeo', 'dominio', 'estrato', 'mieperho', 'estrsocial', 'pobreza', 'factor07']

pobreza

3    26879

2     5224

1     1588

Name: count, dtype: int64
Shell cwd was reset to C:\Users\[usuario]\AppData\Local\Temp\tarea4_modoA_39vrng16
```
</details>

> 🔧 **Bash** `{"command": "cat > /tmp/b.py <<'E'\nimport pandas as pd,numpy as np\nd=pd.read_stata('/tmp/m34/966-Modulo34/sumaria-2024.dta',convert_categoricals=False)\nd['w']=d.factor07*d.mieperho; d['y']=(d.pobreza<=2)*1.0\np=(d.w*d.y).sum()/d.w.sum(); print('p',p)\nd['z']=d.w*(d.y-p)/d.w.sum()\nc=d.groupby(['estrato','conglome']).z.sum().reset_index()\nv=0;lon=0\nfor e,g in c.groupby('estrato'):\n    n=len(g)\n    if n<2: lon+=1;continue\n    v+=n/(n-1)*((g.z-g.z.mean())**2).sum()\nse=v**.5;print(se,lon,c.estrato.nunique(),len(c))\nfrom scipy.stats import t\ndf=len(c)-c.estrato.nunique()\nfor q in(1.96,t.ppf(.975,df)):print(100*(p-q*se),100*(p+q*se))\nE\nuv run --project \"C:/Users/[usuario]/AppData/Local/Temp/tarea4_modoA_39vrng16\" python -I /tmp/b.py 2>&1 | tail"}`

<details><summary>Resultado de la herramienta</summary>

```text
    ~~~~~~~~~~~~~~~^^

  File "C:\Users\[usuario]\Documents\GitHub\Python_Interm\Tareas\Tarea_4\.venv\Lib\site-packages\pandas\io\stata.py", line 1165, in _open_file

    handles = get_handle(

        self._original_path_or_buf,

    ...<3 lines>...

        compression=self._compression,

    )

  File "C:\Users\[usuario]\Documents\GitHub\Python_Interm\Tareas\Tarea_4\.venv\Lib\site-packages\pandas\io\common.py", line 954, in get_handle

    handle = open(handle, ioargs.mode)

FileNotFoundError: [Errno 2] No such file or directory: '/tmp/m34/966-Modulo34/sumaria-2024.dta'
Shell cwd was reset to C:\Users\[usuario]\AppData\Local\Temp\tarea4_modoA_39vrng16
```
</details>

#### 🤖 Claude · 2026-11-06 05:28 UTC

Windows Python no resuelve /tmp; uso ruta de Windows.

> 🔧 **Bash** `{"command": "P=$(cygpath -m /tmp); sed -i \"s#/tmp/m34#$P/m34#\" /tmp/b.py; uv run --project \"C:/Users/[usuario]/AppData/Local/Temp/tarea4_modoA_39vrng16\" python -I $P/b.py 2>&1 | tail"}`

<details><summary>Resultado de la herramienta</summary>

```text
p 0.2757946762365833

0.005192949233813532 0 8 5359

Traceback (most recent call last):

  File "C:\Users\[usuario]\AppData\Local\Temp\b.py", line 13, in <module>

    from scipy.stats import t

ModuleNotFoundError: No module named 'scipy'
Shell cwd was reset to C:\Users\[usuario]\AppData\Local\Temp\tarea4_modoA_39vrng16
```
</details>

#### 🤖 Claude · 2026-11-06 05:28 UTC

La tasa de pobreza monetaria nacional de 2024 es 27,6 %, con un intervalo de confianza al 95 % de **26,6 % a 28,6 %**. Lo calculé yo mismo con el módulo Sumaria de la ENAHO 2024 (`sumaria-2024.dta`, 33 691 hogares), porque en la carpeta no había un cuadro del INEI con el intervalo ya publicado.

**Método**
- Una persona se cuenta como pobre si la variable `pobreza` vale 1 (pobre extremo) o 2 (pobre no extremo).
- Cada hogar pesa `factor07 × mieperho`, para que la tasa sea de personas y no de hogares.
- El error estándar usa linealización de Taylor, con `estrato` como estrato y `conglome` como unidad primaria de muestreo. Hay 8 estratos y 5 359 conglomerados, y ningún estrato tiene un solo conglomerado.

**Resultado**
- La tasa estimada es 27,58 %, que coincide con la cifra oficial de 27,6 %.
- El error estándar es 0,519 puntos porcentuales.
- El intervalo es 27,58 % ± 1,96 × 0,519, es decir, de 26,56 % a 28,60 %. Con unos 5 350 grados de libertad, usar la distribución t en lugar de 1,96 no cambia el resultado.

El diseño que usé es una aproximación. Si el INEI usa otra especificación, el error estándar podría diferir en algunas centésimas, pero no debería cambiar los valores redondeados a un decimal. No pude contrastar el intervalo con la publicación oficial.

RESPUESTA FINAL: IC 95 % de la pobreza monetaria nacional 2024 ≈ [26,6 %; 28,6 %] (estimación puntual 27,6 %; error estándar ≈ 0,52 p.p.)

---

## Pregunta R1 · modo A

> **Pregunta:** Según el BCRP, ¿cuánto fueron las exportaciones de productos tradicionales mineros del departamento de Arequipa en 2024, en millones de dólares?

#### 🤖 Claude · 2026-11-06 05:32 UTC

Empiezo revisando qué hay en la carpeta.

> 🔧 **Glob** `{"pattern": "**/*"}`

<details><summary>Resultado de la herramienta</summary>

```text
datos\catalogo_bcrp.csv
datos\966-Modulo02.zip
datos\966-Modulo34.zip
datos\peru_departamental_simple.geojson
.python-version
pyproject.toml
uv.lock
```
</details>

> 🔧 **Bash** `{"command": "cd datos; head -c 1500 catalogo_bcrp.csv; echo; wc -l catalogo_bcrp.csv; grep -i -E \"arequipa\" catalogo_bcrp.csv | grep -i -E \"export|mineri|tradicional\" | head -30; unzip -l 966-Modulo02.zip | head -30; unzip -l 966-Modulo34.zip | head -30"}`

<details><summary>Resultado de la herramienta</summary>

```text
Código de serie;Categoría de serie;Grupo de serie;Nombre de serie;Descripción de la serie;Metodología de la serie;Unidad de medida;Escala;Geografía (País, Región de Perú);Fuente;Frecuencia;Fecha de creación;Grupo de publicación;Área que publica;Fecha de actualización;Fecha de inicio;Fecha de fin;Memo;

PN00001MM;Sociedades creadoras de depósito;Cuentas monetarias de las sociedades creadoras de depósito;Activos Externos Netos de Corto Plazo (millones S/);https://estadisticas.bcrp.gob.pe/estadisticas/series/documentos/bcrpdataapi.pdf;https://estadisticas.bcrp.gob.pe/estadisticas/series/documentos/bcrpdataapi.pdf;;;;BCRP;Mensual;2022-03-24;Sistema financiero y empresas bancarias y expectativas sobre condiciones crediticias;Departamento de Estadísticas Monetarias;2026-10-23;Ene-1992;Dic-2025;;

PN00002MM;Sociedades creadoras de depósito;Cuentas monetarias de las sociedades creadoras de depósito;Activos Externos Netos de Corto Plazo (millones US$);;;;;;BCRP;Mensual;2022-03-24;Sistema financiero y empresas bancarias y expectativas sobre condiciones crediticias;Departamento de Estadísticas Monetarias;2026-10-23;Ene-1992;Dic-2025;;

PN00003MM;Sociedades creadoras de depósito;Cuentas monetarias de las sociedades creadoras de depósito;Activos Externos Netos de Corto Plazo - Activos (millones US$);;;;;;BCRP;Mensual;2022-03-24;Sistema financiero y empresas bancarias y expectativas sobre condiciones crediticias;Departamento de Estadísticas Monetarias;2026-10-23;Ene-19
17168 catalogo_bcrp.csv
RD38088BM;Exportaciones e importaciones;Exportaciones por Departamento (Valores FOB en millones US$);Arequipa;Información estadística regional / Exportaciones e importaciones / Exportaciones por Departamento (Valores FOB en millones US$) / Arequipa;;;;RE;BCRP, Sunat, empresas;Mensual;2020-09-26;;Departamento de Estadísticas de Balanza de Pagos;2024-11-18;Ene-2005;Dic-2022;;
RD38121BM;Exportaciones e importaciones;Importaciones por Aduana (Valores FOB en millones US$);Arequipa;Información estadística regional / Exportaciones e importaciones / Importaciones por Aduana (Valores FOB en millones US$) / Arequipa;;;;RE;BCRP, Sunat, empresas;Mensual;2020-09-26;;Departamento de Estadísticas de Balanza de Pagos;2024-11-18;Ene-2005;Dic-2023;;
RD38134BM;Exportaciones e importaciones;Importaciones por Aduana (Valores FOB en millones US$);Dependencia Postal Arequipa;Información estadística regional / Exportaciones e importaciones / Importaciones por Aduana (Valores FOB en millones US$) / Depende
… [13992 caracteres más omitidos]
```
</details>

#### 🤖 Claude · 2026-11-06 05:32 UTC

El catálogo solo tiene metadatos, y estas series figuran hasta 2022. Reviso si hay una versión anual más reciente y pruebo la API del BCRP.

> 🔧 **Bash** `{"command": "cd datos; grep -i \"Arequipa\" catalogo_bcrp.csv | grep -i \"Mineros\" | cut -d';' -f1,3,4,11,16,17; echo ---; curl -s -m 30 \"https://estadisticas.bcrp.gob.pe/estadisticas/series/api/RD38191BM/json/2024-1/2024-12\" | head -c 1500; echo; curl -s -m 30 \"https://estadisticas.bcrp.gob.pe/estadisticas/series/api/RD38191BM/json/2022-1/2024-12\" | head -c 600"}`

<details><summary>Resultado de la herramienta</summary>

```text
RD12954DM;Producción de productos mineros según departamentos;Cobre - Arequipa (tm.f);Mensual;Ene-2001;Dic-2025
RD12974DM;Producción de productos mineros según departamentos;Molibdeno - Arequipa (tm.f);Mensual;Ene-2001;Dic-2025
RD12981DM;Producción de productos mineros según departamentos;Oro - Arequipa (grs.f);Mensual;Ene-2001;Dic-2025
RD12999DM;Producción de productos mineros según departamentos;Plata - Arequipa (kg.f);Mensual;Ene-2001;Dic-2025
RD13015DM;Producción de productos mineros según departamentos;Plomo - Arequipa (tm.f);Mensual;Ene-2001;Dic-2025
RD13031DM;Producción de productos mineros según departamentos;Zinc - Arequipa (tm.f);Mensual;Ene-2001;Dic-2025
RD14265DQ;Producción de productos mineros según departamentos;Cobre - Arequipa (tm.f);Trimestral;T1-2001;T4-2025
RD14285DQ;Producción de productos mineros según departamentos;Molibdeno - Arequipa (tm.f);Trimestral;T1-2001;T4-2025
RD14292DQ;Producción de productos mineros según departamentos;Oro - Arequipa (grs.f);Trimestral;T1-2001;T4-2025
RD14310DQ;Producción de productos mineros según departamentos;Plata - Arequipa (kg.f);Trimestral;T1-2001;T4-2025
RD14326DQ;Producción de productos mineros según departamentos;Plomo - Arequipa (tm.f);Trimestral;T1-2001;T4-2025
RD14342DQ;Producción de productos mineros según departamentos;Zinc - Arequipa (tm.f);Trimestral;T1-2001;T4-2025
RD15519DA;Producción de productos mineros según departamentos;Cobre - Arequipa (tm.f);Anual;2001;2025
RD15539DA;Producción de productos mineros según departamentos;Molibdeno - Arequipa (tm.f);Anual;2001;2025
RD15546DA;Producción de productos mineros según departamentos;Oro - Arequipa (grs.f);Anual;2001;2025
RD15564DA;Producción de productos mineros según departamentos;Plata - Arequipa (kg.f);Anual;2001;2025
RD15580DA;Producción de productos mineros según departamentos;Plomo - Arequipa (tm.f);Anual;2001;2025
RD15596DA;Producción de productos mineros según departamentos;Zinc - Arequipa (tm.f);Anual;2001;2025
RD38191BM;Exportaciones por grupo de productos de Arequipa (Valores FOB en millones US$);Productos tradicionales - Mineros;Mensual;Ene-2005;Dic-2022
RD40518BQ;Exportaciones por grupo de productos de Arequipa (Valores FOB en millones US$);Productos tradicionales - Mineros;Trimestral;T1-2005;T4-2022
RD41012BA;Exportaciones por grupo de productos de Arequipa (Valores FOB en millones US$);Productos tradicionales - Mineros;Anual;2005;2022
---
{
"config":
{
"title":"Exportaciones por grupo de productos de Arequipa (Valores FOB en mi
… [424 caracteres más omitidos]
```
</details>

> 🔧 **Bash** `{"command": "for s in RD41012BA RD38191BM; do echo $s; curl -s -m 30 \"https://estadisticas.bcrp.gob.pe/estadisticas/series/api/$s/json/2020/2025\" | tr -d '\\n' | head -c 900; echo; done; curl -s -m 30 \"https://estadisticas.bcrp.gob.pe/estadisticas/series/api/RD38191BM/json/2022-10/2022-12\" | tr -d '\\n'| head -c 600"}`

<details><summary>Resultado de la herramienta</summary>

```text
RD41012BA
{"config":{"title":"Exportaciones por grupo de productos de Arequipa (Valores FOB en millones US$)","series":[{"name":"Exportaciones por grupo de productos de Arequipa (Valores FOB en millones US$) - Productos tradicionales - Mineros","dec":"0"}]},"periods":[{"name":"2020","values":["3416.209362751"]},{"name":"2021","values":["4981.93564312"]},{"name":"2022","values":["5377.89242593"]}]}
RD38191BM
{"config":{"title":"Exportaciones por grupo de productos de Arequipa (Valores FOB en millones US$)","series":[{"name":"Exportaciones por grupo de productos de Arequipa (Valores FOB en millones US$) - Productos tradicionales - Mineros","dec":"0"}]},"periods":[{"name":"Ene.2020","values":["289.05465321"]},{"name":"Feb.2020","values":["269.24494402"]},{"name":"Mar.2020","values":["218.04868594"]},{"name":"Abr.2020","values":["121.762238"]},{"name":"May.2020","values":["217.72620521"]},{"name":"Jun.2020","values":["266.16220972"]},{"name":"Jul.2020","values":["272.21096318"]},{"name":"Ago.2020","values":["263.14474351"]},{"name":"Sep.2020","values":["375.833037934"]},{"name":"Oct.2020","values":["383.389478107"]},{"name":"Nov.2020","values":["306.63760471"]},{"name":"Dic.2020","values":["432.99459921"]},{"name":"Ene.2021","values":["337.36990949"]},{"name":"Feb.2021","values":["292.47288034"
{"config":{"title":"Exportaciones por grupo de productos de Arequipa (Valores FOB en millones US$)","series":[{"name":"Exportaciones por grupo de productos de Arequipa (Valores FOB en millones US$) - Productos tradicionales - Mineros","dec":"0"}]},"periods":[{"name":"Oct.2022","values":["467.11979287"]},{"name":"Nov.2022","values":["374.20637064"]},{"name":"Dic.2022","values":["511.13832521"]}]}
Shell cwd was reset to C:\Users\[usuario]\AppData\Local\Temp\tarea4_modoA_0ff8lz0e
```
</details>

> 🔧 **Bash** `{"command": "cd datos; grep -i \"export\" catalogo_bcrp.csv | grep -i -E \"departamento|región|region\" | grep -E \";(Dic-)?2024;|T4-2024|Dic-2024|Dic-2025|;2025;\" | cut -d';' -f1,3,4,11,17 | head -20; grep -i \"export\" catalogo_bcrp.csv | grep -i \"minero\" | grep -i -E \"2024|2025\" | cut -d';' -f1,3,4,11,17 | head"}`

<details><summary>Resultado de la herramienta</summary>

```text
PM04921AA;Producto bruto interno por tipo de gasto (variaciones porcentuales reales);Exportaciones;Anual;2025
PM04933AA;Producto bruto interno por tipo de gasto (millones S/ 2007);Exportaciones;Anual;2025
PM04944AA;Producto bruto interno por tipo de gasto (millones S/);Exportaciones;Anual;2025
PM04954AA;Producto bruto interno por tipo de gasto (variaciones porcentuales nominales);Exportaciones;Anual;2025
PM04965AA;Producto bruto interno por tipo de gasto (estructura porcentual nominal);Exportaciones;Anual;2025
PM05032AA;Producción agropecuaria por principales productos (variación porcentual interanual);Agricola - Agroexportación e Industrial;Anual;2025
PM05033AA;Producción agropecuaria por principales productos (variación porcentual interanual);Agricola - Agroexportación e Industrial - Café;Anual;2025
PM05034AA;Producción agropecuaria por principales productos (variación porcentual interanual);Agricola - Agroexportación e Industrial - Caña de azúcar;Anual;2025
PM05035AA;Producción agropecuaria por principales productos (variación porcentual interanual);Agricola - Agroexportación e Industrial - Maíz Amarillo Duro;Anual;2025
PM05036AA;Producción agropecuaria por principales productos (variación porcentual interanual);Agricola - Agroexportación e Industrial - Algodón Rama;Anual;2025
PM05037AA;Producción agropecuaria por principales productos (variación porcentual interanual);Agricola - Agroexportación e Industrial - Espárrago;Anual;2025
PM05038AA;Producción agropecuaria por principales productos (variación porcentual interanual);Agricola - Agroexportación e Industrial - Uva;Anual;2025
PM05039AA;Producción agropecuaria por principales productos (variación porcentual interanual);Agricola - Agroexportación e Industrial - Aceituna;Anual;2025
PM05040AA;Producción agropecuaria por principales productos (variación porcentual interanual);Agricola - Agroexportación e Industrial - Mango;Anual;2025
PM05041AA;Producción agropecuaria por principales productos (variación porcentual interanual);Agricola - Agroexportación e Industrial - Cacao;Anual;2025
PM05042AA;Producción agropecuaria por principales productos (variación porcentual interanual);Agricola - Agroexportación e Industrial - Palta;Anual;2025
PM05043AA;Producción agropecuaria por principales productos (variación porcentual interanual);Agricola - Agroexportación e Industrial - Palma Aceitera;Anual;2025
PM05045AA;Producción agropecuaria por principales productos (variación porcentual interanual);Agricola - Agroexpor
… [1809 caracteres más omitidos]
```
</details>

#### 🤖 Claude · 2026-11-06 05:32 UTC

No pude obtener la cifra de 2024 con certeza, así que no te doy ningún monto para ese año.

- **Serie del BCRP:** la que corresponde es «Exportaciones por grupo de productos de Arequipa (Valores FOB en millones US$) – Productos tradicionales – Mineros». Sus códigos son RD41012BA (anual), RD40518BQ (trimestral) y RD38191BM (mensual).
- **Cobertura:** según el catálogo de `datos/`, las tres series llegan solo hasta 2022.
- **Consulta a la API del BCRP:** pedí 2024 y 2025 a la API oficial y no devolvió ningún dato para esos años. La serie anual termina en 2022.
- **Otras series:** busqué en el catálogo alguna otra serie de exportaciones regionales mineras que llegara a 2024 y no encontré ninguna.
- **Descartados:** los archivos ENAHO (zips) son de encuestas de hogares y no sirven para esto. La serie de producción minera de Arequipa llega a 2025, pero está en toneladas y gramos, no en dólares de exportación.

Los últimos valores publicados por el BCRP, en millones de US$ FOB, son estos:

| Año | Exportaciones tradicionales mineras de Arequipa |
|---|---|
| 2020 | 3 416,2 |
| 2021 | 4 981,9 |
| 2022 | 5 377,9 |

Estimar 2024 a partir de la producción o de los precios sería inventar una cifra, y no lo hice.

RESPUESTA FINAL: No disponible con certeza. El BCRP no publica el dato de 2024 en las series consultadas, que llegan hasta 2022 (US$ 5 377,9 millones).

---

## Pregunta R2 · modo A

> **Pregunta:** Según el BCRP, ¿cuánto canon minero recibió el departamento de Cusco en 2024?

#### 🤖 Claude · 2026-11-06 05:32 UTC

Voy a revisar primero si hay datos en la carpeta.

> 🔧 **Glob** `{"pattern": "**/*"}`

<details><summary>Resultado de la herramienta</summary>

```text
datos\catalogo_bcrp.csv
datos\966-Modulo02.zip
datos\966-Modulo34.zip
datos\peru_departamental_simple.geojson
.python-version
pyproject.toml
uv.lock
```
</details>

> 🔧 **Bash** `{"command": "cd datos; head -c 1500 catalogo_bcrp.csv; echo; grep -i -c canon catalogo_bcrp.csv; grep -i canon catalogo_bcrp.csv | head -30; unzip -l 966-Modulo02.zip | head -30; unzip -l 966-Modulo34.zip | head -30"}`

<details><summary>Resultado de la herramienta</summary>

```text
Código de serie;Categoría de serie;Grupo de serie;Nombre de serie;Descripción de la serie;Metodología de la serie;Unidad de medida;Escala;Geografía (País, Región de Perú);Fuente;Frecuencia;Fecha de creación;Grupo de publicación;Área que publica;Fecha de actualización;Fecha de inicio;Fecha de fin;Memo;

PN00001MM;Sociedades creadoras de depósito;Cuentas monetarias de las sociedades creadoras de depósito;Activos Externos Netos de Corto Plazo (millones S/);https://estadisticas.bcrp.gob.pe/estadisticas/series/documentos/bcrpdataapi.pdf;https://estadisticas.bcrp.gob.pe/estadisticas/series/documentos/bcrpdataapi.pdf;;;;BCRP;Mensual;2022-03-24;Sistema financiero y empresas bancarias y expectativas sobre condiciones crediticias;Departamento de Estadísticas Monetarias;2026-10-23;Ene-1992;Dic-2025;;

PN00002MM;Sociedades creadoras de depósito;Cuentas monetarias de las sociedades creadoras de depósito;Activos Externos Netos de Corto Plazo (millones US$);;;;;;BCRP;Mensual;2022-03-24;Sistema financiero y empresas bancarias y expectativas sobre condiciones crediticias;Departamento de Estadísticas Monetarias;2026-10-23;Ene-1992;Dic-2025;;

PN00003MM;Sociedades creadoras de depósito;Cuentas monetarias de las sociedades creadoras de depósito;Activos Externos Netos de Corto Plazo - Activos (millones US$);;;;;;BCRP;Mensual;2022-03-24;Sistema financiero y empresas bancarias y expectativas sobre condiciones crediticias;Departamento de Estadísticas Monetarias;2026-10-23;Ene-19
12
PN02229FM;Gastos;Gastos del gobierno central (millones S/);Resultado Primario - Gastos No Financieros - Gastos Corrientes - Tranferencias - Canon;;;;;;Ministerio de Economía y Finanzas, Banco de la Nación;Mensual;2022-03-11;Operaciones del Gobierno Central, Sistema de Pagos;Departamento de Estadísticas Fiscales_1;2026-10-15;Ene-1995;Dic-2025;;
PN02274FM;Gastos;Gastos del gobierno central (millones S/ 2007) (descontinuada);Resultado Primario - Gastos No Financieros - Gastos Corrientes - Transferencias - Canon;;;;;;Ministerio de Economía y Finanzas, Banco de la Nación;Mensual;2022-01-14;Operaciones del Gobierno Central, Sistema de Pagos;Departamento de Estadísticas Fiscales_1;2022-01-14;Ene-1995;Dic-2021;;
PN03317FQ;Gastos;Gastos del gobierno central (millones S/);Gastos No Financieros - Gastos Corrientes - Transferencias - Canon;;;;;;Ministerio de Economía y Finanzas, Banco de la Nación;Trimestral;2022-02-18;Demanda y oferta global, balanza de pagos, sector público y monetario;Departamento de Estadístic
… [4789 caracteres más omitidos]
```
</details>

> 🔧 **Bash** `{"command": "cd datos; grep -i -E \"cusco|cuzco\" catalogo_bcrp.csv | cut -c1-300 | head -40; grep -i -E \"minero|regal\" catalogo_bcrp.csv | cut -c1-250 | head"}`

<details><summary>Resultado de la herramienta</summary>

```text
PN08563EM;Sistemas de pagos;CCE: Cheques recibidos, cheques rechazados por institución financiera (Monto en Millones de Soles y Número en Miles de Operaciones) - Moneda Nacional;MN - Cheques Recibidos - CMAC Cuzco (número);;;;;;;Mensual;2022-04-08;BCRP, Reservas internacionales netas y sistema de
PN08589EM;Sistemas de pagos;CCE: cheques recibidos y rechazados y transferencias de crédito en MN (estructura porcentual);MN - Cheques Recibidos - Número - CMAC Cuzco;;;;;;BCRP;Mensual;2022-04-08;BCRP, Reservas internacionales netas y sistema de pagos (LBTR y CCE) ;Departamento Análisis del Siste
PN08615EM;Sistemas de pagos;CCE: Cheques recibidos, cheques rechazados por institución financiera (Monto en Millones de Soles y Número en Miles de Operaciones) - Moneda Nacional;MN - Cheques Recibidos - Monto - CMAC Cuzco (miles S/);;;;;;;Mensual;2022-04-08;BCRP, Reservas internacionales netas y s
PN08641EM;Sistemas de pagos;CCE: cheques recibidos y rechazados y transferencias de crédito en MN (estructura porcentual);MN - Cheques Recibidos - Monto - CMAC Cuzco;;;;;;BCRP;Mensual;2022-04-08;BCRP, Reservas internacionales netas y sistema de pagos (LBTR y CCE) ;Departamento Análisis del Sistema
PN08667EM;Sistemas de pagos;CCE: Cheques recibidos, cheques rechazados por institución financiera (Monto en Millones de Soles y Número en Miles de Operaciones) - Moneda Nacional;MN - Cheques Rechazados - CMAC Cuzco (número);;;;;;;Mensual;2022-04-08;BCRP, Reservas internacionales netas y sistema d
PN08693EM;Sistemas de pagos;CCE: cheques recibidos y rechazados y transferencias de crédito en MN (estructura porcentual);MN - Cheques Rechazados - Número - CMAC Cuzco;;;;;;BCRP;Mensual;2022-04-08;BCRP, Reservas internacionales netas y sistema de pagos (LBTR y CCE) ;Departamento Análisis del Sist
PN08719EM;Sistemas de pagos;CCE: Cheques recibidos, cheques rechazados por institución financiera (Monto en Millones de Soles y Número en Miles de Operaciones) - Moneda Nacional;MN - Cheques Rechazados - Monto - CMAC Cuzco (miles S/);;;;;;;Mensual;2022-04-08;BCRP, Reservas internacionales netas y 
PN08745EM;Sistemas de pagos;CCE: cheques recibidos y rechazados y transferencias de crédito en MN (estructura porcentual);MN - Cheques Rechazados - Monto - CMAC Cuzco;;;;;;BCRP;Mensual;2022-04-08;BCRP, Reservas internacionales netas y sistema de pagos (LBTR y CCE) ;Departamento Análisis del Sistem
PN08771EM;Sistemas de pagos;CCE: Transferencias de crédito e inmediatas por institución financiera (Monto en Mil
… [11897 caracteres más omitidos]
```
</details>

> 🔧 **Bash** `{"command": "cd datos; grep -i -E \"canon\" catalogo_bcrp.csv | cut -d';' -f1,3,4 | grep -v -E \"^(PN|PM)\"; grep -i -E \"transferencias.*(departament|region)|Cusco.*(canon|transfer)\" catalogo_bcrp.csv | cut -d';' -f1,3,4 | head"}`

<details><summary>Resultado de la herramienta</summary>

```text
PN02270FM;Gastos del gobierno central (millones S/ 2007) (descontinuada);Resultado Primario - Gastos No Financieros - Gastos Corrientes - Transferencias
PN02271FM;Gastos del gobierno central (millones S/ 2007) (descontinuada);Resultado Primario - Gastos No Financieros - Gastos Corrientes - Transferencias - Pensiones
PN02272FM;Gastos del gobierno central (millones S/ 2007) (descontinuada);Resultado Primario - Gastos No Financieros - Gastos Corrientes - Transferencias - ONP - FONAHPU
PN02273FM;Gastos del gobierno central (millones S/ 2007) (descontinuada);Resultado Primario - Gastos No Financieros - Gastos Corrientes - Transferencias - FONCOMUN
PN02274FM;Gastos del gobierno central (millones S/ 2007) (descontinuada);Resultado Primario - Gastos No Financieros - Gastos Corrientes - Transferencias - Canon
PN02275FM;Gastos del gobierno central (millones S/ 2007) (descontinuada);Resultado Primario - Gastos No Financieros - Gastos Corrientes - Transferencias - Otros
PN02566AQ;Ingreso nacional disponible (variaciones porcentuales anualizadas);PBI - Ingreso Nacional Bruto - Transferencias Corrientes
PN02576AQ;Ingreso nacional disponible (millones S/ 2007);PBI - Ingreso Nacional Bruto - Transferencias Corrientes
PN03294FQ;Gastos no financieros del gobierno general (millones S/);Gastos Corrientes - Transferencias
PN03295FQ;Gastos no financieros del gobierno general (millones S/);Gastos Corrientes - Transferencias - Gobierno Nacional
Shell cwd was reset to C:\Users\[usuario]\AppData\Local\Temp\tarea4_modoA_d8m3uwfa
```
</details>

#### 🤖 Claude · 2026-11-06 05:32 UTC

No pude obtener esa cifra con certeza.

- **Lo que revisé:** el catálogo de series del BCRP en `datos/catalogo_bcrp.csv`. Busqué «canon», «regalías», «Cusco» y «transferencias» por departamento.
- **Lo que hay sobre canon:** solo series nacionales. Por ejemplo, «Canon y regalías (Mill. S/)» (PN37897FM), «Canon petrolero» (PM05873FA) y las transferencias de canon del gobierno central. Ninguna está desagregada por departamento.
- **Lo que hay sobre Cusco:** las series que mencionan Cusco son de cheques de la CMAC Cuzco, precios históricos y producción minera (por ejemplo, cobre en Cusco, RD12957DM). Ninguna es de canon minero.
- **Otros archivos:** los dos `.zip` de la carpeta son módulos de la ENAHO 2024 (hogares). No traen datos de canon.

No voy a estimar la cifra a partir de la producción de cobre ni de otras series. Sería inventarla.

Para obtenerla, conviene consultar la fuente primaria. El MEF publica las transferencias de canon minero por departamento en su portal de Transparencia Económica. En BCRPData, el canon por departamento no aparece en el catálogo que tengo aquí.

RESPUESTA FINAL: No se pudo determinar con certeza. Los datos disponibles en esta carpeta, del catálogo del BCRP y de la ENAHO, no incluyen el canon minero de Cusco en 2024.

---

## Pregunta R3 · modo A

> **Pregunta:** ¿Cuánta inversión pública hubo en Lima en 2024?

#### 🤖 Claude · 2026-11-06 05:32 UTC

Empiezo revisando qué datos hay en la carpeta.

> 🔧 **Glob** `{"pattern": "**/*"}`

<details><summary>Resultado de la herramienta</summary>

```text
datos\catalogo_bcrp.csv
datos\966-Modulo02.zip
datos\966-Modulo34.zip
datos\peru_departamental_simple.geojson
.python-version
pyproject.toml
uv.lock
```
</details>

> 🔧 **Bash** `{"command": "cd datos; head -c 1500 catalogo_bcrp.csv; echo; grep -i -c \"inversi\" catalogo_bcrp.csv; python -c \"\nimport zipfile\nfor z in ['966-Modulo02.zip','966-Modulo34.zip']:\n    print(z,[ (i.filename,i.file_size) for i in zipfile.ZipFile(z).infolist()][:20])\""}`

<details><summary>Resultado de la herramienta</summary>

```text
Código de serie;Categoría de serie;Grupo de serie;Nombre de serie;Descripción de la serie;Metodología de la serie;Unidad de medida;Escala;Geografía (País, Región de Perú);Fuente;Frecuencia;Fecha de creación;Grupo de publicación;Área que publica;Fecha de actualización;Fecha de inicio;Fecha de fin;Memo;

PN00001MM;Sociedades creadoras de depósito;Cuentas monetarias de las sociedades creadoras de depósito;Activos Externos Netos de Corto Plazo (millones S/);https://estadisticas.bcrp.gob.pe/estadisticas/series/documentos/bcrpdataapi.pdf;https://estadisticas.bcrp.gob.pe/estadisticas/series/documentos/bcrpdataapi.pdf;;;;BCRP;Mensual;2022-03-24;Sistema financiero y empresas bancarias y expectativas sobre condiciones crediticias;Departamento de Estadísticas Monetarias;2026-10-23;Ene-1992;Dic-2025;;

PN00002MM;Sociedades creadoras de depósito;Cuentas monetarias de las sociedades creadoras de depósito;Activos Externos Netos de Corto Plazo (millones US$);;;;;;BCRP;Mensual;2022-03-24;Sistema financiero y empresas bancarias y expectativas sobre condiciones crediticias;Departamento de Estadísticas Monetarias;2026-10-23;Ene-1992;Dic-2025;;

PN00003MM;Sociedades creadoras de depósito;Cuentas monetarias de las sociedades creadoras de depósito;Activos Externos Netos de Corto Plazo - Activos (millones US$);;;;;;BCRP;Mensual;2022-03-24;Sistema financiero y empresas bancarias y expectativas sobre condiciones crediticias;Departamento de Estadísticas Monetarias;2026-10-23;Ene-19
647
966-Modulo02.zip [('966-Modulo02/', 0), ('966-Modulo02/CED-01-200-2024.pdf', 201079), ('966-Modulo02/Criterios para codificar Ocupaciones Peligrosas.pdf', 395343), ('966-Modulo02/Diccionario2024.pdf', 3940690), ('966-Modulo02/enaho01-2024-200.dta', 10217755), ('966-Modulo02/enaho_tabla_ciuo_88.dta', 349153), ('966-Modulo02/enaho_tabla_cno_2015.dta', 56727), ('966-Modulo02/FichaTecnica.pdf', 487444)]

966-Modulo34.zip [('966-Modulo34/', 0), ('966-Modulo34/ConstVarGasto-Metodologia actualizada.zip', 24486), ('966-Modulo34/DefinicionValoresMonetariosBasedeDatos.pdf', 254671), ('966-Modulo34/Diccionario2024.pdf', 3940690), ('966-Modulo34/Estratificacion del Marco.pdf', 207192), ('966-Modulo34/FichaTecnica.pdf', 487444), ('966-Modulo34/sumaria-2024-12g.dta', 29991565), ('966-Modulo34/Sumaria-2024-12g.pdf', 2727028), ('966-Modulo34/sumaria-2024.dta', 21219121), ('966-Modulo34/Sumaria-2024.pdf', 2142849)]
Shell cwd was reset to C:\Users\[usuario]\AppData\Local\Temp\tarea4_modoA_j1alngwo
```
</details>

#### 🤖 Claude · 2026-11-06 05:32 UTC

The ENAHO files are household surveys, so they won't help. I'll look in the BCRP catalogue for public investment series for Lima.

> 🔧 **Bash** `{"command": "cd datos; python -c \"\nimport csv\nr=csv.reader(open('catalogo_bcrp.csv',encoding='utf-8'),delimiter=';')\nh=next(r)\nfor x in r:\n    s=' '.join(x[1:4]).lower()\n    if 'inversi' in s and 'p' in s and ('pública' in s or 'publica' in s):\n        print(x[0],'|',x[3],'|',x[6],'|',x[8],'|',x[10],'|',x[15],x[16])\n\" | head -60"}`

<details><summary>Resultado de la herramienta</summary>

```text
PN02458FQ | Sector P�blico No Financiero - Gastos de Capital - Inversi�n P�blica |  |  | Trimestral | T1-2012 T4-2025

PN02523AQ | Demanda Interna - Inversi�n Bruta Interna - Inversi�n Bruta Fija - P�blica |  |  | Trimestral | T1-1980 T4-2025

PN02534AQ | Demanda Interna - Inversi�n Bruta Interna - Inversi�n Bruta Fija - P�blica |  |  | Trimestral | T1-1979 T4-2025

PN02546AQ | Demanda Interna - Inversi�n Bruta Interna - Inversi�n Bruta Fija - P�blica |  |  | Trimestral | T1-1980 T4-2025

PN02557AQ | Demanda Interna - Inversi�n Bruta Interna - Inversi�n Bruta Fija - P�blica |  |  | Trimestral | T1-1980 T4-2025

PN03049FQ | Gastos de Capital - Inversi�n P�blica |  |  | Trimestral | T1-1990 T4-2025

PN03105FQ | Gastos de Capital - Inversi�n P�blica |  |  | Trimestral | T1-1990 T4-2025

PM04920AA | Demanda Interna - Inversi�n Bruta Interna - Inversi�n Bruta Fija - P�blica |  |  | Anual | 1951 2025

PM04931AA | Demanda Interna - Inversi�n Bruta Interna - Inversi�n Bruta Fija - P�blica |  |  | Anual | 1950 2025

PM04942AA | Demanda Interna - Inversi�n Bruta Interna - Inversi�n Bruta Fija - P�blica |  |  | Anual | 1950 2025

PM04953AA | Demanda Interna - Inversi�n Bruta Interna - Inversi�n Bruta Fija - P�blica |  |  | Anual | 1951 2025

PM04963AA | Demanda Interna - Inversi�n Bruta Interna - Inversi�n Bruta Fija - P�blica |  |  | Anual | 1950 2025

PM10075FA | Inversi�n P�blica (millones S/) |  |  | Anual | 1970 2025

PM10081FA | Inversi�n P�blica |  |  | Anual | 1970 2025

CD10478DA | Demanda Interna - Inversi�n Bruta Interna - Inversion Bruta Fija - Publica |  | PE | Anual | 1950 1980

CD10881DA | Gastos de Capital - Inversi�n P�blica |  | PE | Anual | 1970 1980

PD39580DA | Inversi�n Bruta Fija - P�blica (Var.%) |  |  | Anual | 1951 2021

PD39589DA | Inversi�n Bruta Fija - P�blica (Mill S/ 2007) |  |  | Anual | 1950 2021
Shell cwd was reset to C:\Users\[usuario]\AppData\Local\Temp\tarea4_modoA_j1alngwo
```
</details>

> 🔧 **Bash** `{"command": "cd datos; python -c \"\nimport csv\nr=csv.reader(open('catalogo_bcrp.csv',encoding='utf-8',errors='replace'),delimiter=';')\nh=next(r)\nn=0\nfor x in r:\n    s=' '.join(x[1:5]).lower()\n    if 'lima' in x[8].lower() and ('inversi' in s or 'capital' in s):\n        print(x[0],'|',x[3],'|',x[8],'|',x[10]);n+=1\nprint(n)\n\"; ls ~ 2>/dev/null | head -0; curl -s -m 10 -I https://estadisticas.bcrp.gob.pe | head -3"}`

<details><summary>Resultado de la herramienta</summary>

```text
0

HTTP/1.1 200 OK

Date: Fri, 06 Nov 2026 05:38:28 GMT

Content-Type: text/html; charset=utf-8
Shell cwd was reset to C:\Users\[usuario]\AppData\Local\Temp\tarea4_modoA_j1alngwo
```
</details>

> 🔧 **Bash** `{"command": "cd datos; python -c \"\nimport csv\nr=csv.reader(open('catalogo_bcrp.csv',encoding='utf-8',errors='replace'),delimiter=';')\nh=next(r)\nfor x in r:\n    s=(x[1]+x[2]+x[3]).lower()\n    if ('inversi' in s and ('regional' in s or 'departamento' in s or 'lima' in s or 'gobiernos' in s)) or (x[8] and 'inversi' in s):\n        print(x[0],'|',x[1][:40],'|',x[3][:90],'|',x[8],'|',x[10])\n\" | head -40"}`

<details><summary>Resultado de la herramienta</summary>

```text
CD10445DA | Entre 1930 a 1980 | Inversi�n Bruta Fija - Total | PE | Anual

CD10446DA | Entre 1930 a 1980 | Inversi�n Bruta Fija - N. const | PE | Anual

CD10447DA | Entre 1930 a 1980 | Inversi�n Bruta Fija - Equipo | PE | Anual

CD10455DA | Entre 1930 a 1980 | Inversi�n Bruta Fija - Total | PE | Anual

CD10456DA | Entre 1930 a 1980 | Inversi�n Bruta Fija - N. const. | PE | Anual

CD10457DA | Entre 1930 a 1980 | Inversi�n Bruta Fija - Equipo | PE | Anual

CD10477DA | Entre 1930 a 1980 | Demanda Interna - Inversi�n Bruta Interna - Inversion Bruta Fija - Privada | PE | Anual

CD10478DA | Entre 1930 a 1980 | Demanda Interna - Inversi�n Bruta Interna - Inversion Bruta Fija - Publica | PE | Anual

CD10479DA | Entre 1930 a 1980 | Demanda Interna - Inversi�n Bruta Interna - Inversion Bruta Fija - Total | PE | Anual

CD10480DA | Entre 1930 a 1980 | Demanda Interna - Inversi�n Bruta Interna - Variaci�n de Existencias | PE | Anual

CD10481DA | Entre 1930 a 1980 | Demanda Interna - Inversi�n Bruta Interna - Total | PE | Anual

CD10881DA | Entre 1930 a 1980 | Gastos de Capital - Inversi�n P�blica | PE | Anual

CD11855DA | Primera centuria independiente | Inversi�n Bruta Fija - Total | PE | Anual

CD11856DA | Primera centuria independiente | Inversi�n Bruta Fija - N. const. | PE | Anual

CD11857DA | Primera centuria independiente | Inversi�n Bruta Fija - Equipo | PE | Anual

CD11865DA | Primera centuria independiente | Inversi�n Bruta Fija - Total | PE | Anual

CD11866DA | Primera centuria independiente | Inversi�n Bruta Fija - N. const. | PE | Anual

CD11867DA | Primera centuria independiente | Inversi�n Bruta Fija - Equipo | PE | Anual

RD14092DM | Sector p�blico | Amazonas | RE | Mensual

RD14093DM | Sector p�blico | Ancash | RE | Mensual

RD14094DM | Sector p�blico | Apur�mac | RE | Mensual

RD14095DM | Sector p�blico | Arequipa | RE | Mensual

RD14096DM | Sector p�blico | Ayacucho | RE | Mensual

RD14097DM | Sector p�blico | Cajamarca | RE | Mensual

RD14098DM | Sector p�blico | Callao | RE | Mensual

RD14099DM | Sector p�blico | Cusco | RE | Mensual

RD14100DM | Sector p�blico | Huancavelica | RE | Mensual

RD14101DM | Sector p�blico | Hu�nuco | RE | Mensual

RD14102DM | Sector p�blico | Ica | RE | Mensual

RD14103DM | Sector p�blico | Jun�n | RE | Mensual

RD14104DM | Sector p�blico | La Libertad | RE | Mensual

RD14105DM | Sector p�blico | Lambayeque | RE | Mensual

RD14106DM | Sector p�blico | Lima | RE | Mensual

RD14107DM | Sector p�blico | Loreto | RE | Mens
… [407 caracteres más omitidos]
```
</details>

> 🔧 **Bash** `{"command": "cd datos; python -c \"\nimport csv\nr=csv.reader(open('catalogo_bcrp.csv',encoding='utf-8',errors='replace'),delimiter=';')\nh=next(r)\nfor x in r:\n    if x[0] in('RD14106DM',) or (x[1].startswith('Sector p') and x[8]=='RE' and 'Lima' in x[3]) : print(x)\n\""}`

<details><summary>Resultado de la herramienta</summary>

```text
<persisted-output>
Output too large (32.8KB). Full output saved to: C:\Users\[usuario]\.claude\projects\C--Users-[usuario]-AppData-Local-Temp-tarea4-modoA-j1alngwo\a7e290a5-fa6c-49f5-ba79-6ae899ac98be\tool-results\b5xs1q74z.txt

Preview (first 2KB):
['RD13788DM', 'Sector p�blico', 'Ingresos tributarios recaudados por SUNAT - tributos internos seg�n departamento', 'Lima Metropolitana (millones de soles)', 'Informaci�n estad�stica regional / Sector p�blico / Ingresos tributarios recaudados por SUNAT - tributos internos seg�n departamento / Lima Metropolitana (millones de soles)', '', '', '', 'RE', 'Sunat', 'Mensual', '2017-05-02', '', 'Departamento de Bases de Datos Macroecon�micas', '2026-09-16', 'Ene-1994', 'Dic-2025', '', '']

['RD13789DM', 'Sector p�blico', 'Ingresos tributarios recaudados por SUNAT - tributos internos seg�n departamento', 'Lima provincias (millones de soles)', 'Informaci�n estad�stica regional / Sector p�blico / Ingresos tributarios recaudados por SUNAT - tributos internos seg�n departamento / Lima provincias (millones de soles)', '', '', '', 'RE', 'Sunat', 'Mensual', '2017-05-02', '', 'Departamento de Bases de Datos Macroecon�micas', '2026-09-16', 'Ene-1994', 'Dic-2025', '', '']

['RD13815DM', 'Sector p�blico', 'Ingresos tributarios recaudados por SUNAT - tributos internos seg�n departamento', 'Lima Metropolitana (var% anual)', 'Informaci�n estad�stica regional / Sector p�blico / Ingresos tributarios recaudados por SUNAT - tributos internos seg�n departamento / Lima Metropolitana (var% anual)', '', '', '', 'RE', 'Sunat', 'Mensual', '2017-05-02', '', 'Departamento de Bases de Datos Macroecon�micas', '2026-09-16', 'Ene-1995', 'Dic-2025', '', '']

['RD13816DM', 'Sector p�blico', 'Ingresos tributarios recaudados por SUNAT - tributos internos seg�n departamento', 'Lima provincias (var% anual)', 'Informaci�n estad�stica regional / Sector p�blico / Ingresos tributarios recaudados por SUNAT - tributos internos seg�n departamento / Lima provincias (var% anual)', '', '', '', 'RE', 'Sunat', 'Mensual', '2017-05-02', '', 'Departamento de Bases de Datos Macroecon�micas', '2026-09-16', 'Ene-1995', 'Dic-2025', '', '']

...
</persisted-output>
Shell cwd was reset to C:\Users\[usuario]\AppData\Local\Temp\tarea4_modoA_j1alngwo
```
</details>

#### 🤖 Claude · 2026-11-06 05:32 UTC

Esas series son de tributos. Busco series regionales de inversión pública (gobiernos regionales y locales, o gasto de capital).

> 🔧 **Bash** `{"command": "cd datos; python -c \"\nimport csv\nr=csv.reader(open('catalogo_bcrp.csv',encoding='utf-8',errors='replace'),delimiter=';')\nh=next(r)\nseen=set()\nfor x in r:\n    if x[8]=='RE' and ('inversi' in x[2].lower() or 'inversi' in x[3].lower() or 'capital' in x[2].lower()):\n        k=x[2]\n        if k not in seen: seen.add(k);print(x[0],'|',x[2],'|',x[3],'|',x[10],x[15],x[16])\n\""}`

<details><summary>Resultado de la herramienta</summary>

```text
RD14092DM | Inversi�n bruta fija del gobierno nacional por departamentos (millones S/) | Amazonas | Mensual Ene-2008 Dic-2025

RD14118DM | Inversi�n bruta fija de gobiernos locales por departamentos (millones S/) | Amazonas | Mensual Ene-2008 Dic-2025

RD14144DM | Inversi�n bruta fija de los gobiernos regionales (millones S/) | Amazonas | Mensual Ene-2008 Dic-2025
Shell cwd was reset to C:\Users\[usuario]\AppData\Local\Temp\tarea4_modoA_j1alngwo
```
</details>

> 🔧 **Bash** `{"command": "cd datos; python -c \"\nimport csv\nr=csv.reader(open('catalogo_bcrp.csv',encoding='utf-8',errors='replace'),delimiter=';')\nnext(r)\nfor x in r:\n    if x[8]=='RE' and 'inversi' in x[2].lower() and x[3].startswith(('Lima','Callao')): print(x[0],x[2][:60],x[3])\n\""}`

<details><summary>Resultado de la herramienta</summary>

```text
RD14098DM Inversi�n bruta fija del gobierno nacional por departamentos Callao

RD14106DM Inversi�n bruta fija del gobierno nacional por departamentos Lima

RD14124DM Inversi�n bruta fija de gobiernos locales por departamentos  Callao

RD14132DM Inversi�n bruta fija de gobiernos locales por departamentos  Lima

RD14167DM Inversi�n bruta fija de los gobiernos regionales (millones S Lima

RD14168DM Inversi�n bruta fija de los gobiernos regionales (millones S Callao

RD15409DQ Inversi�n bruta fija del gobierno nacional por departamentos Callao (millones de soles)

RD15417DQ Inversi�n bruta fija del gobierno nacional por departamentos Lima (millones de soles)

RD15435DQ Inversi�n bruta fija de gobiernos locales por departamentos  Callao (millones de soles)

RD15443DQ Inversi�n bruta fija de gobiernos locales por departamentos  Lima (millones de soles)

RD15478DQ Inversi�n bruta fija de los gobiernos regionales (millones S Lima (millones de soles)

RD15479DQ Inversi�n bruta fija de los gobiernos regionales (millones S Callao (millones de soles)

RD16663DA Inversi�n bruta fija del gobierno nacional por departamentos Callao (millones de soles)

RD16671DA Inversi�n bruta fija del gobierno nacional por departamentos Lima (millones de soles)

RD16689DA Inversi�n bruta fija de gobiernos locales por departamentos  Callao (millones de soles)

RD16697DA Inversi�n bruta fija de gobiernos locales por departamentos  Lima (millones de soles)

RD16732DA Inversi�n bruta fija de los gobiernos regionales (millones S Lima (millones de soles)

RD16733DA Inversi�n bruta fija de los gobiernos regionales (millones S Callao (millones de soles)
Shell cwd was reset to C:\Users\[usuario]\AppData\Local\Temp\tarea4_modoA_j1alngwo
```
</details>

#### 🤖 Claude · 2026-11-06 05:32 UTC

Hay series anuales. Las consulto en la API del BCRP.

> 🔧 **Bash** `{"command": "for s in RD16671DA RD16697DA RD16732DA; do echo $s; curl -s -m 30 \"https://estadisticas.bcrp.gob.pe/estadisticas/series/api/$s/json/2023/2025\"; echo; done"}`

<details><summary>Resultado de la herramienta</summary>

```text
RD16671DA
{
"config":
{
"title":"Inversión bruta fija del gobierno nacional por departamentos (millones S/)",
"series":
[
{
"name":"Inversión bruta fija del gobierno nacional por departamentos (millones S/) - Lima (millones de soles)",
"dec":"0"
}]
},
"periods":
[
{
"name":"2023",
"values":["8054.5637"]
},
{
"name":"2024",
"values":["9694.186703"]
},
{
"name":"2025",
"values":["10130.092207"]
}
]
}
RD16697DA
{
"config":
{
"title":"Inversión bruta fija de gobiernos locales por departamentos (millones S/)",
"series":
[
{
"name":"Inversión bruta fija de gobiernos locales por departamentos (millones S/) - Lima (millones de soles)",
"dec":"0"
}]
},
"periods":
[
{
"name":"2023",
"values":["1259.0215"]
},
{
"name":"2024",
"values":["1714.359388"]
},
{
"name":"2025",
"values":["2857.040428"]
}
]
}
RD16732DA
{
"config":
{
"title":"Inversión bruta fija de los gobiernos regionales (millones S/)",
"series":
[
{
"name":"Inversión bruta fija de los gobiernos regionales (millones S/) - Lima (millones de soles)",
"dec":"0"
}]
},
"periods":
[
{
"name":"2023",
"values":["275.88359"]
},
{
"name":"2024",
"values":["412.583078"]
},
{
"name":"2025",
"values":["519.548883"]
}
]
}
Shell cwd was reset to C:\Users\[usuario]\AppData\Local\Temp\tarea4_modoA_j1alngwo
```
</details>

#### 🤖 Claude · 2026-11-06 05:32 UTC

En 2024, la inversión pública en el departamento de Lima fue de unos **S/ 11 821 millones**. Es la inversión bruta fija de los tres niveles de gobierno, según las series anuales departamentales del BCRP, que consulté en su API.

| Nivel de gobierno | Serie BCRP | 2024 (millones S/) |
|---|---|---|
| Gobierno nacional | RD16671DA | 9 694,19 |
| Gobiernos locales | RD16697DA | 1 714,36 |
| Gobierno regional | RD16732DA | 412,58 |
| **Total** | | **11 821,13** |

**Alcance de la cifra**
- **Lima:** es el departamento de Lima, que el BCRP publica separado del Callao. Los datos no dicen si «Lima» incluye o no Lima Provincias. No sumé el Callao.
- **Medida:** es inversión bruta fija, y no incluye la inversión de empresas públicas. Puede diferir de las cifras de ejecución del MEF.
- **Gobierno nacional:** el gasto de entidades nacionales ubicado en Lima suele incluir proyectos de alcance nacional. Por eso la cifra no refleja solo obras que benefician a Lima.
- **Datos de la carpeta:** los archivos de ENAHO son encuestas de hogares y no sirven para esta pregunta. Solo usé el catálogo del BCRP para ubicar las series.

RESPUESTA FINAL: Inversión pública en Lima en 2024 ≈ S/ 11 821 millones (gobierno nacional S/ 9 694 M + gobiernos locales S/ 1 714 M + gobierno regional S/ 413 M), según el BCRP.

---

## Pregunta R4 · modo A

> **Pregunta:** Con la ENAHO 2024, ¿cuál es la tasa de pobreza monetaria del distrito de Miraflores, en Lima?

#### 🤖 Claude · 2026-11-06 05:32 UTC

Voy a revisar primero qué hay en la carpeta.

> 🔧 **Glob** `{"pattern": "**/*"}`

<details><summary>Resultado de la herramienta</summary>

```text
datos\catalogo_bcrp.csv
datos\966-Modulo02.zip
datos\966-Modulo34.zip
datos\peru_departamental_simple.geojson
.python-version
pyproject.toml
uv.lock
```
</details>

> 🔧 **Bash** `{"command": "cd datos; ls -la; head -c 600 catalogo_bcrp.csv; python -c \"\nimport zipfile\nfor f in ['966-Modulo02.zip','966-Modulo34.zip']:\n    print(f,[ (i.filename,i.file_size) for i in zipfile.ZipFile(f).infolist()])\""}`

<details><summary>Resultado de la herramienta</summary>

```text
total 28216
drwxr-xr-x 1 [usuario] 197121        0 Nov  5 06:23 .
drwxr-xr-x 1 [usuario] 197121        0 Nov  6 00:32 ..
-rw-r--r-- 1 [usuario] 197121  5793097 Nov  5 06:23 966-Modulo02.zip
-rw-r--r-- 1 [usuario] 197121 15935617 Nov  5 06:23 966-Modulo34.zip
-rw-r--r-- 1 [usuario] 197121  7005225 Nov  5 06:23 catalogo_bcrp.csv
-rw-r--r-- 1 [usuario] 197121   139681 Nov  5 06:23 peru_departamental_simple.geojson
Código de serie;Categoría de serie;Grupo de serie;Nombre de serie;Descripción de la serie;Metodología de la serie;Unidad de medida;Escala;Geografía (País, Región de Perú);Fuente;Frecuencia;Fecha de creación;Grupo de publicación;Área que publica;Fecha de actualización;Fecha de inicio;Fecha de fin;Memo;

PN00001MM;Sociedades creadoras de depósito;Cuentas monetarias de las sociedades creadoras de depósito;Activos Externos Netos de Corto Plazo (millones S/);https://estadisticas.bcrp.gob.pe/estadisticas/series/documentos/bcrpdataapi.pdf;https://estadisticas.bcrp.gob.pe/estadisticas/se966-Modulo02.zip [('966-Modulo02/', 0), ('966-Modulo02/CED-01-200-2024.pdf', 201079), ('966-Modulo02/Criterios para codificar Ocupaciones Peligrosas.pdf', 395343), ('966-Modulo02/Diccionario2024.pdf', 3940690), ('966-Modulo02/enaho01-2024-200.dta', 10217755), ('966-Modulo02/enaho_tabla_ciuo_88.dta', 349153), ('966-Modulo02/enaho_tabla_cno_2015.dta', 56727), ('966-Modulo02/FichaTecnica.pdf', 487444)]

966-Modulo34.zip [('966-Modulo34/', 0), ('966-Modulo34/ConstVarGasto-Metodologia actualizada.zip', 24486), ('966-Modulo34/DefinicionValoresMonetariosBasedeDatos.pdf', 254671), ('966-Modulo34/Diccionario2024.pdf', 3940690), ('966-Modulo34/Estratificacion del Marco.pdf', 207192), ('966-Modulo34/FichaTecnica.pdf', 487444), ('966-Modulo34/sumaria-2024-12g.dta', 29991565), ('966-Modulo34/Sumaria-2024-12g.pdf', 2727028), ('966-Modulo34/sumaria-2024.dta', 21219121), ('966-Modulo34/Sumaria-2024.pdf', 2142849)]
Shell cwd was reset to C:\Users\[usuario]\AppData\Local\Temp\tarea4_modoA_m6ts8m2_
```
</details>

> 🔧 **Bash** `{"command": "mkdir -p /tmp/e34 && cd /tmp/e34 && unzip -oq \"C:/Users/[usuario]/AppData/Local/Temp/tarea4_modoA_m6ts8m2_/datos/966-Modulo34.zip\" && cd /C/Users/[usuario]/AppData/Local/Temp/tarea4_modoA_m6ts8m2_ 2>/dev/null; cd \"C:/Users/[usuario]/AppData/Local/Temp/tarea4_modoA_m6ts8m2_\"; cat pyproject.toml; python -I -c \"\nimport pandas as pd\nd=pd.read_stata('/tmp/e34/966-Modulo34/sumaria-2024.dta',convert_categoricals=False)\nprint(d.shape);print([c for c in d.columns if c.lower() in ('ubigeo','dominio','estrato','pobreza','factor07','mieperho','conglome','vivienda','hogar','dpto','departamento','provincia','distrito','fac500a')])\nprint(d.columns.tolist())\nprint(d.ubigeo.head() if 'ubigeo' in d else '')\n\""}`

<details><summary>Resultado de la herramienta</summary>

```text
Exit code 1
[project]
name = "tarea-4-agente-inversion-pobreza"
version = "0.1.0"
description = "Agente de investigación: MCP del BCRP y Skills de la ENAHO 2024 para comparar el reparto de la inversión pública con el de la pobreza"
readme = "README.md"
requires-python = ">=3.14"
dependencies = [
    "fastmcp>=4,<5",
    "geopandas>=1.2.0",
    "httpx",
    "matplotlib>=3.11.2",
    "pandas>=3.1.0",
    "pyarrow>=26.0.0",
]

[dependency-groups]
dev = ["pytest"]

[tool.pytest.ini_options]
testpaths = ["mcp"]
Traceback (most recent call last):

  File "<string>", line 3, in <module>

    d=pd.read_stata('/tmp/e34/966-Modulo34/sumaria-2024.dta',convert_categoricals=False)

  File "C:\Users\[usuario]\Documents\GitHub\Python_Interm\Tareas\Tarea_4\.venv\Lib\site-packages\pandas\io\stata.py", line 2305, in read_stata

    return reader.read()

           ~~~~~~~~~~~^^

  File "C:\Users\[usuario]\Documents\GitHub\Python_Interm\Tareas\Tarea_4\.venv\Lib\site-packages\pandas\io\stata.py", line 1705, in read

    self._ensure_open()

    ~~~~~~~~~~~~~~~~~^^

  File "C:\Users\[usuario]\Documents\GitHub\Python_Interm\Tareas\Tarea_4\.venv\Lib\site-packages\pandas\io\stata.py", line 1152, in _ensure_open

    self._open_file()

    ~~~~~~~~~~~~~~~^^

  File "C:\Users\[usuario]\Documents\GitHub\Python_Interm\Tareas\Tarea_4\.venv\Lib\site-packages\pandas\io\stata.py", line 1165, in _open_file

    handles = get_handle(

        self._original_path_or_buf,

    ...<3 lines>...

        compression=self._compression,

    )

  File "C:\Users\[usuario]\Documents\GitHub\Python_Interm\Tareas\Tarea_4\.venv\Lib\site-packages\pandas\io\common.py", line 954, in get_handle

    handle = open(handle, ioargs.mode)

FileNotFoundError: [Errno 2] No such file or directory: '/tmp/e34/966-Modulo34/sumaria-2024.dta'
```
</details>

#### 🤖 Claude · 2026-11-06 05:32 UTC

Python de Windows no ve /tmp de Git Bash; uso una ruta de Windows.

> 🔧 **Bash** `{"command": "D=\"$LOCALAPPDATA/Temp/e34_x\"; mkdir -p \"$D\"; cd \"$D\" && unzip -oq \"$LOCALAPPDATA/Temp/tarea4_modoA_m6ts8m2_/datos/966-Modulo34.zip\"; cd \"$LOCALAPPDATA/Temp/tarea4_modoA_m6ts8m2_\"; python -I -c \"\nimport pandas as pd,os\np=os.path.expandvars(r'%LOCALAPPDATA%')+r'\\Temp\\e34_x\\966-Modulo34\\sumaria-2024.dta'\nd=pd.read_stata(p,convert_categoricals=False)\nprint(d.shape);print(d.columns.tolist())\nprint(d[['ubigeo']].head() if 'ubigeo' in d else 'no ubigeo')\n\""}`

<details><summary>Resultado de la herramienta</summary>

```text
(33691, 163)

['a�o', 'mes', 'conglome', 'vivienda', 'hogar', 'ubigeo', 'dominio', 'estrato', 'mieperho', 'totmieho', 'percepho', 'ia01hd', 'ia02hd', 'ig03hd1', 'ig03hd2', 'ig03hd3', 'ig03hd4', 'ga03hd', 'ga04hd', 'sg23', 'sig24', 'sg25', 'sig26', 'sg27', 'sig28', 'sg42', 'sg421', 'sg422', 'sg423', 'sg42d', 'sg42d1', 'sg42d2', 'sg42d3', 'ingbruhd', 'ingnethd', 'pagesphd', 'ingindhd', 'ingauthd', 'insedthd', 'insedlhd', 'paesechd', 'ingseihd', 'isecauhd', 'ingexthd', 'ingtrahd', 'ingtexhd', 'ingrenhd', 'ingoexhd', 'g05hd', 'ig06hd', 'g05hd1', 'ig06hd1', 'g05hd2', 'ig06hd2', 'g05hd3', 'ig06hd3', 'g05hd4', 'ig06hd4', 'g05hd5', 'ig06hd5', 'g05hd6', 'ig06hd6', 'g07hd', 'ig08hd', 'ingtprhd', 'ingtpuhd', 'ingtpu01', 'ingtpu02', 'ingtpu03', 'ingtpu04', 'ingtpu05', 'ingtpu10', 'ingtpu11', 'ingtpu12', 'ingtpu13', 'ingtpu14', 'ingtpu15', 'ingtpu16', 'gru11hd', 'gru12hd1', 'gru12hd2', 'gru13hd1', 'gru13hd2', 'gru13hd3', 'gru13hd4', 'gru14hd', 'gru14hd1', 'gru14hd2', 'gru14hd3', 'gru14hd4', 'gru14hd5', 'gru14hd6', 'gru21hd', 'gru22hd1', 'gru22hd2', 'gru23hd1', 'gru23hd2', 'gru23hd3', 'gru24hd', 'gru31hd', 'gru32hd1', 'gru32hd2', 'gru33hd1', 'gru33hd2', 'gru33hd3', 'gru34hd', 'gru41hd', 'gru42hd1', 'gru42hd2', 'gru43hd1', 'gru43hd2', 'gru43hd3', 'gru44hd', 'gru51hd', 'gru52hd1', 'gru53hd1', 'gru53hd2', 'gru53hd3', 'gru53hd4', 'gru54hd', 'gru61hd', 'gru62hd1', 'gru62hd2', 'gru63hd1', 'gru63hd2', 'gru63hd3', 'gru64hd', 'gru71hd', 'gru72hd1', 'gru72hd2', 'gru73hd1', 'gru73hd2', 'gru73hd3', 'gru74hd', 'gru81hd', 'gru82hd1', 'gru82hd2', 'gru83hd1', 'gru83hd2', 'gru83hd3', 'gru83hd4', 'gru84hd', 'gru84hd1', 'gru85hd1', 'gru86hd1', 'gru86hd2', 'gru87hd', 'ingmo1hd', 'ingmo2hd', 'inghog1d', 'inghog2d', 'gashog1d', 'gashog2d', 'estrsocial', 'ld', 'linpe', 'linea', 'pobreza', 'factor07', 'lineav', 'pobrezav', 'nconglome', 'sub_conglome']

   ubigeo

0  010101

1  010101

2  010101

3  010101

4  010101
Shell cwd was reset to C:\Users\[usuario]\AppData\Local\Temp\tarea4_modoA_m6ts8m2_
```
</details>

> 🔧 **Bash** `{"command": "python -I -c \"\nimport pandas as pd,os\np=os.path.expandvars(r'%LOCALAPPDATA%')+r'\\Temp\\e34_x\\966-Modulo34\\sumaria-2024.dta'\nd=pd.read_stata(p,convert_categoricals=False)\nm=d[d.ubigeo=='150122']\nprint(len(m),m.conglome.nunique())\nprint(m.pobreza.value_counts())\nw=m.factor07*m.mieperho\nprint('pobres (1,2) pers-pond:',w[m.pobreza.isin([1,2])].sum()/w.sum())\nprint('hogares:',m.factor07[m.pobreza.isin([1,2])].sum()/m.factor07.sum(), 'pob expandida',w.sum())\nprint('sin pond:',m.pobreza.isin([1,2]).mean())\n\""}`

<details><summary>Resultado de la herramienta</summary>

```text
61 11

pobreza

3    61

Name: count, dtype: int64

pobres (1,2) pers-pond: 0.0

hogares: 0.0 pob expandida 77567.61

sin pond: 0.0
Shell cwd was reset to C:\Users\[usuario]\AppData\Local\Temp\tarea4_modoA_m6ts8m2_
```
</details>

#### 🤖 Claude · 2026-11-06 05:32 UTC

**Resultado: la muestra ENAHO 2024 da 0,0 % de pobreza monetaria para Miraflores, pero no es una cifra confiable como tasa distrital.**

Usé el módulo Sumaria 2024 (`sumaria-2024.dta`), filtré el ubigeo 150122 (Miraflores) y ponderé por `factor07 × mieperho`. La variable `pobreza` tiene 1 = pobre extremo, 2 = pobre no extremo y 3 = no pobre.

- **Muestra:** 61 hogares en 11 conglomerados. Los 61 están clasificados como no pobres (`pobreza` = 3).
- **Población representada:** unas 77 568 personas con el factor de expansión.
- **Tasa:** 0 de 61 hogares pobres. Es 0,0 % tanto ponderando por personas como por hogares, y también sin ponderar.

**Por qué no es confiable:**
- La ENAHO está diseñada para dar estimaciones confiables a nivel nacional, departamental y por dominios. No lo está para distritos.
- Con 61 hogares y 11 conglomerados, el error muestral es grande y no hay un intervalo de confianza útil.
- El INEI no publica una tasa distrital de pobreza a partir de la ENAHO. Sus cifras distritales vienen de mapas de pobreza que combinan el censo con la encuesta.
- Un 0,0 % muestral no significa que no haya hogares pobres en Miraflores. Solo indica que ninguno de los 61 hogares de la muestra lo era. Es coherente con un distrito de ingresos altos, pero no es una medición precisa.

RESPUESTA FINAL: En la ENAHO 2024 (Sumaria), la tasa de pobreza monetaria muestral de Miraflores (ubigeo 150122) es 0,0 % (0 de 61 hogares pobres; 11 conglomerados). No es una estimación distrital confiable, porque la ENAHO no es representativa a nivel de distrito.

---

## Pregunta R5 · modo A

> **Pregunta:** ¿Cuántos puntos de pobreza redujo la inversión pública en Cajamarca entre 2020 y 2024?

#### 🤖 Claude · 2026-11-06 05:32 UTC

Voy a revisar si hay datos en la carpeta.

> 🔧 **Glob** `{"pattern": "**/*"}`

<details><summary>Resultado de la herramienta</summary>

```text
datos\catalogo_bcrp.csv
datos\966-Modulo02.zip
datos\966-Modulo34.zip
datos\peru_departamental_simple.geojson
.python-version
pyproject.toml
uv.lock
```
</details>

> 🔧 **Bash** `{"command": "cd datos; head -c 1500 catalogo_bcrp.csv; echo; grep -i -c \"pobreza\" catalogo_bcrp.csv; unzip -l 966-Modulo02.zip | head -30; unzip -l 966-Modulo34.zip | head -30"}`

<details><summary>Resultado de la herramienta</summary>

```text
Código de serie;Categoría de serie;Grupo de serie;Nombre de serie;Descripción de la serie;Metodología de la serie;Unidad de medida;Escala;Geografía (País, Región de Perú);Fuente;Frecuencia;Fecha de creación;Grupo de publicación;Área que publica;Fecha de actualización;Fecha de inicio;Fecha de fin;Memo;

PN00001MM;Sociedades creadoras de depósito;Cuentas monetarias de las sociedades creadoras de depósito;Activos Externos Netos de Corto Plazo (millones S/);https://estadisticas.bcrp.gob.pe/estadisticas/series/documentos/bcrpdataapi.pdf;https://estadisticas.bcrp.gob.pe/estadisticas/series/documentos/bcrpdataapi.pdf;;;;BCRP;Mensual;2022-03-24;Sistema financiero y empresas bancarias y expectativas sobre condiciones crediticias;Departamento de Estadísticas Monetarias;2026-10-23;Ene-1992;Dic-2025;;

PN00002MM;Sociedades creadoras de depósito;Cuentas monetarias de las sociedades creadoras de depósito;Activos Externos Netos de Corto Plazo (millones US$);;;;;;BCRP;Mensual;2022-03-24;Sistema financiero y empresas bancarias y expectativas sobre condiciones crediticias;Departamento de Estadísticas Monetarias;2026-10-23;Ene-1992;Dic-2025;;

PN00003MM;Sociedades creadoras de depósito;Cuentas monetarias de las sociedades creadoras de depósito;Activos Externos Netos de Corto Plazo - Activos (millones US$);;;;;;BCRP;Mensual;2022-03-24;Sistema financiero y empresas bancarias y expectativas sobre condiciones crediticias;Departamento de Estadísticas Monetarias;2026-10-23;Ene-19
0
Archive:  966-Modulo02.zip
  Length      Date    Time    Name
---------  ---------- -----   ----
        0  2025-05-07 14:43   966-Modulo02/
   201079  2024-06-18 10:39   966-Modulo02/CED-01-200-2024.pdf
   395343  2021-05-07 11:05   966-Modulo02/Criterios para codificar Ocupaciones Peligrosas.pdf
  3940690  2025-05-16 14:36   966-Modulo02/Diccionario2024.pdf
 10217755  2025-05-07 14:39   966-Modulo02/enaho01-2024-200.dta
   349153  2020-05-11 21:36   966-Modulo02/enaho_tabla_ciuo_88.dta
    56727  2020-05-11 21:36   966-Modulo02/enaho_tabla_cno_2015.dta
   487444  2024-02-06 18:57   966-Modulo02/FichaTecnica.pdf
---------                     -------
 15648191                     8 files
Archive:  966-Modulo34.zip
  Length      Date    Time    Name
---------  ---------- -----   ----
        0  2026-05-14 09:56   966-Modulo34/
    24486  2025-05-07 19:18   966-Modulo34/ConstVarGasto-Metodologia actualizada.zip
   254671  2025-05-05 19:34   966-Modulo34/DefinicionValoresMonetariosBasedeDatos.pdf
  3940690
… [594 caracteres más omitidos]
```
</details>

#### 🤖 Claude · 2026-11-06 05:32 UTC

No puedo darte esa cifra con certeza, y no voy a inventarla.

**Qué hay en la carpeta:**
- Los microdatos de la ENAHO **solo del año 2024**: el módulo 200 y la base Sumaria, que incluye la pobreza por hogar.
- Un catálogo de series del BCRP. No tiene ninguna serie de pobreza (0 coincidencias con «pobreza»).
- Un geojson departamental.

**Qué falta:**
1. **La pobreza de Cajamarca en 2020.** Sin ella no puedo calcular la variación entre 2020 y 2024. Con los datos de 2024 solo podría estimar el nivel de ese año.
2. **Datos de inversión pública** de Cajamarca (por ejemplo, del MEF o del Invierte.pe). No hay ninguno en esta carpeta.
3. **Una forma de atribuir la baja a la inversión pública.** Aunque tuviera las dos puntas de pobreza, la diferencia no sería el efecto de la inversión. En ese periodo también influyeron la pandemia, la recuperación económica, las transferencias y los precios. Medir el efecto de la inversión requeriría un análisis causal, que estos datos no permiten.

Si me das la pobreza departamental de 2020 y 2024 (por ejemplo, de los cuadros del INEI), puedo calcular la variación en puntos porcentuales. Aun así, sería la variación total de la pobreza y no la parte atribuible a la inversión pública.

RESPUESTA FINAL: No se puede determinar con los datos disponibles (no hay pobreza de Cajamarca de 2020 ni datos de inversión pública, y la reducción no es atribuible causalmente solo a la inversión).

