#!/usr/bin/ruby

require "mysql2"

# パラメータチェック
if ARGV.size() == 0 then
  puts'ERROR: No paramaters'
  puts 'Usage: ins_asset date asset profit'
  exit(9)
end

# MySQL に接続
mysql = Mysql2::Client::new(:host=>'localhost', :username=>'user', :password=>'ust62kjy', :database=>'user')


# 指定した日がすでに登録されているか？
sql = %(SELECT COUNT(*) AS CT FROM YJFX_Asset WHERE `date` = '#{ARGV[0]}')

# puts sql

result = mysql.query(sql)

if result.first['CT'] > 0 then
  puts "ERROR: This day already exists."
  exit(8)
end

result.free()


# データを挿入する。
sql = %{INSERT INTO YJFX_Asset(`date`,asset,profit_loss) VALUES('#{ARGV[0]}', #{ARGV[1]}, #{ARGV[2]})}

# puts sql

begin
  result = mysql.query(sql)
  puts "OK"
rescue
  puts "FATAL ERROR: Failed to insert data."
end

# 終わり
mysql.close
print "Done.\n"

