import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='tedu.cn',
    db='tedu',
    charset='utf8'
)
cur = conn.cursor()
sql2 = "insert into departments(dep_name) values(%s)"
data = [('hr',), ('op',)]
result = cur.executemany(sql2, data)
print(result)
conn.commit()
cur.close()
conn.close()
