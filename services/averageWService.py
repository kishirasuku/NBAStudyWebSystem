from manageDB import conn_db
from flask import Flask
import mysql.connector
from models.averageW import averageW

try:
    conn = conn_db()
    cursor = conn.cursor()    #カーソルを取得
except:
    print("DB Error")

def queryAverageW(year):
    cursor.execute('SELECT * FROM average_w')
    rows = cursor.fetchall()

    for row in rows:
        if row[0] == year:
            return averageW(row)
