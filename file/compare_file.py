#!/usr/local/env python
# -*- coding: utf8 -*-

src_file='/etc/passwd'
dst_file='/tmp/mima'

src_fobj=open(src_file)
dst_fobj=open(dst_file)
result_fobj=open('/tmp/result.txt','w')

src_set=set(src_fobj)
dst_set=set(dst_fobj)


result=dst_set - src_set

result_fobj.writelines(result)

src_fobj.close()
dst_fobj.close()
result_fobj.close()