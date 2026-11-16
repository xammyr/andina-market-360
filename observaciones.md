# Observaciones de Interfaz de GitHub · Andina Market 360

## Ejemplo 3.2 · Examen de un Repositorio Público (5 pestañas esenciales)
| Pestaña | Función técnica observada | Aplicación en Andina Market 360 |
| :--- | :--- | :--- |
| **Code** | Navegación por el árbol de archivos, selector de ramas (`main`, `feature/*`), historial de commits y botón para clonar/descargar ZIP. | Permite ver `src/resumen.py`, `data/ventas.csv` y verificar que no existan credenciales. |
| **Issues** | Registro de tareas pendientes, errores (*bugs*) y solicitudes de funcionalidades con estados abierto/cerrado. | Servirá para reportar fallos de suma de ventas o solicitar nuevos gráficos por sede. |
| **Pull Requests** | Espacio de revisión colaborativa y propuesta de cambios con diff visual antes de integrar a `main`. | Canal obligatorio para validar mejoras de código y pruebas antes de publicar. |
| **Actions** | Plataforma de CI/CD que ejecuta flujos de trabajo automatizados definidos en `.github/workflows/`. | Ejecutará automáticamente `unittest` ante cada `push` para validar los cálculos. |
| **Settings** | Administración de colaboradores, ramas protegidas, GitHub Pages, secretos y permisos. | Configura el despliegue de la web en GitHub Pages y las reglas de protección de `main`. |

---

## Ejemplo 3.3 · Búsqueda de proyectos por tema
- **Filtro de búsqueda utilizado:** `topic:python sales dashboard`
- **Repositorios comparados:**
  1. `pallets/flask`: Alta actividad, licencias claras (BSD-3-Clause), pruebas exhaustivas y documentación detallada.
  2. Proyectos personales pequeños: Falta de suite de pruebas unitarias (`tests/`) o instrucciones de despliegue incompletas en el README.
- **Conclusión para Andina Market 360:** Mantener siempre pruebas reproducibles (`unittest`) y un manual claro de ejecución en local sin dependencias innecesarias.
