#!/usr/bin/env python3
#  BINDATA バイナリファイル index.cgi
import WebPage as cgi
import Text as text
import MySQL as mysql
import FileSystem as fs

SELECT = "SELECT id, title, original, datatype, ISNULL(data) as nulldata, info FROM Binaries"


# ページクラス
class BinDataPage(cgi.WebPage) :
  # コンストラクタ
  def __init__(self, template="") :
    super().__init__(template)
    self.__mysql = mysql.MySQL()
    self.vars['images'] = ""
    if self.isParam('filter') :
      filter = self.getParam('filter')
      if filter == "image" :
        where = " WHERE datatype='.jpg' OR datatype='.png' OR datatype='.gif'"
        self.vars['content'] = self.getContent(where)
      elif filter == "audio" :
        where = " WHERE datatype='.wav' OR datatype='.mp4' OR datatype='.m4a'"
        self.vars['content'] = self.getContent(where)
      elif filter == "zip" :
        where = " WHERE datatype='.zip' OR datatype='.gz' OR datatype='.bz2'"
        self.vars['content'] = self.getContent(where)
      else :
        self.vars['content'] = "<tr><td>不正なパラメータ</td></tr>"
    else :
      self.vars['content'] = self.getContent()
    return

  # Binaries テーブルの内容一覧を得る。
  def getContent(self, where="") :
    buff = ""
    sql = SELECT + where
    rows = self.__mysql.query(sql)
    if len(rows) == 0 :
      self.vars['message'] = 'データがありません。(件数が0)'
    else :
      for row in rows :
        buff += cgi.WebPage.table_row(row)
        buff += "\n"
    filter = self.getParam('filter')
    if filter == 'image' :
      self.vars['images'] = self.getImages(rows)
    return buff

  # 画像を表示する。
  def getImages(self, rows) :
    buff = ""
    for row in rows :
      id = row[0]
      title = row[1]
      buff += "<li><figure>"
      buff += f"<img src=\"image.cgi?id={id}\" />"
      buff += f"<figcaption>{title}</figcaption></figure></li>\n"
    return buff



# 応答をクライアントへ返す。
wp = BinDataPage('templates/index.html')
wp.echo()
