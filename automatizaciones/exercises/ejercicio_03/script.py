import subprocess
import os
from pathlib import Path
import zipfile
from datetime import datetime

PGPASSWORD='labpass'
BACKUPS_DIR = Path('./backups')
BACKUP_FILE = BACKUPS_DIR / "backup.sql"
REPORT_DIR = Path('./reports')

env_vars = os.environ.copy()
env_vars["PGPASSWORD"] = PGPASSWORD
backups_deleted = []

def create_backup():
    with open(BACKUP_FILE, 'w') as f:
        subprocess.run(
            [
                "pg_dump",
                "-h", "localhost",
                "-U", "labuser",
                "-d", "labdb",
            ],
            stdout=f,
            env=env_vars
        )


def compress_backup(time):
    with zipfile.ZipFile(BACKUPS_DIR/f'{time}.zip', 'w', compression=zipfile.ZIP_DEFLATED) as zf:
        zf.write(BACKUP_FILE, arcname=BACKUP_FILE)

def clean_workspace():
    os.remove(BACKUP_FILE)


def clean_backups(time):

    for file in BACKUPS_DIR.iterdir():
        timestamp = file.stat().st_mtime

        file_date = datetime.fromtimestamp(timestamp)

        age = datetime.fromtimestamp(time) - file_date

        if age.days > 7:
            file.unlink()
            backups_deleted.append(file.name)
    
    if backups_deleted:
        with open(REPORT_DIR / f"{time}.txt", 'w') as f:
            for name in backups_deleted:
                f.write(f'El Backup f{name} eliminado\n')
                



time = datetime.now().timestamp()

create_backup()
compress_backup(time)
clean_workspace()
clean_backups(time)



