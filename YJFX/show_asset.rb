#!/usr/bin/ruby

require "mysql2"

# MySQL に接続
mysql = Mysql2::Client::new(:host=>'localhost', :username=>'user', :password=>'ust62kjy', :database=>'user')

sql = %(SELECT id, `date`, format(asset, 0) as ASSET, format(profit_loss, 0) as PROFIT, format(asset + profit_loss, 0) as EVAL_ASSET, info FROM YJFX_Asset ORDER BY id DESC LIMIT 100)
#puts sql
result = mysql.query(sql)

# 結果を表示する。
puts "id\tdate\t\tasset\t\tprofit\t\teval_asset\tinfo"
puts "----------------------------------------------------------------------------------"
result.each do |row|
  printf("%d\t%s\t%s\t%s\t%s\t%s\n", row['id'], row['date'].to_s(), row['ASSET'], row['PROFIT'], row['EVAL_ASSET'], row['info'])
end
puts "----------------------------------------------------------------------------------"

result.free()

# 終わり
puts "Done."
mysql.close()

