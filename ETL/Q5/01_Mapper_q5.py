#!/usr/bin/env python
import os
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import json
#fi = open("15619f14twitter-parta-aa", 'r')
#fo = open("f01_Q5", 'w')
file_path = os.environ["map_input_file"]
for t_line in sys.stdin:
    t_line = t_line.strip()
    if t_line:
        d_line = json.loads(t_line)
        user = d_line["user"]["id_str"]
        id = int(d_line["id_str"])
        if 'retweeted_status' in d_line:
            retweet_user_id = d_line["retweeted_status"]["user"]["id"]
            print '%d\t%s\t%s' % (id, user, retweet_user_id)
        #fo.write('%s\t%s\t%s\n' % (id, user, retweet_user_id))
        else:
            retweet_user_id = '0'
            print '%d\t%s\t%s' % (id, user, retweet_user_id)
    #   fo.write('%s\t%s\t%s\n' % (id, user, retweet_user_id))
#fi.close()
#fo.close()