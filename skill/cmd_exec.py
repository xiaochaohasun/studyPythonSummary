#!/usr/bin/env python
# -*- coding: utf8 -*-

import subprocess

commands=[
    'mkdir /tmp/abc',
    'echo hello > /tmp/abc/myfile.txt',
    'cat /tmp/abc/myfile.txt'
]

def fun0():
    print '1st command is failed.'

def fun1():
    print '2nd command is failed.'


def fun2():
    print '3rd command is failed.'

fun_dict={'0':fun0,'1':fun1,'2':fun2}

for i in range(len(commands)):
    ret_val=subprocess.call(commands[i],shell=True)
    if ret_val != 0:
        fun_dict[i]()
        break