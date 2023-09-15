#!/usr/bin/env python3
#  CGI インタプリタ設定 v1.2
from Py365Lib import Common, FileSystem as fs, Text

INTERPRETERS = '''1: /usr/bin/env python3
2: D:/python311/python.exe
3: C:/perl/perl.exe
4: D:/Ruby32-x64/bin/ruby.exe
9: Quit
'''

# ファイルにインタプリタを適用する。
def apply(fileName, interpreter) :
    lines = fs.readLines(fileName)
    if lines[0].startswith('#!') :
        lines[0] = "#!" + interpreter + "\n"
        fs.writeLines(fileName, lines)
    else :
        print("Skiped: 行の先頭にインタプリタ指定が見当たりません。" + fileName)
    return

# 条件入力
fileName = ""
interpreterNo = 1
if Common.count_args() == 0 :
    fileName = Common.readline("対象のファイル・フォルダを指定してください。> ")
    print(INTERPRETERS)
    interpreterNo = Common.readline("番号を選択してください。> ")
else :
    fileName = Common.args(0)
    if Common.count_args() > 1:
       interpreterNo = Common.args(1)
    else:
      print(INTERPRETERS)
      interpreterNo = Common.readline("番号を選択してください。> ")
if interpreterNo == "9":
    print("処理が取り消されました。")
    exit(1)
interpreterLines = INTERPRETERS.split('\n')
interpreter = Text.substring(interpreterLines[int(interpreterNo) - 1], 3)
print(interpreter + " が " + fileName + " に適用されます。")
a = Common.readline("実行しますか？ (y/n)")
if a != 'y' :
    Common.stop(9, "実行が取り消されました。")

# インタプリタ適用
if fs.isFile(fileName) :
    apply(fileName, interpreter)
else :
    files = fs.listFiles2(fileName)
    for f in files :
        print(f)
        ext = fs.getExtension(f)
        if ext == ".cgi" :
            apply(f, interpreter)
        else :
            print("Skipped")
        # end if
    # end for

print("正常終了。")
