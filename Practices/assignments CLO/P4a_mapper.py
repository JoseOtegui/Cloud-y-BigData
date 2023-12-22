#!/usr/bin/python

import sys
import csv

for line in csv.reader(sys.stdin):
    id=line[1]
    rating=line[2]

    print(id + "\t" + rating)
    
