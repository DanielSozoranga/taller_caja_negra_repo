# taller_caja_negra_repo

## Desafío Lógico 1: 

**Pregunta:** Según lo investigado en ISTQB, ¿es posible que un Defecto (Bug) exista en el código fuente de presupuesto_analisis.py durante años sin llegar a causar nunca un Fallo (Failure)?

Sí, es posible. Un defecto puede permanecer inactivo en el código durante años, y solo se convertirá en un fallo visible si el usuario ingresa los datos exactos que obliguen al programa a ejecutar esa línea defectuosa en específico. Si esa ruta nunca se utiliza, el fallo jamás ocurrirá.  

## Desafío Lógico 2

**Pregunta:** Imaginen que corrigen todos los bugs y el script funciona perfecto, pero el cliente afirma que "necesitaba un sistema para calcular nóminas, no presupuestos". ¿Qué principio fundamental del testing de ISTQB se acaba de violar aunque el código esté limpio?


Se viola el principio de Validación esto quiere decir que el sistema pasa la Verificación lo que significa que funciona bien segun lo que se solicito construir pero el problema esta en la Validación porque no resuelve lo que el cliente realmente necesitaba.

## STLC vs SDLC

El SDLC es conocido como el ciclo de vida del desarrollo del software, mientras que el STLC corre en paralelo lo cual valida cada etapa del SDLC desde la perspectiva de testing.

## Shift-Left Testing aplicado en este proyecto

En este taller aplicamos Shift-Left Testing al automatizar las pruebas con PyTest y GitHub Actions por ende en vez de probar manualmente se puede decir que antes de entregar, las pruebas corren automáticamente en cada push, detectando errores lo antes posible en el desarrollo y haciendo el proceco automatico.