#!/usr/bin/env python
import sys
from operator import itemgetter, attrgetter
#Iutput Format:Retweet_from:User:\tId\tRetweet_by:User:\tId:\n
#fi = open("f01_Q5",'r')
#fo = open("f02_Q5",'w')
file_path = os.environ["map_input_file"]
List = []
for line in sys.stdin:
    [id, user, retweet_id] = line.split("\t",2)
    List.append((int(user), int(id), int(retweet_id)))
List_sorted = sorted(List, key=itemgetter(0,1))
for elem in List_sorted:
    print '%d\t%d\t%d' %(elem[0], elem[1], elem[2])
    fo.write ('%d\t%d\t%d\n' %(elem[0], elem[1], elem[2]))
#fi.close()
#fo.close()
