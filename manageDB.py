from flask import Flask
import mysql.connector

#DB接続情報
def conn_db():
      conn = mysql.connector.connect(
              host = '127.0.0.1',      #localhostでもOK
              port = '3306',
              user = 'root',
              passwd = 'kishimoto1',
              db = 'nba_websystem'
      )
      return conn

#本体
sql = 'SELECT * FROM average_w'

try:
      conn = conn_db()              #ここでDBに接続
      cursor = conn.cursor()       #カーソルを取得
      cursor.execute(sql)             #selectを投げる
      rows = cursor.fetchall()      #selectの結果を全件タプルに格納
except(mysql.connector.errors.ProgrammingError) as e:
      print('エラー')
      print(e)