# BANKS README.txt

## AppConf.ini
MySQL の接続情報

    host=localhost
    uid=user
    pwd=ust62kjy
    db=user



## CREATE_VIEW_BALANCE.sql
日ごとの残高表示 View "vw_balance" の定義

## CreateTable_BANKS.sql
預金残高テーブル "BANKS" の定義

## Ins_Banks.py
BANKS テーブルに残高を登録する。
使い方
  python3 Ins_Banks.py 銀行コード 残高 (省略可能)口座種別

  銀行コードの例
    三井住友銀行
    住信SBI銀行
    武蔵野銀行

  (省略可能)口座種別
    普通       0 (デフォルト)
    外貨(USD)  1
    円定期     2
    ドル定期   3

## show_balance.py
残高一覧を表示する (ビュー vw_balance 表示)。
使い方
  python3 show_balance.py


