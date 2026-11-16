# Ficha de Portafolio Profesional · Andina Market 360

## 1. Resumen Ejecutivo (Pitch del Proyecto)
Andina Market 360 es una solución integral y reproducible para la consolidación automatizada de operaciones comerciales multisede (Lima, Ica y Arequipa). Reemplaza la manipulación manual de hojas de cálculo por una arquitectura ágil de control de versiones con Git, procesamiento analítico en Python, pruebas automatizadas en CI/CD y despliegue web estático continuo en GitHub Pages.

---

## 2. Ficha Técnica del Proyecto
| Parámetro | Detalle |
| :--- | :--- |
| **Repositorio Oficial:** | [https://github.com/xammyr/andina-market-360](https://github.com/xammyr/andina-market-360) |
| **Dashboard en Vivo:** | [https://xammyr.github.io/andina-market-360/](https://xammyr.github.io/andina-market-360/) |
| **Versión Estable:** | `v1.0.0` (SemVer) |
| **Lenguajes y Tecnologías:** | Python 3, Git, GitHub Actions, HTML5, CSS3, JSON, Markdown |
| **Dataset Utilizado:** | 12 transacciones comerciales sintéticas (`data/ventas.csv`) |
| **Integridad de Datos:** | Verificación estricta `cantidad * precio_unitario == total` (100% cuadre) |

---

## 3. Resultados Comerciales Consolidados (Línea Base Enero 2026)
| Sede Operativa | Monto Facturado | Participación | Nivel de Rendimiento |
| :--- | :---: | :---: | :--- |
| **Sede Lima (Principal)** | S/ 814.00 | 44.1% | Líder comercial en ingresos y volumen |
| **Sede Ica** | S/ 555.00 | 30.1% | Segundo puesto con alta rotación en abarrotes |
| **Sede Arequipa** | S/ 476.00 | 25.8% | Estabilidad con ventas corporativas |
| **TOTAL CONSOLIDADO:** | **S/ 1,845.00** | **100.0%** | **12 operaciones verificadas sin discrepancias** |

---

## 4. Arquitectura y Flujo Técnico
```text
[data/ventas.csv] ──(lectura)──> [src/resumen.py] ──(valida)──> [tests/test_resumen.py]
                                         │
                                  (genera JSON)
                                         ▼
                            [docs/data/resumen.json]
                                         │
                                   (fetch web)
                                         ▼
                             [docs/index.html en Pages]
```

---

## 5. Competencias Profesionales Demostradas
1. **Control de Versiones Avanzado:** Gestión de ramas (`main`, `feature/*`), resolución de conflictos en 3 vías, uso de `git revert`, `git stash`, `git reflog` y `git cherry-pick`.
2. **Colaboración y Gobernanza:** Gestión de tareas mediante GitHub Issues y Projects Kanban, plantillas de contribución (`CONTRIBUTING.md`, plantillas de Issues/PR) y revisiones mediante Pull Requests.
3. **Automatización CI/CD:** Flujo de integración continua con GitHub Actions testeando en matriz Python (3.10 y 3.11) con despliegue automatizado en GitHub Pages.
4. **Seguridad y Auditoría:** Cero secretos en commits, alertas automáticas de Dependabot activas, política de seguridad `SECURITY.md` y copias de respaldo forense offline con `git bundle`.
