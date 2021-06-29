#!/usr/bin/env python
import sys
from csv import reader

# Read input from STDIN and output pair of vin_number and list of inciditent type, make and year.

for row in sys.stdin:
    
    row = row.strip().split(",")
    key = row[1]
    value = row[2]
    print  '%s\t%s' % (key, value)

# Code to test functionality reading the csv file directly.
# with open('/home/jv/Python/SB/SB_Projects/Hadoop_Mini-Project/input_test.csv', 'r') as f:
    
#     read = reader(f)
#     post_sales = list(read)

# for row in post_sales:
        
#     key = row[1]
#     value = row[2]
#     print  '%s\t%s' % (key, value)