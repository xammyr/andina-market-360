# Inventario de Archivos Iniciales - Andina Market 360

| Carpeta o archivo | Propósito | Quién lo revisa |
| :--- | :--- | :--- |
| `README.md` | Explica el caso, la tabla de indicadores y cómo probarlo | Revisor/a |
| `data/ventas.csv` | 12 ventas ficticias (`id_venta`, `fecha`, `sede`, `producto`, `cantidad`, `precio_unitario`, `total`) | Analista de datos |
| `src/resumen.py` | Suma las ventas por sede y exporta el resultado a JSON | Desarrollador/a |
| `tests/test_resumen.py` | 4 pruebas unitarias locales | Desarrollador/a |
| `docs/` | Sitio estático: `index.html`, `style.css`, `manual.md` y `data/resumen.json` | Revisor/a |
| `.github/workflows/ci.yml` | Ejemplo de ejecución automática de pruebas | Desarrollador/a |

## Verificación de datos
El CSV solo contiene datos de ventas simuladas (sin nombres de clientes reales, correos personales, contraseñas ni tokens de autenticación). 
Además, la fórmula `cantidad * precio_unitario == total` coincide exactamente en las 12 filas.
