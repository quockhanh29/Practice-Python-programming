with open('sample11_6_1.txt', 'w') as f:
    for i in range(0,11):
        f.write(str(i))
        f.write('\n')

s = 0
with open('sample11_6_1.txt', 'r') as f:
    for j in f:
        s += int(j)
    print(str(s))

import csv
s1 = 0
len1 = 0
with open('sample11_2_1.csv', 'r', newline='') as f:
    reader = csv.reader(f)
    #l1 = len(list(f))
   # print(l1)
    for row in reader:
        s1 +=int(row[1])
        print(s1)
        len1 +=1
    print('%.1f' %(s1/len1))

import xml.etree.ElementTree as et
tree = et.parse('sample11_3.xml')
root = tree.getroot()
l = len(root)
#len2 = 0
s2 = 0
for person in root:
    age = person.find('age').text
    #len2 +=1
    s2 +=int(age)
print('%.1f' %(s2/l))

import json
s3 = 0
len3 = 0
with open('sample11_4_1.json', 'r') as f:
    people = json.load(f)
    for person in people:
        len3 +=1
        s3 += int(person['age'])
    print('%.1f' %(s3/len3))
