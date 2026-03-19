from pathlib import Path
import os
import random
import time
from datetime import datetime, timedelta

BACKUPS_DIR = Path("/home/monchi789/Projects/ejercicios-entrevista/automatizaciones/exercises/ejercicio_03/backups")

def randomize_dates():
    now = datetime.now()

    for file in BACKUPS_DIR.glob("*.zip"):
        # días aleatorios entre 10 y 30
        days_ago = random.randint(10, 30)

        random_date = now - timedelta(days=days_ago)

        timestamp = random_date.timestamp()

        os.utime(file, (timestamp, timestamp))

        print(f"{file.name} -> {random_date}")

if __name__ == "__main__":
    randomize_dates()