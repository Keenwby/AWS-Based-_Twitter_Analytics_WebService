#!/usr/bin/env python
import os
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import json
#fi = open("15619f14twitter-parta-aa", 'r')
fo = open("f02_Q3", 'w')
#file_path = os.environ["map_input_file"]
for t_line in sys.stdin:
    t_line = t_line.strip()
    if t_line:
        [by_user, from_user] = t_line.split("\t", 1)
        print "%s\t%s" % (from_user, by_user)
        #Output Format:Retweet_from:\tRetweet_by:\n
        fo.write ('%s\t%s\n' % (from_user, by_user))
#fi.close()
fo.close()
