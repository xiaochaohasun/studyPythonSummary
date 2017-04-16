#!/usr/bin/env python3

from db_connect import Departments,session



dep_dev = Departments(dep_name='developments')
print(dep_dev.dep_name)
print(dep_dev.dep_id)

session.add(dep_dev)
session.commit()
print(dep_dev.dep_id)
session.close()