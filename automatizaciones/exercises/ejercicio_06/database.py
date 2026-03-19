import sqlite3
from pathlib import Path

path = Path(__file__).parent
database_path = path / "articles.db"


con = sqlite3.connect(database_path)

cur = con.cursor()

cur.execute("CREATE TABLE article(id, name)")