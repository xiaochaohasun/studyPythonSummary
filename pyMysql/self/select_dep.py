#!/usr/bin/env python3

from db_connect import Departments,session
from sqlalchemy.orm import aliased


new_dep=aliased(Departments)

for instance in session.query(Departments).order_by(Departments.dep_id):
    print(instance.dep_id,instance.dep_name)



for instance in session.query(Departments.dep_name.label('部门')):
    print(instance.部门)



for dep_id,dep_name in session.query(new_dep.dep_id,new_dep.dep_name).\
    order_by(new_dep.dep_id):
    print(dep_id,dep_name)


for dep_id,dep_name in session.query(new_dep.dep_id,new_dep.dep_name).\
    order_by(new_dep.dep_id)[0:2]:
    print(dep_id,dep_name)

session.close()
