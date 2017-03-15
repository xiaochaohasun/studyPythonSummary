#!/usr/bin/evn python
# -*- coding: utf8 -*-

import mktxtfile

width = 48

data = mktxtfile.get_content()

print '+%s+' % ('*' * width)
for line in data:
    sp_wid, extra = divmod((width - len(line)), 2)
    print '+%s%s%s+' % (' ' * sp_wid, line, ' ' * (sp_wid + extra))
print '+%s+' % ('*' * width)