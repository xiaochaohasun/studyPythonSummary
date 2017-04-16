#!/usr/bin/env python

import socket

host=''
port=21567
addr=(host,port)

c=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    data = raw_input('> ')
    if data == '':
        break
    c.sendto(data+'\r\n',addr)

    print c.recvfrom(1024)[0]

c.close()