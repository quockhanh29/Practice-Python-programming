import csv

with open ('sample11_2_2.csv', 'w', newline='') as f:
    cout = csv.DictWriter(f, ['name', 'age', 'sex'])
    cout.writeheader()
    cout.writerow({'name': 'alice', 'age': 23, 'sex': 'F'})
    cout.writerow({'name':'bob', 'age': 31, 'sex': 'M'})
    cout.writerow({'name':'charlie', 'age':26, 'sex':'M'})
