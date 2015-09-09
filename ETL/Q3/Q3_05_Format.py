#!/usr/bin/env python
#Filename: Reducer_Q3.py
import sys
#Retweet_from:User:\tId:\tRetweet_by:User:\tId:\n
fi = open("f05_Q3_1_2_n",'r')
fo = open("f06_Q3_1_2_n",'w')
i = 0
for line in fi.readlines():
    i += 1
    if i == 1:
        continue
    else:
        #line[-2:-1] = ''
	#print '%s' % (line)
        fo.write ('%s' % (line))
fi.close()
fo.close()
