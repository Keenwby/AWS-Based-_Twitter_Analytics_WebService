#!/usr/bin/env python
import os
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
fo = open("Q4_D", 'w')
for t_line in sys.stdin:
    t_line = t_line.strip()
    if(t_line):
        [year, month, day] = t_line.split("-", 2)
        if month == 'Jan':
            month = '01'
        if month == 'Feb':
            month = '02'
        if month == 'Apr':
            month = '04'
        if month == 'May':
            month = '05'
        if month == 'Jun':
            month = '06'
        if month == 'Jul':
            month = '07'
        if month == 'Aug':
            month = '08'
        if month == 'Sep':
            month = '09'
        if month == 'Oct':
            month = '10'
        if month == 'Nov':
            month = '11'
        if month == 'Dec':
            month = '12'
        if month == 'Mar':
            month = '03'
        print "%s-%s-%s" % (year, month, day)
        fo.write("%s-%s-%s\n" % (year, month, day))
fo.close
