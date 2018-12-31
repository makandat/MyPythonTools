"# gyunoya" 

# YJFX
YJFX 約定履歴を MySQL に読み込む。読み込み先は下のテーブル。
<br />
>    CREATE TABLE `YJFX_Settle` (<br />
>      `id` decimal(16,0) NOT NULL,<br />
>      `CurrencyPair` char(7) NOT NULL,<br />
>      `Sell` char(1) NOT NULL DEFAULT '0',<br />
>      `price1` decimal(11,2) NOT NULL,<br />
>      `Date1` datetime NOT NULL,<br />
>      `price2` decimal(11,2) NOT NULL,<br />
>      `Date2` datetime NOT NULL,<br />
>      `Benefit` decimal(10,0) DEFAULT NULL,<br />
>      PRIMARY KEY (`id`)<br />
>    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;<br />
<br />
約定履歴のコードは SJIS なので、読み込み前に UTF-8 に変換しておく。<br />

使い方
> $ ReadSettlement.py trade_history.csv
<br />
YJFX_Settle の内容を表示するには、ShowSettlement.py を使用する。
<br />
約定履歴ファイルは、次のような感じである。
<br />
>	注文番号,新規決済,通貨ペア,売買,約定価格,注文数量,注文日時,約定日時,新規注文番号,新規約定価格,売買損益,決済手数料<br />
>	10621787349,決済,ドル/円,売,113.600,10000,2018/11/27 19:04:49,2018/11/27 21:04:34,10620136938,112.45,11500,<br />
>	10621787142,決済,ユーロ/円,売,128.700,10000,2018/11/27 19:04:06,2018/11/27 19:20:07,10621228202,127.9,8000,<br />
>	10621408997,決済,ドル/円,売,113.400,10000,2018/11/26 15:58:01,2018/11/26 23:25:25,10620020030,112.796,6040,<br />
>	10620713793,決済,ユーロ/円,売,129.012,10000,2018/11/21 21:59:40,2018/11/21 21:59:40,10620350250,128.1,9120,<br />


# showa
* age.py   年齢から誕生年を表示する。
* gtos.py  元号から西暦に変換する。
* stog.py  西暦から元号に変換する。
<br />
  詳細は showa/README.txt 参照<br />


# RENAME
## RenameDirs.py
  指定したディレクトリに含まれるサブディレクトリに "[", "]" が含まれていたら "(", ")" に、"#" が含まれていたら "_" に、<br />
  "'" が含まれていたら "" に置き換えるような mv コマンド(複数)からなるシェルスクリプトを生成する。<br />

## RenameNumber.py
  指定したディレクトリに含まれるファイルの名前を先頭から順に \w\d+\.\w に変更する。<br />
###  指定できるパラメータ<br />
*    ディレクトリ(最後の/は付けない)
*    ファイルのワイルドカード(すべての場合は'*.*'。必ず引用符で囲むこと。)
*    ファイル名の固定部分(英字のみ)
*    数字部分の桁数

## RenameExt.py
  指定したディレクトリに含まれるファイルの拡張子を変更する。
###  指定できるパラメータ
*    ディレクトリ
*    変更前の拡張子
*    変更後の拡張子

# BANKS

## Ins_Banks.py
　下のような BANKS テーブルにデータを挿入する。<br />
　コマンド引数は、銀行コード、残高、口座種別(省略可能)<br />
　　　銀行コードの例  三井住友銀行 0009, 武蔵野銀行: 0133, 住信SBIネット銀行: 0013<br />
　　　口座種別　0=普通 1=外貨 2=定期 3=定期(USD)　デフォルトは 0。<br />

    CREATE TABLE BANKS (
     ID INT NOT NULL AUTO_INCREMENT,
     DAY CHAR(10) NOT NULL, 
     BANK VARCHAR(20) NOT NULL,
     DEPOSIT CHAR(1) NOT NULL DEFAULT '0',
     BALANCE DECIMAL NOT NULL, 
     INFO VARCHAR(50),
     PRIMARY KEY(ID)
    ) CHARACTER SET=UTF8;


## show_balance.py
　BANKS テーブルの内容を表示する。<br />

