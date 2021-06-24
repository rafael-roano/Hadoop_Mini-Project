import sys

tab = '\t'

# [Define group level master information]

processed_vin = None
accident_counter = 0
master_make = None
master_year = None


def reset():
    # [Logic to reset master info for every new group]
    global processed_vin, accident_counter, master_make, master_year
    
    processed_vin = None
    accident_counter = 0
    master_make = None
    master_year = None
    


# Run for end of every group

def flush(processed_vin, accident_counter, master_make, master_year):

    for i in range(accident_counter):
        key = processed_vin
        value = ["A", master_make, master_year]
        print (f"{key}{tab}{value}")


for row in sys.stdin:

    row = row.split(tab)
    vin = row[0]

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

flush(processed_vin, accident_counter, master_make, master_year) 