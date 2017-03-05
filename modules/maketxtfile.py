#!/usr/bin/env python
# -*- coding: utf8 -*-

'''according to user input make a file

'''
import os


def get_fname():
    while True:
        fname = raw_input('please input file name of full path:')
        if not os.path.exists(fname):
            break
        print '%s already exists.Try another.' % fname

    return fname


def get_content():
    content = []
    while True:
        line = raw_input('(enter to quit)>:')
        if line == '':
            break
        content.append(line+'\n')

    return content


def write_file(fname, content):
    fobj = open(fname, 'w')
    fobj.writelines(content)
    fobj.close()


def main():
    fname = get_fname()
    content = get_content()
    #data=['%s\n' % line for line in content]
    write_file(fname, content)


if __name__ == '__main__':
    main()

