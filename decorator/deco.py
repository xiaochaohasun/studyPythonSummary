#!/usr/bin/env python

import time

def deco(func):
    def timeit():
        start=time.time()
        ret_val=func()
        end=time.time()
        return ret_val,end-start
    return timeit


@deco
def loop():
    result=[]
    for i in range(1,11):
        result.append(i)
        time.sleep(0.3)

    return result

if __name__ == '__main__':
    print loop()