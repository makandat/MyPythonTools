#!/usr/bin/env python3
#  ディレクトリで特殊な文字が使われていたら削除または置き換えて名前を変更する。
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

# ディレクトリの名前変更コマンドを作成する。
def renameDirs(dir0) :
    lines = "#!/bin/bash\n"
    dirs = fs.listDirectories(dir0)
    for dp in dirs :
        nd = rename(dp)
        if Text.contain(' ', dp) :
            dp = "'" + dp + "'"
            nd = "'" + nd + "'"
        if dp != nd :
            lines += f"mv -v {dp} {nd}\n"
        lines += renameDirs(dp)
    return lines

# 対象のディレクトリを得る。
if Common.count_args() < 2 :
    Common.stop("対象のディレクトリとスクリプトファイルの名前(パス)を指定してください。")

# 対象のディレクトリ
dir0 = Common.args()[0]
if not fs.isDirectory(dir0) :
    Common.stop(f"{dir0} はディレクトリとして存在しません。")

# スクリプトファイルのパス
savePath = Common.args()[1]


# ディレクトリの名前変更コマンドを作成する。
lines = renameDirs(dir0)

# スクリプトを作成する。
try :
    fs.writeAllText(savePath, lines)
    print(f"\n終わり。{savePath} が作成されました。")
except Exception as e :
    Common.esc_print("red", "エラーを検出。{0}".format(e.message))
    exit(9)
