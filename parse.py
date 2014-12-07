#!/usr/bin/python

import sys

f = open('names-last-raw.csv','r')
for line in f:
    fields = line.split('\t')
    if (len(fields) == 11):
        name = fields[0].capitalize()
        count = fields[2].replace(',','')
        sys.stdout.write(name + ',' + count + '\n')
