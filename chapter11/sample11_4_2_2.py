import json

people = [
    {'name': 'avid', 'age':17, 'sex': 'M'},
    {'name': 'ellie', 'age': 28, 'sex':'F'},
]
with open('sample11_4_1.json', 'w') as f:
    json.dump(people, f, indent=2)
