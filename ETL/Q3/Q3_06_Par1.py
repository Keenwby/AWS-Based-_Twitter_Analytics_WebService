#!/usr/bin/env python
#Filename: Reducer_Q3.py
import sys
#Retweet_from:User:\tId:\tRetweet_by:User:\tId:\n
current_from_user_id = 0
from_user_id = 0
fi = open("f06_Q3_1_2_n",'r')
fo = open("f07_Q3_1_2_n",'w')
for line in fi.readlines():
    line = line.strip()
    #print '%s/' % (line)
    fo.write ('%s/\n' % (line))
fi.close()
fo.close()
