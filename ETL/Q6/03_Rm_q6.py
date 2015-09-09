#!/usr/bin/env python
import os
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
fi = open("f02_Q6", 'r')
fo = open("f03_Q6", 'w')
current_id = 0
id = 0
for line in fi.readlines():
    [user, num, id] = line.split('\t',2)
    id = int(id)
    if current_id == id:
        continue
    else:
        print '%s\t%s' % (user, num)
        fo.write ('%s\t%s\n' % (user, num))
    current_id = id
fi.close()
fo.close()