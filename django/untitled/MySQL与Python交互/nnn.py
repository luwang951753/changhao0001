from changSql import ChangSql

c = ChangSql("localhost","root","123456","qq")
#SQL语句
sql = "select * from bandcard"
data = c.get_all(sql)
for row in data:
    print(row[0], row[1])













































































































































