#!/usr/bin/env python
import sys

# tab = '\t'

# Group level master info definition

processed_vin = None
accident_counter = 0
master_make = None
master_year = None


def reset():
    # Reset master info for every new group

    global processed_vin, accident_counter, master_make, master_year
    
    processed_vin = None
    accident_counter = 0
    master_make = None
    master_year = None
    

def flush(processed_vin, accident_counter, master_make, master_year):
    # Filter and propagate make and year to the accident records. Write output for every group.

    for i in range(accident_counter):
        key = processed_vin
        value = ["A", master_make, master_year]
        print  '%s\t%s' % (key, value)
        # print (f"{key}{tab}{value}")
        # print(key + tab + str(value))
        

# Read input from STDIN, iterate over all sorted key-value pairs and find the make and year required to populate the accident records.

for row in sys.stdin:

    # Parse input and update the master info

    row = row.split('\t')
    vin = row[0]

    # Detect key changes

    if vin != processed_vin:
    
        if processed_vin != None:

            flush(processed_vin, accident_counter, master_make, master_year)       
            processed_vin = None
            accident_counter = 0
            master_make = None
            master_year = None
  
    value = row[1].split(",")
    incident_type = value[0].strip().strip("[").strip("'")
    make = value[1].strip().strip("'")
    year = value[2].strip().strip("]").strip("'")
 
    if incident_type == "A":
        accident_counter += 1
    if make:
        master_make = make
    if year:
        master_year = year

    processed_vin = vin
# Output last group if required.
flush(processed_vin, accident_counter, master_make, master_year) 