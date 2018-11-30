#!/usr/bin/env python3
#  YJFX 約定一覧読み込み
#
'''
CREATE TABLE YJFX_Settle (
  id decimal not null,
  CurrencyPair char(7) not null,
  Sell char(1) not null default '0',
  Price1 decimal not null,
  Date1 datetime not null,
  Price2 decimal not null,
  Date2 datetime not null,
  Benefit decimal,
  primary key(id)
);
'''
from Py356Lib import *


if Common.count_args() == 0 :
  Common.stop(9, "CSV ファイルを指定してください。")

fileName = Common.args()[0]



print(f"{fileName} を読み込みました。")
exit(0)
