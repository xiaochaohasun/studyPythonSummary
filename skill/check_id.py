#!/usr/bin/env python
# -*- coding: utf8 -*-

import string

first_chas = string.letters + '_'
other_chas = first_chas + string.digits


def check_id(idt):
    if idt[0] not in first_chas:
        return '1st char invalid.'
    for ind, ch in enumerate(idt[1:]):
        if ch not in other_chas:
            return 'position %s:%s is invalid' % (ind + 2, ch)

    return '%s is valid.' % idt


if __name__ == '__main__':
    idt = raw_input('identifier:')
    print check_id(idt)
