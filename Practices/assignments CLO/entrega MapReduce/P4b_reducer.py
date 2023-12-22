#!/usr/bin/python

import sys

previous = None

for line in sys.stdin:
    key, value = line.split('\t')
    
    if key != previous:
        if previous is not None:
            print(previous + '\t' + value, end=",\t")
        previous = key
    else:
        print(value, end=",\t")

print(previous + '\t' + value)
