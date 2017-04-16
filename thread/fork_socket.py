# -*- coding:utf8 -*-
#!/usr/bin/env python

import os
import sys
import socket
import time

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(('',21567))
s.listen()

while True:
    cli_sock,cli_addr = s.accept()
    pid = os.fork()
    if pid:
        cli_sock.close()
        while True:
            result = os.waitpid(-1, os.WNOHANG)
            if result[0] == 0:
                break
    else:
        s.close()
        while True:
            data = cli_sock.recv(1024)
            if data.strip() == '':
                cli_sock.close()
                sys.exit(0)
            cli_sock.send("[%s] %s" % (time.ctime(), data))

s.close()