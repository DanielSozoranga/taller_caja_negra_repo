# Investigacion Teorica - Clases 04 y 05

## Actividad 1: Taxonomia de Niveles de Prueba

| Nivel | Objeto de Prueba | Base de Prueba | Defectos Tipicos Buscados | Rol Responsable | Entorno de Ejecucion |
|---|---|---|---|---|---|
| Pruebas Unitarias | Componentes o modulos individuales aislados | Diseño detallado y codigo fuente del componente | Errores logicos internos, calculos incorrectos, rutas no ejecutadas | Desarrollador | IDE local, con mocks/stubs de dependencias |
| Pruebas de Integracion | Interfaces y flujo de datos entre componentes | Arquitectura de software, especificacion de interfaces (APIs) | Incompatibilidad de interfaces, perdida de datos entre modulos | Integrador / Desarrollador Senior | Entorno de integracion continua (CI) |
| Pruebas de Sistema | El sistema completo end-to-end | Especificacion de requisitos (SRS), casos de uso | Fallos funcionales completos, defectos no funcionales (rendimiento, seguridad) | Equipo de QA independiente | Entorno de staging/QA |
| Pruebas de Aceptacion (UAT) | El sistema desde la optica del negocio/usuario | Requisitos de negocio, criterios de aceptacion | Desalineacion entre lo construido y la necesidad real | Cliente / Product Owner | Entorno de aceptacion (UAT) |

Diferencia Component vs System Integration Testing: Component Integration Testing prueba modulos dentro de una misma aplicacion, controlados por el mismo equipo. System Integration Testing prueba sistemas completos e independientes, por ejemplo tu app con una pasarela de pago externa, con latencia real y contratos de API que no controlas.
