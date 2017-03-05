#!/usr/bin/env python
# -*- coding: utf8 -*-

'''generate random character

this module include a function and a global varable.

The module of program is default generate a 8 digit number passworld ,
The modules according to you requests print result when you input a digit number.
'''


from random import choice
import string
import sys

all_chs = string.letters + string.digits


def gen_pass(n=8):
    result = ''
    for i in xrange(n):
        result += choice(all_chs)
    return result


if __name__ == '__main__':
    print gen_pass()
    print gen_pass(4)
