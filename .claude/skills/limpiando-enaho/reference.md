# Referencia de la ENAHO 2024

Las etiquetas vienen de los metadatos de los propios archivos `.dta` del INEI.

## Archivos

| Zip | Archivo usado | Una fila por |
|---|---|---|
| `966-Modulo34.zip` | `sumaria-2024.dta` | hogar |
| `966-Modulo02.zip` | `enaho01-2024-200.dta` | persona |

El zip del módulo 34 también trae `sumaria-2024-12g.dta`, con más columnas. Da la misma pobreza nacional, pero no se usa.

## Variables de la base

| Variable | Etiqueta del INEI | Valores |
|---|---|---|
| `conglome`, `vivienda`, `hogar` | Llaves del hogar | Texto, con ceros a la izquierda |
| `codperso` | Llave de la persona dentro del hogar | Texto |
| `ubigeo` | Ubicación geográfica | Texto de 6 dígitos; los 2 primeros son el departamento |
| `dominio` | Dominio geográfico | `8` = Lima Metropolitana |
| `estrato` | Estrato geográfico | `1` a `5` = 2,000 habitantes o más; `6` a `8` = menos de 2,000 y áreas rurales |
| `pobreza` | Pobreza | `1` pobre extremo, `2` pobre no extremo, `3` no pobre |
| `factor07` | Factor de expansión anual, proyecciones CPV-2007 | Del hogar |
| `mieperho` | Total de miembros del hogar | Número |
| `facpob07` | Factor de expansión anual de población, proyecciones CPV-2007 | De la persona |
| `p203` | Parentesco con el jefe o jefa del hogar | Código |
| `p204` | ¿Es miembro del hogar? | `1` sí, `2` no |
| `p205` | ¿Se encuentra ausente del hogar 30 días o más? | `1` sí, `2` no |
| `p206` | ¿Está presente en el hogar 30 días o más? | `1` sí, `2` no |
| `p207` | Sexo | `1` hombre, `2` mujer |
| `p208a` | Edad en años cumplidos | Número |

Variables construidas: `departamento` (`ubigeo[:2]`), `urbano` (`estrato <= 5`), `pobre` (`pobreza <= 2`), `pobre_extremo` (`pobreza == 1`) y `anio`.

## Qué peso usar

| Corte | Peso | Por qué |
|---|---|---|
| Nacional, área, departamento | Hogares únicos con `factor07 × mieperho` | Reproduce las cifras de referencia de la clase, calculadas con la sumaria |
| Sexo, edad y otras características de la persona | `facpob07` | La característica es de la persona, no del hogar |

Con `facpob07`, la pobreza nacional da 27.53 % y la de los departamentos se aleja hasta 0.52 puntos de la referencia (Puno).
Con `factor07 × mieperho`, la nacional da 27.58 % y los departamentos se alejan como máximo 0.05 puntos.

## Trampas

- `pobreza` es un código: nunca se promedia.
- Las llaves pierden los ceros a la izquierda si se convierten a número.
- La columna del año llega como `aÑo`; por eso los nombres se normalizan antes de usarlos.
- Las cifras son estimaciones de encuesta sin intervalo de confianza: una diferencia pequeña entre dos grupos no basta para afirmar que son distintos.
- La ENAHO tiene más módulos. Si la pregunta pide una variable que no está en esta base, hay que avisarlo en vez de aproximarla.
