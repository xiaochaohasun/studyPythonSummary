# -*- coding:utf8 -*-
#!/usr/bin/env python

import os
import sys
import socket
import time
import threading


def work(cli_sock,cli_addr):
    while True:
            data = cli_sock.recv(1024)
            if data.strip() == '':
                cli_sock.close()
                break
            cli_sock.send("[%s] %s" % (time.ctime(), data))

if __name__ == "__main__" :
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    s.bind(('',21567))
    s.listen(1)
    try:
        while True:
            cli_sock,cli_addr = s.accept()
            t = threading.Thread(target=work,args=(cli_sock,cli_addr))
            t.setDaemon(True)
            t.start()
    except:
        s.close()