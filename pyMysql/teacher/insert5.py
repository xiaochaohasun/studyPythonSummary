import pymysql
import time

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='tedu.cn',
    db='tedu',
    charset='utf8'
)
cur = conn.cursor()
sql9 = "insert into salary(date, emp_id, basic, extra) values(%s, %s, %s, %s)"
data = (time.strftime('%Y-%m-%d'), 1, 10000, 5000)
result = cur.execute(sql9, data)
print(result)
conn.commit()
cur.close()
conn.close()
