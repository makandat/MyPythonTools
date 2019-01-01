#!/usr/bin/env python3
#  Pictures ディレクトリ内のサブ・ディレクトリを Pictures テーブルに登録する。
#  (登録済みのディレクトリは、二重登録しない)
#  表示される SQL をリダイレクトしてファイル保存して実行すること。
'''
USE user
CREATE TABLE `Pictures` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `TITLE` varchar(50) NOT NULL,
  `CREATOR` varchar(50) NOT NULL,
  `PATH` varchar(500) NOT NULL,
  `MARK` varchar(10) DEFAULT NULL,
  `INFO` varchar(100) DEFAULT NULL,
  `FAV` char(1) DEFAULT '0',
  `COUNT` int(8) DEFAULT '0',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=279 DEFAULT CHARSET=utf8;
'''


from Py365Lib import MySQL, Common, Text, FileSystem as fs

# サブディレクトリを検索して、Pictures テーブルに登録する。
def insertFolders(parentDir) :
  dirs = fs.listDirectories(parentDir)
  for dir in dirs :
    # 作者名
    parts = Text.split("/", dir)
    creator = parts[len(parts) - 1]
    # 作品名s
    subdirs = fs.listDirectories(dir)
    if len(subdirs) == 0 :
      p = Text.split(' ', creator)
      creator = p[0]
      insertData(dir, creator)
    else :
      for subdir in subdirs :
        insertData(subdir, creator)
  return



# データをMySQLに挿入する。
def insertData(dir, creator) :
  global mark
  global cmd
  parts = Text.split('/', dir)
  title = parts[len(parts) - 1]
  cmd = f"INSERT INTO Pictures(TITLE, CREATOR, `PATH`, MARK) VALUES('{title}', '{creator}', '{dir}', '{mark}');"
  print(cmd)
  return


## プログラム開始
if Common.count_args() == 0 :
  Common.stop(1, "親ディレクトリを指定してください。", Common.ESC_FG_YELLOW)

cmd = ""
mark = 'NONE'

parentDir = Common.args()[0]
if Common.count_args() > 1 :
  mark = Common.args()[1]
insertFolders(parentDir)
