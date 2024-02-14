import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv('.env')

class DB:
    def __init__(self):
        try:
            self.mydb = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def querry(self, sqlstmt, data):
        cursor = self.mydb.cursor()
        cursor.execute(sqlstmt, data)
        return cursor

    def insert(self, sqlstmt, data):
        cursor = self.querry(sqlstmt, data)
        self.mydb.commit()
        cursor.close()

    def select(self, sqlstmt, data):
        cursor = self.querry(sqlstmt, data)
        result = cursor.fetchall()
        cursor.close()
        return result
    
    def update(self, sqlstmt, data):
        cursor = self.querry(sqlstmt, data)
        self.mydb.commit()
        cursor.close()

    def delete(self, sqlstmt, data):
        cursor = self.querry(sqlstmt, data)
        self.mydb.commit()
        cursor.close()
    