#!/usr/bin/env python3
import sys
import re
import string

if len(sys.argv)<2:
    sys.exit(1)

s=sys.argv[1]

if len(s)<2 or len(s)%2 == 1 or re.search(r'[h-zH-Z]', s):
    sys.exit(1)

values = dict()
for index, letter in enumerate(string.ascii_lowercase[0:7]):
   values[letter] = index

print(''.join(chr(97 + values[s[0]]*7 + values[s[1]]) for s in [op+code for op, code in zip(s[0::2], s[1::2])]))
