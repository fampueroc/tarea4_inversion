# ¿La inversión pública se reparte donde vive la población pobre? Perú, 2020–2024

*Informe final, Tarea 4. Fiorella Ampuero, con Claude Code. Fecha: 6 de noviembre de 2026.*

## 1. Pregunta y delimitación

**Pregunta.** Entre 2020 y 2024, ¿la inversión pública se repartió entre los departamentos del Perú en proporción a dónde vive la población pobre?

**Delimitación.**

- **Unidad:** los 25 departamentos que publica el BCRP, con Lima y Callao por separado. Lima se trata como un solo departamento, como lo publica el BCRP. Un recuadro separa Lima Metropolitana y Lima provincias solo donde la fuente lo permite.
- **Inversión:** inversión bruta fija del gobierno nacional, los gobiernos regionales y los gobiernos locales, acumulada 2020–2024, en millones de soles corrientes (BCRP).
- **Pobreza:** pobreza monetaria 2024 y participación de cada departamento en el total de pobres del país (INEI, ENAHO 2024).
- **Comparación:** se compara la *parte* de la inversión de cada departamento con su *parte* de los pobres. Un cociente de 1 significa que recibe la misma parte de inversión que su parte de pobres.
- **Alcance:** el estudio es descriptivo. Compara dos repartos y no afirma que la inversión cause ni reduzca la pobreza, ni que un gobierno sea eficiente o ineficiente.

## 2. Fuentes y metodología

### Fuentes

| Fuente | Contenido | Archivo guardado |
|---|---|---|
| BCRP, inversión bruta fija del gobierno nacional por departamentos (series `RD16657DA`–`RD16681DA`; total `RD16682DA`) | 2020–2024, millones S/ | `salidas/bcrp_inversion_gobierno_nacional_2020_2024.csv` |
| BCRP, inversión de los gobiernos regionales por departamentos (series `RD16709DA`–`RD16733DA`; Municipalidad Metropolitana de Lima `RD16734DA`) | 2020–2024, millones S/ | `salidas/bcrp_inversion_gobiernos_regionales_2020_2024.csv` |
| BCRP, inversión de los gobiernos locales por departamentos (series `RD16683DA`–`RD16707DA`) | 2020–2024, millones S/ | `salidas/bcrp_inversion_gobiernos_locales_2020_2024.csv` |
| BCRP, exportaciones mineras por departamento (series `RD40961BA`–`RD41369BA`; «sin ubigeo» `RD41386BA`; total `PM40047BA`) | 2018–2022, millones US$ FOB | `salidas/bcrp_exportaciones_mineras_2018_2022.csv` |
| INEI, ENAHO 2024, módulos 34 (sumaria) y 02 (miembros del hogar) | Pobreza monetaria | `datos/966-Modulo34.zip`, `datos/966-Modulo02.zip` → `salidas/personas_2024.parquet` |
| INEI, *Perú: Evolución de la Pobreza Monetaria 2015-2024*, anexo p. 220 | Referencia oficial para validar | `.claude/skills/analizando-reparto/referencias/inei_pobreza_2024.csv` |
| Límites departamentales | Mapa y superficie (km²) | `datos/peru_departamental_simple.geojson` |

Los datos del BCRP se descargaron con la herramienta `cuadre_territorial` del servidor MCP `bcrp`, con `guardar=True`, y no se copió ninguna cifra a mano. El BCRP actualizó por última vez las series de inversión el 30-04-2026.

### Metodología

