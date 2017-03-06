#!/usr/bin/python

from difflib import SequenceMatcher

str1="hello world"
str2="world"

match=SequenceMatcher(None,str1,str2).find_longest_match(0,len(str1),0,len(str2))

#print match
# match object is of type difflib.Match - with a,b and size properties

print str1[match.a:match.a+match.size]