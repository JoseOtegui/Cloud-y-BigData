#!/usr/bin/python

import sys

previous = None
sum = 0
dias = 0

for line in sys.stdin:
    key, value = line.split('\t')
    
    if key != previous:
        if previous is not None:
            print(previous + '\t' + str(sum/dias))
        previous = key
        sum = 0
        dias = 0
    
    sum = sum + int(value)
    dias += 1

print(previous + '\t' + str(sum/dias))
