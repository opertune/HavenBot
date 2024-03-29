import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv('.env')

class DB:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )

    def querry(self, sqlstmt, data):
        self.mydb.reconnect()
        cursor = self.mydb.cursor()
        cursor.execute(sqlstmt, data)
        return cursor

    def insert(self, sqlstmt, data):
        self.mydb.reconnect()
        cursor = self.querry(sqlstmt, data)
        self.mydb.commit()
        cursor.close()

    def select(self, sqlstmt, data):
        self.mydb.reconnect()
        cursor = self.querry(sqlstmt, data)
        result = cursor.fetchall()
        cursor.close()
        return result
    
    def update(self, sqlstmt, data):
        self.mydb.reconnect()
        cursor = self.querry(sqlstmt, data)
        self.mydb.commit()
        cursor.close()

    def delete(self, sqlstmt, data):
        self.mydb.reconnect()
        cursor = self.querry(sqlstmt, data)
        self.mydb.commit()
        cursor.close()
    