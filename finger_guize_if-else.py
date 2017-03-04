#!/usr/bin/env python
# -*- coding:utf8 -*-
import sys
import random

random_list=['剪刀','石头','布']

print '退出请输入:exit'
while(True):
	rand=random.choice(random_list)
	user_input=raw_input("输入您的猜拳:")

	if(user_input=="exit"):
		sys.exit()

	if not user_input in random_list:
		print '请输入剪刀、石头、布！'
		continue

	if(user_input=="剪刀"):
		if(rand=="剪刀"):
			print '计算机也出剪刀，打平了！'
		elif(rand=="石头"):
			print '计算机出石头，你输了！'
		else:
			print '计算机出布，你赢了！'
	if(user_input=="石头"):
		if(rand=="剪刀"):
			print '计算机出剪刀，你赢了！'
		elif(rand=="石头"):
			print '计算机也出石头，打平了！'
		else:
			print '计算机出布，你输了！'
	if(user_input=="布"):
		if(rand=="剪刀"):
			print '计算机出剪刀，你输了！'
		elif(rand=="石头"):
			print '计算机出石头，你赢了！'
		else:
			print '计算机也出布，打平了！'
