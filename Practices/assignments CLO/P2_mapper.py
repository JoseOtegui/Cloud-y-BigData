#!/usr/bin/python

import sys
import re

for line in sys.stdin:
    words = re.sub(r'\W+', ' ', line).split()
    
    print(words[0] + "\t1")
