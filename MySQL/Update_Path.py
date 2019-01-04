#!/usr/bin/env python3
#  PATH の内容を修正する。
from Py365Lib import *


# 開始
tableName = 'Music'

mysql = MySQL.MySQL(host='localhost', uid='user',pwd='ust62kjy', db='user')

sqlSELECT = "SELECT id, `path` FROM Music"
sqlUPDATE = "UPDATE Music SET `PATH`='{0}' WHERE id={1}"
rows = mysql.query(sqlSELECT)
for row in rows :
  id = row[0]
  path = Text.replace("/Videos/", "/ミュージック/", row[1])
  path = Text.replace("//", "/", path)
  path = Text.replace("'", "''", path)
  sql = Text.format(sqlUPDATE, path, id)
  print(sql)
  mysql.execute(sql)


