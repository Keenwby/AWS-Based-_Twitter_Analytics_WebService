#!/usr/bin/env python
#Filename: Reducer_Q3.py
import sys
#Retweet_from:User:\tId:\tRetweet_by:User:\tId:\n
current_place = None
place = None
current_date = None
date = None
rank = 0
fi = open("Q4_G",'r')
fo = open("Q4_H",'w')
for line in fi.readlines():
    line = line.strip()
    [date, place, text, index, id, count] = line.split('\t',5)
    id = id.replace(':', ',')
    if current_place == place and current_date == date:
        rank += 1
        fo.write ('%s\t%s\t%s:%s\t%d\n ' % (date, place, text, id, rank))
    else:
        rank  = 1
        fo.write ('%s\t%s\t%s:%s\t%d\n ' % (date, place, text, id, rank))
        current_place = place
        current_date = date
fi.close()
fo.close()
