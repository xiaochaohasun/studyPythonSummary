for ch in 'abcd':
    print ch

for i in [1, 2, 3]:
    print i

for word in ("hello", "world"):
    print word

adict = {'name': 'bob', 'age': 21}
for key in adict:
    print key, adict[key]


py_str='hello world!'

for i in range(len(py_str)):
    print i,py_str[i]



#表达式生成列表 单数平方
# example 1 : [i ** 2 for i in range(1.11) if i % 2 ==1 ]
# result:[1, 9, 25, 49, 81]

#生成ip地址列表
# example 2 : ['192.168.1.' + str(i) for i in range(1,11)]

# result:['192.168.1.1', '192.168.1.2', '192.168.1.3', '192.168.1.4', '192.168.1.5',
#  '192.168.1.6', '192.168.1.7', '192.168.1.8', '192.168.1.9', '192.168.1.10']
