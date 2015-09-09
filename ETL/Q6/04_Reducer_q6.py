#!/usr/bin/env python
#from operator import itemgetter
import sys
fo = open("f04_Q6",'w')
current_word = None
current_count = 0
word = None
#input comes from standard input
for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)
    try:
        count = int(count)
    except ValueError:
            continue
#The sorting part has been done
#So we can just process the current_word with the previous one
    if current_word == word:
        current_count += count
        #Another new word comes
    else:
        if current_word:
            print '%s\t%s' % (current_word, current_count)
            fo.write ('%s\t%s\n' % (current_word, current_count))
        current_word = word
        current_count = count
#Output the last word if needed
if current_word == word:
    print '%s\t%s' % (current_word, current_count)
    fo.write ('%s\t%s\n' % (current_word, current_count))
fo.close()
