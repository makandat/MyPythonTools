#!/usr/bin/env python3

#  ファイル一覧を Videos テーブルへインポートでするための SQL を出力する。
#  (注意) ファイル一覧は UTF-8、json ファイルは SJIS で作成する。
#  json ファイルの例
'''
{
  "album":165
  "media":"HD-LLU3",
  "series":"アニソン",
  "mark":"アニメ",
  "info":""
}
'''
from Py365Lib import Common, FileSystem as fs, MySQL

# START
# パラメータ確認
if Common.count_args() < 1 :
  Common.stop("Usage : Ins_VideosSQL.py filelist [json]")
filelist = Common.args(0)
album = 0
media = "media"
series = "series"
mark = "mark"
info = "info"
if Common.count_args() >= 2 :
  json = fs.readJson(Common.args(1))
  album = json["album"]
  media = json["media"]
  series = json["series"]
  mark = json["mark"]
  info = json["info"]
else :
  pass

#  ファイルリストを読む。
filename = "insert.sql"
lines = fs.readLines(filelist)
firstdata = True
sql = ""
#with open(filename, mode="w", encoding='utf_8_sig') as f :
with open(filename, mode="w", encoding='shift_jis') as f :
  f.write("INSERT INTO Videos VALUES\n")
  for path in lines :
    if firstdata :
      firstdata = False
    else :
      f.write(sql + ",\n")
    path = path.strip().replace("'", "''").replace('\\', '/')
    print(path)
    title = fs.getFileName(path)
    ext = fs.getExtension(path)
    title = title.replace(ext, "")
    sql = f"(NULL, {album}, '{title}', '{path}', '{media}', '{series}', '{mark}', '{info}', 0, 0, 0, 0, NULL)"
  f.write(sql + ";\n")
print("Done.")

