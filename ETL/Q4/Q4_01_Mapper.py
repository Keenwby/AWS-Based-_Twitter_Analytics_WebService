#!/usr/bin/env python
import os
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import json
import re
rule = re.compile(r'\btime\b')
#fi = open("15619f14twitter-parta-aa", 'r')
fo = open("Q4database", 'w')
#file_path = os.environ["map_input_file"]
current_text = None
text = None
for t_line in sys.stdin:
    t_line = t_line.strip()
    if t_line:
        d_line = json.loads(t_line)
        hashtags = d_line["entities"]["hashtags"]
        if hashtags:
        #find the place_name
            place = d_line["place"]
            if place and place["name"]:
                place_name = place["name"]
            else:
                time_zone = d_line["user"]["time_zone"]
                if time_zone :
                    match = rule.search(time_zone.lower())
                    if not match:
                        place_name = time_zone
                    else:
                        continue
                else:
                    continue
        #reformat the time
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
            new_date = year + '-' + month + '-' + day
            #remove repeated text
            for content in hashtags:
                text = content["text"]
                index = str(content["indices"][0])
                if current_text == text:
                    continue
                else:
                    print '%s\t%s\t%s\t%s\t%s' % (new_date, place_name, text, index, d_line["id_str"])
                    fo.write ('%s\t%s\t%s\t%s\t%s\n' % (new_date, place_name, text, index, d_line["id_str"]))
                current_text = text
#fi.close()
fo.close()