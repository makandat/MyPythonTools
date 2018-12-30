#!/usr/bin/env python3
#  ディレクトリ内のファイルの拡張子を変更する。
from Py365Lib import Common, Text, FileSystem as fs

# ディレクトリ内のファイルの拡張子を変更するコマンドを表示する。
#   実行するときは、リダイレクトでファイル保存して実行する。
def changeAllExt(target, oldExt, newExt) :
  files = fs.listFiles(target, "*." + oldExt)
  for fold in files :
    fnew = fs.changeExt(fold, "." + newExt)
    if Text.contain(' ', fold) :
      cmd = f"mv -v '{fold}' '{fnew}'"
    else :
      cmd = f"mv -v {fold} {fnew}"
    print(cmd)
  return

# メインプログラム
if Common.count_args() < 3 :
  Common.stop(9, "RenameExt.py\n  パラメータにディレクトリと変更前と変更後の拡張子を指定します。\n  拡張ののドットは不要です。\n", Common.ESC_NORMAL)

args = Common.args()
target = args[0]

if not fs.isDirectory(target) :
  Common.stop(1, f"{target} は不正なディレクトリです。")

extOld = args[1]
extNew = args[2]

changeAllExt(target, extOld, extNew)

print("正常終了。")

