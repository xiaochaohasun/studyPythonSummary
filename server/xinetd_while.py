#!/usr/bin/env python
import  sys
import time

print 'Welcome.'
while True:
    print 'Please enter a string:'
    sys.stdout.flush()
    line=sys.stdin.readline().strip()
    if len(line) == 0:
        break
    print 'you enterd %s  has %d characters' % (time.time(),len(line))
