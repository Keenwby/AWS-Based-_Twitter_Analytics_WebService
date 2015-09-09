#!/usr/bin/env python
import sys
from operator import itemgetter, attrgetter
#Iutput Format:Retweet_from:User:\tId\tRetweet_by:User:\tId:\n
fi = open("f04_Q5",'r')
fo = open("f05_Q5",'w')
List = []
for line in fi.readlines():
    [id, text] = line.split("\t",1)
    List.append((int(id), text))
List_sorted = sorted(List, key=itemgetter(0))
for elem in List_sorted:
    print '%d\t%s' %(elem[0], elem[1])
    fo.write ('%d\t%s' %(elem[0], elem[1]))
fi.close()
fo.close()
