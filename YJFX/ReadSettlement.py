#!/usr/bin/env python3
#  YJFX 約定一覧読み込み
#
'''
CREATE TABLE YJFX_Settle (
  id decimal(16,0) not null,
  CurrencyPair char(7) not null,
  Sell char(1) not null default '0',
  Price1 decimal(10,2) not null,
  Date1 datetime not null,
  Price2 decimal(10,2) not null,
  Date2 datetime not null,
  Benefit decimal(10,0),
  primary key(id)
);
'''
from decimal import *
from Py365Lib import *
from pprint import pprint
import csv


# 通貨ペアを略号にする。
def getCurrencyPair(s) :
  if s == "ドル/円" :
    return 'USD/JPY'
  elif s == 'ユーロ/円' :
    return 'EUR/JPY'
  elif s == '豪ドル/円' :
    return 'AUD/JPY'
  else :
    return '---/---'


#
#  プログラム開始
#  ==============
if Common.count_args() == 0 :
  Common.stop(9, "CSV ファイルを指定してください。")

fileName = Common.args()[0]
client = MySQL.MySQL()

with open(fileName, "r") as fcsv :
  f = csv.reader(fcsv, delimiter="," , doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
  next(f)  # ヘッダー読み飛ばし
  for row in f :
    id = Decimal(row[0])
    currency = getCurrencyPair(row[2])
    sell = '1' if row[3] == '売' else '0'
    price1 = Decimal(row[4])
    date1 = row[6]
    price2 = Decimal(row[9])
    date2 = row[7]
    benefit = Decimal(row[10])
    sql = f"INSERT INTO YJFX_Settle VALUES({id}, '{currency}', '{sell}', {price2}, '{date1}', {price2}, '{date2}', {benefit})"
    client.execute(sql)
    print(sql)

sql = "SELECT Sum(Benefit) FROM YJFX_Settle"
rows = client.query(sql)
print("Benefit = {0:d}".format(rows[0])

print("終了")
exit(0)
