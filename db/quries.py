import sqlite3
from pathlib import Path
from datetime import datetime, timedelta

def init_db():
    global db, cursor
    db = sqlite3.connect(Path(__file__).parent.parent / "db.sqlite3")
    cursor = db.cursor()


def create_tables():
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS existed_texts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT,
            time DATETIME
        )
        """
    )
    db.commit()

def get_text():
    cursor.execute(
        """
        SELECT * FROM existed_texts
        """
    )
    return [i for i in cursor.fetchall()]

def save_text(text):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute(
        """
        INSERT INTO existed_texts (text, time)
        VALUES (:t, :time)
        """,
        {
            "t": text,
            "time": current_time,
        }
    )
    db.commit()

def drop_db():
    one_hour_ago = (datetime.now() - timedelta(minutes=3)).strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute(
        """
        DELETE FROM existed_texts
        WHERE time <= :time_threshold
        """,
        {
            "time_threshold": one_hour_ago,
        }
    )
    db.commit()

if __name__ == "__main__":
    init_db()
    create_tables()

