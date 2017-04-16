#!/usr/bin/env python3

from db_connect import Departments,session

dep_hr = Departments(dep_name='hr')
dep_op = Departments(dep_name='op')
dep_finance = Departments(dep_name='财务')
dep_xz = Departments(dep_name='行政')

session.add_all([dep_hr,dep_op,dep_finance,dep_xz])
session.commit()
session.close()