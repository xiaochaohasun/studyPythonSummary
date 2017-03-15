#!/usr/bin/env python

import sys
import time

width=20
count=0

sys.stdout.write('#' * width)

while True:
    sys.stdout.write(
        '\r%s@%s' % (('#' * count),('#' * (width-count-1)))
    )

    sys.stdout.flush()
    count += 1
    if count == width:
        count =0

    time.sleep(0.2)
