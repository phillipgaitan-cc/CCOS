import sqlite3
from pathlib import Path

DB_PATH = Path("database/ccos.db")
SCHEMA_PATH = Path("database/schema.sql")


def initialize_database():
    conn = sqlite3.connect(DB_PATH)

    with open(SCHEMA_PATH, "r") as f:
        conn.executescript(f.read())

    conn.commit()
    conn.close()


if __name__ == "__main__":
    initialize_database()
    print("CCOS database created.")