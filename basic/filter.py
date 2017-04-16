#!/usr/bin/env python

from random import randint

def func1(num):
    return num % 2

def func2(num):
    return num * 2

def func3(x,y):
    return x + y

if __name__ == '__main__':
    num_list=[randint(0,100) for i in range(10)]
    print num_list

    print filter(func1,num_list)
    print filter(lambda x : x % 2,num_list)

    print map(func2,num_list)
    print map(lambda x : x * 2,num_list)

    print reduce(func3,num_list)
    print reduce(lambda x,y : x+y ,num_list)