CREATE VIEW vw_balance AS select day,sum(balance) as balance from BANKS group by day;
