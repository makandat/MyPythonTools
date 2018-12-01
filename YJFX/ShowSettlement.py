#!/usr/bin/env python3
from Py365Lib import *

client = MySQL.MySQL()
sql = "SELECT * FROM YJFX_Settle"
rows = client.query(sql)
for row in rows :
  print(row)
sql = "SELECT Sum(Benefit) FROM YJFX_Settle";
rows = client.query(sql)
row = rows[0]
Common.esc_print("magenta", "\nBenefit = {:,} JPY".format(row[0]))

