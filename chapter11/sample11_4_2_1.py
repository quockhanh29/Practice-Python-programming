import json

with open('sample11_4_1.json', 'r') as f:
    people = json.load(f)
    for person in people:
        print (person)
