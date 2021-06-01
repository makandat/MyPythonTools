#!/usr/bin/env python3
#  再帰的に中間ファイルを削除する。
from Py365Lib import Common, FileSystem as fs
import os

# 中間ファイルの拡張子
iexts = (".obj", ".res", ".resw", ".pdb", ".pch", ".rc", ".rc2")

# パラメータを得る。
print("== 再帰的に中間ファイルを削除する。==")
# 対象のフォルダを得る。
if Common.count_args() == 0 :
  Common.stop(9, "フォルダを指定してください。")
folder = Common.args(0)
a = Common.readline(folder + "に対して再帰的に中間ファイルを削除します。よろしいですか？ (y/n)")
if a != "y" :
  Common.stop(1, "実行を中止しました。")

# 実行する。
files = fs.listFilesRecursively(folder, asstr=True)
for f in files:
  ext = fs.getExtension(f)
  for e in iexts:
    if ext == e :
      print("削除： " + f)
      os.remove(f)
    else :
      pass
print("終了。")
