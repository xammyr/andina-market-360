# Andina Market 360 — Consolidación Comercial

Caso empresarial transversal del **Cuaderno de Prácticas Git y GitHub (36 Capítulos)**. Consolida operaciones comerciales ficticias de las sedes **Lima, Ica y Arequipa** mediante Python, pruebas automatizadas y publicación estática en GitHub Pages.

## Tabla de Indicadores (Línea Base Ficticia)

| Sede | Total Esperado (CSV) | Operaciones | Fuente de Cálculo |
| :--- | :---: | :---: | :--- |
| **Lima** | S/ 814.00 | 4 | `data/ventas.csv` |
| **Ica** | S/ 555.00 | 4 | `data/ventas.csv` |
| **Arequipa** | S/ 476.00 | 4 | `data/ventas.csv` |
| **TOTAL** | **S/ 1,845.00** | **12** | `src/resumen.py` |

## Inicio Rápido

```bash
# 1. Ejecutar las 4 pruebas unitarias de referencia
python -m unittest discover -s tests -v

# 2. Calcular resumen en consola
python src/resumen.py

# 3. Exportar JSON para el dashboard web
python src/resumen.py --json docs/data/resumen.json
```

## Documentación y Gobernanza
- [Manual de Operaciones](docs/manual.md)
- [Guía de Contribución](CONTRIBUTING.md)
- [Política de Seguridad](SECURITY.md)
- [Historial de Versiones](CHANGELOG.md)
Tablero actualizado para análisis de operaciones comerciales.