#!/usr/bin/env python
# -*- coding: utf8 -*-

'''print 30 *

This module of program is show-how a hide attributer of modules __name__ how to use .
'''

hi='hello world'
hello='welcome'

def pstar(n=30):
    return '*' * n


#主动执行时候属性__name__的值为__main__，
# 当使用import在别的文件引入时，该属性的值为文件名modules_import,使用场景为当引入某个写好的文件时候，不会直接打印
if __name__ == '__main__':       #输入main,按下tab-快捷方式
    print pstar()
    print hi,hello
