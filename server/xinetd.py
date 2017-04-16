#!/usr/bin/env python

import sys

print 'Welcome.'
print 'Please enter a string:'
sys.stdout.flush()
line=sys.stdin.readline().strip()
print 'you enterd %d characters' % len(line)