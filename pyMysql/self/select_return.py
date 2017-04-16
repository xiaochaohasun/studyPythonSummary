#!/usr/bin/env python3

from sqlalchemy.orm import sessionmaker,aliased
from db_connect import Employees,session

new_emp=aliased(Employees)

query=session.query(new_emp.name,new_emp.phone).order_by(new_emp.emp_id)
# print(query)
# print(query.all())
# print(query.first())
# print(query.one())


query2=session.query(new_emp.name,new_emp.phone).filter(new_emp.emp_id=='4')
print(query2.one())
print(query2.scalar())


query3=session.query(new_emp.name,new_emp.phone).filter(new_emp.emp_id=='5')
print(query3.count())