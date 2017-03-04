#!/usr/bin/env python
# -*- coding:utf8 -*-

import sys
import random

choice_list = ['石头', '剪刀', '布']
guize_list = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]
prompt="""(0)石头
(1)剪刀
(2)布
(3)exit
please input your choice(0/1/2/3):"""


while (True):
    print '\033[34;1m########################\033[0m'      #30-40表示字体颜色，40以上表示背景颜色
    user = int(raw_input(prompt))
    rand = random.choice(choice_list)
    if (user == 3):
        sys.exit()
    if (user < 0 or user > 3):
        print '\033[31;1m请按照选择输入，其他均无效！\033[0m'
        continue
    print "Computer's choice %s,Your choice %s!" % (choice_list[user],rand)
    if (choice_list[user] == rand):
        print "\033[32;1m打平了！！！\033[0m"
    elif [choice_list[user], rand] in guize_list:
        print '\033[35;1mYour WIN!!!\033[0m'
    else:
        print "\033[36;1mYour LOSE!!!\033[0m"
