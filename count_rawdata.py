import csv
from collections import Counter

data_out = open("2014_beneficial.csv", "rU")
reader = csv.reader(data_out)
next(reader,None)

first_counters = {}
second_counters = {}
third_counters = {}

for rows in reader:
    primary = rows[0], rows[1].strip()
    first_counters.setdefault(primary,0)
    first_counters[primary] += 1
    secondary = rows[0], rows[2].strip()
    second_counters.setdefault(secondary,0)
    second_counters[secondary] += 1
    third = rows[0], rows[3].strip()
    third_counters.setdefault(third,0)
    third_counters[third] += 1

A = Counter(first_counters)
B = Counter(second_counters)
C = Counter(third_counters)


new = A + B + C
print(new)

with open('mycsvfile.csv', 'w') as f:  # Just use 'w' mode in 3.x
    w = csv.writer(f)
    w.writerows(new.items())






