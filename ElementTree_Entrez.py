import Bio.Entrez as ez
import xml.etree.ElementTree as ET

ez.email = "mohammed.albughaili@gmail.com"

# with ez.efetch(db="gene", id="92344", retmode="xml") as handle:
#     record2 = ET.parse(handle)

with ez.efetch(db="protein", id="2187428178", retmode="xml") as handle:
    record2 = ET.parse(handle)

record2 = record2.getroot()
print(record2)
print(record2.tag)
print(record2[0].tag)
print(record2[0][0].tag)

for x in record2.findall("GBSeq"):
    print(x.find("GBSeq_definition").text),
    print(x.find("GBSeq_source").text)
    print(x.find("GBSeq_sequence").text)

# for i in range(len(record2[0])):
#     print(record2[0][i].tag)
#     print(record2[0][i].text)
