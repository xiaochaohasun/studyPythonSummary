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
sql1 = "select dep_id, dep_name from departments"
cur.execute(sql1)
result = cur.fetchall()
print(result)
cur.close()
conn.close()
