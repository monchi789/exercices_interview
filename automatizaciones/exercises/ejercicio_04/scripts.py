"""
Script: analyze_logs.py

Objetivo:
1. Leer un archivo de logs grande de forma eficiente
2. Contar los niveles de log (INFO, WARNING, ERROR)
3. Detectar los 10 errores más frecuentes
4. Generar un reporte en formato JSON

Este enfoque es eficiente porque procesa el archivo línea por línea
(streaming) sin cargar todo en memoria.
"""

import re
import json
from pathlib import Path
from collections import Counter

# Ruta del archivo de logs
LOG_FILE = Path("logs/app.log")

# Archivo de salida del reporte
REPORT_FILE = Path("report.json")

# ------------------------------------------------------------
# Regex para encontrar el nivel del log
# Busca palabras exactas: INFO, WARNING o ERROR
# \b significa "límite de palabra"
# ------------------------------------------------------------
level_pattern = re.compile(r"\b(INFO|WARNING|ERROR)\b")

# ------------------------------------------------------------
# Contadores
# Counter es una estructura eficiente para contar elementos
# ------------------------------------------------------------
level_counter = Counter()   # cuenta niveles de log
error_counter = Counter()   # cuenta mensajes de error


# ------------------------------------------------------------
# Procesamiento del archivo de logs
# ------------------------------------------------------------
with open(LOG_FILE, "r") as file:

    # Leer el archivo línea por línea (importante para logs grandes)
    for line in file:

        # Buscar el nivel de log usando regex
        match = level_pattern.search(line)

        # Si se encontró un nivel
        if match:

            # Obtener el nivel encontrado (INFO, WARNING, ERROR)
            level = match.group(1)

            # Incrementar contador del nivel
            level_counter[level] += 1

            # Si es un error, analizamos el mensaje
            if level == "ERROR":

                # Extraer el mensaje después de la palabra ERROR
                # Ejemplo:
                # "2026-03-09 ERROR Database connection failed"
                message = line.split("ERROR")[-1].strip()

                # Contar ese mensaje de error
                error_counter[message] += 1


# ------------------------------------------------------------
# Obtener los 10 errores más frecuentes
# most_common(n) devuelve una lista de tuplas
# ------------------------------------------------------------
top_errors = error_counter.most_common(10)


# ------------------------------------------------------------
# Construir el reporte final
# ------------------------------------------------------------
report = {
    "log_levels": dict(level_counter),
    "top_10_errors": top_errors
}


# ------------------------------------------------------------
# Guardar reporte en JSON
# indent=4 solo mejora la legibilidad
# ------------------------------------------------------------
with open(REPORT_FILE, "w") as file:
    json.dump(report, file, indent=4)


# ------------------------------------------------------------
# Mostrar resultados en consola
# ------------------------------------------------------------
print("Análisis completado.")
print(f"Logs analizados: {LOG_FILE}")
print(f"Reporte generado: {REPORT_FILE}")

print("\nConteo de niveles:")
print(level_counter)

print("\nTop 10 errores:")
for error, count in top_errors:
    print(f"{error} -> {count}")