#!/usr/bin/python3
from Py365Lib import Common, FileSystem as fs, Text

#  pixiv_rename.py ver. 2.2
#    3桁の数字にも対応

# 指定されたフォルダの画像ファイルを同じ長さにリネームする。
def rename_files(folder) :
  # 画像ファイル一覧を得る。
  print(folder)
  files = fs.listFiles(folder, asstr=True)
  # 画像ファイルをリネーム
  for fpath in files :
    #fpath = Common.from_bytes(f)
    ext = fs.getExtension(fpath).lower()
    # 画像ファイルのみを対象にする。
    if ext == ".jpg" or ext == ".png" or ext == ".gif" :
      # ファイル名が nnnnnnn_pnn[.jpg] か
      fname = fs.getFileName(fpath)
      ff = Text.split("_", fname)
      if not (ext in ff[1]) :
        ff[1] += ext
      if len(ff) == 3 :
        # 3分割できて 'master' が含まれる場合は 'master..' 部分を削除する。
        #fname_old = fname
        fname = ff[0] + '_' + ff[1]
        #print(fname_old + " to " + fname) 
      elif len(ff) != 2 :
        # _ で2分割できない場合(ファイル名の形式が異なる場合)はスキップする。
        print("Skipped " + fname)
        continue
      else :
        # その他の場合は何もしない。(2分割できた場合)
        pass
      # 連続番号部分の形式を確認する。
      sf = ff[1]
      if ff[1].startswith('p') :
        if len(ff[1]) == 6 or (len(ff) == 3 and len(ff[1]) == 2) :
          # 連続番号が1桁の場合
          sf = "p0" + Text.substring(ff[1], 1)
          newname = folder + "/" + ff[0] + "_" + sf
          fs.move(fpath, newname)
          print("Renamed: " + newname)
        elif len(ff) == 3 and len(ff[1]) == 7 :
          # _master1200 があり連続番号が2桁の場合
          newname = folder + "/" + fname
          fs.move(fpath, newname)
        elif len(ff[1]) == 8 or (len(ff) == 3 and len(ff[1]) == 4) :
          # 連続番号が3桁または連続番号が3桁かつ _master1200 がある場合
          sn = Text.substring(ff[1], 1)
          if sn == '1' :
            # 連続番号が3桁かつ100番台の場合
            sf = "q" + Text.substring(ff[1], 2)
            newname = folder + "/" + ff[0] + "_" + sf
            fs.move(fpath, newname)
            print("Renamed: " + newname)
          elif sn == '2' :
            # 連続番号が3桁かつ200番台の場合
            sf = "r" + Text.substring(ff[1], 2)
            newname = folder + "/" + ff[0] + "_" + sf
            fs.move(fpath, newname)
            print("Renamed: " + newname)
          else :
            # 連続番号が3桁かつ300番台以上の場合はサポートしない(スキップする)
            pass
        else :
          # 連続番号が2桁の場合 
          #print("Passed: " + fpath)
          pass
    else :
      #fs.move(fpath, fpath + ".jpg")
      print("Non image passed: " + fpath)
  return  

#  スタート
if Common.count_args() == 0 :
  folder = Common.readline("対象の画像フォルダを入力します。")
else :
  folder = Common.args(0)

if not fs.isDirectory(folder) :
  Common.stop(1, folder + " は正しいディレクトリではありません。")

# 指定されたフォルダの画像ファイルを同じ長さにリネームする。
rename_files(folder)

print("正常終了。")
