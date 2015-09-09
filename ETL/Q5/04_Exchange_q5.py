#!/usr/bin/env python
import os
import sys
#fi = open("xaa", 'r')
fo = open("f04_xaf", 'w')
for line in sys.stdin:
    line = line.strip()
    [id, fromu, byu] = line.split('\t',2)
    if byu == '0':
        #print '%s\t%s' % (fromu, byu)
        fo.write ('%s\t%s\n' % (fromu, byu))
    else:
        #print '%s\t%s' % (byu,fromu)
        fo.write ('%s\t%s\n' % (byu,fromu))
fo.close()
