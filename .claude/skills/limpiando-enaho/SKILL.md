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
