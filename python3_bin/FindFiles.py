#!/usr/bin/env python3
#  ファイルで指定されたファイルをディレクトリから再帰的に見つける。
import sys, os, glob, json, re

#
#  main()
#  ======
def main() :
  # コマンドライン引数から対象ディレクトリを得る。
  path = "."
  if len(sys.argv) == 1 :
    print("使い方： python FindFiles.py 対象のディレクトリ\n")
    exit(9)
  else :
    path = sys.argv[1]
  # 設定ファイルを読む。
  file_templates = []
  with open("FindFiles.txt") as f :
    file_templates = f.readlines() 
  # 対象ディレクトリを再帰的にスキャンして、目的のファイルを表示する。
  scan(path, file_templates)
  return

#
#  対象ディレクトリを再帰的にスキャンして、目的のファイルを表示する。
#  scan(path, file_templates)
#
def scan(path, file_templates) :
  files = glob.glob(path + "/**/*", recursive=True)
  for f in files :
    pn = str(f).rstrip()
    fn = os.path.basename(pn)
    for p in file_templates :
      pattern = p.rstrip()
      if re.match(pattern, fn) != None :
        pfn = pn.replace("\\", "/")
        print(pfn)
      else :
        pass
  return

# 実行開始
main()
print("Done.")
