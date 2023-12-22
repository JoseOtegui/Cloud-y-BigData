#!/usr/bin/python

import sys
import re
import csv

for line in csv.reader(sys.stdin):
    date=line[0]
    close=line[4]

    partes=words = re.sub(r'\W+', '-', date).split() #ver si esto lo divide en año mes y dia
    year=partes[0]
    
    print(year + "\t" + close)
    
