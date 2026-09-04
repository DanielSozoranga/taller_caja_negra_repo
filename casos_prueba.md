Casos de Prueba - Sistema de Analisis de Presupuesto

Mapa Conceptual

Error: el programador se equivoco, no penso en que socios podia ser 0.
Defecto (bug): la linea de codigo queda mal, falta validar socios.
Fallo: el programa se cae o da un resultado incorrecto cuando se ejecuta esa linea.

QA vs QC vs Testing:
QA es prevenir, mejorar el proceso para que hayan menos bugs.
QC es revisar el producto ya hecho para encontrar bugs.
Testing son las pruebas concretas que se corren dentro de QC.

7 principios de ISTQB, resumen corto:
1. El testing encuentra bugs, no prueba que no existan.
2. No se puede probar todo, es imposible.
3. Mientras antes se prueba, menos cuesta arreglar.
4. Los bugs se agrupan en las mismas partes del codigo.
5. Si repites las mismas pruebas, dejan de encontrar bugs nuevos.
6. Cada sistema se prueba distinto segun su contexto.
7. Que no haya bugs no significa que el programa sirva para lo que el usuario necesita.

Tabla de Casos de Prueba

CP-01: Presupuesto negativo
Entrada: presupuesto=-1000, socios=2, meses=3
Esperado: deberia rechazar el valor
Real: lo acepta y calcula todo negativo
Estado: Failed

CP-02: Socios en 0
Entrada: presupuesto=1000, socios=0, meses=3
Esperado: deberia mostrar un aviso, sin cerrarse
Real: ZeroDivisionError, el programa se cierra
Estado: Failed

CP-03: Meses = 2
Entrada: presupuesto=1000, socios=2, meses=2
Esperado: interes de $40.00
Real: interes de $80.00
Estado: Failed

Defectos encontrados

CP-01, linea 4: presupuesto = float(input(...)) no valida que sea positivo. Deja pasar numeros negativos sin avisar.

CP-02, linea 5 y 13: socios = int(input(...)) no valida que sea mayor a 0. Cuando socios es 0, la linea 13 (total / socios) revienta con ZeroDivisionError.

CP-03, linea 10: intereses = presupuesto * tasa_interes_mensual * (meses ** 2) usa meses al cuadrado en vez de usarlo normal. Por eso el interes sale mas alto de lo que deberia.

Validado por: Daniel Sozoranga, Tester Principal
Ejecutado y diagnosticado por: Ricardo Alvarez, Desarrollador/Analista