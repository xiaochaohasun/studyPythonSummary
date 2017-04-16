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
sql1 = "delete from departments where dep_id=%s"
result = cur.execute(sql1, (6,))
print(result)
conn.commit()
cur.close()
conn.close()
