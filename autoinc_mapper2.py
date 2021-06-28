#!/usr/bin/env python
import sys

# tab = '\t'

# Read input from STDIN and output composite keys constructed by vehicle make and year. Value is the count of 1

for row in sys.stdin:

    row = row.split('\t')
    value = row[1].split(",")
    make = value[1].strip().strip("'")
    year = value[2].strip().strip("]").strip("'")
    composite_key = (make, year)
    
    print  '%s\t%s' % (composite_key, 1)
    # print (f"{composite_key}{tab}1")
    # print (str(composite_key) + tab + "1")