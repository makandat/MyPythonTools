#!/usr/bin/python3
# 元号の生年から年齢を求める。
from Py365Lib import Common

if Common.count_args() == 0:
 Common.stop(9, "Enter birth_year(Showa)", Common.ESC_FG_YELLOW)

showa = int(Common.args()[0])
AGE0 = 92
age = AGE0 - showa + 1
print("s{0}".format(age))

