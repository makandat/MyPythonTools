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
    count = 0
    lines = "#!/bin/bash\n"
    dirs = fs.listDirectories(dir0)
    for dp in dirs :
        nd = rename(dp)
        if Text.contain(' ', dp) :
            dp = "'" + dp + "'"
            nd = "'" + nd + "'"
        if dp != nd :
            lines += f"mv -v {dp} {nd}\n"
            count += 1
    # １件もない場合はサブディレクトリを見てみる。
    if count == 0 :
        for dir1 in dirs :
            dirs1 = fs.listDirectories(dir1)
                for dir2 in dirs1 :
                    nd = rename(dp)
                    if Text.contain(' ', dp) :
                        dp = "'" + dp + "'"
                        nd = "'" + nd + "'"
                    if dp != nd :
                        lines += f"mv -v {dp} {nd}\n"
                        count += 1
    return lines

# 対象のディレクトリを得る。
if Common.count_args() < 2 :
    Common.stop(9, "対象のディレクトリとスクリプトファイルの保存先(パス)を指定してください。")

# 対象のディレクトリ
dir0 = Common.args()[0]
if not fs.isDirectory(dir0) :
    Common.stop(9, f"{dir0} はディレクトリとして存在しません。")

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
