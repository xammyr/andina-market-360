# Manual Operativo — Andina Market 360

Este manual describe la ejecución reproducible del tablero comercial a partir de la base ficticia [ventas.csv](../data/ventas.csv).

## Comandos de verificación
1. Ejecutar pruebas unitarias:
   ```bash
   python -m unittest discover -s tests -v
   ```
2. Regenerar salida JSON para la web:
   ```bash
   python src/resumen.py --json docs/data/resumen.json
   ```
3. Levantar servidor local de previsualización:
   ```bash
   python -m http.server 8000 --directory docs
   ```
