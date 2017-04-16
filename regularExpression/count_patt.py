#!/usr/bin/env python

import re


def count_patt(fname, patt):
    result = {}
    cpatt = re.compile(patt)

    with open(fname) as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:
                key = m.group()
                result[key] = result.get(key, 0) + 1

    return result


def sort(str_list):
    if len(str_list) ==0 or len(str_list) ==1:
        return str_list

    middle=str_list.pop()
    smaller=[]
    large=[]

    for item in str_list:
        if item[-1] < middle[-1]:
            smaller.append(item)
            continue
        large.append(item)

    return sort(large) + [middle] + sort(smaller)



if __name__ == '__main__':
    log_file = 'access_log-20160717'
    ip = '^(\d+\.){3}\d+'
    br = 'Firefox|MSIE'
    a= count_patt(log_file, ip)
    print a.items()
    print sort(a.items())
    # print count_patt(log_file, br)
