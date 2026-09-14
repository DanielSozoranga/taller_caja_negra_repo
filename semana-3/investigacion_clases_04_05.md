# Investigacion Teorica - Clases 04 y 05

## Actividad 1: Taxonomia de Niveles de Prueba

| Nivel | Objeto de Prueba | Base de Prueba | Defectos Tipicos Buscados | Rol Responsable | Entorno de Ejecucion |
|---|---|---|---|---|---|
| Pruebas Unitarias | Componentes o modulos individuales aislados | Diseño detallado y codigo fuente del componente | Errores logicos internos, calculos incorrectos, rutas no ejecutadas | Desarrollador | IDE local, con mocks/stubs de dependencias |
| Pruebas de Integracion | Interfaces y flujo de datos entre componentes | Arquitectura de software, especificacion de interfaces (APIs) | Incompatibilidad de interfaces, perdida de datos entre modulos | Integrador / Desarrollador Senior | Entorno de integracion continua (CI) |
| Pruebas de Sistema | El sistema completo end-to-end | Especificacion de requisitos (SRS), casos de uso | Fallos funcionales completos, defectos no funcionales (rendimiento, seguridad) | Equipo de QA independiente | Entorno de staging/QA |
| Pruebas de Aceptacion (UAT) | El sistema desde la optica del negocio/usuario | Requisitos de negocio, criterios de aceptacion | Desalineacion entre lo construido y la necesidad real | Cliente / Product Owner | Entorno de aceptacion (UAT) |

Diferencia Component vs System Integration Testing: Component Integration Testing prueba modulos dentro de una misma aplicacion, controlados por el mismo equipo. System Integration Testing prueba sistemas completos e independientes, por ejemplo tu app con una pasarela de pago externa, con latencia real y contratos de API que no controlas.

## Actividad 2: Estrategias de Integracion y Analisis V&V

Por que Big-Bang es antipatron, 3 razones:
1. Dificulta localizar defectos: si falla todo el sistema en conjunto, no se sabe con exactitud que componente lo causo.
2. Se detecta defectos de interfaz muy tarde, por ende a la hora de corregirlos cuesta mas.
3. Bloquea el testing hasta que todos los modulos esten listos, sin feedback incremental.

V&V: Prueba de Sistema es Verificacion, hace la preguntad de si se construyo segun las especificaciones (ejemplo: el score se calcula igual que en el documento tecnico). Prueba de Aceptacion es Validacion, pregunta si es lo que el usuario necesita (ejemplo: el banco decide si el sistema le resuelve el problema real, aunque cumpla la especificacion al 100%).

| Estrategia | Ventajas | Desventajas | Usa |
|---|---|---|---|
| Top-Down | Muestra un esqueleto funcional temprano | Los modulos criticos de bajo nivel se prueban al final | Stubs |
| Bottom-Up | Pone prioridad a la logica critica de bajo nivel  | No se puede mostrar el sistema completo hasta el final | Drivers |
| Sandwich | Hace una combinacion de ambas y  reduce el tiempo total | Requiere mas coordinacion ya que usa Stubs y Drivers a la vez | Ambos |

## Actividad 3: Matematicas de la Particion de Equivalencia

En vez de probar cada valor posible uno por uno, se agrupan en bloques donde todos se comportan igual. A esto se le llama relacion de equivalencia, y segun Jorgensen cumple 3 reglas: un valor se relaciona consigo mismo, si A se relaciona con B entonces B se relaciona con A, y si A se relaciona con B y B con C entonces A se relaciona con C. Con eso se puede probar un solo valor de cada grupo en vez de todos.

Clase valida: grupo de valores que el sistema debe aceptar (ejemplo: edad de 18 a 75). Clase invalida: grupo de valores que debe rechazar (ejemplo: edad de 10 o de 90). Cada grupo necesita su propia prueba.

Enmascaramiento de fallos: no se deben probar dos datos invalidos juntos en un mismo caso, porque si el sistema rechaza la prueba no se sabe cual de los dos causo el rechazo.

$$ Cobertura = \frac{\text{Numero de Particiones de Equivalencia Cubiertas}}{\text{Numero Total de Particiones de Equivalencia Identificadas}} \times 100 $$

## Actividad 4: Ingenieria de Especificaciones (Caso Bancario)

Para el caso bancario se utiliza un sistema de aprobacion de creditos, con 4 datos de entrada. Para cada uno se define que rango es valido y cuales son invalidos:

| Variable | Valida | Invalida baja | Invalida alta |
|---|---|---|---|
| Edad | 18 a 75 | menor a 18 | mayor a 75 |
| Ingreso neto | 500 a 10000 dolares | menor a 500 | mayor a 10000 |
| Scoring | 300 a 850 | menor a 300 | mayor a 850 |
| DTI | 0% a 40% | no aplica | mayor a 40% |

Dado un solo caso "todo valido" se cubren las 4 clases validas a la vez. Despues, un caso por cada clase invalida (una por vez, sin mezclar, por el enmascaramiento de fallos de la Actividad 3). En total dan 8 casos los cuales no se repite ninguno:

| ID | Edad | Ingreso | Scoring | DTI | Esperado |
|---|---|---|---|---|---|
| CP-01 | 35 | 5000 | 600 | 25% | Aprobado |
| CP-02 | 17 | 5000 | 600 | 25% | Rechazado, edad baja |
| CP-03 | 80 | 5000 | 600 | 25% | Rechazado, edad alta |
| CP-04 | 35 | 400 | 600 | 25% | Rechazado, ingreso bajo |
| CP-05 | 35 | 15000 | 600 | 25% | Rechazado, ingreso alto |
| CP-06 | 35 | 5000 | 250 | 25% | Rechazado, scoring bajo |
| CP-07 | 35 | 5000 | 900 | 25% | Rechazado, scoring alto |
| CP-08 | 35 | 5000 | 600 | 50% | Rechazado, DTI alto |