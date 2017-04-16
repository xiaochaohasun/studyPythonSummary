#!/usr/bin/env python

def get_info(name,age):
    print '%s is %s years old.' % (name,age)

get_info('bob',23)
get_info(23,'bob')
get_info(age=23,name='bob')

#get_info(age=23,'bob')   #error
#get_info(age=23,name)    #error
#get_info(23,name='bob')  #error,name has mutiple args
get_info('bob',age=23)    #right,default keyword arg must be put it last.