#!/usr/bin/env python3
#  テーブル BANKS の内容表示、ビュー vw_balance 表示
from Py365Lib import *
from pprint import pprint

client = MySQL.MySQL()

Common.esc_print('cyan', '銀行別残高一覧')

rows = client.query("SELECT * FROM BANKS")
print("id  日付    銀行コード  口座     残高")
for row in rows :
  print("{0:4d} {1}  {2}  {3}  {,:}".format(row[0], row[1], row[2], row[3], row[4], row[5]))

print()
Common.esc_print('cyan', '日付ごとの残高一覧')
rows = client.query("SELECT * FROM vw_balance")
print("日付    残高")
for row in rows :
  print("{0}  {,:}".format(row[0], row[1]))

