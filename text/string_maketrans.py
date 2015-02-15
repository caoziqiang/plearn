#!/usr/bin/python
import string

s = 'the quick brown fox jumped over the lazy dog'
print s
leet = string.maketrans('abcdefg','1234567')
print s.translate(leet)
