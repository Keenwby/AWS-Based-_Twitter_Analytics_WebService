#!/usr/bin/env python
#Filename: Reducer_Q3.py
import sys
#Retweet_from:User:\tId:\tRetweet_by:User:\tId:\n
current_from_user_id = None
from_user_id = None
fi = open("f05_Q5",'r')
fo = open("f06_Q5",'w')
for line in fi.readlines():
    line = line.strip()
    [from_user_id, by_user_id] = line.split('\t',1)
    if current_from_user_id == from_user_id:
        #print ':%s' % (by_user_id),
        fo.write (':%s' % (by_user_id))
    else:
        #The first line is empty
        #print '\n'
        fo.write ('\n')
        #print from_user_id + '\t',
        fo.write ('%s\t' % (from_user_id))
        #print '%s' % (by_user_id),
        fo.write ('%s' % (by_user_id))
    current_from_user_id = from_user_id
fi.close()
fo.close()
