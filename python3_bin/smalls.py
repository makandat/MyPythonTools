#!/usr/bin/env python3
#  Pillow/smalls.py v.1.4.1
from PIL import Image, ImageFilter
from Py365Lib import Common, FileSystem as fs

# 縮小画像のサイズを計算する。
def getImageSize(im) :
  imgw = im.size[0]
  imgh = im.size[1]
  if imgw > imgh:
    # 横長の時
    nw = SIZE
    nh = SIZE * imgh // imgw
  else:
    # 縦長の時
    nw = SIZE * imgw // imgh
    nh = SIZE
  return (nw, nh)

# *************************************************
# この値が縮小画像のデフォルトサイズになる。
SIZE = 1600
#SIZE = 1920
#SIZE = 2560
# 縮小画像ファイルのデフォルト保存先
SAVEPATH = 'C:/Temp/small/'
# True なら JPEG で保存
JPEG = True
# *************************************************

# ここから開始
if Common.count_args() == 0 :
  print("画像縮小専用 Usage: python smalls.py folder size save_path")
  folder = Common.readline("画像ファイルの存在するフォルダパスを入力します。(Enter のみで中止。ファイルサイズと保存先はデフォルト値)> ")
  if folder == "" :
    Common.stop("処理を中止しました。")
else :
  folder = Common.args(0)
  if Common.count_args() >= 2 :
    SIZE = int(Common.args(1))
  if Common.count_args() >= 3 :
    SAVEPATH = Common.args(2)

# 指定されたフォルダ内の画像ファイル一覧を得る。
files = fs.listFiles(folder)

a = Common.readline(f"{len(files)} 個のファイルを {SIZE} x {SIZE} 以内に縮小して {SAVEPATH} に保存します。(y/n)")
if a != 'y':
  Common.stop(9, "処理を中断しました。")

if not fs.exists(SAVEPATH):
  fs.mkdir(SAVEPATH)

i = 0
for f in files:
  #fn = f.decode()
  fn = f
  ext = fs.getExtension(fn)
  if (ext == ".jpg" or ext == ".png"):
    #print(fn)
    im = Image.open(fn)
    #print(im.format, im.size, im.mode)
    im = im.convert('RGB')
    newsize = getImageSize(im)
    if im.size[0] > newsize[0] or im.size[1] > newsize[1] :
      newim = im.resize(newsize)
    else:
      newim = im
    newPath = SAVEPATH + fs.getFileName(fn)
    if JPEG:
      newPath = newPath.replace(".png", ".jpg")
    newim.save(newPath)
    i += 1
    print(f"{newPath} に {i} 個目のファイルを保存しました。")
  else:
    print(f"{fn} をスキップしました。")
