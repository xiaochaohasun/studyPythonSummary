#!/usr/bin/env python


class A(object):
    def get_name(self):
        print 'A'

    def pstar(self):
        print '*'* 20


class B(object):
    def display_name(self):
        print 'B'

    def pstar(self):
        print '#' * 20


class C1(A,B):
    pass


class C2(B,A):
    pass


if __name__ == '__main__':
    c1 =C1()
    c1.get_name()
    c1.display_name()
    c1.pstar()

    c2 =C2()
    c2.get_name()
    c2.display_name()
    c2.pstar()