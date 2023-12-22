#!/usr/bin/python

import sys

previous = None
sum = 0
meteoritos = 0

for line in sys.stdin:
    key, value = line.split('\t')
    
    if key != previous:
        if previous is not None:
            print(previous + '\t' + sum/meteoritos)
        previous = key
        sum = 0
        meteoritos = 0
    
    sum = sum + int(value)
    meteoritos += 1

print(previous + '\t' + sum/meteoritos)
