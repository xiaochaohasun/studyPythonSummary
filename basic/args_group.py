#!/usr/bin/env python

def get_args(*args):   #tuple
    print args

#result
# ()
# ('abc',)
# (10, 20, 30)


def get_kwargs(**kwargs):  #dict
    print kwargs

#result
# {}
# {'age': 23, 'name': 'bob'}


def get_info(name,age):
    print '%s is %s years old.' % (name,age)

if __name__ == '__main__':
    get_args()
    get_args('abc')
    get_args(10,20,30)

    get_kwargs()
    get_kwargs(name='bob',age=23)
    info = ['bob','25']
    get_info(*info)
    info_dict={'name':'bob','age':23}
    get_info(**info_dict)