import socket
from datetime import datetime
from pathlib import Path
import time 

script_dir = Path(__file__).parent

report_file = script_dir / "report.txt"

def check_port(host, port):
    try:
        with socket.create_connection((host, port), timeout=3):
            return True
    except OSError:
        return False
    
ports = [
    {
        "service": "Backend",
        "port": 8000
    },
    {
        "service": "Database",
        "port": 5432
    },
    {
        "service": "Redis",
        "port": 6379
    }
]

def check_services():
    for i in ports:
        if check_port("localhost", i["port"]):
            print(f"Service {i["service"]} is active on port {i['port']}")
        else:
            message = f"The service {i['service']} is down - {datetime.now()}\n"
            with open(report_file, "a") as f:
                f.write(message)

while True:
    print("Iniciamos el analisis")
    check_services()
    print("Terminamos el analisis")
    time.sleep(30)