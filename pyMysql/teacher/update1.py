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
sql1 = "update departments set dep_name=%s where dep_name=%s"
result = cur.execute(sql1, ('operations', 'op'))
print(result)
conn.commit()
cur.close()
conn.close()
