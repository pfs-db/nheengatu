import sqlite3
from datetime import datetime


def create_db(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS database_growth (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            glossar_size INTEGER,
            lexicon_size INTEGER
        )
    """
    )
    conn.commit()
    conn.close()


def log_db_sizes(db_path, glossar_size, lexicon_size):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO database_growth (timestamp, glossar_size, lexicon_size)
        VALUES (?, ?, ?)
    """,
        (datetime.now().isoformat(), glossar_size, lexicon_size),
    )
    conn.commit()
    conn.close()
