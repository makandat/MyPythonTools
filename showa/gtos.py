#!/usr/bin/python3
# 西暦を元号に変換する。
from Py365Lib import Common

if Common.count_args() == 0 :
 Common.stop(9, "Enter year. (yyyy)", Common.ESC_FG_YELLOW)

y = int(Common.args()[0])

if y >= 1926 and y < 1989 :
 g = "s"
 x = y - 1926 + 1
else :
 g = "h"
 x = y - 1989 + 1

print("{0}{1}".format(g, x))

