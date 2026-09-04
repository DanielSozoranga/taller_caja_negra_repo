# Casos de Prueba — Sistema de Análisis de Presupuesto

## Mapa Conceptual

- **Error**: el programador se equivoca (no pensó en que `socios` podía ser 0).
- **Defecto (bug)**: la línea de código queda mal (falta validar `socios`).
- **Fallo**: el programa se cae o da un resultado incorrecto cuando se ejecuta esa línea.

**QA vs QC vs Testing:**
- QA = prevenir (mejorar el proceso para que hayan menos bugs).
- QC = revisar el producto ya hecho para encontrar bugs.
- Testing = las pruebas concretas que se corren dentro de QC.

**7 principios de ISTQB (resumen corto):**
1. El testing encuentra bugs, no prueba que no existan.
2. No se puede probar todo, es imposible.
3. Mientras antes se prueba, menos cuesta arreglar.
4. Los bugs se agrupan en las mismas partes del código.
5. Si repites las mismas pruebas, dejan de encontrar bugs nuevos.
6. Cada sistema se prueba distinto según su contexto.
7. Que no haya bugs no significa que el programa sirva para lo que el usuario necesita.

---

## Tabla de Casos de Prueba

| ID | Descripción | Entrada | Esperado | Real | Estado |
|----|---|---|---|---|---|
| CP-01 | Presupuesto negativo | presupuesto=-1000, socios=2, meses=3 | Debería rechazar el valor | Lo acepta y calcula todo negativo | Failed |
| CP-02 | Socios en 0 | presupuesto=1000, socios=0, meses=3 | Debería mostrar un aviso, sin cerrarse | ZeroDivisionError, el programa se cierra | Failed |
| CP-03 | Meses = 2 | presupuesto=1000, socios=2, meses=2 | Interés esperado: $40.00 | Interés real: $80.00 | Failed |

---

## Defectos encontrados

**CP-01 — línea 4:** `presupuesto = float(input(...))` no valida que sea positivo. Por eso deja pasar números negativos sin avisar.

**CP-02 — línea 5 y 13:** `socios = int(input(...))` no valida que sea mayor a 0. Cuando `socios=0`, la línea 13 (`total / socios`) revienta con ZeroDivisionError.

**CP-03 — línea 10:** `intereses = presupuesto * tasa_interes_mensual * (meses ** 2)` usa `meses` al cuadrado en vez de usarlo normal. Por eso el interés sale más alto de lo que debería.

---

**Validado por:** Daniel Sozoranga — Tester Principal
**Ejecutado y diagnosticado por:** Ricardo Alvarez — Desarrollador/Analista