#!/usr/bin/env python

import re

class Counter(object):
    def __init__(self,fname):
        self.fname=fname

    def count_patt(self,patt):
        result={}
        cpatt = re.compile(patt)

        with open(self.fname) as fobj:
            for line in fobj:
                m = cpatt.search(line)
                if m:
                    key = m.group()
                    result[key] = result.get(key, 0) + 1

        return result

if __name__ == '__main__':
    log_file = 'access_log-20160717'
    ip = '^(\d+\.){3}\d+'
    br = 'Firefox|MSIE'
    c=Counter(log_file)
    print c.count_patt(ip)
    print c.count_patt(br)


