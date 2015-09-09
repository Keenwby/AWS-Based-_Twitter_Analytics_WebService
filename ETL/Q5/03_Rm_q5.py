#!/usr/bin/env python
import os
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
#fi = open("f02_Q5", 'r')
#fo = open("f03_Q5", 'w')
current_id = 0
id = 0
for line in sys.stdin:
    line = line.strip()
    [id, user, text] = line.split('\t',2)
    id = int(id)
    if current_id == id:
        continue
    else:
        print '%s\t%s' % (user, text)
        #fo.write ('%s\t%s' % (user, text))
    current_id = id
#fi.close()
#fo.close()