#!/usr/bin/env python
# -*- coding: utf8 -*-

alist=['hello','world','greet']


#result:
# 0 hello
# 1 world
# 2 greet
#三种方式结果都一样
for i in range(len(alist)):
    print i,alist[i]


for element in enumerate(alist):
    print element[0],element[1]


for i,item in enumerate(alist):
    print i,item


#sorted
print(sorted(alist))

#result
#['greet', 'hello', 'world']



#reversed
for i in reversed(alist):
    print i,

#result
# greet world hello