#!/usr/bin/env python

class AddrBook(object):
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone


    def get_phone(self):
        return self.phone

    def update_phone(self,newph):
        self.phone=newph
        print '%s update phone number:%s' % (self.name,self.phone)



if __name__ == '__main__':
    bob=AddrBook('bob','1334567800')
    alice=AddrBook('alice','158202039302')
    print bob.get_phone()
    bob.update_phone('1508080080')
    print bob.get_phone()