#!/usr/bin/env python
# -*- coding: utf8 -*-


import random

result = random.randint(1, 100)  # 随机产生1-100之间的数字，包含1，100
counter = 0

while counter < 5:
    answer = int(raw_input('please input you guize number:'))

    if answer == result:
        print 'You guize is right.congratulations!!!'
        break
    elif answer > result:
        print 'You guize number is too big!!!'
    else:
        print 'You guize number is too small!!!'

    counter += 1
else:
    print 'answer is:', result
