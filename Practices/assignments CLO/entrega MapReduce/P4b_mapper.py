#!/usr/bin/python

import sys


for line in sys.stdin:
    data = line.split(" ")
    id=data[0]
    avg=data[1]

    range=0

    if avg<=1: range=1
    elif 1<avg<=2: range=2
    elif 2<avg<=3: range=3
    elif 3<avg<=4: range=4
    elif 4<avg<=5: range=5
    
    print(range + "\t" + id)
