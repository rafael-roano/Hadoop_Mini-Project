#!/usr/bin/env python
import sys

# tab = '\t'
freq = {}

# Read input from STDIN and count the individual values by key. Output key as the combination of make and year, and count as value.

for row in sys.stdin:
    row = row.strip().split('\t')
       
    composite_key = row[0]
    # print(composite_key)
        
    if composite_key in freq.keys():
        freq[composite_key] += 1
    else:
        freq[composite_key] = 1

for (composite_key, count) in freq.items():
   
    # print (f"{composite_key}{tab}{count}")
    # print(composite_key + tab + str(count))
    print  '%s\t%s' % (composite_key, count)