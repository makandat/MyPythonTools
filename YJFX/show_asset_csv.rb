#!/usr/bin/ruby

require "mysql2"

# MySQL に接続
mysql = Mysql2::Client::new(:host=>'localhost', :username=>'user', :password=>'ust62kjy', :database=>'user')

sql = %(SELECT id, `date`, asset as ASSET, profit_loss as PROFIT, info FROM YJFX_Asset ORDER BY `date`)
#puts sql
result = mysql.query(sql)

# 結果を表示する。
result.each do |row|
  printf("%s\t%s\t%s\t%s\n", row['date'].to_s(), row['ASSET'], row['PROFIT'], row['info'])
end
result.free()

# 終わり
mysql.close()

