#！/usr/bin/env python
# -*- coding: utf8 -*-


#变量互换
# a,b =b,a

####查询关键字
# import keyword
# keyword.iskeyword(‘pass’)
# keyword.kwlist

#使用内建函数id()查询对象的身份
# a=10
# id(a)
# a=20
# id(a)
#由于数字类型是不可变，所以重新赋值之后身份不同


#使用内建函数type()查看对象的类型
# a=10
# type(a)

#比较两个数字，第一个数字大返回1，小返回-1，相等返回0
#cmp(10,20)

#int转换，base代表进制，可以为24，自己定义
#int('100',base=2)

#绝对值
#abs(-100)


#divmod可以等到商和余数
#a.b=divmod(10,3)
#a=3,b=1  --result

#2的3次方
#pow(2,3)

#ord函数可以将数字转换为assic码值
#ord('a')  --97
#ord('A')  --65

#chr函数可以将数字转换为assic码值
#chr(100) --d
#chr(66)  --B
