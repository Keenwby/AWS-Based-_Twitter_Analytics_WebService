#!/usr/bin/env python
import os
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
fi = open("Q3_B", 'r')
fo = open("Q3_C", 'w')
current_text = None
text = None
for line in fi.readlines():
    [text,e] = line.split('\n',1)
    if current_text == text:
        continue
    else:
        print text
        fo.write ('%s\n' % (text))
    current_text = text
fi.close()
fo.close()