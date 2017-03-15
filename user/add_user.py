#!/usr/bin/env python
# -*- coding: utf8 -*-

import string
import sys
import subprocess
import randpass2

contents = '''userinfo:
user:${username}
password=${password}
'''
tmlate = string.Template(contents)


def add_user(username, pwd, user_file):
    subprocess.call('useradd %s' % username, shell=True)
    subprocess.call(
        'echo %s | passwd --stdin %s' % (pwd, username), shell=True
    )

    fobj = open(user_file, 'a')  # append
    fobj.write(tmlate.substitute(username=username, password=pwd))
    fobj.close()


if __name__ == '__main__':
    pwd = randpass2.gen_pass()
    user_file = '/tmp/users.txt'
    add_user(sys.argv[1], pwd, user_file)
