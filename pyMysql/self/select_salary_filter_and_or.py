#!/usr/bin/env python3

from db_connect import Salary,Employees,session
from sqlalchemy.orm import aliased
from sqlalchemy import and_,or_


sal=aliased(Salary)

for empid in session.query(sal.emp_id).filter(sal.basic > 10000).filter(sal.extra > 1000):
    print(empid)

print('-' * 50)
for empid in session.query(sal.emp_id).filter(sal.basic > 10000).filter(sal.extra > 1000):
    print(empid)

print('-' * 50)
for row in session.query(sal.emp_id,sal.basic,sal.extra).filter(and_(sal.basic > 10000,sal.extra > 2000)):
    print(row.emp_id)


print('-' * 50)
for row in session.query(sal.emp_id,sal.basic,sal.extra).filter(or_(sal.basic > 10000 ,sal.extra > 3000)):
    print(row.emp_id)

session.close()
