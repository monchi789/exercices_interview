import random
from datetime import datetime, timedelta
from pathlib import Path

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "app.log"

levels = ["INFO", "WARNING", "ERROR"]

error_messages = [
    "Database connection failed",
    "Timeout contacting payment API",
    "User authentication failed",
    "File not found",
    "Permission denied",
    "Invalid input data",
    "Redis connection lost",
    "Service unavailable",
    "Disk write error",
    "Email sending failed",
]

info_messages = [
    "User logged in",
    "User logged out",
    "Order created",
    "Cache refreshed",
    "Background job completed",
]

warning_messages = [
    "High memory usage",
    "Slow query detected",
    "API response delayed",
]

def generate_logs(lines=20000):
    start_time = datetime.now() - timedelta(days=1)

    with open(LOG_FILE, "w") as f:
        for i in range(lines):

            level = random.choices(
                levels,
                weights=[70, 20, 10]
            )[0]

            if level == "ERROR":
                message = random.choice(error_messages)
            elif level == "WARNING":
                message = random.choice(warning_messages)
            else:
                message = random.choice(info_messages)

            timestamp = start_time + timedelta(seconds=i)

            log = f"{timestamp} {level} {message}\n"

            f.write(log)

    print(f"Logs generados en {LOG_FILE}")


if __name__ == "__main__":
    generate_logs()