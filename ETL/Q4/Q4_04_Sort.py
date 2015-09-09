#!/usr/bin/env python
import sys
from operator import itemgetter, attrgetter
#Iutput Format:Retweet_from:User:\tId\tRetweet_by:User:\tId:\n
fi = open("Q4_D",'r')
fo = open("Q4_E",'w')
List = []
for line in fi.readlines():
    [date, location, text, index, id] = line.split("\t", 4)
    List.append((date, location, text, index, id))
List_sorted = sorted(List, key=itemgetter(0,1,2,4))
for elem in List_sorted:
    fo.write ('%s\t%s\t%s\t%s\t%s' %(elem[0], elem[1], elem[2], elem[3], elem[4]))
fi.close()
fo.close()
