#!/usr/bin/env python3
from Py365Lib import *
from pprint import pprint

SELECT = "SELECT count(id) FROM YJFX_Settle WHERE id={0}"
INSERT = "INSERT INTO YJFX_Settle(id, CurrencyPair, Sell, price1, Date1, price2, Date2, Benefit) VALUES({0}, '{1}', '{2}', {3}, '{4}', {5}, '{6}', {7})"

mysql = MySQL.MySQL()

# データ読み込み
def insertData(fileName) :
  global mysql
  data = FileSystem.readAllText(fileName)
  lines = Text.split("\n", data)
  # タイトル行を読み飛ばす。
  i = 1
  while i < len(lines) :
    line = lines[i]
    print(line)
    if line == "" :
      break
    pline = Text.split(',', line)
    # id (取引番号)
    id = pline[0]
    # CurrencyPair
    currency = getCurrencyCode(pline[2])
    # Sell
    sell = '1' if pline[3] == '売' else '0'
    # price1, Date1 (取得)
    price1 = Text.replace(',', '', pline[9])
    Date1 = pline[6]
    # price2, Date2 (決済)
    price2 = Text.replace(',', '', pline[4])
    Date2 = pline[7]
    # Benefit
    benefit = Text.replace(',', '', pline[10])
    # すでに登録済みか確認
    if not exists(id) :
      # テーブルに挿入
      sql = Text.format(INSERT, id, currency, sell, price1, Date1, price2, Date2, benefit)
      mysql.execute(sql)
    i += 1
  return i


# Currency Pair コードを得る。
def getCurrencyCode(jc) :
  code = "?"
  if jc == "ドル/円" :
    code = "USD/JPY"
  elif jc == "豪ドル/円" :
    code = "AUD/JPY"
  elif jc == "ユーロ/円" :
    code = "EUR/JPY"
  elif jc == "ユーロ/ドル" :
    code = "EUR/USD"
  else :
    pass
  return code

# id が登録済みかを返す。
def exists(id) :
  global mysql
  n = mysql.getValue(Text.format(SELECT, id))
  return n > 0


if Common.count_args() == 0 :
  Common.stop(9, "CSV ファイルを指定してください。")

# メイン
#try :
filePath = Common.args()[0]
insertData(filePath)
print("正常終了。")
#except Exception as e:
#  Common.esc_print("red", str(e))

