#!/usr/bin/env python

import addressbook
class EmplAddrBook(addressbook.AddrBook):
    def __init__(self,name,phone,email):
        # addressbook.AddrBook.__init__(self,name,phone)    #one way
        super(EmplAddrBook,self).__init__(name,phone)       #two way
        self.email=email

    def get_email(self):
        return self.email



if __name__ == '__main__':
    tom=EmplAddrBook('tom Green','13290909009','tom@qq.com')
    print tom.get_phone()
    print tom.get_email()