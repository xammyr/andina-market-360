# Registro de Evidencias · Capítulo 01
**Caso:** Andina Market 360 (datos ficticios)  
**Fecha:** 15/11/2026  

---

## Ejemplos Guiados Desarrollados

### CAP01_E01 · Definir el problema empresarial
- **Archivo/comando:** `proyecto.md`, sección 1.
- **Resultado observado:** Necesidad, problema, usuarios y resultado esperado registrados en líneas separadas, junto con 3 preguntas de negocio y su fuente de datos.
- **Fecha:** 15/11/2026

### CAP01_E02 · Distinguir Git de GitHub
- **Archivo/comando:** `proyecto.md`, sección 2.
- **Resultado observado:** Git conserva versiones en la computadora local; GitHub aloja y permite revisar cambios remotamente. Flujo: `archivo → Git local → GitHub remoto → revisión del equipo`. Ningún paso requiere que GitHub ejecute el script de ventas.
- **Fecha:** 15/11/2026

### CAP01_E03 · Inventariar los archivos iniciales
- **Archivo/comando:** `inventario.md`; comprobación de seguridad con búsqueda de palabras clave (`password`, `token`, `secret`, `api_key`).
- **Resultado observado:** El CSV cuenta con las 7 columnas requeridas y las 12 filas cuadran exactamente (`cantidad * precio_unitario == total`). Cero secretos ni datos reales encontrados.
- **Fecha:** 15/11/2026

### CAP01_E04 · Diseñar una estructura de trabajo
- **Archivo/comando:** `proyecto.md`, sección 4.
- **Resultado observado:** Estructura modular (`data/`, `src/`, `tests/`, `docs/`, `.github/`, `evidencias/`) justificada para procesamiento desatendido y visualización estática vía JSON.
- **Fecha:** 15/11/2026

### CAP01_E05 · Establecer un objetivo medible
- **Archivo/comando:** `python -m unittest discover -s tests -v` y `python src/resumen.py`
- **Resultado observado:**
  ```text
  Ran 4 tests in 0.002s - OK
  Resumen Andina Market 360 (12 operaciones):
    - Lima: S/ 814.00
    - Ica: S/ 555.00
    - Arequipa: S/ 476.00
    TOTAL: S/ 1845.00
  ```
- **Fecha:** 15/11/2026

---

## Ejercicios Propuestos (Retos)

### Reto 1.1 · Nueva pregunta comercial
- **Resultado obtenido:** ¿Cuál es el ticket promedio por sede? 
  - Lima: S/ 203.50 (S/ 814 / 4)
  - Ica: S/ 138.75 (S/ 555 / 4)
  - Arequipa: S/ 119.00 (S/ 476 / 4)
- **Cómo lo comprobé:** Cálculo en Python dividiendo el total por sede entre el conteo de ventas de cada sede en `data/ventas.csv`.

### Reto 1.2 · Mapa de tres roles del proyecto
| Rol | Responsabilidad principal | Evidencia de revisión |
| :--- | :--- | :--- |
| **Analista de datos** | Mantiene `data/ventas.csv` y valida que los datos sean 100% ficticios | Ficha de validación del CSV (conteo de filas y sumas) |
| **Desarrollador/a** | Mantiene `src/` y `tests/`; ejecuta suite de pruebas | Salida de terminal de unittest con `OK` |
| **Revisor/a** | Evalúa cambios mediante Pull Request o revisión cruzada | Aprobación de Pull Request o checklist firmado |

### Reto 1.3 · Clasificación de cinco acciones cotidianas
| Acción cotidiana | Dónde ocurre | Cómo se comprueba |
| :--- | :--- | :--- |
| Guardar una versión de `proyecto.md` | Git local | `git log --oneline` |
| Comparar cambios antes de confirmarlos | Git local | `git diff` |
| Revisar cambios de un compañero en un Pull Request | Plataforma GitHub | Pestaña *Pull requests* en GitHub |
| Publicar la página del proyecto | Plataforma GitHub (GitHub Pages) | URL del sitio en `github.io` |
| Calcular el resumen de ventas | Herramienta externa (Python) | `python src/resumen.py` |

---

## Control de Salida del Capítulo 01
| Verificación final | Estado |
| :--- | :---: |
| Realicé los cinco ejemplos y verifiqué los resultados | [x] Sí |
| Resolví los tres retos sin copiar el caso resuelto | [x] Sí |
| Guardé evidencias sin secretos ni datos reales | [x] Sí |
| Identifiqué una mejora para el capítulo siguiente | [x] Sí |

- **Mejora sugerida para el Capítulo 02:** Configurar la cuenta de GitHub con autenticación en dos pasos (2FA) y preparar el perfil profesional sin exponer datos personales.
