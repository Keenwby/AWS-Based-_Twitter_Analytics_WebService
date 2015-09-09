#!/usr/bin/env python
import os
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import json
#fi = open("15619f14twitter-parta-aa", 'r')
#fo = open("f01_Q3database", 'w')
file_path = os.environ["map_input_file"]
for t_line in sys.stdin:
    t_line = t_line.strip()
    if t_line:
        d_line = json.loads(t_line)
        if str(d_line).find("retweeted_status") != -1:
            user_id = d_line["user"]["id_str"]
            retweet_user_id = d_line["retweeted_status"]["user"]["id"]
            print "%s\t%s" % (retweet_user_id, user_id)
            #Output Format:Retweet_from:\tRetweet_by:\n
            fo.write ('%s\t%s\n' % (retweet_user_id, user_id))
#fi.close()
fo.close()
