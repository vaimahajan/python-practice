#!/usr/bin/python

import re
from collections import Counter

teststring="Wow I cannot believe this. This is me learning regex"

#for counting from file:
#with open('file.txt') as f:
#	passage=f.read()
#words=re.findall(r'\w+',passage)

words=re.findall(r'\w+',teststring)

small_words=[]
for word in words:
	small_words.append(word.lower())

counts=Counter(small_words)

print teststring
print counts
print counts.most_common(1)		#returns list with most top 'n' most common words