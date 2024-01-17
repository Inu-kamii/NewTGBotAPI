import os

import psycopg2


class DBContext:
    def __init__(self):
        connection_string = os.getenv('DATABASE_URL')
        self.conn = psycopg2.connect(connection_string)

    def fetch_all(self, query, params=None):
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        result = cursor.fetchall()
        return result

    def execute_query(self, query, params=None):
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        self.conn.commit()