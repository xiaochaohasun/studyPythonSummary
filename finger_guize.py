#!/usr/bin/env python
# -*- coding:utf8 -*-

import sys
import random

random_list=['石头','剪刀','布']
guize_list=[['石头','剪刀'],['剪刀','布'],['布','石头']]

print ''
print '#######输入exit退出！##########'
print ''

while(True):
	user=raw_input('请输入您的猜拳(石头/剪刀/布):')
	rand=random.choice(random_list)
	if(user=='exit'):
		sys.exit()
	if not user in random_list:
		print '请输入石头、剪刀、布，其他均无效！'	
		continue
	if(user==rand):
		print '计算机出%s,打平了!' % rand
	elif[user,rand] in guize_list:
		print '计算机出%s,你赢了！' % rand
	else:
		print "计算机出%s,你输了！" % rand	

