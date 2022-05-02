import csv
import sys


file_to_read = sys.argv[1]

with open(file_to_read, newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)




