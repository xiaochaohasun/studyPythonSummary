#!/usr/bin/env python

def count(start=0):
    counter=[start]
    def incr():
        counter[0] +=1
        return counter[0]

    return incr

if __name__ == '__main__':
    a=count()
    b=count(10)
    print a()
    print a()
    print b()
    print b()
    print a()
    print b()