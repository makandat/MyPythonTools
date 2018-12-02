#!/usr/bin/env python3
#  ディレクトリやファイル名で特殊な文字が使われていたら削除または置き換えて名前を変更する。
from Py365Lib import Common, Text, FileSystem as fs

# 特定文字を置き換える。
def rename(fp) :
    if fs.isDirectory(fp) :
        result = Text.replace('[', '', fp)
        result = Text.replace(']', '', result)
    else :
        result = Text.replace('[', '(', fp)
        result = Text.replace(']', ')', result)
    result = Text.replace('#', '_', result)
    result = Text.replace("'", "", result)
    return result
    

# 対象のディレクトリを得る。
if Common.count_args() < 2 :
    Common.stop("対象のディレクトリとスクリプトファイルの名前(パス)を指定してください。")

# 対象のディレクトリ
dir0 = Common.args()[0]
if not fs.isDirectory(dir0) :
    Common.stop(f"{dir0} はディレクトリとして存在しません。")

# スクリプトファイルのパス
savePath = Common.args()[1]

lines = "#!/bin/bash\n"

# ファイル一覧を得る。
files = fs.listFiles(dir0)
for fp in files :
    nf = rename(fp)
    if Text.contain(' ', fp) :
        fp = "'" + fp + "'"
        nf = "'" + nf + "'"
    if fp != nf :
        lines += "mv -v {0} {1}\n".format(fp, nf)

# ディレクトリ一覧を得る。
dirs = fs.listDirectories(dir0)
for dp in dirs :
    nd = rename(dp)
    if Text.contain(' ', dp) :
        dp = "'" + dp + "'"
        nd = "'" + nd + "'"
    if dp != nd :
        lines += f"mv -v {dp} {nd}\n"

# スクリプトを作成する。
try :
    fs.writeAllText(savePath, lines)
    print(f"\n終わり。{savePath} が作成されました。")
except Exception as e :
    Common.esc_print("red", "エラーを検出。{0}".format(e.message))
    exit(9)
