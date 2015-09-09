#!/usr/bin/env python
import sys
from operator import itemgetter, attrgetter
#Iutput Format:Retweet_from:User:\tId\tRetweet_by:User:\tId:\n
fi = open("f01_Q6",'r')
fo = open("f02_Q6",'w')
List = []
for line in fi.readlines():
    [user, id] = line.split("\t",1)
    List.append((int(user), int(id)))
List_sorted = sorted(List, key=itemgetter(0,1))
for elem in List_sorted:
    print '%d\t1\t%d' %(elem[0], elem[1])
    fo.write ('%d\t1\t%d\n' %(elem[0], elem[1]))
fi.close()
fo.close()
