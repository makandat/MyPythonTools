#!/usr/bin/env python3
#  BINDATA バイナリファイル image.cgi
import WebPage as cgi
import Text, FileSystem
import MySQL as mysql
import sys


SELECT_DATA = "SELECT datatype, hex(data) AS img FROM Binaries WHERE id={0}"


# ページクラス
class ImageData(cgi.WebPage) :
  # コンストラクタ
  def __init__(self, template="") :
    super().__init__(template)
    self.__mysql = mysql.MySQL()
    if self.isParam('id') :
      id = self.getParam('id')
      self.sendImage(id)
    else :
      pass

  # 画像データを応答として返す。
  def sendImage(self, id:int) -> None :
    sql = Text.format(SELECT_DATA, id)
    rows = self.__mysql.query(sql)
    datatype = rows[0][0]
    data = rows[0][1]
    i = 0
    buff =  list()
    for c in data :
      if  i % 2 == 1 :
        b = 16 * ImageData.nibble(c0) + ImageData.nibble(c)
        buff.append(b)
      else :
        c0 = c
      i += 1
    if datatype == '.jpg' :
      type = b'jpeg'
    elif datatype == '.png' :
      type = b'png'
    else :
      type = b'gif'
    s = b"Content-Type: image/" + type + b"\n\n" + bytes(buff)
    sys.stdout.buffer.write(s)
    return

  # ニブルに変換する。
  @staticmethod
  def nibble(c) :
    n = ord(c)
    if n >= 0x3a :
      n -= 0x41
      n += 10
    else :
      n -= 0x30
    return n

# 画像データを返す。
ImageData()
