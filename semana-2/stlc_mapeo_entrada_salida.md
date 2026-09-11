# Mapeo del Proyecto al STLC (ISTQB / ISO 29119) y Criterios de Entrada y Salida

## Fases del STLC aplicadas al proyecto

| Fase STLC (ISTQB / ISO 29119) | Tarea realizada en este proyecto |
|---|---|
| 1. Análisis de requisitos | Revisión de `presupuesto_analisis.py` entregado por el profesor: qué recibe (presupuesto, socios, meses) y qué debe calcular (interés, total, cuota por socio). |
| 2. Planificación de pruebas | Se definió la estrategia de caja negra: partición de equivalencia y valores límite sobre `presupuesto`, `socios` y `meses` (cero, negativos). |
| 3. Análisis y diseño de casos de prueba | Se diseñaron los casos CP-01 (socios en cero), CP-02 (meses negativos) y CP-03 (socios negativos) en `casos_prueba.md`. |
| 4. Configuración del entorno de pruebas | Se extrajo la lógica de cálculo a una función pura, `calcular()`, para poder probarla sin simular teclado. Se configuró PyTest y un runner de GitHub Actions (Ubuntu + Python 3.11). |
| 5. Ejecución de las pruebas | Los 3 casos manuales, más un caso de control con datos válidos, se automatizaron en `test_presupuesto.py` y corren con `pytest`, tanto en local como en cada `push` mediante `.github/workflows/ci_pipeline.yml`. |
| 6. Cierre del ciclo de pruebas | Se documentaron los defectos con su línea y causa raíz en `casos_prueba.md`, y se dejó evidencia reproducible mediante el check de GitHub Actions. |

## Criterios de Entrada

1. **El código bajo prueba está disponible y es importable.** `presupuesto_analisis.py` expone la función `calcular(presupuesto, socios, meses)`, independiente de `input()`, lo que permite invocarla directamente desde las pruebas automatizadas sin simular teclado.
2. **El entorno de ejecución está definido.** El workflow de GitHub Actions instala Python 3.11 y PyTest en una máquina limpia, garantizando que las pruebas corran en las mismas condiciones sin importar quién haga el `push`.

## Criterios de Salida

1. **Todos los casos de prueba planificados fueron ejecutados y quedaron documentados**, con su línea de código y causa raíz identificada, sin importar si el resultado fue correcto o no.
2. **El pipeline de integración continua corre de forma automática y reproducible**: cada `push` dispara `ci_pipeline.yml`, que instala dependencias y ejecuta `pytest`, dejando un check verde o rojo visible en la pestaña Actions, sin intervención manual.

**Nota metodológica:** el criterio de salida nunca fue "que todas las pruebas pasen", fue "que todas se hayan ejecutado y documentado". Esto es consistente con el primer principio de ISTQB: *el testing muestra la presencia de defectos, no su ausencia.*
