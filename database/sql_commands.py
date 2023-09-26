import sqlite3
from database import sql_queries
import asyncio

class Database:
    def __init__(self):
        self.connection = sqlite3.connect("db.sqlite3", check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.loop = asyncio.get_running_loop()

    def sql_create_db(self):
        if self.connection:
            print("Database connected successfully")

        self.connection.execute(sql_queries.CREATE_WORDS_TABLE)
        self.connection.commit()

    def sql_insert_word(self, word):
        self.cursor.execute(sql_queries.INSERT_WORD_QUERY, (None, word))
        self.connection.commit()

    def sql_select_word(self):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "word": row[1]
        }
        return self.cursor.execute(sql_queries.SELECT_WORD_QUERY).fetchall()

    def sql_delete_word(self, id):
        self.cursor.execute(sql_queries.DELETE_USER_FORM_QUERY, (id,))
        self.connection.commit()
