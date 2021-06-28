#!/usr/bin/env python
import sys
# from csv import reader

# tab = '\t'

# Read input from STDIN and output pair of vin_number and list of inciditent type, make and year.

for row in sys.stdin:
    
    row = row.split(",")
    key = row[2]
    value = [row[1], row[3], row[5]]
    print  '%s\t%s' % (key, value)
    
    # print (f"{key}{tab}{value}")
    # print(key + tab + str(value))
    

# Code to test functionality reading the csv file directly.
# with open('/home/jv/Python/SB/SB_Projects/Hadoop_Mini-Project/data.csv', 'r') as f:
    
#     read = reader(f)
#     post_sales = list(read)

# for row in post_sales:
        
#     key = row[2]
#     value = [row[1], row[3], row[5]]
#     tab = '\t'    
#     print (f"{key}{tab}{value}")