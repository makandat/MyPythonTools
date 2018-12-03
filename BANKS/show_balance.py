#!/usr/bin/env python3
#  テーブル BANKS の内容表示、ビュー vw_balance 表示
from Py365Lib import *
from pprint import pprint

client = MySQL.MySQL()

Common.esc_print('cyan', '銀行別残高一覧')

rows = client.query("SELECT * FROM BANKS")
for row in rows :
  pprint(row)

print()
Common.esc_print('cyan', '日付ごとの残高一覧')
rows = client.query("SELECT * FROM vw_balance")
for row in rows :
  pprint(row)

