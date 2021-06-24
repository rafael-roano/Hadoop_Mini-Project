import sys

tab = '\t'
freq = {}


for row in sys.stdin:
    row = row.strip().split(tab)
       
    composite_key = row[0]
    # print(composite_key)
        
    if composite_key in freq.keys():
        freq[composite_key] += 1
    else:
        freq[composite_key] = 1

for (composite_key, count) in freq.items():
   
    print (f"{composite_key}{tab}{count}")