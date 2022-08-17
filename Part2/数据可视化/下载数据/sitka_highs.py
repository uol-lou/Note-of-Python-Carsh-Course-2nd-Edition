import csv

filename = 'dataexport_20220817T193734.csv'

with open(filename) as f:
    reader = csv.reader(f)
    head_row = next(reader)
    print(head_row)