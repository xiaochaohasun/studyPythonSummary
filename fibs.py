#!/usr/bin/env python
# -*- coding: utf8 -*-

fibs = [0, 1]

user = int(raw_input('please input a fibs num:'))

for i in xrange(user - 2):
    fibs.append(fibs[-1] + fibs[-2])

print fibs
