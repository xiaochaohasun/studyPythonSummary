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
sql8 = "insert into employees(emp_name, genda, phone, dep_id) values(%s, %s, %s, %s)"
data = ('bob', 'male', '15011223344', 3)
result = cur.execute(sql8, data)
print(result)
conn.commit()
cur.close()
conn.close()
