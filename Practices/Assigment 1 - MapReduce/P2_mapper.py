#!/usr/bin/python

import sys
import re

for line in sys.stdin:
    regex = ('(?:(GET|POST) )(\S+)')              # Stores the regex
    url = re.findall(regex, line)[0][1]           # Uses the findall method and stores it in url variable

    print(url + "\t1")
