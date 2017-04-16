#!/usr/bin/env python

class Myclass(object):
    def __init__(self,name):
        self.name=name

    def display_name(self):
        print self.name

if __name__ == '__main__':
    a=Myclass('bob')
    a.display_name()