1. **Cuadre del BCRP.** Para cada nivel de gobierno y cada año, la suma de los 25 departamentos debe igualar el total oficial. En los gobiernos regionales la diferencia corresponde a la Municipalidad Metropolitana de Lima, que se asigna a Lima.
2. **Limpieza de la ENAHO** (skill `limpiando-enaho`). Se unen la sumaria y el módulo 02, se conservan los residentes habituales y se valida la pobreza nacional contra la cifra oficial.
3. **Estimación con diseño muestral** (skill `analizando-reparto`). Se usan conglomerados (`conglome`) dentro de estratos departamento × estrato, con linealización. Se toman hogares únicos ponderados con `factor07 × mieperho`. Hay intervalos de confianza (IC) del 95 % para la pobreza, para la parte de pobres y para el cociente inversión/pobres.
4. **Partes, no conteos.** El INEI ajusta los conteos absolutos a las proyecciones de población, así que la base pública no reproduce el total de pobres. En cambio, las tasas y las partes sí coinciden con lo publicado.
5. **Indicadores de reparto:**
   - el cociente (% de la inversión 2020–2024) ÷ (% de los pobres 2024);
   - índices de concentración, con los departamentos ordenados de mayor a menor pobreza (un valor negativo indica que se concentra en los más pobres);
   - una regresión descriptiva de la inversión por habitante (en logaritmo) sobre la pobreza y el log de la densidad, con errores estándar robustos;
   - una correlación de Spearman con la parte de las exportaciones mineras 2018–2022.
6. **Visualizaciones:** un gráfico de barras de la pobreza (skill `graficando-enaho`) y un mapa coroplético unido por ubigeo, no por nombre (skill `mapeando-enaho`).

### Validaciones (todas aprobadas)

- **ENAHO nacional:** pobreza monetaria de 27.58 % con la sumaria y 27.53 % con personas, frente a 27.6 % oficial. Pobreza extrema de 5.50 %, frente a 5.5 % oficial. Hay 108,664 residentes habituales y 25 departamentos, y el resultado fue «APROBADO» (`salidas/validacion.txt`).
- **ENAHO por ámbito:** en los 27 ámbitos (los departamentos con Lima en dos partes, más el nacional), la diferencia máxima con el INEI es de 0.05 puntos. El semiancho de los IC está entre 0.95 y 1.01 veces el del INEI (`salidas/analisis.txt`).
- **Mapa:** los 25 departamentos tienen dato y la diferencia máxima con la referencia del curso es de 0.05 puntos (`salidas/mapa_vs_referencia.csv`).
- **BCRP, inversión:** los tres niveles cuadran con el total oficial todos los años, con diferencia sin explicar de 0 (`cuadre_territorial`; `salidas/analisis.txt`).

## 3. Contexto: evolución de la inversión 2020–2024

**Gobierno nacional** (herramienta `resumen`, serie `RD16682DA`, 2020–2024):

- pasó de 12,545.7 millones S/ en 2020 (el mínimo) a 25,109.3 millones S/ en 2024 (el máximo);
- el cambio fue de +12,563.6 millones, una variación de +100.14 %, con un promedio de 18,753.1 millones S/;
- la subida no fue continua: en 2022 el total (16,957.4) quedó algo por debajo del de 2021 (17,153.0), según los totales oficiales que devolvió `cuadre_territorial`.

**Los tres niveles juntos:** 226,627 millones S/ corrientes en 2020–2024, de 30,402 millones en 2020 a 57,945 millones en 2024 (`salidas/analisis.txt`).

![Inversión pública por nivel de gobierno, 2020–2024](../figuras/bcrp_inversion_anual.png)

*Figura 1. Inversión bruta fija por nivel de gobierno. Fuente: BCRP, series RD de inversión por departamentos (`salidas/bcrp_inversion_*_2020_2024.csv`).*

## 4. Dónde vive la población pobre (ENAHO 2024)

- **Mayor pobreza:** Cajamarca (45.0 %), Loreto (43.0 %), Puno (39.9 %), Pasco (39.0 %) y Huánuco (39.0 %).
- **Menor pobreza:** Ica (6.0 %), Moquegua (11.0 %) y Madre de Dios (11.1 %).
- **Promedio nacional:** 27.6 %.
- **Lima** tiene una tasa cercana al promedio (27.1 %), pero por su tamaño concentra el **32.11 %** de los pobres del país (IC 95 % 29.54–34.67).

Fuente: INEI, ENAHO 2024, con `graficando-enaho` y `salidas/indicadores.csv`.

