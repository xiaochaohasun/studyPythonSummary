#!/usr/bin/env python3

from db_connect import Employees,session
from sqlalchemy.orm import aliased

new_emp=aliased(Employees)

for name,phone in session.query(Employees.name,Employees.phone):
    print(name,phone)

print('-'* 50)
for name,phone in session.query(new_emp.name,new_emp.phone):
    print(name,phone)

print('-'* 50)
for name,phone in session.query(new_emp.name,new_emp.phone).filter(new_emp.name=='john'):
    print(name,phone)


print('-'* 50)
for name,phone in session.query(new_emp.name,new_emp.phone).filter(new_emp.name!='john'):
    print(name,phone)


print('-'* 50)
for name,phone in session.query(new_emp.name,new_emp.phone).filter(new_emp.name.like('j%')):
    print(name,phone)

print('-'* 50)
for name,phone in session.query(new_emp.name,new_emp.phone).filter(new_emp.name.in_(['bob','john'])):
    print(name,phone)

print('-'* 50)
for name,phone in session.query(new_emp.name,new_emp.phone).filter(~new_emp.name.in_(['bob','john'])):
    print(name,phone)

print('-'* 50)
for name,phone in session.query(new_emp.name,new_emp.phone).filter(new_emp.name.is_(None)):
    print(name,phone)

print('-'* 50)
for name,phone in session.query(new_emp.name,new_emp.phone).filter(new_emp.name.isnot(None)):
    print(name,phone)



session.close()