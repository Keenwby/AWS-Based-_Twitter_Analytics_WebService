#!/usr/bin/env python
#Filename: Reducer_Q3.py
import sys
#Retweet_from:User:\tId:\tRetweet_by:User:\tId:\n
current_from_user_id = 0
from_user_id = 0
fi = open("f04_Q3_1_2_n",'r')
fo = open("f05_Q3_1_2_n",'w')
for line in fi.readlines():
    line = line.strip()
    [fromid, byid] = line.split('\t',1)
    from_user_id = fromid
    by_user_id = byid
    if current_from_user_id == from_user_id:
	#print ':%s' % (by_user_id),
        fo.write (':%s' % (by_user_id))
    else:
        #The first line is empty
	#print '\n'
        fo.write ('\n')
	#print ('%s\t' % (from_user_id)),
        fo.write ('%s\t' % (from_user_id))
	#print '%s' % (by_user_id),
        fo.write ('%s' % (by_user_id))
    current_from_user_id = from_user_id
fi.close()
fo.close()
