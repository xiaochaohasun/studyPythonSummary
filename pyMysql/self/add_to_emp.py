#!/usr/bin/env python

from db_connect import Employees,session


bob = Employees(name='bob', genda='male', phone='13312345678', dep_id=1)
alice = Employees(name='alice', genda='female', phone='13422556677', dep_id=4)
john = Employees(name='john', genda='male', phone='13488990066', dep_id=5)
jack = Employees(name='jack', genda='male', phone='15011223355', dep_id=5)
session.add_all([bob, alice, john, jack])
session.commit()
session.close()