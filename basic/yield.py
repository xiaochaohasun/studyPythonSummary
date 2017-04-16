#!/usr/bin/env python

def gen_block(fobj):
    lines=[]
    count=0
    for line in fobj:
        lines.append(line)
        count+=1
        if count ==10:
            yield lines
            lines=[]
            count=0
    if lines:
        yield lines


if __name__ == '__main__':
    fname='/etc/passwd'
    with open(fname) as fobj:
        for block in gen_block(fobj):
            print block