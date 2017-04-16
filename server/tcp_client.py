#!/usr/bin/env python


import socket

host='127.0.0.1'
port=21567
addr=(host,port)


c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect(addr)

while True:
    try:
        data=raw_input('> ')
    except (KeyboardInterrupt,EOFError,socket.error):
        print '\nBye-bye'
        break

    c.send(data+'\r\n')

    print c.recv(1024)