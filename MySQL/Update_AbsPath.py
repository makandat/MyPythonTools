#!/usr/bin/env python3
#  PATH の内容が相対パスだったら絶対パスに修正する。
from Py365Lib import *


# 開始
if Common.count_args() == 0 :
  stop(9, "パラメータがありません。テーブル名 (Videos, Music) のどちらかを指定します。")

tableName = Common.args()[0]

mysql = MySQL.MySQL(host='localhost', uid='user',pwd='ust62kjy', db='user')

sqlSELECT = f"SELECT id, `path` FROM {tableName} WHERE `PATH` NOT LIKE '/home/user/%'"
sqlUPDATE = "UPDATE {0} SET `PATH`='{1}' WHERE id={2}"
rows = mysql.query(sqlSELECT)
for row in rows :
  if tableName == 'Music' :
    sql = Text.format(sqlUPDATE, tableName, '/home/user/ミュージック/' + Text.replace("'", "''", row[1]), row[0])
  else :
    sql = Text.format(sqlUPDATE, tableName, '/home/user/ビデオ/' + Text.replace("'", "''", row[1]), row[0])
  print(sql)
  mysql.execute(sql)


