#!/usr/bin/env python

from random import randint

def quick_sort(num_list):
    num_len=len(num_list)
    if num_len ==0 or num_len ==1:
        return num_list

    middle=num_list.pop()
    smaller=[]
    larger=[]

    for num in num_list:
        if num < middle:
            smaller.append(num)
            continue
        larger.append(num)
    return quick_sort(smaller) + [middle] + quick_sort(larger)

if __name__ == '__main__':
    nums=[randint(1,100) for i in range(10)]
    print nums
    print quick_sort(nums)