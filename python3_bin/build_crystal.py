#!/usr/bin/python3
#  Crystal サンプルプログラムを一気にビルドする。
from Py365Lib import Common, Text, FileSystem as fs

# ソースのビルドが必要かチェックする。
def outfile_check(source, dest):
    if not fs.exists(dest):
        return True
    tdest = fs.getStat(dest).st_mtime
    tsource = fs.getStat(source).st_mtime
    if tdest < tsource:
        return True
    return False

# Main
def main():
    if Common.count_args() == 0:
      print("Usage: build_crystal dirpath\n")
      Common.stop(1)

    dirpath = Common.args(0)
    files = fs.listFiles(dirpath, "*.cr")
    outdir = dirpath + "/bin"
    if Common.is_windows():
        outdir = dirpath + "\\bin"
    for g in files:
        fname = Text.substr(g, 2, len(g) - 4)
        outfile = f"{outdir}/{fname}"
        if Common.is_windows():
            outfile = f"{outdir}\\{fname}"
        if outfile_check(g, outfile): # ビルドが必要か？
            cr = f"crystal build -o {outfile} -d {g}"
            print(cr)
            cmd = cr.split(" ")
            if Common.exec(cmd) == 0:
                print("OK")
            else:
                print("Failed.")
        else:
            print("Skipped: " + g)

# スタート
main()
