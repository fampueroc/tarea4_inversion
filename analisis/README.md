# Borradores de exploración (no forman parte del flujo final)

Estos tres scripts son **borradores** de los primeros días del proyecto (5-nov-2026). Sirvieron para revisar con la autora los primeros números y decidir el enfoque **antes** de escribir la versión final. Se conservan solo como evidencia del proceso.

**La versión final y validada está en la skill [`analizando-reparto`](../.claude/skills/analizando-reparto/scripts/analizar.py)**: es la que usa el agente y la que produce todas las cifras del informe. No hace falta correr estos borradores para reproducir nada.

| Borrador | Para qué sirvió | Qué pasó después |
|---|---|---|
| `explorar_primeros_numeros.py` | Primer cruce: parte de la inversión frente a parte de los pobres, curva de concentración | Se descartó la correlación entre % de inversión y % de pobres (0.89), porque salía alta solo por el tamaño de Lima. Se agregó la comparación con la población total |
| `explorar_densidad.py` | Separar Lima Metropolitana de Lima provincias y explorar la densidad poblacional, a pedido de la autora | Se decidió tratar Lima como un departamento con un recuadro aparte, y se incorporó la densidad como hallazgo 3 |
| `validar_ic.py` | Comprobar que el método de errores estándar reproduce los intervalos oficiales del INEI | La misma validación quedó dentro de `analizar.py`, que se detiene si no se cumple |

Algunas cifras de estos borradores, como la correlación de 0.89, **no se usan en el informe** precisamente porque se revisaron y descartaron.