![Pobreza monetaria por departamento, 2024](../figuras/pobreza_departamento.png)

*Figura 2. Pobreza monetaria por departamento (% de personas). Fuente: INEI, ENAHO 2024, ponderado con factor07 × mieperho (`figuras/pobreza_departamento.png`).*

![Mapa de la pobreza monetaria por departamento, 2024](../mapas/pobreza_departamento.png)

*Figura 3. Mapa de la pobreza monetaria por departamento. Fuente: INEI, ENAHO 2024; límites de `datos/peru_departamental_simple.geojson` (`mapas/pobreza_departamento.png`).*

## 5. Hallazgos

Todas las cifras de esta sección provienen de `salidas/analisis.txt` y `salidas/indicadores.csv`, que cruzan las series del BCRP de la sección 2 con la ENAHO 2024.

### Hallazgo 1: los departamentos con más pobreza reciben una parte de la inversión menor que su parte de pobres

**Los cinco departamentos más pobres** (Cajamarca, Loreto, Puno, Pasco y Huánuco):

- reúnen el **24.3 %** de los pobres del país;
- tienen el **16.0 %** de la población;
- recibieron el **15.7 %** de la inversión 2020–2024.

Es decir, su parte de la inversión se parece a su parte de la población, no a su parte de pobres.

**Siete departamentos** tienen todo el IC 95 % del cociente inversión/pobres por debajo de 1:

| Departamento | Pobreza 2024 | % de los pobres del país | % de la inversión 2020–2024 | Inversión / pobres [IC 95 %] |
|---|---|---|---|---|
| Cajamarca | 45.0 % | 7.36 % | 4.40 % | 0.60 [0.54–0.68] |
| Loreto | 43.0 % | 5.10 % | 3.18 % | 0.62 [0.56–0.71] |
| Puno | 39.9 % | 6.66 % | 4.36 % | 0.65 [0.57–0.77] |
| Huánuco | 39.0 % | 3.80 % | 2.55 % | 0.67 [0.58–0.79] |
| Callao | 33.9 % | 4.07 % | 2.58 % | 0.63 [0.53–0.78] |
| La Libertad | 30.2 % | 6.61 % | 5.01 % | 0.76 [0.67–0.88] |
| Lima | 27.1 % | 32.11 % | 19.77 % | 0.62 [0.57–0.67] |

**Los cocientes más altos** están en departamentos con poca pobreza:

| Departamento | Pobreza 2024 | Inversión / pobres [IC 95 %] |
|---|---|---|
| Moquegua | 11.0 % | 7.50 [5.61–11.28] |
| Madre de Dios | 11.1 % | 5.32 [3.74–9.20] |
| Ica | 6.0 % | 5.27 [3.98–7.80] |
| Cusco | 18.5 % | 3.43 [2.81–4.41] |

**Pasco** (39.0 %) es la excepción entre los cinco más pobres: su cociente es 0.90 y el IC [0.75–1.12] incluye el 1.

![Inversión / pobres por departamento](../figuras/inversion_vs_pobres.png)

*Figura 4. Cociente entre la parte de la inversión 2020–2024 y la parte de la población pobre 2024, con IC 95 %. Fuentes: BCRP (series RD); INEI, ENAHO 2024 (`figuras/inversion_vs_pobres.png`).*

### Hallazgo 2: la población pobre se concentra en los departamentos más pobres, pero la inversión no

Los índices de concentración ordenan los departamentos de mayor a menor pobreza:

| Concepto | Índice de concentración |
|---|---|
| Población pobre | −0.169 |
| Inversión total | +0.062 |
| Gobierno nacional | +0.027 |
| Gobiernos regionales | +0.026 |
| Gobiernos locales | +0.120 |

- **Inversión total:** el índice positivo indica que se concentra levemente hacia los departamentos *menos* pobres.
- **Por nivel de gobierno:** ningún nivel tiene un índice negativo. La inversión local es la que más se aleja del reparto de los pobres.

![Curvas de concentración](../figuras/curva_concentracion.png)

