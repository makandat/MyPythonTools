#!/usr/bin/env python3
#    RenameNumber.py
#  ディレクトリ内のファイル名を連続番号のあるファイル名にする。
#  パラメータ
#    ディレクトリ(最後の/は付けない)
#    ファイルのワイルドカード(すべての場合は'*.*'。必ず引用符で囲むこと。)
#    ファイル名の固定部分(英字のみ)
#    数字部分の桁数
#    
from Py365Lib import Common, Text, FileSystem as fs

# ディレクトリ内のファイル名を連続番号のあるファイル名にする。
#   実行するときはリダイレクトを利用してファイル保存してコマンドとして実行する。
def renameAll(args) :
  dir = args[0]
  wild = args[1]
  fix = args[2]
  cols = args[3]
  i = 1
  files = fs.listFiles(dir, wild)
  sortedFiles = sorted(files)
  for fold in sortedFiles :
    ext = fs.getExtension(fold)
    fmt = "{0:0" + cols + "d}"
    fnew = dir + "/" + fix + Text.format(fmt, i) + ext
    cmd = f"mv -v {fold} {fnew}"
    print(cmd)
    i += 1



# メインプログラム
EXPLAIN = '''#    RenameNumber.py
ディレクトリ内のファイル名を連続番号のあるファイル名にする。
  パラメータ
    ディレクトリ(最後の/は付けない)
    ファイルのワイルドカード(すべての場合は'*.*'。必ず引用符で囲むこと。)
    ファイル名の固定部分(英字のみ)
    数字部分の桁数
'''

if Common.count_args() < 3 :
  Common.stop(9, EXPLAIN, Common.ESC_NORMAL)

renameAll(Common.args())

print("正常終了。")
