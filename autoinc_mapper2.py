import sys

tab = '\t'

# Read input from STDIN and output pair of vin_number and list of inciditent type, make and year.

for row in sys.stdin:

    row = row.split(tab)
    value = row[1].split(",")
    make = value[1].strip().strip("'")
    year = value[2].strip().strip("]").strip("'")
    composite_key = (make, year)
    
    print (f"{composite_key}{tab}1")

    
