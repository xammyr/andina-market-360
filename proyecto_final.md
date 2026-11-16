# Proyecto Integrador Final · Andina Market 360

## 1. Alcance y Justificación del Caso (Ejemplo 36.1)
El proyecto resuelve la necesidad crítica de consolidar la información de ventas dispersa entre sedes territoriales (Lima, Ica, Arequipa) sin intervención manual que induzca a errores de digitación o sumas equivocadas. 
Garantiza trazabilidad completa de cambios, reproducibilidad de cálculos mediante Python estándar y disponibilidad pública del panel gerencial vía GitHub Pages.

---

## 2. Comprobación Integral de la Solución (Ejemplo 36.3)
Comandos ejecutados para la verificación completa del sistema:
```bash
# 1. Verificación de calidad de código y suite de pruebas unitarias
python -m unittest discover -s tests -v

# 2. Generación del resumen analítico para el tablero web
python src/resumen.py --json docs/data/resumen.json

# 3. Estado limpio del repositorio
git status --short
```

### Resultados Observados de Referencia:
- Pruebas unitarias: **4/4 pruebas aprobadas (OK)** sin dependencias de red.
- Cifras consolidadas:
  - Lima: S/ 814.00
  - Ica: S/ 555.00
  - Arequipa: S/ 476.00
  - Total consolidado: S/ 1,845.00 (12 operaciones exactas).
- Enlace web público activo: [https://xammyr.github.io/andina-market-360/](https://xammyr.github.io/andina-market-360/)
- Tag de entrega estable: `v1.0.0` registrado en Git y en Releases de GitHub.

---

## 3. Autoevaluación según la Rúbrica de 100 Puntos (Anexo B)

| Criterio Observable | Puntaje Máximo | Puntaje Obtenido | Justificación y Evidencia |
| :--- | :---: | :---: | :--- |
| **Repositorio y control de versiones** | 20 | 20 | Commits claros con convenciones, flujo de ramas (`feature/`), resolución de conflictos y tag `v1.0.0`. |
| **Procesamiento de datos** | 20 | 20 | Dataset ficticio en `data/ventas.csv`, script `src/resumen.py` y generación matemática exacta de totales por sede. |
| **Pruebas y automatización** | 20 | 20 | 4 pruebas unitarias en `test_resumen.py` y pipeline de GitHub Actions ejecutando matriz Python con check verde. |
| **Publicación y documentación** | 15 | 15 | README completo, `manual.md`, CHANGELOG, y sitio web publicado en GitHub Pages. |
| **Colaboración y trazabilidad** | 10 | 10 | Issues (#1 y #2) registrados, tablero Kanban en Projects y Pull Request fusionado con checklist de revisión. |
| **Seguridad y uso responsable** | 10 | 10 | Cero credenciales ni datos reales en el historial, Dependabot activo y política `SECURITY.md`. |
| **Sustentación y evidencias** | 5 | 5 | Carpeta `evidencias/capturas/` con capturas oficiales debidamente nombradas y documentadas. |
| **TOTAL:** | **100** | **100** | **Cumplimiento total de los requerimientos de la guía** |

---

## 4. Conclusiones y Mejoras a Futuro
1. **Conclusión:** La adopción de Git y GitHub junto a scripts analíticos automáticos elimina el error humano en los cierres contables y permite auditorías de código transparentes.
2. **Mejora 1 (Datos):** Expandir el dataset para incluir series históricas mensuales y análisis de estacionalidad.
3. **Mejora 2 (Visualización):** Incorporar gráficos dinámicos con librerías JavaScript ligeras (ej. Chart.js) consumiendo directamente `resumen.json`.
4. **Mejora 3 (Gobernanza):** Configurar ramas protegidas (*Branch Protection Rules*) obligando aprobación de dos revisores antes de cualquier merge a `main`.
