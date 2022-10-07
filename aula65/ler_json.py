import json

with open('abc.json', 'r') as arquivo:
    print(json.loads(arquivo.read()))