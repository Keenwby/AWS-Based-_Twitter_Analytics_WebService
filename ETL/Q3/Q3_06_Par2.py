#!/usr/bin/env python
#Filename: Reducer_Q3.py
fi = open("f07_Q3_n",'r')
fo = open("f08_Q3_n",'w')
for line in fi.readlines():
    line = line.strip()
    [userid, content] = line.split('\t',1)
    [byu, tou] = content.split('/',1)
    byid = byu.split(':')
    toid = tou.split(':')
    if tou:
        #print userid + '\t'
        fo.write('%s\t' % (userid))
        for elem in byid:
            if elem in toid:
                elem = '(' + elem + ')'
                #print elem + ':',
                fo.write ('%s:' % (elem))
            else:
                #print elem + ':',
                fo.write ('%s:' % (elem))
        #print '\n'
        fo.write('\n')
    else:
        #print userid + '\t' + byu + ':'
        fo.write('%s\t%s:\n' % (userid, byu))
fi.close()
fo.close()
