#!/usr/bin/env python
import os
import sys
reload(sys)
file_path = os.environ["map_input_file"]

sys.setdefaultencoding( "utf-8" )
import json


for t_line in sys.stdin:
    t_line = t_line.strip()
    if(t_line):
        d_line = json.loads(t_line)
        [week, month, day, time, zero, year] = d_line["created_at"].split(" ", 5)
        if month == 'Jan':
            month = '01'
        if month == 'Feb':
            month = '02'
        if month == 'Apr':
            month = '04'
        if month == 'May':
            month = '05'
        if month == 'June':
            month = '06'
        if month == 'July':
            month = '07'
        if month == 'Aug':
            month = '08'
        if month == 'Sept':
            month = '09'
        if month == 'Oct':
            month = '10'
        if month == 'Nov':
            month = '11'
        if month == 'Dec':
            month = '12'
        if month == 'Mar':
            month = '03'
        new_date = year + '-' + month + '-' + day + '+' + time


        text = d_line["text"]
        text = text.replace('\n','\\n')
        text = text.replace('\r','\\r')
        print "%s\t%s\t%s\t%s\t" % (d_line["user"]["id_str"], new_date, d_line["id_str"], text)
        


