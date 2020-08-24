import json

with open('names.json') as f:
    j = json.load(f)
print(j.get('1'))
