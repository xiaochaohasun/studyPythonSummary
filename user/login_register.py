#!/usr/bin/env python
# -*- coding: utf8 -*-

import  getpass

users_dict={}

def register():
    user=raw_input('plase input name:').strip()
    if user not in users_dict:
        passwd=raw_input('please intut password:').strip()
        users_dict[user]=passwd
    else:
        print 'user %s already exists.' % user

def login():
    username=raw_input('please input your name:')
    password=getpass.getpass('please input your name:')
    # if username in users_dict and users_dict[username]==password:
    if users_dict.get(username)==password:
            print 'Login successful.'
    else:
        print 'Loing incorrect!'
def ask_action():
    cmds = {'0': register, '1': login}
    prompt = '''(0)register user
(1)login
(2)exit
please input your choice(0/1/2):'''
    while True:
        choice = raw_input(prompt).strip()[0]
        if choice not in '012':
            print 'Invalid choice,Try again.'
            continue
        if choice == '2':
            break
        cmds[choice]()


if __name__ == '__main__':
    ask_action()
