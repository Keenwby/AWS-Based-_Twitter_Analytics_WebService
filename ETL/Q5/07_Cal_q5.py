#!/usr/bin/env python
#Filename: Reducer_Q3.py
import sys
from operator import itemgetter, attrgetter
#Retweet_from:User:\tId:\tRetweet_by:User:\tId:\n
fi = open("f06_Q5",'r')
fo = open("f07_Q5",'w')
i = 0
for line in fi.readlines():
    count = 0
    count1 = 0
    count2 = 0
    count3 = 0
    i += 1
    if i == 1:
        continue
    else:
        line = line.strip()
        [user_id, content] = line.split('\t',1)
        retweet_id= content.split(':')
        retweet_id = sorted(retweet_id)
        #print retweet_id
        current_elem = None
        for elem in retweet_id:
            if len(elem) != 0:
                if elem == '0':
                    count1 += 1
                else:
                    count2 += 3
                    if elem == current_elem:
                        continue
                    else:
                        count3 += 10
                    current_elem = elem
        count = count1 + count2 + count3
        #print '%s\t%d\t%d\t%d\t%d' % (user_id, count1, count2, count3, count)
        fo.write ('%s\t%d\t%d\t%d\t%d\n' % (user_id, count1, count2, count3, count))
fi.close()
fo.close()
