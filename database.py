import psycopg2
import psycopg2 as psql
import os
from dotenv import load_dotenv
load_dotenv()


class Database:
    @staticmethod
    def connect(query: str, query_type: str):
        db = psycopg2.connect(
            database=os.getenv('DATABASE'),
            user=os.getenv('USER'),
            password=os.getenv('PASSWORD'),
            host=os.getenv('HOST'),
            port=os.getenv('PORT')
        )
        cursor = db.cursor()
        data = ["insert", "update", "delete", "alter"]
        cursor.execute(query)
        if query_type in data:
            db.commit()
            if query_type == "insert":
                return "inserted successfully"

            else:
                return cursor.fetchall()

