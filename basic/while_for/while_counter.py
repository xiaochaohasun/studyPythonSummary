#!/usr/bin/env python
# -*- coding: utf8 -*-

# DRY: Don't Repeat Yourself

# is ok!!
# while True:
#     yn=raw_input('continue:(y/n)')
#     if yn == 'n':
#         break
#     print 'working....'
#
# print 'done!'


result = 0
counter = 0

while counter < 101:
    counter += 1         # counter = counter + 1
    # if counter % 2 ==1:
    if counter % 2:      # counter is 1 or 0
        continue
    result += counter    # result = result + counter

print result
