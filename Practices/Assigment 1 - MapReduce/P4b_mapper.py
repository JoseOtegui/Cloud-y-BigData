#!/usr/bin/python

import sys
import csv

for line in csv.reader(sys.stdin):
    id=line[1]
    rating=line[2]

    range=0

    if rating<=1: range=1
    elif 1<rating<=2: range=2
    elif 2<rating<=3: range=3
    elif 3<rating<=4: range=4
    elif 4<rating<=5: range=5
    
    print(range + "\t" + id)
