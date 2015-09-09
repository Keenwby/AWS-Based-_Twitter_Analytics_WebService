#!/usr/bin/env python
import os
import sys
reload(sys)
file_path = os.environ["map_input_file"]

sys.setdefaultencoding( "utf-8" )
import re
import time
import urllib2
rule = re.compile('[^\W_]+')
word = []
num = []
ban = []
blacklist = []
#store the sentiment words
while True:
    try:
        get = urllib2.urlopen('https://s3.amazonaws.com/F14CloudTwitterData/AFINN.txt').readlines()
        break
    except:
        time.sleep(1)
        continue
for line_1 in get:
    [w,n] = line_1.split("\t", 1)
    word.append(w)
    num.append(n)
#store the banned words
while True:
    try:
        get = urllib2.urlopen('https://s3.amazonaws.com/F14CloudTwitterData/banned.txt').readlines()
        break
    except:
        time.sleep(1)
        continue
for line_2 in get:
    b = line_2.split("\n",1)
    ban.append(b)
for j in range(0, len(ban)):
    blacklist.append(str(ban[j][0].decode('rot13')))
#The cleaning function
def replace(match):
    word = match.group()
    if word.lower() in blacklist:
        return word[0] + '*' * (len(word)-2) + word[-1]
    else:
        return word
for line in sys.stdin:
    count = 0
    line = line.strip()
    #print line
    user, date, id, text = line.split("\t", 3)
    #sentiment analysis
    t_word = rule.findall(text.lower())
    for t_elem in t_word:
        for j in range(0, len(word)):
            if t_elem == word[j]:
                count += int(num[j])
    #Clean the words in blacklist
    text = re.sub(r'\b\w*\b', replace, text)
    print "%s\t%s\t%s:%s:%s" % (user, date, id, count, text)
