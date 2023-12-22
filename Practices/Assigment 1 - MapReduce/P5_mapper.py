#!/usr/bin/python

import sys
import csv

for line in csv.reader(sys.stdin):
    tipo = line[2]
    mass = line[4]
    
    print(tipo + "\t" + mass)
