import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect("analysis.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS analysis (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT,
            query TEXT,
            result TEXT,
            created_at TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_analysis(filename, query, result):
    conn = sqlite3.connect("analysis.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO analysis (filename, query, result, created_at)
        VALUES (?, ?, ?, ?)
    """, (filename, query, result, datetime.now().isoformat()))
    conn.commit()
    conn.close()