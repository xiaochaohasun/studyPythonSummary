#!/usr/bin/env python
# -*- coding: utf8 -*-

#example 1

def gen_fibs():
    fibs = [0, 1]

    user = int(raw_input('please input a fibs num:'))

    for i in xrange(user - 2):
        fibs.append(fibs[-1] + fibs[-2])

    return fibs

print gen_fibs()

#将输出写入文件
fib_list=gen_fibs()
f=open('/tmp/fibs.txt','w')
f.write(str(fib_list))
f.close()


#example 2

#带参数
# def gen_fibs(num):
#     fibs = [0, 1]
#
#     for i in xrange(num - 2):
#         fibs.append(fibs[-1] + fibs[-2])
#
#     return fibs
#
# #读取用户输入参数
# num=raw_input('number:')
# print gen_fibs(num)
#
#
# #从文件中读取参数
# f=open('/tmp/number.txt')  #echo -n 30 > /tmp/number.txt
# num2=int(f.read())
#
# fib_list=gen_fibs(num2)
# f=open('/tmp/fibs.txt','w')
# f.write(str(fib_list))
# f.close()
