#!/usr/bin/env python3

import mysql.connector
import time

print("hello, world.")


for i in range(15, 0, -1):
  print(i)
  time.sleep(1)

conn = mysql.connector.connect(
  host='sandbox-mysql',
  port='3306',
  user='root',
  password='rootpw',
  database='world'
)

conn.ping(reconnect=True)

print(conn.is_connected())

cur = conn.cursor()

cur.execute("SELECT * FROM city")

rows = cur.fetchall()

for row in rows:
  print(row)

cur.close()
conn.close()
