#!/usr/bin/env python

x =10

def func():
    global x
    x='hello'
    print x


func()
print x