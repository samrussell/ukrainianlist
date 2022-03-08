from collections import defaultdict
import json

with open("wfl-uk.txt") as file:
    data = file.read()

lines = data.split("\n")[:-1]
entries = [line.split("\t") for line in lines]

lookup = defaultdict(lambda: [])


for entry in entries:
    lemma = entry[0]
    #for i in range(len(lemma)):
    i = 0
    char = lemma[i:i+1]
    double = lemma[i:i+2]
    triple = lemma[i:i+3]
    quad = lemma[i:i+4]
    five = lemma[i:i+5]
    lookup[char].append(entry)
    if len(double) == 2:
        lookup[double].append(entry)
    if len(triple) == 3:
        lookup[triple].append(entry)
    if len(quad) == 4:
        lookup[quad].append(entry)
    if len(five) == 5:
        lookup[five].append(entry)

with open("lookup.json", "wb") as file:
    output = json.dumps(lookup, ensure_ascii=False).encode('utf8')
    file.write(output)

print("done")
