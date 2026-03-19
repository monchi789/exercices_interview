# Importamos la libreria pathlib para trabajar con rutas de archivos
from pathlib import Path
from datetime import datetime

# Optener la ruta del directorio del script
script_dir = Path(__file__).parent

# Ruta de la carpeta de archivos dentro de ../sandbox/uploads/
uploads_folder = script_dir.parent.parent / "sandbox" / "uploads"

# Generamos la ruta del archivo de reportes
report_file = script_dir / "report.txt"

report_file_names = []

# Obtenemos el valor de la fecha actual
now = datetime.now()

# Iteramos cada item de la ruta
for file in uploads_folder.iterdir():

    # Optenemos la fecha de creación del archivo en valor de segundos
    timestamp = file.stat().st_mtime

    # Formateamos el valor a un valor datetime
    file_date = datetime.fromtimestamp(timestamp)

    # Calculamos la diferencia entre la fecha de creación del archivo y la fecha actual
    age = now - file_date

    # Comprovamos que el archivo no sea mayor a 7 dias
    if age.days > 7:
        file.unlink()
        report_file_names.append(file.name)

with open(report_file, "w") as f:
    for name in report_file_names:
        f.write(f"Archivo {name} eliminado\n")
