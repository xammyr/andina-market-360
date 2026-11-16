# Proyecto Andina Market 360

## Objetivo
Organizar y analizar las ventas de una empresa ficticia con sedes en Lima, Ica y Arequipa.

## 1. Definición del problema (Ejemplo 1.1)
- **Necesidad:** Consolidar las ventas y mostrar los resultados por sede sin editar informes manualmente.
- **Problema:** Las ventas se registran en hojas separadas y los informes se arman a mano, lo que demora la entrega y permite errores de suma.
- **Usuarios:** Gerencia comercial (decide), jefes de sede (revisan su sede) y analista de datos (ejecuta el programa y mantiene el repositorio).
- **Resultado esperado:** Un resumen automático por sede, calculado desde `data/ventas.csv` y mostrado en una página web.

### Preguntas que debe responder el proyecto
| Pregunta | Respuesta con los datos de prueba | Dónde se obtiene |
| :--- | :--- | :--- |
| ¿Qué sede lidera? | Lima, con S/ 814.00 (Ica S/ 555.00, Arequipa S/ 476.00) | `por_sede` en `docs/data/resumen.json` |
| ¿Qué producto vende más? | Por ingresos: Arroz Extra 5kg, S/ 220.00. Por unidades: Fideos Spaghetti 1kg, 25 unidades | Columnas `total` y `cantidad` de `data/ventas.csv` |
| ¿Cómo cambia el total mensual? | Con esta base no cambia: las 12 ventas son de enero de 2026 (del 05 al 16), S/ 1845.00 | Columna `fecha` de `data/ventas.csv` |

---

## 2. Herramientas (Ejemplo 1.2)
- **Git:** Registra versiones y cambios de archivos en la computadora.
- **GitHub:** Aloja el repositorio y permite revisar cambios con otras personas.
- **Python:** Ejecuta el programa que calcula las ventas.

### Flujo de trabajo
```text
archivo (editar) → Git local (commit) → GitHub remoto (push) → revisión del equipo (pull request)
```
1. Modifico archivos locales.
2. Git registra los cambios en un repositorio local.
3. Envío los cambios al repositorio remoto de GitHub, cuando lo configure.
4. Otras personas pueden revisar los cambios en una pull request.

**Comprobación:** Ningún paso depende de que GitHub ejecute el código de ventas. Python ejecuta el código localmente.

---

## 3. Inventario de archivos iniciales (Ejemplo 1.3)
Ver archivo `inventario.md`.

---

## 4. Estructura de trabajo (Ejemplo 1.4)
```text
andina-market-360/
├── README.md
├── proyecto.md
├── inventario.md
├── data/
│   └── ventas.csv
├── src/
│   └── resumen.py
├── tests/
│   └── test_resumen.py
├── docs/
│   ├── index.html
│   ├── style.css
│   ├── manual.md
│   └── data/resumen.json
├── evidencias/
└── .github/
    └── workflows/ci.yml
```

**Justificación:** El dashboard debe leer un JSON generado automáticamente por Python y no un CSV editado a mano para garantizar repetibilidad, trazabilidad y pruebas unitarias automáticas sin errores de tipeo humano.

---

## 5. Criterios de éxito (Ejemplo 1.5)
| Indicador | Meta | Responsable | Evidencia requerida |
| :--- | :--- | :--- | :--- |
| Ventas de prueba en `data/ventas.csv` | 12 | Analista de datos | Salida de `python src/resumen.py`: Resumen Andina Market 360 (12 operaciones) |
| Total de ventas calculado | S/ 1845.00 (Lima 814, Ica 555, Arequipa 476) | Analista de datos | Misma salida y `docs/data/resumen.json` |
| Pruebas locales | 4 pruebas correctas | Desarrollador/a | Salida de `python -m unittest discover -s tests -v` con OK |
| Resumen web | La página muestra los datos del JSON | Desarrollador/a | Captura de `http://localhost:8000` |
| Historial en Git | Al menos 1 commit del proyecto | Desarrollador/a | Salida de `git log --oneline -5` |
