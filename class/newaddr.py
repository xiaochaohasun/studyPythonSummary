#!/usr/bin/env python

class Userinfo(object):
    def __init__(self,phone,email):
        self.phone=phone
        self.email=email


    def get_phone(self):
        return self.phone

    def update_phone(self,newph):
        self.phone=newph


    def get_email(self):
        return self.email

    def update_email(self,newem):
        self.email=newem

class AddrBook(object):
    def __init__(self,name,phone,email):
        self.name=name
        self.info=Userinfo(phone,email)


if __name__ == '__main__':
    bob=AddrBook('bob','1334567800','bob@qq.com')
    print bob.info.get_phone()
    bob.info.update_email('bob@tedu.cn')
    print bob.info.get_email()