*Figura 5. Curvas de concentración de la inversión 2020–2024 y de la población pobre 2024. Fuentes: BCRP (series RD); INEI, ENAHO 2024 (`figuras/curva_concentracion.png`).*

### Hallazgo 3: con igual densidad, más pobreza se asocia a algo menos de inversión por habitante, pero la estimación es imprecisa

La regresión descriptiva de la inversión por habitante sobre la pobreza y la densidad (25 departamentos, R² = 0.31) da:

- **Pobreza:** −0.0118 por punto (EE robusto 0.0066; IC 95 % −0.0247 a +0.0012). Con igual densidad, un punto más de pobreza se asocia a cerca de −1.2 % de inversión por habitante. El IC incluye el cero, así que **no se puede descartar que no haya asociación**.
- **Densidad:** el coeficiente del log de la densidad es −0.1118 (EE 0.0414; IC 95 % −0.1929 a −0.0307). Duplicar la densidad se asocia a cerca de −7.5 % de inversión por habitante.

Esta asociación de la densidad ayuda a describir por qué Lima (322 hab/km²) y Callao (8,080 hab/km²) tienen cocientes bajos. Lima tiene la menor inversión por habitante de los 25 departamentos (794 S/), aunque concentra el 37.53 % de la inversión del gobierno nacional.

![Inversión por habitante según densidad y pobreza](../figuras/densidad_inversion.png)

*Figura 6. Inversión 2020–2024 por habitante según densidad y pobreza. Fuentes: BCRP (series RD); INEI, ENAHO 2024; superficie del geojson (`figuras/densidad_inversion.png`).*

### Complemento: minería

- **Correlación:** la correlación de Spearman entre el cociente inversión/pobres y la parte de las exportaciones mineras 2018–2022 es de **0.20** en 25 departamentos (`salidas/analisis.txt`; series `RD40961BA`–`RD41369BA`). Es una asociación débil.
- **Casos:** varios departamentos con cocientes altos tienen una parte minera alta, como Moquegua (8.49 % de las exportaciones mineras), Arequipa (14.61 %) y Áncash (13.00 %) (`salidas/indicadores.csv`). Otros con poca minería, como Madre de Dios (0.22 %), también tienen cocientes altos.
- Este análisis no permite atribuir la inversión a los ingresos mineros.

### Recuadro: Lima Metropolitana y Lima provincias

| Ámbito | Pobreza 2024 [IC 95 %] | % de los pobres del país | Inversión regional 2020–2024 |
|---|---|---|---|
| Lima Metropolitana (provincia de Lima) | 27.6 % [25.0–30.1] | 29.8 % | 455 millones S/ |
| Lima provincias (región Lima) | 21.7 % [18.3–25.1] | 2.3 % | 1,516 millones S/ |

Fuente: `salidas/recuadro_lima.csv`. El BCRP no separa la inversión del gobierno nacional ni la de los gobiernos locales entre las dos Limas, por eso el recuadro solo compara la inversión regional.

## 6. Interpretación

Entre 2020 y 2024, la inversión pública **no se repartió en proporción a dónde vive la población pobre**:

- **Más pobreza, menos inversión relativa:** los departamentos con más pobreza (Cajamarca, Loreto, Puno, Huánuco) recibieron una parte de la inversión cerca de un tercio menor que su parte de pobres.
- **Menos pobreza, más inversión relativa:** departamentos con poca pobreza (Moquegua, Ica, Madre de Dios) recibieron entre 5 y 7.5 veces su parte de pobres.
- **Más cerca de la población que de la pobreza:** en el agregado, el reparto se parece más al de la población que al de los pobres. Ningún nivel de gobierno concentra su inversión en los departamentos más pobres.

**Lima** pesa mucho en el resultado. Tiene casi un tercio de los pobres del país y recibe cerca de un quinto de la inversión, pero eso va junto con su alta densidad. Parte de la diferencia puede deberse a que un mismo monto atiende a más personas en zonas densas. Estos datos no permiten afirmarlo ni descartarlo.

