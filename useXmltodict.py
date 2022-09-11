import xmltodict

with open('Experiments.xml') as fd:
    doc = xmltodict.parse(fd.read())

print(doc)
print("")
print(doc["experiments"])
print("")
print(doc["experiments"]["experiment"])
print("")
print(doc["experiments"]["experiment"]["name"])
print("")
print(doc["experiments"]["experiment"]["name"][0]["title"])
