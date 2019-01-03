#!/usr/bin/env python3
#  Music テーブルのデータ挿入
from Py365Lib import *

AUDIO = ['.mp3', '.wma', '.m4a', '.wav', '.ogg']

# INSERT 文を作る。
def insertData(dir) :
  # ファイルを列挙
  files = sorted(FileSystem.listFiles(dir))
  count = 0
  for f in files :
    if isAudio(f) :
      sql = makeSql(f)
      print(sql)
      count += 1
    else :
      continue
  # ファイルが見つからないときは、サブディレクトリを調べる。
  if count > 0 :
    return
  dirs = FileSystem.listDirectories(dir)
  for d in dirs :
    insertData(d)
  return

# AUDIOファイルか調べる。
def isAudio(filePath) :
  ext = FileSystem.getExtension(filePath)
  for x in AUDIO :
    if ext == x :
      return True
  return False

# SQL を作る。
def makeSql(filePath) :
  parts = Text.split('/', filePath)
  title = Text.replace("'", "''", parts[len(parts) - 2] + "/" + parts[len(parts) - 1])
  path = Text.replace("'", "''", filePath)
  sql = f"INSERT INTO Music(title, path) VALUES('{title}', '{path}');"
  return sql


# プログラム開始
if Common.count_args() == 0 :
  stop(9, "音声フォルダを指定してください。")

insertData(Common.args()[0])
