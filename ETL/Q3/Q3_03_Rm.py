#!/usr/bin/env python
import os
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
#fi = open("f03_Q3", 'r')
fo = open("f04_Q3", 'w')
current_text = None
text = None
for line in sys.stdin:
    text = line.strip()
    if current_text == text:
        continue
    else:
        print text
        fo.write ('%s\n' % (text))
    current_text = text
#fi.close()
fo.close()