**Lo que no se concluye:** los resultados describen una falta de proporcionalidad, no su causa. No dicen si la inversión redujo o no la pobreza, ni si el reparto es adecuado. Otros factores que no se miden aquí pueden explicar el reparto, como el canon, las transferencias, la capacidad de ejecución o los costos de construcción.

## 7. Limitaciones

1. **Soles corrientes.** La inversión no está deflactada: el +100.14 % del gobierno nacional mezcla volumen y precios. Las partes por departamento no dependen del deflactor si los precios suben por igual en todos.
2. **Desfase temporal.** Se compara la inversión acumulada 2020–2024 con la pobreza de un solo año, 2024. La pobreza también cambió en el periodo.
3. **Asignación territorial.** El BCRP asigna la inversión del gobierno nacional al departamento donde se registra. Los proyectos de alcance nacional pueden quedar en Lima, y la Municipalidad Metropolitana de Lima se asignó a Lima.
4. **Exportaciones mineras, cuadre incompleto.** `cuadre_territorial` informó que la suma de departamentos **no cuadra** con el total oficial (`PM40047BA`) en 2018, 2019, 2020 y 2022:
   - la diferencia sin explicar es de 5.74, 14.48, −4.01 y 101.95 millones US$, respectivamente;
   - en 2021 sí cuadra;
   - en 2020–2022 hay montos «sin ubigeo» (`RD41386BA`) de hasta 2,883 millones US$;
   - las series por departamento se actualizaron por última vez el 20-12-2024 y el BCRP las publica solo hasta 2022.

   Por eso el complemento minero es aproximado. Las cifras no se rellenaron ni se corrigieron.
5. **Pocas observaciones.** Con 25 departamentos, la regresión y la correlación son imprecisas. El coeficiente de la pobreza no es distinto de cero al 95 %.
6. **Error muestral.** Los IC solo reflejan el error de la ENAHO. Las cifras del BCRP se tratan como exactas.
7. **Conteos.** No se reportan números absolutos de pobres, porque la base pública no reproduce los 9,395 mil que publica el INEI con proyecciones de población.

**Fallas de herramientas:** ninguna herramienta falló. El único problema que reportaron fue el cuadre incompleto de las exportaciones mineras, descrito en el punto 4.

## 8. Reproducibilidad

Los comandos se corren desde la raíz de `Tarea_4`, con el entorno `uv` del proyecto (`pyproject.toml`, `uv.lock`):

```bash
# 1. Datos del BCRP (servidor MCP bcrp, herramienta cuadre_territorial, guardar=True)
#    inversion_gobierno_nacional, inversion_gobiernos_regionales, inversion_gobiernos_locales: 2020–2024
#    exportaciones_mineras: 2018–2022
#    Resumen del gobierno nacional: resumen("RD16682DA", "2020", "2024")

# 2. ENAHO 2024: limpieza y validación
uv run .claude/skills/limpiando-enaho/scripts/limpiar.py --anio 2024

# 3. Gráfico y mapa
uv run .claude/skills/graficando-enaho/scripts/graficar.py --por departamento
uv run .claude/skills/mapeando-enaho/scripts/mapear.py

# 4. Cruce inversión–pobreza
uv run .claude/skills/analizando-reparto/scripts/analizar.py
```

**Salidas:**

| Tipo | Archivos |
|---|---|
| Validación | `salidas/validacion.txt`, `salidas/mapa_vs_referencia.csv` |
| Análisis | `salidas/analisis.txt`, `salidas/indicadores.csv`, `salidas/recuadro_lima.csv` |
| Datos del BCRP | `salidas/bcrp_*.csv`, con código de serie y URL de la API del BCRP en cada fila |
| Figuras | `figuras/*.png`, `mapas/pobreza_departamento.png` |

Los microdatos de la ENAHO (`datos/966-Modulo34.zip`, `datos/966-Modulo02.zip`) se bajan del portal de microdatos del INEI, como indica `README.md`.
