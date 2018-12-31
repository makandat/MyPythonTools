# https://github.com/makandat/gynoya/YJFX.git

## test
テストデータ用フォルダ

## AppConf.ini
MySQL への接続情報
    host=localhost
    uid=user
    pwd=ust62kjy
    db=user

## CREATE_YJFX_Settle.sql
YJFX_Settle テーブルの定義

## CreateTable_YJFX_ASSET.sql
YJFX_ASSET テーブルの定義

## ins_asset.rb
YJFX_ASSET テーブルにデータを挿入する。
使い方
  ruby ins_asset.rb 日付 資産 損益
    日付の例 '2018-12-31'

## ReadSettlement.py
YJFX_Settle テーブルにデータを挿入する。
使い方
  python3 ReadSettlement.py CSVファイル
    CSVファイルは期間取引照会で決済一覧をダウンロードしたものを UTF-8, LF に変換する。


## show_asset.rb
YJFX_ASSET テーブルの内容を表示する。
使い方
  ruby show_asset.rb

## ShowSettlement.py
YJFX_Settle テーブルの内容と損益の合計を表示する。
使い方
  python3 ShowSettlement.py

