#!/usr/bin/env python
import os
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import json
#fi = open("15619f14twitter-parta-aa", 'r')
#fo = open("f01_Q6", 'w')
file_path = os.environ["map_input_file"]
for t_line in sys.stdin:
    t_line = t_line.strip()
    if t_line:
        d_line = json.loads(t_line)
        user = d_line["user"]["id_str"]
        id = d_line["id_str"]
        if 'media' in d_line["entities"]:
            media = d_line["entities"]["media"]
            for type in media:
                if type["type"] == 'photo':
                    print '%s\t%s' % (user, id)
                    #fo.write ('%s\t%s\n' % (user, id))
#fi.close()
#fo.close()