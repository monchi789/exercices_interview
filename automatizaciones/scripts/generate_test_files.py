from pathlib import Path
from datetime import datetime, timedelta
import random

folder = Path(__file__).parent.parent / "sandbox" / "uploads"

folder.mkdir(parents=True, exist_ok=True)

for i in range(20):

    file = folder / f"file_{i}.txt"

    file.write_text("test file")

    days_old = random.randint(0, 15)

    fake_time = datetime.now() - timedelta(days=days_old)

    timestamp = fake_time.timestamp()

    import os
    os.utime(file, (timestamp, timestamp))

print("Files generated")