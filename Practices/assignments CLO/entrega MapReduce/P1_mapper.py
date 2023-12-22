#!/usr/bin/python3

import sys
import re
count = 0

for line in sys.stdin:
    if sys.argv[1] in line:
        print(line)
        

    