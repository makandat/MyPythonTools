#!/usr/bin/env python3
#  MYSQL BANKS テーブルへ INSERT
from Py365Lib import *
from decimal import *

# パラメータチェック
if Common.count_args() < 2 :
  message = '''コマンドライン引数を指定してください。
  銀行コード: 三井住友銀行 0009, 武蔵野銀行: 0133, 住信SBIネット銀行: 0013
  残高   円換算で
  (省略可能)口座種別:  0=普通 1=外貨 2=定期 3=定期(USD)　デフォルトは 0。
'''
  Common.stop(9, message)

# MySQL に接続する。(AppConf.ini 必要)
client = MySQL.MySQL()

# SQL を作成する。
try :
  day = DateTime.now().toString()
  bank = Common.args()[0]
  balance = Decimal(Common.args()[1])
  deposit = '0'
  if count_args() >= 3 :
    deposit = Common.args()[2]
  sql = f"INSERT INTO BANKS(DAY, BANK, DEPOSIT, BALANCE) VALUES('{day}', '{bank}', '{deposit}', {balance})"
  client.execute(sql)
except Exception as e :
  Common.stop(1, e.message)

# 終わり
print("データを追加しました。")

