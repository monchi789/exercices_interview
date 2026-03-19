from pathlib import Path
import random
import string

FILES_DIR = Path("files")
FILES_DIR.mkdir(exist_ok=True)

def generate_files(n=20):

    for i in range(n):

        filename = FILES_DIR / f"file_{i}.txt"

        content = "".join(random.choices(string.ascii_letters, k=1000))

        with open(filename, "w") as f:
            f.write(content)

    print(f"{n} archivos generados en {FILES_DIR}")

if __name__ == "__main__":
    generate_files()