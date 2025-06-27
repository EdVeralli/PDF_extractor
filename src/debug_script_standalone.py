#!/usr/bin/env python3
"""
Script de depuración para verificar los cálculos de estadísticas de downtime
"""

import csv
from pathlib import Path

def debug_calculate_downtime_statistics(data_path):
    """
    Versión de depuración para ver todos los valores calculados
    """
    stats = {
        'main_url_uptime': 0,
        'main_url_downtime': 0,
        'ash_url_uptime': 0,
        'ash_url_downtime': 0,
        'total_time': 0,
        'ash_downtime_percentage': 0
    }
    
    print("=== DEPURACIÓN DE CÁLCULOS ===")
    
    # Leer uptime_report_main_url.csv
    main_csv_path = Path(data_path) / "uptime_report_main_url.csv"
    print(f"\nLeyendo: {main_csv_path}")
    print(f"Existe: {main_csv_path.exists()}")
    
    if main_csv_path.exists():
        with open(main_csv_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            row_count = 0
            for row in reader:
                row_count += 1
                if 'uptime_segundos' in row and row['uptime_segundos']:
                    try:
                        value = int(row['uptime_segundos'])
                        stats['main_url_uptime'] += value
                        print(f"  Fila {row_count}: uptime = {value}")
                    except ValueError as e:
                        print(f"  Fila {row_count}: Error uptime = {e}")
                if 'downtime_segundos' in row and row['downtime_segundos']:
                    try:
                        value = int(row['downtime_segundos'])
                        stats['main_url_downtime'] += value
                        print(f"  Fila {row_count}: downtime = {value}")
                    except ValueError as e:
                        print(f"  Fila {row_count}: Error downtime = {e}")
    
    # Leer uptime_report_ash_url.csv
    ash_csv_path = Path(data_path) / "uptime_report_ash_url.csv"
    print(f"\nLeyendo: {ash_csv_path}")
    print(f"Existe: {ash_csv_path.exists()}")
    
    if ash_csv_path.exists():
        with open(ash_csv_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            row_count = 0
            for row in reader:
                row_count += 1
                if 'uptime_segundos' in row and row['uptime_segundos']:
                    try:
                        value = int(row['uptime_segundos'])
                        stats['ash_url_uptime'] += value
                        print(f"  Fila {row_count}: uptime = {value}")
                    except ValueError as e:
                        print(f"  Fila {row_count}: Error uptime = {e}")
                if 'downtime_segundos' in row and row['downtime_segundos']:
                    try:
                        value = int(row['downtime_segundos'])
                        stats['ash_url_downtime'] += value
                        print(f"  Fila {row_count}: downtime = {value}")
                    except ValueError as e:
                        print(f"  Fila {row_count}: Error downtime = {e}")
    
    # Calcular totales
    stats['total_time'] = (stats['main_url_uptime'] + stats['main_url_downtime'] + 
                          stats['ash_url_uptime'] + stats['ash_url_downtime'])
    
    print("\n=== RESUMEN DE VALORES ===")
    print(f"main_url_uptime: {stats['main_url_uptime']:,}")
    print(f"main_url_downtime: {stats['main_url_downtime']:,}")
    print(f"ash_url_uptime: {stats['ash_url_uptime']:,}")
    print(f"ash_url_downtime: {stats['ash_url_downtime']:,}")
    print(f"TOTAL TIME: {stats['total_time']:,}")
    
    # Calcular porcentaje
    if stats['total_time'] > 0:
        stats['ash_downtime_percentage'] = (stats['ash_url_downtime'] / stats['total_time']) * 100
        print(f"\nCÁLCULO PORCENTAJE:")
        print(f"{stats['ash_url_downtime']} / {stats['total_time']} * 100 = {stats['ash_downtime_percentage']:.4f}%")
    
    return stats

def main():
    """Función principal"""
    print("Script de depuración de estadísticas de downtime")
    print("=" * 50)
    
    # Obtener la ruta absoluta de la carpeta src
    src_path = Path(__file__).parent.absolute()
    
    # Construir la ruta absoluta a la carpeta data
    data_path = src_path.parent / "data"
    
    print(f"Buscando archivos en: {data_path}")
    
    # Ejecutar depuración
    stats = debug_calculate_downtime_statistics(data_path)
    
    print("\n" + "=" * 50)
    print("Depuración completada")

if __name__ == "__main__":
    main()
