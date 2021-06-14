import csv

with open('sample11_2_1.csv', 'w', newline ='') as f:
    writer = csv.writer(f)
    writer.writerow(['alice', 23, 'F'])
    writer.writerow(['bob', 31, 'M'])
    writer.writerow(['charlie', 26, 'M'])

