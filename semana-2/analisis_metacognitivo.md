# Análisis Metacognitivo: 3 Preguntas de Cierre

## 1. ¿Por qué correr las pruebas en la nube (GitHub Actions) y no solo en local?

Correr las pruebas únicamente en la máquina local depende de que una persona se acuerde de hacerlo, y de que su computadora tenga exactamente el mismo entorno (versión de Python, dependencias) que se usará después: el clásico "en mi máquina funciona". Ejecutarlas en la nube resuelve ambos problemas: (1) el entorno se reconstruye desde cero en cada corrida, sobre una máquina limpia con Python 3.11, así que el resultado es reproducible sin importar quién suba el código; y (2) la ejecución no depende de que nadie se acuerde de correr nada: se dispara sola con cada `push`, y el resultado queda como evidencia pública, verificable por cualquiera del equipo.

## 2. ¿Qué significa técnicamente que el pipeline esté en "luz verde"?

Significa que `ci_pipeline.yml` terminó sin errores en todos sus pasos, y en particular que `pytest` finalizó con código de salida 0: ninguna de las 4 pruebas lanzó una excepción no esperada ni falló ningún `assert`. No significa que el sistema esté libre de bugs: significa que los casos que se escribieron y corrieron se comportaron como se esperaba. Esto conecta con el primer principio de ISTQB: el testing muestra la presencia de defectos, no su ausencia; un defecto en una ruta nunca probada puede seguir ahí sin que la luz verde lo delate.

## 3. Si nos presionan: "¿por qué cierran esta fase si hubo casos de prueba fallidos?": Criterios de Salida bajo presión

Porque el Criterio de Salida de esta fase nunca fue "que todos los casos pasen", fue "que todos los casos planificados se hayan ejecutado y quedado documentados, con su causa raíz identificada". Un caso en estado *fallido* (como CP-01, CP-02 y CP-03 al probar el código original entregado por el profesor) no es una fase incompleta: es exactamente el resultado esperado de un proceso de testing que funciona bien, porque confirma defectos reales, medibles y ya localizados en el código. Cerrar la fase de testing no es lo mismo que cerrar el proyecto de desarrollo: la fase termina cuando se generó evidencia confiable del estado del sistema, y esa evidencia (incluidos los fallos) es lo que se entrega como insumo para la siguiente iteración.
