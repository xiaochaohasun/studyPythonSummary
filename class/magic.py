#!/usr/bin/env python

class Books(object):
    def __init__(self, tittle, author):
        self.tittle = tittle
        self.author = author

    # one way
    def __str__(self):
        return self.tittle

    # two way
    # def __repr__(self):
    #     return self.tittle

    def __call__(self):
        print '%s is written by %s .' % (self.tittle, self.author)


class Number(object):
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other

    def __radd__(self, other):
        return self.num + other

    def __sub__(self, other):  # __rsub__=-, __mul__=*, __div__ =/
        return self.num - other

    def __gt__(self, other):  # >
        return self.num > other


if __name__ == '__main__':
    py_book = Books('<Core python>', 'Wesley')
    print py_book
    py_book()

    a = Number(10)
    print a + 5
    print 5 + a
    print a - 5
    print a > 5
