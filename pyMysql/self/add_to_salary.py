#!/usr/bin/env python3

from db_connect import Salary,session
from datetime import date


date1=date(2017,1,1)
date2=date(2017,2,2)

bob1 = Salary(date=date1, emp_id=1, basic=10000, extra=3000)
bob2 = Salary(date=date2, emp_id=1, basic=10000, extra=4000)
alice1 = Salary(date=date1, emp_id=2, basic=6000, extra=2000)
alice2 =Salary(date=date2, emp_id=2, basic=6000, extra=3000)
john1 = Salary(date=date1, emp_id=3, basic=12000, extra=1000)
john2 = Salary(date=date2, emp_id=3, basic=12000, extra=2000)
jack1 = Salary(date=date1, emp_id=4, basic=11000, extra=1000)
jack2 = Salary(date=date2, emp_id=4, basic=11000, extra=2000)

session.add_all([bob1, bob2, alice1, alice2, john1, john2, jack1, jack2])
session.commit()
session.close()
