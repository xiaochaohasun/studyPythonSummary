#!/usr/bin/env python
# -*- coding: utf-8 -*-

import readline
import rlcompleter

readline.parse_and_bind('tab: complete')

#1.查看python  sys.path
#python
#>>>import sys
#>>>sys.path

#2.编辑tab.py后放入sys.path任意一个变量中

#3.加入全局变量
#vim /etc/profile
#export PATHSTATRTUP=/path/tab.py
