import argparse
import csv
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DEFAULT_CSV = BASE_DIR / "data" / "ventas.csv"


def calcular_resumen(ruta_csv: Path = DEFAULT_CSV) -> dict:
    totales_sede = {"Lima": 0.0, "Ica": 0.0, "Arequipa": 0.0}
    operaciones = 0
    total_general = 0.0

    with open(ruta_csv, mode="r", encoding="utf-8", newline="") as f:
        lector = csv.DictReader(f)
        for fila in lector:
            sede = fila["sede"].strip()
            monto = float(fila["total"])
            totales_sede[sede] = round(totales_sede.get(sede, 0.0) + monto, 2)
            total_general = round(total_general + monto, 2)
            operaciones += 1

    return {
        "proyecto": "Andina Market 360",
        "tipo_datos": "Ficticio / Didáctico",
        "operaciones": operaciones,
        "por_sede": totales_sede,
        "total_general": total_general,
    }


def main():
    parser = argparse.ArgumentParser(description="Consolida ventas ficticias de Andina Market 360.")
    parser.add_argument("--csv", type=Path, default=DEFAULT_CSV, help="Ruta al archivo ventas.csv")
    parser.add_argument("--json", type=Path, help="Ruta de salida para exportar resumen.json")
    args = parser.parse_args()

    resumen = calcular_resumen(args.csv)

    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        with open(args.json, mode="w", encoding="utf-8") as out:
            json.dump(resumen, out, indent=2, ensure_ascii=False)
        print(f"JSON generado en {args.json}: {resumen['operaciones']} operaciones | Total S/ {resumen['total_general']:.2f}")
    else:
        print(f"Resumen Andina Market 360 ({resumen['operaciones']} operaciones):")
        for sede, monto in resumen["por_sede"].items():
            print(f"  - {sede}: S/ {monto:.2f}")
        print(f"  TOTAL: S/ {resumen['total_general']:.2f}")


if __name__ == "__main__":
    main()
