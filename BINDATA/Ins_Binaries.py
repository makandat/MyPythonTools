#!/usr/bin/env python3
#  バイナリーファイルをテーブル Binaries に挿入する。
import Common
import FileSystem as fs
import MySQL as mysql
import Text

INSERT = "INSERT INTO Binaries(title, original, datatype, data) VALUES('{0}', '{1}', '{2}', {3})"

# バイナリーファイル filePath をテーブル Binaries に挿入する。
def insertBinaries(filePath) :
  ext = fs.getExtension(filePath)
  fileName = fs.getFileName(filePath)
  hexa = bin2hex(filePath)
  sql = Text.format(INSERT, fileName, filePath, ext, hexa)
  client = mysql.MySQL()
  client.execute(sql)
  return

# バイナリーファイルをヘキサに変換する。
def bin2hex(filePath) :
  buff = "0x"
  b = fs.readBinary(filePath)
  buff += b.hex()
  return buff
  
# メイン
if Common.count_args() == 0 :
  Common.stop("ファイルを指定してください。")

filePath = Common.args()[0]

insertBinaries(filePath)
print('Done.')
