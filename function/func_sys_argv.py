#!/usr/bin/env python
# -*- coding: utf8 -*-

"""cp /bin/ls command to /root/ls
   file read and write method how to use
"""

import sys


def copy_command(src_fname,dst_fname):

    src_fobj=open(src_fname)
    dst_fobj=open(dst_fname,'w')

    while True:
        data=src_fobj.read(4096)     #一般系统默认分区后的默认block都是4096字节=4k
        # if len(data) == 0:       #读取指针读取到最后，再次读取就为空
        # if not data:             #空字符串值为False
        if data == '':
            break
        dst_fobj.write(data)

    #关闭并释放资源
    src_fobj.close()
    dst_fobj.close()

copy_command(sys.argv[1],sys.argv[2])

