import csv
import os
import sys

result=[]
fname = sys.argv[1]

# input
with open(fname, newline='', encoding='cp932') as csvfile:
    content = csv.reader(csvfile, delimiter=',', lineterminator='\r\n',skipinitialspace=True)
    header = True
    for row in content:
        result.append(row)

outname = "output_" + fname

# output
with open(outname, 'w', newline='', encoding='cp932') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', lineterminator='\r\n', quoting=csv.QUOTE_ALL)
    writer.writerows(result)