#!/usr/bin/python3
from Py365Lib import Common, Text

# 元号を西暦に変換する。
if Common.count_args() == 0 :
 Common.stop(9, "Enter Japanese Gengo year. like s20, h10 where characters must be 3.", Common.ESC_FG_YELLOW)

g = Common.args()[0]

if Text.tolower(g[0]) == 's' :
 y0 = 1926
elif Text.tolower(g[0]) == 'h' :
 y0 = 1989
else :
 y0 = 1912

gengo = Text.Text(g)

if gengo.length == 3 :
  y = int(gengo.right(2))
  x = y + y0 - 1
  print(x)
else :
  Common.stop(1, "Error: Inpur length must be 3.")
