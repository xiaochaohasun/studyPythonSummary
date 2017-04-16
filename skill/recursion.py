#!/usr/bin/env python

def recursion(num):
    if num ==1:
        return 1
    return num * recursion(num -1)

if __name__ == '__main__':
    print recursion(5)
    print recursion(10)


alist=[10,20,5,200]

def little():
    if len(alist)==1:
        return alist[0]
    a=alist[0] if alist[0] > alist[1] else alist[1]
    alist.remove(a)
    return little()

print little()
