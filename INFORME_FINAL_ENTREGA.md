# INFORME CONSOLIDADO DE PRÁCTICAS · GIT Y GITHUB
## CASO EMPRESARIAL: ANDINA MARKET 360 (36 CAPÍTULOS COMPLETOS)

---

### DATOS GENERALES DE ENTREGA
- **Estudiante / Usuario de GitHub:** [xammyr](https://github.com/xammyr)
- **Repositorio Oficial del Proyecto:** [https://github.com/xammyr/andina-market-360](https://github.com/xammyr/andina-market-360)
- **Sitio Web en Vivo (GitHub Pages):** [https://xammyr.github.io/andina-market-360/](https://xammyr.github.io/andina-market-360/)
- **Versión Oficial Publicada:** `v1.0.0` (Lanzamiento inicial en Releases)
- **Fecha de Cierre:** 16 de noviembre de 2026
- **Total de Evidencias y Capturas:** 35 capturas archivadas en `evidencias/capturas/`

---

## 1. RESUMEN DEL CASO EMPRESARIAL
Andina Market 360 es una empresa comercial con sedes en **Lima**, **Ica** y **Arequipa**. El proyecto reemplazó la consolidación manual de hojas de cálculo por una arquitectura moderna de software con:
1. **Control de Versiones (Git y GitHub):** Historial atómico, flujo de ramas, resolución de conflictos y revisiones formales con Pull Requests.
2. **Procesamiento de Datos:** Script Python sin librerías externas (`src/resumen.py`) que lee 12 transacciones ficticias (`data/ventas.csv`) y genera un archivo estructurado `docs/data/resumen.json`.
3. **Calidad y Automatización (CI/CD):** 4 pruebas unitarias locales en `tests/test_resumen.py` y pipeline automático en GitHub Actions bajo matriz de Python 3.10 y 3.11.
4. **Publicación Continua:** Dashboard web estático accesible públicamente en GitHub Pages.

---

## 2. RESULTADOS COMERCIALES OBTENIDOS (LÍNEA BASE)
| Sede Operativa | Monto Facturado | Participación | Nivel de Rendimiento |
| :--- | :---: | :---: | :--- |
| **Lima (Principal)** | S/ 814.00 | 44.1% | Líder en ingresos y volumen comercial |
| **Ica** | S/ 555.00 | 30.1% | Alto dinamismo en ventas minoristas |
| **Arequipa** | S/ 476.00 | 25.8% | Estabilidad con operaciones corporativas |
| **TOTAL CONSOLIDADO** | **S/ 1,845.00** | **100.0%** | **12 operaciones verificadas al 100%** |

*Comprobación de cuadre:* `cantidad * precio_unitario == total` verificado en las 12 filas del CSV.

---

## 3. REGISTRO MAESTRO DE EVIDENCIAS (ANEXO A)
*Control de avance real de las 36 sesiones del cuaderno:*

| Cap. | Tema Central | 5 Ejemplos | 3 Retos | Evidencia Principal |
| :---: | :--- | :---: | :---: | :--- |
| **01** | Introducción a GitHub | [x] | [x] | `proyecto.md`, `inventario.md` y `CAP01_E05.png` |
| **02** | Creación y configuración de una cuenta | [x] | [x] | `perfil.md`, `perfil_publico.md` y `CAP02_E01.png` |
| **03** | Conociendo la interfaz de GitHub | [x] | [x] | `observaciones.md`, `seguimiento.md` y fichas |
| **04** | Creación y administración de repositorios | [x] | [x] | Repositorio remoto creado (`CAP04_E01.png`), `README.md`, `.gitignore` |
| **05** | Fundamentos del control de versiones | [x] | [x] | Bitácora de 3 espacios de Git y trazabilidad |
| **06** | Instalación y configuración de Git | [x] | [x] | `git init -b main`, config local y primer commit (`CAP06_E04.png`) |
| **07** | Comandos fundamentales de Git | [x] | [x] | `git status`, `git diff` y commit (`CAP07_E01.png`, `CAP07_E03.png`) |
| **08** | Trabajo con ramas o branches | [x] | [x] | `feature/resumen-sedes`, merge y delete (`CAP08_E01.png`, `CAP08_E03.png`) |
| **09** | Sincronización con repositorios remotos | [x] | [x] | `git remote add origin` y `git push` (`CAP09_E03.png`, `CAP09_E04.png`) |
| **10** | Resolución de conflictos e historial | [x] | [x] | Conflicto A/B resuelto, revert, stash y reflog (`CAP10_E01.png` al `E05`) |
| **11** | GitHub Desktop y Visual Studio Code | [x] | [x] | Inspección visual en Source Control de VS Code (`CAP11_E04.png`) |
| **12** | Documentación con Markdown | [x] | [x] | `docs/manual.md`, `CONTRIBUTING.md` (`CAP12_E04.png`) |
| **13** | Gestión de tareas con Issues y Projects | [x] | [x] | Issues #1 y #2, y Tablero Kanban en Projects (`CAP13_E01.png`, `CAP13_E04.png`) |
| **14** | Pull Requests y colaboración | [x] | [x] | Rama `feature/ficha-sedes`, PR abierto y Merged (`CAP14_E02.png`, `CAP14_E05.png`) |
| **15** | Revisión profesional de código | [x] | [x] | Evaluación de diff, pruebas unitarias y checklist de calidad |
| **16** | Participación en proyectos de código abierto | [x] | [x] | Guía de contribución responsable y compromiso ético |
| **17** | Administración de repositorios | [x] | [x] | Reglas de protección, plantillas `.github/` y `CODEOWNERS` |
| **18** | Versiones, etiquetas y lanzamientos | [x] | [x] | Tag `v1.0.0` y Release publicada en GitHub (`CAP18_E02.png`, `CAP18_E04.png`) |
| **19** | Publicación de sitios con GitHub Pages | [x] | [x] | Configuración en `/docs` y web publicada (`CAP19_E01.png`, `CAP19_E04.png`) |
| **20** | Gestión de archivos y paquetes | [x] | [x] | Exclusiones en `.gitignore` y empaquetado seguro |
| **21** | Introducción a GitHub Actions | [x] | [x] | Workflow `.github/workflows/ci.yml` ejecutado (`CAP21_E04.png`) |
| **22** | Integración continua (CI) | [x] | [x] | Ejecución automática de unittest ante cada push con check verde |
| **23** | Entrega y despliegue continuos (CD) | [x] | [x] | Generación de JSON y actualización automática en Pages |
| **24** | Automatización avanzada | [x] | [x] | Matriz de pruebas en Python 3.10 y 3.11 (`CAP24_E03.png`) |
| **25** | Seguridad de cuentas y autenticación | [x] | [x] | Higiene de credenciales, 2FA y cero secretos en Git |
| **26** | Seguridad del código y dependencias | [x] | [x] | `SECURITY.md`, escaneo de Dependabot y PRs automáticos (`CAP26_E02.png`) |
| **27** | Reglas, auditoría y calidad | [x] | [x] | Respaldo forense local con `git bundle create` (`CAP27_E04.png`) |
| **28** | GitHub Organizations y equipos | [x] | [x] | Gobernanza de equipos: Datos, Calidad y Web |
| **29** | GitHub CLI | [x] | [x] | Equivalencias de comandos `gh` con la interfaz web |
| **30** | GitHub Codespaces | [x] | [x] | Entorno reproducible en contenedor `.devcontainer/` (`CAP30_E01.png`) |
| **31** | APIs, webhooks e integraciones | [x] | [x] | Consumo de API REST pública de GitHub y lectura JSON |
| **32** | GitHub Copilot e IA | [x] | [x] | Política de uso ético y validación humana obligatoria |
| **33** | Git y GitHub a nivel avanzado | [x] | [x] | Aplicación de `git cherry-pick` entre ramas (`CAP33_E02.png`) |
| **34** | Solución de problemas frecuentes | [x] | [x] | Diagnóstico de rutas, detached HEAD y conflictos |
| **35** | Portafolio profesional en GitHub | [x] | [x] | Documento de presentación profesional `portfolio.md` (`CAP35_E01.png`) |
| **36** | Proyecto integrador final | [x] | [x] | Sustentación técnica, ejecución integral OK (`CAP36_E03.png`) |

---

## 4. EVALUACIÓN SEGÚN LA RÚBRICA DE 100 PUNTOS (ANEXO B)

| Criterio Evaluado | Puntaje Máximo | Puntaje Logrado | Comprobación y Evidencia |
| :--- | :---: | :---: | :--- |
| **1. Repositorio y control de versiones** | 20 pts | **20 pts** | Commits atómicos con convención (`feat:`, `docs:`, `fix:`, `chore:`), ramas aisladas, merge, cherry-pick y tag oficial `v1.0.0`. |
| **2. Procesamiento de datos** | 20 pts | **20 pts** | Dataset comercial de 12 transacciones exactas en `data/ventas.csv` y script `src/resumen.py` que calcula S/ 1,845.00 sin errores. |
| **3. Pruebas y automatización** | 20 pts | **20 pts** | Suite de 4 pruebas unitarias aprobadas al 100% y CI ejecutando matriz de Python 3.10 y 3.11 en GitHub Actions. |
| **4. Publicación y documentación** | 15 pts | **15 pts** | README estructurado, manual operativo, CHANGELOG y sitio web publicado en vivo en GitHub Pages. |
| **5. Colaboración y trazabilidad** | 10 pts | **10 pts** | Issues documentados (#1 y #2), tablero Kanban en Projects y Pull Request formal con checklist de revisión y merge. |
| **6. Seguridad y uso responsable** | 10 pts | **10 pts** | Cero tokens ni contraseñas en Git, exclusiones en `.gitignore`, `SECURITY.md` y escaneos de Dependabot. |
| **7. Sustentación y evidencias** | 5 pts | **5 pts** | Registro de 35 capturas de pantalla organizadas con nomenclatura estándar en `evidencias/capturas/`. |
| **TOTAL** | **100 pts** | **100 / 100** | **PROYECTO COMPLETO Y DEFENDIBLE** |

---

## 5. CHECKLIST FINAL DE ENTREGA (ANEXO C)
- [x] No hay contraseñas, tokens, claves privadas ni datos de personas reales.
- [x] El CSV contiene exclusivamente datos sintéticos de práctica.
- [x] Todos los cambios responden a necesidades e Issues registrados.
- [x] Las pruebas unitarias se ejecutaron con resultado `OK` en local y en la nube.
- [x] El repositorio remoto está sincronizado con la rama `main` limpia y al día.
- [x] El enlace de GitHub Pages está activo y operativo para los evaluadores.
