#!/usr/bin/env python
import os
import sys
reload(sys)
#file_path = os.environ["map_input_file"]
sys.setdefaultencoding( "utf-8" )
fo = open("small_02_part00055", 'w')
for t_line in sys.stdin:
    t_line = t_line.strip()
    if(t_line):
        [id, date, text] = t_line.split("\t", 2)
        [year, month, day] = date.split("-", 2)
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
        new_date = year + '-' + month + '-' + day
        print "%s\t%s\t%s" % (id, new_date, text)
        fo.write("%s\t%s\t%s\n" % (id, new_date, text))
fo.close


